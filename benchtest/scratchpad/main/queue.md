# Queues

## xlsx-writer queue (products with a CP2 approval ruling, apply in this order, one at a time)
| # | Slug | CP2 ruling | Queued | Applied (commit) |
|---|---|---|---|---|
| 1 | presidio | R022 | 2026-10-09 | |
| 2 | sdp | R023 | 2026-10-09 | |
| 3 | modelarmor | R024 (+ R025 pre-P8 merger edit first) | 2026-10-09 | |

## Open questions (from agents)
| Q file | Product | Routed to | State | Ruling |
|---|---|---|---|---|
| explorer/20261009_presidio_q01.md: official org after the transfer (data-privacy-stack vs Microsoft) and the header prefix | presidio | user at presidio CP1 | resolved | see CP1 ruling |
| explorer/20261009_presidio_q02.md: six single columns vs a merged set; recognizer-family granularity; + (i) PD5 column vs inventory-only, (ii) ~30 family rows vs ~120 per-entity rows (P1) | presidio | user at presidio CP1 | resolved | see CP1 ruling |

| explorer/20261009_modelarmor_q01.md: 10 columns (R002 split) vs 6 vs folding MA9/MA10; antivirus + MCP screening as inventory or MA11; prefix `Model Armor:` (Q03); P1 adds alt (e) 14 cols if response-side file/image evidence appears, MA11 = tool-call screening (MCP and Agent Gateway) | modelarmor | user at modelarmor CP1 | resolved | see CP1 ruling |
| explorer/20261009_sdp_q01–q03.md: prefix `Sensitive Data Protection:` vs `Google Cloud …`; content policy (SD7) column vs inventory; fold SD2→SD1, SD4→SD3 | sdp | user at sdp CP1 | resolved | see CP1 ruling |

| modelarmor P5 r2 Q1/Q2: Google Cloud AUP forbids using Services "to test … to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted" — does red-team testing of Model Armor fall under it? Synthetic data only for Preview features (Pre-GA terms: no personal data)? | modelarmor (+ bench design) | user at modelarmor CP2 | resolved | R025 |

## Resolved questions
| Q file | Ruling | Decided by |
|---|---|---|
| sdp P8 Q1/Q2 (sheet name "3g. Sensitive Data Protection Inventory" is 39 chars > Excel 31) | accept "3g. SDP Inventory" (auto-default: naming); full name stays in A1 title; diagrams/docs cite the tab name; future inventory sheet names must be ≤31 chars | main |
| modelarmor P8-prep R025 Q1 (bench-rule bullet in MA7/MA8, whose Detail names exclusion rules only as unsupported) | keep: R025 literal scope "any column whose Detail names exclusion rules" | main |
| modelarmor P8-prep R025 Q2 (bench rule plain text vs checker's bold end-label) | accept: rule text plain, single [Documented] covers the terms quote (drafts README label convention) | main |
| modelarmor P5 r2 Q1/Q2 (AUP testing clause; Preview synthetic data) | R025 | user |
| B1 CP2 (presidio, sdp, modelarmor) | R022, R023, R024 | user |
| modelarmor P7 Q1 (T21 read via curl + stdlib parse) | R021: counts as verbatim; label [Not disclosed] | main |
| modelarmor P7 Q2 (Service Extensions latency figure) | yes: Google docs on docs.cloud.google.com, attributed "Service Extensions docs" (R007 item 1, Apigee precedent) | main |
| modelarmor P7 Q3 (load-balancer route limits) | add to INV(b) now ([Documented], attributed) | main |
| sdp P7 Q1 (Apigee row, path deprecated) | marker `— (legacy, not in Table 3)`; P8 config markers include legacy | main |
| sdp P7 Q2 (SD6 R7 AUP bullet) | policy wording [Documented] + applicability [Inferred] (CLAUDE.md rule 2) | main |
| sdp P7 Q3 (who records fix 7) | merger, in Verifier fixes | main |
| sdp P6 Q4 (cross-product headers) | closed: verifier confirmed exact match with modelarmor/presidio/sentinel | main |
| presidio P7 Q1 (surrogate_ahds Covered-by) | add PD5 (consistent test) | main |
| presidio P7 Q2 (/tree/ URLs → 400 not 403) | merger updates changes.md 5b; url-checker told at P9 | main |
| presidio P6 Q1 (2523c7b placement: labelled fact in PD2 R2, plain R8 question) | confirmed (README: no labels in R8) | main |
| presidio P6 Q2/Q3 (recommit; CLAUDE.md row; seeds 0.0.60) | done by main (CLAUDE.md row updated at CP1; seeds note added at P4) | main |
| presidio P6 Covered-by surrogate_ahds | leave as merged (resolver proposal); verifier may flag | main |
| presidio P6 Q5 (NeMo E/F "not verified" default string) | NeMo frozen (R001); carry into the final run summary as a follow-up note | main |
| modelarmor P6 Q3 (AUP bullets extended to MA2/MA3/MA4) | confirmed (same test content) | main |
| modelarmor P6 Q4 (banner check for Terraform/gcloud/console/SCC rows) | no extra pass; stay [Not disclosed] (optional) | main |
| modelarmor P6 Q1/Q5 (service.pb.go line spot-check at modelarmor/v1.3.0; Service Extensions verbatim retry) | → P7 verifier | main |
| sdp P6 Q1 (discovery doc URL in R9?) | keep plain-text citation, no URL cell (lessons 12: no googleapis.com API hosts in URL lists) | main |
| sdp P6 Q2/Q3/Q6 (ruling ids removed; extra edits; T36) | accepted; verifier reviews extra edits at P7 | main |
| sdp P6 Q4 (cross-product headers) | main re-compares after modelarmor/presidio P6 | main |
| presidio P5 Q1 (2.2.364 release body unreadable) | Option A: CHANGELOG at tag substitute (R015); main's add_repo showed only anonymous git reads, no API | main |
| presidio P5 Q2 (T66 Covered-by for operator rows and Docker row) | list a header only where that column's Detail cites the row's function; merger applies resolver's proposal under that test | main |
| presidio P5 Q3 (main HEAD 2523c7b REMOVE_INTERSECTIONS fix after the tag) | merger adds one PD2 R8 bullet labelled [Documented: develop/unreleased] citing the commit; pin stays 2.2.364 | main |
| presidio P5 Q4 (third-party licence/model-card sources) | accepted under R019; read date + last-modified suffices | main |
| presidio P5 Q5 (P9 URL notes: github.com 403 → raw check; 13 /blob/→/tree/; re-pin presidio-research to 0.3.2) | merger fixes URLs; url-checker uses raw equivalents for github.com (R020) | main |
| presidio P5 Q6 (process text removal; checks) | merger runs check_drafts | main |
| modelarmor P5 r2 Q3 (T41 range) | covered by resolutions_1 (PARTLY RESOLVED) + r2 cross-range note; merger uses both | main |
| modelarmor P5 r2 Q4 (T78 date 2026-10-09, T80 page footers) | merger records in modelarmor_changes.md | main |
| modelarmor P5 r2 Q6 (Pre-GA suffix) | intro sentence only; Preview rows keep Status "Preview" (auto-default: equivalent wordings) | main |
| sdp P5 r2 Q1 (Google sample repos dlp-dataflow-deidentification, community) | yes, as "supporting only" with [Documented: repo …@sha] (R013: Google sample repos are supporting) | main |
| sdp P5 r2 Q2 (T65 drop SD4 from hash row) | yes: hashing is one-way, SD4 is reversible tokenisation (R018 keeps SD4) | main |
| sdp P5 r2 Q3/Q4 (T92/T93 terms facts) | accept resolver's text: general Google Cloud terms [Documented] + [Inferred] applicability; benchmarking/AUP in SD6 R7/R8 and INV(f) (R019) | main |
| sdp P5 r2 Q5 (T78 file bytes on content.inspect) | Detail-level in SD1 R3; job-based file scans inventory only | main |
| sdp P5 r2 Q6 (T51/T63 permission questions) | stay open (needs-testing, bench) | main |
| modelarmor P5 r1 Q1 (pin google-cloud-go@37f936ac HEAD vs tag modelarmor/v1.3.0) | merger re-pins to `modelarmor/v1.3.0` (README rule 8; resolver showed service.pb.go identical) | main |
| modelarmor P5 r1 Q2 (T25 other-language client versions) | INV(b) Client libraries only + one short R4 bullet | main |
| modelarmor P5 r1 Q3 (T23 status for banner-free rows) | "GA [Inferred]" only where the page was read and shows no launch-stage banner; unread pages stay [Not disclosed]/[To be verified] | main |
| modelarmor P5 r1 Q4 (T21 Service Extensions page empty via fetch_text) | summarising fetch can't carry a label (CLAUDE.md rule 4) → [To be verified]; P7 verifier may retry verbatim | main |
| modelarmor P5 r1 Q5 (shared resolver scratch folder) | each agent uses its own subfolder `resolver/<slug><N>/` | main |
| sdp P5 r1 Q1 (T5 marker on Model Armor/Gemini Enterprise rows; T7 Apigee/Data Fusion/BigQuery cross-refs) | T5: R011 + R012; T7: R007 item 1 (Google-authored pages official) | main |
| sdp P5 r1 Q2/Q5 (clone denied → raw GitHub fallback; absence labels) | R020 | main |
| sdp P5 r1 Q3/Q4 (T49 conflict stays two [Documented] bullets; T44 PERSON_NAME ~2026-11-02 and MEDICAL_ID legacy ~2026-10-11 dates) | merger keeps both; verifier re-reads release notes at P7, url-checker run at P9 | main |
| presidio CP1 (Q01, Q02, T1–T7, local runs) | R016, R019 | user |
| modelarmor CP1 (Q01, D1–D7) | R017, R019 | user |
| sdp CP1 (Q01–Q03, T1–T4, T92/T93) | R018, R019 | user |
| modelarmor P4 Q2/Q3 (doc-answerable H items; T55 NRIC built-in infoType per sdp_cols_a) | → modelarmor P5 resolver (with sdp evidence for T55) | main |
| modelarmor P4 Q4/Q5 (triager file renames; Settled table; T83 block (d) = 20 rows → counts 10/15/16/20/16) | accepted; counts asserted at P8 | main |
| modelarmor P4 Q1 (D1–D7: split 10/6, MA11 tool-call screening, alt (e) 14 cols, antivirus, prefix, live testing/terms, Preview reliance) | user at modelarmor CP1 | user |
| sdp P4 Q5 / T19 ("out of purpose" label) | R015 ([Inferred] everywhere, premise named) | main |
| sdp P4 Q6 (Apigee/Data Fusion/BigQuery/demo cross-refs; marker on Model Armor and Gemini Enterprise rows) | keep: Google-authored pages on docs.cloud.google.com/cloud.google.com are official (R007 item 1); R011 marker correct, Model Armor named in text only (R012) | main |
| sdp P4 Q7 (Google API discovery doc + IAM permissions reference for T9) | yes: both Google-owned official pages (googleapis.com discovery, docs.cloud.google.com/iam) | main |
| sdp P4 Q8 (re-add reviewer notes to cols A/B) | optional suggestion dropped (auto-default); P7 verifier spot-checks quotes | main |
| sdp P4 Q9 (seeds host; inventory row counts) | seeds already on docs.cloud.google.com; counts asserted at P8 from final | main |
| sdp P4 Q1–Q4 (prefix T1; SD7 + Gemini Enterprise access T2/T10; fold SD2/SD4, split SD5 T3/T4; terms pages + sensitive test data T92/T93) | user at sdp CP1 | user |
| presidio P4 Q5 (vendor release notes/tags) | R015 (ls-remote + clone at tag; CHANGELOG at tag) | main |
| presidio P4 Q6 / T57 ("out of purpose" label) | R015 ([Inferred] everywhere, premise named) | main |
| presidio P4 Q7 (0.0.60 = image-redactor, structured = 0.0.8; NeMo `<ENTITY_TYPE>` note) | merger records in presidio_changes.md; seeds note added; NeMo sheets frozen (R001) | main |
| presidio P4 Q1–Q4 (T1 ownership/prefix, T2–T4 column split + PD5 + inventory granularity, T6 component licences, local-run consent) | user at presidio CP1 | user |
| explorer/20261009_presidio_q03.md (presidio-research placement) | R010 | main |
| explorer/20261009_presidio_q04.md (column ID prefix) | R009 | main |
| presidio P1 report: Covered-by marker for current non-column rows | R011 | main |
| modelarmor P0 Q02 (MA5/MA6 vs SDP) | R012 | main |
| modelarmor P0 Q04 / presidio P1 (vendor GitHub access) | R013 | main |
| modelarmor P1 Q-D (inventory sheet letter) | rule: R003 — letter assigned at P8 in workbook order; brief's `3f` is provisional | main |
| sdp P1 Q04 (sheet letter) / Q05 (seeds host) | R003 (letter at P8); seeds already on docs.cloud.google.com | main |
| presidio P2 inventory Q1 (markers + `alpha` status) | main: config `markers` = legacy + inventory-only (R011); no status validator exists in inventory_sheet.py → vendor wording `alpha` stands (R007 vendor wording) | main |
| presidio P2 inventory Q3 (2.2.364 release notes, presidio-research tag) | routed to presidio P5 resolver via triage | main |
| presidio P2 inventory Q4 (NeMo row sourced from NVIDIA docs) | keep, attributed in plain text (R007 item 1 precedent: wrapper vendor's docs for its own semantics) | main |
| presidio P2 inventory Q5 (14/31/10/14 vs targets) | accept; brief targets are not binding, P8 config asserts final counts | main |
| presidio P2 cols_a Q3 (notebook figures in R5 Summary) | R014 | main |
| presidio P2 cols_a Q2 (release notes / latest tag) | routed to presidio P5 resolver (hint: `git ls-remote --tags` works where github.com pages 403) | main |
| presidio P2 cols_a Q4 (test /supportedentities on Docker image) | needs-testing item → triage → CP1 (pulling images is outside read-only rule) | main |
| modelarmor P2 inventory Q1 (BLOCKS 10/15/16/18/16; markers incl. R011) | recorded for P8 config | main |
| modelarmor P2 inventory Q2 (Agent Gateway ingress MA1–MA8 vs egress marker) | bundled with modelarmor CP1 Q-B (tool-call screening) | user at CP1 |
| modelarmor P2 inventory Q3 (console + monitoring rows) | keep; brief targets not binding | main |
| modelarmor P2 inventory Q4 (Terraform registry page official?) | registry.terraform.io is HashiCorp's, not Google's → not an official source for Model Armor; cite Google's own Terraform docs on docs.cloud.google.com if found, else [To be verified]; Apigee status → P5 resolver | main |
| modelarmor P2 cols_b Q1 (response-side file/image evidence → alt (e) split?) | default single MA9/MA10; to user at CP1 with evidence summary | user at CP1 |
| modelarmor P2 cols_b Q2 (align inventory block (b)/(d)) | inventory already has us-east7/global/Seoul/Melbourne; remaining cross-draft items → triage → merger | main |
| modelarmor P2 cols_b Q3 (release-note GA vs page "(Preview)") | status: a dated release-note statement beats an undated page label; keep both as a labelled conflict pair; Apigee status → P5 resolver | main |
| modelarmor P2 cols_a Q1 (block (d) 18 vs 20 regions) | merger: block (d) lists the union (20), with a labelled note that us-east7 and global appear only in the feature table (C15) | main |
| modelarmor P2 cols_a Q2 (Apigee flow-variable bullets) | keep: Apigee docs on docs.cloud.google.com are Google's official docs (R007 item 1); attribute "Apigee docs" in plain text | main |
| modelarmor P2 cols_a Q3 (RAI/PI/URL on OCR and extracted text) | → triage → P5 resolver | main |
| modelarmor P2 cols_a Q5 (default level C3, CSAM in limited regions C14, confidenceLevel semantics) | needs-testing → triage → CP1 | main |
