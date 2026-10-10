import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
fin=open("benchtest/drafts/purplellama_two_level.md",encoding='utf-8').read().splitlines()
S={};col=None;row=None
for l in fin:
    m=re.match(r"^## Column (PL\d)",l)
    if m: col=m.group(1);continue
    m=re.match(r"^### (R\d)",l)
    if m: row=m.group(1);continue
    if l.startswith("Summary: "): S[(col,row)]=l[9:]
P={};col=None
for l in open("benchtest/drafts/purplellama_summaries_preview.md",encoding='utf-8').read().splitlines():
    m=re.search(r"(PL\d)\b",l)
    if l.startswith("#") and m: col=m.group(1)
    m=re.match(r"- \*\*(R\d)\*?\*\* \((\d+)w, (\d+) bullets\): (.*)$",l)
    if m: P[(col,m.group(1))]=(int(m.group(2)),m.group(4))
bad=0
for k,v in S.items():
    p=P.get(k)
    body=re.sub(r"\s*\*\*\[[^\]]+\]\*\*\s*$","",v); w=len(re.sub(r"\*\*","",body).split())
    if not p or p[1]!=v: print("DIFF",k); bad+=1
    elif p[0]!=w: print("WC",k,p[0],w)
    lim=60 if k[1]=="R7" else 45
    if w>lim: print("OVER",k,w)
print(len(S),"summaries",len(P),"preview; mismatches",bad)
