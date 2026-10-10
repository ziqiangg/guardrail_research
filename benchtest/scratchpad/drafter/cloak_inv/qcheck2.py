import re
src = open('benchtest/scratchpad/drafter/cloak_inv/qcheck.py', encoding='utf-8').read().split("txt = open")[0]
exec(src)
corp += ' ' + norm(open('benchtest/scratchpad/drafter/cloak_inv/owners/spacy_en.txt', encoding='utf-8').read())
txt = open('benchtest/drafts/cloak_inventory.md', encoding='utf-8').read()
bad = n = 0
for ln in txt.splitlines():
    cells = ln.split(' | ') if ln.startswith('|') else [ln]
    for c in cells:
        if c.count('"') % 2:
            print('ODD:', c[:100])
        for m in re.finditer(r'"([^"]{8,}?)"', c):
            q = norm(m.group(1))
            for seg in re.split(r'\s*(?:\.\.\.|…)\s*', q):
                seg = seg.strip().rstrip('.,;')
                if len(seg.split()) < 3:
                    continue
                n += 1
                if seg in corp or seg in corp2 or seg.lower() in corp.lower():
                    continue
                bad += 1
                print('MISS:', seg[:170])
print(n, bad)
