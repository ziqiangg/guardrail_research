import re,sys,io,difflib,glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
D="benchtest/drafts/"
def parse(p):
    blocks={}; cur=None; intro={}
    for line in open(p,encoding='utf-8').read().splitlines():
        m=re.match(r"^## (\(\w\))",line)
        if m: cur=m.group(1); blocks[cur]=[]; intro[cur]=[]; continue
        if line.startswith("## "): cur=None; continue
        if cur is None: continue
        if line.startswith("|"):
            cells=[c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r"[-: ]*",c) for c in cells): continue
            blocks[cur].append(cells)
        elif line.strip(): intro[cur].append(line.strip())
    return blocks,intro
ob,oi=parse(D+"purplellama_inventory.md"); fb,fi=parse(D+"purplellama_inventory_final.md")
log=open(D+"purplellama_changes.md",encoding='utf-8').read()
ops=""
for f in glob.glob("benchtest/scratchpad/merger/purplellama/ops_*.py")+["benchtest/scratchpad/merger/purplellama/merge_pl.py"]: ops+=open(f,encoding='utf-8').read()
ops=re.sub(r"\s+"," ",ops.replace("\'","'").replace('\\"','"'))
logn=re.sub(r"\s+"," ",log)
def frags(old,new):
    sm=difflib.SequenceMatcher(None,old,new,autojunk=False); out=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op in("replace","insert") and j2-j1>=12: out.append(new[j1:j2])
    return out
n=0
for b in fb:
    if len(ob.get(b,[]))!=len(fb[b]): print("ROWCOUNT",b,len(ob.get(b,[])),len(fb[b]))
    okeys={tuple(r[:2]):r for r in ob.get(b,[])}
    hdr=fb[b][0]
    for r in fb[b]:
        o=okeys.get(tuple(r[:2])) or (ob[b][fb[b].index(r)] if len(ob[b])==len(fb[b]) else None)
        if o is None: print("NEWROW?",b,r[0][:60]); continue
        for k,(x,y) in enumerate(zip(o,r)):
            if x==y: continue
            n+=1
            for f in frags(x,y):
                g=f.strip().lstrip(". ;").strip()[:40]
                if len(g)<12: continue
                if g in logn or g in ops: continue
                print("UNMATCHED",b,r[0][:30],"/",hdr[k][:25],"|",f[:200])
    if oi[b]!=fi[b]:
        for f in frags(" ".join(oi[b])," ".join(fi[b])):
            g=f.strip().lstrip(". ;").strip()[:40]
            if len(g)>=12 and g not in logn and g not in ops: print("INTRO UNMATCHED",b,f[:200])
print("changed cells",n)
for b in fb: print(b,len(fb[b])-1,"rows",len(fb[b][0]),"cols")
