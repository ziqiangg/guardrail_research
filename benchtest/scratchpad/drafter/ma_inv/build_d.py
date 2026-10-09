import re,json
def lines(f): return [l.rstrip('\n') for l in open(f,encoding='utf-8')]
# feature availability: supported features by region
fa=lines('feature-availability-by-region.txt')
i=[k for k,l in enumerate(fa) if l.startswith('Supported features by region')][0]
# find table start after "| Region/multi-region" header following i
j=[k for k in range(i,len(fa)) if fa[k].startswith('| Region/multi-region')][0]
rows={}
k=j+6
cur=None
buf=[]
txt=fa[k:]
# tokenise: a row starts with '| <name>' then '|' then filters lines then '| ' 4 values
k=0
order=[]
while k<len(txt):
    l=txt[k]
    if l.startswith('Send feedback'): break
    m=re.match(r'^\| (\S+)$',l)
    if m and k+1<len(txt) and txt[k+1]=='|':
        name=m.group(1); k+=2; filt=[]
        while not txt[k].startswith('|'):
            filt.append(txt[k]); k+=1
        vals=[]
        while len(vals)<4:
            vals.append(txt[k][2:].strip()); k+=1
        rows[name]=dict(filters=filt,ml=vals[0],csam=vals[1],img=vals[2],av=vals[3]); order.append(name)
    else: k+=1
print(order, len(order))
json.dump(rows,open('far.json','w'),indent=1)
# data residency table
dr=lines('data-residency.txt')
i=[k for k,l in enumerate(dr) if l.startswith('| Region/multi-region')][0]
t=dr[i+6:]
res={}
k=0
while k<len(t):
    l=t[k]
    if l.startswith('1The Feature support'): break
    m=re.match(r'^\| (\S+)$',l)
    if m and t[k+1].startswith('| '):
        name=m.group(1); vals=[t[k+x][2:].strip() for x in range(1,6)]
        res[name]=dict(jur=vals[0],rest=vals[1],use=vals[2],transit=vals[3],support=vals[4]); k+=6
    else: k+=1
print(len(res)); json.dump(res,open('dr.json','w'),indent=1)
# locations
lo=lines('locations.txt')
desc={}
for k,l in enumerate(lo):
    if re.match(r'^\| [a-z]+(-[a-z]+\d*)?$',lo[k]) and k>0 and lo[k-1].startswith('| ') and (re.match(r'^\| [A-Z]',lo[k-1])):
        desc[lo[k][2:]]=lo[k-1][2:]
print(desc)
json.dump(desc,open('loc.json','w'),indent=1)
# filter versions
fv=lines('set-filter-version.txt')
i=[k for k,l in enumerate(fv) if l.startswith('| Version')][0]
t=fv[i:]
vers={}
k=0
cur=None
for l in t:
    if l.startswith('For information about what'): break
    m=re.match(r'^\| (v\d)$',l)
    if m: cur=m.group(1); vers[cur]=[]; continue
    if cur and re.match(r'^[a-z]+-?[a-z]*\d*( \(.*)?$',l.strip()) or (cur and l.startswith('australia-southeast2')) or (cur and l.strip() in ('eu','us')):
        vers[cur].append(l.strip())
print(json.dumps(vers,indent=1))
json.dump(vers,open('fv.json','w'),indent=1)
