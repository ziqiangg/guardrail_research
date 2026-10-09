import subprocess, re, concurrent.futures as cf
rows=[l.rstrip('\n').split('\t') for l in open('urls.txt')]
def check(u):
    def curl(x):
        r=subprocess.run(['curl','-s','-o','/dev/null','-L','-w','%{http_code} %{url_effective}','--max-time','30','-A','Mozilla/5.0',x],capture_output=True,text=True)
        return r.stdout.strip()
    def curl_nofollow(x):
        r=subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}','--max-time','30','-A','Mozilla/5.0',x],capture_output=True,text=True)
        return r.stdout.strip()
    m=re.match(r'https://github.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)$',u)
    if m:
        raw=f'https://raw.githubusercontent.com/{m[1]}/{m[2]}/{m[3]}/{m[4]}'
        s=curl(raw); 
        if not s.startswith('200'): s2=curl(raw); s=s2
        return (u, 'raw '+s.split()[0], curl_nofollow(u))
    s=curl(u)
    if not s.startswith('200'): s=curl(u)
    return (u, s, curl_nofollow(u))
with cf.ThreadPoolExecutor(8) as ex:
    res=list(ex.map(lambda r: check(r[0]), rows))
with open('url_check.txt','w') as f:
    for (u,s,d),r in zip(res,rows):
        f.write(f'{s}\tdirect={d}\t{u}\t{r[1]}\n')
from collections import Counter
print(Counter(s.split()[0] if not s.startswith('raw') else 'raw '+s.split()[1] for u,s,d in res))
for u,s,d in res:
    if not (s.startswith('200') or s=='raw 200'): print(s,d,u)
