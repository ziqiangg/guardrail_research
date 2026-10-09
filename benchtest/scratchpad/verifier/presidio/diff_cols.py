"""P7 verifier (presidio): independent difflib diff of cols_a+cols_b vs two_level; each added/removed line
is searched in presidio_changes.md by normalised prefixes."""
import re, difflib, sys
D = "benchtest/drafts/"
def parse(path):
    cols, cur, row = {}, None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## Reviewer notes"):
            cur = None; continue
        m = re.match(r"^## Column (PD\d):", line)
        if m:
            cur = m.group(1); cols[cur] = {r: [] for r in range(1, 10)}; row = None; continue
        if cur is None: continue
        m = re.match(r"^### R([1-9])\s*$", line)
        if m: row = int(m.group(1)); continue
        if row and (line.startswith("Summary: ") or line.startswith("• ") or line.startswith("  – ")):
            cols[cur][row].append(line)
    return cols
def norm(s):
    s = s.replace("**", "").replace("…", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip()
orig = {}; orig.update(parse(D+"presidio_cols_a.md")); orig.update(parse(D+"presidio_cols_b.md"))
fin = parse(D+"presidio_two_level.md")
chg = norm(open(D+"presidio_changes.md", encoding="utf-8").read())
def inlog(x):
    n = norm(x)
    n = re.sub(r"^(Summary: |• |– )", "", n)
    for L in (60, 40, 25):
        seg = n[:L]
        if seg and seg in chg: return True
    # try middle segment
    if len(n) > 80 and n[30:80] in chg: return True
    return False
print("columns orig", sorted(orig), "final", sorted(fin))
add_un, rem_un, adds, rems = [], [], 0, 0
for c in sorted(fin):
    for r in range(1, 10):
        o, f = orig[c][r], fin[c][r]
        sm = difflib.SequenceMatcher(None, o, f, autojunk=False)
        for t, i1, i2, j1, j2 in sm.get_opcodes():
            if t == "equal": continue
            for x in f[j1:j2]:
                adds += 1
                if not inlog(x): add_un.append(f"{c} R{r} +: {x[:260]}")
            for x in o[i1:i2]:
                rems += 1
                if not inlog(x): rem_un.append(f"{c} R{r} -: {x[:260]}")
print("added lines", adds, "removed lines", rems)
print("ADDED not found in changes.md:", len(add_un))
for u in add_un: print(" ", u)
print("REMOVED not found in changes.md:", len(rem_un))
for u in rem_un: print(" ", u)
