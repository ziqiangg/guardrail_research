import re,sys,collections,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
D='benchtest/drafts/'
files={'A':'purplellama_cols_a.md','B':'purplellama_cols_b.md','INV':'purplellama_inventory.md','EV':'purplellama_eval_tooling.md'}
BR=re.compile(r'\[([^\]\n]{1,80})\]')
ALLOWED=re.compile(r'^(Documented(: (repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)$')
for k,f in files.items():
    t=open(D+f,encoding='utf-8').read().split('\n')
    cnt=collections.Counter()
    odd=[]
    for i,l in enumerate(t,1):
        for m in BR.finditer(l):
            s=m.group(1)
            if ALLOWED.match(s):
                key=s if not s.startswith('Documented: repo') else 'Doc:repo '+s.split('@')[0][len('Documented: repo '):]
                cnt[key.split('@')[0]]+=1
            elif re.search(r'Documented|Inferred|verified|disclosed|^I$',s):
                odd.append((i,s))
    print(k,dict(cnt))
    print('  odd:',odd[:20])
# bullets with 2+ labels
LAB=re.compile(r'\[(Documented(?:: [^\]]+)?|Inferred|To be verified|Not disclosed)\]')
for k in ('A','B'):
    t=open(D+files[k],encoding='utf-8').read().split('\n')
    sec=None
    for i,l in enumerate(t,1):
        m=re.match(r'^## Column (PL\d)',l)
        if m: col=m.group(1)
        if l.startswith('• ') or l.startswith('Summary:'):
            ls=[x.group(0) for x in LAB.finditer(l)]
            bl=[x for x in ls if '**'+x+'**' in l]
            if len(bl)>1: print('MULTI',k,i,col,bl)
            if len(ls)>1 and l.startswith('• '): print('multi-nonbold',k,i,col,ls)
