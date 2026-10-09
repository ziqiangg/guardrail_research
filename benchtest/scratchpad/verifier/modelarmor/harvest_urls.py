import re
D="benchtest/drafts/"
urls={}
cur=None; row=None
for line in open(D+"modelarmor_two_level.md",encoding="utf-8"):
    m=re.match(r"^## Column (MA\d+):",line)
    if m: cur=m.group(1); continue
    m=re.match(r"^### R(\d)\s*$",line)
    if m: row=int(m.group(1)); continue
    if row==9 and line.startswith("• "):
        u=line[2:].strip(); urls.setdefault(u,set()).add(cur+" R9")
# inventory: last column of each table
blk=None
for line in open(D+"modelarmor_inventory_final.md",encoding="utf-8"):
    m=re.match(r"^## \((\w)\)",line)
    if m: blk=m.group(1); continue
    if blk and line.startswith("|"):
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        last=cells[-1]
        for u in re.findall(r"https?://[^\s;]+",last):
            urls.setdefault(u.rstrip(".,"),set()).add("INV("+blk+")")
skip=[u for u in urls if re.search(r"googleapis\.com|\{|\}",u)]
keep=sorted(u for u in urls if u not in skip)
open("benchtest/scratchpad/verifier/modelarmor/urls.txt","w").write("\n".join(keep)+"\n")
open("benchtest/scratchpad/verifier/modelarmor/urls_used.tsv","w").write("\n".join(u+"\t"+", ".join(sorted(urls[u])) for u in keep)+"\n")
print(len(urls),"harvested;",len(keep),"to check; skipped:",skip)
