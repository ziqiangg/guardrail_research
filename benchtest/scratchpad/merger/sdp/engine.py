"""Merge engine for the sdp P6 merge. Exact-match edits with a change log; every edit asserts it matches once."""
import re

ROOT = "/home/user/guardrail_research/benchtest/drafts/"
LOG = []  # dicts: file, loc, tid, before, after, reason, full


def short(s, n=170):
    s = s.strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


class Doc:
    def __init__(self, name, lines, kind):
        self.name, self.lines, self.kind = name, lines, kind

    def secs(self):
        out, col, row, blk = [], None, None, "head"
        for ln in self.lines:
            if self.kind == "col":
                m = re.match(r"^## Column (SD\d+):", ln)
                if m:
                    col, row = m.group(1), None
                m = re.match(r"^### (R\d)\s*$", ln)
                if m:
                    row = m.group(1)
                out.append(f"{col} {row}" if col and row else (col or ""))
            else:
                m = re.match(r"^## \((\w)\)", ln)
                if m:
                    blk = f"({m.group(1)})"
                elif ln.startswith("## Reviewer notes"):
                    blk = "RN"
                out.append(blk)
        return out

    def find(self, sec, key, count=1):
        secs = self.secs()
        idx = [i for i, ln in enumerate(self.lines) if secs[i] == sec and key in ln]
        assert len(idx) == count, f"{self.name} [{sec}] key {key!r}: {len(idx)} matches (wanted {count})"
        return idx

    def _log(self, sec, tid, before, after, reason, full=False):
        LOG.append(dict(file=self.name, loc=sec, tid=tid, before=before, after=after, reason=reason, full=full))

    # whole-line replace (one or several new lines)
    def rep(self, sec, key, new, tid, reason, full=False):
        (i,) = self.find(sec, key)
        old = self.lines[i]
        new = new if isinstance(new, list) else [new]
        self.lines[i : i + 1] = new
        self._log(sec, tid, old, "\n".join(new), reason, full)

    def sub(self, sec, key, old, new, tid, reason, full=False, count=1):
        idx = self.find(sec, key)
        i = idx[0]
        assert self.lines[i].count(old) == count, f"{self.name} [{sec}] {key!r}: substring {old!r} found {self.lines[i].count(old)}x"
        before = self.lines[i]
        self.lines[i] = self.lines[i].replace(old, new)
        self._log(sec, tid, before, self.lines[i], reason, full)

    def ins_after(self, sec, key, new, tid, reason):
        (i,) = self.find(sec, key)
        new = new if isinstance(new, list) else [new]
        self.lines[i + 1 : i + 1] = new
        self._log(sec, tid, "(none)", "\n".join(new), reason)

    def ins_before(self, sec, key, new, tid, reason):
        (i,) = self.find(sec, key)
        new = new if isinstance(new, list) else [new]
        self.lines[i:i] = new
        self._log(sec, tid, "(none)", "\n".join(new), reason)

    def delete(self, sec, key, tid, reason):
        (i,) = self.find(sec, key)
        old = self.lines[i]
        del self.lines[i]
        self._log(sec, tid, old, "(deleted)", reason)

    def add_r9(self, col, urls, tid, reason):
        """Append bullets at the end of R9 of a column (before the next column heading or end of file)."""
        secs = self.secs()
        idx = [i for i, s in enumerate(secs) if s == f"{col} R9"]
        assert idx, col
        last = idx[-1]
        existing = {ln[2:].strip() for ln in self.lines[idx[0] : last + 1] if ln.startswith("• ")}
        new = [f"• {u}" for u in urls if u not in existing]
        if not new:
            return
        self.lines[last + 1 : last + 1] = new
        self._log(f"{col} R9", tid, "(none)", "\n".join(new), reason)

    def gsub(self, pattern, new, tid, reason, count=None, flags=0, secs_filter=None):
        n = 0
        secs = self.secs()
        for i, ln in enumerate(self.lines):
            if secs_filter and not secs_filter(secs[i]):
                continue
            nl, k = re.subn(pattern, new, ln, flags=flags)
            if k:
                n += k
                self.lines[i] = nl
        if count is not None:
            assert n == count, f"{self.name} gsub {pattern!r}: {n} replacements (wanted {count})"
        self._log("(many)", tid, pattern, new, f"{reason} ({n} replacements)")
        return n

    # inventory cell helpers -------------------------------------------------
    @staticmethod
    def split_row(line):
        assert line.startswith("| ") and line.endswith(" |"), line[:60]
        return line[2:-2].split(" | ")

    @staticmethod
    def join_row(cells):
        return "| " + " | ".join(cells) + " |"

    def cell(self, sec, rowkey, idx, new=None, old=None, repl=None, tid="", reason="", count=1):
        """Edit one table cell: whole replace (new) or substring replace (old->repl)."""
        i_list = self.find(sec, "| " + rowkey + " |")
        (i,) = i_list
        cells = self.split_row(self.lines[i])
        before = cells[idx]
        if new is not None:
            cells[idx] = new
        else:
            assert before.count(old) == count, f"{self.name} [{sec}] {rowkey!r} cell {idx}: {old!r} found {before.count(old)}x"
            cells[idx] = before.replace(old, repl)
        self.lines[i] = self.join_row(cells)
        self._log(f"{sec} row '{rowkey}' cell {idx + 1}", tid, before, cells[idx], reason)
