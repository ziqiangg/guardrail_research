import re,glob
s=open('benchtest/drafts/cloak_cols_a.md',encoding='utf-8').read()
D='benchtest/scratchpad/drafter/cloak_cols_a/'
src=''
for f in glob.glob(D+'docs/*')+glob.glob(D+'*.txt')+glob.glob(D+'pdf/*.txt'):
    src+=open(f,encoding='utf-8',errors='ignore').read()+'\n'
def norm(t):
    t=t.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')
    t=' '.join(t.replace('*',' ').replace('`',' ').replace(chr(92),' ').split())
    return t.lower()
N=norm(src)
bad=0
for l in s.split('## Reviewer notes')[0].splitlines():
    if not l.startswith('\u2022'): continue
    for q in re.findall(r'"([^"]{14,})"',l):
        for x in q.split('\u2026'):
            x=norm(x).strip(' .;,')
            if len(x)>10 and x not in N:
                bad+=1; print('MISS:',x[:110])
print('misses',bad)
