import re,glob,sys,subprocess
base='benchtest/scratchpad/drafter/cloak_cols_b/'
corpus=''
for f in glob.glob(base+'docs/*.md')+glob.glob(base+'portal/*.txt')+[base+'terms.txt',base+'usenix.txt',base+'pb_45908b48c0a8b6d3855a154c0e41a12958a99205.mdx']:
    corpus+=open(f,encoding='utf-8',errors='replace').read()+'\n'
home=subprocess.run(['python','benchtest/tools/fetch_text.py','https://www.cloak.gov.sg'],capture_output=True,text=True,encoding='utf-8').stdout
corpus+=home
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    s=re.sub(r'\*\*|`|[\\]','',s)
    s=re.sub(r'\]\([^)]*\)','',s); s=re.sub(r'\]\[#\]','',s); s=s.replace('[','').replace(']','').replace('⚠️','').replace('> ',' ')
    s=re.sub(r'<br>',' ',s)
    s=re.sub(r'\s+',' ',s)
    return s.lower()
C=norm(corpus)
# remove pipes/table spacing variants
C2=C.replace(' | ',' ')
txt=open('benchtest/drafts/cloak_cols_b.md',encoding='utf-8').read()
bad=0
for i,ln in enumerate(txt.splitlines(),1):
    if not ln.startswith('•') and not ln.startswith('  –'): continue
    for q in re.findall(r'"([^"]{6,})"',ln):
        for part in q.split('…'):
            p=norm(part).strip(' .,;')
            if len(p)<6: continue
            if p in C or p in C2 or p.replace(' | ',' ') in C2: continue
            print(f'L{i} NOT FOUND: {q[:140]}'); bad+=1
print('missing',bad)
