import re
D="benchtest/drafts/"
def norm(s):
    s = s.replace("**", "").replace("`", "").replace("\\|", "|").replace("read 2026-10-09","2026-10-09")
    s = re.sub(r"^\s*(•|–)\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()
res = norm(open(D+"modelarmor_resolutions_1.md",encoding="utf-8").read()+" "+open(D+"modelarmor_resolutions_2.md",encoding="utf-8").read())
res = res.replace("37f936ac","modelarmor/v1.3.0")
out=[]
for line in open("benchtest/scratchpad/verifier/modelarmor/unlogged_g.txt",encoding="utf-8"):
    loc, x = line.split(": ",1)
    t = norm(x)
    hit = any(len(t[s:s+40])>=25 and t[s:s+40] in res for s in (0,10,30,60,100))
    if not hit: out.append(line.rstrip())
print(len(out))
open("benchtest/scratchpad/verifier/modelarmor/not_in_res.txt","w",encoding="utf-8").write("\n".join(out))
