import re, collections, importlib.util, sys
spec = importlib.util.spec_from_file_location('items', 'benchtest/scratchpad/triager/modelarmor_items.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
ITEMS = M.ITEMS
ID = {it['key']: 'T%d' % (i + 1) for i, it in enumerate(ITEMS)}
assert len(ID) == len(ITEMS), 'duplicate key'

def ref(s):
    def r(m):
        k = m.group(1)
        if k not in ID:
            raise KeyError(k)
        return ID[k]
    return re.sub(r'\{k:(\w+)\}', r, s)

def files(it):
    t = it['loc'] + ' ' + it['item']
    f = set()
    for n in re.findall(r'\bMA(\d+)\b', it['loc']):
        n = int(n)
        f.add('A' if n in (1, 2, 3, 4, 7, 8) else 'B')
    if re.search(r'\bA RN-', it['loc']):
        f.add('A')
    if re.search(r'\bB RN', it['loc']):
        f.add('B')
    if 'INV' in it['loc']:
        f.add('INV')
    return f

for it in ITEMS:
    it['files'] = files(it)

n = len(ITEMS)
cls = collections.Counter(it['cls'] for it in ITEMS)
pri = collections.Counter(it['pri'] for it in ITEMS)
cp = collections.Counter((it['cls'], it['pri']) for it in ITEMS)
hg = sum(1 for it in ITEMS if it['hg'])
hg_cls = collections.Counter(it['cls'] for it in ITEMS if it['hg'])
perfile = {f: collections.Counter(it['cls'] for it in ITEMS if f in it['files']) for f in ('A', 'B', 'INV')}
perfile_n = {f: sum(perfile[f].values()) for f in perfile}
perfile_h = {f: sum(1 for it in ITEMS if f in it['files'] and it['pri'] == 'H') for f in perfile}
nofile = [ID[it['key']] for it in ITEMS if not it['files']]

# R8 bullet mapping (column -> list of keys); 102 bullets
R8 = collections.OrderedDict([
 ('MA1 (9)', 'model_id, rai_default, conf_meaning, accuracy, lang, csam_doc/csam_test, topic, latency, ocr_doc'),
 ('MA2 (11)', 'model_id, rai_default, conf_meaning, ip_sample, accuracy, userprompt_effect, lang, csam_doc, topic, resp_files, latency'),
 ('MA3 (11)', 'model_id, pi_level_test, pi_default, conf_meaning, accuracy, pi_taxonomy, ocr_doc, excl_schema, skipped_regions/lang, rn1010, latency'),
 ('MA4 (10)', 'model_id, pi_resp_doc/pi_resp_test, pi_level_test, pi_default, three_word, accuracy, userprompt_effect, excl_schema, tool_json, latency'),
 ('MA7 (9)', 'url_source, url_variants, url_order, accuracy, url_source, ocr_doc, useast7, url_input, latency'),
 ('MA8 (10)', 'url_source, url_variants, url_order, url_stream, accuracy, url_source, userprompt_effect, ocr_doc, useast7, latency'),
 ('MA5 (10)', 'basic_count_doc/basic_count_test, us_regions, findings_with_deid, deid_inspect_only, floor_adv, sdp_quota/latency, filterresults_shape, likelihood/accuracy, limit_int, sdp_quota'),
 ('MA6 (9)', 'basic_resp, sdp_resp_result, userprompt_effect, deid_forward, apigee_status, mcp_status, sdp_quota/latency, deid_inspect_only, accuracy'),
 ('MA9 (11)', 'resp_files, extractor, oversize, embedded_doc/embedded_test, antivirus, ge_modal, file_tokens, formats, rich_doc, langchain, file_result'),
 ('MA10 (12)', 'resp_files, ocr_doc/ocr_test, csam_pixels, ocr_lang, formats, file_tokens, include_findings, deid_inspect_only, bbox, embedded_doc, ge_modal, image_ga'),
])
R8_TXT = []
unmapped = set()
for c, ks in R8.items():
    ids = []
    for part in [p.strip() for p in ks.split(',')]:
        sub = [ID[x] for x in part.split('/')]
        ids.append('/'.join(sub))
    R8_TXT.append('%s to %s' % (c, ', '.join(ids)))

def rows():
    out = []
    for it in ITEMS:
        t = ID[it['key']]
        c = it['cls']
        if it['hg']:
            c = c + ' (honest gap)'
        out.append('| %s | %s | %s | %s | %s | %s |' % (t, ref(it['item']), ref(it['loc']), c, ref(it['src']), it['pri']))
    return '\n'.join(out)

H_ITEMS = [it for it in ITEMS if it['pri'] == 'H']

md = []
w = md.append
w('# Model Armor triage of open evidence items (DRAFT)')
w('')
w('Sources triaged: `modelarmor_cols_a.md` (MA1 to MA4, MA7, MA8), `modelarmor_cols_b.md` (MA5, MA6, MA9, MA10), `modelarmor_inventory.md` (sheet 3x: tables (a) filters 10 rows, (b) integration paths 15, (c) template and floor-setting parameters 16, (d) locations 18, (e) quotas, limits and pricing 16), the brief `modelarmor_brief.md` (scope, conflicts C1 to C13, gaps G1 to G12), the three Reviewer-notes sections, `scratchpad/explorer/20261009_modelarmor_p0.md` and `_q01.md`, rulings R002, R007, R009, R011, R012, R013, R014, and `scratchpad/main/queue.md` (P2 questions routed to triage). Date 2026-10-09. No web research done; source suggestions only. Local copies of four vendor pages in `scratchpad/drafter/ma_pages/` (quotas, floor settings, sanitize page, Apigee SanitizeModelResponse policy; working copies, not sources) were opened to classify T%s, T%s, T%s and T%s; nothing here is verified against a live page. Scripts used are in `scratchpad/triager/`.' % (ID['token_semantics'][1:], ID['userprompt_doc'][1:], ID['pi_default'][1:], ID['chunk'][1:]))
w('')
w('## Legend')
w('- File short names: A = modelarmor_cols_a.md, B = modelarmor_cols_b.md, INV = modelarmor_inventory.md, BR = the brief, queue = `scratchpad/main/queue.md`.')
w('- Location notation: `MAn Rk` = column MAn, row Rk (Summary, bullet kind or count in brackets). `INV(a)` to `INV(e)` = inventory table, then the row name and the cell (for example `INV(a) RAI Default`). `A RN-n` = Reviewer-notes bullet n of A (22 bullets, in order: 1 retrieval, 2 page dates, 3 repo read, 4 C14, 5 C15, 6 C16, 7 C1, 8 C3, 9 C5, 10 C6, 11 C9, 12 C10, 13 C11, 14 C12, 15 C13, 16 Apigee scope, 17 sample oddities, 18 region facts, 19 antivirus, 20 Inferred premises, 21 nothing published, 22 not read). `B RN-0` = B retrieval paragraph; `B RN-1` = response-side evidence block (for, against, reading); `B RN-2.n` = "Corrections and additions to the brief" bullet n (1 method pages, 2 IMAGE enum and XLYM, 3 Gemini Enterprise modalities, 4 basic infoTypes, 5 Agent Gateway, 6 MCP status, 7 feature table 20 rows, 8 floor RAI default, 9 Apigee FunctionResponseSource, 10 include_findings, 11 release-note history, 12 MODALITY_UNSPECIFIED); `B RN-3` = paired source conflicts; `B RN-4` = uncertain items. `INV RN n.m` = inventory Reviewer note n, sub-bullet m (1.1 PI advice, 1.2 basic SDP, 1.3 default level, 1.4 embedded images, 1.5 token limits, 1.6 retirement date, 1.7 antivirus, 1.8 exclusion rules, 1.9 SCC, 1.10 logSanitizeOperations, 1.11 Go client, 1.12 feature table rows).')
w('- Labels: ND = [Not disclosed]; TBV = [To be verified]; INF = [Inferred]; SUM = a Summary line. R8 = unlabelled R8 bullet.')
w('- Class: a = answerable from official docs or code (named page, repo path or release note); b = needs testing or vendor access (stays open); "honest gap" = closed vendor internals or undisclosed behaviour that no public document is expected to answer; c = licensing or terms.')
w('- Priority: H = affects a Summary line (R1 to R7) or a headline number or parameter (default level, threshold, location count, token limits); M = Detail level; L = cosmetic or low impact.')
w('- Short source names for the suggestions: OV overview; TPL manage-templates; SAN sanitize-prompts-responses; FLR configure-floor-settings; QUO quotas; FAR feature-availability-by-region; DR data-residency; LOC locations; FV set-filter-version; RN release-notes; RT REST templates reference; RR REST SanitizationResult; EXC configure-exclusion-rules; LOG configure-logging; INT integrations; AGW agent-gateway page; GE Gemini Enterprise page; NET networking page; LC LangChain page; MCPD MCP page; PROD product page; PRC pricing page. All under https://docs.cloud.google.com/model-armor/ unless named otherwise.')
w('')
w('## Counts')
w('')
w('Total %d deduplicated items (T1 to T%d), drawn from 102 R8 bullets (A 60, B 42), the explicit open labels (A body: ND 57, TBV 16; B body: ND 48, TBV 3; INV body: ND 26, TBV 11; counts include Summary labels), the three Reviewer-notes sections, the queue questions routed to triage, and the cross-draft comparison.' % (n, n))
w('')
w('| Class | Count | of which H | of which honest gap |')
w('|---|---|---|---|')
for c, label in (('a', 'a doc-answerable'), ('b', 'b needs testing or access'), ('c', 'c licensing and terms')):
    w('| %s | %d | %d | %d |' % (label, cls[c], cp[(c, 'H')], hg_cls[c]))
w('| Total | %d | %d | %d |' % (n, pri['H'], hg))
w('')
w('Priority totals: H %d, M %d, L %d.' % (pri['H'], pri['M'], pri['L']))
w('')
w('Class by priority:')
w('')
w('| Class | H | M | L |')
w('|---|---|---|---|')
for c in 'abc':
    w('| %s | %d | %d | %d |' % (c, cp[(c, 'H')], cp[(c, 'M')], cp[(c, 'L')]))
w('')
w('Items touching each source file (an item can touch several files; dedup note below):')
w('')
w('| File | Items | a | b | c | of which H |')
w('|---|---|---|---|---|---|')
for f, name in (('A', 'modelarmor_cols_a.md (MA1 to MA4, MA7, MA8)'), ('B', 'modelarmor_cols_b.md (MA5, MA6, MA9, MA10)'), ('INV', 'modelarmor_inventory.md (5 tables)')):
    w('| %s | %d | %d | %d | %d | %d |' % (name, perfile_n[f], perfile[f]['a'], perfile[f]['b'], perfile[f]['c'], perfile_h[f]))
w('')
w('Dedup note: the same open question recurs across the six A columns and in both directions (backing model, accuracy, latency, default level, Apigee status, languages, OCR text) and is merged into one id with every location listed. Where a question has both a "does a document say it" half and a "does it hold in the live service" half, it is split into an a item and a b item (%s with %s, %s with %s, %s with %s, %s with %s, %s with %s, %s with %s, %s with %s, %s with %s). Items %s touch no draft (suggested).' % (
    ID['rai_default_doc'], ID['rai_default'], ID['pi_advice_doc'], ID['pi_level_test'], ID['csam_doc'], ID['csam_test'], ID['ocr_doc'], ID['ocr_test'], ID['pi_resp_doc'], ID['pi_resp_test'], ID['userprompt_doc'], ID['userprompt_effect'], ID['basic_count_doc'], ID['basic_count_test'], ID['embedded_doc'], ID['embedded_test'], ID['lib_licence']))
w('')
w('R8 bullet mapping (all 102 R8 bullets map to an id): ' + '; '.join(R8_TXT) + '.')
w('')
w('Provenance note: all three files state that every page was read as raw text with `fetch_text.py` (A, B) or raw HTML (INV), repo facts from a shallow clone of googleapis/google-cloud-go at 37f936ac (R013), and no fact from a summarising fetch. Not read at all: the whitepaper linked from the product page (BR G10), the Terraform resource page (T%s), the Security Command Center findings detail beyond one table, and the two Google sample repos (unreachable). Mechanical checks: `check_drafts.py columns` gives 0 errors on A (6 columns) and B (4 columns); `check_drafts.py inventory` gives 0 errors on INV (10/15/16/18/16 rows); no Summary exceeds its word limit (longest R7: MA3 at 56 of 60; longest others 44 of 45); every Covered-by cell in INV(a) and INV(b) is one of the ten brief headers or the inventory-only marker (0 stray values).' % ID['terraform'][1:])
w('')
w('## Triage table')
w('')
w('| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |')
w('|---|---|---|---|---|---|')
w(rows())
w('')

# ------------------------------------------------------------------ CP1 decisions
w('## Decision-bearing items for CP1 (not counted as T-ids)')
w('')
w('These need the user, not a resolver. Evidence from the drafts is given; no recommendation beyond what the evidence supports.')
w('')
w('- **D1 Column split and count (Q-A, R002).** Facts: Model Armor has separate per-direction methods (userPromptData with sanitizeUserPrompt, modelResponseData with sanitizeModelResponse, plus streaming variants), so the R002 exception (one undifferentiated check with no direction flag) is not met. Drafting evidence: in the six A columns, 56 to 66 of the 81 to 94 R1 to R7 bullets of each column are word-for-word identical to a bullet in another A column (387 of the 863 R1 to R7 bullets across the ten columns are repeated); the input and output pairs share 51 (MA1 and MA2), 44 (MA3 and MA4) and 54 (MA7 and MA8) identical bullets, and 8 Summary pairs are word-for-word identical (MA1 R3 with MA3 R3; R4 of MA1 and MA2; R9 of MA1 and MA2; R4 and R5 and R9 of MA3 and MA4; R4 and R5 of MA7 and MA8). MA5 and MA6 share only 9 bullets, MA9 and MA10 have almost none (3 and 4), so the SDP pair and the two modality columns are real content. The direction-specific facts are few: request field and method, the response-side use case, the userPrompt field ({k:userprompt_doc}), tool and MCP routes in MA4 and MA8, streaming URL chunks ({k:url_stream}). Options: (a) 10 columns as drafted; (b) 6 columns (R002 exception, would drop the Input-level and Output-level headers and lose the per-direction test inputs that R002 gives as its reason); (c) fold MA9 and MA10 into MA1 to MA8 Detail (loses about 160 bullets with almost no duplication, and the largest open items {k:resp_files}, {k:embedded_doc}, {k:antivirus}); (e) 14 columns, see D3.'.replace('{k:userprompt_doc}', ID['userprompt_doc']).replace('{k:url_stream}', ID['url_stream']).replace('{k:resp_files}', ID['resp_files']).replace('{k:embedded_doc}', ID['embedded_doc']).replace('{k:antivirus}', ID['antivirus']))
w('- **D2 MA11 tool-call and tool-response screening (Q-B, alt (d)).** Facts: MCP payload coverage (tools/call, prompts/get, tool execution errors) is already in MA3 R3, MA4 R2 and R3, MA6 R2, R3 and R4; Agent Gateway egress (MCP, A2A, OpenAI-format) is one INV(b) row with the inventory-only marker, while Agent Gateway ingress lists MA1 to MA8 (INV RN 3); Apigee has a FunctionResponseSource element for tool data (B RN-2.9, not used in any column). The function has no filter of its own (it reuses RAI, PI, SDP and URL via floor settings or Agent Gateway templates) and no template of its own. Open items that an MA11 would carry: %s (status conflict), %s (structured tool output), %s (de-identified forwarding), %s (response-side PI). The queue bundles INV Q2 (Agent Gateway ingress versus egress marker) into this decision.' % (ID['mcp_status'], ID['tool_json'], ID['deid_forward'], ID['pi_resp_test']))
w('- **D3 Alt (e), 14 columns (split MA9 and MA10 by direction).** Evidence block is B RN-1: for (REST method reference types modelResponseData as a DataItem that can hold a byte item; Go types give ModelResponseData as DataItem and ByteDataItem_IMAGE; overview says images are screened "in the prompts and responses"; release note 2026-06-25 says "within prompts and responses"; overview limitations name both methods) and against (no request body or result for a file or image sent as a response anywhere; sanitize-page byte-item examples use userPromptData only; the response example is text and has no sdp result; documents have no direction statement). Limits (4 MB, one image, us and eu, no text-plus-image) are stated once for both methods, so no documented difference justifies a split. B kept single columns. Only %s (a test) can move this; the documentation ceiling is reached. Not a reason to hold CP1.' % ID['resp_files'])
w('- **D4 Antivirus scanning: Table 3 column, inventory only, or dropped.** Facts: result type virusScanFilterResult (PDF only), a region-table row and release note 2026-04-10 exist; the product page says "Detects malicious files, malware, and unsafe URLs"; no configuration setting or page was found (A, B and INV all say so). Default per R011 is the inventory-only marker, already applied in INV(a). If %s finds a setting, MA9 R1 and R2 Summaries need a clause and a column or Detail may be warranted.' % ID['antivirus'])
w('- **D5 Header prefix (Q-C, R009).** Default `Model Armor:`; alternative `Google Cloud Model Armor:`. All ten headers and every INV Covered-by cell use the default (0 stray values). Frozen after CP2. No draft evidence argues for the alternative.')
w('- **D6 Licensing, terms and live testing.** %d of %d items are class b and need a Google Cloud project with billing, Model Armor API enabled, harmful and jailbreak test content, image routes only in us or eu (cross-border for a Singapore tester), and for %s a Gemini Enterprise subscription. CLAUDE.md hard rule 5 forbids calling vendor APIs during research and says nothing about a later test phase. Needs a user ruling on whether and when the bench provisions a live project and accepts the Pre-GA Offerings Terms for Preview features ({k:prega}) and the Google Cloud terms for testing ({k:live_terms}). Class c items: %s.'.replace('{k:prega}', ID['prega']).replace('{k:live_terms}', ID['live_terms']) % (cls['b'], n, ID['embedded_test'], ', '.join(ID[i['key']] for i in ITEMS if i['cls'] == 'c')))
w('- **D7 SDP overlap wording (R012, already ruled).** Not a new decision, but the forward references to "the Sensitive Data Protection columns on sheet 3" in MA5, MA6 and MA10 and the Singapore NRIC claim ({k:sg_nric}) depend on the sdp CP1 outcome (column split, prefix, whether an SD column exists). Resolve after the sdp ruling.'.replace('{k:sg_nric}', ID['sg_nric']))
w('')

# ------------------------------------------------------------------ closed items
w('## Settled items (no T-id; nothing to resolve)')
w('')
w('| Item | Where | Settled by |')
w('|---|---|---|')
w('| Apigee flow-variable bullets (A RN-16: brief allowed the Apigee pages only for the two policy names) | MA1 R5, MA2 R5, MA3 R5, MA4 R5, MA7 R3 and R5, MA8 R3 and R5, MA6 R3 and R5 | queue: kept, attributed "Apigee docs not Model Armor docs" (R007 item 1) |')
w('| Terraform registry page is not an official source | INV(b) Terraform | queue; open follow-up is %s |' % ID['terraform'])
w('| Inventory sheet letter `3f` is provisional | BR, INV title | R003 (letter assigned at P8) |')
w('| Block (d) lists the union of 20 locations with a labelled note | INV(d) | queue (C15 ruling); the data for the two extra rows is %s |' % ID['useast7'])
w('| Filter-version retirement 2026-12-17 against the earlier 2026-11-29 (C6) | MA1 R4 to MA4 R4 (two bullets each), INV(c) filterVersionSelector | both dates carried with labels; later note wins; no open question |')
w('| Token-limit history 2,000 / 10,000 / 65,536 (C5) | MA1 R6 to MA4 R6, INV(e) | history carried as superseded; current quotas page wins; the over-limit wording is %s |' % ID['token_semantics'])
w('| v3 release date 2026-04-27 in the sample response against 2026-05-25 (C13) | A RN-15 | not used in any draft |')
w('| Release-note SKIP_DETECTION (2025-07-28) against EXECUTION_SKIPPED now | MA5 R6, B RN-2.11 | history against current, current wins; carried in MA5 R6 |')
w('| Docs host move and redirect (seed URL 301 to docs.cloud.google.com; `cloud.google.com/model-armor/docs` 404) | INV intro | recorded with date; owner Google Cloud throughout; no ownership change |')
w('')

# ------------------------------------------------------------------ label hygiene
w('## Label hygiene')
w('')
w('Scope: A (6 columns), B (4 columns), INV (5 tables; labelled cells 80, 105, 96, 198 and 64 in tables (a) to (e), excluding the Covered-by and Source URL columns; the Kind column of (e) is an enum and carries no label by design). Allowed forms: [Documented], [Documented: repo <repo>@<ref>], [Documented: develop/unreleased], [Inferred], [To be verified], [Not disclosed]. Counts are occurrences of the exact bracket text in the file body, Reviewer notes excluded, Summary labels included.')
w('')
w('| File | [Documented] | of which repo-pinned | [Inferred] | [To be verified] | [Not disclosed] |')
w('|---|---|---|---|---|---|')
w('| A | 423 | 5 (google-cloud-go@37f936ac) | 73 | 16 | 57 |')
w('| B | 287 | 7 (google-cloud-go@37f936ac) | 26 | 3 | 48 |')
w('| INV | 609 | 4 (google-cloud-go@37f936ac 3, apigee-samples@2b1a9f00 1) | 38 | 11 | 26 |')
w('')
w('Standard forms in use: yes. Non-standard label forms: none found. Repo labels carry one repo each, an 8-character sha, and every pinned fact has a matching full-sha blob URL in R9 or in the Source URL cell (service.pb.go, CHANGES.md, version.go, apigee-samples README). Bracket pairs that are not labels: `[]` array suffixes in code names (A 6, B 5, INV 6, for example raiFilters[], findings[], ruleSets[]) and quoted placeholders `[IP_ADDRESS]`, `[REDACTED_IMAGE]` in B MA5 R5 and MA10 R5 (4 occurrences). A label parser matching only the five forms ignores them; low risk, no change needed unless the build regex is wider than the five forms.')
w('')
w('| Issue | Count / where | Proposed fix |')
w('|---|---|---|')
w('| Status rule S: "GA [Inferred] (status rule S)" is a mass inference from the absence of a Pre-GA banner | 21 cells: INV(a) 7 rows, INV(b) direct REST 1, INV(c) 13 rows. Applied unevenly: Apigee [TBV], gcloud, console, Terraform, SCC [ND] although they lack a banner too | See %s. Keep the rule only if applied to every row without a stated stage, or use the column\'s own "Not documented" value |' % ID['rule_s'])
w('| Cells mixing two or more label types | INV: (a) 11 cells, (b) 8, (c) 1, (d) 2, (e) 1 | Say which fact the open label applies to, as in the INV(a) RAI Default cell; split where a Documented fact and a TBV fact share a clause |')
w('| Two sources on opposite sides inside one bullet (README 3 rule 4: two bullets, each labelled) | A MA1 R2 and MA2 R2 CSAM bullet ("cannot be turned off" and the feature table "No" in one [Documented] bullet); A RN-4 says two bullets, but the R1 bullet carries only the overview side | Split the R2 bullet into two, one per page (%s) |' % ID['csam_doc'])
w('| Absence clause inside a [Documented] bullet | B MA5 R2 and MA6 R2 "Source conflict ... no page reconciles the two counts" | Keep the two count bullets [Documented]; move "no page reconciles" to its own [Not disclosed] bullet naming the pages checked |')
w('| [Inferred] used for an absence | A MA1 R5 and MA2 R5 "false-positive risk ratings ... no measured rates accompany them [Inferred]"; A MA3 R5 and MA4 R5 "no separate default statement ... [Inferred]" (contradicted by INV, %s) | Use [Not disclosed] and name the pages checked; for the PI default follow %s |' % (ID['pi_default'], ID['pi_default']))
w('| [Documented] used for a judgement | A MA7 R1 "frames the filter mainly around output"; A MA7 R2 and MA8 R2 "that is a separate capability and not part of this column" (scope decision, sources only list a result type) | [Inferred] with the premise, or reword to the sourced facts (%s, %s) |' % (ID['url_input'], ID['antivirus']))
w('| One bullet, several facts | A R4 "Release status of routes" (7 routes in one [Documented] bullet) in MA1 to MA4, MA7, MA8; pricing bullet (standalone allowance and SCC inclusion); data-handling bullet (stateless, Cloud Logging, logSanitizeOperations) | README 4: one fact per bullet; split, which also lets %s and %s attach to the right route |' % (ID['apigee_status'], ID['mcp_status']))
w('| Absence claim from a code grep covering two packages, one cited | A MA3 R4 and MA4 R4 (Go client has no FilterVersion, FilterRule, exclusion field; grep of apiv1 and apiv1beta); R9 lists only the apiv1 service.pb.go | Add the apiv1beta blob URL to R9 (INV(b) already lists it); label stays [Not disclosed] (%s) |' % ID['go_lag'])
w('| R9 omits a URL the same fact needs in another column | MA2, MA4, MA8 R9 lack the sanitizeModelResponse REST method page that B cites for the userPrompt field; MA1 to MA4 absence bullets name "blog" among pages checked with no blog URL in R9 | Add the method page URL (%s); add the blog URL or drop "blog" from the checked lists |' % ID['userprompt_doc'])
w('| Hint style differs | A "(overview, 2026-10-09)"; B "(overview, read 2026-10-09)"; INV omits a date in cells and states it in the intro | Normalise to one form at merge; cosmetic |')
w('| Docs "Last updated" dates stated inconsistently | INV intro against A RN-2 | %s |' % ID['footer_dates'])
w('| Covered-by values | all valid: INV(a) 10 rows and INV(b) 15 rows are each one or more exact brief headers separated by semicolons, or the marker `— (inventory only, not in Table 3)` (8 rows: Antivirus in (a); gcloud, Terraform, Agent Gateway egress, MCP servers, Security Command Center, console and monitoring in (b)) | none; P8 config `markers` tuple must include the R011 marker |')
w('')

# ------------------------------------------------------------------ style
w('## Style issues in columns')
w('')
w('1. **R4 Summary label differs between files.** All six A columns label R4 [Not disclosed] (the model is not named); all four B columns label R4 [Documented], although MA5 R4, MA9 R4 and MA10 R4 also state an absence in the Summary ("The detectors are not described", "The extractor and its handling of scans and layout are not described", "The OCR engine is not disclosed"). One convention is needed (weakest label wins, README 4).')
w('2. **Absence or gap stated in a Summary that carries [Documented] (12 Summaries).** B MA5 R3 ("Documented examples exist for the prompt side only"), MA5 R4, MA5 R5 ("no published accuracy figure"); MA6 R2 ("Model Armor docs do not say whether the basic list is the same for responses"), MA6 R3 ("Documented examples for response-side de-identification are missing"), MA6 R5; MA9 R3, MA9 R4, MA9 R5; MA10 R3, MA10 R4, MA10 R5. The label is the weakest among the facts drawn on, so these become [Not disclosed] or the clause moves to R8.')
w('3. **Summary not entailed by Detail, or label stronger than Detail.** (a) A MA4 R2: "MCP tool results" as a target for injection, while the quoted Detail says "MCP tool execution errors (target for prompt injection by malicious MCP tools authors)"; (b) A MA4 R1: "all show the filter running on model responses" labelled [Documented], Detail calls the reading [Inferred] (%s); (c) A MA2 R5: leads with the masked-IP sample, Detail says it cannot be used as evidence (%s); (d) A MA1 R5 and MA2 R5: "two different defaults" when INV records three (%s); (e) B MA5 R6 and MA6 R6: "Text over 130,000 tokens is skipped" (%s); (f) A MA1 R1 and MA2 R1: CSAM check "cannot be turned off" without the limited-region caveat (%s); (g) B MA9 R4: "Extraction runs inside the managed service" has no Detail bullet (INF at most); (h) B MA10 R2: "Documented targets ... in an image\'s pixels or its text" while two Detail bullets are [Inferred] and one is [Not disclosed] (%s); (i) A MA7 R1 "mainly" (%s).' % (ID['pi_resp_doc'], ID['ip_sample'], ID['rai_default_doc'], ID['token_semantics'], ID['csam_doc'], ID['ocr_doc'], ID['url_input']))
w('4. **Identical Summaries across a pair or a column set (8 pairs).** MA1 R3 = MA3 R3; MA1 R4 = MA2 R4; MA3 R4 = MA4 R4; MA7 R4 = MA8 R4; MA3 R5 = MA4 R5; MA7 R5 = MA8 R5; MA1 R9 = MA2 R9; MA3 R9 = MA4 R9. The brief says write both columns in full; identical R5 Summaries for MA3 and MA4 are also wrong in substance (MA4 R5 Detail shows a response example with no confidence field).')
w('5. **Code identifiers in Summaries.** B MA10 R3 ("typed IMAGE") and MA10 R6 ("The type must be IMAGE") use an enum value; B MA9 R3 and R6 use "byte item" and "byte data type" in prose. Rewrite as "image type". Other upper-case tokens are acronyms or file formats (API, CSAM, PDF, OCR, URL, MCP).')
w('6. **Shared boilerplate.** 387 of 863 R1 to R7 bullets are repeated word for word in another column (A columns 56 to 66 of 81 to 94 each; B columns 3 to 10). Not an error, but it drives D1 and makes the merge diff large; the merger should keep one wording per fact.')
w('7. **Cross-references to other products are absent.** The brief asks for R4 or R8 cross-references (NeMo Guardrails, Presidio and Sentinel for PII; Llama Guard and Sentinel for content safety and prompt attacks). Only the Sensitive Data Protection cross-reference exists (MA5, MA6, MA10). Optional; add at merge or leave to sheet 4.')
w('8. **Reviewer notes and process wording.** None found in column bodies or inventory cells ("this draft", "I checked", "see Reviewer notes": 0 hits; every quote under 40 words: 0 over). Reviewer-notes sections (A 22 bullets, B 5 blocks, INV 6 notes) must move to the change log at merge.')
w('9. **Short product names.** "Agent Platform", "Agent Runtime" and "Gemini Enterprise" appear side by side; the first use in each column should give the docs name once ("Gemini Enterprise Agent Platform") (%s).' % ID['naming'])
w('10. **R7 first bullet.** All R7 first Detail bullets start `**Minimum setup:**` and carry [Inferred]; A bullets end with a full stop before the label ("... `pi_and_jailbreak` result. **[Inferred]**"), B bullets do not. Normalise (README example has no full stop before the label).')
w('')

# ------------------------------------------------------------------ contradictions
w('## Contradictions')
w('')
w('Source conflicts and cross-file inconsistencies, each with the ids that resolve them.')
w('')
C = [
 "userPrompt field of sanitizeModelResponse: A (MA2, MA4, MA8 R3, R8 and A RN-3) says only the Go client documents it and the docs pages do not mention it; B (MA6 R3, R6 and B RN-2.1) quotes the REST method reference that documents it; the Apigee SanitizeModelResponse policy page has a UserPromptSource element and a userPrompt flow variable. See {k:userprompt_doc}, {k:userprompt_effect}.",
 "PI and jailbreak default level: A MA3 R5 and MA4 R5 [Inferred] 'would behave as Low and above', no page states it; INV(a) and INV(c) [Documented] floor settings default PI to LOW_AND_ABOVE. See {k:pi_default}.",
 "RAI default level: A MA1 R5 and MA2 R5 give two statements (console High; REST unspecified equals LOW_AND_ABOVE or 'a reasonable default'); INV and B RN-2.8 add a third (floor-settings page: Medium and above). R5 Summary says 'two'. See {k:rai_default_doc}, {k:rai_default}.",
 "RAI, PI and URL on OCR text: INV(a) OCR row states 'depending on the filter configuration' as [Documented]; MA10 R2 says which filters examine OCR text is [Not disclosed]; MA1, MA3, MA7 and MA8 mark it [To be verified]. Same sentence, three treatments. See {k:ocr_doc}.",
 "CSAM: overview 'cannot be turned off' against the feature table 'No' in seven limited-support locations. A Summaries R1 assert it runs; INV(a) CSAM row says 'Always on' and 'not available in limited-support regions' in two cells. See {k:csam_doc}, {k:csam_test}.",
 "MCP status: release note 2026-04-22 GA against floor-settings page link '(Preview)'. MA6 R4 holds both; MA1 to MA4, MA7, MA8 R4 and INV(b) MCP state GA only. See {k:mcp_status}.",
 "PI on responses: MA4 R1 overview 'scans prompts and responses' and sample response output with a pi_and_jailbreak result, against templates page 'in a prompt'; Summary label [Documented] against an [Inferred] bullet; INV(a) PI Applies to is [Documented] Input and Output. See {k:pi_resp_doc}, {k:pi_resp_test}.",
 "logSanitizeOperations: logging page 'full content' against overview 'metadata or snippets as configured'. A and B R4 state the full-content side; INV(c) records both. See {k:logsan}.",
 "Over-limit behaviour: A and B R6 (and MA5, MA6 R6 Summaries) say text over the limit is skipped; quotas page and INV(e) say a detected match still returns MATCH_FOUND. See {k:token_semantics}.",
 "Streaming limits: A and B R6 say real-time mode has unlimited tokens; sanitize page (and INV(e)) add that individual chunks must not exceed the token limits. See {k:chunk}.",
 "Singapore identifiers: MA5 R7 and MA6 R7 say a custom detector is needed; the SDP drafts document a built-in SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER infoType. See {k:sg_nric}.",
 "Locations: A MA7 R6 and MA8 R6 say the feature table lists us-east7 and global rows; INV(d) has 18 rows and omits them; queue ruling asks for 20. See {k:useast7}.",
 "Embedded images: overview 'doesn't screen images embedded within files' and integrations page (for Gemini Enterprise) against Gemini Enterprise page 'Images contained inside other files and documents'. INV(a) OCR Limit cell states the overview side only. See {k:embedded_doc}, {k:embedded_test}.",
 "Gemini Enterprise modalities: integrations options table 'Text, documents' against the Gemini Enterprise page (images). See {k:ge_modal}.",
 "Basic SDP infoTypes: overview and REST six; sanitize page seven (PASSWORD; SSN and ITIN only for US-based regions). B reads the sanitize lists as prompt-only. See {k:basic_count_doc}, {k:basic_resp}.",
 "filterResults shape: REST reference keyed map against sanitize-page examples as an array. See {k:filterresults_shape}.",
 "Image finding box: REST boundingBoxes (list) against sanitize-page boundingBox (object). See {k:bbox}.",
 "PI threshold advice: overview Medium (High for Gemini Enterprise); templates page High; overview table Low and above for high-stakes categories; floor-settings illustration Medium. See {k:pi_advice_doc}, {k:pi_level_test}.",
 "Go client against docs: docs describe filterVersionSelector, filterRuleSettings, dataResidencyCompliant, MCP floor setting; Go v1 at 37f936ac has none. Exclusion-rules page shows filterRuleSettings, REST FilterConfig does not. See {k:go_lag}, {k:excl_schema}.",
 "Agent Gateway 'block and redact' (intro) against 'allows or blocks' (flow); networking 'modify'. Only Apigee documents extracting redacted data. See {k:deid_forward}.",
 "Product-page 'Detects malicious files, malware' and the antivirus result type against the A statement that antivirus is 'a separate capability and not part of this column' (MA7, MA8) and the INV statement that no setting exists. See {k:antivirus}.",
 "Status rule S: 21 cells 'GA [Inferred]' while comparable rows without a banner are [Not disclosed] or [To be verified]. See {k:rule_s}, {k:apigee_status}, {k:terraform}.",
 "Pricing wording: 'four characters excluding white space' (pricing page) against 'about 4 characters' (overview, quotas); INV(e) SCC tier row wording against the pricing table. See {k:pricing}.",
 "Security Command Center: integrations page (floor-setting violation sends a finding) against SCC findings page (only FLOOR_SETTINGS_VIOLATION). See {k:scc}.",
 "REST enum Excel types: XLYM in the DataItem text against XLTM in overview and release notes. See {k:xltm}.",
 "MODALITY_UNSPECIFIED 'all modalities' against empty modalities 'text only'. See {k:modality_unspec}.",
 "Docs page dates: INV intro (all 2026-10-06 except release notes) against A RN-2 (2026-09-07, 2026-10-05, 2026-10-07). See {k:footer_dates}.",
 "Release note dated 2026-10-10 present on 2026-10-09 (system date); A and INV carry it as read, INV does not use it as a fact. See {k:rn1010}.",
 "Not conflicts but easy to misread: release-note token limits (2,000, 10,000) are history; v1 and v2 retirement 2026-11-29 is superseded by 2026-12-17; the sample response v3 releaseDate 2026-04-27 is example output; SKIP_DETECTION (release note 2025-07-28) is history. See the Settled items table.",
]
for i, c in enumerate(C, 1):
    w('%d. %s' % (i, ref(c)))
w('')
w('## Self-check')
w('')
w('- Items %d; all %d ids in the table are unique; every `{k:...}` reference resolved; %d item touches no draft (%s, the suggested licence item).' % (n, n, len(nofile), ', '.join(nofile) if nofile else 'none'))
w('- Counts in this file are generated from the item list by `scratchpad/triager/build_triage.py` (items in `items.py`), so class, priority and per-file totals add up (a %d + b %d + c %d = %d; H %d + M %d + L %d = %d).' % (cls['a'], cls['b'], cls['c'], n, pri['H'], pri['M'], pri['L'], n))
w('- Statistics quoted (label counts, duplicate bullets, Summary word counts, Covered-by validation) come from `stats.py` and `labels.py` and inline checks in the same folder; `check_drafts.py` exit codes were 0 for all three inputs.')

out = '\n'.join(md) + '\n'
open('benchtest/drafts/modelarmor_triage.md', 'w', encoding='utf-8').write(out)
print('items', n, dict(cls), dict(pri), 'hg', hg)
print('perfile', perfile_n, perfile_h)
print('H ids', [ (ID[i['key']], i['key']) for i in H_ITEMS])
