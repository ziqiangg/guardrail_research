import re
D="benchtest/drafts/"
urls={}
row=None
for line in open(D+"lionguard_two_level.md",encoding="utf-8"):
    m=re.match(r"^### R([1-9])\s*$",line)
    if m: row=int(m.group(1)); continue
    if row==9 and line.startswith("• "):
        urls.setdefault(line[2:].strip(),set()).add("LN1 R9")
blk=None
for line in open(D+"lionguard_inventory_final.md",encoding="utf-8"):
    m=re.match(r"^## \((\w)\)",line)
    if m: blk=m.group(1); continue
    if blk and line.startswith("|"):
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r"[-: ]*",c) for c in cells) or cells[-1]=="Source URL": continue
        for u in cells[-1].split(" ; "):
            urls.setdefault(u.strip(),set()).add(f"INV ({blk})")
# inline URLs elsewhere in either final (not in R9 / Source URL)
other=set()
for f in ("lionguard_two_level.md","lionguard_inventory_final.md"):
    for u in re.findall(r"https?://[^\s|;)`\"]+", open(D+f,encoding="utf-8").read()):
        u=u.rstrip(".,")
        if u not in urls: other.add(u)
with open("benchtest/scratchpad/verifier/lionguard/urls.txt","w",encoding="utf-8") as o:
    for u in sorted(urls): o.write(u+"\t"+", ".join(sorted(urls[u]))+"\n")
print(len(urls),"distinct URLs; inline-only:",sorted(other))
