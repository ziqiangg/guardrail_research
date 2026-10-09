import re,sys
def norm(s):
    s=s.replace('“','"').replace('”','"').replace('’',"'").replace('‘',"'")
    s=re.sub(r'[*`_#|>\[\]\(\)]',' ',s)
    s=re.sub(r'\s+',' ',s).strip().lower()
    return s
repo=open(sys.argv[1],encoding='utf-8').read()
hf=open(sys.argv[2],encoding='utf-8').read()
hfn=norm(hf)
miss=[]
tot=0
for line in repo.split('\n'):
    # split into sentences
    for sent in re.split(r'(?<=[.!?:])\s+',line):
        n=norm(sent)
        if len(n)<25: continue
        tot+=1
        if n not in hfn:
            miss.append(sent[:160])
print('sentences',tot,'missing in HF text',len(miss))
for m in miss[:60]: print(' -',m)
