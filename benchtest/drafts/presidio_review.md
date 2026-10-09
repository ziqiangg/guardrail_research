# Presidio workbook: fresh verifier review

Date of checks: 2026-10-09. Reviewer: gr-verifier (did not draft, triage, resolve or merge). Inputs read: CLAUDE.md, drafts/README.md, rulings R010, R011, R013, R014, R015, R016, R019, R020, queue.md "Resolved questions" rows starting "presidio", lessons.md; presidio_two_level.md (read in full), presidio_inventory_final.md (structure, Covered-by column and selected rows in full), presidio_changes.md (read in full), presidio_summaries_preview.md (compared mechanically with the final), presidio_resolutions_1.md (method notes, T9 to T11, T20 to T30, Report), presidio_brief.md (headers). Originals presidio_cols_a.md, presidio_cols_b.md and presidio_inventory.md were diffed, not re-read. Vendor code was read from shallow clones of data-privacy-stack/presidio at tag 2.2.364 (779dbd28) and at main (2523c7b, plus its parent), data-privacy-stack/presidio-research at tag 0.3.2 (06d20306), and through `python benchtest/tools/fetch_text.py` on raw.githubusercontent.com at the same tags (R020). Docs pages were read with fetch_text.py. Nothing was installed, run or pulled. Scripts and outputs are in benchtest/scratchpad/verifier/presidio/. No file other than this one and that folder was modified.

## Verdict: PASS WITH FIXES

The merge is faithful. All 27 spot-checks at source match, the four Summary edits main asked about (PD1 R2, PD1 R5, PD5 R4, PD3 R4) and the two unrequested "moving to" edits (PD2 R4, PD3 R4) are correct, logged and entailed, no known wrong string survives, and every substantive change I could diff is in presidio_changes.md. The checker gives 0 errors on both finals. Of 223 distinct URLs, 208 return 200 (github.com blobs checked through their raw equivalents); the other 15 are github.com directory or commit pages that the session proxy refuses (400 or 403), and I confirmed each one in a clone. There are 4 required fixes:

1. The PD2 R2 develop/unreleased bullet on commit 2523c7b was written without the commit being read. It carries an inference under a Documented label and leaves out the one fact a test bench needs.
2. The PD1 R1 Summary is not entailed by its own Detail.
3. The PD4 R6 Summary is not entailed by its own Detail.
4. The surrogate_ahds Covered-by cell applies main's test inconsistently, and its logged reason is factually wrong.

None of the fixes changes a headline number.

## Required fixes

1. **PD2 R2, bullet on main commit 2523c7b (lines 316 and 411, R9 line 447): inference inside a develop/unreleased bullet, written from main's note without reading the commit.**
   - Problem: the bullet ends "so the tagged behaviour described here may differ on main". That is an inference inside a `[Documented: develop/unreleased]` bullet (README section 3 rule 5). presidio_changes.md section 4 item 1 says "no commit text was read". I read it.
     - Commit 2523c7b74a469270c5c78bb253f140eafca21e31, committed 2026-10-08, is titled "fix(anonymizer): stop REMOVE_INTERSECTIONS from leaving flagged text in clear (#2331)".
     - It changes only the `REMOVE_INTERSECTIONS` pass of `_remove_conflicts_and_get_text_manipulation_data`. The sort key becomes `(element.start, element.end)` and the final filter becomes `element.start < element.end`. It also extends the enum docstring and adds two test cases.
     - `anonymizer_engine.py` at tag 2.2.364 is byte-identical to the commit's parent. Tag 2.2.364 therefore still has `sort(key=lambda element: element.start)` (line 197) and `if element.start <= element.end` (line 216).
     - Traced on the commit's first new test case (A 0-10 score 0.9, B 5-15 score 0.5, C 8-20 score 0.4), the tagged pass ends with C trimmed to zero length at 10-10 and B at 10-15. Characters 15 to 20, which C flagged, are left unanonymised. Main returns C at 15-20.
     - The default strategy (`MERGE_SIMILAR_OR_CONTAINED`) and the REST route, which cannot set a strategy (PD2 R4), never run this pass. So the fix does not change 2.2.364 default or REST behaviour. It matters to Python callers who choose `REMOVE_INTERSECTIONS`, and the effect is leakage, not only a "difference".
   - Replace PD2 R2 line 316 with these two bullets:
     - `• Main commit 2523c7b (2026-10-08, after tag 2.2.364) is titled "fix(anonymizer): stop REMOVE_INTERSECTIONS from leaving flagged text in clear (#2331)"; it changes only the REMOVE_INTERSECTIONS pass, sorting by start and end and dropping results trimmed to zero length **[Documented: develop/unreleased]**` (write REMOVE_INTERSECTIONS in backticks)
     - `• At tag 2.2.364 that pass sorts by start only and keeps zero-length results (`anonymizer_engine.py@2.2.364:197,216`), so a Python caller who selects `REMOVE_INTERSECTIONS` can get flagged text back unchanged; the default strategy and the REST route do not run this pass (premise: the tagged code read against the test cases the commit adds) **[Inferred]**`
   - Replace PD2 R8 line 411 with: `• Whether `REMOVE_INTERSECTIONS` at tag 2.2.364 leaves flagged text in clear on real overlapping results, as main commit 2523c7b (#2331; develop/unreleased) indicates, and whether the next release fixes it (see R2; needs testing)`
   - Replace PD2 R9 line 447 with the full-SHA URL: `• https://github.com/data-privacy-stack/presidio/commit/2523c7b74a469270c5c78bb253f140eafca21e31`
   - PD2 R2 Summary: no change needed. The PD2 R8 Summary can stay. Optionally add "intersection trimming at 2.2.364" to its list; it stays under 45 words.

2. **PD1 R1 Summary: not entailed by its own Detail.**
   - Problem: the Summary says the Analyzer "returns each entity type with its position and a confidence score" and is labelled **[Documented]**. The only R1 bullet that mentions results is the **[Inferred]** "no verdict" bullet ("the result fields (R5) hold spans, scores ..."). The result fields are documented only in R5.
   - Fix: add after the `POST /analyze` bullet (line 10): `• Each result carries `entity_type`, `start`, `end` and `score` (`recognizer_result.py@2.2.364:34-46`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**`
   - recognizer_result.py at 2.2.364 is already in PD1 R9. The Summary stays as it is (35 words).

3. **PD4 R6 Summary: not entailed by its own Detail.**
   - Problem: the Summary says the call "Needs ... an OCR engine (Tesseract installed, or an Azure endpoint and key) and the Analyzer's English spaCy model". No R6 bullet mentions Tesseract or the spaCy model; both are only in R2 and R4.
   - Fix: add two bullets at the top of PD4 R6:
     - `• Installation page: "Install an OCR engine. The default version uses the Tesseract OCR Engine." (Presidio docs, installation page) **[Documented]**`
     - `• Installation page: "Presidio image redactor uses the presidio-analyzer … which requires a spaCy language model:" followed by the en_core_web_lg download (Presidio docs, installation page) **[Documented]**` (write en_core_web_lg in backticks)
   - Both quotes are on https://presidio.dataprivacystack.org/installation/ (lines 222 to 225 of the fetched text), which is already in PD4 R9. The Summary stays as it is (43 words).

4. **Inventory (c), surrogate_ahds row, "Covered by Table 3 column": main's test applied inconsistently.**
   - Problem: main's ruling (queue.md, presidio P5 Q2) is "list a header only where that column's Detail cites the row's function". PD5 R4 line 834 cites "the AHDS surrogate when its extra is installed" in the operator list that PD5 can use. On that basis keep, which PD5 R7 never tests, was given PD5, but surrogate_ahds was not.
   - The logged reason (changes.md section 3 (c) and section 4 item 5: "PD5 hardcodes the Anonymize type; the surrogate needs an extra") does not hold:
     - surrogate_ahds is an Anonymize operator. It is appended to `ANONYMIZERS` at operators_factory.py@2.2.364:26, which is the list that data_processors.py uses with `OperatorType.Anonymize` (lines 78-80).
     - The extra applies equally to PD2, where the row is covered.
   - Replace the cell with: `Presidio: PII anonymisation and masking in text (Anonymizer) ; Presidio: PII detection and anonymisation in structured data (tables and JSON)`
   - Log the change in presidio_changes.md section 3 (c), with a corrected reason.
   - If main prefers to keep the cell, then the keep row's PD5 header should go for the same reason, and the section 4 item 5 rationale should be corrected.

## Optional suggestions

- PD2 R9 and PD3 R9 Summaries were rewritten in the merge but omit presidio-research, although both R9 lists carry presidio-research@0.3.2 URLs (PD2: README, presidio_pseudonymize.py, docs/evaluation.md; PD3: README, docs/evaluation.md). Suggested PD2 R9: `Summary: Presidio docs site pages, the Presidio repository at tag 2.2.364 and one commit on its main branch, the presidio-research repository at tag 0.3.2, and one Microsoft Learn page.` Suggested PD3 R9: `Summary: Presidio docs site pages, the Presidio repository at tag 2.2.364, the presidio-research repository at tag 0.3.2, and the NVIDIA NeMo Guardrails page on Presidio.`
- PD5 R9 Summary lists "licence" among the repo files, but PD5 R9 has no LICENSE URL. The licence fact in PD5 R4 comes from `presidio-structured/pyproject.toml` line 10 (`license = "MIT"`). Either add `https://github.com/data-privacy-stack/presidio/blob/2.2.364/LICENSE` to PD5 R9 or drop "licence" from the Summary.
- Inventory (a) presidio-research, "Version read" cell: "tag 0.3.2 is the highest tag". The repository also has a tag `0.22`, which sorts above 0.3.2 by version number. It is commit 0a2b7872 dated 2025-01-08, whose pyproject.toml says `version = "0.2.2"`, so it is a mistyped older tag. Suggest "tag 0.3.2 is the latest release tag (tag 0.22, dated 2025-01-08, carries version 0.2.2)". The label can stay.
- PD3 R2 Summary says "Presidio documents three routes" (AES, the pseudonymization mapping, LiteLLM). Its Detail also describes the OpenAI toolkit's session concept as a separate route. "All start from what the Analyzer detected" rests on an **[Inferred]** bullet under a **[Documented]** Summary. Suggest "Presidio documents AES encryption, a client-held mapping in the pseudonymization sample, session-based toolkits and LiteLLM's restore of masked tokens; each restores only what was detected."
- PD1 R1 Summary "runs recognizers over one string" sits beside the R1 batch bullet (a list in `text` is run as a batch over REST). Consider "over one string per call (or a list over REST)".
- PD1 R4 bullet "2.2.364 is the highest version tag of the repository (git ls-remote --tags, 2026-10-09)" carries the repo pin label. It is a git listing fact, which README section 3 rule 7 would label `[Documented]` with "(observed 2026-10-09)". I re-ran the listing: 2.2.364 is the highest numeric tag (the v0.5 to v0.95 tags are legacy). The fact is right either way.
- The third-party licence URLs in inventory (a) and (b) point to `main` or `master` branches (spaCy, pytesseract, Tesseract, pydicom, Stanza, transformers, GLiNER, LangExtract, Ollama). They are not vendor repos, and R019 accepts read date plus last-modified, but pinning them to a tag would make the P9 check reproducible.
- changes.md section 5b expects "14 /tree/ URLs" to be checked as exceptions. Through the proxy, the 13 country /tree/ URLs answer 400 (not 403) and /tree/e1987e57 answers 403. gr-url-checker should expect both codes.

## 1. Unlogged differences (Check 1)

Method: `benchtest/scratchpad/verifier/presidio/diff_cols.py`.
- Parses PD1 to PD3 from cols_a and PD4 to PD6 from cols_b, and the final, into (column, row) line lists.
- Runs difflib SequenceMatcher per row. Each added or removed line is searched in presidio_changes.md by normalised 60, 40 and 25-character prefixes (bold markers and ellipses removed).
- Inventory: `diff_inv.py` compares the files cell by cell (all 69 rows; keys identical in both versions) plus the block intros and the scope paragraph.

Results:
- Columns: 158 lines added, 89 removed. All 89 removals and 143 additions match a log entry directly.
- The other 15 additions are later parts of multi-bullet entries that the log truncates with "…". Examples: the PD1 R2 80/81 count bullet (T20), the gh-pages bullets (T14), the NGINX and App Service bullets (T52), the PD2 R2 NONE inference and the 2523c7b bullet (T30, main Q3), and the PD6 R7 InputSample bullet (T12).
- I matched each of those 15 to its operation in benchtest/scratchpad/merger/presidio/ops_cols.py, where it sits in the same call as a logged first bullet. None is a new fact without a reason code.
- Inventory: 9 pieces did not prefix-match. All were licence sentences appended after a full stop (T6), the Legacy V1 hint (T65), the encrypt key-size cell (T38) and the Docker Covered-by append (T66). I found each one by hand in section 3.
- Summaries: the 25 changed Summaries listed in changes.md section 5 are exactly the ones that differ. presidio_summaries_preview.md equals the final file for all 54 Summaries and word counts (script check).
- The two unrequested Summary edits (PD2 R4 and PD3 R4 "now under" to "moving to") are logged in section 2 and explained in section 4 item 4.
- Result: no substantive unlogged change. The change log's "Before"/"After" cells are truncated, but every truncated entry maps to a reason code.

## 2. Sourcing and label strength (Check 2)

- Changed `[Documented]` facts trace to a resolution quote, with one exception: the 2523c7b bullet (fix 1), which traces to main's queue note only. I have now verified it at source, so the remaining problem is its inference and its wording, not its existence.
- Spot-checked resolution-based facts all match at source (section 4): T9, T10, T11, T13, T14, T20, T24, T26, T30, T38, T44, T52, T7 (Document Intelligence retention).
- Inferences labelled Documented: fix 1. I also scanned every `[Documented]` bullet containing "so", "therefore", "may", "probably" or "because" (25 hits). The rest are direct consequences of the quoted code or quoted docs text, for example "salt = os.urandom(32), so the same value gets a different hash each time". I accept them.
- Absence claims: every `[Not disclosed]` bullet names what was checked. No absence is labelled `[Documented]`.
- R014: PD1 R5 Summary keeps the setup qualifier in the same sentence ("for default recognizers at threshold 0.4 on synthetic data"). The figure is presented as a notebook result, not a vendor accuracy claim. The relative uplift (+38 percent) and the commit-date bounds are `[Inferred]`.
- R015 and R020: the out-of-purpose bullets are `[Inferred]` with "premise: the Home page module list" in all six columns. The release body is not used. CHANGELOG at the tag is the substitute.
- Leftover scan (lessons.md item 6) over both finals found 0 hits for: "default settings", "0cb36502", "about 80", "about 120", "now under the", "Release 2.2.364", "[unreleased]", "Source conflict C", "403", "readable", "CP1", "Q01", "R010", "shallow", "Reviewer notes", "this draft", "I checked" and "thin default".
  - "16 pattern recognizers" occurs once, in the PD1 R2 notebook bullet. There it correctly describes the notebook output, not the Summary.
  - "proxy" occurs only as "LiteLLM proxy".
  - `[To be verified]` occurs 3 times, all in the inventory: Stanza model licences, and release notes in rows 22 and 98. All three are logged as residual.

## 3. Summary entailment and style (Check 3)

- Checker run on the final columns: `python benchtest/tools/check_drafts.py columns benchtest/drafts/presidio_two_level.md --final --expect 6` gives "RESULT: 0 errors, 0 warnings".
- Coverage: 6 columns, 54 Summaries. None is over its limit (the maximum is 45 for R1 to R6 and R8; the R7 maximum is 51, PD3).
- R8 lines start with "**Key open questions.**" and carry no label. R9 lines are plain.
- The six headers equal the brief headers exactly (string compare).
- Pins: every file cited as `file@2.2.364`, `@0.3.2` or `@e1987e57` in R1 to R8 has an R9 URL with the same file name and ref in the same column (script, 0 misses). The repo labels used are presidio@2.2.364, presidio-research@0.3.2, presidio@e1987e57 and, in the inventory, presidio@037d239f.
- Entailment: every Summary is supported by its own row's Detail except PD1 R1 (fix 2) and PD4 R6 (fix 3). The weaker cases in the optional list are PD3 R2 and the R9 Summaries of PD2, PD3 and PD5.
- The Summaries main asked about:
  - PD1 R2: "groups its types into Global, 18 country sections and a medical section" is entailed by the structure bullet. "A default English setup loads pattern recognizers plus a spaCy name and place model" is entailed by the notebook-4 bullet (repo label) and by default.yaml. Label `[Documented]` is fair.
  - PD1 R5: entailed by the notebook-4 bullet and the threshold bullets.
  - PD5 R4: "Package version 0.0.8, marked alpha, under the MIT licence" is entailed by the pyproject bullet, the getting-started alpha quote and the licence bullet.
  - PD3 R4: "128, 192 or 256-bit key" is entailed by the encrypt.py bullet.
  - PD2 R4 and PD3 R4: "moving to the Data Privacy Stack community" is entailed by their Detail bullets citing the transition page ("in the process of transitioning"). The FAQ's perfect tense ("has since transitioned") sits beside it in PD1 R4 as the second side of the conflict (README section 3 rule 4). The edit is correct.

## 4. Spot-checks at source (Check 4)

Docs pages were read with fetch_text.py (verbatim). Code was read in clones at the tags, and at raw.githubusercontent.com for presidio-research 0.3.2. The commit was read with git show.

| # | Claim | Location | Source URL | Verbatim quote or value seen | Match |
|---|---|---|---|---|---|
| 1 | 80 entity ids live, 81 at the tag, extra PH_UMID | PD1 R2 (Summary basis) | https://presidio.dataprivacystack.org/supported_entities/ ; https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/supported_entities.md | Parsed: live 80 distinct ids, tag 81; only difference PH_UMID, tag line 161 "… Disabled by default." | MATCH |
| 2 | Global, 18 country sections, Medical | PD1 R2 Summary | https://presidio.dataprivacystack.org/supported_entities/ | Page contents: Global, USA, UK, Spain, Italy, Poland, Singapore, Australia, India, Finland, Korea, Nigeria, Philippines, Canada, Sweden, South Africa, Thai, Turkey, Germany, Medical / Clinical | MATCH |
| 3 | default_recognizers.yaml: 74 entries, 73 names, 50 disabled, 24 enabled (list as given); supported_languages en; SgFinRecognizer line 135 | PD1 R2 | https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default_recognizers.yaml | YAML parse: 74 / 73 / 50 / 24; enabled list identical; line 135 `- name: SgFinRecognizer` | MATCH |
| 4 | Notebook 4: 19 supported entities, 17 recognizers (16 pattern plus SpacyRecognizer) | PD1 R2 | https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/notebooks/4_Evaluate_Presidio_Analyzer.ipynb | Output lists 19 entity names and 17 recognizer names ending 'UrlRecognizer', 'SpacyRecognizer' | MATCH |
| 5 | F2 0.661, P 0.733, R 0.646; threshold 0.4; 1500 samples; IoU 0.75; 5.84 s; "not recommended for production" | PD1 R5 Summary and Detail | same notebook (raw at 0.3.2) | "{'F2': 0.661, 'Precision': 0.733, 'Recall': 0.646}"; "AnalyzerEngine(default_score_threshold=0.4)"; "1500"; "SpanEvaluator(iou_threshold=0.75)"; "Wall time: 5.84 s"; "Using Presidio with default parameters (not recommended for production)." | MATCH |
| 6 | Wrapper default threshold 0.4 at line 19 | PD1 R5 | https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/presidio_evaluator/models/presidio_analyzer_wrapper.py | line 19 `score_threshold: float = 0.4,` | MATCH |
| 7 | Notebook 5: F2 0.91, P 0.921, R 0.907; OpenMed model; threshold 0.3; experiment_20260723-102549.json | PD1 R5 | https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/notebooks/5_Evaluate_Custom_Presidio_Analyzer.ipynb | "{'F2': 0.91, 'Precision': 0.921, 'Recall': 0.907}"; `model_name="OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1"`; `default_score_threshold=0.3`; "experiment_20260723-102549.json" | MATCH |
| 8 | "~30%" and F2 advice | PD1 R5 | https://presidio.dataprivacystack.org/evaluation/ | "boost the f score in ~30%."; "we recommend to use the β=2 score, which gives more importance to recall." | MATCH |
| 9 | presidio-research 0.3.2 pyproject: version, MIT, requires-python, analyzer floor | PD1 R7, inventory (a) | https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/pyproject.toml | line 3 `version = "0.3.2"`, line 6 `license = {text = "MIT"}`, line 7 `requires-python = ">=3.11,<3.14"`, line 18 `"presidio-analyzer>=2.2.364",`; tag commit 06d20306 dated 2026-08-04 | MATCH (see the 0.22 tag note) |
| 10 | presidio-structured alpha | PD5 R4 Summary and Detail | https://presidio.dataprivacystack.org/getting_started/getting_started_structured/ | "Alpha: This package is currently in alpha, meaning it is in its early stages of development. Features and functionality may change as the project evolves." | MATCH |
| 11 | Changelog 2.2.352 alpha entry; structured 0.0.8, MIT, Python <3.15, anonymizer floor | PD5 R4 | https://github.com/data-privacy-stack/presidio/blob/2.2.364/CHANGELOG.md ; .../presidio-structured/pyproject.toml | line 531 "Added alpha of presidio-structured, a library (presidio-structured) which re-uses existing logic …", under "## [2.2.352] - Jan 22nd 2024" (line 528); `version = "0.0.8"`, `license = "MIT"`, `"presidio-anonymizer (>=2.2.364,<3.0.0)"` | MATCH |
| 12 | Key sizes and cipher steps | PD3 R4 Summary and Detail | https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-anonymizer/presidio_anonymizer/operators/encrypt.py ; .../aes_cipher.py ; .../decrypt.py | encrypt.py:43 "Invalid input, {self.KEY} must be of length 128, 192 or 256 bits"; :25 `key = key.encode("utf8")`; aes_cipher.py:22 PKCS7 padder, :24 `iv = os.urandom(16)`, :27 `base64.urlsafe_b64encode(`, :41-42 decode and `iv = decoded_text[:16]`; decrypt.py:37 `Encrypt().validate(params)` | MATCH |
| 13 | Ownership tense ("moving to") | PD2 R4 and PD3 R4 Summaries; PD1 R4 | https://presidio.dataprivacystack.org/project_transition/ ; https://presidio.dataprivacystack.org/faq/ | "The Presidio project is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project …"; "Microsoft supports this transition …"; FAQ "It was originally created at Microsoft and has since transitioned to an independent, vendor-neutral project …" | MATCH (both sides carried in PD1 R4) |
| 14 | Commit 2523c7b on main after the tag, #2331, REMOVE_INTERSECTIONS | PD2 R2, R8, R9 | https://github.com/data-privacy-stack/presidio/commit/2523c7b74a469270c5c78bb253f140eafca21e31 | "fix(anonymizer): stop REMOVE_INTERSECTIONS from leaving flagged text in clear (#2331)", committed 2026-10-08; main head per ls-remote; tag file identical to the parent | MATCH on the facts; wording and label issue (fix 1) |
| 15 | Default operator replace, replace.py default string | PD2 R2 | .../anonymizer_engine.py ; .../operators/replace.py ; https://presidio.dataprivacystack.org/anonymizer/ | line 16 `DEFAULT = "replace"`; replace.py:18 `return f"<{params.get('entity_type')}>"`; page "anonymization operator is "replace" for all entities" | MATCH |
| 16 | Hash salt: random 32 bytes; under 16 bytes rejected | PD2 R2, R6 | .../operators/hash.py ; anonymizer page | :54 `salt = os.urandom(32)`; :47 `if len(salt) < 16:`; :49 "Salt must be at least 16 bytes (128 bits)."; page "Starting from version 2.2.361, the hash operator uses random salt by default for security." | MATCH |
| 17 | Docstring example positions in the new text | PD2 R1 | .../anonymizer_engine.py | "text: My name is BIP, BIP." with items `'start': 16, 'end': 19` and `'start': 11, 'end': 14` (lines 76-81) | MATCH |
| 18 | Image Redactor beta | PD4 R1 | https://presidio.dataprivacystack.org/image-redactor/ ; docs/image-redactor/index.md@2.2.364:3 | "Please notice, this package is still in beta and not production ready." (both) | MATCH |
| 19 | Tesseract default, tested v5.2.0, two OCR engines | PD4 R4 | https://presidio.dataprivacystack.org/image-redactor/ | "Presidio was tested with v5.2.0."; "Presidio offers two engines for OCR based PII removal. The first is the default engine which uses Tesseract OCR." | MATCH |
| 20 | REST multipart threshold 0.4 | PD4 R5 Summary | .../presidio-image-redactor/app.py | line 65 `redacted_image = self.engine.redact(im, color_fill, score_threshold=0.4)` | MATCH |
| 21 | Regex timeout default 60, changelog under 2.2.362 | PD6 R4 | .../pattern_recognizer.py ; CHANGELOG.md | :21 `REGEX_TIMEOUT_SECONDS = int(os.environ.get("REGEX_TIMEOUT_SECONDS", 60))`; CHANGELOG:161 "Configurable regex execution timeout (default 60 seconds) …", section "## [2.2.362] - 2026-03-15" (line 134) | MATCH |
| 22 | CHANGELOG has no 2.2.364 section; score_thresholds at lines 10 and 74; BatchDeanonymizeEngine line 38 | PD1 R4, PD3 R4, PD6 R4 | CHANGELOG.md@2.2.364 | line 5 "## [unreleased]", line 55 "## [2.2.363] - 2026-06-28"; line 10 per-recognizer threshold entry; line 74 "Recognizer registry YAML entries now accept score_thresholds …"; line 38 "Added BatchDeanonymizeEngine …" | MATCH |
| 23 | Tag commit and date; highest tag | PD1 R4 | git ls-remote and clone at tag | 779dbd286d5ef4d1fbe2514275fb1bce358f2417, 2026-07-22 11:17:15 +0300; highest numeric tags 2.2.361 … 2.2.364 | MATCH |
| 24 | Docs host 301 and Microsoft stub | PD1 R4 | https://data-privacy-stack.github.io/presidio/ ; https://microsoft.github.io/presidio/ | HTTP 301 to https://presidio.dataprivacystack.org/ (observed 2026-10-09); stub 200 with "This page has moved." | MATCH |
| 25 | gh-pages head e1987e57, 2026-07-04, live installation lists 3.10 to 3.13 | PD1 R4 | https://github.com/data-privacy-stack/presidio/tree/e1987e57d4474f14f9da03884ca1a99ece7dc6a5 | ls-remote refs/heads/gh-pages = e1987e57; commit date 2026-07-04 18:30:22 +0300; installation/index.html lists `<li>3.10</li>` … `<li>3.13</li>` only | MATCH |
| 26 | FAQ authentication, library not service | PD1 R1, R6 | https://presidio.dataprivacystack.org/faq/ | "Presidio is a library or SDK rather than a service."; "Presidio API endpoints do not include built-in authentication by design." | MATCH |
| 27 | Kubernetes sample ingress by default; Document Intelligence 24-hour retention | PD1 R6; PD4 R4 | https://presidio.dataprivacystack.org/samples/deployments/k8s/ ; https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/document-intelligence/data-privacy-security | "Presidio is deployed with an ingress controller by default, and uses nginx as ingress.class."; "The service stores submitted input data and analyze results for 24 hours after an analysis operation completes." | MATCH |

I also checked the following without giving each its own table row; all match:
- `ner_strength: float = 0.85,` (spacy_recognizer.py:41).
- default.yaml line 25 `- ORGANIZATION # Has many false positives`.
- Structured `language: str = "en"` (analysis_builder.py:95, :174) and `mixed_strategy_threshold: float = 0.5,` (:176). The effective detection threshold is 0 at lines 39-41; line 28 itself defaults to None, which the bullet's range covers.
- GLiNER defaults `urchade/gliner_multi_pii-v1` and `threshold: float = 0.30` (lines 37, 40).
- mask.py validation lines 47-54 and validators.py:54 "Expected parameter".
- `ANONYMIZERS` and `DEANONYMIZERS` (operators_factory.py:24-28).
- The `NONE` docstring at conflict_resolution_strategy.py:15 with two enum members.

Tally: 27 checked, 27 MATCH, 0 MISMATCH, 0 UNVERIFIABLE. Item 14 matches on the facts but carries required fix 1.

## 5. Inventory consistency (Check 5)

- Checker: `python benchtest/tools/check_drafts.py inventory benchtest/drafts/presidio_inventory_final.md --headers benchtest/drafts/presidio_two_level.md` gives (a) 14 rows x 8 cols, (b) 31 x 8, (c) 10 x 8, (d) 14 x 8, and "RESULT: 0 errors, 0 warnings". The counts equal the original draft and the P8 config numbers in changes.md section 5.
- No `**`, no backtick and no stray `|` in any cell (independent grep counts 0 and 0; every row has 8 cells).
- Labels: only allowed forms: [Documented: repo data-privacy-stack/presidio@2.2.364] 241, [Documented] 206, [Inferred] 51, [Not disclosed] 30, [Documented: repo data-privacy-stack/presidio-research@0.3.2] 8, [To be verified] 3 and [Documented: repo data-privacy-stack/presidio@037d239f] 1.
- Covered-by: every value is an exact Table 3 header (split on ";") or a marker. The inventory-only marker is used by presidio-cli, the presidio meta-package, presidio-research and the command-line path; the legacy marker by Legacy V1. The planned marker is not used.
- Covered-by choices (main's test: list a header only where that column's Detail cites the row's function):
  - PD5 on the seven operator rows: replace, redact, hash, mask, custom and encrypt are cited in PD5 R4 (factory list) and tested in PD5 R7. keep is cited in R4 only. These are acceptable.
  - surrogate_ahds is also cited in PD5 R4 but omitted, for a reason that is wrong. This is fix 4.
  - decrypt and deanonymize_keep are correctly PD3 only (PD5 R4 says they are not reachable through StructuredEngine).
  - PD6 on the Docker row: PD6 R7 Minimum setup names "docker run of the Analyzer image and a POST /analyze with ad_hoc_recognizers", so the test passes. PD5 is correctly absent: no structured image exists (PD5 R3, inventory (d) Docker caveat).
  - The REST Analyzer row carries PD1 and PD6, the REST Anonymizer row PD2 and PD3, and the Batch engines row PD1 to PD3 (BatchDeanonymizeEngine). These are consistent.
- Status "alpha" for presidio-structured is outside the header vocabulary (stable/beta/legacy). Main ruled that vendor wording stands (queue.md, P2 inventory Q1), and the cell quotes GSS.

## 6. URLs (Check 6)

Scope (lessons.md item 12): only R9 bullets of the six columns and inventory "Source URL" cells, deduplicated, giving 223 distinct URLs. That equals the 223 in changes.md section 5b.
- Hosts: github.com 161, presidio.dataprivacystack.org 50, learn.microsoft.com 4, huggingface.co 4, data-privacy-stack.github.io 1, microsoft.github.io 1, docs.nvidia.com 1, ollama.com 1.
- No API host, no `{…}` template and no localhost URL is in that set. Two URL-like strings in non-source inventory cells (http://localhost:11434 and the NVIDIA page with a trailing colon) were not requested.
- Method: `curl -s -L --max-time 30`, with a retry on non-200.
- Each github.com `/blob/<ref>/<path>` URL was checked through its raw.githubusercontent.com equivalent at the same ref (R020; github.com answers 403 to this session).
- Directory and commit pages, which cannot be served raw, were confirmed with git (clone at the tag, ls-remote, fetch of the commit).
- Full list: benchtest/scratchpad/verifier/presidio/url_check.txt.

| Class | Count | URLs | Verdict |
|---|---|---|---|
| 200 direct | 62 | all presidio.dataprivacystack.org pages (50), data-privacy-stack.github.io/presidio/ (301 then 200), microsoft.github.io/presidio/ stub, 4 learn.microsoft.com pages, 4 huggingface.co model cards, docs.nvidia.com Presidio page, ollama.com qwen2.5:1.5b | OK |
| 200 through raw equivalent | 146 | every github.com /blob/ URL: data-privacy-stack/presidio at 2.2.364 and at 037d239f, presidio-research at 0.3.2, and 10 third-party licence or meta files on main or master; direct github.com GET gives 403 for all 146 | OK (proxy limit, R020) |
| 400 through proxy | 13 | github.com/data-privacy-stack/presidio/tree/2.2.364/.../country_specific/{australia, germany, india, italy, korea, nigeria, philippines, singapore, spain, sweden, turkey, uk, us}/ | Expected: directory pages cannot be served raw; all 13 folders exist at tag 2.2.364 in the clone (3 to 14 files each) |
| 403 through proxy | 2 | github.com/data-privacy-stack/presidio/tree/e1987e57d4474f14f9da03884ca1a99ece7dc6a5 ; github.com/data-privacy-stack/presidio/commit/2523c7b | Expected: e1987e57 is the gh-pages head (ls-remote) and was fetched; 2523c7b is the main head (ls-remote) and was read with git show. Fix 1 swaps the commit URL for its full-SHA form |
| 404 or other | 0 | none | none |

Real URL failures: 0.
