import re,collections
for name in ['cols_a','cols_b','inventory']:
    t=open(f'benchtest/drafts/modelarmor_{name}.md',encoding='utf-8').read()
    c=collections.Counter(re.findall(r'\[(Documented(?:: repo [^\]]+)?|Inferred|To be verified|Not disclosed|[^\]\[\n]{0,40})\]',t))
    std=('Documented','Inferred','To be verified','Not disclosed')
    print(name, {k:v for k,v in c.items() if k.startswith(std) or k in std})
    odd={k:v for k,v in c.items() if not k.startswith(std)}
    print(' non-label bracket pairs:', dict(list(odd.items())[:30]))
t=open('benchtest/drafts/modelarmor_inventory.md',encoding='utf-8').read().splitlines()
# inventory cell label check
tabs={}
cur=None
for i,l in enumerate(t,1):
    if l.startswith('## ('): cur=l[:6]
    if l.startswith('|') and not l.startswith('|---'):
        cells=[x.strip() for x in l.strip().strip('|').split('|')]
        tabs.setdefault(cur,[]).append((i,cells))
LAB=re.compile(r'\[(Documented|Inferred|To be verified|Not disclosed)')
for k,rows in tabs.items():
    hdr=rows[0][1]
    nolab=0; mixed=0; cells=0; total=0
    for i,c in rows[1:]:
        for j,x in enumerate(c):
            if hdr[j].startswith('Source URL') or hdr[j].startswith('Covered'): continue
            total+=1
            if not LAB.search(x): nolab+=1; print('  no label',k,i,hdr[j],x[:70])
            labs=set(LAB.findall(x))
            if len(labs)>1: mixed+=1
    print(k,'rows',len(rows)-1,'cells',total,'nolabel',nolab,'mixed-label cells',mixed)
# Inventory status GA [Inferred]
s=open('benchtest/drafts/modelarmor_inventory.md',encoding='utf-8').read()
print('GA [Inferred] (status rule S):',s.count('GA [Inferred] (status rule S)'))
print('To be verified in INV:', s.count('[To be verified]'))
