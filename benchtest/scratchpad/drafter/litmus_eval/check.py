import sys,re
sys.path.insert(0,'benchtest')
import build_eval_sheet as B
p='benchtest/drafts/litmus_eval_tooling.md'
s=B.parse_md(p); print('sections',len(s))
t=open(p,encoding='utf-8').read()
body=t.split('## Reviewer notes')[0]
LAB=re.compile(r'\[(Documented(: [^\]]+)?|Inferred|To be verified|Not disclosed)\]')
sec=None;cnt={}
for line in body.splitlines():
    if line.startswith('## '): sec=line[3:]; continue
    if line.startswith('Summary:'):
        txt=re.sub(r'\*\*\[[^\]]+\]\*\*\s*$','',line[9:]).replace('**','')
        print(sec,'summary words',len(txt.split()), bool(re.search(r'\*\*\[[^\]]+\]\*\*\s*$',line)), '`' in line)
    if line.startswith('• ') and not LAB.search(line): print('NOLABEL',sec,line[:70])
    if line.startswith('|') and not line.startswith('|---') and not re.match(r'\| (Tool|Dataset|Result) ',line):
        last=line.replace(chr(92)+'|','~').split(' | ')[-1]
        if not LAB.search(last): print('ROW NOLABEL',line[:60])
for m in LAB.finditer(body):
    k=m.group(0).split(':')[0].strip('[]'); cnt[k]=cnt.get(k,0)+1
print(cnt)
for sec in ['Overview','Red-teaming','Engine coverage','Reuse for the test bench','Open questions']:
    seg=body.split('## '+sec)[1].split('\n## ')[0]
    print(sec,sum(1 for l in seg.splitlines() if l.startswith('• ')))
for sec in ['Tools','Datasets','Published results']:
    seg=body.split('## '+sec)[1].split('\n## ')[0]
    print(sec,sum(1 for l in seg.splitlines() if l.startswith('|'))-2)
