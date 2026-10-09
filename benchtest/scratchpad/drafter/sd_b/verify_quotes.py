import re, sys, glob, pathlib
D = pathlib.Path('/home/user/guardrail_research/benchtest/scratchpad/drafter/sd_b/pages')
CODE = pathlib.Path('/tmp/gcp_dlp_b/packages/google-cloud-dlp')
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
corpus = {}
for f in D.glob('*.txt'):
    corpus[f.name] = norm(f.read_text(encoding='utf-8'))
for f in ['google/cloud/dlp_v2/types/dlp.py', 'google/cloud/dlp_v2/services/dlp_service/client.py', 'setup.py', 'README.rst', 'google/cloud/dlp/gapic_version.py']:
    corpus['CODE:' + f] = norm((CODE / f).read_text(encoding='utf-8'))
alltext = ' || '.join(corpus.values())
# raw code lines for cite check
rawcode = {f: (CODE / f).read_text(encoding='utf-8').split('\n') for f in ['google/cloud/dlp_v2/types/dlp.py', 'google/cloud/dlp_v2/services/dlp_service/client.py', 'setup.py', 'README.rst', 'google/cloud/dlp/gapic_version.py']}
short = {'dlp_v2/types/dlp.py': 'google/cloud/dlp_v2/types/dlp.py', 'dlp_v2/services/dlp_service/client.py': 'google/cloud/dlp_v2/services/dlp_service/client.py', 'setup.py': 'setup.py', 'README.rst': 'README.rst', 'dlp/gapic_version.py': 'google/cloud/dlp/gapic_version.py'}
path = sys.argv[1]
bad = 0; nq = 0; longq = 0
for i, ln in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
    if ln.startswith('• https://') or ln.startswith('## Reviewer'):
        continue
    for q in re.findall(r'"([^"]{12,})"', ln):
        nq += 1
        parts = [norm(p) for p in re.split(r'…', q) if len(p.strip()) >= 6]
        for p in parts:
            if p not in alltext:
                bad += 1; print(f'L{i} NOT FOUND: {p[:110]}')
        if len(q.split()) >= 40:
            longq += 1; print(f'L{i} QUOTE >= 40 words ({len(q.split())}): {q[:70]}')
    # code cites: file@tag:line ; check that quoted text inside same bullet appears on/near that line when the quote is from code
    for m in re.finditer(r'([\w/\.]+)@google-cloud-dlp-v3\.40\.0:(\d+)', ln):
        f, n = m.group(1), int(m.group(2))
        if f not in short: print(f'L{i} unknown cite file {f}'); bad += 1; continue
        raw = rawcode[short[f]]
        if n < 1 or n > len(raw): print(f'L{i} cite out of range {f}:{n}'); bad += 1
print(f'quotes checked: {nq}; problems: {bad}; long: {longq}')
