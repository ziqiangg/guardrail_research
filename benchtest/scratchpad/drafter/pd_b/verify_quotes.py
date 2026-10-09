import re,glob,os
corpus=''
for f in glob.glob('/home/user/guardrail_research/benchtest/scratchpad/drafter/pd_b/pages/*.txt'):
    corpus+=open(f,encoding='utf-8',errors='replace').read()+'\n'
for root in ['/tmp/presidio_probe/docs','/tmp/presidio_probe/presidio-image-redactor','/tmp/presidio_probe/presidio-structured','/tmp/presidio_probe/presidio-analyzer','/tmp/presidio_probe/presidio-anonymizer']:
    for dp,dn,fn in os.walk(root):
        if '.git' in dp or 'node_modules' in dp: continue
        for f in fn:
            if f.endswith(('.py','.md','.yaml','.yml','.toml','.sh','Dockerfile','.ipynb')) or f=='Dockerfile':
                try: corpus+=open(os.path.join(dp,f),encoding='utf-8',errors='replace').read()+'\n'
                except: pass
for f in ['CHANGELOG.md','LICENSE','README.MD']:
    corpus+=open('/tmp/presidio_probe/'+f,encoding='utf-8').read()+'\n'
# add notebook sources (joined cell text)
import json
for f in glob.glob('/tmp/presidio_probe/docs/samples/python/*.ipynb'):
    try:
        nb=json.load(open(f)); corpus+='\n'.join(''.join(c['source']) for c in nb['cells'])+'\n'
    except: pass
def norm(x):
    x=x.replace('\\"','"').replace('**','').replace('`','')
    return re.sub(r'\s+',' ',x).strip()
C=norm(corpus)
bad=0
for ln in open('/home/user/guardrail_research/benchtest/drafts/presidio_cols_b.md',encoding='utf-8'):
    if not ln.startswith('• '): continue
    t=re.sub(r'`[^`]*`',lambda m:m.group(0),ln)
    for q in re.findall(r'"([^"]{12,})"',ln):
        parts=[norm(p) for p in re.split(r'…',q) if len(p.strip())>6]
        for p in parts:
            if p not in C:
                bad+=1; print('NOT FOUND:',p[:140])
print('done, missing:',bad)
