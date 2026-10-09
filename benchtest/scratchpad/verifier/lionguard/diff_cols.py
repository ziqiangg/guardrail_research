"""P7 verifier (lionguard): difflib diff of cols_a vs two_level; added/removed lines searched in changes.md
(and, for information, in resolutions_1.md) by normalised prefixes."""
import re, difflib
D = "benchtest/drafts/"
def parse(path):
    cols, cur, row = {}, None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## Reviewer notes"):
            cur = None; continue
        m = re.match(r"^## Column (LN\d):", line)
        if m:
            cur = m.group(1); cols[cur] = {r: [] for r in range(1, 10)}; row = None; continue
        if cur is None: continue
        m = re.match(r"^### R([1-9])\s*$", line)
        if m: row = int(m.group(1)); continue
        if row and (line.startswith("Summary: ") or line.startswith("• ") or line.startswith("  – ")):
            cols[cur][row].append(line)
    return cols
def norm(s):
    s = s.replace("**", "").replace("…", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()
orig = parse(D+"lionguard_cols_a.md"); fin = parse(D+"lionguard_two_level.md")
chg = norm(open(D+"lionguard_changes.md", encoding="utf-8").read())
res = norm(open(D+"lionguard_resolutions_1.md", encoding="utf-8").read())
def inside(x, hay):
    n = re.sub(r"^(Summary: |• |– )", "", norm(x))
    for L in (60, 40, 25):
        if n[:L] and n[:L] in hay: return True
    if len(n) > 80 and n[30:80] in hay: return True
    return False
adds = rems = 0; un = []
for c in fin:
    for r in range(1, 10):
        o, f = orig[c][r], fin[c][r]
        sm = difflib.SequenceMatcher(None, o, f, autojunk=False)
        for t, i1, i2, j1, j2 in sm.get_opcodes():
            if t == "equal": continue
            for x in f[j1:j2]:
                adds += 1
                if not inside(x, chg): un.append(("+", c, r, x, inside(x, res)))
            for x in o[i1:i2]:
                rems += 1
                if not inside(x, chg): un.append(("-", c, r, x, inside(x, res)))
print("added", adds, "removed", rems, "not prefix-matched in changes.md", len(un))
for s, c, r, x, inres in un: print(f"{s} {c} R{r} [in resolutions: {inres}] {x[:300]}")
