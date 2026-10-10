# Litmus workbook: fresh verifier review

Date of checks: 2026-10-10. Reviewer: gr-verifier (did not draft, triage, resolve or merge). Inputs read: CLAUDE.md, drafts/README.md, rulings R003, R011, R032 and R038 in full (R007, R015, R019, R020, R021 as applied in the files), queue.md rows naming litmus (P1 Q-B, Q-C; P4 Q1 to Q3; P5 Q1 to Q5; explorer q02, q03); litmus_eval_tooling_final.md and litmus_inventory_final.md (read in full), litmus_changes.md (read in full), litmus_resolutions_1.md (T11, T20 and the evidence lines named below), litmus_triage.md (T20 row, contradictions), litmus_summaries_preview.md (compared with the final). The originals litmus_eval_tooling.md and litmus_inventory.md were diffed with Python difflib, not re-read. Sources were re-read today with `python benchtest/tools/fetch_text.py` (raw text), plain curl or raw.githubusercontent.com at the pins: the four AI Guardian Litmus docs pages, the docs home and AI Guardian home pages, the Sentinel getting-started page, the five developer-portal Litmus pages and the portal Terms of Use, the one-pager PDF (downloaded with a browser User-Agent, md5 6423235d77ce909ea5742e52d41d7c92, read with pdftotext and pypdf metadata), the playbook files litmus.md, kaleidoscope.md, sentinel.md, wog-safety-testing.md and safety.mdx at 45908b48, the live staging and production playbook pages, action.yml at v0.0.1, Moonshot files at 0.4.0, 0.4.11, 0.5.0 and 0.7.6, moonshot-data at 0.7.6, the Kaleidoscope docs page, arXiv 2607.14673 and blog.ai.gov.sg/tag/evals. Link targets were read from raw page HTML with the Python standard-library parser. Public GitHub API (repository metadata, organisation listing, repository search), git ls-remote, the Internet Archive availability and CDX endpoints and the PyPI JSON pages were read with plain GETs. No sign-in, no form, no request to form.gov.sg, to any litmus.*.aiguardian.gov.sg host or to any /api/ path of those hosts, no install, nothing run. Scripts, page copies and URL results are in benchtest/scratchpad/verifier/litmus/. No file other than this one and that folder was modified.

## Verdict: PASS WITH FIXES

The merge is faithful to the triage, the resolutions and main's P5 rulings. Every substantive difference between the originals and the finals is in litmus_changes.md. The eval file parses into the 8 sections in parser order (build_eval_sheet.parse_md returns 8), and the inventory passes the checker with 0 errors and 0 warnings: (a) 4, (b) 5, (c) 6 = 15 rows, all 15 Covered-by cells carry the inventory-only marker. The three Summaries are 44, 36 and 43 words excluding the label (limit 45, lessons 18 target at most 44). The two CORRECTIONs (T11 locators, T55 three hosts in five sources) and the A1 staging pin note are applied. No leftover of "before launch", "four hosts", "four forms", "WOG AI Testing", conflict ids C1 to C21, ruling ids, T-ids, "this draft", "illustrative", "typo" or Reviewer notes remains in either final.

I spot-checked 44 facts at source: 43 MATCH and 1 MISMATCH. The mismatch is the repository count of the govtech-responsibleai organisation (fix 1). I requested 36 of the 41 distinct URLs (the 5 do-not-request URLs were skipped). 20 return 200. The 5 expected non-200 from changes.md 5b behave as expected, plus one base path. The github.com blob pages answered 503 or 504 intermittently, and all their raw.githubusercontent.com equivalents at the same ref return 200 (appendix).

There are 4 required fixes:

1. Eval Overview line 40: the govtech-responsibleai organisation has 12 public repositories, not 11.
2. Eval Engine coverage line 137: "do not read "built on Moonshot" into it" is an instruction to the reader (README section 4).
3. Inventory block (a) intro, line 9: "it is not a guardrail" is an unlabelled classification in a parsed note. It is the leftover of the Overview lead that T20 replaced with the quoted "does not defend one at runtime".
4. Inventory (c) endpoint row, Conflict or note cell: "so it expects a JSON string or object" is an inference under a `[Documented: repo …]` label.

None of the fixes changes a Summary, a row count or a headline fact.

## Required fixes

1. **Eval Overview line 40, organisation size: "(11 repositories)" (MISMATCH).**
   - Problem: the organisation listing `https://api.github.com/orgs/govtech-responsibleai/repos?per_page=100` returned 12 public repositories on 2026-10-10: playbook, KnowOrNot, RabakBench, experiment_knowornot, meta-evaluator, extend_KnowOrNot, CIRCLE, toolbox, agentic-risk-capability-framework, realtime-api-guardrail-demo, kaleidoscope, guardopt. All 12 were created before 2026-06 and none is archived; `public_repos` is also 12. The repository search for "litmus" in the organisation still returns 0, so the absence itself stands. The figure 11 probably came from the MCP search result (resolutions T8), not from an organisation listing.
   - Replace "and the `govtech-responsibleai` organisation (11 repositories) has none (checked 2026-10-10)" with: "and the `govtech-responsibleai` organisation (12 public repositories, listed 2026-10-10) has none (checked 2026-10-10)".
   - Also correct the T8 line in changes.md section 7c ("lists 11 repositories" to "lists 12 public repositories") and log the edit.

2. **Eval Engine coverage line 137: an instruction to the reader.**
   - Problem: the bullet ends "; do not read "built on Moonshot" into it **[Not disclosed]**". README section 4 says finals carry "no instructions to the reader". R032 also asks for suggestion wording and not directives.
   - Replace the tail "…and the Moonshot and AI Verify Foundation pages); do not read "built on Moonshot" into it **[Not disclosed]**" with: "…and the Moonshot and AI Verify Foundation pages); no source states that the hosted service is built on Moonshot **[Not disclosed]**".
   - Log it in changes.md section 2.7.

3. **Inventory block (a) intro (line 9): "Litmus tests an application, it is not a guardrail."**
   - Problem: T20 found that "not a guardrail" is a classification and not a quoted sentence. It replaced the Overview lead with "not a runtime defence", which rests on the playbook sentence, and kept the classification only as the `[Inferred]` Direction bullet (eval line 18). The block (a) intro is parsed into a merged note on the sheet. It still carries the classification, with no label. The inventory therefore says more, and more weakly sourced, than the eval sheet on the same fact.
   - Replace "All rows are inventory only: Litmus tests an application, it is not a guardrail." with: "All rows are inventory only: Litmus tests an application; it does not defend one at runtime [Documented: repo govtech-responsibleai/playbook@45908b48] (PB tools/litmus.md@45908b48:46)."
   - The PB pin is already defined in the same intro and the legend, so no Source URL change is needed. Log it in changes.md section 3.

4. **Inventory (c) endpoint row, "Conflict or note" cell (line 38): inference under a repo label.**
   - Problem: the cell reads "The sample Action inserts the value, unquoted, into a JSON array named endpoints, so it expects a JSON string or object [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1]". The insertion is in the file (action.yml lines 34 to 36: `"endpoints": [` / `${{ inputs.endpoint }}` / `],`). The conclusion "so it expects a JSON string or object" is the drafter's reading (README section 3 rule 5).
   - Replace that sentence with: "The sample Action inserts the value, unquoted, into a JSON array named endpoints [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1] (action.yml@190600937062:34-36). The value must therefore already be valid JSON, such as a quoted string [Inferred] (premise: it is placed unquoted inside a JSON array)."
   - The cell has no `|`, `**` or backticks. Log it in changes.md section 3.

## Optional suggestions

- **Mixed line-locator forms.** changes.md section 1 says that line locators moved to the "file@ref:line form". The eval final still has "(PB tools/litmus.md line 57)" (lines 19, 139), "line 46" (lines 24, 125), "line 9" (105), "line 52" (124), "(PB tools/kaleidoscope.md line 22" (112), "safety.mdx, line 17)" (111) and "(line 46)" for action.yml (130). The line numbers are all correct; I re-read each at the pin. T11 limited its edits to the wrong locators, so either convert the rest to `tools/litmus.md@45908b48:57` and so on, or narrow the section 1 row to "locators the resolver corrected".
- **Eval line 45: absence wording under `[Documented]`.** "No archived copy of either address: the Internet Archive availability API returned no snapshot …" opens with an absence claim. Suggested, matching the inventory's observation form: "The Internet Archive availability API returned no snapshot for either address and its CDX index no rows (checked 2026-10-10; control: one capture of Litmus-Getting-Started on 2026-05-13) **[Documented]**".
- **Eval Reuse line 151.** "Pass conditions in the test page depend on the application (for example "unless it is a medical chatbot")". The quoted words are in the Medical Description column ("…while avoiding misinformation or unverified claims, unless it is a medical chatbot"), and Financial has "unless it is a financial services specific chatbot". Neither is in the Outcome (pass condition) column. Suggested: "Some test descriptions depend on the application (Medical: "unless it is a medical chatbot"; Financial: "unless it is a financial services specific chatbot"), so a bench could record the application's purpose with each case. **[Inferred]**"
- **Eval Tools row 6 (line 58), Evaluates cell.** The last sentence, 'Described as "a contextual, functional evaluation module within Litmus".', has no label of its own. Append " [Documented: repo govtech-responsibleai/playbook@45908b48]", as the inventory Kaleidoscope row does for the same quote.
- **Eval Overview line 24.** "(sheet 3e, columns AA to AG, …)": columns AA to AG are on sheet 3, and 3e is the Sentinel inventory sheet. Suggested: "(Table 3 columns AA to AG and inventory sheet 3e, plain-text cross-reference)".
- **Inventory onboarding row, Needs cell.** "The GovTech one-pager (file name dated 2025-09-16)". The eval uses the stronger provenance from T10, "created 2025-09-16 per the PDF metadata" (CreationDate D:20250916121143+08'00', re-read today). Align the wording.
- **Eval Engine coverage Summary.** "No list of supported models or guardrails" is backed for models (line 123). For guardrails it is backed only indirectly, by line 128 on guardrailed endpoints. "No list of supported models or providers" would track line 123 exactly and keeps the word count at 43.
- **Moonshot bullets lines 132 and 133** do not repeat "(AI Verify Foundation repo, not a GovTech source)". The parsed Tools note defines MS that way, so this is only for readers who see the bullet alone.
- **Eval Open questions line 173** has two question marks (one after "links to?" and one at the end of the bracket). Drop the first, or end the bracket with a full stop.
- **Eval Tools note (line 49)** "Kaleidoscope is recorded as one row and its repository was not researched." is mild process wording on the sheet. "Kaleidoscope is one row, from GovTech pages only." says the same.
- **changes.md 5b.** Add `https://www.aiguardian.gov.sg/docs/wiki/` (the DOCS short-name base, HTTP 403 AccessDenied, no index object at that path) to the expected non-200 list. Also note that github.com blob pages answered 503 or 504 intermittently from this session, not 403.

## 1. Unlogged differences (Check 1)

Method:
- `scratchpad/verifier/litmus/diff_files.py` runs difflib SequenceMatcher on lines, then word-level diffs on each replaced line pair. Each fragment is searched (normalised 40 to 60-character prefixes) in changes.md and in resolutions_1.md.
- `diff_lines.py` and `diff_cells.py` diff the Tools and Datasets table rows and every inventory row cell by cell. They ignore the logged short-name renames AIG to DOCS and DEV to PORTAL.
- Every fragment not found by the prefix match was matched by hand.

Eval file:
- 39 changed regions.
- Each maps to a section 2 entry or to a section 2.11 conflict-id rewrite:
  - title "(draft," (2.1);
  - Version scope T8, A1 and R019 (2.1);
  - Overview Summary T20 (2.2);
  - bullets split or added for T20, T4, T21, T22, T10, T32, T23, T5, T3, T17, T18, T14 and T13 (2.2);
  - Tools note T59, T60 and T30, and rows 1 to 6 T30, T9, T11, T61, T18, T26, T28, T31 and T6, plus the note after the table (2.3);
  - Datasets note T42, three taxonomy bullets T41, row 1 T35, 14 "Category:" prefixes T43, Domestic Affairs T39 (2.4);
  - Published results T10, T40, T46, T28 and T40 (2.5);
  - Red-teaming T48 (2.6);
  - Engine Summary T51 and T50, and bullets T51, T49, T50, T11, T12, T7, T53, T17, T52, T9 and T54 (2.7);
  - Reuse T44, T40 and T58 (2.8);
  - Open questions T52, T53, T54, T28, T50, T4, T3, T39, T32, T41, T14, T15 and T6 (2.9);
  - Reviewer notes moved (2.10).
- The Overview Summary and the Engine coverage Summary are the only Summary changes. The preview matches the final for all three Summaries.

Inventory file:
- Every changed cell maps to a section 3 entry: scope paragraph T59; legend T8, A1 and T55; block (a) intro T58 and T60; web app row T9, T21, T3 and T54; API row T9; CI/CD row T18 and T63; onboarding row T4, T9, T14, T13 and T3; Baseline+ T42 and T35; wog-baseline-v1 T11, T28 and T63; Kaleidoscope T63, T6 and T32; base_url T9.
- Two small edits are covered only by the broader entry: the dropped "read 2026-10-10," in the Kaleidoscope row (with the T63 pin change) and the AIG/DEV renames (T60, per line).
- Row keys and row counts are unchanged.

Result: no substantive unlogged change.

## 2. Sourcing and label strength (Check 2)

- **Changed `[Documented]` facts trace to resolution evidence or the draft:**
  - From resolution evidence: T4 (Kaleidoscope audience quote), T3 (Terms of Use clause), T10 (PDF title and metadata), T13 and T14 (HTTP facts and CDX), T17 and T18 (404 and ls-remote), T20 (line 25 trigger quote), T23 (home-page wording), T26 (GitHub/Gitlab heading), T31 (judge quotes), T39 (Domestic Affairs both texts), T40 (staging and production refusal sentences), T41 (three taxonomies), T49 (two API keys), T50 (sentinel.md:95), T51 (curl example), T7, T12 and T53 (Moonshot and moonshot-data), T54 (home-page login link), T35 (Baseline names appear in both tables).
  - The merger-made Documented text is limited to consistency edits that conflict decision 10 names, and each restates a resolver finding for the same fact. I re-read every quoted text today; see the table in Check 4.
- **Inferences labelled Documented:**
  - Inventory (c) endpoint row (fix 4).
  - Eval line 45, an absence opening under `[Documented]` (optional).
  - I scanned both finals for "so", "therefore", "likely", "probably", "because", "thus" and "intended". The other hits are under `[Inferred]` (eval 18, 64, 135; inventory 9, 16, 25, 38 first half), inside a question (eval 158, 169) or inside a quote (eval 58). Two are a direct reading of quoted text: eval 98, under an `[Inferred]` Label cell, and inventory 40, where "a default exists in the example" is read from `|| '1'`.
- **Absence claims:** every `[Not disclosed]` bullet and cell names what was checked. The resolver's mixed Terms bullet is split, as conflict decision 6 says.
- **Leftovers that contradict a resolution:** "it is not a guardrail" in the inventory (a) intro (fix 3; T20). Nothing else: "before launch" 0, "four hosts" or "four forms" 0, "Sentinel-Getting-Started" 0, "three addresses" 0, "Illustrative" 0, "typo" 0, "Closed beta" 0, "WOG AI Testing" 0.
- **R032 wording in Reuse:** all ten bullets are proposals ("A possible use", "could be", "a bench could", "Suggested design cautions", "are suggested to be kept out of shared logs"). There are no hits for "the bench will", "bench rule", "we use", "should" or "must" (one "must" is inside an `[Inferred]` premise in Published results row 3). The block (a) intro reads "A bench could treat Litmus as a reference … [Inferred]".
- **Main's P5 rulings:**
  - The Open questions carry only `[Not disclosed]` (13) and `[To be verified]` (5).
  - Staging pin 45908b48 with the production-versus-staging note is in the Version scope and the INV legend. I verified that the production pages carry the cited litmus.md, kaleidoscope.md, safety.mdx and sentinel.md statements except the line 53 refusal sentence.
  - The Overview Summary is the resolver's recommended text (44 words).
  - The Engine Summary is the resolver's new text (43 words).
  - Baseline within Baseline+ is `[Documented]` in both files (eval Datasets "Used by" column and Label; inventory Baseline+ caveat). The id mapping is `[Inferred]` in both (eval Datasets row 1; inventory Baseline Tests row).
- **Eval versus inventory, same fact:**
  - These agree: hosts (three hosts, five sources); 404 plus ls-remote for aiguardian-litmus-test; 403 pages and the `[Inferred]` reading; Kaleidoscope availability today `[Not disclosed]` in both; LitmusClient `[To be verified]` in both; eligibility (availability `[Documented: repo …]`, rule `[Not disclosed]`); maturity (portal label `[Documented]`, others `[Not disclosed]` with the same checked list).
  - Two differ. The not-a-guardrail wording is fix 3. The one-pager date wording is optional.
  - The Kaleidoscope features are `[Documented]` in the inventory and `[Documented: repo …]` in the eval. Both are valid: the same features are on the Kaleidoscope docs page ("Define Custom Rubrics", "persona-driven generation", "Calibrate LLM Judges").
- **Moonshot "not GovTech":**
  - Each Moonshot or moonshot-data bullet carries its own repo label at a tag. Bullets 131, 134 and 136 state "AI Verify Foundation repo, not a GovTech source", and the parsed Tools note defines MS that way.
  - The link stays `[Inferred]` (line 135) and the engine `[Not disclosed]` (line 137), as main's explorer q02 ruling asks.

## 3. Summary entailment and style (Check 3)

- Parser: `build_eval_sheet.parse_md('benchtest/drafts/litmus_eval_tooling_final.md')` returns 8 sections, in the order Overview, Tools, Datasets, Published results, Red-teaming, Engine coverage, Reuse for the test bench, Open questions.
- Inventory checker: `python benchtest/tools/check_drafts.py inventory benchtest/drafts/litmus_inventory_final.md` gives "(a) Access paths: 4 rows x 8 cols", "(b) Test suites: 5 rows x 7 cols", "(c) Integration parameters: 6 rows x 7 cols", "RESULT: 0 errors, 0 warnings". There are no `**` or backticks in the inventory (grep count 0). The 15 of 15 Covered-by cells equal "— (inventory only, not in Table 3)". The columns checker does not apply (no Table 3 columns, R003).
- Word counts, excluding the label (with the label): Overview 44 (45), Red-teaming 36 (38), Engine coverage 43 (45). All are at or under limit minus 1. `**` counts are 4, 4 and 4. No backtick, underscore or `$` appears in any Summary.
- Bullets per section: Overview 34, Red-teaming 8, Engine coverage 26, Reuse 10, Open questions 18, Datasets 3 standalone. Every bullet ends with an allowed label. Bracket scan over both files: no non-standard form.
- Entailment:
  - **Overview:**
    - "not a runtime defence": line 15.
    - "scores an application's responses to curated prompts": lines 10 to 13 ("hundreds of curated prompts"; "automated internal evaluation of these responses").
    - "from a web app or CI/CD": lines 8 and 17.
    - "available to public sector teams": line 19.
    - "a May 2025 portal page labels it proof of concept": line 22.
    - Label `[Documented]`: every clause rests on a quote. Entailed.
  - **Red-teaming:** "curated adversarial prompts" (line 105), "variations of the DAN prompt" (line 107), and no mutation, automated generation or red-team automation (line 108). Entailed.
  - **Engine coverage:**
    - "over HTTP": line 118, the curl request.
    - "Setup needs an endpoint, an API key and a parameter specification": line 117.
    - "no list of supported models": line 123. "or guardrails" is backed only indirectly (optional).
    - "no judge model": line 129.
    - "no support statement for guardrailed endpoints": line 128.
    - Entailed.

## 4. Spot-checks at source (Check 4)

All reads were made on 2026-10-10. Pinned files were read raw at the pin. Line numbers are file lines, confirmed with plain `curl | grep -n`; fetch_text.py adds one status line, which was subtracted.

| # | Claim | Location | Source URL | Verbatim quote or value seen | Match |
|---|---|---|---|---|---|
| 1 | Multi-tenant SaaS, CI/CD and Web App | EV Overview 8 | https://www.aiguardian.gov.sg/docs/wiki/Litmus-Overview | "Litmus provides a multi-tenant SaaS service enabling development teams to perform frequent and seamless AI safety and security testing for Generative AI applications. It allows testing within the CI/CD pipeline and via a Web App" | MATCH |
| 2 | Testing as a Service for WOG; baseline assurance | EV Overview 9 | same | "The objective is to provide a "Testing as a Service" platform for WOG application developers"; "providing baseline assurance that AI applications mitigate risks" | MATCH |
| 3 | Four run steps | EV Overview 10-14; Red-teaming 106; Engine 121 | same | "2: Litmus sends hundreds of curated prompts to the tenant’s application, which then forwards them to the LLM."; "3: Litmus performs an automated internal evaluation of these responses and automatically generates a report."; "to analyse trends and make comparisons" | MATCH |
| 4 | NAIG wording versus home-page wording; footer | EV Overview 30-32 | same; https://www.aiguardian.gov.sg/docs/ ; https://www.aiguardian.gov.sg/ | "aligned with public sector AI ethics, policies, and National AI Group (NAIG) guidelines"; "aligned with public sector AI ethics, policies, and guidelines" (both home pages); "© 2026 AI Programme, GovTech" | MATCH |
| 5 | Does not defend at runtime; designed to be used together | EV 15, 24, 125; INV fix 3 | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/litmus.md | line 46 "Litmus tests a system; it does not defend one at runtime." … "The two are designed to be used together: Litmus identifies which risks your system actually exhibits, and Sentinel mitigates them in production." | MATCH |
| 6 | Not functional; Kaleidoscope module within Litmus | EV 16, 27 | same | line 17 "It does not evaluate whether your system does its job well." … "Kaleidoscope, which is the contextual evaluation module within Litmus." | MATCH |
| 7 | Run triggers | EV 17 | same | line 25 "You can trigger the same run manually from the web application, on a schedule, or from a CI/CD job on each commit or deployment" | MATCH |
| 8 | Curated adversarial prompts; on demand or CI/CD | EV 105; INV (a) web app | same | line 9 "It sends curated adversarial prompts at your AI system, scores the responses, and returns a report, either on demand through a web application or automatically from a CI/CD pipeline." | MATCH |
| 9 | Pitfalls: endpoint, refusal (staging and production) | EV 124, 96, 150 | same, line 52, 53; https://playbooks.aip.gov.sg/responsibleai/tools/litmus/ | "Results describe whatever endpoint you registered. If guardrails sit in front of your production endpoint but not the tested one, the scores describe a system nobody uses."; staging "A system that refuses every request may score well on refusal-based safety tests"; production "A system that refuses everything scores well on safety suites while being unusable" | MATCH |
| 10 | Availability, TechPass, production login link | EV 19, 139; INV (a) web app, onboarding | same, line 57 | "Litmus is available to public sector teams through [AI Guardian](https://www.aiguardian.gov.sg), which carries the current onboarding guide. The web application is at [litmus.aiguardian.gov.sg](https://litmus.aiguardian.gov.sg/login) and signs in with TechPass." | MATCH |
| 11 | Kaleidoscope page statements | EV 28, 58, 112; INV (b) | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/kaleidoscope.md | 9 "Kaleidoscope is a contextual, functional evaluation module within Litmus."; 15 "performs well for its intended users, tasks, and context"; 22 "Synthesise realistic, varied inputs using persona-driven generation."; 24 "calibrated against human annotations"; 26 "Only reliable judges are kept for wider scoring."; 39 "Try the open-sourced Kaleidoscope module today, or stay tuned for more updates to access it via Litmus." | MATCH |
| 12 | Guardrail is no substitute for testing | EV 126 | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/sentinel.md | line 95 "A guardrail in front of a system does not tell you what the system does without it. Test the system as well as defending it." | MATCH |
| 13 | Safety testing versus red-teaming; LitmusClient example lines | EV 111, 57, 97; INV (b) wog-baseline-v1 | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/evaluating-ai-systems/safety.mdx | 17 "Red-teaming generates novel prompts … while safety testing focuses on common attacks and is kept deliberately generic"; 429-430 "returns category-level refusal scores"; 432 `from litmus import LitmusClient`; 437 `suite="wog-baseline-v1",`; 440 `print(category, score.refusal_rate)` | MATCH |
| 14 | WOG framework: ASR definition, no Litmus mention, L1/L2, Graphic Content, Race & Religion | EV 64, 98, 148 | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/wog-safety-testing.md | "Attack Success Rate (ASR) measures how often a chatbot produces an unsafe response when given an adversarial prompt."; "litmus" occurs 0 times; rows "Hateful \| L1", "Graphic Content \| —", "Race & Religion \| —" | MATCH |
| 15 | Sample Action: host, body lines, headers, params, inputs, About, archive | EV 54, 55, 130, 141; INV (a), (c) | https://github.com/dsaidgovsg/aiguardian-test-action/blob/190600937062c100d0c10181e3edf71702230244/action.yml | 28 "url: https://litmus.dev.aiguardian.gov.sg/api/v1/benchmarks"; 31-44 JSON body (run_name … runner_processing_module, "num_of_prompts": 1); 45 `headers: '{"X-API-Key": ${{ inputs.litmus_key }}}'`; 46 `params: '{"type": "cookbook"}'`; inputs run_name (required, default "${{ github.workflow_ref }}/${{ github.run_id }}/${{ github.run_attempt }}"), litmus_key "key for litmus aa", endpoint, cookbpooks "cookcbooks to run against the model endpoint"; repository API: archived true, description "sample gha for litmus", tag v0.0.1 = main = 19060093 | MATCH |
| 16 | Onboarding steps, interest form, application details, curl example | EV 21, 117, 118; INV (a) onboarding, (c) endpoint | https://www.aiguardian.gov.sg/docs/wiki/Litmus-Getting-Started | "Fill up the Litmus and Sentinel interest form at https://form.gov.sg/67a2f35fdd4157c04aed3cea"; "We will reach out to you shortly with necessary steps to onboard thereafter"; "URL endpoint for your AI application" / "API key for authentication" / "API parameters specification"; `--header 'Content-Type: application/json'`, `--header 'x-api-key: …'`, `"topic": [], "history": []` | MATCH |
| 17 | CI/CD step: workflow file, action name and inputs, heading, Actions tab | EV 55; INV (a) CI/CD, (c) | same | "(.github/workflows/litmus-test.yml)"; "configures the CI pipeline to run safety checks automatically on each push and pull request."; "uses: dsaidgovsg/aiguardian-litmus-test@<version>"; base_url, run_name `${{ github.run_id }}-${{ github.run_attempt }}`, endpoint, num_of_prompts `${{ vars.NUM_OF_PROMPTS \|\| '1'}}`, api_key `${{ secrets.LITMUS_KEY }}`; no test_suites line; "c) Push Changes to GitHub/Gitlab"; "results visible under the Actions tab in your repository" | MATCH |
| 18 | Parameter table: six rows, Required Yes, Default "-" | INV (c) all rows | same | base_url "The base URL of the Litmus API server. ()"; run_name "A unique name for the test run. Best created using a composite workflow run unique ID"; endpoint "The model endpoint to be tested"; test_suites "A comma-separated string of test suite names. Use aiguardian-baseline-tests for our baseline tests"; num_of_prompts "Value of 0 means run all prompts"; api_key "API key provided by the AIGuardian team during onboarding"; each "Yes", "-" | MATCH |
| 19 | Web app ad hoc, results, custom model testing | EV 53, 56, 94; INV (a), (b) | same | "For ad hoc application testing, choose from compiled Baseline tests in the WebApp and hit "Run Tests" to begin."; "Analyse the test outcomes Litmus Website:"; "Results will show pass/fail status for each test case"; "Corrective measures and guardrails will be recommended for failing tests"; "Custom model testing can be requested at aiguardian@tech.gov.sg" | MATCH |
| 20 | Link targets: base_url, home "Try Litmus Now" | EV 140, 142; INV (a) API, web app; (c) base_url | same; https://www.aiguardian.gov.sg/ | anchor with empty text -> https://litmus.aiguardian.gov.sg/api/v1/; "Try Litmus Now" -> https://litmus.aiguardian.gov.sg/login (raw HTML, stdlib parser; not visited) | MATCH |
| 21 | Portal Overview: PROOF OF CONCEPT, page date, Login link, footer, customisable | EV 22, 138; INV (a) web app, (b) custom | https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/overview | "PROOF OF CONCEPT"; "Last updated 19 May 2025"; "Login to Litmus" with href https://litmus.stg.aiguardian.gov.sg/login; "© 2026 Government of Singapore. Last Updated 08 Oct 2026"; "Customisable testing scenarios" | MATCH |
| 22 | Portal Features: API, custom workflow, UI glitches, date | EV 54, 56, 109; INV (a) API, (b) custom | https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/features-roadmap | "Utilise the Litmus API to connect with internal systems"; "Design tailored test cases that simulate real user interactions and end-to-end workflows"; "UI glitches, and bugs"; "Last updated 06 May 2025" | MATCH |
| 23 | Portal How it works: four categories and headings | EV 66; INV (b) Baseline | https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/how-it-works | "Litmus uses four main categories of tests"; "Security Tests", "Undesirability Tests", "Specialised Advice Tests", "Political Tests"; "Last updated 13 May 2025" | MATCH |
| 24 | Portal onboarding guide link | EV 42, 173; INV (a) onboarding | https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/getting-started ; .../resources | "To begin, refer to this onboarding guide." with href https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide (Resources links the same target) | MATCH |
| 25 | Two suites, 6 and 14 rows, test names, Baseline+ introduction wording | EV Datasets; INV (b) Baseline, Baseline+ | https://www.aiguardian.gov.sg/docs/wiki/Test-Information-Documentation | "two test suite options to choose from when running tests: Baseline Tests and Baseline+"; "Baseline Tests consists of 6 key tests across these four categories."; under Baseline+ "Baseline Tests consists of all 14 tests across these four categories."; Baseline rows DAN, Medical, Hateful, Insults, Domestic Affairs, Social Policies; Baseline+ 14 rows in the order of the eval table | MATCH |
| 26 | Dataset sentences and pass conditions (DAN, Cybersecurity, misconduct, Domestic Affairs both texts) | EV Datasets rows; EV 107 | same | "The dataset includes variations of the DAN prompt"; "resists the jailbreak attempt"; "The dataset contains a mix of benign and malicious inputs"; "The dataset ranges from socially condemned but legal behaviour to clearly illegal acts under Singapore law."; "whether the model refuses to answer due to potential misinterpretation and misrepresentation"; "maintains a neutral stance, presents information factually, and avoids partisan bias or inflammatory rhetoric" | MATCH |
| 27 | "model" versus "application" on the test page | EV 122 | same | Medical and Domestic Affairs "the model’s"; Hateful, Insults, Sexual, Cybersecurity "the application’s" | MATCH |
| 28 | "unless it is a medical chatbot" | EV Reuse 151 | same | in the Medical Description column: "…avoiding misinformation or unverified claims, unless it is a medical chatbot" (not in the Outcome column) | MATCH (quote; see optional on "pass conditions") |
| 29 | Troubleshooting quotes | INV (a) web app, API; EV 170 | https://www.aiguardian.gov.sg/docs/wiki/Litmus-Troubleshooting | "Ensure configurations (devices, browsers) are correctly set"; "Ensure your account setup is complete and subscription is active"; "Verify your API key and ensure you're using the correct endpoint" | MATCH |
| 30 | One-pager: title, TaaS sentence, runtime, domains, dashboards, metrics, collaborate, creation date | EV 26, 67, 95; INV (a) onboarding, (b) Baseline | https://isomer-user-content.by.gov.sg/22/6c4f97dc-3b8b-4701-8592-cd12d72012dd/20250916_Litmus%20and%20Sentinel%20one%20pager.pdf | "AI Guardian: Litmus & Sentinel" / "Global Overview Document"; "Litmus is a Testing-as-a-Service platform that provides automated pre-deployment safety, security, and behaviour testing for generative AI applications."; "Sentinel operates during runtime"; "(toxicity, bias, misinformation, robustness)"; "Pass/fail dashboards with remediation advice."; "Test coverage: Number of scenarios/risks evaluated."; "Pass/fail rates: Proportion of scenarios passed."; "Pilot with your AI applications to customise test suites."; CreationDate D:20250916121143+08'00' | MATCH |
| 31 | Kaleidoscope docs: audience and plan | EV 20, 29; INV (b) Kaleidoscope | https://govtech-responsibleai.github.io/kaleidoscope/ | "Litmus is AI Guardian’s testing and evaluation platform for Whole-of-Government AI products. We are extending Litmus to support Kaleidoscope’s structured evaluation workflow in the upcoming months." | MATCH |
| 32 | Shared interest form on the Sentinel page | EV 25 | https://www.aiguardian.gov.sg/docs/sentinel/sentinel-getting-started | "Fill up the Litmus and Sentinel interest form at" | MATCH |
| 33 | Portal Terms of Use clause | EV 36 | https://www.developer.tech.gov.sg/terms-of-use | "The featured products and services are subject to separate terms of use." | MATCH |
| 34 | Documented action repository missing | EV 39, 55; INV (a) CI/CD | https://github.com/dsaidgovsg/aiguardian-litmus-test | HTTP 404; git ls-remote "remote: Repository not found." | MATCH |
| 35 | 403 AccessDenied addresses; made-up path; Overview 200 | EV 42, 43; INV (a) onboarding | https://www.aiguardian.gov.sg/litmus ; .../docs/wiki/Litmus-Onboarding-Guide | "HTTP/1.1 403 Forbidden", "Server: AmazonS3", "X-Cache: Error from cloudfront"; /docs/wiki/Zz-Not-A-Page-20261010 403; Litmus-Overview 200 | MATCH |
| 36 | Wayback availability and CDX control | EV 45; INV (a) onboarding | https://archive.org/wayback/available?url=www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide ; CDX for Litmus-Getting-Started | {"archived_snapshots": {}}; CDX row "20260513141315 … Litmus-Getting-Started … 200" | MATCH |
| 37 | Docusaurus version and Last-Modified | EV Version scope; INV legend | https://www.aiguardian.gov.sg/docs/wiki/Litmus-Overview | `<meta name="generator" content="Docusaurus v3.10.0">`; Last-Modified Thu, 08 Oct 2026 08:42:14 GMT | MATCH |
| 38 | Moonshot tags, dates, DTO fields, route, enum, 0.7.6 field, identical DTO, licence | EV 131-134 | https://github.com/aiverify-foundation/moonshot/blob/ab4dbbad9177ff8590838071de82079b6d47ad51/moonshot/integrations/web_api/schemas/benchmark_runner_dto.py (and the other pinned files) | tags 0.4.11 = ab4dbbad (2024-10-25), 0.5.0 = f1b816c0 (2024-12-10), 0.7.6 = 03e9344d (2026-02-05); no tag between 0.4.11 and the Action commit 2024-10-29; DTO lines 4-13 with `num_of_prompts: int` at 10; routes/benchmark.py:14 `@router.post("/api/v1/benchmarks")`; types.py@0.7.6:74-76 `COOKBOOK = "cookbook"`, `RECIPE = "recipe"`; 0.7.6 DTO line 10 `prompt_selection_percentage`; DTO md5 identical at 0.4.0, 0.4.11, 0.5.0; LICENSE.md "Apache License Version 2.0" | MATCH |
| 39 | moonshot-data names | EV 136 | https://github.com/aiverify-foundation/moonshot-data/blob/30fac12375476ac1eb9f47e5872ea5d379c1aa4c/cookbooks/undesirable-content.json | cookbook "name": "Undesirable Content"; recipes/jailbreak-dan.json "This recipe assesses whether the system will be jailbroken using the common jailbreak methods." (tag 0.7.6 = 30fac123) | MATCH |
| 40 | Kaleidoscope repo main, arXiv date | EV 58 | https://github.com/govtech-responsibleai/kaleidoscope ; https://arxiv.org/abs/2607.14673 | refs/heads/main e806bf39bb4ccd1c5e8ab831ed8ef027fa4b5890, no tags; "[Submitted on 16 Jul 2026]" | MATCH |
| 41 | Playbook pin and README deployments | EV Version scope; INV legend | git ls-remote govtech-responsibleai/playbook | refs/heads/staging 45908b48c0a8b6d3855a154c0e41a12958a99205 (committed 2026-09-14T13:36:44Z); main 97338569; staging site litmus page "Last updated on Sep 14, 2026"; production "Last updated on Jul 29, 2026" | MATCH |
| 42 | GitHub org search: dsaidgovsg only the sample; govtech-responsibleai none, "11 repositories" | EV 40, 137 | https://api.github.com/orgs/govtech-responsibleai/repos?per_page=100 ; search litmus org:dsaidgovsg / org:govtech-responsibleai | search: 1 result dsaidgovsg/aiguardian-test-action; 0 results in govtech-responsibleai; organisation listing has 12 public repositories | MISMATCH (count; fix 1) |
| 43 | No LICENSE in the playbook root; Action repo holds only action.yml | EV 33 | https://api.github.com/repos/govtech-responsibleai/playbook/contents/?ref=45908b48… ; …/aiguardian-test-action/contents/?ref=v0.0.1 | playbook root: .agents, .claude, .githooks, .github, .gitignore, AGENTS.md, CLAUDE.md, CONTRIBUTING.md, PAGE-STANDARDS.md, README.md, website (no LICENSE); Action: ['action.yml'] | MATCH |
| 44 | PyPI names | EV 165; INV (b) wog-baseline-v1 | https://pypi.org/pypi/litmus/json (and the four other names) | litmus-client, litmusclient, aiguardian, govtech-litmus: 404; litmus: "Autogenerate pytest unit test skeletons from your existing modules." by Edward Johnson | MATCH |

I also checked these without a separate row; all match:
- The production playbook Litmus, Kaleidoscope, Safety evals and Sentinel pages carry the cited statements ("does not evaluate whether your system does its job well", "which is the contextual evaluation module within Litmus", "on a schedule, or from", "Results describe", "stay tuned", "WOG-curated", "refusal_rate", "deliberately generic", "Treating guardrails as a substitute for testing"). Only the line 53 refusal sentence differs, as the Version scope says.
- The staging Kaleidoscope page shows "Last updated on Jul 25, 2026", as the inventory Kaleidoscope row says.
- blog.ai.gov.sg/tag/evals/ has no "litmus".
- The docs sidebar lists four Litmus pages.

Tally: 44 checks, 43 MATCH, 1 MISMATCH, 0 UNVERIFIABLE.

## 5. Inventory consistency (Check 5)

- Row counts: (a) 4, (b) 5, (c) 6 = 15. This equals R038 and the BLOCKS proposed in changes.md 5b.
- Covered by: 15 of 15 cells are exactly "— (inventory only, not in Table 3)" (R011, R003: no Table 3 columns).
- Labels: only allowed forms. Counts equal changes.md 8c: [Documented] 69, repo test-action 12, repo playbook 13, [Inferred] 6, [Not disclosed] 25, [To be verified] 6.
- No `**`, no backticks, no literal `|` inside cells (checker cell counts 8/7/7 per table).
- The Source URL column is last in every table, and URLs are separated by " ; ". Every repo label in a row has a pinned URL with the same ref in the same row or in the block (a) intro or legend.
- The block (a) intro is parsed into the sheet note and now holds the short-name legend (T60). Fix 3 is the one unlabelled factual clause in it.

## 6. URLs (Check 6)

36 of the 41 distinct URLs in the two finals were requested with curl, following redirects (`scratchpad/verifier/litmus/url_check.txt`, `url_retry.txt`). These 5 were not requested by instruction: https://form.gov.sg/67a2f35fdd4157c04aed3cea, https://litmus.aiguardian.gov.sg/api/v1/, https://litmus.aiguardian.gov.sg/login, https://litmus.dev.aiguardian.gov.sg/api/v1/benchmarks, https://litmus.stg.aiguardian.gov.sg/login.

| URL | Status | Used in |
|---|---|---|
| https://arxiv.org/abs/2607.14673 | 200 | EV Tools row 6 |
| https://blog.ai.gov.sg/tag/evals/ | 200 | EV Published results |
| https://github.com/aiverify-foundation/moonshot-data/blob/30fac12375476ac1eb9f47e5872ea5d379c1aa4c/cookbooks/undesirable-content.json | 503 on github.com (3 tries); raw at same sha 200 | EV Engine 136 |
| https://github.com/aiverify-foundation/moonshot/blob/03e9344dc9fc949ae05b1f38580611fce36528ab/LICENSE.md | 503 (3 tries); raw 200 | EV Engine 134 |
| https://github.com/aiverify-foundation/moonshot/blob/03e9344dc9fc949ae05b1f38580611fce36528ab/moonshot/integrations/web_api/types/types.py | 503 (3 tries); raw 200 | EV Engine 133 |
| https://github.com/aiverify-foundation/moonshot/blob/ab4dbbad9177ff8590838071de82079b6d47ad51/moonshot/integrations/web_api/schemas/benchmark_runner_dto.py | 503 (3 tries); raw 200 | EV Engine 131 |
| https://github.com/aiverify-foundation/moonshot/blob/f1b816c0bdb26051bea8890d5ff73b460b3efe33/moonshot/integrations/web_api/schemas/benchmark_runner_dto.py | 503 (3 tries); raw 200 | EV Engine 132 |
| https://github.com/dsaidgovsg/aiguardian-litmus-test | 404 (expected; missing repository, HTTP fact in the text) | EV 39, INV (a) CI/CD |
| https://github.com/dsaidgovsg/aiguardian-test-action | 200 | INV (a) CI/CD text |
| https://github.com/dsaidgovsg/aiguardian-test-action/blob/190600937062c100d0c10181e3edf71702230244/action.yml | 503 then 200; raw 200 | EV Version scope, Tools, Engine; INV (a), (c) |
| https://github.com/govtech-responsibleai/kaleidoscope | 200 | EV Tools row 6; INV (b) |
| https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/ | 503 (3 tries; a directory, tree view 504); contents API at the sha 200 | EV and INV short-name legends |
| https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/evaluating-ai-systems/safety.mdx | 503 then 200; raw 200 | EV Tools row 5, Published results, Red-teaming; INV (b) |
| https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/kaleidoscope.md | 503 then 200; raw 200 | EV Tools row 6; INV (b) |
| https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/litmus.md | 503 (4 tries); raw 200 | EV Tools; INV (a), (b) |
| https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/wog-safety-testing.md | 504 then 200; raw 200 | EV Published results |
| https://govtech-responsibleai.github.io/kaleidoscope/ | 200 | EV Overview, Tools; INV (b) |
| https://govtech-responsibleai.github.io/playbook/tools/wog-safety-testing/ | 200 | EV Datasets note |
| https://isomer-user-content.by.gov.sg/22/6c4f97dc-3b8b-4701-8592-cd12d72012dd/20250916_Litmus%20and%20Sentinel%20one%20pager.pdf | 403 plain curl (expected); 200 with a browser User-Agent | EV Overview, Published results; INV (a) onboarding |
| https://www.aiguardian.gov.sg/ | 200 | EV 31, 142; INV (a) web app |
| https://www.aiguardian.gov.sg/docs/ | 200 | EV 31 |
| https://www.aiguardian.gov.sg/docs/sentinel/sentinel-getting-started | 200 | EV 25 |
| https://www.aiguardian.gov.sg/docs/wiki/ | 403 AccessDenied (short-name base path, not a page; not in the 5b list, optional) | EV and INV legends |
| https://www.aiguardian.gov.sg/docs/wiki/Litmus-Getting-Started | 200 | many |
| https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide | 403 (expected; HTTP fact in the text) | EV 42; INV (a) onboarding |
| https://www.aiguardian.gov.sg/docs/wiki/Litmus-Overview | 200 | EV Published results; INV (c) |
| https://www.aiguardian.gov.sg/docs/wiki/Litmus-Troubleshooting | 200 | INV (a) web app |
| https://www.aiguardian.gov.sg/docs/wiki/Test-Information-Documentation | 200 | EV Datasets; INV (b) |
| https://www.aiguardian.gov.sg/litmus | 403 (expected; HTTP fact in the text) | EV 42; INV (a) onboarding |
| https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/ | 200 | short-name legends |
| https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/features-roadmap | 200 | EV Tools; INV (a), (b) |
| https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/getting-started | 200 | INV (a) onboarding |
| https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/how-it-works | 200 | INV (b) Baseline |
| https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/overview | 200 | EV Tools; INV (a), (b) |
| https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/resources | 200 | INV (a) onboarding |
| https://www.developer.tech.gov.sg/terms-of-use | 200 | EV 36 |

Classification of non-200:
- Expected by design (changes.md 5b): the one-pager (403 to plain curl, 200 with a browser User-Agent), aiguardian-litmus-test (404), /litmus and Litmus-Onboarding-Guide (403).
- Base path: /docs/wiki/ (403, S3 has no index object at that path).
- Transient server errors: the github.com blob pages answered 503 or 504 on some or all tries from this session. All raw.githubusercontent.com equivalents at the same ref return 200, and 4 of the 11 blob pages returned 200 on retry, so the pages exist at the pins. These are not dead links. P9 should re-run them, and changes.md 5b's "403 from the session proxy" note can say "403, 503 or 504".
