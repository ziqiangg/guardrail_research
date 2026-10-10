import re
for f in ['litmus_eval_tooling','litmus_inventory']:
    L=open(f'benchtest/drafts/{f}.md',encoding='utf-8').read().split('\n')
    print('==',f)
    for i,l in enumerate(L,1):
        for m in re.finditer(r'\b(analyz\w*|behavior\w*|color\w*|organiz\w*|license\b|licensing|favor\w*|center\w*|catalog\b|defense|prioritiz\w*|recogniz\w*|summariz\w*|normaliz\w*|customiz\w*|minimiz\w*)',l,re.I):
            print(' US?',i,m.group(0))
    for i,l in enumerate(L,1):
        for m in re.finditer(r'"([^"]{20,})"',l):
            n=len(m.group(1).split())
            if n>=30 and n<80: print(' quote',i,n,m.group(1)[:60])
    mx=[]
    for i,l in enumerate(L,1):
        if l.startswith('|'):
            for c in l.replace('\|','/').split('|')[1:-1]:
                mx.append((len(c),i))
    mx.sort(reverse=True); print(' max cells',mx[:6])
    lim=150 if 'eval' in f else 43
    for i,l in enumerate(L,1):
        if i>lim: break
        for m in re.finditer(r'\b(R0\d\d|this draft|Reviewer notes?|brief|checkpoint)\b',l):
            print(' proc',i,m.group(0))
