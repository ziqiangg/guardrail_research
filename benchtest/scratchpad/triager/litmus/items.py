# -*- coding: utf-8 -*-
# Item data for the Litmus triage. key, group, text, loc, cls, src, prio, files
# cls codes: a, b (needs testing), bg (b honest gap), bc (b CP1 decision), c
# files: E = litmus_eval_tooling.md, I = litmus_inventory.md, B = brief / queue / rulings
ITEMS = []

def add(key, group, text, loc, cls, src, prio, files):
    ITEMS.append(dict(key=key, group=group, text=text, loc=loc, cls=cls, src=src, prio=prio, files=files))

G1 = "CP1 decisions"
G2 = "Licensing, terms and access (class c)"
G3 = "Pins, sources, provenance and process"
G4 = "Overview and Summary lines"
G5 = "Tools table"
G6 = "Datasets table"
G7 = "Published results"
G8 = "Red-teaming"
G9 = "Engine coverage"
G10 = "Reuse, style and merge hygiene"

# ---------------------------------------------------------------- G1
add("q_a", G1,
    "[CP1] Q-A separate inventory sheet `3x. Litmus Inventory` (drafted: 15 rows, blocks (a) access paths 4, (b) test suites 5, (c) integration parameters 6) or none (access paths, suites and parameters folded into the eval sheet). Evidence: R003 already pre-approves an inventory sheet per new product, so (a) needs no new-sheet ruling; 9 of the 15 rows restate eval content in other columns (INV(a) web app, API and CI/CD = EV Tools rows 1 to 3; INV(a) onboarding = EV Overview bullets 17 and 18; INV(b) Baseline and Baseline+ = EV Datasets suite rows; wog-baseline-v1 = Tools row 5; custom scenarios = Tools row 4; Kaleidoscope = Tools row 6); the 6 rows of block (c) have no eval-sheet row and carry the C2 and C3 differences against the sample Action; the README section 6 parser accepts several tables in one section, so (b) could move block (c) into a second Tools table.",
    "BR Inventory (Q-A, default and alternative); queue.md (explorer q01 row; litmus P1 Q-C); INV:13-16, INV:24-28, INV:36-41, INV RN-1 (INV:45); EV:38-43, EV:51-52",
    "bc",
    "User at CP1 (closes when chosen, NeMo b22 precedent). Letters are assigned at P8 and depend on Cloak (3l is the next free letter): (a) gives an inventory sheet then `Litmus Eval Tooling`, (b) the eval sheet alone; names are 20 and 23 characters (limit 31). Option (a) needs `build_litmus_inventory.py` (BLOCKS 4/5/6, inventory-only marker in `markers`, panel with no Table 3 count, queue Q-C); no Summary changes either way",
    "H", "EIB")

add("q_b", G1,
    "[CP1] Q-B Kaleidoscope scope: one Tools row plus mentions in Overview, the Datasets note and INV(b) with no repository research (drafted default), or treat it as its own evaluation-tool subject (own eval rows or sheet; repo `govtech-responsibleai/kaleidoscope` main e806bf39, no tags; paper arXiv 2607.14673; docs site). Evidence: the playbook calls it \"a contextual, functional evaluation module within Litmus\", open source today and reaching Litmus later (\"stay tuned\"; docs \"upcoming months\"); it evaluates functional quality (rubrics, persona-driven test sets, calibrated LLM judges), not safety or guardrails; R003 and CLAUDE.md pre-approve eval sheets only for Litmus and CyberSecEval, so a Kaleidoscope sheet needs a user ruling; the drafts read only the playbook page, the docs home and the arXiv abstract; its licence is unread (see {kal_lic}).",
    "BR Scope (Out of scope) and Q-B; queue.md (litmus P1 Q-B); EV:24-25, EV:43, EV:91, EV:144; INV:28; INV RN-5(iii) (INV:49)",
    "bc",
    "User at CP1 (a new sheet is not pre-approved). If the user wants more than a row: a separate product slug with its own P0 to P10 pass is cleaner than widening Litmus. Default needs no research",
    "H", "EIB")

# ---------------------------------------------------------------- G2
add("terms", G2,
    "Litmus terms of use, pricing, quota, service levels, data handling and retention (Litmus keeps the reports that tenants open for trends and comparisons, Overview step 4; the interest form was not opened) are all [Not disclosed]; the Troubleshooting page says \"subscription is active\", which hints at a subscription model that nothing else describes.",
    "EV:28, EV:140 (Open questions); INV:13 (web app caveats), INV:16 (onboarding caveats); BR F22 and Open items",
    "c",
    "Terms of use, privacy and cookie links in the footers of www.aiguardian.gov.sg and www.developer.tech.gov.sg (R019 allows reading terms pages); the interest-form page is not opened (R019). If no terms page mentions Litmus the [Not disclosed] stands, with the pages named",
    "M", "EI")

add("elig", G2,
    "Who may use Litmus. Playbook: \"available to public sector teams through AI Guardian\"; portal: a \"Testing as a Service\" platform for WOG developers; one-pager invites collaboration (\"Pilot with your AI applications to customise test suites\"); no explicit eligibility rule. EV Open question 139 says [Not disclosed], but INV(a) row 4 Needs cell turns the playbook sentence into a requirement under [Documented: repo ...] (label mismatch, see {label_mismatch}). The Overview Summary says nothing about access, and access decides whether anyone outside government can run Litmus.",
    "EV:6 (Summary), EV:17, EV:23, EV:139; INV:16 (Needs cell); INV RN-5(iv) (INV:49); BR Open items (eligibility), F14",
    "c",
    "Re-read the portal Overview and Getting Started, the one-pager section \"How to Collaborate\" and the playbook sentence; decide whether the Summary should carry \"available to public sector teams\" (word budget: the Summary has 44 words before its label). Eligibility for other organisations stays [Not disclosed] unless a page states it. Whether to request onboarding is the user's own decision outside research (R019)",
    "H", "EIB")

add("reuse_terms", G2,
    "Reuse terms of the quoted GovTech material: docs footer \"(c) 2026 AI Programme, GovTech\", playbook footer \"Copyright (c) 2025-2026 Government Technology Agency of Singapore\", the one-pager PDF and the portal carry no licence statement; the sample Action repository has one file (`action.yml`) and no LICENSE; the playbook repository licence at the pin is not recorded. Quotes stay under 40 words.",
    "EV:27, EV:3 (Version scope); INV:5; BR F22",
    "c",
    "LICENSE file of `govtech-responsibleai/playbook` at 45908b48 and of `dsaidgovsg/aiguardian-test-action` at v0.0.1 (file lists already read); site terms of use (same pages as {terms}). Record only; no legal reading",
    "L", "EIB")

add("kal_lic", G2,
    "Licence of the Kaleidoscope repository and terms of the arXiv paper are unread (Kaleidoscope is recorded as one row, repository not researched). Depends on {q_b}.",
    "EV:43 (Tools row 6); INV:28; BR Pin (Kaleidoscope)",
    "c",
    "Only if Q-B goes beyond one row: LICENSE of `govtech-responsibleai/kaleidoscope` main e806bf39 (no tags) and the paper page. Otherwise leave and say so in the change log",
    "L", "EIB")

add("ms_lic", G2,
    "Licence of the cited third-party repository `aiverify-foundation/moonshot` (AI Verify Foundation, not GovTech) is not recorded, although three tagged files are cited as the premise for the [Inferred] link; only route and field names are quoted. R019 says third-party component licences are listed citing each owner's page and marked as not the vendor's docs.",
    "EV:105-108, EV:3 (MS short name); INV RN-5(v) (INV:49)",
    "c",
    "LICENSE of `aiverify-foundation/moonshot` at 0.5.0 and 0.7.6 (already cloned or read); one plain-text note \"(AI Verify Foundation repo, not a GovTech source)\" is already in the bullets",
    "L", "E")

# ---------------------------------------------------------------- G3
add("docs_pin", G3,
    "The AI Guardian docs (Docusaurus site) carry no pin: the source repository was not located, so every docs fact is [Documented] with \"read 2026-10-10\". The drafts do not say whether the page HTML has an \"Edit this page\" or GitHub link, or whether a docs deploy repo exists.",
    "EV:3 (Version scope), EV:8-14; INV:3, INV:5 (AIG short name); BR Pin",
    "a",
    "Page HTML or sidebar footer of the docs site for an edit link or repository name; if a repo is found, match 2 or 3 distinctive passages (README section 3 rule 8) and pin; otherwise keep unpinned with the read date (Sentinel and Presidio precedent)",
    "M", "EIB")

add("anchors", G3,
    "Facts that come from link targets read in the raw page HTML and not from visible text: the `base_url` link `https://litmus.aiguardian.gov.sg/api/v1/`, the portal \"Login to Litmus\" link (staging host), the portal Onboarding Guide link, the playbook login link. They carry conflict C6 and the Onboarding Guide premise and are labelled [Documented]; the method was urllib with a browser User-Agent (see {procslip}).",
    "EV:39, EV:111-113, EV:152 (RN-3); INV:13, INV:14, INV:16, INV:36, INV RN-3 (INV:47), INV RN-6 (INV:50)",
    "a",
    "Re-read the anchors with `fetch_text.py` or plain curl (R021) and record the method in the scratchpad; keep \"not visited\" wording. If a link cannot be re-read, relabel [To be verified]",
    "M", "EI")

add("onepager", G3,
    "One-pager PDF provenance: read through pdftotext on a copy downloaded with curl and a browser User-Agent after plain curl got HTTP 403; it is dated only by its file name (2025-09-16); the drafts do not name which official GovTech page links it (the brief calls it a \"Global Overview Document\"). Quotes used: \"Testing-as-a-Service platform\", \"Pass/fail dashboards with remediation advice\", \"Pilot with your AI applications\", the domains \"toxicity, bias, misinformation, robustness\", the Key Metrics names.",
    "EV:23, EV:75, EV:150 (RN-1); INV:16; BR Official sources and F14",
    "a",
    "Find the portal Resources or Overview link that points to the PDF (establishes ownership and a date); re-check the five quoted phrases against a second extraction of the same file. R021 accepts a plain curl read; the User-Agent question is in QUESTIONS",
    "M", "EIB")

add("locators", G3,
    "Line locators into pinned files are inconsistent: the `LitmusClient` example is cited at safety.mdx lines 432-437 and 440 (EV:42), 432-440 (BR) and 427-440 (INV:26); playbook litmus.md \"line 46\" is cited for three different quotes (not a runtime defence; used together; Sentinel provides the runtime guardrails) and \"line 52\", \"line 57\", \"line 9\", \"line 17\" for others; the fetch_text status line shifts counts by one (EV RN-2).",
    "EV:15, EV:17, EV:21, EV:24, EV:42, EV:85, EV:90, EV:101-102, EV:112; INV:26; EV:151 (RN-2)",
    "a",
    "Re-read litmus.md, kaleidoscope.md, safety.mdx and action.yml at the pins and standardise `file@ref:line`; also the Moonshot DTO (lines 4-13), route (line 14) and types.py (lines 74-76)",
    "L", "EI")

add("ms_tags", G3,
    "Moonshot pins: three tags are cited (0.4.0 `958e7b91`, 0.5.0 `f1b816c0`, latest 0.7.6 `03e9344d`) but the drafts do not say which tag was current when the sample Action was written (2024-10-29) or that each SHA is the commit behind the tag.",
    "EV:105-108, EV:106-108 (blob URLs); BR Pin (Moonshot)",
    "a",
    "`git ls-remote --tags` with peeled commits and the tag dates (R013 shallow clone already available); state the tag nearest 2024-10-29 as the comparison point. Does not change the [Inferred] label",
    "L", "E")

add("wayback", G3,
    "Wayback claim is wider than the evidence: EV:146 says \"no Wayback snapshot found\" for all three 403 pages, but the brief records that the CDX query for the Sentinel wiki path could not be completed (Internet Archive offline; \"treat as not checked\"); INV:16 correctly says only the availability API was used.",
    "EV:146; INV:16; BR 403 section (Wayback paragraph)",
    "a",
    "Retry the CDX index for `Sentinel-Getting-Started` or narrow EV:146 to \"availability API returned no snapshot\" (R007 item 2: archived copies count as [Documented] with the date)",
    "L", "EIB")

add("p403", G3,
    "The three HTTP 403 pages (`/litmus`, `Litmus-Onboarding-Guide`, wiki `Sentinel-Getting-Started`) sit in Open questions as [Inferred] (\"most likely not published\"); README section 6 allows only [To be verified] or [Not disclosed] there, and README section 3 rule 7 says HTTP facts are [Documented]. The Sentinel wiki-path page is not a Litmus page (the real Sentinel page returns 200 and is a cross-reference only).",
    "EV:146, EV:147; INV:16; BR 403 section; queue.md (q03)",
    "a",
    "Move the HTTP facts (status, headers, made-up path also 403, date) to a Detail bullet labelled [Documented]; keep one [Inferred] conclusion with its premise; drop the Sentinel wiki path from the Litmus sheet or keep it in the INV onboarding row only. Whether the Getting Started page is the Onboarding Guide stays [Inferred] ({onboard_guide})",
    "M", "EIB")

add("onboard_guide", G3,
    "Is the live Getting Started page the \"Litmus Onboarding Guide\" that the portal links to (unreachable address)? Premise only: the portal says \"To begin, refer to this onboarding guide\", the Getting Started page carries onboarding steps, and the playbook says AI Guardian \"carries the current onboarding guide\"; no capture of the guide was found.",
    "EV:147; INV:16 (Caveats); BR 403 section; INV RN-5",
    "bg",
    "No public document is expected to answer (the only capture of the Getting Started page is 2026-05-13 and the guide path was never archived); keep [Inferred] with the premise",
    "L", "EIB")

add("procslip", G3,
    "Process slips to record: one unauthenticated GET to `huggingface.co/api/datasets` outside the brief (nothing used); browser-User-Agent GETs of docs pages, link anchors and the one-pager PDF after plain curl returned 403. main's log (litmus P2) already files the Hub listing under the P4 Hub-metadata ruling.",
    "EV:153 (RN-4), EV:150 (RN-1); INV RN-3, RN-6; main/log.md litmus P2 line; queue.md (purplellama P4 Q1 ruling)",
    "a",
    "Main ruling (CLAUDE.md hard rule 5; R019; R021; the HF-metadata precedent). Reads were GET-only on public pages; the open point is whether a spoofed browser User-Agent is acceptable (see QUESTIONS Q1). Record in the change log either way",
    "L", "EB")

add("repo_search", G3,
    "Absence claim without a named method: \"a repository search of the `dsaidgovsg` and `govtech-responsibleai` GitHub organisations for litmus finds only the archived sample Action\" does not say how the search was run (GitHub search, org listing, MCP, UI). README section 3 rule 2 asks for what was checked.",
    "EV:29, EV:110",
    "a",
    "State the method and date in the bullet (e.g. GitHub search through the MCP, org repository listing); no new research if the scratchpad notes record it (scratchpad/drafter/litmus_p1)",
    "L", "E")

add("gh404", G3,
    "The same fact has two methods: INV says the documented Action repository \"returns HTTP 404 on github.com\"; EV and the brief say `git ls-remote` returns \"Repository not found\".",
    "INV:15 (Host cell); EV:29, EV:40; BR Pin and C2",
    "a",
    "Choose one method (or give both) and one label; both are HTTP-level facts [Documented] with the date",
    "L", "EI")

add("aip_host", G3,
    "The `LitmusClient` code comment points to onboarding at `https://playbooks.aip.gov.sg/responsibleai/`, a host not seen elsewhere; noted and not cited. Whether it is a GovTech playbook mirror or another AI Programme site is not recorded.",
    "EV:157 (RN-8); INV RN-5(vi) (INV:49)",
    "a",
    "Read the playbook line at the pin for the exact comment; check the host's owner only through the playbook text or an official GovTech page (no visit if the sign-in is required). Low value; may be dropped from the Reviewer notes",
    "L", "EI")

# ---------------------------------------------------------------- G4
add("sum_lead", G4,
    "Overview Summary label and lead: the lead \"not a guardrail\" is a classification; the documented support is the playbook sentence \"Litmus tests a system; it does not defend one at runtime\" (repo-pinned) and the one-pager \"Sentinel operates during runtime\", while the R002 direction note itself is [Inferred] (EV:16). The Summary carries plain [Documented]. Also check \"before launch\" (documented by the one-pager \"pre-deployment\", not by the docs Overview) and \"scores the responses\" (playbook wording).",
    "EV:6 (Summary), EV:15, EV:16, EV:23; BR Overview target row",
    "a",
    "Reword the lead to the quoted language (a testing service that does not defend a system at runtime) or add the [Inferred] premise; confirm each Summary claim has a bullet (README section 4 rule 5). Word count is 44 before the label (45 with it), so the rewrite must not add words",
    "H", "E")

add("sum_status", G4,
    "Maturity conflict C4: the portal Overview shows \"PROOF OF CONCEPT\" (page dated 19 May 2025) while the docs, one-pager and playbook describe an onboarding service with no maturity label; the Overview Summary calls Litmus a hosted testing service and does not mention the label. Whether to add a qualifier is a Summary decision for the merger; the fact itself cannot be resolved from public pages.",
    "EV:6 (Summary), EV:19, EV:20, EV:140; INV:13 (Status cell); BR C4",
    "bg",
    "No page dates the change; the vendor does not say (checked portal, docs, one-pager, playbook). Keep both bullets as written; main or the merger decides whether the Summary carries \"portal label: proof of concept\"",
    "H", "EIB")

add("ov_bullets", G4,
    "Overview bullets that carry more than one fact under one label (README section 4 rule 5): EV:28 lists model, judge, dataset size, licence, terms, pricing, quota, data handling and retention as one absence; EV:29 joins an HTTP fact (\"Repository not found\") with an org-search absence; EV:20 and EV:26 hold two sources in one bullet (C4 second side, C9 two quotes).",
    "EV:20, EV:26, EV:28, EV:29",
    "a",
    "Split into one fact per bullet during merge (no new sources); keep \"checked ...\" lists per absence",
    "M", "E")

add("ov_naig", G4,
    "C9 NAIG wording: the docs Overview says \"aligned with public sector AI ethics, policies, and National AI Group (NAIG) guidelines\" and the docs home page omits NAIG; both quotes sit in one bullet under one label (README section 3 rule 4 asks for two bullets).",
    "EV:26; BR C9 and F3",
    "a",
    "Split into two bullets, each [Documented] with its page; no further source needed",
    "L", "E")

add("ov_version", G4,
    "No release, version, release notes or change history exist for the hosted service; the only dates are page-level \"Last updated\" lines (portal, playbook) and the site-wide footer date.",
    "EV:3, EV:30; INV:3, INV:15 (version for the Action not stated); BR Pin",
    "bg",
    "Vendor publishes none (checked docs pages, portal pages, playbook page). Nothing to resolve",
    "L", "EIB")

# ---------------------------------------------------------------- G5
add("api", G5,
    "Litmus API: no reference page, OpenAPI file or SDK page; request and response schema for results, authentication beyond the API key, rate limits and limits on other paths are [Not disclosed]; whether the `base_url` link target (production host) and the sample Action route `/api/v1/benchmarks` (development host, archived) describe the same API is [To be verified].",
    "EV:39 (Tools row 2), EV:105, EV:109; INV:14, INV:36; BR Open items",
    "bg",
    "No public document expected (checked the four docs pages, portal pages, playbook pages, sample Action). Answering needs onboarding, which is outside research (R019); stays open for a user-approved run or a vendor reply",
    "M", "EIB")

add("action", G5,
    "CI/CD Action identity (C2): the docs name `dsaidgovsg/aiguardian-litmus-test@<version>` (repository not found; the version value is never given) with inputs `base_url`, `run_name`, `endpoint`, `num_of_prompts`, `api_key`; the only public Action is the archived sample `dsaidgovsg/aiguardian-test-action@v0.0.1` with `run_name`, `litmus_key`, `endpoint`, `cookbpooks` (sic) and a hard-coded development host. Which is current, and whether the sample is an early form, is open.",
    "EV:40 (Tools row 3), EV:136; INV:15, INV:36-41; BR C2",
    "bg",
    "Vendor does not say; the Getting Started page is undated. Both sides are already written with labels; no further doc is expected. Closes only with vendor confirmation",
    "M", "EIB")

add("params", G5,
    "Parameter table versus example workflow (C3): the table marks `test_suites` and `num_of_prompts` required with default \"-\", but the example step has no `test_suites` line and sets `num_of_prompts` to `'1'` by default; the sample Action also gives `run_name` a default while marking it required (INV:37).",
    "EV:40, EV:133, EV:136; INV:37, INV:39, INV:40; BR C3",
    "bg",
    "Needs the live service or the vendor to say which is right; the INV block (c) carries both sides, the eval sheet one side only (see {q_a} for where this detail lives if no inventory sheet is built)",
    "M", "EIB")

add("client", G5,
    "Does the `LitmusClient` Python example exist as a package or API (C7: suite `wog-baseline-v1`, method `run_safety_suite`, output `refusal_rate`)? Drafts say no package, client library or API page confirms it ([To be verified]); the org search found only the sample Action. No check of PyPI or of the playbook's own wording around the example (\"illustrative\"?) is recorded.",
    "EV:42 (Tools row 5), EV:77, EV:137; INV:26; BR C7, F19",
    "a",
    "Read safety.mdx around lines 420-445 at the pin for any disclaimer; read-only look at a PyPI project page or index entry for a GovTech `litmus` package (main to confirm that a PyPI page read is allowed, as in the purplellama T19 question). If nothing, [To be verified] stands",
    "M", "EIB")

add("custom", G5,
    "Custom scenarios, user simulation and custom model testing exist as feature names and an email route only; format, authoring and availability are [Not disclosed]. C10: the portal says \"UI glitches, and bugs\", \"user simulation\" and \"Customisable testing scenarios\" and the Troubleshooting page says \"devices, browsers\", which read like general software testing while the docs describe prompt testing only.",
    "EV:41 (Tools row 4), EV:89, EV:142; INV:27, INV:46 (RN-2); BR C10, F13, F23",
    "bg",
    "Vendor wording only (checked docs, portal, playbook, one-pager). Both readings are recorded; do not infer UI testing. Stays open",
    "M", "EIB")

add("map_sent", G5,
    "Tools row 1 maps the web app's test themes to two Sentinel columns under [Inferred] (premise: test names equal the column's threat themes and harm categories). The two headers were compared with `sentinel_two_level.md` and match exactly (SN2 `GovTech Sentinel: Prompt-attack detection`, SN1 `GovTech Sentinel: Localised harmful-content classification (LionGuard 2)`). The Evaluates cell holds prose (README section 6 asks for sheet 3 headers or plain function names). LionGuard now has its own column (sheet 3 column BD, header `LionGuard: Localised harmful-content classification`), which the cross-reference does not mention.",
    "EV:38 (Tools row 1), EV:34 (Tools note), EV:118 (Reuse); BR Tools row 1",
    "a",
    "Write the cell as exact headers separated by semicolons plus a plain-function phrase; consider adding the LionGuard header after the P8 check that it is in the workbook; keep [Inferred]",
    "M", "E")

add("kal_wording", G5,
    "Kaleidoscope row wording to re-verify in the pinned playbook file: \"performs well for its intended users, tasks, and context\", rubrics \"in natural language\", \"persona-driven generation\", judges \"calibrated against human annotations\", and \"kept only when reliable\" (the last is a paraphrase under [Documented: repo ...]). Depends on {q_b}.",
    "EV:43 (Tools row 6), EV:91; INV:28",
    "a",
    "kaleidoscope.md at 45908b48 (lines near 9 and 22); replace paraphrases by short verbatim quotes or relabel [Inferred]",
    "L", "EI")

add("kal_status", G5,
    "Kaleidoscope status in Litmus (C12, new): the playbook Litmus page calls it \"the contextual evaluation module within Litmus\" (present tense) while the Kaleidoscope page says \"stay tuned for more updates to access it via Litmus\" and the docs home says Litmus is being extended \"in the upcoming months\". INV asks whether it is available to tenants now ([To be verified]); EV asks only when it arrives ([Not disclosed]).",
    "EV:24, EV:25, EV:43, EV:144; INV:28; BR F17, F20",
    "bg",
    "Vendor plan, no date on the docs home (checked the three pages). Align the two files to one question and one label; both quotes stay as separate bullets",
    "M", "EIB")

add("judge", G5,
    "Evaluator or judge mechanism and backing model for Litmus scoring are [Not disclosed] (\"automated internal evaluation\" only). The same absence is repeated in Overview, the six Tools rows (\"Judge needed\" and Engine cells), Engine coverage, Published results and Open questions, and is part of the Engine coverage Summary (\"no judge model\").",
    "EV:28, EV:38-43 (Judge needed and Engine cells), EV:94 (Summary), EV:104, EV:110, EV:129; BR Open items",
    "bg",
    "Vendor publishes none (checked docs, portal, one-pager, playbook, sample Action, the two GitHub organisations). Nothing to resolve; merge the repetitions into one Detail bullet and one Open question",
    "H", "E")

# ---------------------------------------------------------------- G6
add("counts", G6,
    "Headline counts: 2 suites, 6 Baseline tests, 14 Baseline+ tests, 4 categories, 8 Baseline+ only tests, and the per-test Used by column (Baseline and Baseline+ for DoAnythingNow, Medical, Hateful, Insults, Domestic Affairs, Social Policies). The drafter counted rows (EV RN-9 reports table counts); a P4 recount of the drafts agrees (6 + 8 = 14; 16 Datasets rows), but the page itself was not re-read here.",
    "EV:47, EV:51-66; INV:24, INV:25; BR F9, F10",
    "a",
    "Re-fetch Test-Information-Documentation with `fetch_text.py` and count the two tables and the Used by sentences; the figures appear in INV and the Datasets table, not in a Summary",
    "H", "EIB")

add("label_mismatch", G6,
    "Same fact, different labels across the two drafts: (i) `aiguardian-baseline-tests` selects the 6-test suite: EV:51 states the id in the suite row as a documented fact, INV:24 labels the mapping [Inferred] (premise: both say baseline; no page links them); (ii) the six Baseline tests all appear in Baseline+: EV Used by column is documented, INV:25 labels it [Inferred] (read from two tables); (iii) public-sector eligibility: INV:16 [Documented: repo ...], EV:139 [Not disclosed] (see {elig}).",
    "EV:51, EV:52, EV:53-66 (Used by); INV:24, INV:25, INV:16; INV RN-5(i)(ii)",
    "a",
    "Choose one label and basis per fact: the Getting Started sentence \"Use aiguardian-baseline-tests for our baseline tests\" is the only link, so [Inferred] with that premise is the safer form in both files",
    "M", "EI")

add("size", G6,
    "Per-test dataset size, prompts per test, provenance, licence and origin, languages and update cadence are [Not disclosed] for the 2 suites and 14 tests (the Overview says only \"hundreds of curated prompts\" per run); no prompt set is published, so there is nothing to download or redistribute.",
    "EV:47, EV:51-66, EV:126, EV:132; INV:24, INV:25; BR Open items",
    "bg",
    "Vendor publishes none (checked test page, Getting Started, Overview, Troubleshooting, five portal pages, playbook, GovTech HF dataset cards). Stays open",
    "M", "EIB")

add("hundreds", G6,
    "How \"hundreds of curated prompts\" (Overview), `num_of_prompts` (\"Value of 0 means run all prompts\"; example default 1; sample Action 1) and the two suites relate is not stated; the total prompt count of Baseline Tests or Baseline+ is not published.",
    "EV:12 (Overview step 2), EV:133; INV:40 (num_of_prompts row); BR Open items",
    "bg",
    "Vendor does not say (checked Overview and Getting Started). Stays open; the Summary does not quote the figure",
    "M", "EIB")

add("passrule", G6,
    "Pass or fail rule per test, scoring formula, thresholds and report schema are [Not disclosed]; only the qualitative Outcome column exists. C8: Getting Started and the one-pager say pass/fail per test case, the playbook example says category-level refusal scores.",
    "EV:74-80, EV:76, EV:134, EV:42; INV:26 (result shape); BR C8, F11",
    "bg",
    "Vendor publishes none (checked test page, Getting Started, Overview, portal, one-pager, playbook, sample Action). Both result shapes are already written with labels",
    "M", "EIB")

add("domestic", G6,
    "Domestic Affairs (C13, new): the test description says the test checks whether the model \"refuses to answer\", while the Outcome column says success is a model that \"maintains a neutral stance\"; both sit in one cell and EV Open question 143 labels the question [To be verified].",
    "EV:64, EV:143, EV:155 (RN-6)",
    "bg",
    "Page-internal wording; no other page decides it. Relabel the Open question [Not disclosed] if no source can verify it, or keep [To be verified] for a future run",
    "L", "E")

add("refusal_based", G6,
    "Cross-source conflict not yet recorded (C14, new): the playbook calls Litmus tests \"refusal-based\" and warns that a system that refuses every request may score well, but the docs test page's pass conditions for Medical, Financial, Legal, Geopolitics and Social Policies require substantive, balanced or limited answers, so a refuse-everything system would not pass those. The drafts quote the playbook sentence (EV:78, EV:122) and the Outcome text (EV:55-57, EV:65-66) separately and never set the two side by side.",
    "EV:55-57, EV:65-66, EV:78, EV:122; INV:26; BR F18, C8",
    "a",
    "Add two labelled bullets (README section 3 rule 4) or a Datasets note: playbook sentence [Documented: repo ...], test-page Outcome text [Documented]; no new source",
    "M", "E")

add("taxonomy1", G6,
    "Taxonomy conflict C1: the docs test page uses Security, Specialised Advice, Undesirable Content, Political Content (14 tests); the portal How it works lists four categories (Security, Undesirability with Toxic and Harmful, Specialised Advice with Medical, Political with Domestic and Social); the one-pager lists \"toxicity, bias, misinformation, robustness\". EV states only the docs-page taxonomy in the body and puts the other two in Open question 145 as [To be verified]; INV:24 carries all three.",
    "EV:47, EV:145; INV:24; BR C1, F12",
    "a",
    "Write the portal and one-pager taxonomies as two labelled facts in the Datasets note (README section 3 rule 4); the docs test page stays the primary (most detailed). Open question 145 can then be dropped",
    "M", "EI")

add("wording_defects", G6,
    "Page-internal wording defects: C5 (the Baseline+ introduction says \"Baseline Tests consists of all 14 tests\"; EV and INV call it a \"typo\" or \"copy error\", an inference labelled [Documented]); the Self-Harm description ends \"as long as they are out of context\" (odd, not quoted; EV RN-7).",
    "EV:47, EV:156 (RN-7); INV:25; BR C5",
    "a",
    "State the fact plainly (\"the introduction under the Baseline+ heading says Baseline Tests ... 14 tests\") and drop \"typo\"/\"copy error\", or label that reading [Inferred]; decide whether the Self-Harm sentence is worth one note",
    "L", "EI")

add("brackets", G6,
    "Label-lookalike category prefixes in the Datasets Contents cells (\"[Security]\", \"[Specialised Advice]\", \"[Undesirable Content]\", \"[Political Content]\") use the bracket form reserved for evidence labels; a label scan or a reader may take them for labels.",
    "EV:53-66 (14 rows)",
    "a",
    "Write \"Security:\" or \"(Security)\"; no source needed",
    "L", "E")

add("wog", G6,
    "Playbook WOG safety taxonomy: \"12 risk categories\" with levels L1 and L2, the ASR definition, and the claim that Graphic Content and Race and Religion are categories the 14 tests lack (brief F21 lists 11 names; Graphic Content is not among them). The framework page does not mention Litmus (searched the file).",
    "EV:47, EV:78, EV:120; BR F21",
    "a",
    "Re-read `website/docs/tools/wog-safety-testing.md` at 45908b48 (category list, level wording, metric section) and correct the Reuse bullet if a name is missing",
    "L", "E")

# ---------------------------------------------------------------- G7
add("no_scores", G7,
    "No published Litmus score, rate, count, agency result, sample report, scoring formula or report schema; one-pager Key Metrics (test coverage, pass/fail rates, automation frequency, integration speed, remediation cycle time) are programme metrics and not values.",
    "EV:74-80, EV:70, EV:75; BR Published results row",
    "bg",
    "Vendor publishes none (checked developer portal, docs, playbook, blog.ai.gov.sg homepage and evals tag, GovTech HF cards, one-pager). Re-check only if a Litmus announcement appears before P6",
    "M", "E")

add("refusal_label", G7,
    "The Published results row for the playbook refusal-score example carries [To be verified] on the whole row, but the documented part (the code comment and the printed `refusal_rate` field) is a code fact; the unverified part is that Litmus ever returns that output. One label for two things.",
    "EV:77, EV:42",
    "a",
    "Split the Label cell: code and comment [Documented: repo ...], real output [To be verified] (README section 4 rule 5 applies by analogy)",
    "L", "E")

# ---------------------------------------------------------------- G8
add("adaptive", G8,
    "Automated attack generation, prompt mutation, adaptive or multi-turn red-teaming for Litmus is not described (the Red-teaming Summary leads with it); the `history` field in the example body shows multi-turn input exists in the request shape but its test use is not stated.",
    "EV:83 (Summary), EV:88, EV:89, EV:141; BR Open items",
    "bg",
    "Vendor does not say (checked Overview, Getting Started, test page, Troubleshooting, five portal pages, one-pager, playbook). Stays [Not disclosed]",
    "H", "E")

add("rt_label", G8,
    "Red-teaming bullet EV:89 puts a documented quote (feature names under [Documented]) and an absence (\"how they work is not described\") in one bullet; the absence should be [Not disclosed] with what was checked.",
    "EV:89; INV:27",
    "a",
    "Split into two bullets",
    "L", "EI")

# ---------------------------------------------------------------- G9
add("models", G9,
    "Supported models, providers, endpoint types, request and response formats beyond the example body, size limits, timeouts and rate limits are [Not disclosed] (the Engine Summary says \"no list of supported models or guardrails\"). The `x-api-key` header in the example body is the tenant application's own key, separate from the Litmus API key.",
    "EV:94 (Summary), EV:96-97, EV:100, EV:138; INV:38 (endpoint row), INV:41 (api_key row)",
    "bg",
    "Vendor publishes none (checked Getting Started, Overview, Troubleshooting, test page, portal, playbook). Stays open",
    "H", "EI")

add("guardrailed", G9,
    "Can a guardrailed endpoint (for example one protected by Sentinel) be registered and tested, and how are blocks scored? Documented sides: the playbook says results \"describe whatever endpoint you registered\" and that Litmus and Sentinel \"are designed to be used together\"; an explicit statement is [Not disclosed]. The check names the Sentinel Overview docs page only; the real Sentinel getting-started page (`/docs/sentinel/sentinel-getting-started`, HTTP 200) and the playbook Sentinel page are not named as checked for a Litmus or testing statement.",
    "EV:94 (Summary), EV:101-103, EV:138; BR Engine coverage row and Open items; BR 403 section (real Sentinel path)",
    "a",
    "Residual docs check: Sentinel getting-started page, playbook `tools/sentinel.md` at 45908b48 and sheet 3e text for any statement about testing a guarded endpoint; if none, [Not disclosed] stands as an honest gap",
    "H", "E")

add("over_http", G9,
    "Engine coverage Summary says Litmus tests an application endpoint \"over HTTP\"; no Detail bullet says HTTP (bullets give a URL endpoint, an API key, a parameter specification and a JSON body with an `x-api-key` header). The Summary is 44 words before its two-word label and 46 with it (workbook count, lesson 18).",
    "EV:94 (Summary), EV:96, EV:97",
    "a",
    "Add an [Inferred] bullet (premise: URL, JSON body and header) or drop \"over HTTP\"; trim two words so the Summary stays at 45 or fewer with the label",
    "H", "E")

add("moonshot", G9,
    "Moonshot link: three code-fact bullets (sample Action; Moonshot 0.5.0 and 0.4.0; 0.7.6) plus one [Inferred] bullet and the engine [Not disclosed] (main ruling q02, not reopened). Open question 130 asks \"is Litmus built on or compatible with Moonshot\" under [To be verified], but no GovTech page can verify it; only AI Verify Foundation or Moonshot pages could mention Litmus or AI Guardian, and none were named as checked.",
    "EV:105-110, EV:130, EV:154 (RN-5); INV RN-5(v); BR F16, Open items; queue.md (q02)",
    "a",
    "Optional residual check: Moonshot README or docs and the AI Verify Foundation site for \"Litmus\" or \"AI Guardian\"; if nothing, relabel Open question 130 [Not disclosed] (it asks about vendor internals) and keep the [Inferred] bullet",
    "M", "EB")

add("cookbooks", G9,
    "Do any of the 14 tests reuse AI Verify cookbooks or datasets? Only a name resemblance is recorded (a Jailbreak-DAN recipe in `moonshot-data`); \"not checked beyond the name\" (EV:131).",
    "EV:131; BR Open items",
    "a",
    "Read the `aiverify-foundation/moonshot-data` cookbook and recipe names at a tag (R013) and list the matches against the 14 test names; the question about reuse stays [Not disclosed] or [To be verified]",
    "L", "E")

add("host_cur", G9,
    "Which host is current for the web app and the API (C6): portal \"Login to Litmus\" -> staging; playbook and Getting Started `base_url` link -> production; sample Action -> development. None was visited (R019).",
    "EV:111-114, EV:135; INV:13, INV:14, INV:5; BR C6",
    "bg",
    "Needs a visit or the vendor; the sources are quoted with their hosts. Stays [To be verified]",
    "M", "EIB")

add("host_count", G9,
    "Wording: C6 is described as \"four hosts\" (brief) and \"four forms\" (INV:5), but there are three distinct hosts (`litmus.aiguardian.gov.sg`, `litmus.stg.aiguardian.gov.sg`, `litmus.dev.aiguardian.gov.sg`) named in four places (portal, playbook, Getting Started link, sample Action).",
    "EV:111-114; INV:5; BR C6",
    "a",
    "Say \"three hosts in four sources\"; no source needed",
    "L", "EIB")

add("modalities", G9,
    "Retrieval, tool-call, multimodal (image or file) and multi-turn tests, and languages tested, are [Not disclosed].",
    "EV:141; BR Open items; INV:38 (endpoint row)",
    "bg",
    "Vendor does not say (checked Overview, Getting Started, test page, portal). Stays open",
    "M", "E")

add("model_vs_app", G9,
    "C11: the test page says \"model\" for some tests and \"application\" for others; the Overview says the tenant application forwards prompts to the LLM; INV:38 reads \"model endpoint\" as the application endpoint under [Inferred]. Both sides are written; no source decides.",
    "EV:99; INV:38; BR C11",
    "a",
    "Keep \"application endpoint\" as the documented object (Overview step 2); no further check",
    "L", "EI")

# ---------------------------------------------------------------- G10
add("r032", G10,
    "R032 wording audit of EV Reuse (10 bullets), INV(a) intro and the Reuse-style sentences elsewhere: every bench statement uses \"could\", \"possible\" or \"suggested\"; no decided plan found. Two tidy-ups: \"any run would be a user decision outside this research\" (EV:124) and \"(a proposal, R032)\" in a final cell (INV:9).",
    "EV:117-126; INV:9; EV:34",
    "a",
    "Remove the ruling id from INV:9 and the process phrase from EV:124; no bench-design question goes to the user (R032)",
    "L", "EI")

add("process_lang", G10,
    "Process language and ruling ids in parsed text: \"(R002)\" and \"in this draft\" in Overview bullet EV:16; \"(R019)\" in EV:18; \"(R003)\" in the Tools note EV:34; INV intro INV:9 and the INV(a) note cite R032; README section 4 forbids process language in finals (unparsed lines EV:3 and INV:3 also cite R019, R003, R011).",
    "EV:16, EV:18, EV:34, EV:3; INV:9, INV:3, INV:5",
    "a",
    "Product-neutral rewording at merge (\"Litmus has no Table 3 column\" without the ruling id)",
    "M", "EI")

add("shortnames", G10,
    "Short-name legends live in lines the parsers do not read (EV Version scope line 3; INV paragraph before `## (a)`), while parsed cells use DOCS, PORTAL, PB, ACT, MS (EV) and AIG, DEV, PB, ACT (INV): two names for the same sources, and the workbook cells may show abbreviations with no legend.",
    "EV:3, EV:8-147 (cells); INV:5, INV:13-41 (cells)",
    "a",
    "Check how the NeMo and Sentinel sheets handle the legend (README sections 5 and 6) and either spell the page names out in cells or put the legend in the parsed note; use one set of names across both sheets",
    "M", "EI")

add("overlong", G10,
    "Sections run past the brief's targets and repeat each other: Engine coverage 19 bullets (target about 8), Open questions 19 (about 12), Red-teaming 7 (about 5), Reuse 10 (about 8); the judge, dataset-size, eligibility and host absences each appear 3 to 5 times (Overview, Tools, Engine, Open questions).",
    "EV:6-30, EV:85-91, EV:96-114, EV:117-126, EV:129-147",
    "a",
    "Condense at merge; keep each absence once with its \"checked ...\" list and point the Open question to it",
    "L", "E")

add("rn_move", G10,
    "Reviewer notes sections (EV:149-158, INV:43-50) must leave the finals and move into `litmus_changes.md`.",
    "EV:149-158; INV:43-50",
    "a",
    "Merger",
    "L", "EI")

add("urls_unpinned", G10,
    "Source cells mix pinned and unpinned URLs: INV:15 lists the repository root `https://github.com/dsaidgovsg/aiguardian-test-action` beside the pinned blob URL; INV:26 and INV:28 list live playbook pages (`govtech-responsibleai.github.io/playbook/...`) next to pinned blobs; INV:28 cites the playbook Kaleidoscope page as plain [Documented] while the same row's Litmus quote carries the pinned repo label; EV uses the pinned `kaleidoscope.md` blob.",
    "INV:15, INV:26, INV:28; EV:43",
    "a",
    "Pin or drop (README section 3 rule 8; presidio T14 precedent: match 2 or 3 passages of the live page to the pinned file); the EV Kaleidoscope row already read the pinned file",
    "L", "EI")
