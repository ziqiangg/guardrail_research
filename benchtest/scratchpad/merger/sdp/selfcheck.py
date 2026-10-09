import re, sys, json
sys.path.insert(0,'/home/user/guardrail_research/benchtest/scratchpad/merger/sdp')
ROOT='/home/user/guardrail_research/benchtest/drafts/'
LABEL=r"\[(?:Documented(?:: (?:repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)\]"
BOLD=re.compile(r"\*\*"+LABEL+r"\*\*\s*$")
def words(s):
    s=re.sub(r"\*\*"+LABEL+r"\*\*\s*$","",s).replace("**","")
    return len(s.split())
def parse(path):
    cols=[];cur=None;rn=None;mode=None
    for ln in open(path,encoding='utf-8').read().split('\n'):
        m=re.match(r"^## Column (SD\d+): (.+)$",ln)
        if m: cur={'id':m.group(1),'header':m.group(2),'R':{}};cols.append(cur);rn=None;continue
        m=re.match(r"^### R([1-9])\s*$",ln)
        if m and cur: rn=int(m.group(1));cur['R'][rn]={'s':None,'d':[]};mode=None;continue
        if cur is None or rn is None: continue
        if ln.startswith('Summary: '): cur['R'][rn]['s']=ln[9:].strip()
        elif ln.strip()=='Detail:': mode='d'
        elif mode=='d' and (ln.startswith('• ') or ln.startswith('  – ')): cur['R'][rn]['d'].append(ln)
    return cols
if __name__=='__main__':
    cols=parse(ROOT+'sdp_two_level.md')
    out={}
    # pins
    pin_problems=[];dup=[]
    lab_counts={}
    for c in cols:
        r9=[l[2:].strip() for l in c['R'][9]['d'] if l.startswith('• ')]
        if len(r9)!=len(set(r9)): dup.append(c['id'])
        for n in range(1,9):
            for l in c['R'][n]['d']:
                for m in re.finditer(r"\[Documented: repo ([^@\]]+)@([^\]]+)\]",l):
                    repo,ref=m.groups()
                    if not any(ref in u and 'google-cloud-python' in u for u in r9):
                        pin_problems.append((c['id'],n,ref))
                for m in re.finditer(LABEL,l):
                    lab_counts[m.group(0)]=lab_counts.get(m.group(0),0)+1
    print('pin problems:',pin_problems)
    print('R9 duplicates:',dup)
    print('labels in Detail:',lab_counts)
    # summary stats
    over=[];nolabel=[]
    tot=0
    for c in cols:
        for n in range(1,10):
            s=c['R'][n]['s'];tot+=1
            lim=60 if n==7 else 45
            if words(s)>lim: over.append((c['id'],n,words(s)))
            if n<=7 and not BOLD.search(s): nolabel.append((c['id'],n))
    print('summaries:',tot,'over limit:',over,'missing label:',nolabel)
    # R9 bullets: every repo blob URL tag
    for c in cols:
        bad=[l for l in c['R'][9]['d'] if 'github.com/googleapis' in l and 'google-cloud-dlp-v3.40.0' not in l]
        if bad: print('bad R9 url',c['id'],bad)
    print('bullets per column:',{c['id']:sum(len(c['R'][n]['d']) for n in range(1,10)) for c in cols})
