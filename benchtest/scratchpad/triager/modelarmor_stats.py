import re,sys,collections
files={'A':'benchtest/drafts/modelarmor_cols_a.md','B':'benchtest/drafts/modelarmor_cols_b.md'}
LAB=re.compile(r"\*\*\[(Documented(?:: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*\s*$")
tot=collections.Counter()
rows=[]
for k,p in files.items():
    cur=None;row=None
    for ln in open(p,encoding='utf-8'):
        ln=ln.rstrip('\n')
        m=re.match(r'^## Column (MA\d+):',ln)
        if m: cur=m.group(1);continue
        if ln.startswith('## Reviewer'): cur=None
        if not cur: continue
        m=re.match(r'^### R(\d)',ln)
        if m: row=int(m.group(1));continue
        if ln.startswith('Summary: '):
            s=ln[9:]
            lab=LAB.search(s)
            body=LAB.sub('',s).strip()
            w=len(re.sub(r'\*\*','',body).split())
            rows.append((k,cur,row,'S',w,lab.group(1) if lab else None))
        elif ln.startswith('• '):
            lab=LAB.search(ln)
            rows.append((k,cur,row,'B',0,lab.group(1) if lab else None))
c=collections.defaultdict(collections.Counter)
for k,col,r,t,w,l in rows:
    if t=='B':
        if r==8: c[(k,col)]['R8']+=1
        elif r<=7:
            c[(k,col)][(l or 'none').split(':')[0]]+=1
for key in sorted(c): print(key,dict(c[key]))
print('--- summaries over limit / label mismatches')
for k,col,r,t,w,l in rows:
    if t=='S':
        lim=60 if r==7 else 45
        if w>lim: print('OVER',col,r,w)
for k,col,r,t,w,l in rows:
    if t=='S' and r<=7:
        print(col,'R%d'%r,w,l)
