import re,glob,sys
def norm(s):
    s=s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')
    s=s.replace("|"," ")
    return re.sub(r"\s+"," ",s).strip()
corpus=""
for f in glob.glob("raw/*.txt"):
    corpus+=" "+norm(open(f,encoding="utf-8",errors="replace").read())
corpus+=" "+norm(open("/tmp/ma_clone/gcg/modelarmor/apiv1/modelarmorpb/service.pb.go",encoding="utf-8").read())
corpus_l=corpus
txt=open("/home/user/guardrail_research/benchtest/drafts/modelarmor_cols_a.md",encoding="utf-8").read()
txt=txt.split("## Reviewer notes")[0]
miss=0;n=0
for ln_no,ln in enumerate(txt.splitlines(),1):
    ln2=re.sub(r"`[^`]*`","",ln)   # drop inline code
    for q in re.findall(r'"([^"]{6,})"',ln2):
        parts=[p.strip(" .,;") for p in q.split("…")]
        for p in parts:
            if len(p)<6: continue
            n+=1
            if len(q.split())>40: print("LONG",ln_no,q[:60])
            if norm(p).strip(" .,;") not in corpus_l:
                miss+=1; print("MISS L%d: %s"%(ln_no,p))
print("quotes checked",n,"misses",miss)
