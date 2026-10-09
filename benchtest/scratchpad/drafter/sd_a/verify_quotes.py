import re,glob,sys,os
W='/home/user/guardrail_research/benchtest/scratchpad/drafter/sd_a/'
corp=[]
def norm(s): return re.sub(r'\s+',' ',s)
files=glob.glob(W+'*.txt')+glob.glob('/tmp/gcp_dlp_a/packages/google-cloud-dlp/google/cloud/dlp_v2/types/*.py')+['/tmp/gcp_dlp_a/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py','/tmp/gcp_dlp_a/packages/google-cloud-dlp/setup.py','/tmp/gcp_dlp_a/packages/google-cloud-dlp/README.rst','/tmp/gcp_dlp_a/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py','/tmp/gcp_dlp_a/packages/google-cloud-dlp/CHANGELOG.md']
big=[]
for f in files:
    t=open(f,encoding='utf-8',errors='ignore').read()
    big.append(norm(t))
    big.append(norm(re.sub(r'\s*\n\|\s*',' | ',t)))
    big.append(norm(re.sub(r'\s*\n\|?\s*\n',' ',t)))
B='\n'.join(big)
bad=0;n=0
for fn in sys.argv[1:]:
    for i,l in enumerate(open(fn,encoding='utf-8'),1):
        if not (l.startswith('• ') or l.startswith('  – ')): continue
        for m in re.finditer(r'"([^"]{6,})"',l):
            q=m.group(1)
            for frag in [x.strip() for x in q.split('…') if x.strip()]:
                n+=1
                f2=norm(frag).strip(' .,;:')
                if f2 not in B:
                    bad+=1; print(os.path.basename(fn),i,'NOT FOUND:',frag[:140])
print('checked',n,'bad',bad)
