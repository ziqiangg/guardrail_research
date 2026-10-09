import re,sys
cols={};cur=None;row=None
for line in open("benchtest/drafts/modelarmor_two_level.md",encoding="utf-8"):
    line=line.rstrip("\n")
    m=re.match(r"^## Column (MA\d+):",line)
    if m: cur=m.group(1); cols[cur]={}; continue
    m=re.match(r"^### R(\d)\s*$",line)
    if m: row=int(m.group(1)); cols[cur][row]=[]; continue
    if cur and row: cols[cur][row].append(line)
for a in sys.argv[1:]:
    c,r=a.split(":")
    print(f"===== {c} R{r}")
    for l in cols[c][int(r)]:
        if l.strip(): print(l[:int(sys.argv[0] and 600)])
