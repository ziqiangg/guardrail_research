import re,json,collections
L=open("infotypes_ref.txt",encoding="utf-8").read().split("\n")
# find category table start
start=next(i for i,l in enumerate(L) if l.strip()=="| Availability")+1
end=next(i for i in range(start,len(L)) if L[i].startswith("Send feedback") or L[i].startswith("Except as otherwise"))
recs=[];cur=None
for l in L[start:end]:
    m=re.match(r"^\| ([A-Z0-9_/&\-\.]+)$",l)
    if m and (cur is None or len(cur)>=1):
        # new record when line starts with "| NAME"
        cur=[m.group(1)];recs.append(cur);continue
    if cur is not None: cur.append(l)
out=[]
for r in recs:
    name=r[0]; rest="\n".join(r[1:])
    cells=[c.strip() for c in rest.split("|")]
    cells=[c for c in cells]
    out.append((name,cells))
print(len(out))
json.dump(out,open("cat_raw.json","w"))
for n,c in out[:6]: print(n,c)
