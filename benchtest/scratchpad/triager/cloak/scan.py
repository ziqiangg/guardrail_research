import re,sys,collections
D="benchtest/drafts/"
def cols(path):
    out={};cur=None;row=None
    for i,l in enumerate(open(path,encoding='utf-8').read().split("\n"),1):
        m=re.match(r"^## Column (CK\d): (.*)$",l)
        if m: cur=m.group(1);out[cur]={'hdr':m.group(2),'rows':collections.OrderedDict(),'start':i};row=None;continue
        if l.startswith("## Reviewer"): cur=None
        if cur is None: continue
        m=re.match(r"^### R(\d)",l)
        if m: row=int(m.group(1));out[cur]['rows'][row]={'sum':None,'b':[]};continue
        if row is None: continue
        if l.startswith("Summary: "): out[cur]['rows'][row]['sum']=(i,l[9:])
        elif l.startswith("• "): out[cur]['rows'][row]['b'].append((i,l))
    return out
A=cols(D+"cloak_cols_a.md");B=cols(D+"cloak_cols_b.md");C={**A,**B}
LAB=re.compile(r"\*\*\[(Documented(?:: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*\s*$")
print("headers");
for k,v in C.items(): print(k,v['hdr'])
tot=collections.Counter()
for k,v in C.items():
    print("==",k)
    for r,d in v['rows'].items():
        labs=collections.Counter()
        for i,b in d['b']:
            m=LAB.search(b); labs[m.group(1).split(":")[0] if m else 'none']+=1
        s=d['sum'][1]; body=LAB.sub("",s).strip(); w=len(re.sub(r"\*\*","",body).split())
        print(k,"R%d"%r,"bullets",len(d['b']),dict(labs),"sumwords",w, "line",d['sum'][0])
        for x,y in labs.items(): tot[(k,x)]+=y
print(tot)
# TBV / ND lines
for k,v in C.items():
    for r,d in v['rows'].items():
        if r>7: continue
        for i,b in d['b']:
            if '[To be verified]' in b: print("TBV",k,r,i)
