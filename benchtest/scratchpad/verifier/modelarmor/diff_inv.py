"""P7 verifier: cell-by-cell diff of modelarmor_inventory.md vs _final; changed cells checked against changes.md section 3."""
import re, difflib
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
def G(s):
    s = s.replace("read 2026-10-09", "2026-10-09").replace("google-cloud-go@37f936ac", "google-cloud-go@modelarmor/v1.3.0")
    s = s.replace("blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/", "blob/modelarmor/v1.3.0/")
    return s
ob, oi, oh = parse(D + "modelarmor_inventory.md")
fb, fi, fh = parse(D + "modelarmor_inventory_final.md")
log = open(D + "modelarmor_changes.md", encoding="utf-8").read()
sec3 = log.split("## 3. Inventory changes")[1].split("## 4.")[0]
def norm(s): return re.sub(r"\s+"," ",s.replace("`","")).strip()
s3 = norm(sec3)
problems = []
for b in sorted(fb):
    orows = {r[0]: r for r in ob[b][1:]}
    print(b, "orig rows", len(ob[b])-1, "final rows", len(fb[b])-1)
    if ob[b][0] != fb[b][0]:
        problems.append(f"({b}) header changed")
    for f in fb[b][1:]:
        o = orows.get(f[0])
        if o is None:
            problems.append(f"({b}) NEW ROW {f[0][:60]}"); continue
        for j,(oc,fc) in enumerate(zip(o,f)):
            oc = G(oc)
            if oc == fc: continue
            sm = difflib.SequenceMatcher(None, oc, fc, autojunk=False)
            added = " ".join(fc[j1:j2] for t,i1,i2,j1,j2 in sm.get_opcodes() if t in ("insert","replace")).strip()
            removed = " ".join(oc[i1:i2] for t,i1,i2,j1,j2 in sm.get_opcodes() if t in ("delete","replace")).strip()
            key = norm(added)[:50]
            ok = len(key) < 12 or key in s3 or any(norm(added)[k:k+40] in s3 for k in range(0, max(1,len(norm(added))-40), 20))
            tag = "ok " if ok else "UNMATCHED"
            problems.append(f"{tag} ({b}) '{f[0][:35]}' col{j+1}: +[{added[:220]}] -[{removed[:160]}]")
    for k in orows:
        if k not in {r[0] for r in fb[b][1:]}:
            problems.append(f"({b}) ROW REMOVED/RENAMED {k[:60]}")
    if [G(x) for x in oi[b]] != fi[b]:
        problems.append(f"({b}) intro changed")
open("benchtest/scratchpad/verifier/modelarmor/diff_inv.txt","w",encoding="utf-8").write("\n".join(problems))
print(len(problems), sum(1 for p in problems if p.startswith("UNMATCHED")))
