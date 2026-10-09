import sys, re
sys.path.insert(0, "/home/user/guardrail_research/benchtest/tools")
import fetch_text as F
url, pat = sys.argv[1], sys.argv[2]
st, final, ct, body = F.fetch(url)
print(st, final)
seen=set()
for m in re.finditer(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', body, re.S):
    h, t = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
    if re.search(pat, h, re.I) and (h,t) not in seen:
        seen.add((h,t)); print(h, '|', ' '.join(t.split())[:80])
