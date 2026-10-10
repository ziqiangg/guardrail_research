import re,sys,io,glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ops = ""
for f in glob.glob("benchtest/scratchpad/merger/purplellama/ops_*.py")+["benchtest/scratchpad/merger/purplellama/merge_pl.py"]:
    ops += open(f,encoding='utf-8').read()
ops_n = re.sub(r"\s+"," ",ops.replace("\'","'").replace('\\"','"'))
for line in open("benchtest/scratchpad/verifier/purplellama/diff_cols_out.txt",encoding='utf-8'):
    m = re.match(r"(PL\d R\d) ([+-]) (.*)", line)
    if not m: continue
    t = re.sub(r"\*\*\[.*?\]\*\*\s*$","",m.group(3)).strip()
    t = t.lstrip("• ").strip()
    found=None
    for k in (50,35,25):
        for st in (0, 20, 40):
            frag = t[st:st+k]
            if len(frag)==k and frag in ops_n: found=(st,k); break
        if found: break
    # find reason: the next string that looks like T\d+
    rsn=""
    if found:
        i = ops_n.find(t[found[0]:found[0]+found[1]])
        mm = re.search(r'"((?:T\d+|R0\d\d|style|Suppl|supplementary|hygiene|main)[^"]{0,120})"', ops_n[i:i+6000])
        rsn = mm.group(1) if mm else "?"
    print(m.group(1), m.group(2), "FOUND" if found else "NOT-IN-OPS", "|", t[:70], "|", rsn[:110])
