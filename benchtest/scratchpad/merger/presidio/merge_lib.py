"""Helpers for the presidio P6 merge: line-level edits on column drafts and cell-level edits on the inventory.
Every edit is logged (location, before, after, reason) so presidio_changes.md can be generated from the log."""
import re

LOG = []          # dicts: file, loc, kind, before, after, reason
COUNTS = {}


def _log(file, loc, kind, before, after, reason):
    LOG.append(dict(file=file, loc=loc, kind=kind, before=before, after=after, reason=reason))
    COUNTS[kind] = COUNTS.get(kind, 0) + 1


class Cols:
    """Column drafts: dict id -> {'heading': str, 'lines': [..]} in file order."""

    def __init__(self, paths):
        self.cols = {}
        self.order = []
        self.reviewer_notes = {}
        for p in paths:
            cur = None
            notes = None
            for ln in open(p, encoding="utf-8").read().splitlines():
                if ln.startswith("## Column"):
                    m = re.match(r"^## Column ([A-Z]+\d+):", ln)
                    cur = m.group(1)
                    self.cols[cur] = {"heading": ln, "lines": []}
                    self.order.append(cur)
                    notes = None
                elif ln.startswith("## Reviewer notes"):
                    cur = None
                    notes = []
                    self.reviewer_notes[p] = notes
                elif cur is not None:
                    self.cols[cur]["lines"].append(ln)
                elif notes is not None:
                    notes.append(ln)
        for c in self.cols.values():
            while c["lines"] and not c["lines"][-1].strip():
                c["lines"].pop()

    def row(self, col, n):
        L = self.cols[col]["lines"]
        s = None
        for i, ln in enumerate(L):
            if re.match(r"^### R%d\s*$" % n, ln):
                s = i
            elif s is not None and re.match(r"^### R\d\s*$", ln):
                return s, i
        if s is None:
            raise KeyError((col, n))
        return s, len(L)

    def find(self, col, n, anchor):
        L = self.cols[col]["lines"]
        s, e = self.row(col, n)
        hits = [i for i in range(s, e) if anchor in L[i]]
        if len(hits) != 1:
            raise AssertionError("%s R%d anchor %r matched %d lines: %s" % (col, n, anchor, len(hits), [L[i][:70] for i in hits]))
        return hits[0]

    # ---- edits ----
    def summary(self, col, n, new, reason):
        i = self.find(col, n, "Summary: ")
        L = self.cols[col]["lines"]
        old = L[i]
        assert old.startswith("Summary: ")
        L[i] = new
        _log("cols", "%s R%d Summary" % (col, n), "summary", old, new, reason)

    def summary_text(self, col, n, old, new, reason):
        i = self.find(col, n, "Summary: ")
        L = self.cols[col]["lines"]
        assert L[i].count(old) == 1, (col, n, old)
        before = L[i]
        L[i] = L[i].replace(old, new)
        _log("cols", "%s R%d Summary" % (col, n), "summary", before, L[i], reason)

    def sub(self, col, n, anchor, old, new, reason, kind="edit"):
        i = self.find(col, n, anchor)
        L = self.cols[col]["lines"]
        assert L[i].count(old) == 1, (col, n, anchor, old, L[i][:100])
        before = L[i]
        L[i] = L[i].replace(old, new)
        _log("cols", "%s R%d" % (col, n), kind, before, L[i], reason)

    def repl(self, col, n, anchor, newlines, reason, kind="replace"):
        """Replace the one line holding anchor with one or more new lines."""
        i = self.find(col, n, anchor)
        L = self.cols[col]["lines"]
        before = L[i]
        if isinstance(newlines, str):
            newlines = [newlines]
        L[i:i + 1] = newlines
        _log("cols", "%s R%d" % (col, n), kind, before, "\n".join(newlines), reason)

    def ins_after(self, col, n, anchor, newlines, reason):
        i = self.find(col, n, anchor)
        L = self.cols[col]["lines"]
        if isinstance(newlines, str):
            newlines = [newlines]
        L[i + 1:i + 1] = newlines
        _log("cols", "%s R%d" % (col, n), "add", "(anchor: %s)" % L[i][:90], "\n".join(newlines), reason)

    def ins_before(self, col, n, anchor, newlines, reason):
        i = self.find(col, n, anchor)
        L = self.cols[col]["lines"]
        if isinstance(newlines, str):
            newlines = [newlines]
        before = L[i]
        L[i:i] = newlines
        _log("cols", "%s R%d" % (col, n), "add", "(none; inserted before: %s)" % before[:90], "\n".join(newlines), reason)

    def delete(self, col, n, anchor, reason):
        i = self.find(col, n, anchor)
        L = self.cols[col]["lines"]
        before = L.pop(i)
        _log("cols", "%s R%d" % (col, n), "delete", before, "(deleted)", reason)

    def add_url(self, col, url, reason):
        s, e = self.row(col, 9)
        L = self.cols[col]["lines"]
        assert not any(l.strip() == "• " + url for l in L[s:e]), (col, url)
        L.insert(e, "• " + url)
        _log("cols", "%s R9" % col, "url", "(none)", "• " + url, reason)

    def render(self, ids):
        out = []
        for cid in ids:
            c = self.cols[cid]
            out.append(c["heading"])
            out.extend(c["lines"])
            out.append("")
        return "\n".join(out).rstrip("\n") + "\n"


class Inv:
    def __init__(self, path):
        self.lines = open(path, encoding="utf-8").read().splitlines()
        self.reviewer_notes = []
        k = next(i for i, l in enumerate(self.lines) if l.startswith("## Reviewer notes"))
        self.reviewer_notes = self.lines[k + 1:]
        self.lines = self.lines[:k]
        while self.lines and not self.lines[-1].strip():
            self.lines.pop()

    def block_range(self, blk):
        s = next(i for i, l in enumerate(self.lines) if l.startswith("## (%s)" % blk))
        e = next((i for i in range(s + 1, len(self.lines)) if self.lines[i].startswith("## ")), len(self.lines))
        return s, e

    @staticmethod
    def split(line):
        return [x.strip() for x in line.strip()[1:-1].split(" | ")] if line.startswith("|") else None

    def table(self, blk):
        s, e = self.block_range(blk)
        hdr_i = next(i for i in range(s, e) if self.lines[i].startswith("|"))
        hdr = self.split(self.lines[hdr_i])
        rows = [i for i in range(hdr_i + 2, e) if self.lines[i].startswith("|")]
        return hdr, rows

    def row_index(self, blk, key):
        hdr, rows = self.table(blk)
        hits = [i for i in rows if self.split(self.lines[i])[0].startswith(key)]
        assert len(hits) == 1, (blk, key, len(hits))
        return hdr, hits[0]

    def _col(self, hdr, name):
        ix = [k for k, h in enumerate(hdr) if h.startswith(name)]
        assert len(ix) == 1, (name, hdr)
        return ix[0]

    def cell_get(self, blk, key, colname):
        hdr, i = self.row_index(blk, key)
        return self.split(self.lines[i])[self._col(hdr, colname)]

    def _put(self, i, cells):
        for c in cells:
            assert "|" not in c, c[:80]
        self.lines[i] = "| " + " | ".join(cells) + " |"

    def sub(self, blk, key, colname, old, new, reason, kind="edit", count=1):
        hdr, i = self.row_index(blk, key)
        cells = self.split(self.lines[i])
        k = self._col(hdr, colname)
        assert cells[k].count(old) == count, (blk, key, colname, old, cells[k].count(old), cells[k][:120])
        before = cells[k]
        cells[k] = cells[k].replace(old, new)
        self._put(i, cells)
        _log("inv", "INV (%s) %s / %s" % (blk, key[:40], colname[:30]), kind, before, cells[k], reason)

    def append(self, blk, key, colname, text, reason):
        """Append a sentence to a cell, in the cell style (sentences joined by '. ', no final full stop)."""
        hdr, i = self.row_index(blk, key)
        cells = self.split(self.lines[i])
        k = self._col(hdr, colname)
        before = cells[k]
        cells[k] = cells[k].rstrip() + ". " + text.rstrip(".")
        self._put(i, cells)
        _log("inv", "INV (%s) %s / %s" % (blk, key[:40], colname[:30]), "add", "(end of cell) " + before[-80:], cells[k][len(before):].lstrip(". "), reason)

    def url_add(self, blk, key, urls, reason):
        hdr, i = self.row_index(blk, key)
        cells = self.split(self.lines[i])
        before = cells[-1]
        for u in urls:
            assert u not in cells[-1], u
            cells[-1] = cells[-1] + " ; " + u
        self._put(i, cells)
        _log("inv", "INV (%s) %s / Source URL" % (blk, key[:40]), "url", "(none)", " ; ".join(urls), reason)

    def para_sub(self, old, new, reason, line_prefix=None):
        """Replace text in a non-table paragraph line (scope paragraph or block intro)."""
        hits = [i for i, l in enumerate(self.lines) if old in l and not l.startswith("|")]
        assert len(hits) == 1, (old[:60], len(hits))
        i = hits[0]
        assert self.lines[i].count(old) == 1
        before = self.lines[i]
        self.lines[i] = before.replace(old, new)
        loc = "INV scope paragraph" if i == 2 else "INV intro (line %d)" % (i + 1)
        _log("inv", loc, "edit", old, new, reason)

    def render(self):
        return "\n".join(self.lines).rstrip("\n") + "\n"


def short(s, n=230):
    s = s.replace("**", "").replace("\n", " // ")
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > n:
        s = s[:n - 1].rstrip() + "…"
    return s.replace("|", "\\|")
