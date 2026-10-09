import re,sys
LAB=re.compile(r"\*\*\[(Documented(: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*\s*$")
bad=0
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip() or line.startswith('#'): continue
    i,row,s=line.split('|',2)
    body=LAB.sub('',s).strip()
    words=len(re.sub(r'\*\*','',body).split())
    limit=60 if row=='7' and i.endswith('R7') else 45
    ok=words<=limit and s.count('**')%2==0 and not re.search(r'[`_$]',s)
    if i.endswith('R7'): ok = ok and ('**Minimum setup:**' in s)
    if i.endswith('R8'): ok = ok and s.startswith('**Key open questions.**') and not LAB.search(s)
    elif not LAB.search(s) and not i.endswith('R9'): ok=False
    print(('OK  ' if ok else 'FAIL'),i,words,'/',limit)
    bad+= (not ok)
print('fail count',bad)
