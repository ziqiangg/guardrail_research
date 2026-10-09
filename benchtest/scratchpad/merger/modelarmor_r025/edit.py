import re, io
P="benchtest/drafts/modelarmor_two_level.md"
t=open(P,encoding="utf-8").read()
parts=re.split(r"(?m)^(?=## Column )",t)
Q='"Customer should not use Pre-GA Offerings to process personal data or other data subject to legal or regulatory compliance requirements"'
def bullet(here):
    return ("• Bench rule (user, 2026-10-09): Preview features are tested with synthetic data only, because the Pre-GA Offerings Terms advise against processing personal data "
            f"({here}); the terms say {Q} (Google Cloud General Service Terms, 2026-10-09) **[Documented]**\n")
hints={"MA1":"here the Preview feature is template exclusion rules","MA2":"here the Preview feature is template exclusion rules","MA3":"here the Preview feature is template exclusion rules","MA4":"here the Preview feature is template exclusion rules",
"MA7":"template exclusion rules are Preview but list this filter as unsupported","MA8":"template exclusion rules are Preview but list this filter as unsupported",
"MA9":"here the Preview feature is the LangChain integration; document screening itself carries no Preview label","MA10":"here the Preview feature is image screening"}
log=[]
out=[]
for p in parts:
    m=re.match(r"## Column (MA\d+):",p)
    if m and m.group(1) in hints:
        cid=m.group(1)
        i=p.index("\n### R7"); j=p.index("\n### R8")
        r7=p[i:j+1]
        if cid=="MA10":
            old="• Image tests should use synthetic images only, because the Pre-GA terms in R4 advise against processing personal data in Pre-GA Offerings **[Inferred]**\n"
            assert old in r7
            r7=r7.replace(old,bullet(hints[cid])); log.append((cid,"replaced"))
        else:
            r7=r7+bullet(hints[cid]); log.append((cid,"added"))
        p=p[:i]+r7+p[j+1:]
        if cid=="MA9":
            k=p.index("\n### R9"); 
            assert "service-terms" not in p[k:]
            p=p.rstrip("\n")+"\n• https://cloud.google.com/terms/service-terms\n"
            if parts.index(p) if False else False: pass
            log.append((cid,"R9 url added"))
    out.append(p)
res="".join(out)
open(P,"w",encoding="utf-8",newline="").write(res)
print(log)
