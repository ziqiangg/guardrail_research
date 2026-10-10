import re, difflib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
D = "benchtest/drafts/"
def parse(path):
    cols = {}; col=None; row=None
    for line in open(path, encoding='utf-8').read().splitlines():
        m = re.match(r"^## Column (PL\d+):", line)
        if m: col=m.group(1); row=None; cols[col]={}; continue
        if line.startswith("## "): col=None; continue
        m = re.match(r"^### (R[1-9])\s*$", line)
        if m and col: row=m.group(1); cols[col][row]=[]; continue
        if col and row and line.strip(): cols[col][row].append(line.rstrip())
    return cols
orig = {}
orig.update(parse(D+"purplellama_cols_a.md")); orig.update(parse(D+"purplellama_cols_b.md"))
fin = parse(D+"purplellama_two_level.md")
log = open(D+"purplellama_changes.md", encoding='utf-8').read()
def norm(s):
    s = re.sub(r"\*\*|`", "", s); s = s.replace("…","").replace("...","")
    s = re.sub(r"^\s*(• |– |Summary: )", "", s.strip())
    return re.sub(r"\s+"," ",s).strip()
lognorm = norm(log.replace("\n"," "))
lognorm = re.sub(r"\s+"," ",re.sub(r"\*\*|`","",log)).replace("…","").replace("...","")
def inlog(s):
    n = norm(s)
    for k in (60,40,25):
        if len(n)>=k and n[:k] in lognorm: return f"p{k}"
    # try mid fragments
    for i in range(0, max(1,len(n)-40), 30):
        if n[i:i+40] in lognorm: return "mid"
    return None
tot_add=tot_rem=0; un=[]
for c in sorted(fin):
    for r in [f"R{i}" for i in range(1,10)]:
        a = orig.get(c,{}).get(r,[]); b = fin[c].get(r,[])
        sm = difflib.SequenceMatcher(None,a,b,autojunk=False)
        for op,i1,i2,j1,j2 in sm.get_opcodes():
            if op=="equal": continue
            for x in a[i1:i2]:
                tot_rem+=1
                if not inlog(x): un.append((c,r,"-",x))
            for x in b[j1:j2]:
                tot_add+=1
                if not inlog(x): un.append((c,r,"+",x))
print("added",tot_add,"removed",tot_rem,"unmatched",len(un))
for u in un: print(u[0],u[1],u[2],u[3][:330]); print()
