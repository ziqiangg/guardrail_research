import re,glob,sys
base='benchtest/scratchpad/drafter/ma_b/'
raw=''
for f in glob.glob(base+'*.txt'):
    raw+=' '+open(f,encoding='utf-8',errors='replace').read()
raw+=' '+open(base+'gcgo/modelarmor/apiv1/modelarmorpb/service.pb.go',encoding='utf-8').read()
def norm(t):
    t=t.replace('“','"').replace('”','"').replace('’',"'")
    return re.sub(r'\s+',' ',t)
R=norm(raw)
# remove leading '| ' table markers variant: also create version with ' | ' removed
R2=R.replace(' | ',' ')
txt=open('benchtest/drafts/modelarmor_cols_b.md',encoding='utf-8').read()
miss=0;tot=0
for i,l in enumerate(txt.split('\n'),1):
    if not l.startswith(('•','  –')): continue
    l2=re.sub(r'`[^`]*`','',l)
    for m in re.finditer(r'"([^"]{8,})"',l2):
        q=norm(m.group(1)).strip().rstrip('.,;')
        tot+=1
        qs=re.split(r'…|\.\.\.',q)
        ok=all(part.strip() in R or part.strip() in R2 for part in qs)
        if not ok:
            miss+=1; print('MISS L%d: %s'%(i,q))
print('quotes',tot,'miss',miss)
