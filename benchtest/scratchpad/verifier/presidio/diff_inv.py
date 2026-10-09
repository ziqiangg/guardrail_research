"""P7 verifier (presidio): cell-by-cell diff of presidio_inventory.md vs presidio_inventory_final.md;
changed pieces searched in presidio_changes.md (normalised)."""
import re, difflib
D = "benchtest/drafts/"
def parse(path):
    blocks, cur, intro, head = {}, None, {}, []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## Reviewer notes") or line.startswith("## Self-check"):
            cur = "_x"; blocks[cur] = []; intro[cur] = []; continue
        m = re.match(r"^## \((\w)\)", line)
        if m:
            cur = m.group(1); blocks[cur] = []; intro[cur] = []; continue
        if cur is None:
            head.append(line); continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r"[-: ]*", c) for c in cells): continue
            blocks[cur].append(cells)
        elif line.strip():
            intro[cur].append(line)
    return blocks, intro, head
def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("…", "")).strip()
chg = norm(open(D+"presidio_changes.md", encoding="utf-8").read())
ob, oi, oh = parse(D+"presidio_inventory.md")
fb, fi, fh = parse(D+"presidio_inventory_final.md")
def found(piece):
    p = norm(piece)
    if len(p) < 12: return True
    for L in (60, 40, 25):
        if p[:L] in chg: return True
    if len(p) > 70 and p[-40:] in chg: return True
    return False
probs = []
for b in [k for k in fb if k != "_x"]:
    print(b, "rows", len(ob[b])-1, "->", len(fb[b])-1)
    for i, (o, f) in enumerate(zip(ob[b], fb[b])):
        if o[0] != f[0]: probs.append(f"({b}) row {i} key {o[0]} -> {f[0]}")
        for j, (oc, fc) in enumerate(zip(o, f)):
            if oc == fc: continue
            sm = difflib.SequenceMatcher(None, oc, fc, autojunk=False)
            for t, i1, i2, j1, j2 in sm.get_opcodes():
                if t == "equal": continue
                piece = fc[j1:j2] if t != "delete" else oc[i1:i2]
                # expand to word context
                ctx = fc[max(0,j1-30):j2+30] if t!="delete" else oc[max(0,i1-30):i2+30]
                if len(norm(piece)) >= 12 and not found(piece) and not found(ctx):
                    probs.append(f"({b}) '{f[0][:35]}' col{j+1} {t}: {norm(piece)[:200]}")
    oin, fin_ = " ".join(oi[b]), " ".join(fi[b])
    if oin != fin_:
        sm = difflib.SequenceMatcher(None, oin, fin_, autojunk=False)
        for t, i1, i2, j1, j2 in sm.get_opcodes():
            if t == "equal": continue
            piece = fin_[j1:j2] if t != "delete" else oin[i1:i2]
            if len(norm(piece)) >= 12 and not found(piece):
                probs.append(f"({b}) intro {t}: {norm(piece)[:200]}")
oh_, fh_ = " ".join(oh), " ".join(fh)
sm = difflib.SequenceMatcher(None, oh_, fh_, autojunk=False)
for t, i1, i2, j1, j2 in sm.get_opcodes():
    if t == "equal": continue
    piece = fh_[j1:j2] if t != "delete" else oh_[i1:i2]
    if len(norm(piece)) >= 12 and not found(piece):
        probs.append(f"scope {t}: {norm(piece)[:200]}")
print("unmatched pieces:", len(probs))
for p in probs: print(" ", p)
