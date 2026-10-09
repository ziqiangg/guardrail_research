# Llama Guard triage of open evidence items (DRAFT)

Sources triaged: `lg_cols_a.md` (LG1, LG2), `lg_cols_b.md` (LG3, LG4, LG5), `lg_inventory.md` (sheet 3d: tables (a) variants, (b) crosswalk, (c) integration paths), plus the three "Reviewer notes" sections. No research done; source suggestions only. Nothing here is verified.

Legend
- File short names: A = lg_cols_a.md, B = lg_cols_b.md, INV = lg_inventory.md.
- Location notation: `LGn Rk` = column LGn, row Rk (Summary or Detail bullet named in brackets). `INV(a) <variant>` = variant table row; `INV(b) <concept>` = crosswalk row; `INV(c) <path>` = integration path row; `RN-A` / `RN-B` / `INV-RN n` = Reviewer notes of A, B, INV (n = numbered item).
- Labels: ND = [Not disclosed]; TBV = [To be verified]; NF = [Not found]; R8 = unlabelled R8 bullet; INF = [Inferred] dependent on an unchecked premise; SUM = fact or number depends on a summarised WebFetch.
- Class: a = doc-answerable (official Meta source or official repo), b = needs testing (stays open), c = licensing.
- Priority: H = affects a Summary line or a headline number; M = Detail-level; L = cosmetic or low impact.
- Short source names: PL = meta-llama/PurpleLlama @ 172c1074 (Llama-Guard{,2,3,4}/**/MODEL_CARD.md, Llama-Guard3/1B/ET_INSTRUCTIONS.md); HF = huggingface.co/meta-llama/<model>; DOCS3/DOCS4/DOCS2 = dev.meta.ai/llama/docs/model-cards-and-prompt-formats/{llama-guard-3,llama-guard-4,meta-llama-guard-2}/; PROT = dev.meta.ai/llama/llama-protections/; CB = meta-llama/llama-cookbook @ 2f22a9eb; OGX = ogx-ai/ogx; NEMO = NVIDIA-NeMo/Guardrails.

## Counts

Total 59 deduplicated items (T1 to T59), drawn from 29 R8 bullets, the explicit labels in A (4 ND) and B (3 TBV, 4 ND), the inventory cells (14 ND, 4 TBV, 4 NF), and the Reviewer notes of A, B and INV.

| Class | Count | of which H |
|---|---|---|
| a doc-answerable | 44 | 16 |
| b needs testing | 12 | 3 |
| c licensing | 3 (T58 and T59 are "suggested", not in drafts) | 1 |
| Total | 59 | 20 |

Priority totals: H 20, M 25, L 14.

Items touching each source file (an item can touch several): lg_cols_a.md 28, lg_cols_b.md 34, lg_inventory.md 35.

Dedup note: identical items appearing in several columns are merged into one id and all locations are listed (the threshold, latency, LG4 language, custom-category and OGX items each appear in 3 to 6 places). Where one open question has both a "does a doc say it" half and a "does it hold on our data" half, it is split into two ids (a + b), as in the NeMo triage. Items marked "(suggested)" are not open in the drafts; they are licence questions a reviewer would normally ask and are added for completeness.

Raw label census (before dedup): [Not disclosed] A 4, B 4, INV 14 table cells (+1 prose); [To be verified] A 0, B 3, INV 4 (+2 non-standard "[To be verified: ...]" forms); [Not found] INV 4; R8 bullets LG1 7, LG2 7, LG3 6, LG4 5, LG5 4 = 29 (INV has no R8; its "Not found" list gives 5 bullets).

## Triage table

| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |
|---|---|---|---|---|---|
| T1 | Is any decision threshold for the first-token "unsafe" probability documented for 3-8B, 3-8B-INT8, 3-1B, 3-11B-V, LG4? (8B card only says "apply score thresholding"; LG2 uses 0.5) | A LG1 R5 [ND, and "absence in fetched text" bullet], A LG1 R8, A LG2 R5 [ND], A LG2 R8, B LG3 R5 [ND], B LG3 R8 (x2: "official F1 or threshold", "any official threshold"), B LG4 R4 (Score bullet), INV(a) 3-1B / 3-8B-INT8 / 3-11B-V / LG4 Score method [ND], INV Not-found list | a | PL 8B/1B/11B/LG4 MODEL_CARD.md; HF cards; DOCS3 and DOCS4 (raw); CB notebook llama_guard_text_and_vision_inference.ipynb (output_scores sample); arXiv 2411.10414 and 2411.17713; Llama 3 paper arXiv 2407.21783 section on Llama Guard. Expect "not disclosed" to stand | H |
| T2 | What cut-off to use on the first-token probability on our data (precision/recall trade-off per version) | A LG1 R7 (threshold sweep bullet), A LG1 R8, A LG2 R8; INV(a) score-method cells | b | Run each version on a labelled set; sweep threshold; report PR curve. Cannot be answered from docs | H |
| T3 | Official latency / throughput figures for any version | A LG1 R4 [ND], A LG1 R8, A LG2 R4 [ND], A LG2 R8, INV Not-found list, INV(c) ExecuTorch row (caveat), INV(a) 3-1B-INT4 headline | a | arXiv 2411.17713 (abstract: at least 30 tokens/s on mobile; check body table for device and prompt length); PL 1B MODEL_CARD.md; Meta LG4 blog (ai.meta.com/blog/llamacon-llama-news/); HF cards. Expect none for 8B / 11B-V / LG4 | M |
| T4 | Measured latency and throughput on our hardware | A LG1 R7 (logger records latency), A LG2 R7 | b | Time inference per version at fixed prompt length; GPU/CPU stated | M |
| T5 | Context length of every variant (LG1, LG2, 3-1B, 3-1B-INT4, 3-8B, 3-8B-INT8, 3-11B-V, LG4) | INV(a) all 8 rows "model context length" [ND]; INV Not-found list; INV intro paragraph | a | HF config.json (gated: needs accepted licence + token), PL cards, base-model cards (Llama 2 / 3 / 3.1 / 3.2 / Llama 4 Scout on HF and llama.com docs), arXiv 2312.06674 (4096 fine-tune length) | M |
| T6 | LG4 language coverage conflict: card = English plus the 7 LG3 languages; DOCS4 = optimised for English with English text component; PROT = "12 languages" | A LG1 R6 (Detail bullets x3), A LG1 R8, A LG2 R6, A LG2 R8, B LG3 R3 (bullet), B LG3 R6, B LG3 R8, RN-A, RN-B, INV(a) LG4 Languages | a | PL LG4 MODEL_CARD.md; HF Llama-Guard-4-12B; DOCS4; PROT (read raw, not summarised); Meta LG4 blog post. Also check which 12 languages PROT means | H |
| T7 | 3-1B card evaluation table has Vietnamese and Indonesian columns outside the 8-language list; does 3-1B (and 3-1B-INT4) support them? | A LG1 R8, A LG2 R6, A LG2 R8, RN-A, RN-B, INV(a) 3-1B Languages, INV(a) 3-1B-INT4 Languages, INV-RN 5 | a | PL Llama-Guard3/1B/MODEL_CARD.md (table and supported-language list), HF Llama-Guard-3-1B, arXiv 2411.17713, DOCS3 | M |
| T8 | LG1 and LG2 supported languages [ND]; 3-11B-V wording "English only" (brief) vs "optimized for English" (card) | INV(a) LG1 Languages [ND], INV(a) LG2 Languages [ND], INV(a) 3-11B-V Languages, RN-A | a | PL Llama-Guard/MODEL_CARD.md, PL Llama-Guard2/MODEL_CARD.md, HF cards, DOCS2, PL 11B card | L |
| T9 | LG4 image tiling (336x336 tiles plus a global tile): not found in B, yet INV(a) LG4 Modality labels "dynamic 336x336 tiles" [Documented: DOCS4]. The two files disagree | B LG3 R4 [TBV], B LG3 R8, RN-B, INV(a) LG4 Modality | a | DOCS4 (raw text of the LG4 prompt-format section and image-token description); PL LG4 MODEL_CARD.md; HF Llama-Guard-4-12B preprocessor config (gated); Llama 4 model docs on llama.com | H |
| T10 | LG4 performance with more than about 3 images (card caveat); behaviour at 10+ images | B LG3 R4 (card quote), B LG3 R7 (10+ image set), B LG3 R8 | b | Multi-image test set (2 to 12 images) per brief R7; card gives no number beyond "tested mostly with three" | M |
| T11 | Full text of the LG4 DOCS4 "Complete Example" with multiple images (only a summary was returned) | B LG3 R8 | a | DOCS4 raw page; developer.meta.com/ai/docs mirror | M |
| T12 | "Response is text only; image output is not classified" and "S14 text only" premises | B LG3 R6 [INF], B LG4 R4 | a | PL 11B and LG4 MODEL_CARD.md; DOCS3, DOCS4 | L |
| T13 | Is custom category text (categories / excluded_category_keys via chat template) documented for LG4? (none found) | A LG1 R8, A LG2 R8, B LG5 R1 (Summary), B LG5 R4 (3-8B and LG4 HF pages bullet), B LG5 R8 (x2), INV(a) LG4 Custom categories [NF], INV(c) HF transformers row Categories configurable [NF] | a | HF Llama-Guard-4-12B (raw README / chat_template.json in repo), PL LG4 card, DOCS4 "customize" section, CB notebook (check for an LG4 cell) | H |
| T14 | Do the 3-8B and 3-8B-INT8 chat templates accept categories / excluded_category_keys? | B LG5 R4 [TBV], B LG5 R8, INV(a) 3-8B Custom categories [TBV], INV(a) 3-8B-INT8, INV(c) HF row [NF] | a | HF Llama-Guard-3-8B and -INT8 (raw README + tokenizer_config chat_template), PL 8B card, DOCS3 | H |
| T15 | Do categories / excluded_category_keys actually work (or error / are ignored) on 3-8B, 3-8B-INT8 and LG4 | B LG5 R7 (LG4 probe bullet), B LG5 R4 [TBV] | b | Run `apply_chat_template(..., categories=..., excluded_category_keys=...)` on each version; inspect rendered prompt and verdicts | H |
| T16 | Do custom category keys other than "S1" style work? | B LG5 R5 [TBV] | b | Try keys like C1, "ACCT" and numeric; check verdict parsing | M |
| T17 | Limits on number or length of custom categories [ND] | B LG5 R6 [ND] | b | Docs unlikely to state; probe category count and description length vs verdict quality. Quick doc check of DOCS3/DOCS4 first | L |
| T18 | Contents of the customization notebook (llama_guard_customization_via_prompting_and_fine_tuning.ipynb) and whether the linked llama-recipes path still exists | B LG5 R4 (3-1B card bullet), B LG5 R8 | a | CB tree getting-started/responsible_ai/llama_guard at 2f22a9eb (read notebook raw); PL 1B card link | M |
| T19 | Cookbook inference notebook only searched by pattern, not read in full: "does not load LG4"; Colab badge and 1B-card links use old paths | B LG5 R4 (notebook bullets), RN-B (last items), INV(c) cookbook notebooks row caveats | a | CB llama_guard_text_and_vision_inference.ipynb raw JSON; repo history for path move | L |
| T20 | Documented zero-shot / few-shot results for LG3 or LG4 (only LG1 paper reports them) | B LG5 R2 [INF], B LG5 R8 | a | arXiv 2411.10414, 2411.17713, Llama 3 paper (2407.21783), PL cards, DOCS3/DOCS4 | M |
| T21 | Zero-shot and few-shot custom-policy quality of current models on our taxonomy | B LG5 R7 (zero-shot / few-shot bullets), B LG5 R8 | b | Run names-only, with-description and 2 to 4 examples per category; measure per-category F1 | M |
| T22 | 3-1B-INT4 custom prompts feasible (.pte takes a prompt string) | INV(a) 3-1B-INT4 Custom categories [INF], INV(c) ExecuTorch row (Categories configurable [INF]) | b | Run INT4 .pte with an edited example-prompt.txt; PL ET_INSTRUCTIONS.md for prompt handling | L |
| T23 | How tool calls and tool outputs are serialised into the Llama Guard prompt; any tool role in the docs (summarised fetch only) | B LG4 R3 [ND] and bullet "Meta docs ... no mention of tool", B LG4 R6 [ND], B LG4 R6 [INF] (code as text in agent turn), B LG4 R8 (x2), B LG4 R1 Summary ("no general function-call validation format") | a | DOCS3 and DOCS4 raw text (search for tool, function, ipython roles); PL 8B card (tool-use sections); llama-models repo tool prompt docs; CB notebooks | H |
| T24 | Which tool-call serialisation (JSON function call, Tool label turn, fenced code) the classifier reacts to; S14 behaviour on image + code screenshot | B LG4 R7 (serialisation, screenshot bullets) | b | Run serialisation variants on 3-8B / LG4 / 3-1B; record S14 hit rate | M |
| T25 | LG4 evaluation on tool-use categories or S14 (card gives none); whether LG4 was evaluated on search tool calls; language of S14 evaluation | B LG4 R4 (LG4 card averages bullet), B LG4 R6 (S14 language), B LG4 R8 | a | PL LG4 MODEL_CARD.md; DOCS4; Meta LG4 blog | M |
| T26 | Does 3-8B-INT8 support S14 as documented (its card not read separately; rests on 8B Table 5 and HF intro summary) | B LG4 R1 (versions with S14 bullet), B LG4 R8, RN-B (last), INV(a) 3-8B-INT8 Taxonomy / S14 [SUM] | a | HF Llama-Guard-3-8B-INT8 raw README; PL 8B card Quantization section | M |
| T27 | Search tool calls have no dedicated category and "both prompt and agent output can be judged" are inferences | B LG4 R2 [INF], B LG4 R3 [INF] | a | PL 8B card (Evaluation tables and training-data notes), DOCS3 | M |
| T28 | OGX 1.0 /v1/moderations: release notes say it replaces the Safety API; 2026-06-23 blog says the standalone endpoint was removed (Responses `guardrails: true` uses external endpoint) | A LG1 R4 (OGX 1.0 bullet), A LG2 R4, INV(c) /v1/moderations row [TBV], INV(c) provider row ("removed in 1.0"), INV-RN 2 | a | OGX docs/releases/RELEASE_NOTES_1.0.md, docs/blog/2026-06-23-guardrails-responses-api.md, docs/docs/providers/responses/inline_builtin.mdx, main-branch API route listing (raw files) | H |
| T29 | Is OGX's S1-S13-only list for LG4 intentional (card lists S14)? | A LG1 R4 (bullet), A LG2 R4, B LG4 R4, B LG4 R8, RN-A, RN-B, INV(b) Code interpreter abuse, INV-RN 4 | a | OGX llama_guard.py @v0.4.4 git blame / PRs / issues; PL LG4 card; CB prompt_format_utils (14-entry list) | M |
| T30 | OGX "checks the last message only": code builds the prompt from the whole message list and asks about the last message. A LG1 R3/R4/LG2 R4 say last-message-only | A LG1 R3 (OGX bullet), A LG1 R4 (OGX bullet), A LG2 R4, B RN-B (item 5), INV(c) OGX provider row Input/Output, INV-RN 3 | a | OGX llama_guard.py @v0.4.4 (re-read raw; compare `run_shield` message handling); then fix wording in A to match | H |
| T31 | OGX role label: capitalised last-message role ("Assistant") vs documented `Agent` | A LG1 R4 (bullet), B LG4 R3 (bullet), RN-A | a | OGX llama_guard.py @v0.4.4; DOCS3 / DOCS4 role placeholder text | L |
| T32 | OGX moderation scores: safe result sets every category to 1.0, unsafe 1.0/0.0; brief said "0/1 only" | A LG1 R5 (bullet), B LG3 R5 (bullet), B LG4 R5 (bullet), RN-A, RN-B, INV(c) /v1/moderations row | a | OGX llama_guard.py @v0.4.4 `run_moderation` (raw); confirm it is a quirk not intent | L |
| T33 | How OGX moderation handles response-role classification after Safety API removal | A LG2 R8, A LG2 R3 (OGX bullet) | a | OGX v0.4.4 run_moderation vs main 1.0 docs; moderation provider docs | M |
| T34 | Does the HF repo id of 3-11B-V reach OGX's vision branch (core-model id string not read) | B LG3 R4 [INF], B LG3 R8 | a | OGX llama_guard.py @v0.4.4 and the model registry / `CoreModelId` definitions (llama_models mapping) | M |
| T35 | NeMo docs example model type: `llama_guard_2` (A LG1 R4 / LG2 R4, brief) vs `llama_guard` + LlamaGuard-7b (INV, raw docs at v0.24.1); live site may differ from tag | A LG1 R4 (NeMo bullet), A LG2 R4, RN-A (item on llama_guard_2), INV(c) NeMo row Caveats, INV-RN 8 | a | NEMO v0.24.1 docs/configure-rails/guardrail-catalog/community/llama-guard.mdx; live docs.nvidia.com page (content-safety and llama-guard pages); flows.co model_name; config model `type` key semantics | H |
| T36 | NeMo `policy_violations`: populated? violations split on space while model returns comma-separated (so `S1,S2` becomes one item); metadata "currently unused" in flow | INV(c) NeMo row Caveats [Documented: repo; effect INF], A LG1 R5 (NeMo bullet) | b | Read actions.py/flows.co again (a), but the effect needs a run with a real model reply on an unsafe case | M |
| T37 | ExecuTorch instructions: bare string passed to `apply_chat_template` (sample looks incomplete); download step points at llama-stack CLI reference | INV(c) ExecuTorch row Caveats [judgement INF] | a | PL Llama-Guard3/1B/ET_INSTRUCTIONS.md raw; torchchat / ExecuTorch repos docs | L |
| T38 | Llama API `/moderations`: request schema (messages array, model), response schema, category list; doc page 404; request shape from a search snippet | INV(c) Llama API row [TBV: snippet], INV(c) row [NF] x2, INV-RN (summarised caveats, Not-found list), A LG1 R4 (Llama API bullet, SUM) | a | llama.developer.meta.com API reference (moderations), dev.meta.ai/docs/api/*, PROT raw text | M |
| T39 | PGD response-classification at 8/255: A LG2 R2 says 6% to 27%; B LG3 R2 says 22% at 8/255 (27% at 128 and 255). Brief said 6 to 27 | A LG2 R2 (bullet), B LG3 R2 (sub-bullet), RN-B (first item) | a | arXiv 2411.10414 Table 3 (HTML /html/2411.10414 raw or PDF); fix A to match | H |
| T40 | Adversarial numbers all from summarised arXiv fetch: prompt 21% -> 70% / 82% / 82%; GCG prompt 4% -> 72%; response 16% -> 30% / 75% | A LG1 R2 (bullet), A LG2 R2 (bullets), B LG3 R2 (sub-bullets), RN-A, RN-B | a | arXiv 2411.10414 sections on adversarial robustness (raw HTML or PDF) | H |
| T41 | 3-1B-INT4 size: paper abstract 440 MB vs HF .pte listing 458 MB | INV(a) 3-1B-INT4 Distribution / Headline eval, INV-RN 7 | a | arXiv 2411.17713 (abstract and body; MB vs MiB, with or without embeddings), HF Llama-Guard-3-1B-INT4 file listing (raw), PL 1B card | H |
| T42 | LG2 headline numbers: own set F1 0.915 / AUPRC 0.974 / FPR 0.040 vs 0.877 / 0.927 / 0.081 on the LG3 English response set (different sets) | INV(a) LG2 Headline eval, INV-RN 6, A LG2 R5 (LG2 comparison in 8B bullet) | a | PL Llama-Guard2/MODEL_CARD.md; PL Llama-Guard3/8B card eval tables (confirm set description for each) | M |
| T43 | LG1 paper numbers (zero-shot AUPRC 0.847 vs OpenAI API 0.856, no adaptation 0.837, few-shot 0.872; 4096 sequence length; AUPRC 0.945 / 0.953 / 0.626; quotes on taxonomy adaptation) from summarised fetches | B LG5 R1 (quotes), B LG5 R4 (LG1 paper bullets), INV(a) LG1 Custom / Context / Headline eval, INV Summarised-fetch caveats | a | arXiv 2312.06674 (raw HTML /html/2312.06674 and PDF Table 4); PL Llama-Guard/MODEL_CARD.md | H |
| T44 | Prompt-only evaluation numbers for 3-1B and LG4 (cards do not label whether tables are prompt or response) | A LG1 R6 (bullet), A LG1 R8, RN-A (last) | a | PL 1B and LG4 MODEL_CARD.md evaluation text; HF cards; arXiv 2411.17713 | M |
| T45 | Comparable response-level numbers across LG4, 3-8B, 3-1B (and 11B-V) on one test set; cross-card F1 values are not comparable | A LG2 R5 [INF], A LG2 R8, A LG2 R7 | b | Run all versions on one labelled response set (same languages, S1-S13) | H |
| T46 | Llama 3 paper numbers cited by the LG3 card (trade-off statement) not checked | RN-A (trade-off bullet) | a | arXiv 2407.21783 (Llama 3 herd of models) safety section; PL 8B card citation | L |
| T47 | LG1 release date: arXiv 2023-12-07 vs HF fetch 2023-07-18 (Llama 2 date) | INV(a) LG1 Release date [TBV], INV-RN (summarised caveats) | a | HF LlamaGuard-7b repo commit history and model card; arXiv 2312.06674 submission date; Meta announcement 2023-12-07 (ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai) | M |
| T48 | Release dates for LG2, 3-1B, 3-1B-INT4, 3-8B, 3-8B-INT8, 3-11B-V, LG4 are licence "Version Release Date" lines only (and the LG4 licence date vs announcement) | INV(a) rows LG2, 3-1B, 3-1B-INT4, 3-8B, 3-8B-INT8, 3-11B-V, LG4 Release date; INV Not-found list | a | Meta launch posts (ai.meta.com/blog: Llama 3.1, 3.2, Llama 4 / LlamaCon), HF repo "created" dates, PL commit history, arXiv 2411.10414 / 2411.17713 dates | M |
| T49 | LlamaCon post date 2025-04-29 and wording from summarised fetch | INV(a) LG4 Release date [SUM] | a | https://ai.meta.com/blog/llamacon-llama-news/ raw text | L |
| T50 | LG1 O-code order: cookbook/paper (O3 Criminal Planning, O4 Guns, O5 Substances, O6 Self-Harm) vs brief and HF summary (O3 Guns, O4 Substances, O5 Suicide, O6 Criminal Planning); PL card has no codes | INV(a) LG1 Taxonomy, INV(b) intro paragraph and all LG1 code cells, INV(c) cookbook row (LG1 order), INV-RN 1 | a | CB prompt_format_utils.py LLAMA_GUARD_1_CATEGORY; arXiv 2312.06674 (Table of categories, raw HTML); HF LlamaGuard-7b README (gated, via token); PL Llama-Guard/MODEL_CARD.md | H |
| T51 | Meta docs say llama-models repo has no Llama Guard template (absence not checked directly) | A LG1 R4 [INF] | a | github.com/meta-llama/llama-models (search for "Guard", prompt format docs); DOCS3/DOCS4 | M |
| T52 | Meta docs pages (DOCS3, DOCS4, PROT) read only through a summarising fetch; every quote and fact depends on it: role rule, "not designed for image-only", generated-image exclusion, "one image per prompt", S14 definition and "1B not optimized for S14", "can be customized for zero-shot or few-shot", "optimized for English", PROT "/moderations" and "12 languages" | A RN-A, B RN-B, A LG1 R2/R3/R6, A LG2 R3, B LG3 R3, B LG4 R2/R3/R4, B LG5 R1, INV(a) 3-8B / 3-1B / LG4 rows, INV(c) HF row | a | Re-read DOCS3, DOCS4, PROT, DOCS2 raw (curl from a non-blocked host, or developer.meta.com mirror); verify each quote verbatim | H |
| T53 | Hugging Face card facts from summarised fetches: licence names and dates, usage code (AutoModelForCausalLM, Llama4ForConditionalGeneration, BitsAndBytesConfig), file listing (.pte, params.json), 3-1B custom-category snippets (not in PL 1B card), INT8 intro | A LG1 R4 (HF bullet), A LG2 R4 (HF bullet), B LG5 R4 (3-1B and 3-11B-V HF snippets, 3-8B/LG4 absence), RN-B (item on 1B card), INV(a) licence / distribution cells, INV(c) HF row, INV Summarised-fetch caveats | a | HF raw README of each repo (needs gated access with accepted licence + token), config/tokenizer_config chat_template; PL cards as mirror | H |
| T54 | Cookbook LG3 category list always has 14 categories including S14 even for 1B / 11B-V (cards: S1-S13) | INV(b) Code interpreter abuse, INV(c) cookbook row, INV-RN 9 | a | CB prompt_format_utils.py (raw) and later cookbook commits; PL 1B and 11B cards | L |
| T55 | Naming drift: "Sex-Related Crimes" (cards) vs "Sex Crimes" (docs, cookbook, OGX); "Suicide & Self-Harm" vs "Self-Harm"; "Child Sexual Exploitation" vs "Child Exploitation"; cookbook wording "according our" vs docs "according to our" | INV(b) rows 3, 4, 10, INV-RN 10, RN-B (wording item) | a | PL cards vs DOCS3 / DOCS4 vs CB prompt_format_utils.py; decide canonical names | L |
| T56 | Llama Guard on jailbreak or prompt-injection prompts (Meta points to Prompt Guard 2); behaviour not measured | A LG1 R8 (last bullet), A LG1 R2, A LG2 R2, B LG4 R2 | b | Out of scope except a one-line mention; test only if wanted. Doc side already covered by PL LG4 card and PROT | L |
| T57 | Licence names, versions and dates per variant (LG1 Llama 2 CLA, LG2 Meta Llama 3 CLA, 3-8B/INT8 Llama 3.1, 3-1B/INT4/11B-V Llama 3.2, LG4 Llama 4 Community License Agreement) | A LG1 R4 (licence bullets), A LG2 R4 (Licences bullet), INV(a) all Licence cells and release dates, INV(a) LG1 (cookbook header says "Llama 2 Community License Agreement") | c | HF repo LICENSE / USE_POLICY files for each model; llama.com/llama2/license, /llama3/license, /llama3_1/license, /llama3_2/license, /llama4/license; Acceptable Use Policies | H |
| T58 | (suggested) Llama 3.2 and Llama 4 licences carry a multimodal / vision-model restriction for EU-domiciled users or entities; does it apply to 3-11B-V and LG4 | not in drafts; relevant to B LG3 R4 (versions) and INV(a) 3-11B-V and LG4 rows | c | llama.com/llama3_2/license (Additional terms), llama.com/llama4/license, Llama 3.2 / 4 AUP; HF 11B-V and LG4 cards | M |
| T59 | (suggested) Redistribution and derivative terms for the quantised variants (INT8 via bitsandbytes, INT4 .pte): naming ("Llama" prefix) and attribution duties | not in drafts; relevant to INV(a) 3-8B-INT8 and 3-1B-INT4 rows | c | Applicable licence text (3.1 / 3.2) sections on derivative works and attribution | L |

## Label hygiene for 3d

Scope: `lg_inventory.md`. Allowed forms: [Documented], [Documented: repo <repo>@<ref>], [Documented: develop/unreleased], [Inferred], [To be verified], [Not disclosed]. Counts are occurrences of the exact bracket text in the whole file (tables and prose); `[INST]` (a NeMo prompt token), `[...]`, `[]` are not labels.

Standard forms in use (no change): [Documented] 20, [Not disclosed] 15, [Inferred] 9, [To be verified] 4, [Documented: repo ogx-ai/ogx@v0.4.4] 2, [Documented: repo meta-llama/llama-cookbook@2f22a9eb] 1, [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1] 1.

Non-standard forms (each is a distinct bracket text), with proposed normalisation. Source hints become plain text after the bracket, e.g. "[Documented] (PL 8B card)".

| Non-standard form | Count | Proposed normalised label |
|---|---|---|
| [Documented: repo] (bare) | 17 | [Documented: repo <repo>@<ref>], filling in the repo from the row (cookbook@2f22a9eb, ogx-ai/ogx@v0.4.4, NVIDIA-NeMo/Guardrails@v0.24.1) |
| [Documented: PL 1B card] | 9 | [Documented: repo PurpleLlama@172c1074] (1B card) |
| [Documented: PL card] | 8 | [Documented: repo PurpleLlama@172c1074] (card) |
| [Documented: PL 8B card] | 6 | [Documented: repo PurpleLlama@172c1074] (8B card) |
| [Documented: PL LG4 card] | 6 | [Documented: repo PurpleLlama@172c1074] (LG4 card) |
| [Documented: PL 11B card] | 5 | [Documented: repo PurpleLlama@172c1074] (11B card) |
| [Documented: PL ET_INSTRUCTIONS.md] | 3 | [Documented: repo PurpleLlama@172c1074] (ET_INSTRUCTIONS.md) |
| [Documented: PL] | 2 | [Documented: repo PurpleLlama@172c1074] |
| [Documented: PL Llama-Guard/MODEL_CARD.md] | 1 | [Documented: repo PurpleLlama@172c1074] |
| [Documented: PL 8B card, Quantization section] | 1 | [Documented: repo PurpleLlama@172c1074] (8B card, Quantization) |
| [Documented: PL 8B card Table 5] | 1 | [Documented: repo PurpleLlama@172c1074] (8B card Table 5) |
| [Documented: PL card and paper] | 1 | [Documented] (PL LG1 card and arXiv 2312.06674) |
| [Documented: PL LG4 card, dev.meta.ai protections page] | 1 | [Documented] (PL LG4 card; PROT) |
| [Documented: PL; judgement Inferred] | 1 | split: [Documented: repo PurpleLlama@172c1074] for the observed sample; [Inferred] for "looks incomplete" |
| [Documented: HF page] | 7 | [Documented] (HF page; summarised fetch, see T53) |
| [Documented: HF page, summarised] | 2 | [Documented] (HF page, summarised) |
| [Documented: HF licence date only] | 3 | [Documented] (HF licence "Version Release Date" only) |
| [Documented: HF "Meta Llama 3 Version Release Date", a licence date only] | 1 | [Documented] (HF, licence date only) |
| [Documented: HF "Llama 3.2 Version Release Date", a licence date only] | 1 | [Documented] (same) |
| [Documented: HF "Llama 3.1 Version Release Date", a licence date only] | 1 | [Documented] (same) |
| [Documented: HF "Llama 4 Community License Agreement" effective date] | 1 | [Documented] (HF licence effective date) |
| [Documented: HF intro, summarised] | 1 | [Documented] (HF intro, summarised) |
| [Documented: HF file listing, summarised] | 1 | [Documented] (HF file listing, summarised) |
| [Documented: HF cards] | 1 | [Documented] (HF cards) |
| [Documented: HF 1B card; cookbook notebook] | 2 | [Documented] (HF 1B card, summarised) or [Documented: repo llama-cookbook@2f22a9eb] (notebook); one label per fact, split if both |
| [Documented: HF page; cookbook file header says "Llama 2 Community License Agreement"] | 1 | [Documented] (HF page); mention the cookbook header in text |
| [Documented: dev.meta.ai LG3 page] | 5 | [Documented] (DOCS3, summarised) |
| [Documented: dev.meta.ai LG4 page] | 2 | [Documented] (DOCS4, summarised) |
| [Documented: dev.meta.ai LG2 page] | 1 | [Documented] (DOCS2) |
| [Documented: dev.meta.ai protections page, summarised] | 1 | [Documented] (PROT, summarised) |
| [Documented: protections page; LG4 card says "Llama Moderations API for text and images"] | 1 | [Documented] (PROT; LG4 card) |
| [Documented: dev.meta.ai LG3 page says prompt-only checks must not contain the agent reply; response checks need both] | 1 | [Documented] (DOCS3); move the sentence outside the bracket |
| [Documented: arXiv abs, summarised] | 3 | [Documented] (arXiv abstract, summarised) |
| [Documented: arXiv submission date, not a licence date] | 1 | [Documented] (arXiv submission date) |
| [Documented: arXiv paper, summarised fetch] | 1 | [Documented] (arXiv 2312.06674, summarised) |
| [Documented: arXiv html, summarised] | 1 | [Documented] (arXiv HTML, summarised) |
| [Documented: arXiv abstract] | 1 | [Documented] (arXiv abstract) |
| [Documented: ai.meta.com LlamaCon post, summarised] | 1 | [Documented] (ai.meta.com post, summarised) |
| [Documented: LG3-8B card] | 1 | [Documented] (LG3-8B card) |
| [Documented: LG2 card] | 1 | [Documented] (LG2 card) |
| [Documented: cookbook notebook] | 2 | [Documented: repo llama-cookbook@2f22a9eb] |
| [Documented: repo directory listing at 2f22a9eb] | 1 | [Documented: repo llama-cookbook@2f22a9eb] |
| [Documented: repo docs] | 2 | [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1] (docs mdx) |
| [Documented: repo blog] | 2 | [Documented: repo ogx-ai/ogx@main] (blog 2026-06-23); ref "main" must be pinned to a commit if possible |
| [Documented: repo ogx-ai/ogx main docs] | 1 | [Documented: repo ogx-ai/ogx@main] (pin to a commit) |
| [Documented: repo ogx-ai/ogx main, listing] | 1 | [Documented: repo ogx-ai/ogx@main] (pin to a commit) |
| [Documented: repo flows.co] | 1 | [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1] |
| [Documented: repo; effect Inferred] | 1 | split: [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1] for code; [Inferred] for the effect |
| [Documented, same 1B card] | 1 | [Documented: repo PurpleLlama@172c1074] (same 1B card) |
| [Not found] | 4 | [Not disclosed] (or [To be verified] if a source is still unread, e.g. T13 / T14 / T38) |
| [To be verified: search-result snippet only; the doc URL redirected to a 404] | 1 | [To be verified] (search snippet only; doc URL 404) |
| [To be verified against raw HF README, which is gated] | 1 | [To be verified] (against raw HF README, gated). Appears in Reviewer notes, not a table cell |

Total non-standard bracket occurrences: about 114 in 52 distinct forms (the Reviewer notes also contain 2 of the [To be verified ...] and [Documented ...] mentions as prose). Rule of thumb: every `[Documented: PL ...]` becomes `[Documented: repo PurpleLlama@172c1074]`; every `[Documented: dev.meta.ai ...]`, `[Documented: HF ...]`, `[Documented: arXiv ...]` becomes plain `[Documented]` with the source in parentheses after the bracket (the brief only allows the repo form to carry a ref).

Bold and backticks inside inventory table cells (need stripping before the sheet):
- Bold in cells: line 14 (3-1B-INT4 Distribution: `**Distinct official artifact.**`), line 31 (crosswalk Specialized advice: `**S6**`), line 50 (OGX provider Status: `**removed in 1.0**`), line 51 (OGX /v1/moderations Status: `**Contradictory, treat as [To be verified]**`; note this also embeds a label inside bold). Four cells. Line 62 (Self-check) quotes `**S6**` outside a table; line 67 to 76 Reviewer notes use `**...**` lead words, which are fine outside table cells.
- Backticks in cells: 13 to 18 (variant rows: `apply_chat_template(...)`, `llama_guard_3_1b_pruned_xnnpack.pte`, `BitsAndBytesConfig(load_in_8bit=True)`, `MllamaForConditionalGeneration`, `Llama4ForConditionalGeneration`, `AutoProcessor`, `categories=` / `excluded_category_keys=`), and all integration rows 47 to 55 (function, config and flag names). Roughly 15 table lines carry backticks; strip or keep as plain text per the sheet rules (code identifiers may be allowed in Detail but not in Summary-like cells).
- Other table-cell hazards: pipe-free (no stray `|` found inside cells); the long Source URL cells contain several URLs separated by ` ; `; non-ASCII "—" and "-" ranges "S1-S13" are fine; the LG1 release-date cell contains two dates plus two labels in one cell; the Not-found cells use [Not found] (see above).
- Also in A and B (not the inventory): bare `**[Documented: repo]**` appears in A LG1 R5 and A LG2 R5 (needs repo and ref), and B uses `**[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**` with an org prefix (acceptable but inconsistent with `[Documented: repo llama-cookbook@2f22a9eb]` used in A); B R7 uses `**Minimum setup:**` as the brief requires.

## Contradictions

Source conflicts and cross-file inconsistencies, each with the ids that resolve them.

1. LG2 headline F1 0.915 (own set; AUPRC 0.974, FPR 0.040, LG2 card) vs 0.877 (LG3-8B card English response set; AUPRC 0.927, FPR 0.081). Not a true conflict (different test sets); both appear and must be labelled with their set. INV(a) LG2, INV-RN 6; A LG2 R5 uses only 0.877. See T42.
2. OGX 1.0 `/v1/moderations`: 1.0 release notes say it replaces the Safety API; the 2026-06-23 blog says the standalone endpoint was removed, with Responses `guardrails: true` calling an external moderation endpoint. A LG1 R4 and LG2 R4 state "replaced" as Documented; INV(c) leaves it [To be verified]. See T28.
3. NeMo docs model type: A LG1 R4 / LG2 R4 and the brief say the docs example uses `llama_guard_2`; INV (raw v0.24.1 docs page) shows `llama_guard` with LlamaGuard-7b, and a live-site snippet showed `llama_guard_2` with Meta-Llama-Guard-2-8B. The flow hard-codes `llama_guard`. A and INV disagree on the same Documented claim. See T35.
4. LG1 O-code ordering: cookbook code and paper (summarised) = O3 Criminal Planning, O4 Guns, O5 Substances, O6 Self-Harm; brief and a summarised HF page = O3 Guns, O4 Substances, O5 Suicide, O6 Criminal Planning; PL LG1 card has no codes. INV uses the cookbook order. See T50.
5. 3-1B languages: 8-language list (EN, FR, DE, HI, IT, PT, ES, TH) vs card evaluation table with Vietnamese and Indonesian columns. See T7.
6. LG4 languages: card = English plus 7 LG3 languages; DOCS4 = English-optimised, text component English; PROT = 12 languages. INV(a) LG4 follows the card. See T6.
7. 3-1B-INT4 size: 440 MB (arXiv 2411.17713 abstract, summarised) vs 458 MB (HF .pte listing, summarised). See T41.
8. LG4 tile size: B LG3 R4 says 336x336 + global tile is not stated in any source read [To be verified]; INV(a) LG4 labels "dynamic 336x336 tiles" as [Documented: DOCS4]. See T9.
9. PGD response-classification at 8/255: A LG2 R2 (and brief) 6% to 27%; B LG3 R2 (arXiv Table 3, summarised) 22% at 8/255, 27% at 128/255 and 255/255. See T39.
10. OGX "last message only": A LG1 R3 / R4 and LG2 R4 vs B RN-B and INV(c) / INV-RN 3 (whole conversation in the prompt, only the role word and instruction refer to the last message; first user message dropped in one case). See T30.
11. OGX LG4 categories: code gives S1-S13 and comments "same categories as Llama Guard 3" citing the LG4 card, which lists S14 (text only). See T29.
12. OGX role label: "Assistant" (capitalised last-message role) vs documented `Agent`. See T31.
13. OGX moderation scores: brief "0/1 only"; code sets every category to 1.0 when safe. See T32.
14. Cookbook LG3 list always includes S14, but 3-1B and 3-11B-V cards list S1-S13 only. See T54.
15. 3-1B custom-category snippet: brief says the 3-1B card documents it; the PL 1B MODEL_CARD.md does not show it (it links a notebook); the snippet comes from a summarised HF fetch. See T53, T13.
16. INT8 S14: B LG4 R1 says "same taxonomy per its card family" (from the 8B card); INV(a) 3-8B-INT8 says S1-S14 from a summarised HF intro. Own card not read. See T26.
17. 11B-V language: brief "English only" vs card "optimized for English". See T8.
18. LG1 release date: arXiv 2023-12-07 vs HF fetch 2023-07-18 (Llama 2 date). See T47.
19. Naming drift across cards, docs and cookbook ("Sex-Related Crimes" / "Sex Crimes"; "Suicide & Self-Harm" / "Self-Harm"; "Child Sexual Exploitation" / "Child Exploitation"; "according our" / "according to our"). See T55.
20. Cross-card F1 (LG3-8B about 0.94 vs LG4 about 0.61) is not comparable (different in-house sets); LG2 on the LG3 card vs its own card (item 1). See T45, T42.
21. Llama API /moderations: PROT claims availability for LG4; the API doc page returned 404, so request and response shape are unverified. See T38.
22. NeMo violations parsing: model returns comma-separated codes, NeMo splits on spaces; effect only inferred. See T36.
23. A LG1 R5 labels "LG3-1B and LG4 cards give no threshold ... absence in fetched text" as [Documented]; absence claims from summarised fetches are not documentation. See T1, T52.
