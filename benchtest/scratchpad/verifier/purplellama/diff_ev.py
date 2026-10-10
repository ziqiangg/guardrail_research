import re,sys,io,difflib,glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
D="benchtest/drafts/"
a=open(D+"purplellama_eval_tooling.md",encoding='utf-8').read().splitlines()
b=open(D+"purplellama_eval_tooling_final.md",encoding='utf-8').read().splitlines()
log=re.sub(r"\s+"," ",open(D+"purplellama_changes.md",encoding='utf-8').read())
ops=""
for f in glob.glob("benchtest/scratchpad/merger/purplellama/ops_*.py")+["benchtest/scratchpad/merger/purplellama/merge_pl.py"]: ops+=open(f,encoding='utf-8').read()
ops=re.sub(r"\s+"," ",ops.replace("\'","'").replace('\\"','"').replace("\\|","\|"))
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
add=rem=0
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=="equal": continue
    rem+=i2-i1; add+=j2-j1
    for i,new in enumerate(b[j1:j2]):
        old = a[i1+i] if i1+i<i2 else ""
        s2=difflib.SequenceMatcher(None,old,new,autojunk=False)
        for o,x1,x2,y1,y2 in s2.get_opcodes():
            if o in("replace","insert") and y2-y1>=15:
                f=new[y1:y2].strip().lstrip(". ;").strip()
                g=f[:35]
                if len(g)>=15 and g not in log and g not in ops:
                    g2=f[10:45]
                    if g2 not in log and g2 not in ops:
                        print("UNMATCHED L%d"%(j1+i+1), "|", f[:220])
print("added",add,"removed",rem)
