"""Line-based editor that applies logged edits to a draft by ORIGINAL line number and keeps a change log."""
import re


def short(s, n=110):
    s = s.replace("**", "").replace("|", "/").replace("`", "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


class Doc:
    def __init__(self, path, tag):
        self.tag = tag
        self.orig = open(path, encoding="utf-8").read().split("\n")
        self.cur = {i + 1: l for i, l in enumerate(self.orig)}
        self.ins = {}
        self.dele = set()
        self.log = []  # dicts: loc, kind, before, after, why

    # ---- logging
    def _log(self, loc, kind, before, after, why):
        self.log.append(dict(loc=loc, kind=kind, before=short(before), after=short(after), why=why))

    # ---- edit primitives
    def sub(self, n, old, new, loc, kind, why, count=1):
        line = self.cur[n]
        assert isinstance(line, str), (n, "line already split")
        c = line.count(old)
        assert c == count, (self.tag, n, old[:60], "found", c, "expected", count)
        self.cur[n] = line.replace(old, new)
        self._log(loc, kind, old, new, why)

    def rsub(self, n, pattern, new, loc, kind, why, count=1):
        line = self.cur[n]
        found = re.findall(pattern, line)
        assert len(found) == count, (self.tag, n, pattern, len(found))
        self.cur[n] = re.sub(pattern, new, line)
        self._log(loc, kind, str(found[0]), new, why)

    def replace(self, n, new, loc, kind, why):
        """new: str or list of lines (split)."""
        before = self.cur[n]
        self.cur[n] = new
        after = new if isinstance(new, str) else " // ".join(new)
        self._log(loc, kind, before, after, why)

    def delete(self, n, loc, why, kind="delete"):
        before = self.cur[n]
        self.dele.add(n)
        self._log(loc, kind, before, "(deleted)", why)

    def after(self, n, lines, loc, why, kind="add"):
        if isinstance(lines, str):
            lines = [lines]
        self.ins.setdefault(n, []).extend(lines)
        self._log(loc, kind, "(none)", " // ".join(lines), why)

    def silent_delete(self, ns):
        for n in ns:
            self.dele.add(n)

    # ---- output
    def result(self):
        out = []
        for n in range(1, len(self.orig) + 1):
            if n not in self.dele:
                v = self.cur[n]
                if isinstance(v, list):
                    out.extend(v)
                else:
                    out.append(v)
            out.extend(self.ins.get(n, []))
        return "\n".join(out)
