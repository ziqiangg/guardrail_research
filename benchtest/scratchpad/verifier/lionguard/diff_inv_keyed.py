"""Key-aligned cell diff of lionguard_inventory.md vs _final (block d has an inserted row)."""
import re, difflib, sys
sys.path.insert(0, "benchtest/scratchpad/verifier/lionguard")
D = "benchtest/drafts/"
def rows(path):
    out, cur = {}, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## Reviewer notes") or line.startswith("## Self-check"): cur = None; continue
        m = re.match(r"^## \((\w)\)", line)
        if m: cur = m.group(1); out[cur] = {}; continue
        if cur and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r"[-: ]*", c) for c in cells): continue
            out[cur][cells[0][:40]] = cells
    return out
o, f = rows(D+"lionguard_inventory.md"), rows(D+"lionguard_inventory_final.md")
for b in f:
    for k, fc in f[b].items():
        if k not in o[b]: print(f"({b}) NEW ROW {k}"); continue
        oc = o[b][k]
        for j, (x, y) in enumerate(zip(oc, fc)):
            if x != y:
                sm = difflib.SequenceMatcher(None, x.split(), y.split(), autojunk=False)
                for t, i1, i2, j1, j2 in sm.get_opcodes():
                    if t != "equal":
                        print(f"({b}) {k[:30]} col{j+1} {t}: -[{' '.join(x.split()[i1:i2])[:160]}] +[{' '.join(y.split()[j1:j2])[:220]}]")
    for k in o[b]:
        if k not in f[b]: print(f"({b}) REMOVED ROW {k}")
