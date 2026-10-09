import re,sys,collections
LAB=re.compile(r"\*\*\[(Documented(?:: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*\s*$")
def parse(path):
    cols={};cur=None;row=None
    for ln in open(path,encoding='utf-8'):
        ln=ln.rstrip('\n')
        m=re.match(r'^## Column (SD\d):',ln)
        if m: cur=m.group(1);cols[cur]={};continue
        if ln.startswith('## '): cur=None;continue
        m=re.match(r'^### R([1-9])\s*$',ln)
        if m and cur: row=int(m.group(1));cols[cur][row]={'sum':None,'b':[]};continue
        if cur and row:
            if ln.startswith('Summary: '): cols[cur][row]['sum']=ln[9:]
            elif ln.startswith('• ') or ln.startswith('  – '): cols[cur][row]['b'].append(ln)
    return cols
cols={}
for p in [a for a in sys.argv[1:] if a!="-v"]: cols.update(parse(p))
tot=collections.Counter()
for c,rows in cols.items():
    cnt=collections.Counter()
    for r,d in rows.items():
        s=d['sum'];body=LAB.sub('',s).strip();w=len(re.sub(r'\*\*','',body).split())
        lim=60 if r==7 else 45
        flag=' OVER' if w>lim else ''
        bad=[ch for ch in ['`','_','$','%'] if ch in s]
        nonascii=[ch for ch in s if ord(ch)>127]
        if flag or bad or nonascii: print(c,'R%d'%r,w,'words',flag,bad,nonascii)
        lab=LAB.search(s); sl=lab.group(1) if lab else None
        print(f"{c} R{r} sum={w}w label={sl} bullets={sum(1 for b in d['b'] if b.startswith('• '))}") if '-v' in sys.argv else None
        for b in d['b']:
            if not b.startswith('• '): continue
            m=LAB.search(b)
            k=m.group(1).split(':')[0] if m else ('nolabel' if r in (8,9) else 'MISSING')
            cnt[(r,k)]+=1; tot[k]+=1
    print(c,'summaries:',{r:(rows[r]['sum'] and (LAB.search(rows[r]['sum']).group(1).split(':')[0] if LAB.search(rows[r]['sum']) else 'none')) for r in rows})
    print(c,'labels',{k:sum(v for (r,kk),v in cnt.items() if kk==k) for k in ['Documented','Inferred','To be verified','Not disclosed','nolabel','MISSING']}, 'R8 bullets',sum(v for (r,kk),v in cnt.items() if r==8))
print(tot)
