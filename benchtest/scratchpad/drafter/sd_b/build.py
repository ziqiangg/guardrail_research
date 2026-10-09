"""Resolve {{L:file|needle|nth}} code cites and {{D:page}} / {{M:..}} hints in template.md -> sdp_cols_b.md"""
import re, sys, pathlib
ROOT = pathlib.Path('/tmp/gcp_dlp_b/packages/google-cloud-dlp')
TAG = 'google-cloud-dlp-v3.40.0'
FILES = {
    'T': ('google/cloud/dlp_v2/types/dlp.py', 'dlp_v2/types/dlp.py'),
    'C': ('google/cloud/dlp_v2/services/dlp_service/client.py', 'dlp_v2/services/dlp_service/client.py'),
    'S': ('setup.py', 'setup.py'),
    'R': ('README.rst', 'README.rst'),
    'G': ('google/cloud/dlp/gapic_version.py', 'dlp/gapic_version.py'),
}
cache = {}
def lines(k):
    if k not in cache:
        cache[k] = (ROOT / FILES[k][0]).read_text(encoding='utf-8').split('\n')
    return cache[k]
def cite(m):
    k, needle, nth = m.group(1), m.group(2), int(m.group(3) or 1)
    hits = [i + 1 for i, l in enumerate(lines(k)) if needle in l]
    if len(hits) < nth:
        sys.exit(f'NO MATCH {k} {needle!r} nth={nth} hits={hits}')
    return f'{FILES[k][1]}@{TAG}:{hits[nth-1]}'
def doc(m):
    return f'(SDP docs, {m.group(1)} page, read 2026-10-09)'
def other(m):
    return f'({m.group(1)}, read 2026-10-09)'
t = pathlib.Path('/home/user/guardrail_research/benchtest/scratchpad/drafter/sd_b/template.md').read_text(encoding='utf-8')
t = re.sub(r'\{\{L:([A-Z])\|([^|}]+)(?:\|(\d+))?\}\}', cite, t)
t = re.sub(r'\{\{D:([^}]+)\}\}', doc, t)
t = re.sub(r'\{\{O:([^}]+)\}\}', other, t)
if '{{' in t:
    sys.exit('unresolved placeholder: ' + re.search(r'\{\{[^}]*\}\}', t).group(0))
pathlib.Path('/home/user/guardrail_research/benchtest/drafts/sdp_cols_b.md').write_text(t, encoding='utf-8')
print('written', len(t.split('\n')), 'lines')
