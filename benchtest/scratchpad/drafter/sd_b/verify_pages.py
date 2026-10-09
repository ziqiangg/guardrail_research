import re, sys, pathlib
D = pathlib.Path('/home/user/guardrail_research/benchtest/scratchpad/drafter/sd_b/pages')
CODE = pathlib.Path('/tmp/gcp_dlp_b/packages/google-cloud-dlp')
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
M = {
 'pseudonymization':'pseudo','transformations-reference':'transf','quickstart De-identify and re-identify sensitive data':'quickstart_deid',
 'concepts-method-types':'methodtypes','sensitive-data-protection-overview':'overview','REST projects.content.reidentify':'restreid',
 'REST projects.content.deidentify':'restdeid','REST projects.locations.content.reidentify':'restdeidconf','REST InspectConfig':'restconfig',
 'concepts-infotypes':'concepts_infotypes','roles and permissions':'roles','api-endpoints':'apiendpoints','auth':'auth','create-wrapped-key':'wrapped',
 'deidentify-sensitive-data':'deid','release-notes':'relnotes','likelihood':'likelihood','limits':'limits','concepts-image-redaction':'conceptsimg',
 'redacting-sensitive-data-images':'redimg','inspecting-images':'inspimg','infotypes-reference':'infotypes_ref','supported-file-types':'supported',
 'locations':'locations','REST projects.image.redact':'restimg','REST projects.locations.image.redact':'restlocimg','REST RedactImageResponse':'restredactresp',
 'REST InspectResult':'restfinding','REST organizations.deidentifyTemplates':'rest_deidtemplates','creating-custom-infotypes-rules':'rules',
 'Sensitive Data Protection pricing page':'pricing','Sensitive Data Protection SLA page':'sla','Model Armor overview page':'ma_overview',
 'Gemini Enterprise protect-sensitive-data page':'gemini'}
pages = {k: norm((D / (v + '.txt')).read_text(encoding='utf-8')) for k, v in M.items()}
CF = {'dlp_v2/types/dlp.py':'google/cloud/dlp_v2/types/dlp.py','dlp_v2/services/dlp_service/client.py':'google/cloud/dlp_v2/services/dlp_service/client.py','setup.py':'setup.py','README.rst':'README.rst','dlp/gapic_version.py':'google/cloud/dlp/gapic_version.py'}
code = {k: norm((CODE / v).read_text(encoding='utf-8')) for k, v in CF.items()}
bad = 0; checked = 0; noref = 0
parent = None
for i, ln in enumerate(open(sys.argv[1], encoding='utf-8').read().split('\n'), 1):
    if ln.startswith('• '): parent = ln
    elif ln.startswith('  – ') and parent: ln = ln + ' ' + parent  # inherit hints
    refs = []
    for m in re.finditer(r'\(SDP docs, (.+?) page, read 2026-10-09\)', ln): refs.append(('P', m.group(1)))
    for m in re.finditer(r'\((Sensitive Data Protection pricing page|Sensitive Data Protection SLA page|Model Armor overview page|Gemini Enterprise protect-sensitive-data page), read 2026-10-09\)', ln): refs.append(('P', m.group(1)))
    for m in re.finditer(r'([\w/\.]+)@google-cloud-dlp-v3\.40\.0:\d+', ln): refs.append(('C', m.group(1)))
    qs = re.findall(r'"([^"]{12,})"', ln.split(' • ')[0] if ln.startswith('  – ') else ln)
    if not qs: continue
    if not refs:
        noref += 1; print(f'L{i} quote without page or code hint: {qs[0][:60]}'); continue
    for q in qs:
        for p in [norm(x) for x in q.split('…') if len(x.strip()) >= 6]:
            checked += 1
            ok = any((pages.get(n) if k == 'P' else code.get(n)) and p in (pages.get(n) if k == 'P' else code.get(n)) for k, n in refs)
            if not ok:
                bad += 1; print(f'L{i} not in cited source(s) {[n for _, n in refs]}: {p[:100]}')
print(f'checked {checked}, bad {bad}, quotes without hint {noref}')
