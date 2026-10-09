import re,sys
sys.path.insert(0,'benchtest/scratchpad/merger/modelarmor')
import lib
C,_=lib.parse_cols('benchtest/drafts/modelarmor_two_level.md')
# repo labels vs R9
for c,d in C.items():
    r9=" ".join(d['rows'][9]['detail'])
    body=" ".join(" ".join(d['rows'][n]['detail']) for n in range(1,8))
    for m in set(re.findall(r"\[Documented: repo ([^@\]]+)@([^\]]+)\]",body)):
        repo,ref=m
        ok = (repo in r9 or repo.split('/')[-1] in r9) and ref in r9
        if not ok: print("R9 MISSING for",c,repo,ref)
# duplicate bullets inside a row
for c,d in C.items():
    for n,r in d['rows'].items():
        seen={}
        for l in r['detail']:
            if l.startswith('• '):
                k=l
                if k in seen: print("DUP",c,n,l[:80])
                seen[k]=1
# URLs in R1-R8 text that are not in R9 (docs/github urls)
for c,d in C.items():
    r9=set(l[2:].strip() for l in d['rows'][9]['detail'])
    for n in range(1,9):
        for l in d['rows'][n]['detail']:
            for u in re.findall(r"https?://[^\s)]+",l):
                if u not in r9 and not u.startswith("https://modelarmor"):
                    print("URL not in R9",c,n,u)
