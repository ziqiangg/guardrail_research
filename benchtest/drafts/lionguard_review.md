# LionGuard workbook: fresh verifier review

Date of checks: 2026-10-10. Reviewer: gr-verifier (did not draft, triage, resolve or merge). Inputs read: CLAUDE.md, drafts/README.md, rulings R005, R031 and R032 in full (R007, R009, R011, R015, R019, R020, R021 as applied in the files), queue.md rows starting "lionguard"; lionguard_two_level.md (read in full), lionguard_inventory_final.md (read in full), lionguard_changes.md (read in full), lionguard_resolutions_1.md (read in full), lionguard_triage.md (H items, headings), lionguard_summaries_preview.md (compared mechanically with the final). The originals lionguard_cols_a.md and lionguard_inventory.md were diffed, not re-read. Sources were re-read today with `python benchtest/tools/fetch_text.py` (raw text): the three model repos at their pinned shas (README, model code, inference.py, config.json, requirements.txt, LICENSE), lionguard-v1 config.json at 92cc0491, the demo Space files at 4ade46d1, the two dataset cards, the playbook page at 45908b48, arXiv 2507.15339 (html and abs), 2507.05980 (html and abs) and 2407.10995 (html), the three blog posts, the Sentinel Guardrails page, and the owners' pages (OpenAI embeddings and data controls, Gemini model page and Additional Terms, Gemma terms and Prohibited Use Policy, Google Generative AI Prohibited Use Policy, EmbeddingGemma page). The public Hugging Face Hub metadata JSON was read with plain unauthenticated GETs, as the resolver did. No sign-in, no form, no call to the Sentinel, OpenAI or Gemini API hosts, no install, no download of weights. Scripts and page copies are in benchtest/scratchpad/verifier/lionguard/. No file other than this one and that folder was modified.

## Verdict: PASS WITH FIXES

The merge is faithful to the triage and resolutions. Every substantive difference I could diff between the originals and the finals is in lionguard_changes.md. Both finals pass the checker with 0 errors and 0 warnings. The inventory has 4/11/8/11/4 = 38 rows, and its Covered-by counts are 21 header cells, 2 legacy and 15 inventory-only. The corrections from the resolutions (T21, T22, T25) are applied, and no known wrong string survives in a built cell. I spot-checked 36 facts at source: 33 MATCH and 3 MISMATCH. All three mismatches are wrong line numbers in code citations; the quoted text itself matches. Of 47 distinct URLs, 45 return 200 and 2 return the expected 403 (openai.com/policies pages, kept on purpose as HTTP facts). There are 5 required fixes:

1. The LN1 R1 Summary is not entailed by its own Detail (OpenAI or Gemini embedding, probabilities, severity levels).
2. The LN1 R7 Minimum setup bullet still says "choose a threshold yourself". This is an instruction to the reader, and it is the leftover of the "Pick your own threshold" wording that the merge removed from the Summary (R032).
3. Five code citations give wrong line numbers (LN1 R3 three bullets, R4 one bullet, R5 one bullet).
4. Inventory (e), "Hosted API behaviour", "What this sheet adds" cell: an inference is labelled `[Documented: repo govtech/lionguard-2@be4e38c9]`, and it covers 2.1 and Lite, which that label does not.
5. The inventory scope paragraph still calls the variants "open models". The T49 resolution removed "open" from the R1 Summary because "'open' depends on the unresolved licence reading T6".

None of the fixes changes a headline number or a Summary word count.

## Required fixes

1. **LN1 R1 Summary: not entailed by its own Detail (lines 3 to 13).**
   - Problem: the Summary (44 words, **[Documented]**) says the classifier "returns a probability for each harm category and severity level" and that "two variants embed text through OpenAI or Gemini, one locally".
     - R1 Detail supports "one locally" (line 11, Lite card), "risk score to each of the categories" (line 6) and the Hugging Face release (line 8).
     - No R1 bullet mentions OpenAI, Gemini, probabilities or severity levels. Those facts are only in R2, R4 and R5.
   - Fix (the Summary stays unchanged at 44 words):
     - Replace line 6 with: `• The playbook says "LionGuard assigns a risk score to each of the categories below. Some categories are further classified into severity levels, with Level 2 indicating higher severity than Level 1" **[Documented: repo govtech-responsibleai/playbook@45908b48]**` (playbook lionguard.md@45908b48 line 25; 27 words quoted).
     - After line 9 add: `• The LionGuard 2 card says it "leverages OpenAI's `text-embedding-3-large` with a multi-head classifier" **[Documented: repo govtech/lionguard-2@be4e38c9]**`
     - After that add: `• The `predict` docstring of LionGuard 2 says "Predict the probabilities of each label being true" (`lionguard2.py@be4e38c9:148`) **[Documented: repo govtech/lionguard-2@be4e38c9]**`
     - After line 10 add: `• The LionGuard 2.1 card says it "leverages Gemini's `gemini-embedding-001` with a multi-head classifier" **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**`
   - All three quotes were re-read today at the pins (README.md line 21 of both cards; lionguard2.py line 148). The R9 URLs for both pins are already in LN1 R9, so no URL change is needed.
   - Log the edit in lionguard_changes.md section 2 and update the R1 bullet count (9 to 12) in section 8b and in the preview.

2. **LN1 R7 line 174, Minimum setup bullet: "choose a threshold yourself" (R032; README section 4 "no instructions to the reader").**
   - Problem: the merge reworded the Summary's "Pick your own threshold" to "No threshold ships" (changes.md row 68), but the Detail bullet that says the same thing kept the imperative "and choose a threshold yourself because none ships".
     - It is the same class of wording as the "you run it yourself" that T49 removed.
     - R032 asks for "what testing would need" to be worded as a suggestion, not as a decided step or an instruction.
   - Replace line 174 with: `• **Minimum setup:** `transformers`, `torch` and `numpy` installed, the chosen model loaded with `trust_remote_code=True`, each test text embedded with that variant's embedder and passed to `predict`; no threshold ships, so a bench would need to choose one **[Inferred]**`
   - Optional, same reason: in line 176, replace "install `sentence-transformers`, log in to Hugging Face and accept Google's conditions for `google/embeddinggemma-300m`, then the classifier" with "`sentence-transformers` installed, a Hugging Face login and acceptance of Google's conditions for `google/embeddinggemma-300m`; the classifier".

3. **Code citations with wrong line numbers (LN1 R3 lines 44 to 46, R4 line 57, R5 line 115).** I re-read the raw files at the pins, after removing the status line that fetch_text.py adds.
   - R3 lines 44, 45 and 46 cite `:152` for "A numpy array of embeddings (N * INPUT_DIMENSION)". In all three files (lionguard2.py@be4e38c9, lionguard2.py@1c3a9ea7, lionguard2lite.py@d56c17a0) the text is on line 151; line 152 is blank. Replace `:152` with `:151` in the three bullets.
   - R4 line 57 cites `lionguard2.py@be4e38c9:119-139` for the layer shapes. The shared layers start at line 118 (`self.shared_layers = nn.Sequential(`) and the heads end at line 138. Replace with `:118-138`.
   - R5 line 115 cites `lionguard2.py@be4e38c9:194-196`. The file has 195 lines; the conversion and return are lines 193 to 195. Replace with `:193-195`.
   - Optional: R4 line 58 `:172-177` is better as `:171-176` (the loop starts at 171 and line 177 is blank).

4. **Inventory (e), row "Hosted API behaviour", column "What this sheet adds": inference under a single-repo Documented label.**
   - Problem: the cell reads "Self-hosted use has no endpoint or Sentinel key: the classifier head is called locally with embeddings the user generates, and the embedder key (OpenAI or Gemini) or the gated Gemma download replaces it [Documented: repo govtech/lionguard-2@be4e38c9] (README usage)".
     - "has no endpoint or Sentinel key" and "replaces it" are a comparison drawn by the drafter. No README says this.
     - The Gemini and Gemma halves come from the 2.1 and Lite repos, which the lionguard-2 label does not cover (README section 3 rules 1 and 5).
   - Replace the cell with: `The README usage loads the classifier from Hugging Face and calls predict locally on embeddings that the user generates with their own OpenAI key [Documented: repo govtech/lionguard-2@be4e38c9] (README usage). The 2.1 card does the same with the user's own Gemini key [Documented: repo govtech/lionguard-2.1@1c3a9ea7] (README usage), and the Lite card with a local google/embeddinggemma-300m embedder [Documented: repo govtech/lionguard-2-lite@d56c17a0] (README usage). Self-hosted use therefore involves no Sentinel endpoint or Sentinel key; the embedder key or the gated Gemma download takes its place [Inferred] (premise: none of the three README usage blocks calls a Sentinel endpoint)`
   - The cell has no `|`, `**` or backticks. Log it in changes.md section 3.

5. **Inventory scope paragraph (line 3): "published as open models".**
   - Problem: T49 removed "open" from the R1 Summary, with the logged reason "'open' depends on the unresolved licence reading T6". The scope paragraph still says "the localised content-moderation classifier published as open models on the Hugging Face org govtech".
     - The paragraph is not parsed into the workbook.
     - It is still a merged final, and the diagrammer takes facts from it.
   - Replace "published as open models on the Hugging Face org govtech" with "published as models on the Hugging Face org govtech". Log it in changes.md section 3.

## Optional suggestions

- LN1 R5 line 143: "Category-level F1 in the paper is far lower than binary F1" is the drafter's comparison. The paper says only "Absolute scores for all seven moderation systems range from 30-70 %, reflecting the intrinsic difficulty of fine-grained safety labels" (section 5.1). Suggested: `• The paper says per-category F1 for all seven moderation systems ranges "from 30-70 %, reflecting the intrinsic difficulty of fine-grained safety labels" (arXiv 2507.15339 section 5.1, Appendix E.3) **[Documented]**`.
- LN1 R4 line 86: the paper says LionGuard 2 "is deployed on the Singapore Government's AI Guardian platform", not "GovTech's". Suggested: "... and is deployed on "the Singapore Government's AI Guardian platform" (arXiv 2507.15339 section 3)".
- LN1 R4 line 73: the full sentence reads "Any future update to this embedding model would require may re-training and benchmarking." The fragment "may re-training and benchmarking" is verbatim but reads as a drafting slip. Suggest quoting "would require may re-training and benchmarking" with "(as written)".
- LN1 R5 line 119: `services.py@4ade46d1:114` is a fallback value inside the empty-text response (`"model_used": model_key or "lionguard-2.1"`). The default is declared in `app/backend/models.py@4ade46d1:12` (`default="lionguard-2.1"`) and in `app/frontend/script.js@4ade46d1:5` (`selectedModel: 'lionguard-2.1'`). Both were re-read today and are under the same Space pin. Citing models.py:12 would be stronger.
- LN1 R4 line 70: the 2.1-labelled bullet ends "so the stale name occurs only in the LionGuard 2 file". That conclusion also rests on the Lite file (line 71). Suggest ending the bullet after `gemini-embedding-001` and adding `• The stale name therefore occurs only in the LionGuard 2 file (premise: the 2.1 and Lite docstrings at line 97 name their own embedders) **[Inferred]**`.
- LN1 R4 line 84: the column names two GitHub paths (lionguard, lionguard-demo). The inventory (d) intro and T44 name four (also lionguard2 and LionGuard). Align the column to four.
- LN1 R4 line 85: the bullet joins a playbook fact and a blog fact under one plain `[Documented]` label. Splitting it gives the playbook half its repo label, as T58 did elsewhere.
- arXiv 2507.15339 Table 1 prints Qwen3-Embedding-0.6B with Test 87.2, above text-embedding-3-large's 77.0. Its ZH, MS and TA values (67.9, 60.9, 56.4) repeat the cohere-embed-multilingual-v3.0 row. Section 4.2.1 says text-embedding-3-large "achieved the highest binary F1". This looks like a typo in the paper. LN1 R4 line 72 quotes the sentence, so a reader who opens Table 1 will see the clash. A short `[Documented]` note in R4 or R8 would carry it (README section 3 rule 4).
- LN1 R7 line 188: "returned HTTP 403 to the fetch tool" could read "returned HTTP 403 to a plain GET" (less process wording).
- LN1 R8 line 216: "(the owners' data-handling pages are quoted in R7; ...)" is an internal cross-reference of the kind T59 removed elsewhere ("see R7"). Suggest "(the owners' data-handling pages are quoted in this column; ...)", or drop the clause.
- LN1 R9 Summary: "dataset" should be "datasets" (R9 cites both lionguard-2-synthetic-instruct and RabakBench).
- Inventory (d), arXiv 2507.15339 row: the arXiv title is "LionGuard 2: Building Lightweight, Data-Efficient & Localised Multilingual Content Moderators". The cell writes "and" for "&"; a title is better verbatim, and "&" is allowed in cells.
- Inventory (c) intro "No embedding service was called and no weights were downloaded." and inventory (d) demo row "no text was submitted to the hosted Space" are statements about how the research was done, and both end up in built cells. They are harmless, but they could be dropped (README section 4 "no process language").
- lionguard_changes.md section 5: "R5 (77.0, confirmed by T21) and R9 and R9 Summaries are unchanged" should read "R5 and R9".

## 1. Unlogged differences (Check 1)

Method:
- `benchtest/scratchpad/verifier/lionguard/diff_cols.py` parses LN1 from cols_a.md and from the final into per-row line lists and runs difflib SequenceMatcher per row.
- Each added or removed line is searched in lionguard_changes.md by normalised 60, 40 and 25-character prefixes (bold markers, backticks and ellipses removed).
- `diff_inv.py` (positional) and `diff_inv_keyed.py` (aligned by row key, needed because block (d) gained a row) compare the inventories cell by cell, word-level.

Results:
- Columns: 94 lines added, 52 removed. All 52 removals and 79 additions prefix-match a log entry.
- The other 15 additions are later parts of multi-bullet entries that the log joins with " // " and truncates. I matched each one by hand:
  - R2 taxonomy split: style 4 entry (row 38). The two halves join exactly to the original line 24 of cols_a.
  - R4 docstring bullets for 2.1 and Lite: T45 entry (row 45). The resolver proposed one combined bullet; the merger split it per repo, as the reason says.
  - R4 LICENSE exclusion: row 48.
  - R5 demo chat route: row 56. R5 max-of-categories bullet: row 61.
  - R6 Lite embedder limit: row 65.
  - R7 Gemma Model Derivative: row 73. R7 OpenAI endpoints table: row 76. R7 Gemini paid tier and Google use policy: row 77.
  - R7 possible sources of evaluation data and the demo-avoidance proposal: row 85.
  - Each of these 15 bullets is also verbatim in lionguard_resolutions_1.md, except the two R4 docstring bullets, which are the logged per-repo split.
- Inventory:
  - Every changed cell maps to a section 3 entry: T52, T19, T31, T22, T25, T29, T6 plus hygiene, T11, T12, T14, T34, T10, T43, T8, T54, T5, T16, T17 and T15 (new row).
  - The scope paragraph, (c) intro and (d) intro edits are logged.
  - Row keys are unchanged except the added arXiv 2507.05980 row.
- Summaries: the 7 changed Summaries listed in changes.md section 5 are exactly the ones that differ. lionguard_summaries_preview.md equals the final for all 9 Summaries (script compare).
- Result: no substantive unlogged change.

## 2. Sourcing and label strength (Check 2)

- Changed `[Documented]` facts trace to a resolution quote: T6, T9, T10, T11, T12, T15, T16, T19, T20, T22, T24, T25, T29, T34, T45, T48, T52, T57, T58, T5.
  - The only merger-made Documented text is the per-repo split of T45. Its facts are in the T45 evidence (lines 97 of the 2.1 and Lite files), and I re-read them today.
- Inferences labelled Documented:
  - Inventory (e) row 1 (fix 4).
  - R4 line 70, the "occurs only" clause (optional).
  - R5 line 143, "far lower than binary F1" (optional).
  - I also scanned every Documented bullet and cell for "so", "therefore", "probably", "because" and "which matches". The remaining hits are inside quotes, carry an `[Inferred]` label, or restate a quoted comparison: R2 line 27 "so the sources differ in strength" names three quoted texts; inventory (a) "which matches the Table 1 order" compares two quoted values.
- Absence claims: every `[Not disclosed]` bullet and cell names what was checked. The hygiene fix in conflict decision 6 is applied: "The LICENSE text has no research-only wording [Not disclosed] (LICENSE read in full)".
- Leftover scan over both finals:
  - 0 hits for: "run it yourself", "open Hugging Face weights", "publishes only the small classifier", "Which header order is right", "is advisable", "remains available", "gemini-embedding-2", "routed as", "R019", "not obviously reconcilable", "the bench will", "bench rule", "we use", "this is the plan", "data-handling decision", "a bench-design choice", "Pick your own threshold", "Reviewer notes", "not worked around", "roughly 4%", "600".
  - "about 4%" occurs twice, both consistent with T25: R5 line 134, the paper's own sentence quoted plus the Table 11 split; and R7 line 198, "the binary head over-predicting in about 4% of examples", which the Table 11 caption supports ("The binary head over-flags in only 4 % of cases").
  - "partial Tamil" occurs only inside quotes (R1 line 12 paper abstract; R2 lines 26 and 27; inventory (a) PB). The R2 Summary now names both the playbook and the paper wording (T27).
  - "yourself" occurs once (fix 2). "open models" occurs once (fix 5).
- R032 wording: R7 proposals read "A bench could ...", "Possible source of evaluation data", "would allow ... unlikely to suit"; the R8 default-variant question ends "(left open)"; inventory (c) reads "A bench could pin a revision". The one exception is fix 2.
- Third-party facts (main P4 Q2): they are limited to model identity, input limit, output dimension, gating, licence and terms, each marked "not GovTech docs". The Gemini lifecycle sentence is gone from both finals.
- Licence conflict (R031 Q04, main P5 Q-C): each text is its own labelled bullet. The relation is one `[Not disclosed]` bullet, and the finals draw no conclusion on permitted use. The paper's ethics paragraph continues: "For operational deployment within the Singapore Government's AI Guardian platform, we restrict API access to internal government applications …". That concerns the hosted service, so it belongs under Sentinel and does not change the relation bullet.

## 3. Summary entailment and style (Check 3)

- Checker: `python benchtest/tools/check_drafts.py columns benchtest/drafts/lionguard_two_level.md --final --expect 1` gives "columns: 1 LN1=LionGuard: Localised harmful-content classification", "RESULT: 0 errors, 0 warnings".
- The header equals R031 Q01 exactly. The prefix is "LionGuard:".
- Word counts (preview, re-counted): 44, 43, 39, 40, 39, 38, 59 (R7, limit 60), 36, 27. None is over its limit.
- R8 starts with "**Key open questions.**" and has no label. R9 is plain.
- Pins: every repo label in R1 to R7 has an R9 URL with the same ref in LN1 R9 (checker; confirmed by hand for lionguard-demo@4ade46d1, RabakBench@3c02a5b8, lionguard-2-synthetic-instruct@8aa43f61 and playbook@45908b48).
- Entailment, row by row:
  - R1: not entailed (fix 1).
  - R2: entailed by the key list (four keys with l1/l2), the playbook "partial Tamil" bullet and the paper "remains moderate" bullet.
  - R3: entailed by the section 3 bullets and the predict docstring bullets.
  - R4: entailed by the embedder-card bullets, the custom-code bullets and the serving-route bullet.
  - R5: entailed by the predict bullets (dictionary of probabilities, no threshold) and the Table 1 and section 5.1 bullets.
  - R6: entailed by the input_dim bullets, the two "users to input their own ... API key" bullets and the Lite task-prefix bullet.
  - R7: entailed by the minimum-setup, Lite-path, login, Gemma Appendix and OpenAI/Gemini path bullets.
  - R8: each listed question has an R8 bullet.

## 4. Spot-checks at source (Check 4)

All reads 2026-10-10 with fetch_text.py (raw). HF files were read at the pinned revision through /raw/<sha>/. Line numbers below count from the file's first line, after removing the status line that fetch_text.py adds.

| # | Claim | Location | Source URL | Verbatim quote or value seen | Match |
|---|---|---|---|---|---|
| 1 | Playbook describes LionGuard as GovTech's localised content moderation guardrail | LN1 R1 | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/lionguard.md | line 11 "LionGuard is GovTech's localised content moderation guardrail for Singapore's linguistic and cultural context, addressing limitations in localisation and contextualisation faced by standard moderation guardrails." | MATCH |
| 2 | Three versions share methodology; open-sourced for self-hosting; 2.1 best performance, Lite local | LN1 R1, R4; INV (a) | same playbook file | "All share the same methodology and differ only in the embedding model they use"; "All three versions are open-sourced for self-hosting via Hugging Face and accessible through the Sentinel API"; "For best performance, we recommend LionGuard 2.1. For local deployment, we recommend LionGuard 2 Lite." | MATCH |
| 3 | Playbook "partial Tamil", Level 2 flags Level 1, retrain in two minutes | LN1 R2, R4 | same playbook file | "Support for English, Singlish, Chinese, Malay, and partial Tamil."; "If a Level 2 instance is detected, Level 1 is also flagged by design."; "can be fully retrained within two minutes on standard CPUs" | MATCH |
| 4 | Card wording and embedders of 2, 2.1, Lite; Lite runs locally | LN1 R1, R4, R6 | https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/README.md ; .../lionguard-2.1/... ; .../lionguard-2-lite/... | "tuned for English/Singlish, Chinese, Malay, and Tamil in the Singapore context"; "It leverages OpenAI's `text-embedding-3-large`"; "It leverages Gemini's `gemini-embedding-001`"; "This `lite` version leverages Google's `embeddinggemma-300m` (768-dimensional embeddings)"; "LionGuard 2 Lite runs fully locally, with no external API calls." | MATCH |
| 5 | Stale docstring text-embedding-3-small at line 97 (2); own embedders at line 97 (2.1, Lite) | LN1 R4 | .../lionguard2.py at the three pins | 2: "encoded with OpenAI's `text-embedding-3-small` model." (97); 2.1: "encoded with Gemini's `gemini-embedding-001` model." (97); Lite: "encoded with Google's `embeddinggemma-300m` model." (97) | MATCH |
| 6 | predict takes "A numpy array of embeddings (N * INPUT_DIMENSION)" at :152 | LN1 R3 (3 bullets) | same files | text present on line 151 in all three files; line 152 blank | MISMATCH (line; fix 3) |
| 7 | Layer shapes at :119-139 | LN1 R4 | lionguard2.py@be4e38c9 | Linear(input_dim, 256) ... Dropout(0.2) at 118-125; heads Linear(128, 32), ReLU, Linear(32, 2) "# 2 thresholds for ordinal classification", Sigmoid at 128-138 | MISMATCH (line; fix 3) |
| 8 | Ordinal averaging at :179-180; P(y>1) comment at :175 | LN1 R5 | lionguard2.py at the three pins | 179 "# If L2 category exists, and P(L2) > P(L1),"; 180 "# Set both P(L1) and P(L2) to their average to maintain ordinal consistency"; 175 "# j=1 uses P(y>1) if L2 category exists" | MATCH |
| 9 | No threshold; returns lists at :194-196 | LN1 R5 | lionguard2.py@be4e38c9 | 193-195 `for key, value in output.items():` / `output[key] = value.numpy().tolist()` / `return output`; file ends at 195 | MISMATCH (line; fix 3) |
| 10 | Parameters, file sizes, last-modified, head shas, gated false, LICENSE identical | LN1 R4; INV (a) | https://huggingface.co/api/models/govtech/lionguard-2 (and -2.1, -2-lite) | 2: "F32":848942, model.safetensors size 3398496, lastModified 2025-11-18T07:20:21Z, sha be4e38c9...; 2.1: 848942, 3398496, 2025-11-18T09:01:38Z, sha 1c3a9ea7...; Lite: 259118, 1039200, 2025-11-18T08:59:25Z, sha d56c17a0...; LICENSE blobId a28fcf41 in all three | MATCH |
| 11 | config: input_dim 3072 (2), 768 (Lite); category_order; auto_map | LN1 R4, R6 | config.json at the pins | "input_dim": 3072; "category_order": ["binary", "hateful", "insults", "sexual", "physical_violence", "self_harm", "all_other_misconduct"]; "AutoModel": "lionguard2.LionGuard2Model"; Lite "input_dim": 768 | MATCH |
| 12 | Embedding calls, Lite task prefix and encode note; 2.1 passes no dimension | LN1 R6 | README.md and inference.py at the pins | 2: `model="text-embedding-3-large",` `dimensions=3072`; 2.1: `genai.Client(api_key=os.getenv("GEMINI_API_KEY"))`, `model="gemini-embedding-001",` `contents=texts` (no dimension); Lite: `f"task: classification \| query: {c}"`, "# NOTE: use encode() instead of encode_documents()" | MATCH |
| 13 | Requirements pins | LN1 R6; INV (c) | requirements.txt at the pins | 2: numpy==2.3.1, openai==1.93.0, transformers==4.50.3, torch==2.3.1; 2.1: numpy==2.3.1, transformers==4.50.3, torch==2.3.1, google-genai==1.50.1 | MATCH |
| 14 | LICENSE text and exclusion | LN1 R4; INV (a), (c) | https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/LICENSE | "and/or any asset or code identified by the Government Technology Agency ("GovTech") as not licensed to you ... the contents of this repository are provided under the MIT License SUBJECT FURTHER TO THE FOLLOWING:" | MATCH |
| 15 | Paper: input/output filter, any text, replaces predecessor, throughput | LN1 R3, R4, R6 | https://arxiv.org/html/2507.15339 | "designed as a lightweight moderation system for any text content"; "both an input filter (screening user prompts) and an output filter (verifying model responses)"; "LionGuard 2 replaces its predecessor and is deployed on the Singapore Government's AI Guardian platform"; "≈300 tokens s−1. As most latency comes from the embedding call" | MATCH (see optional on "GovTech's") |
| 16 | 0.85M parameters, 3.2 MB; single binary head (section 4.2.2) | LN1 R2, R4 | same | "we attached a single binary head (safe/unsafe) as we found it to consistently boost overall F1"; "The resulting classifier contains 0.85M parameters and occupies only 3.2 MB on disk." | MATCH |
| 17 | Training set 26,207 = 20,333 + 2,098 + 3,776; 70% smaller | LN1 R4 | same, section 4.1.4 | "The final training set contained 26,207 unique texts: 20,333 online comments, 2,098 synthetically augmented comments, and 3,776 texts from open-source English datasets."; "70% smaller than what was used for LionGuard 1" | MATCH |
| 18 | Table 1 and Table 3 LionGuard 2 values and header orders; comparators on Test | LN1 R5; INV (a) | same | Table 1 "Test \| RabakBench \| SS \| ZH \| MS \| TA" row "77.0 \| 88.1 \| 87.8 \| 78.4 \| 66.6"; Table 3 "SS \| MS \| ZH \| TA", same values, SGHateCheck 98.8, 92.1, 97.4, 64.5, SGToxicGuard 99.7, 98.2, 99.2, 71.5; Test column OpenAI Moderation 54.7, AWS Bedrock 57.1, LlamaGuard 3 8B 27.1, LlamaGuard 4 12B 26.5; AWS Bedrock RabakBench "69.6 \| – \| 21.1 \| –" | MATCH |
| 19 | Table 4 English benchmarks; Table 5 noise; Table 8 Tamil 66.5 | LN1 R2, R5 | same | "LionGuard 2 \| 73.7 \| 73.7 \| 70.5 \| 100.0"; "LionGuard 2 \| 87.1 \| 85.6"; "LionGuard 2 \| 66.5 \| 64.5 \| 71.5" | MATCH |
| 20 | About 4% disagreement; Table 11 4.19 / 0.70 / 43 075; 9.99; max removes mismatch | LN1 R5, R7; INV (a) | same, section 7.2 and Appendix E.1 | "About 4% of examples aggregated across two localised and three general datasets show disagreement between the binary head and category heads"; "Overall average \| 4.19 \| 0.70 \| 43 075"; 9.99 present; "deriving the binary decision as max(category-scores) removes the mismatch, we keep the dedicated binary head as it boosts performance" | MATCH |
| 21 | Table 13 Chinese 85.0, Malay 81.4, Tamil 41.1; prompt-injection in the red-team brief | LN1 R2 | same, section 5.3 and Appendix E.2 | LionGuard 2 row F1 "85.0 \| 81.4 \| 41.1 \| 72.7"; "prompt-injection or role-playing scenarios" | MATCH |
| 22 | Limitation quote "may re-training and benchmarking"; Tamil moderate; translated Tamil worsened | LN1 R2, R4 | same, sections 7.1, 5.3, 7.3 | "Any future update to this embedding model would require may re-training and benchmarking."; "its Tamil performance remains moderate"; "adding LLM-translated Tamil data worsened results" | MATCH (optional wording) |
| 23 | 1 internal + 16 public benchmarks; category F1 30 to 70 | LN1 R5 | same, section 5.1 | "on 1 internal test set and 16 public benchmarks, including 13 localised datasets ... and 4 general English datasets"; "Absolute scores for all seven moderation systems range from 30-70 %" | MATCH (optional on "far lower") |
| 24 | Ethics, contributions, conclusion statements | LN1 R4; INV (a), (c) | same | "Our model weights are published on Hugging Face exclusively for research and public interest purposes only, with clear usage guidelines that prohibit deployment for harmful applications."; "We release the classifier weights and a portion of our training data to support future research in LLM safety."; "By releasing our model weights and training data subset, we aim to support broader adoption of localisation-aware moderation strategies" | MATCH |
| 25 | arXiv dates and authors (2507.15339, 2507.05980) | INV (d) | https://arxiv.org/abs/2507.15339 ; https://arxiv.org/abs/2507.05980 | "[Submitted on 21 Jul 2025 (v1), last revised 28 Sep 2025 (this version, v2)]", "Authors:Leanne Tan, Gabriel Chua, Ziyu Ge, Roy Ka-Wei Lee"; "[Submitted on 8 Jul 2025 (v1), last revised 2 Feb 2026 (this version, v2)]", "Authors:Gabriel Chua, Leanne Tan, Ziyu Ge, Roy Ka-Wei Lee" | MATCH |
| 26 | RabakBench Table 4 LlamaGuard 4 12B and AWS Bedrock | LN1 R5; INV (a) | https://arxiv.org/html/2507.05980 | "LlamaGuard 4 12B \| 60.53 \| 54.20 \| 65.92 \| 73.77 \| 63.61" (CIs omitted); "AWS Bedrock Guardrail \| 66.50 \| 0.59 \| 18.49 \| 0.57" under Singlish, Chinese, Malay, Tamil | MATCH |
| 27 | Blog 29 Jul 2025: input and output heading, 16 benchmarks, Chinese 88% Malay 78%, open-sourced | LN1 R1, R3, R5; INV (d) | https://blog.ai.gov.sg/introducing-lionguard-2-multilingual-llm-guardrail-for-singapore/ | "29 Jul 2025"; "LionGuard 2 as an input and output guardrail"; "across 16 benchmarks"; "Performance remains robust for Chinese (88%) and Malay (78%)"; "LionGuard 2 is open-sourced, including model weights and part of the training data." | MATCH |
| 28 | Blog 21 Aug 2026: 11 heads, retrained model very soon, Sentinel users only, 200 reports | LN1 R4; INV (a), (d) | https://blog.ai.gov.sg/guardrails-in-the-wild-closing-the-retraining-loop-for-lionguard-2/ | "21 Aug 2026"; "LionGuard 2 uses a shared representation feeding into 11 classification heads"; "For Sentinel users, we'll be rolling out the first retrained LionGuard 2 model, incorporating your feedback, very soon."; "Reporting and access to retrained models are currently only available to Sentinel users within the Singapore Government." | MATCH |
| 29 | Blog 28 Sep 2026: LionGuard 2.1 and Jev numbers, 0.5 threshold, private split, calibration, latency | LN1 R4, R5, R6; INV (a) | https://blog.ai.gov.sg/decision-models-for-guardrails-exploring-jev-and-kev-for-moderation/ | "28 Sep 2026"; LionGuard 2.1 column 0.7318, 0.8618, 0.8420, 0.7267, 0.8688, 1.0000, 0.7397; Jev 0.8385, 0.8745, 0.8766, 0.7805, 0.8809, 1.0000, 0.7639; "using the same 0.5 threshold"; "a held-out private LionGuard test split and RabakBench"; "can be run locally or through an API depending on the variant"; "A fair latency comparison would therefore require a more controlled setup." | MATCH |
| 30 | Sentinel versions table, spelling, token limits, default | LN1 R3, R4, R6; INV (e) | https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails | "lionguard-2 \| OpenAI's text-embedding-large-3 \| 8192"; "lionguard-2-1 \| Google's gemini-embedding-001 \| 2048"; "lionguard-2-lite \| Google's embeddinggemma-300m \| 2048"; "besides the default lionguard-2" | MATCH |
| 31 | Owners' limits and dimensions | LN1 R6; INV (c), (e) | https://developers.openai.com/api/docs/guides/embeddings ; https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001 ; https://huggingface.co/google/embeddinggemma-300m | "By default, the length of the embedding vector is 1536 for text-embedding-3-small or 3072 for text-embedding-3-large."; table "text-embedding-3-large ... 8192"; "Input token limit 2,048"; "Output dimension size Flexible, supports: 128 - 3072"; "Maximum input context length of 2048 tokens" | MATCH |
| 32 | EmbeddingGemma gate, login, licence | LN1 R7; INV (a), (c) | https://huggingface.co/google/embeddinggemma-300m | "This repository is publicly accessible, but you have to accept the conditions to access its files and content."; "Log in or Sign Up to review the conditions and access this model content."; "License: gemma" | MATCH |
| 33 | OpenAI data controls and the /v1/embeddings row | LN1 R7; INV (c) | https://developers.openai.com/api/docs/guides/your-data | "data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)"; "retained for up to 30 days"; row "/v1/embeddings \| No \| 30 days \| None \| Yes" | MATCH |
| 34 | Gemma terms, Prohibited Use Policy, Gemini Additional Terms, Google Generative AI policy | LN1 R7; INV (c) | https://ai.google.dev/gemma/terms ; https://ai.google.dev/gemma/prohibited_use_policy ; https://ai.google.dev/gemini-api/terms ; https://policies.google.com/terms/generative-ai/use-policy | "Last modified: April 1, 2026"; EmbeddingGemma in the Appendix; "for the restricted uses set forth in the Gemma Prohibited Use Policy"; "in violation of applicable laws and regulations."; "For clarity, Outputs are not deemed Model Derivatives."; "Last modified: February 21, 2024"; "Generating content that promotes or encourages hatred;"; "Effective March 23, 2026"; "Do not submit sensitive, confidential, or personal information to the Unpaid Services."; "Your access to Gemini API is a "Paid Service" only when accessing the API through a Cloud Project associated with an active billing account."; "Last Modified: December 17, 2024"; "Do not engage in sexually explicit, violent, hateful, or harmful activities." | MATCH |
| 35 | Demo Space: bands, chat threshold, default model, Google Sheet, OpenAI calls | LN1 R5, R7; INV (d) | https://huggingface.co/spaces/govtech/lionguard-demo/blob/4ade46d19acee9c9088c711533a7c47fe24a8e3b/app/backend/services.py | 123 `if binary_score < 0.4:`, 125 `elif 0.4 <= binary_score < 0.7:`; 232 `return binary_prob > threshold, binary_prob`; 262 `... message, model_key, 0.5)`; 158 and 338 `if GOOGLE_SHEET_URL and GOOGLE_CREDENTIALS:`; 199 to 223 OpenAI chat (gpt-4.1-nano) and `moderations.create`; 114 `"model_used": model_key or "lionguard-2.1"` (models.py:12 `default="lionguard-2.1",`; script.js:5 `selectedModel: 'lionguard-2.1',`) | MATCH (optional on the line cited) |
| 36 | Dataset cards: RabakBench 132 per language and intended use; synthetic-instruct subset and 2,055 / 43 | LN1 R4, R7; INV (d) | https://huggingface.co/datasets/govtech/RabakBench/tree/3c02a5b8574b0d0374d532704be6971e67532e22 ; https://huggingface.co/datasets/govtech/lionguard-2-synthetic-instruct/tree/8aa43f6172eb7eb158fd433fe3cf627c9a30db26 | "5 364 short texts (1,341 per language) ... This repo contains the public set which is 132 samples per language."; "Benchmark moderation APIs / guardrails."; "Fine-tuning models to generate unsafe content."; "This dataset is a subset of the LionGuard 2 training corpus."; "2 055 safe · 43 unsafe (≈ 2 % unsafe)" | MATCH |

I also checked the following without giving each its own table row; all match:
- lionguard-v1 config.json@92cc0491 binary thresholds `"high_recall": 0.2`, `"balanced": 0.5`, `"high_precision": 0.8`, `"model_type": "ridge_classifier"`.
- arXiv 2407.10995: "final training dataset of 138,000 texts"; "LionGuard's PR-AUC score of 0.819 is higher than OpenAI's 0.675"; "LionGuard may not generalize well to other domains and languages".
- Playbook variant table: "Strong performance across all benchmarks, particularly in multilingual settings." and "Most lightweight, on-prem variant with no external API dependency, best for restricted environments and local inference."
- Paper section headings (html v2) for every section number cited: 3, 4.1.3, 4.1.4, 4.2.1, 4.2.2, 5.1, 5.3, 6.3, 7.1 to 7.3, 8, Ethical Considerations, E.1, E.2, E.3.

Tally: 36 checked, 33 MATCH, 3 MISMATCH (all line numbers, fix 3), 0 UNVERIFIABLE.

## 5. Inventory consistency (Check 5)

- Checker: `python benchtest/tools/check_drafts.py inventory benchtest/drafts/lionguard_inventory_final.md --headers benchtest/drafts/lionguard_two_level.md` gives (a) 4 rows x 12 cols, (b) 11 x 7, (c) 8 x 7, (d) 11 x 7, (e) 4 x 6, "RESULT: 0 errors, 0 warnings". This is 4/11/8/11/4 = 38 rows, as logged for the P8 config.
- Covered-by (independent count):
  - 21 cells equal the exact header "LionGuard: Localised harmful-content classification": (a) 3, (b) 11, (c) 7.
  - 2 cells carry "— (legacy, not in Table 3)": the LionGuard 1 row and the BAAI embedder row.
  - 15 cells carry "— (inventory only, not in Table 3)": (d) 11, (e) 4.
  - No Sentinel header is listed anywhere (R005, no double counting). This matches changes.md section 5.
- The T55 convention (block (d) references stay inventory-only; block (c) dependencies carry the LN1 header) is applied consistently.
- No `**` and no backtick in any cell. Every row has the header's cell count, so there is no stray `|`.
- Every bracketed label is one of the allowed forms. Repo labels use 8-character shas.
- Column-inventory agreement:
  - The LN1 facts repeated in the inventory agree: sizes, keys, embedders and dimensions, Table 1 and Table 3 values and the swap inference (both `[Inferred]`), the 4.19 / 0.70 split, throughput, licence texts, terms, and the demo bands and data flow.
  - Exceptions: the two-versus-four GitHub paths checked (optional), and inventory (e) row 1 (fix 4).
- Block intros: (a), (b), (c), (d) and (e) carry no ruling ids, triage ids or session references.

## 6. URLs (Check 6)

Scope: R9 bullets of LN1 and inventory "Source URL" cells, deduplicated, give 47 distinct URLs (`benchtest/scratchpad/verifier/lionguard/urls.txt`). Each was fetched with `curl -s -o /dev/null -L --max-time 60` (results in `url_check.txt`). The endpoint https://sentinel.aiguardian.gov.sg/api/v1/validate appears only as cell text in inventory (e). It is a hosted API host, so it was not called.

- 45 return 200 with no redirect.
- 2 return 403: https://openai.com/policies/terms-of-use and https://openai.com/policies/usage-policies. Both are expected: they are cited as HTTP 403 facts in LN1 R7 line 188 and inventory (c), and changes.md section 5 lists them as expected non-200s.
- https://huggingface.co/datasets/govtech/RabakBench-full returns 200 for the public page; its files are behind a manual gate, as inventory (d) says. https://huggingface.co/google/embeddinggemma-300m likewise returns 200 with gated files.
- The three https://huggingface.co/api/models/govtech/... URLs in R9 are public metadata JSON (200, unauthenticated GET).

### Appendix: URL table

| URL | Status | Used in |
|---|---|---|
| https://ai.google.dev/gemini-api/docs/embeddings | 200 | INV (a), INV (c), LN1 R9 |
| https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001 | 200 | INV (c), LN1 R9 |
| https://ai.google.dev/gemini-api/terms | 200 | INV (c), LN1 R9 |
| https://ai.google.dev/gemma/prohibited_use_policy | 200 | INV (c), LN1 R9 |
| https://ai.google.dev/gemma/terms | 200 | INV (c), LN1 R9 |
| https://arxiv.org/abs/2407.10995 | 200 | INV (a), INV (d) |
| https://arxiv.org/abs/2507.05980 | 200 | INV (d) |
| https://arxiv.org/abs/2507.15339 | 200 | INV (a), INV (d) |
| https://arxiv.org/html/2407.10995 | 200 | INV (a), INV (d) |
| https://arxiv.org/html/2507.05980 | 200 | INV (d), LN1 R9 |
| https://arxiv.org/html/2507.15339 | 200 | INV (a), INV (c), INV (d), LN1 R9 |
| https://blog.ai.gov.sg/decision-models-for-guardrails-exploring-jev-and-kev-for-moderation/ | 200 | INV (a), INV (d), LN1 R9 |
| https://blog.ai.gov.sg/guardrails-in-the-wild-closing-the-retraining-loop-for-lionguard-2/ | 200 | INV (a), INV (d), LN1 R9 |
| https://blog.ai.gov.sg/introducing-lionguard-2-multilingual-llm-guardrail-for-singapore/ | 200 | INV (a), INV (d), LN1 R9 |
| https://developers.openai.com/api/docs/guides/embeddings | 200 | INV (c), INV (e), LN1 R9 |
| https://developers.openai.com/api/docs/guides/your-data | 200 | INV (c), LN1 R9 |
| https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/lionguard.md | 200 | INV (a), INV (d), LN1 R9 |
| https://govtech-responsibleai.github.io/playbook/tools/lionguard/ | 200 | INV (d), LN1 R9 |
| https://govtech-responsibleai.github.io/playbook/tools/sentinel/ | 200 | INV (e) |
| https://huggingface.co/BAAI/bge-large-en-v1.5 | 200 | INV (c) |
| https://huggingface.co/api/models/govtech/lionguard-2 | 200 | LN1 R9 |
| https://huggingface.co/api/models/govtech/lionguard-2-lite | 200 | LN1 R9 |
| https://huggingface.co/api/models/govtech/lionguard-2.1 | 200 | LN1 R9 |
| https://huggingface.co/datasets/govtech/RabakBench-full | 200 | INV (d) |
| https://huggingface.co/datasets/govtech/RabakBench/tree/3c02a5b8574b0d0374d532704be6971e67532e22 | 200 | INV (d), LN1 R9 |
| https://huggingface.co/datasets/govtech/lionguard-2-synthetic-instruct/tree/8aa43f6172eb7eb158fd433fe3cf627c9a30db26 | 200 | INV (d), LN1 R9 |
| https://huggingface.co/google/embeddinggemma-300m | 200 | INV (a), INV (c), LN1 R9 |
| https://huggingface.co/govtech/lionguard-2-lite/blob/d56c17a08a937f2591a906fb5c8ec699a844c422/requirements.txt | 200 | INV (c) |
| https://huggingface.co/govtech/lionguard-2-lite/tree/d56c17a08a937f2591a906fb5c8ec699a844c422 | 200 | INV (a), LN1 R9 |
| https://huggingface.co/govtech/lionguard-2.1/blob/1c3a9ea7718f81ea32e6688c0ff18ac8866525e8/requirements.txt | 200 | INV (c) |
| https://huggingface.co/govtech/lionguard-2.1/tree/1c3a9ea7718f81ea32e6688c0ff18ac8866525e8 | 200 | INV (a), LN1 R9 |
| https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/LICENSE | 200 | INV (c), LN1 R9 |
| https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/README.md | 200 | INV (b), INV (c), INV (e) |
| https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/config.json | 200 | INV (c) |
| https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/inference.py | 200 | LN1 R9 |
| https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/lionguard2.py | 200 | INV (b), LN1 R9 |
| https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/map_benchmark_labels.ipynb | 200 | LN1 R9 |
| https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/requirements.txt | 200 | INV (c) |
| https://huggingface.co/govtech/lionguard-2/tree/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591 | 200 | INV (a), LN1 R9 |
| https://huggingface.co/govtech/lionguard-v1/tree/92cc0491764602c97031693a7f1a2bcc82c6aaf9 | 200 | INV (a), INV (c) |
| https://huggingface.co/spaces/govtech/lionguard-demo/blob/4ade46d19acee9c9088c711533a7c47fe24a8e3b/app/backend/services.py | 200 | LN1 R9 |
| https://huggingface.co/spaces/govtech/lionguard-demo/tree/4ade46d19acee9c9088c711533a7c47fe24a8e3b | 200 | INV (d), LN1 R9 |
| https://openai.com/policies/terms-of-use | 403 (expected; HTTP fact) | INV (c), LN1 R9 |
| https://openai.com/policies/usage-policies | 403 (expected; HTTP fact) | INV (c), LN1 R9 |
| https://policies.google.com/terms/generative-ai/use-policy | 200 | INV (c), LN1 R9 |
| https://www.aiguardian.gov.sg/docs/sentinel/sentinel-getting-started | 200 | INV (e) |
| https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails | 200 | INV (a), INV (e), LN1 R9 |
