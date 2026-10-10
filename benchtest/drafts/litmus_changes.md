# Litmus merge: change log

Inputs merged: litmus_eval_tooling.md (8 sections, 9 Reviewer notes), litmus_inventory.md (blocks 4/5/6, 6 Reviewer notes), litmus_triage.md (63 items, H 11), litmus_resolutions_1.md (63 items: 35 RESOLVED, 5 PARTLY RESOLVED, 2 CORRECTION, 21 STILL OPEN), litmus_brief.md, and the rulings R003, R007, R011, R015, R019, R020, R021, R032, R038 plus main's litmus rows in scratchpad/main/queue.md (P5 Q1 to Q5: Open-question bullets carry only [To be verified] or [Not disclosed]; staging pin with a production-versus-staging note; Overview Summary = the resolver's RECOMMENDED text; Engine Summary = the resolver's new text; Baseline subset of Baseline+ [Documented] in both files, id mapping [Inferred]).

Outputs: litmus_eval_tooling_final.md (8 sections, parses with build_eval_sheet.parse_md), litmus_inventory_final.md (3 blocks, 15 rows), litmus_changes.md (this file), litmus_summaries_preview.md. Litmus has no Table 3 columns (R003), so there is no litmus_two_level.md and no columns check; the final text carries no column IDs. Merge method: every edit was applied by script to the draft lines named in the resolutions (line numbers as at 2026-10-10, EV = eval draft, INV = inventory draft), so each edit below is also the log entry. Bold markers are dropped from quoted text, long text is shortened, and pipes inside cells are shown as slashes. Reason codes: Tn = triage id (resolution in litmus_resolutions_1.md), A1 = the resolver's pin CORRECTION, 'main P5' = main's queue ruling, 'hygiene' = label or look-alike fix, 'style' = wording or process text.

## 1. Global changes

| Scope | Before | After | Reason |
|---|---|---|---|
| Reviewer notes sections | EV 9 notes, INV 6 notes in the drafts | removed from both finals; kept verbatim in section 7 | T62; README section 7 item 2 |
| Sheet set | inventory option (a) (3 blocks) plus eval sheet, pending CP1 | unchanged: inventory blocks 4/5/6 (15 rows), eval sheet with 8 sections; no Table 3 columns; every Covered-by cell is the inventory-only marker | T1, T2 (R038); R003; R011 |
| Overview Summary | 'Litmus is a hosted testing service for AI applications, not a guardrail ... before launch' (44 words excl. label) | resolver's RECOMMENDED text with the eligibility and proof-of-concept qualifiers (44 words excl. label; fallback text not used) | T20, T4, T21; main P5 ruling |
| Engine coverage Summary | 44 words excl. label, 46 incl. (claims 'over HTTP' with no Detail bullet; 'no statement on guardrailed endpoints') | resolver's new text, 43 words excl. label, 45 incl.; 'over HTTP' backed by a new Detail bullet; 'no support statement for guardrailed endpoints' | T51, T50; lessons 18 |
| Playbook pin (EV Version scope, INV legend) | 'staging branch ... the deployed site is built from staging' | same pin 45908b48 (staging) plus the production-versus-staging note: the README lists staging (built from staging) and production (built from main); pinned pages match staging; production carries the same statements except the refusal sentence in tools/litmus.md line 53 | A1 (CORRECTION); main P5 ruling; T40 |
| Open-question labels | two Open questions under [Inferred] (EV:146, EV:147); two vendor-internal questions under [To be verified] | every Open-question bullet carries [To be verified] or [Not disclosed] only (counts in section 8) | main P5 ruling (README section 6); T14, T15, T39, T52, T53 |
| Short-name set | two name sets: DOCS/PORTAL in EV, AIG/DEV in INV; legend only in unparsed lines | one set DOCS, PORTAL, PB, ACT (MS in EV): legend also in the parsed Tools note (EV) and the block (a) intro (INV) | T60 |
| Process wording in parsed text | '(R002)', 'in this draft', '(R019)', '(R003)', '(a proposal, R032)', 'conflict C1 ... C20' (brief conflict ids) | removed or reworded in plain words (24 distinct conflict-id phrasings, 28 occurrences); unparsed lines also lose R003, R011, R019 and 'R007 item 7' | T59, T58; README section 4 |
| Line locators into pinned files | 'line 46', 'lines 31 to 45', 'lines 432 to 437', 'line 11' | file@ref:line form; ACT lines 31-44 (headers 45); safety.mdx 429-440; benchmark_runner_dto.py@0.7.6:10 | T11 |
| Link-target facts | '(link target read from the page)' | method named: read from the page HTML with curl and the Python standard-library parser, 2026-10-10; not visited | T9; R021 |
| Moonshot tags | tags 0.4.0, 0.5.0, 0.7.6 | tags 0.4.11 (in force at the sample Action commit), 0.5.0, 0.7.6; Apache-2.0 licence bullet; moonshot-data name-resemblance bullet | T12, T7, T53; R019 |
| Datasets Contents cells | leading '[Security]' style brackets (look like labels) | 'Category: Security.' style prefix in all 14 test rows | T43 |

## 2. Eval sheet changes (litmus_eval_tooling_final.md)

Entries are in document order. Several new bullets in one 'after' cell are joined by ' // '.

### 2.1 Title and Version scope (unparsed lines) (4 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Title (EV:1) | ## Topic: GovTech Litmus evaluation tooling (draft, reuse assessment for the test bench) | ## Topic: GovTech Litmus evaluation tooling (reuse assessment for the test bench) | 'draft,' removed from the title; finals are not drafts (T62) (style) |
| Version scope (EV:3) | AI Guardian docs pages (Docusaurus site, source repository not located) | AI Guardian docs pages (Docusaurus v3.10.0 per the page's generator tag, deployed 2026-10-08 08:42 UTC per th… | T8: docs pages stay unpinned; evidence for the absence of a source repository stated (edit) |
| Version scope (EV:3) | (full SHA 45908b48c0a8b6d3855a154c0e41a12958a99205, committed 2026-09-14; the pinned website/docs/tools/litmu… | (full SHA 45908b48c0a8b6d3855a154c0e41a12958a99205, committed 2026-09-14). The repository README lists two de… | A1 (CORRECTION): the pinned branch is the staging deployment; production-versus-staging note per main P5 ruling (edit) |
| Version scope (EV:3) | nothing was signed in to, submitted or called (R019). | nothing was signed in to, submitted or called. | T59: ruling id removed from the text (style) |

### 2.2 Overview (15 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Overview Summary (EV:6) | Summary: Litmus is a hosted testing service for AI applications, not a guardrail. It sends curated prompts to… | Summary: Litmus is a hosted testing service for AI applications, not a runtime defence. It scores an applicat… | T20 + T4 + T21 (main P5 ruling): resolver's RECOMMENDED text with eligibility and proof-of-concept qualifiers; 'not a guardrail' and 'before launch' dropped (44 words excluding the label) (summary) |
| Overview, bullet 'Litmus tests a system' (EV:15) | • Litmus tests a system and is not a runtime defence: "Litmus tests a system; it does not defend one at runti… | • Litmus tests a system and is not a runtime defence: "Litmus tests a system; it does not defend one at runti… | T20: split into two one-fact bullets; second quote is on line 17; locators in file@ref:line form (T11) (replace) |
| Overview, after EV:15 | (none) | • Runs can be triggered "manually from the web application, on a schedule, or from a CI/CD job on each commit… | T20: backs 'from a web app or CI/CD' in the Summary and removes the 'before launch' reading (add) |
| Overview, direction bullet (EV:16) | • Direction note (R002): Litmus is not an inline guardrail. It sends prompts to a tenant endpoint and judges… | • Direction: Litmus is not an inline guardrail. It sends prompts to a tenant endpoint and judges the applicat… | T20 + T59: ruling id (R002) and 'in this draft' removed (replace) |
| Overview, after EV:17 | (none) | • The Kaleidoscope documentation calls Litmus "AI Guardian’s testing and evaluation platform for Whole-of-Gov… | T4: audience statement from the Kaleidoscope docs (add) |
| Overview, interest-form bullet (EV:18) | the form was not opened, R019) | the form was not opened) | T59: ruling id removed (style) |
| Overview, status source two (EV:20) | • Status, source two (conflict C4, not resolved): the docs Overview, Getting Started, the one-pager and the p… | • Status, source two (conflict C4, not resolved): the docs Overview, Getting Started and Troubleshooting page… | T21 + T22: checked list widened; Sentinel clause dropped (one fact per bullet) (replace) |
| Overview, one-pager bullet (EV:23) | (a "Global Overview Document", dated by its file name 20250916) | (titled "AI Guardian: Litmus & Sentinel Global Overview Document"; created 2025-09-16 per the PDF metadata, t… | T10: provenance from the PDF itself (edit) |
| Overview, one-pager bullet (EV:23) | text read with pdftotext) | text read with pdftotext and checked with a second extractor) | T10: second extraction (pypdf) found all nine phrases (edit) |
| Overview, Kaleidoscope playbook-side bullet (EV:24) | • Relation to Kaleidoscope, playbook side: Kaleidoscope is "the contextual evaluation module within Litmus" a… | • Kaleidoscope, playbook Litmus page: "Kaleidoscope, which is the contextual evaluation module within Litmus"… | T32: split into the two playbook statements that differ; the 'stay tuned' quote added (replace) |
| Overview, alignment bullet (EV:26) | • Alignment claim: the docs Overview says Litmus gives "Comprehensive risk and behaviour analysis aligned wit… | • Alignment, conflict C9 first side: the docs Overview says "aligned with public sector AI ethics, policies,… | T23: one fact per bullet; AI Guardian home page added as a second source of the shorter wording (replace) |
| Overview, after EV:27 (owner) | (none) | • No licence or reuse statement was found for the quoted GovTech material: the playbook repository at 45908b4… | T5: licence of the quoted material (class c; absence) (add) |
| Overview, 'No model, judge ...' bullet (EV:28) | • No model, judge, dataset size, licence, terms of use, pricing, quota, data-handling or retention statement… | • Evaluator or judge and backing model: not published; the Overview says only "automated internal evaluation"… | T22 + T3: one bullet with six absences split into separate bullets, each with its own checked list; the Terms clause is its own [Documented] bullet (one label per fact) (replace) |
| Overview, 'No open-source Litmus' bullet (EV:29) | • No open-source Litmus server or client: dsaidgovsg/aiguardian-litmus-test, the Action name the docs give, r… | • No public repository for the Action name the docs give: git ls-remote https://github.com/dsaidgovsg/aiguard… | T17 + T18 + T22: the HTTP facts become a [Documented] bullet; the repository search is a separate [Not disclosed] bullet naming the method (replace) |
| Overview, after EV:30 (four new bullets) | (none) | • Two Litmus addresses return HTTP 403 AccessDenied (Server AmazonS3, X-Cache "Error from cloudfront"): https… | T14 + T13: HTTP facts moved from Open questions to Detail as [Documented]; the conclusion stays [Inferred] with its premise; Wayback scope narrowed; Sentinel wiki path dropped (add) |

### 2.3 Tools (18 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Tools note (EV:34) | Litmus has no Table 3 column (R003). | Litmus has no Table 3 column. | T59: ruling id removed (style) |
| Tools note (EV:34) | DOCS, PORTAL, PB, ACT and MS are defined in the Version scope line. | DOCS = the AI Guardian docs at https://www.aiguardian.gov.sg/docs/wiki/; PORTAL = https://www.developer.tech.… | T60: legend in a parsed note so it reaches the sheet (edit) |
| Tools note (EV:34) | its repository was not researched. | its repository was not researched. Table 3 headers named: GovTech Sentinel: Prompt-attack detection; GovTech… | T30: the exact headers named in the Evaluates cell of row 1 are listed in the note (add) |
| Tools row 1 (Litmus web app), Evaluates cell (EV:38) | A possible reuse: the test themes could serve as a reference list when planning tests for GovTech Sentinel: P… | A possible reuse: the six Undesirable Content test names (Hateful, Insults, Sexual, Physical Violence, Self-H… | T30: prose with two Sentinel headers inside replaced; headers listed in the note; LionGuard column named (replace) |
| Tools row 2 (Litmus API), Inputs cell (EV:39) | (not called) [Documented]. The route /api/v1/benchmarks and a request body appear only in the sample Action (… | (link target read from the page HTML with curl and the Python standard-library parser, 2026-10-10; not called… | T9 (triage location EV:39) + T11: link-target method named; locators in file@ref:line form (edit) |
| Tools row 2, Judge cell (EV:39) | / Not disclosed [Not disclosed]. / [Not disclosed]; the sample Action | / [Not disclosed] (see Engine coverage). / [Not disclosed]; the sample Action | T61: repeated absence points to Engine coverage (style) |
| Tools row 3 (CI/CD), Inputs cell (EV:40) | That repository returns "Repository not found" (observed 2026-10-10) [Documented]. | That repository returns "Repository not found" and HTTP 404 on github.com (observed 2026-10-10) [Documented]. | T18: both methods for one fact stated alike in all places (edit) |
| Tools row 3, Inputs cell (EV:40) | (conflict C2) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1]. | (conflict C2) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1]. The step is headed "Push Changes t… | T26: platform wording conflict recorded in the eval sheet (the inventory already carried it) (add) |
| Tools row 3, Judge and Engine cells (EV:40) | / Not disclosed [Not disclosed]. / [Not disclosed]. / DOCS | / [Not disclosed] (see Engine coverage). / [Not disclosed] (see Engine coverage). / DOCS | T61 (style) |
| Tools row 4 (custom scenarios), Judge and Engine cells (EV:41) | / Not disclosed [Not disclosed]. / [Not disclosed]. / DOCS | / [Not disclosed] (see Engine coverage). / [Not disclosed] (see Engine coverage). / DOCS | T61 (style) |
| Tools row 5, Tool cell (EV:42) | Playbook LitmusClient Python example (illustrative) | Playbook LitmusClient Python example (Code example tab) | T28: 'illustrative' was the drafter's word; the page labels the tab 'Litmus' under 'Code example' (edit) |
| Tools row 5, Evaluates cell (EV:42) | The code comment says it "returns category-level refusal scores" (conflict C8 with the docs' pass/fail per te… | The code comment (safety.mdx@45908b48:429-430) says it "returns category-level refusal scores" (conflict C8 w… | T11: comment lines located (edit) |
| Tools row 5, Inputs cell (EV:42) | (safety.mdx lines 432 to 437) | (safety.mdx@45908b48:432-438) | T11: locator corrected to file@ref:line (edit) |
| Tools row 5, Outputs cell (EV:42) | (safety.mdx line 440) | (safety.mdx@45908b48:440) | T11: locator form (edit) |
| Tools row 5, Judge and Engine cells (EV:42) | / Not disclosed. / [Not disclosed]. / https://github.com | / [Not disclosed] (see Engine coverage). / [Not disclosed] (see Engine coverage). / https://github.com | T61 (style) |
| Tools row 6 (Kaleidoscope), Judge cell (EV:43) | Yes: LLM judges, kept only when reliable [Documented: repo govtech-responsibleai/playbook@45908b48] | Yes: LLM judges "calibrated against human annotations"; "Only reliable judges are kept for wider scoring" [Do… | T31: paraphrase replaced by the page's own words (replace) |
| Tools row 6, Engine cell (EV:43) | no tags; not researched here) | no tags; its licence and code were not read, GovTech pages only) | T6 (R038): licence of the Kaleidoscope repository not researched, stated as such (edit) |
| Tools, note after the table | (none) | // Judge needed and Engine cells: the evaluator and the scoring engine are not published for any Litmus row (… | T61: one note replaces the repeated 'Not disclosed [Not disclosed]' cells (add) |

### 2.4 Datasets (20 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Datasets note (EV:47) | Typo (conflict C5): the Baseline+ introduction says "Baseline Tests consists of all 14 tests"; the heading an… | Wording (conflict C5): under the Baseline+ heading the page says "Baseline Tests consists of all 14 tests acr… | T42: 'typo' was an inference; page text stated plainly, reading labelled [Inferred] (replace) |
| Datasets, three standalone bullets after the note | (none) | • Taxonomy, docs test page (primary, most detailed): four categories Security, Specialised Advice, Undesirabl… | T41: the three taxonomies written side by side in the eval sheet (they were an Open question only) (add) |
| Datasets row 1 (Baseline Tests), Dataset cell (EV:51) | Baseline Tests (suite; suite id aiguardian-baseline-tests) | Baseline Tests (suite) | T35: the id-to-suite mapping is not stated by any page, so it leaves the name cell (edit) |
| Datasets row 1, Contents cell (EV:51) | The Getting Started table says "Use aiguardian-baseline-tests for our baseline tests". | The Getting Started table says "Use aiguardian-baseline-tests for our baseline tests" [Documented]; that this… | T35: same label as the inventory (id mapping [Inferred]) (edit) |
| Datasets row 1, Label cell (EV:51) | / [Documented]; size, licence, origin [Not disclosed] / | / [Documented]; id-to-suite mapping [Inferred]; size, licence, origin [Not disclosed] / | T35 (edit) |
| Datasets rows EV:53-66 (14 test rows, Contents cell; 14 edits) | [Security] / [Specialised Advice] / [Undesirable Content] / [Political Content] prefix | Category: Security. / Specialised Advice. / Undesirable Content. / Political Content. prefix | T43: look-alike bracket prefix replaced (kind hygiene) |
| Datasets row 12 (Domestic Affairs), Contents cell (EV:64) | The description says the test checks whether the model "refuses to answer", while the Outcome column says suc… | Description, conflict C13: the test assesses "whether the model refuses to answer due to potential misinterpr… | T39: both sides quoted in full, each labelled (replace) |

### 2.5 Published results (5 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Published results row 2 (one-pager), Conditions cell (EV:75) | (dated by file name, 2025-09-16) | (created 2025-09-16 per the PDF metadata) | T10 (edit) |
| Published results row 3 (per-test pass condition), Numbers cell (EV:76) | playbook page). / Test Information Documentation, "Outcome" column | playbook page). Conflict C14: the playbook warns that "A system that refuses every request may score well on… | T40: the playbook's refusal-based wording set beside the test-page pass conditions, both playbook deployments quoted (add) |
| Published results row 4 (category-level refusal scores), Label cell (EV:77) | / [To be verified] (premise for doubt: no Litmus page shows this output; the example is a code sample) / | / Code and comment [Documented: repo govtech-responsibleai/playbook@45908b48]; that Litmus returns this outpu… | T46: one label per thing (replace) |
| Published results row 4, Conditions cell (EV:77) | Illustrative code in the playbook Safety evals page, tab Litmus | Code example in the playbook Safety evals page, tab Litmus | T28: 'illustrative' was the drafter's word, the page gives no such label (edit) |
| Published results row 5 (ASR), Label cell (EV:78) | the playbook calls Litmus tests "refusal-based" | the playbook calls safety tests "refusal-based" on its staging page | T40: the 'refusal-based' sentence is on the staging page only (edit) |

### 2.6 Red-teaming (1 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Red-teaming, custom scenarios bullet (EV:89) | • "Custom scenarios" and "user simulation" exist as feature names only: "Custom workflow and user simulation… | • "Custom scenarios" and "user simulation" exist as feature names: "Custom workflow and user simulation / Des… | T48: quote [Documented] and absence [Not disclosed] split (replace) |

### 2.7 Engine coverage (18 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Engine coverage Summary (EV:94) | Summary: Litmus tests an application endpoint over HTTP; its scoring engine is not disclosed. The docs ask fo… | Summary: Litmus tests an application endpoint over HTTP; its scoring engine is not disclosed. Setup needs an… | T51 + T50 (main P5 ruling: resolver's new text): 'over HTTP' now backed by a Detail bullet; 'no statement on guardrailed endpoints' narrowed to 'no support statement' because the playbook speaks to guardrails in front of the tested endpoint (43 words excluding the label) (summary) |
| Engine coverage, example request bullet (EV:97) | • The example request body has the fields question, topic (empty list) and history (empty list), sent with an… | • The Getting Started example is a curl request with a Content-Type: application/json header, an x-api-key he… | T51: the bullet now carries the HTTP fact (replace) |
| Engine coverage, after EV:97 (two bullets) | (none) | • The Getting Started page names an API key twice: step 2 lists "API key for authentication" among the tenant… | T49: two API keys under one name written side by side; the reading is [Inferred] (add) |
| Engine coverage, after EV:102 (two bullets) | (none) | • Playbook on Sentinel and testing: "A guardrail in front of a system does not tell you what the system does… | T50: the two adjacent documented statements and the reading drawn from them (add) |
| Engine coverage, guardrailed-endpoint bullet (EV:103) | • An explicit statement that a guardrailed (for example Sentinel-protected) endpoint can be registered and te… | • An explicit statement that a guardrailed (for example Sentinel-protected) endpoint can be registered and te… | T50: checked list widened (replace) |
| Engine coverage, sample Action bullet (EV:105) | (action.yml line 28) | (action.yml@190600937062:28) | T11: locator form (edit) |
| Engine coverage, sample Action bullet (EV:105) | (lines 31 to 45; code read, not run) | (action.yml@190600937062:31-44, headers at 45; code read, not run) | T11: the JSON body is lines 31-44, headers line 45 (edit) |
| Engine coverage, Moonshot tag bullets (EV:106-108) | • Moonshot fact, MS at tag 0.5.0 (AI Verify Foundation repo, not a GovTech source): BenchmarkRunnerDTO has th… | • Moonshot fact, MS at tag 0.4.11 (2024-10-25, the last tag before the sample Action commit of 2024-10-29; AI… | T12 + T11: tag 0.4.11 (the tag in force at the sample Action commit) replaces 0.4.0; 0.5.0 shortened; 0.7.6 locator corrected (line 10, not 11); file@ref:line locators (replace) |
| Engine coverage, Moonshot tag 0.4.0 bullet (EV:107) | • Moonshot fact, MS at tag 0.4.0: the same DTO file text and the same route line as 0.5.0 (code read, not run… | (deleted) | T12: replaced by the 0.4.11 bullet above (DTO file byte-identical at 0.4.0, 0.4.11 and 0.5.0) (delete) |
| Engine coverage, Moonshot tag 0.7.6 bullet (EV:108) | • Moonshot fact, MS at tag 0.7.6 (latest tag, 2026-02-05): the route takes a required type of BenchmarkCollec… | (deleted) | T12: merged into the three-bullet replacement at EV:106 (delete) |
| Engine coverage, after the Moonshot tag bullets | (none) | • Licence of the cited code: Apache License 2.0 (LICENSE.md at 0.7.6; the same text at 0.5.0 and 0.4.11; AI V… | T7: licence of the cited third-party repository (R019) (add) |
| Engine coverage, possible-link bullet (EV:109) | (premise: the matches in the three bullets above; | (premise: the matches in the sample Action bullet and the Moonshot tag bullets above; | reference to 'the three bullets above' kept true after the new licence bullet was inserted between (style) |
| Engine coverage, after EV:109 | (none) | • Name resemblance only: moonshot-data@0.7.6 has the recipe jailbreak-dan ("assesses whether the system will… | T53: name resemblances with AI Verify data, no GovTech statement links them (add) |
| Engine coverage, engine bullet (EV:110) | (checked the docs, portal, playbook, one-pager, sample Action and the two GovTech GitHub organisations) | (checked the docs, portal, playbook, one-pager, sample Action, a GitHub repository search of the two GovTech… | T17 + T52: method of the organisation check named; Moonshot and AI Verify pages added (edit) |
| Engine coverage, host bullet portal (EV:111) | (PORTAL overview, read 2026-10-10; the staging host; not visited) | (PORTAL overview, read 2026-10-10; link target read from the page HTML with curl and the Python standard-libr… | T9: method for link-target facts (edit) |
| Engine coverage, host bullet Getting Started (EV:113) | (href in the page HTML; the visible text | (href in the page HTML read with curl and the Python standard-library parser, 2026-10-10; the visible text | T9: method for link-target facts (edit) |
| Engine coverage, host bullet sample Action (EV:114) | (action.yml line 28; the development host; not called) | (action.yml@190600937062:28; the development host; not called) | T11: locator form (edit) |
| Engine coverage, after EV:114 | (none) | • Host conflict C6, AI Guardian home page: the "Try Litmus Now" button links https://litmus.aiguardian.gov.sg… | T9 + T54 + T55 (CORRECTION: three hosts in five sources): fifth source of the production host (add) |

### 2.8 Reuse for the test bench (3 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Reuse, WOG taxonomy bullet (EV:120) | (for example Graphic Content, Race and Religion) | (by name: Graphic Content and Race & Religion; compared by name only) | T44: names as the playbook writes them; comparison by name only (edit) |
| Reuse, design-cautions bullet (EV:122) | may score well on refusal-based safety tests". | may score well on refusal-based safety tests" (PB tools/litmus.md@45908b48:53). | T40: the staging quote keeps its locator (edit) |
| Reuse, onboarding bullet (EV:124) | • Litmus is offered to public sector teams through onboarding, so a bench could treat it as a reference and n… | • Litmus is offered to public sector teams through onboarding, so a bench could treat it as a reference and n… | T58 (R032): proposal wording with its premise; 'any run would be a user decision' dropped (replace) |

### 2.9 Open questions (13 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Open questions, Moonshot (EV:130) | • Is Litmus built on or compatible with Moonshot (route and body fields match in the sample Action; no GovTec… | • Is Litmus built on or compatible with Moonshot (route and body fields match in the sample Action; no GovTec… | T52: no public source can answer it, so [Not disclosed] replaces [To be verified] (replace) |
| Open questions, AI Verify reuse (EV:131) | • Do any of the 14 tests reuse AI Verify cookbooks or datasets (a Jailbreak-DAN name resemblance only; not ch… | • Do any of the 14 tests reuse AI Verify cookbooks or datasets (name resemblances only, see Engine coverage;… | T53: relabelled; text points to the Engine coverage name-resemblance bullet (replace) |
| Open questions, host (EV:135) | production hosts in the playbook and Getting Started, | production hosts in the playbook, the Getting Started link and the AI Guardian home page, | T54: the AI Guardian home page also links the production host (edit) |
| Open questions, LitmusClient (EV:137) | • Does the LitmusClient Python example in the playbook exist as a package or API (conflict C7 on the suite na… | • Does the LitmusClient Python example in the playbook exist as a package or API (conflict C7 on the suite na… | T28: PyPI check recorded; still open (replace) |
| Open questions, guardrailed endpoint (EV:138) | (checked Getting Started, Overview, Troubleshooting, playbook page) | (checked Getting Started, Overview, Troubleshooting, the Sentinel docs pages and both playbook pages) | T50 (edit) |
| Open questions, eligibility (EV:139) | • Who may use Litmus: the playbook says "available to public sector teams" and the one-pager invites collabor… | • Who else may use Litmus: the playbook says "available to public sector teams", the Kaleidoscope docs say "f… | T4 (replace) |
| Open questions, maturity and terms (EV:140) | (checked the docs, portal, one-pager, playbook) | (checked the docs, portal, the developer portal Terms of Use and Privacy Statement, one-pager, playbook) | T3: Terms of Use and Privacy Statement added to the checked list (edit) |
| Open questions, Domestic Affairs (EV:143) | [To be verified] | [Not disclosed] | T39: no source can answer it; [Not disclosed] (edit) |
| Open questions, Kaleidoscope (EV:144) | • When does Kaleidoscope reach Litmus ("upcoming months"; the docs page shows no date)? [Not disclosed] | • Can Litmus tenants use Kaleidoscope today, and when will it reach Litmus (the playbook Litmus page calls it… | T32: one question aligned with the inventory caveat (replace) |
| Open questions, taxonomy (EV:145) | • Taxonomy: the portal lists four categories (Security, Undesirability, Specialised Advice, Political), the d… | (deleted) | T41: the three taxonomies are now Datasets bullets (delete) |
| Open questions, three 403 pages (EV:146) | • The pages https://www.aiguardian.gov.sg/litmus, https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-G… | (deleted) | T14: the HTTP facts moved to Overview Detail; Open questions carry only [To be verified] or [Not disclosed] (delete) |
| Open questions, onboarding guide (EV:147) | • Is the Getting Started page the "Litmus Onboarding Guide" that the portal links to? The portal says "To beg… | • Is the Getting Started page the "Litmus Onboarding Guide" that the portal links to? The portal says "To beg… | T15: [Inferred] is not an Open-question label (README section 6); relabelled [To be verified] (replace) |
| Open questions, last (new) | (none) | • Licence of the open-source Kaleidoscope repository and terms of the arXiv paper (not stated on the playbook… | T6: licence of the Kaleidoscope repository (class c, not researched per R038) (add) |

### 2.10 Reviewer notes (1 edits)

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Reviewer notes (EV:149-158), 9 notes | ## Reviewer notes (9 notes) | (moved to the change log, section 7a) | T62: README section 7 item 2; finals carry no Reviewer notes (delete) |

### 2.11 Brief conflict ids removed from parsed text (24 patterns, 28 occurrences)

| Before | After | Occurrences | Reason |
|---|---|---|---|
|  per test case (conflict C8). |  per test case. | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C4, not resolved) | (the sources conflict; not resolved) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C8 with the docs' pass/fail per test case) | (this conflicts with the docs' pass/fail per test case) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C11; DOCS Test-Information-Documentation) | (the page mixes both words; DOCS Test-Information-Documentation) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (no test_suites line, conflict C3) | (no test_suites line, although the parameter table marks it required) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C2) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1] | (the two Actions differ) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1] | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| with different inputs (conflict C2); and does the Getting Started example need `test_suites` (conflict C3)? | with different inputs; and does the Getting Started example need `test_suites`, which the parameter table marks required? | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C18) | (the step heading and the text differ) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Wording (conflict C5): | Wording: | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| "wog-baseline-v1", conflict C7) | "wog-baseline-v1", which differs from the id above) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C7 on the suite name `wog-baseline-v1` against `aiguardian-baseline-tests`) | (the suite name `wog-baseline-v1` differs from `aiguardian-baseline-tests`) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Description, conflict C13: | Description (the two texts differ): | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Conflict C14: | Conflict: | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C20) | (the two descriptions differ) | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C6: staging login link | (the hosts differ: staging login link | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| (conflict C4: portal | (the sources differ: portal | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| since the docs describe prompt testing only (conflict C10)? | since the docs describe prompt testing only? | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| playbook example), conflict C8? | playbook example)? | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Alignment, conflict C9 first side: | Alignment, first side of a minor difference: | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Alignment, conflict C9 second side: | Alignment, second side: | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Host conflict C6,  | Host conflict,  | 5 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Taxonomy, conflict C1, developer portal: | Taxonomy, developer portal (differs from the docs test page): | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Taxonomy, conflict C1, one-pager: | Taxonomy, one-pager (differs from both pages): | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |
| Kaleidoscope, conflict C12, playbook Kaleidoscope page: | Kaleidoscope, playbook Kaleidoscope page (it differs from the Litmus page): | 1 | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |

## 3. Inventory changes (litmus_inventory_final.md)

Blocks unchanged in count: (a) Access paths 4, (b) Test suites 5, (c) Integration parameters 6 (15 rows). Short-name renames (AIG to DOCS, DEV to PORTAL) are logged per line.

| Location | Before (shortened) | After (shortened) | Reason |
|---|---|---|---|
| Title (INV:1) | # Litmus inventory (draft, sheet 3x) | # Litmus inventory (final, sheet 3x) | 'draft' removed from the title (T62) (style) |
| Scope paragraph (INV:3) | so it has no Table 3 columns (R003) and every Covered by cell carries the inventory-only marker (R011). | so it has no Table 3 columns and every Covered by cell carries the inventory-only marker. | T59: ruling ids removed (style) |
| Scope paragraph (INV:3) | Nothing was signed in to, submitted or called (R019): the web app, | Nothing was signed in to, submitted or called: the web app, | T59: ruling id removed (style) |
| Short-name legend, AIG/DOCS (INV:5) | (the AI Guardian Docusaurus site, no source repository found, unpinned) | (the AI Guardian Docusaurus site, v3.10.0 per the page's generator tag, deployed 2026-10-08 per the Last-Modi… | T8: evidence for the absence of a source repository and for the missing pin (edit) |
| Short-name legend, PB (INV:5) | the staging branch commit that matches the deployed page text "Last updated on Sep 14, 2026", as for Sentinel… | the staging branch commit, committed 2026-09-14; the README lists two deployments, staging at govtech-respons… | A1 (CORRECTION) + main P5 ruling: staging pin with a production-versus-staging note; T59: 'R007 item 7' removed (edit) |
| Short-name legend, hosts (INV:5) | Host names appear in four forms across pages (see the Litmus web app and Litmus API rows); none was visited. | Three hosts (production, staging, development) appear across five sources (see the Litmus web app and Litmus… | T55 (CORRECTION): three hosts in five sources, not 'four forms' (edit) |
| Block (a) intro (INV:9) | because access is by onboarding (a proposal, R032). | because access is by onboarding [Inferred]. Short names in the cells: DOCS = the AI Guardian docs at https://… | T58 (R032): proposal wording with its label, ruling id removed; T60: legend in the parsed intro so it reaches the sheet (edit) |
| (a) Litmus web app / Host or address (INV:13) | The DEV pages carry a "Login to Litmus" link to https://litmus.stg.aiguardian.gov.sg/login [Documented] (link… | The DEV pages carry a "Login to Litmus" link to https://litmus.stg.aiguardian.gov.sg/login [Documented] (link… | T9: method for link-target facts; home-page host added (same fact as the Engine coverage bullet) (edit) |
| (a) Litmus web app / Status (INV:13) | The AIG pages, the one-pager and the playbook describe an onboarding service and give no maturity label [Not… | The AIG pages, the AI Guardian home page, the one-pager and the playbook describe an onboarding service and g… | T21: checked list matches the eval sheet (all pages checked, no date or withdrawal of the portal label) (edit) |
| (a) Litmus web app / Caveats (INV:13) | is [To be verified]: the playbook names litmus.aiguardian.gov.sg and the portal link names litmus.stg.aiguard… | is [To be verified]: the playbook names litmus.aiguardian.gov.sg, the AI Guardian home page links the same pr… | T3 (checked list) + T54 (home page also links the production host) (edit) |
| (a) Litmus web app / Source URL (INV:13) | / Litmus web app / A web application for ad hoc testing: "For ad hoc application testing, choose from compile… | / Litmus web app / A web application for ad hoc testing: "For ad hoc application testing, choose from compile… | T9: the AI Guardian home page is cited for the home-page login link (url) |
| (a) Litmus API / Host or address (INV:14) | (link target read from the page, 2026-10-10). The sample Action posts | (link target read from the page HTML with curl and the Python standard-library parser, 2026-10-10). The sampl… | T9: method for link-target facts (edit) |
| (a) CI/CD integration / Host or address (INV:15) | returns HTTP 404 on github.com (checked 2026-10-10) [Documented] | returns HTTP 404 on github.com and "Repository not found" on git ls-remote (observed 2026-10-10; a private re… | T18: both methods for one fact, worded as in the eval sheet (edit) |
| (a) CI/CD integration / Source URL (INV:15) | ; https://github.com/dsaidgovsg/aiguardian-test-action ; https://github.com/dsaidgovsg/aiguardian-test-action… | ; https://github.com/dsaidgovsg/aiguardian-test-action/blob | T63: unpinned URL dropped; the pinned action.yml URL stays (url) |
| (a) Onboarding and access request / Needs (INV:16) | A public sector team, per the playbook sentence above [Documented: repo govtech-responsibleai/playbook@45908b… | The playbook states availability for public sector teams, not as a requirement: "Litmus is available to publi… | T4 (C15): removes the label mismatch with the eval sheet's eligibility question (replace) |
| (a) Onboarding and access request / Host or address (INV:16) | [Documented] (link target read from the page); the DEV Resources page links the same target [Documented] | [Documented] (link target read from the page HTML with curl and the Python standard-library parser, 2026-10-1… | T9: method for link-target facts (edit) |
| (a) Onboarding and access request / Status (INV:16) | The three addresses https://www.aiguardian.gov.sg/litmus, https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onbo… | The two addresses https://www.aiguardian.gov.sg/litmus and https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onb… | T14: the Sentinel wiki path is not a Litmus page and is dropped (the real Sentinel page is in the eval sheet) (edit) |
| (a) Onboarding and access request / Status (INV:16) | The Wayback availability API returned no snapshot for the three addresses (archived_snapshots empty, 2026-10-… | The Wayback availability API returned no snapshot for the two addresses (archived_snapshots empty, 2026-10-10… | T13: CDX result added; scope narrowed to the two addresses (edit) |
| (a) Onboarding and access request / Caveats (INV:16) | The three 403 pages most likely do not exist | The two 403 pages most likely do not exist | T14 (edit) |
| (a) Onboarding and access request / Caveats (INV:16) | (checked the AIG pages, the DEV pages, the playbook page and the one-pager) | (checked the AIG pages, the DEV pages and their Terms of Use and Privacy Statement, the playbook page and the… | T3: checked list (edit) |
| (b) Baseline+ / Caveats (INV:25) | under the Baseline+ heading, which looks like a copy error [Documented]. That the six Baseline Tests are all… | under the Baseline+ heading [Documented]. A copy error is the likely reading [Inferred] (premise: the Baselin… | T42 (copy error is a reading, labelled [Inferred]) + T35 (main P5 ruling: Baseline subset of Baseline+ is [Documented] in both files) (replace) |
| (b) wog-baseline-v1 / Where published (INV:26) | (website/docs/evaluating-ai-systems/safety.mdx, lines 427 to 440) | (safety.mdx@45908b48:429-440) | T11: locator in file@ref:line form; lines corrected to 429-440 (edit) |
| (b) wog-baseline-v1 / Caveats (INV:26) | Illustrative code. No package, client library or API page confirms that LitmusClient or this suite name exist… | The page presents it as a code example. No package, client library or API page confirms that LitmusClient or… | T28: 'illustrative' was the drafter's word; PyPI check recorded (replace) |
| (b) wog-baseline-v1 / Source URL (INV:26) | ; https://govtech-responsibleai.github.io/playbook/evaluating-ai-systems/safety/ / | / | T63: unpinned duplicate of the pinned safety.mdx URL dropped (url) |
| (b) Kaleidoscope / Tests included (INV:28) | "Kaleidoscope is a contextual, functional evaluation module within Litmus" [Documented] (playbook Kaleidoscop… | "Kaleidoscope is a contextual, functional evaluation module within Litmus" [Documented: repo govtech-responsi… | T63: playbook Kaleidoscope page pinned to 45908b48 (passages matched), repo label (edit) |
| (b) Kaleidoscope / Tests included (INV:28) | stay tuned for more updates to access it via Litmus" [Documented]. | stay tuned for more updates to access it via Litmus" [Documented: repo govtech-responsibleai/playbook@45908b4… | T63: repo label (edit) |
| (b) Kaleidoscope / Identifier (INV:28) | the repository was not researched here) [Documented] | the repository's licence and code were not read, GovTech pages only) [Documented] | T6 (R038): consistent with the eval sheet (edit) |
| (b) Kaleidoscope / Caveats (INV:28) | Whether it is already available to Litmus tenants is [To be verified]: | Whether Litmus tenants can use it today is [Not disclosed]: | T32: one question, one label across both files (no source can answer it) (edit) |
| (b) Kaleidoscope / Source URL (INV:28) | https://govtech-responsibleai.github.io/playbook/tools/kaleidoscope/ ; | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/… | T63: pinned URL replaces the live staging URL (url) |
| (c) base_url / Description (INV:36) | (link target read from the page, 2026-10-10) | (link target read from the page HTML with curl and the Python standard-library parser, 2026-10-10) | T9: method for link-target facts (edit) |
| INV line 5: short names | AIG x1, DEV x1 | DOCS x1, PORTAL x1 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 13: short names | AIG x6, DEV x3 | DOCS x6, PORTAL x3 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 14: short names | AIG x3, DEV x2 | DOCS x3, PORTAL x2 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 15: short names | AIG x7, DEV x0 | DOCS x7, PORTAL x0 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 16: short names | AIG x3, DEV x4 | DOCS x3, PORTAL x4 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 24: short names | AIG x5, DEV x1 | DOCS x5, PORTAL x1 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 25: short names | AIG x3, DEV x1 | DOCS x3, PORTAL x1 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 26: short names | AIG x1, DEV x0 | DOCS x1, PORTAL x0 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 27: short names | AIG x5, DEV x5 | DOCS x5, PORTAL x5 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 28: short names | AIG x1, DEV x0 | DOCS x1, PORTAL x0 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 38: short names | AIG x1, DEV x0 | DOCS x1, PORTAL x0 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 40: short names | AIG x1, DEV x0 | DOCS x1, PORTAL x0 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| INV line 41: short names | AIG x1, DEV x0 | DOCS x1, PORTAL x0 | T60: one name set (DOCS, PORTAL, PB, ACT) in both files (hygiene) |
| Reviewer notes (INV:43-50), 6 notes | ## Reviewer notes (6 notes) | (moved to the change log, section 7b) | T62 (delete) |

## 4. Conflict decisions

1. **Overview Summary: recommended text versus fallback (T20, T4, T21).** The resolver gave a recommended text with the eligibility and proof-of-concept qualifiers (44 words) and a fallback without them (39 words). Decision: the recommended text, per main P5 ruling. Every clause is backed by a Detail bullet: 'scores responses' (bullets 'Litmus tests a system' and 'How a run works'), 'web app or CI/CD' (new bullet quoting playbook line 25), 'available to public sector teams' (the TechPass and availability bullet), 'May 2025 portal page labels it proof of concept' (status source one). Label [Documented] (every clause rests on a quote).
2. **Playbook pin: staging versus production (A1, T40, T63).** Sources: the pinned file at staging 45908b48 and the production site (Last updated on Jul 29, 2026). Decision: keep the staging pin (R007 item 7 precedent); state both deployments in EV Version scope and the INV legend; the one sentence that differs (tools/litmus.md line 53) is written as two bullets or statements, each labelled (staging [Documented: repo ...@45908b48], production [Documented]) in Published results row 3. Main decides separately whether the Sentinel 3e note needs the same wording (queue: final-summary follow-up).
3. **Open-question labels (resolver note versus main's earlier 'no labels').** Resolver proposed [To be verified] or [Not disclosed] on every Open question and flagged the question; README section 6 and the NeMo and CyberSecEval finals use these labels. Decision: labels kept, per main P5 ruling; no [Inferred] or [Documented] remains in Open questions.
4. **Baseline subset of Baseline+ and the id mapping (T35).** EV Used-by column said [Documented], INV said [Inferred]. Decision: [Documented] in both (membership in each table is read directly), per main P5 ruling; the mapping 'aiguardian-baseline-tests selects the 6-test Baseline Tests suite' stays [Inferred] with its premise in both files.
5. **Eligibility label mismatch (T4, C15).** INV Needs cell said [Documented: repo ...] 'a public sector team'; EV Open question said no rule is stated. Decision: INV says the playbook states availability for public sector teams, not as a requirement, and that an explicit rule for others is [Not disclosed]; EV Open question restated to match.
6. **Terms-of-Use clause bullet (T3, T22).** The resolver's terms bullet mixed a quoted clause with an absence under [Not disclosed] and allowed a split. Decision: two bullets, the quoted clause [Documented] and the absence [Not disclosed] (one label per fact, README section 3 rule 5).
7. **Moonshot tag bullets (T12).** Draft cited 0.4.0, 0.5.0 and 0.7.6; the resolver replaced them by 0.4.11, 0.5.0 and 0.7.6. Decision: applied; the DTO file is byte-identical at 0.4.0, 0.4.11 and 0.5.0 so no fact is lost. The T61 suggestion to merge EV:105 (sample Action) with the 0.4.11 bullet was not applied: the two bullets carry different repo labels.
8. **T61 consolidation (advisory).** T61 proposed about 14 Engine bullets, about 15 Open questions, and 'Not disclosed (see Engine coverage)' in repeated Tools cells. Applied: the repeated Judge and Engine cells now read '[Not disclosed] (see Engine coverage)' with one note under the table (the bracket label is kept so each cell fact still ends with a label); EV:145 and EV:146 dropped, EV:147 one question, EV:130 and EV:131 relabelled. Not applied: bullet merges, because each remaining bullet carries a different label or source and the resolver's own text for T7, T9, T12, T49, T50 and T53 adds bullets. Final counts: Engine coverage 26 bullets, Open questions 18, Overview 34, Red-teaming 8, Reuse 10.
9. **EV:109 premise wording.** 'the matches in the three bullets above' stopped being true once the T7 licence bullet was inserted between the Moonshot tag bullets and the possible-link bullet (T12 said it stays correct). Decision: reworded to 'the sample Action bullet and the Moonshot tag bullets above'.
10. **Edits beyond the resolver's list (consistency, each logged).** EV:39 link-target method (T9 triage location); EV:77 Conditions cell 'Illustrative code' to 'Code example' (T28 wording); EV:114 locator form (T11); INV:13 Status checked list and Host cell home-page login link, plus the home-page URL in the Source cell (T21, T9, T54); INV:28 'the repository was not researched here' aligned with the EV Source cell (T6); EV Tools Judge and Engine cells in rows 2 to 5 (T61). Each follows a resolver finding for the same fact in the other file.
11. **Sentinel wiki path dropped (T14).** The draft listed https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Getting-Started (HTTP 403) as a third Litmus address. Decision: dropped from the Litmus sheets; it is not a Litmus page and the real Sentinel page (HTTP 200) is already in the Overview bullet 'Litmus and Sentinel share one interest form'.

## 5. Change counts and P8 config notes

- Logged edits: 122 in the eval sheet (98 entries plus 24 conflict-id rewrites covering 28 occurrences; the 14 Datasets bracket edits are 14 entries shown as one row), 44 in the inventory; 166 in total.
- Eval by kind (entries, excluding the conflict-id rewrites, which are style): add 15, delete 5, edit 30, hygiene 14, replace 23, style 9, summary 2; conflict-id rewrites: style 24.
- Inventory by kind: delete 1, edit 20, hygiene 13, replace 3, style 3, url 4.
- Resolution items touching text: eval 45 distinct T-ids, inventory 21 (table in section 8d). Items with no text change by design are listed there with the reason.
- Summaries changed: 2 of 3 (Overview, Engine coverage). Red-teaming is unchanged (36 words, 38 with label); see litmus_summaries_preview.md.
- Final eval sections and items (default parser order): Overview: 34 Detail bullets, 0 standalone bullets, 0 table rows; Tools: 0 Detail bullets, 0 standalone bullets, 6 table rows; Datasets: 0 Detail bullets, 3 standalone bullets, 16 table rows; Published results: 0 Detail bullets, 0 standalone bullets, 7 table rows; Red-teaming: 8 Detail bullets, 0 standalone bullets, 0 table rows; Engine coverage: 26 Detail bullets, 0 standalone bullets, 0 table rows; Reuse for the test bench: 0 Detail bullets, 10 standalone bullets, 0 table rows; Open questions: 0 Detail bullets, 18 standalone bullets, 0 table rows.
- Final inventory rows: (a) Access paths 4, (b) Test suites 5, (c) Integration parameters 6 (total 15).

### 5b. P8 config notes (gr-xlsx-writer) and P9 notes

- **Inventory sheet:** name '3x. Litmus Inventory' (20 characters; the letter is assigned at P8 in queue order, R003; Cloak is merged in parallel, so the letters may shift). New config module for the inventory (md = benchtest/drafts/litmus_inventory_final.md). BLOCKS (marker, bold title or None, expected rows): ('## (a) Access paths', 'Access paths', 4), ('## (b) Test suites', 'Test suites', 5), ('## (c) Integration parameters', 'Integration parameters', 6); 15 rows. Covered-by column name 'Covered by Table 3 column' in all three tables (the last-but-one column of each). Short-name legend is in the unparsed paragraph before block (a) and in the block (a) intro (parsed).
- **Markers tuple:** only '— (inventory only, not in Table 3)' (R011), on all 15 rows; legacy and planned are not used. **Panel:** there are no Table 3 columns, so the panel must not require a non-zero Table 3 count or a COUNTIF against Table 3 headers (queue: litmus P1 Q-C); suggested panel items are row counts per block and the number of inventory-only rows (15 of 15). No validators are needed (no crosswalk blocks). No registry prefix, no column IDs, nothing added to products.py MDS or HDR_RE for Table 3.
- **Eval sheet:** sheet name '3x. Litmus Eval Tooling' (23 characters with a one-letter prefix, at most 31), inserted right after the Litmus inventory sheet (R003). The builder needs MD = benchtest/drafts/litmus_eval_tooling_final.md, TITLE and NOTE; proposed TITLE '3x. GovTech Litmus Evaluation Tooling (hosted service, no release; playbook@45908b48)', proposed NOTE 'Evaluation-tool facts, the test list, published results and reuse assessment for the test bench (possible sources and suggestions, not decisions). Labels as in sheet 3.' SECTION_ORDER is unchanged; the file parses to 8 sections; the widest table has 8 columns (Tools). Notes under the Tools and Datasets headings carry the short-name legend and the Table 3 headers named.
- **Sheet 3e cross-reference:** the Overview bullet names 'sheet 3e, columns AA to AG' in plain text (sheet 3e is the Sentinel inventory; the Sentinel columns on sheet 3 are AA to AG). If the P8 writer renumbers sheets, only that plain-text mention changes.
- **URL check (P9):** 41 distinct URLs in the two finals (litmus_urls.txt is not written by the merger). Do NOT request (hard rule 5, R019, lessons 12): https://form.gov.sg/67a2f35fdd4157c04aed3cea; https://litmus.aiguardian.gov.sg/api/v1/; https://litmus.dev.aiguardian.gov.sg/api/v1/benchmarks; https://litmus.stg.aiguardian.gov.sg/login; https://litmus.aiguardian.gov.sg/login. Expected non-200 by design: https://isomer-user-content.by.gov.sg/22/6c4f97dc-3b8b-4701-8592-cd12d72012dd/20250916_Litmus%20and%20Sentinel%20one%20pager.pdf; https://github.com/dsaidgovsg/aiguardian-litmus-test; https://www.aiguardian.gov.sg/litmus; https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide (HTTP facts kept in the text; the one-pager PDF answers 403 to plain curl and 200 to a browser User-Agent; aiguardian-litmus-test is a missing repository). github.com blob pages answer 403 from the session proxy: check the raw.githubusercontent.com equivalent at the same ref. The unpinned live URLs https://govtech-responsibleai.github.io/playbook/tools/wog-safety-testing/ and https://govtech-responsibleai.github.io/kaleidoscope/ are plain-text references.
- **Checker lines (inventory):** table '(a) Access paths': 4 rows x 8 cols; '(b) Test suites': 5 rows x 7 cols; '(c) Integration parameters': 6 rows x 7 cols.

## 6. Remaining open items

Counts in the finals: eval sheet [To be verified] 8 and [Not disclosed] 65 bracket labels in the whole file (Open questions: [To be verified] 5, [Not disclosed] 13 of 18); inventory [To be verified] 6 and [Not disclosed] 25. Class (b) items stay open as [Not disclosed] or [To be verified] statements and Open questions; none is closed without a source.

### 6a. Class b items (needs testing, honest gap or vendor reply), unchanged in substance

| T-id | Class | Priority | Item | Where it stays open in the finals |
|---|---|---|---|---|
| T15 | b | L | Is the Getting Started page the Litmus Onboarding Guide the portal links to (no capture of the guide) | Open question [To be verified]; INV (a) onboarding row Caveats [Inferred] sentence |
| T21 | b (honest gap) | H | Maturity: portal 'PROOF OF CONCEPT' (19 May 2025) versus docs, one-pager and playbook with no label | Overview Summary carries the qualifier; Overview status bullets (source one [Documented], source two [Not disclosed]); Open question on maturity [Not disclosed]; INV (a) web app Status |
| T24 | b (honest gap) | L | No release, version or release notes for the hosted service | Overview [Not disclosed] bullet; INV scope paragraph |
| T25 | b (honest gap) | M | Litmus API: no reference page; result schema, auth beyond the API key, rate limits; base_url link versus sample Action route | Tools row 2; Engine coverage bullets; INV (a) API row Caveats |
| T26 | b (honest gap) | M | CI/CD Action identity: documented dsaidgovsg/aiguardian-litmus-test versus archived sample | Tools row 3; Open question [To be verified]; INV (a) CI/CD row |
| T27 | b (honest gap) | M | Parameter table versus example workflow (test_suites, num_of_prompts, run_name default) | INV block (c) rows; Open question on the Action name and test_suites |
| T29 | b (honest gap) | M | Custom scenarios, user simulation and generic-testing wording (UI glitches, devices, browsers) | Tools row 4; Red-teaming bullets; Open question [To be verified]; INV (b) custom row |
| T32 | b (honest gap) | M | Kaleidoscope status: module within Litmus versus 'stay tuned' versus 'upcoming months' | Overview bullets (three quotes); Open question [Not disclosed]; INV (b) Kaleidoscope row |
| T33 | b (honest gap) | H | Evaluator or judge mechanism and backing model | Overview bullet; Engine coverage bullet and Summary; Open question [Not disclosed]; Tools note |
| T36 | b (honest gap) | M | Per-test dataset size, provenance, licence, languages, cadence | Datasets note and Size/Licence cells; Reuse bullet; Open question [Not disclosed] |
| T37 | b (honest gap) | M | 'hundreds of curated prompts' versus num_of_prompts and the two suites | Open question [Not disclosed]; INV (c) num_of_prompts row |
| T38 | b (honest gap) | M | Pass or fail rule per test, scoring formula, report schema; docs pass/fail versus playbook refusal rate | Published results rows 1 to 4, 7; Open question [Not disclosed]; INV (b) wog-baseline-v1 row |
| T39 | b (honest gap) | M | Domestic Affairs: refuses versus neutral stance | Datasets row Domestic Affairs (both quoted); Open question [Not disclosed] |
| T45 | b (honest gap) | M | No published Litmus scores, sample report or schema | Published results rows 'Published Litmus scores' and 'Sample report' [Not disclosed] |
| T47 | b (honest gap) | H | Automated attack generation, mutation, adaptive or multi-turn red-teaming not described | Red-teaming Summary and bullet [Not disclosed]; Open question on multi-turn and other test types |
| T49 | b (honest gap) | M | Supported models, request and response formats, limits; two API keys under one name | Engine coverage bullets (key bullets added); Open question on guardrailed endpoints |
| T50 | b | H | Can a guardrailed (for example Sentinel-protected) endpoint be tested; how blocks are scored | Engine coverage [Not disclosed] bullet and Summary; Open question [Not disclosed] |
| T54 | b | M | Which host is current (production, staging, development) across five sources | Engine coverage host bullets (five); Open question [To be verified]; INV (a) rows 1 and 2 |
| T56 | b | M | Retrieval, tool-call, multimodal and multi-turn tests, languages tested | Open question [Not disclosed] |

### 6b. Residual parts of handled items (verdict PARTLY RESOLVED, STILL OPEN class c, or an open question left in the finals)

| T-id | Class | Item | Where it stays open |
|---|---|---|---|
| T3 | c | Litmus's own terms, pricing, quota, service levels, data handling and retention (the portal Terms of Use only say featured products have separate terms) | Overview [Not disclosed] bullets (terms and absence, data handling); Open question on maturity and pricing; INV (a) rows 1 and 4 Caveats |
| T4 | c | Eligibility rule for organisations other than public sector teams | Open question [Not disclosed]; INV (a) onboarding row Needs |
| T5 | c | Licence or reuse terms of the quoted GovTech material (no LICENSE in the playbook at 45908b48 or the Action repository) | Overview [Not disclosed] bullet |
| T6 | c | Licence of the Kaleidoscope repository and terms of the arXiv paper (not researched, R038) | new Open question [Not disclosed]; Tools row 6 Engine cell; INV (b) Kaleidoscope row |
| T10 | a (PARTLY) | Which official page links the one-pager PDF (none found on the AI Guardian, portal and playbook pages read) | change log only (no sheet text states it) |
| T28 | a (PARTLY) | Whether the LitmusClient example exists as a package or API (no GovTech package on PyPI; an unrelated project named litmus) | Open question [To be verified]; Tools row 5; INV (b) wog-baseline-v1 row |
| T53 | a (PARTLY) | Whether any of the 14 tests reuse AI Verify cookbooks or datasets (name resemblances only) | Open question [Not disclosed]; Engine coverage name-resemblance bullet |

### 6c. Closed by rulings or resolutions (not open)

- T1, T2: R038 (small inventory sheet; Kaleidoscope one Tools row, GovTech pages only).
- T7 (Apache-2.0 licence of moonshot, [Documented: repo aiverify-foundation/moonshot@0.7.6]), T8 (docs unpinned, source repository not found), T9, T12, T13, T14, T16 to T19, T22, T23, T30, T31, T34, T35, T40 to T44, T46, T48, T51, T52, T55, T57 to T63: applied as logged in sections 2 and 3.

### 6d. Follow-ups noted for main (not Litmus sheet items)

- A1: the Sentinel 3e note on the playbook pin (R007 item 7 rationale 'the deployed site is built from staging') may need the production-versus-staging note; main ruled this a final-summary follow-up (queue, litmus P5 Q1 to Q5).
- The T6 not-researched list: the Kaleidoscope repository (licence, code), the arXiv paper terms and the main branch contents were not read, per R038.

## 7. Moved Reviewer notes and process notes

### 7a. litmus_eval_tooling.md, 9 notes (verbatim)

- Sources read raw on 2026-10-10 with `python benchtest/tools/fetch_text.py`: the four AI Guardian Litmus docs pages, the docs home page, the five portal pages, the pinned playbook files (via raw.githubusercontent.com at the full SHA) plus the live playbook Litmus page, the Kaleidoscope docs page and arXiv abstract, the sample Action `action.yml`, Moonshot files at 0.4.0, 0.5.0 and 0.7.6. The one-pager PDF was downloaded with curl and a browser User-Agent (md5 6423235d77ce909ea5742e52d41d7c92, the same as the P1 copy) and read with pdftotext; the quotes come from `scratchpad/drafter/litmus_p1/onepager.txt`.
- Line numbers: lines cited for pinned files are file lines (fetch_text adds one status line at the top; subtracted). `action.yml` lines 28 and 46 follow that rule.
- The `base_url` link target `https://litmus.aiguardian.gov.sg/api/v1/` comes from the href in the raw page HTML (curl, standard-library regex), not from page text. It was not called.
- A mistaken request: while checking the Hugging Face dataset cards, one fetch went to `https://huggingface.co/api/datasets` (a public listing endpoint, one GET, no sign-in, nothing used from it). It is outside the "no API host" instruction, is not cited anywhere, and is reported to main.
- No Litmus statement about Moonshot exists. The Moonshot match is on the route, the query value and the body fields only; the sample Action dates from 2024-10-29 and is archived.
- Domestic Affairs: the page says in the description that the test checks whether the model "refuses to answer", and in the Outcome column that success is a "neutral stance". Kept both.
- The Self-Harm description ends "as long as they are out of context" (verbatim, odd wording); not quoted.
- The playbook code comment gives onboarding at `https://playbooks.aip.gov.sg/responsibleai/` (a different host from the GovTech playbook site and the AI Guardian site). Not visited and not cited as a source.
- Row counts: Overview 19 bullets; Tools 6 rows; Datasets 16 rows; Published results 7 rows; Red-teaming 7 bullets; Engine coverage 19 bullets; Reuse 10 bullets; Open questions 19 bullets.

### 7b. litmus_inventory.md, 6 notes (verbatim)

1. Row counts: (a) 4, (b) 5, (c) 6; total 15, equal to the brief targets, so the config module for the inventory (build_litmus_inventory.py, not yet written) can assert 4/5/6 and needs no change to the brief. The Covered by column uses the inventory-only marker on every row (R011, main's ruling "same for Litmus"); the config markers tuple must include it and the panel must not require a non-zero Table 3 count.
2. Source conflicts recorded in the cells, each side labelled: Action reference and inputs (documented litmus-test action versus the archived sample, C2); parameter table versus example workflow (test_suites, num_of_prompts, C3); suite identifiers aiguardian-baseline-tests versus wog-baseline-v1 versus type cookbook (C7); result shape pass or fail versus refusal rate (C8); web app and API hosts (litmus.aiguardian.gov.sg in the playbook and the base_url link, litmus.stg.aiguardian.gov.sg in the portal "Login to Litmus" link, litmus.dev.aiguardian.gov.sg in the sample Action, C6); taxonomy (C1); maturity label (C4, only the portal says PROOF OF CONCEPT); Baseline+ introduction typo (C5); generic testing wording (C10); "model" versus "application" (C11).
3. Facts that come from link targets and not visible text: the base_url link (https://litmus.aiguardian.gov.sg/api/v1/), the portal "Login to Litmus" link (https://litmus.stg.aiguardian.gov.sg/login), the portal Onboarding Guide link (https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide) and the playbook login link. They were read from the raw HTML of the pages (anchors) on 2026-10-10 and not visited.
4. Unreachable: https://www.aiguardian.gov.sg/litmus, https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide (HTTP 403 AccessDenied, re-checked 2026-10-10 with fetch_text.py); https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Getting-Started (also 403, re-checked; the real Sentinel page is https://www.aiguardian.gov.sg/docs/sentinel/sentinel-getting-started, HTTP 200 at P1, not re-read here). The web app, the API, the interest form and the dev and staging hosts were not visited (R019). The demo project with litmus-test.yml is not linked anywhere read.
5. Judgement calls: (i) the mapping of aiguardian-baseline-tests to the 6-test Baseline Tests suite is labelled [Inferred]; (ii) "the six Baseline Tests are all in Baseline+" is read from the two tables and labelled [Inferred]; (iii) the Kaleidoscope row is kept in block (b) as a planned contextual suite and not researched beyond the playbook and docs pages (brief Q-B default); (iv) the one-pager pilot sentence is cited in the onboarding row only as an invitation to collaborate, not as an eligibility rule; (v) the Moonshot resemblance of the sample Action body is left to the evaluation-tooling sheet (Engine coverage) and not repeated here; (vi) the playbook example comment mentions "https://playbooks.aip.gov.sg/responsibleai/" for onboarding, a host not otherwise seen and not used.
6. Pages read with fetch_text.py (verbatim text): AIG Overview, Getting Started, Troubleshooting, Test Information Documentation; DEV five pages; playbook Litmus and Kaleidoscope pages; Kaleidoscope docs home; raw files from raw.githubusercontent.com at the pinned SHAs (action.yml, litmus.md, safety.mdx). Link targets from raw HTML (urllib with a browser User-Agent, GET only). The one-pager text is from the P1 pdftotext copy (md5 6423235d77ce909ea5742e52d41d7c92 recorded at P1), not re-fetched. No fact comes from a summarising fetch.

### 7c. Process, method and not-in-sheet notes from the resolutions (moved here per T16, T9, T19, T44, T42, T10, T8, T6)

- T16: one unauthenticated GET to https://huggingface.co/api/datasets outside the brief (nothing used or cited; covered by main's P4 Hub-metadata ruling); a browser User-Agent was needed only to download the one-pager PDF (md5 6423235d77ce909ea5742e52d41d7c92); every docs, portal, playbook and AI Guardian page answered plain curl with HTTP 200 (main P4 Q1: acceptable, logged, not repeated).
- T9: link targets (https://litmus.aiguardian.gov.sg/api/v1/, https://litmus.stg.aiguardian.gov.sg/login, the Onboarding Guide link, the playbook login link, the AI Guardian home page 'Try Litmus Now' link) were read from raw page HTML fetched with plain curl and the Python standard-library HTML parser, 2026-10-10 (R021); none was visited or called.
- T8 method: GitHub MCP repository search 2026-10-10 (litmus org:dsaidgovsg returns only dsaidgovsg/aiguardian-test-action, archived; litmus org:govtech-responsibleai returns 0; the govtech-responsibleai organisation lists 11 repositories, none a docs site for AI Guardian). The docs pages carry no edit link and no editUrl; Last-Modified Thu, 08 Oct 2026 08:42:14 GMT on all five docs pages.
- T10: no GovTech page read links the one-pager PDF (searched anchors for 'isomer' and '.pdf' on the AI Guardian home and docs pages, the five portal pages and the playbook Litmus page). PDF metadata CreationDate 2025-09-16, classification label 'Official (Open)'.
- T11 corrections: the triage premise 'line 46 cited for three different quotes' is accurate and not a defect (all three quotes are on line 46 of PB tools/litmus.md); the real defects were the safety.mdx range (429-441, comment 429-431), the action.yml body range (31-44, headers 45), benchmark_runner_dto.py@0.7.6 line 10, and the brief's '432-440' and the INV legend's '427 to 440' (brief and INV legend not carried into the finals).
- T19 / A1: the playbooks.aip.gov.sg host named in the LitmusClient code comment is the playbook's production site (README.md@45908b48:13 and :73-74); EV RN-8 and INV RN-5(vi) are dropped; no sheet text uses the host as a source.
- T44: the brief's list F21 of WOG taxonomy names (11) was short; the playbook table has 12 risk categories (Hateful L1 L2, Insults and Toxic, Sexual L1 L2, Self-Harm L1 L2, Graphic Content, Misconduct L1 L2, Domestic Politics, Geopolitics, Race and Religion, Financial Advice, Legal Advice, Medical Advice).
- T42: the Self-Harm description ends 'as long as they are out of context' (verbatim, odd wording); not quoted anywhere in the finals.
- T55: 'three hosts in five sources' (AI Guardian home page, PORTAL, playbook, the Getting Started link, the sample Action) replaces the brief's 'Four hosts' (the brief file is not edited).
- T6: not researched, per R038: the Kaleidoscope repository (licence and code), its main branch e806bf39bb4ccd1c5e8ab831ed8ef027fa4b5890 and the arXiv paper 2607.14673 terms.
- T28 / T53 / T52 non-vendor reads (main ruled acceptable, logged): a 2,158-byte wheel of an unrelated PyPI project named litmus was downloaded to scratchpad/resolver/litmus1/ and read as a zip (METADATA only, not installed or run); the PyPI simple index, the Internet Archive availability and CDX endpoints, playbooks.aip.gov.sg and aiverifyfoundation.sg pages were read with GET.
- Staging pin note: one compound command that would have created a bare clone under C:/t was denied by the permission system and not retried (resolver note).

## 8. Self-check

### 8a. Summary word counts (limit 45 excluding the trailing label; lessons 18 asks for at most 44)

| Section | Words excl. label | Words incl. label | `**` count | Code chars | Result |
|---|---|---|---|---|---|
| Overview | 44 | 45 | 4 | none | pass |
| Red-teaming | 36 | 38 | 4 | none | pass |
| Engine coverage | 43 | 45 | 4 | none | pass |

### 8b. Items per section

| Section | Detail bullets | Standalone bullets | Tables | Table rows | Bullets without a label |
|---|---|---|---|---|---|
| Overview | 34 | 0 | 0 | 0 | 0 |
| Tools | 0 | 0 | 1 | 6 | 0 |
| Datasets | 0 | 3 | 1 | 16 | 0 |
| Published results | 0 | 0 | 1 | 7 | 0 |
| Red-teaming | 8 | 0 | 0 | 0 | 0 |
| Engine coverage | 26 | 0 | 0 | 0 | 0 |
| Reuse for the test bench | 0 | 10 | 0 | 0 | 0 |
| Open questions | 0 | 18 | 0 | 0 | 0 |

### 8c. Labels, structure and process wording

- Open-question labels: Not disclosed 13, To be verified 5 of 18 bullets; none other.
- Bracket forms in the eval final: [Documented] 73, [Documented: repo aiverify-foundation/moonshot-data@0.7.6] 1, [Documented: repo aiverify-foundation/moonshot@0.4.11] 1, [Documented: repo aiverify-foundation/moonshot@0.5.0] 1, [Documented: repo aiverify-foundation/moonshot@0.7.6] 2, [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1] 6, [Documented: repo govtech-responsibleai/playbook@45908b48] 26, [Inferred] 24, [Not disclosed] 65, [To be verified] 8; every bracket is an allowed form (scan: none outside the allowed set).
- Bracket forms in the inventory final: [Documented] 69, [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1] 12, [Documented: repo govtech-responsibleai/playbook@45908b48] 13, [Inferred] 6, [Not disclosed] 25, [To be verified] 6; none outside the allowed set.
- Pinned refs (every repo label has the pinned URL with the same ref in the file): govtech-responsibleai/playbook@45908b48 x39, URL with 45908b48: yes; dsaidgovsg/aiguardian-test-action@v0.0.1 x18, URL with 19060093: yes; aiverify-foundation/moonshot@0.4.11 x1, URL with ab4dbbad: yes; aiverify-foundation/moonshot@0.5.0 x1, URL with f1b816c0: yes; aiverify-foundation/moonshot@0.7.6 x2, URL with 03e9344d: yes; aiverify-foundation/moonshot-data@0.7.6 x1, URL with 30fac123: yes.
- Process wording in the finals (counts; 0 expected): EV /R0\d\d/ 0; EV /Reviewer notes/ 0; EV /this draft/ 0; EV /I checked/ 0; EV /see above/ 0; EV /\bT\d{1,2}\b/ 0; EV /\(draft/ 0; INV /R0\d\d/ 0; INV /Reviewer notes/ 0; INV /this draft/ 0; INV /I checked/ 0; INV /see above/ 0; INV /\bT\d{1,2}\b/ 0; INV /\(draft/ 0.
- Inventory: no '**', no backtick in the final (checked); every Covered-by cell is '— (inventory only, not in Table 3)' (15 of 15); row counts per block (a) Access paths 4, (b) Test suites 5, (c) Integration parameters 6.

### 8d. Resolution items: edits per T-id (logged entries mentioning the id; section 2 for the eval sheet, section 3 for the inventory)

| T-id | Verdict (resolver) | Eval edits | Inventory edits | If none |
|---|---|---|---|---|
| T1 | RESOLVED (ruling R038) | 0 | 0 | closed by R038 (CP1): small inventory sheet yes; Kaleidoscope one Tools row; no text change |
| T2 | RESOLVED (ruling R038) | 0 | 0 | closed by R038 (CP1); no text change (the Kaleidoscope Source cell wording is T6) |
| T3 | PARTLY RESOLVED | 2 | 2 |  |
| T4 | PARTLY RESOLVED | 3 | 1 |  |
| T5 | STILL OPEN (checked playbook root, README, CONTRIBUTING, ACT root, footers; not stated) | 1 | 0 |  |
| T6 | STILL OPEN (not researched, R038) | 2 | 1 |  |
| T7 | RESOLVED | 1 | 0 |  |
| T8 | RESOLVED | 1 | 1 |  |
| T9 | RESOLVED | 4 | 5 |  |
| T10 | PARTLY RESOLVED | 3 | 0 |  |
| T11 | CORRECTION | 9 | 1 |  |
| T12 | RESOLVED | 3 | 0 |  |
| T13 | RESOLVED | 1 | 1 |  |
| T14 | RESOLVED | 2 | 2 |  |
| T15 | STILL OPEN (checked portal, Getting Started, playbook, archive) | 1 | 0 |  |
| T16 | RESOLVED | 0 | 0 | process note; moved to section 7 with the one-GET and User-Agent facts; nothing in the sheet text |
| T17 | RESOLVED | 2 | 0 |  |
| T18 | RESOLVED | 2 | 1 |  |
| T19 | RESOLVED | 0 | 0 | host playbooks.aip.gov.sg: no sheet text uses it; EV RN-8 and INV RN-5(vi) go to section 7; pin correction is A1 |
| T20 | RESOLVED | 4 | 0 |  |
| T21 | STILL OPEN (checked all pages; no date or withdrawal) | 2 | 1 |  |
| T22 | RESOLVED | 3 | 0 |  |
| T23 | RESOLVED | 1 | 0 |  |
| T24 | STILL OPEN (no release history; checked pages and HTTP headers) | 0 | 0 | stays open as drafted: [Not disclosed] bullet 'No version, release number or release notes' (Overview) |
| T25 | STILL OPEN | 0 | 0 | stays open as drafted: Tools row 2 and the INV API row ([Not disclosed] and [To be verified] cells) |
| T26 | STILL OPEN (+ C18 bullet) | 1 | 0 |  |
| T27 | STILL OPEN | 0 | 0 | stays open as drafted: INV block (c) carries both sides; EV Open question on the Action name and test_suites |
| T28 | PARTLY RESOLVED | 3 | 1 |  |
| T29 | STILL OPEN | 0 | 0 | stays open as drafted: Open question on UI testing wording [To be verified] |
| T30 | RESOLVED | 2 | 0 |  |
| T31 | RESOLVED | 1 | 0 |  |
| T32 | STILL OPEN (+ C12 bullets) | 2 | 1 |  |
| T33 | STILL OPEN | 0 | 0 | stays open as drafted (Engine Summary keeps 'no judge model'); repeated Tools cells merged by T61 |
| T34 | RESOLVED | 0 | 0 | counts confirmed (2 suites, 6 and 14 tests, 4 categories, 8 Baseline+-only, 12 WOG categories); no change |
| T35 | RESOLVED | 3 | 1 |  |
| T36 | STILL OPEN | 0 | 0 | stays open as drafted: Datasets Size/Licence cells and the Open question on dataset sizes |
| T37 | STILL OPEN | 0 | 0 | stays open as drafted: Open question on 'hundreds of curated prompts' versus num_of_prompts |
| T38 | STILL OPEN | 0 | 0 | stays open as drafted: Published results rows and Open question on the pass or fail rule |
| T39 | STILL OPEN (+ C13 text) | 2 | 0 |  |
| T40 | RESOLVED | 3 | 0 |  |
| T41 | RESOLVED | 2 | 0 |  |
| T42 | RESOLVED | 1 | 1 |  |
| T43 | RESOLVED | 14 | 0 |  |
| T44 | RESOLVED | 1 | 0 |  |
| T45 | STILL OPEN | 0 | 0 | stays open as drafted: Published results rows 'No published scores' and 'Sample report' |
| T46 | RESOLVED | 1 | 0 |  |
| T47 | STILL OPEN | 0 | 0 | stays open as drafted: Red-teaming Summary unchanged (36 words) and the [Not disclosed] bullet |
| T48 | RESOLVED | 1 | 0 |  |
| T49 | STILL OPEN (+ C20 bullets) | 1 | 0 |  |
| T50 | STILL OPEN (checked Sentinel pages, playbook, sheet 3e; not stated) | 4 | 0 |  |
| T51 | RESOLVED | 2 | 0 |  |
| T52 | RESOLVED | 2 | 0 |  |
| T53 | PARTLY RESOLVED | 2 | 0 |  |
| T54 | STILL OPEN (+ new source) | 2 | 1 |  |
| T55 | CORRECTION | 1 | 1 |  |
| T56 | STILL OPEN | 0 | 0 | stays open as drafted: Open question on retrieval, tool-call, multimodal and multi-turn tests |
| T57 | RESOLVED | 0 | 0 | no text change (EV Engine bullet and INV endpoint row already list both sides) |
| T58 | RESOLVED | 1 | 1 |  |
| T59 | RESOLVED | 4 | 3 |  |
| T60 | RESOLVED | 1 | 14 |  |
| T61 | RESOLVED | 5 | 0 |  |
| T62 | RESOLVED | 2 | 2 |  |
| T63 | RESOLVED | 0 | 5 |  |

### 8e. Checker output (run from the repo root)

```
python benchtest/tools/check_drafts.py inventory benchtest/drafts/litmus_inventory_final.md
table '(a) Access paths': 4 rows x 8 cols
table '(b) Test suites': 5 rows x 7 cols
table '(c) Integration parameters': 6 rows x 7 cols
RESULT: 0 errors, 0 warnings

python -c "import sys; sys.path.insert(0,'benchtest'); import build_eval_sheet as B; print(len(B.parse_md('benchtest/drafts/litmus_eval_tooling_final.md')))"
8
```

The columns checker (check_drafts.py columns ... --final --expect N) is not run: Litmus has no Table 3 columns (R003) and no litmus_two_level.md exists. The inventory checker was run without --headers for the same reason (no Table 3 headers to compare; the Covered-by cells are markers only).

