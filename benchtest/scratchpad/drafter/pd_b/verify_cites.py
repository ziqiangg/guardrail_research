import re, sys, os
ROOT='/tmp/presidio_probe/'
txt=open('/home/user/guardrail_research/benchtest/drafts/presidio_cols_b.md',encoding='utf-8').read().splitlines()
cols=[]; cur=None
for ln in txt:
    if ln.startswith('## Column'): cur={'name':ln[:12],'lines':[],'urls':[]}; cols.append(cur)
    elif ln.startswith('## '): cur=None
    elif cur is not None:
        cur['lines'].append(ln)
        m=re.match(r'^• (https://github.com/data-privacy-stack/presidio/blob/2.2.364/(\S+))$',ln)
        if m: cur['urls'].append(m.group(2))
cite=re.compile(r'([A-Za-z0-9_./-]+\.(?:py|md|yaml|yml|toml|sh|json|MD)|Dockerfile|LICENSE)@2\.2\.364((?::\d+(?:-\d+)?(?:,? (?:and )?)?)+)')
for c in cols:
    print('=====',c['name'])
    for ln in c['lines']:
        for m in cite.finditer(ln):
            base=m.group(1)
            cands=[u for u in c['urls'] if u==base or u.endswith('/'+base)]
            if not cands:
                print('!! no url for',base); continue
            if len(cands)>1:
                # prefer exact path match
                ex=[u for u in cands if u==base]
                cands=ex or cands
                if len(cands)>1: print('?? ambiguous',base,cands)
            path=cands[0]
            if not os.path.exists(ROOT+path): print('!! missing file',path); continue
            lines=open(ROOT+path,encoding='utf-8',errors='replace').read().splitlines()
            for r in re.finditer(r':(\d+)(?:-(\d+))?',m.group(2)):
                a=int(r.group(1)); b=int(r.group(2) or a)
                if b>len(lines): print('!! out of range',path,a,b,len(lines)); continue
                seg=' | '.join(l.strip() for l in lines[a-1:min(b,a+2)])[:150]
                print(f'{base}:{a}-{b}  {seg}')
