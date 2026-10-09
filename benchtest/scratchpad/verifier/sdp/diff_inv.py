"""P7 verifier: cell-by-cell diff of sdp_inventory.md vs sdp_inventory_final.md, explained by merger log.json."""
import re, json, difflib
D = "benchtest/drafts/"

def parse(path):
    blocks, cur, intro, head = {}, None, {}, []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## Reviewer notes"):
            cur = None; continue
        m = re.match(r"^## \((\w)\)", line)
        if m:
            cur = m.group(1); blocks[cur] = []; intro[cur] = []; continue
        if cur is None:
            head.append(line); continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r"[-: ]*", c) for c in cells):
                continue
            blocks[cur].append(cells)
        elif line.strip():
            intro[cur].append(line)
    return blocks, intro, head

ob, oi, oh = parse(D + "sdp_inventory.md")
fb, fi, fh = parse(D + "sdp_inventory_final.md")
log = [e for e in json.load(open("benchtest/scratchpad/merger/sdp/log.json", encoding="utf-8")) if e["file"] == "inv"]
afters = [e["after"] for e in log]

def gsub(s):
    s = re.sub(r"\(my count of rows in the infoType categories table, grouped by my own rule\)",
               "(count of rows in the infoType categories table, grouped by the rule in the block note)", s)
    s = re.sub(r"\(my count of the Industry column\)", "(count of the Industry column)", s)
    return s

def explained(new):
    return any(new in a or a in new for a in afters if len(a) > 20)

problems = []
for b in sorted(fb):
    orows, frows = ob[b], fb[b]
    if len(orows) != len(frows):
        problems.append(f"({b}) row count {len(orows)} -> {len(frows)}")
    if orows[0] != frows[0]:
        problems.append(f"({b}) header changed: {orows[0]} -> {frows[0]}")
    for i, (o, f) in enumerate(zip(orows[1:], frows[1:]), 1):
        if o[0] != f[0]:
            problems.append(f"({b}) row {i} key changed: {o[0]} -> {f[0]}")
        for j, (oc, fc) in enumerate(zip(o, f)):
            if oc == fc or gsub(oc) == fc:
                continue
            # find a log entry whose after equals fc (cell edit) or contains the changed piece
            sm = difflib.SequenceMatcher(None, gsub(oc), fc, autojunk=False)
            added = " ".join(fc[j1:j2] for t, i1, i2, j1, j2 in sm.get_opcodes() if t in ("insert", "replace"))
            ok = any(fc == a or (added.strip() and added.strip()[:60] in a) for a in afters)
            if not ok:
                problems.append(f"({b}) row {i} '{f[0][:40]}' cell {j+1}: UNEXPLAINED added: {added[:200]}")
    oin, fin_ = " ".join(oi[b]), " ".join(fi[b])
    if gsub(oin) != fin_ and not any(fin_ == a or fin_[:80] in a for a in afters):
        problems.append(f"({b}) intro changed and not matched to a log entry")
print("blocks:", {b: len(fb[b]) - 1 for b in fb})
print("problems:", len(problems))
for p in problems: print(" ", p)
