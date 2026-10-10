import re, glob, sys
S = 'benchtest/scratchpad/drafter/cloak_inv/'


def norm(t):
    t = t.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"').replace(' ', ' ')
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = t.replace('**', '').replace('`', '')
    t = re.sub(r'\\([<>_*])', r'\1', t)
    t = re.sub(r'<br\s*/?>', ' ', t)
    t = re.sub(r'^\s*[-*>#|]+\s*', '', t, flags=re.M)
    return re.sub(r'\s+', ' ', t)


corp = ''
files = glob.glob(S + 'docs/*') + glob.glob(S + 'portal/*.txt') + [S + 'cloak_home.txt', S + 'mirage.txt', S + 'pdf/terms.txt', S + 'pdf/privacy.txt', S + 'owners/spacy_lic.txt', S + 'owners/pcd_lic.txt', S + 'owners/pycrypto_pypi.txt']
for f in files:
    corp += ' ' + norm(open(f, encoding='utf-8', errors='replace').read())
corp2 = re.sub(r'\s*\|\s*', ' ', corp)
txt = open('benchtest/drafts/cloak_inventory.md', encoding='utf-8').read()
bad = 0
n = 0
for m in re.finditer(r'"([^"]{12,}?)"', txt):
    q = norm(m.group(1))
    for seg in re.split(r'\s*(?:\.\.\.|…)\s*', q):
        seg = seg.strip().rstrip('.,;')
        if len(seg.split()) < 3:
            continue
        n += 1
        if seg in corp or seg in corp2 or seg.lower() in corp.lower():
            continue
        bad += 1
        print('MISS:', seg[:160])
print(n, 'segments', bad, 'missing')
