import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
D="benchtest/drafts/"
urls={}
def add(u,where):
    u=u.rstrip(").,;")
    urls.setdefault(u,set()).add(where)
col=row=None
for l in open(D+"purplellama_two_level.md",encoding='utf-8'):
    m=re.match(r"^## Column (PL\d)",l)
    if m: col=m.group(1)
    m=re.match(r"^### (R\d)",l)
    if m: row=m.group(1)
    if row=="R9" and l.startswith("• http"): add(l[2:].strip(),col+" R9")
blk=None
for l in open(D+"purplellama_inventory_final.md",encoding='utf-8'):
    m=re.match(r"^## \((\w)\)",l)
    if m: blk=m.group(1)
    if blk and l.startswith("|") and not re.match(r"^\|[-: |]+\|\s*$",l):
        cells=[c.strip() for c in l.strip().strip("|").split("|")]
        if "Source URL" in cells[-1]: continue
        for u in re.findall(r"https?://\S+",cells[-1]): add(u,"INV("+blk+")")
sec=None
for l in open(D+"purplellama_eval_tooling_final.md",encoding='utf-8'):
    if l.startswith("## "): sec=l[3:].strip()
    if sec in (None,"Topic"): continue
    for u in re.findall(r"https?://[^\s|`]+",l): add(u,"EV "+str(sec))
for u in sorted(urls): print(u+"\t"+",".join(sorted(urls[u])))
