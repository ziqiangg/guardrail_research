import re
D="benchtest/drafts/"
inv=open(D+"cloak_inventory.md",encoding='utf-8').read()
scope=inv.split("## (a)")[0]
body=inv.split("## (a)",1)[1].split("## Reviewer notes")[0]
cited=set(re.findall(r"\(([A-Z][A-Z0-9\-]{1,9})(?:[,:) ;])",body))
cited|=set(re.findall(r", ([A-Z]{2,9})[,)]",body))
legend=set(re.findall(r"\b([A-Z][A-Z0-9\-]{1,9})\b",scope))
print("short names cited but not in scope paragraph:",sorted(x for x in cited if x not in legend))
# quotes > 40 words
for f in ["cloak_cols_a.md","cloak_cols_b.md","cloak_inventory.md"]:
    t=open(D+f,encoding='utf-8').read()
    for ln,l in enumerate(t.split("\n"),1):
        for q in re.findall(r'"([^"]{200,})"',l):
            if len(q.split())>40: print("LONGQ",f,ln,len(q.split()),q[:60])
# process words
pat=re.compile(r"this draft|I checked|see Reviewer|during research|during this research|not interpreted here|read with pypdf|via pypdf|from the PDF|research is read-only|was not opened|were not opened|not read|bench-design|R019|R032|CP1|CK[123]",re.I)
for f in ["cloak_cols_a.md","cloak_cols_b.md","cloak_inventory.md"]:
    t=open(D+f,encoding='utf-8').read().split("## Reviewer notes")[0]
    for ln,l in enumerate(t.split("\n"),1):
        m=pat.findall(l)
        if m: print("PROC",f,ln,sorted(set(x.lower() for x in m)))
