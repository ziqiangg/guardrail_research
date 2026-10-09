# Llama Guard workbook: fresh verifier review

Date of checks: 2026-10-08. Inputs read: lg_brief.md, lg_cols_a.md, lg_cols_b.md, lg_inventory.md, lg_two_level.md, lg_inventory_final.md, lg_changes.md (full), lg_resolutions_1.md and lg_resolutions_2.md (targeted entries T8, T9, T26-T30, T34, T35, T51). No file other than this one was modified.

## Verdict: PASS WITH FIXES

The merge is faithful. All 18 source spot-checks match, no leftover of the known wrong texts was found, every substantive change that I could diff is in lg_changes.md, and all structural and style rules hold mechanically. There are 9 required fixes: 5 are Summary entailment or staleness problems (including the LG3 R4 OGX question), 1 is a label-purity problem, 1 is an inventory/column coverage mismatch, 1 is an unsupported inventory coverage value, and 1 is a non-standard label form. None changes a fact.

## Required fixes

1. **LG3 R4 Summary (stale current-state claim).** The Summary says "the OGX moderation endpoint ignores images". That was true only at v0.4.4. OGX 1.0 removed the moderation route and the shield (release notes and 2026-06-23 blog, verified), and the LG3 R4 Detail has no bullet saying so. A reader of the Summary alone would believe a live OGX endpoint exists. Yes, it is misleading as written (lg_changes.md section 4 item 15 knowingly kept it).
   - Replace Summary with: `**Fine-tuned vision-language model.** Version 3-11B-Vision takes one image rescaled into four 560 by 560 chunks; Llama Guard 4 is a 12B early-fusion model that accepts several images. Serving via transformers; the OGX v0.4.4 moderation path ignored images and was removed in OGX 1.0. **[Documented]**` (43 words)
   - Add after the OGX shield-path bullets (after the bullet ending "takes the text path, where an image becomes an image placeholder string"): `• OGX 1.0 (May 2026) removed the Safety API and the Llama Guard provider, so the moderation path with its image TODO no longer exists on main (release notes and 2026-06-23 blog) **[Documented: repo ogx-ai/ogx@f8051dd6]**`
   - Add to LG3 R9: `• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/releases/RELEASE_NOTES_1.0.md` and `• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/blog/2026-06-23-guardrails-responses-api.md`. The LG3 R9 Summary can stay.

2. **LG3 R7, last Detail bullet (test cannot be run on current OGX).** Replace with: `• OGX check (v0.4.4 only; the moderation route and shields were removed in OGX 1.0): send an image-bearing message through the moderation endpoint and confirm the image is ignored; register the shield with the core id and with the HF id and compare **[Inferred]**`

3. **LG3 R5, OGX bullet (inference inside a [Documented] bullet).** The bullet ends "...sets every category score to 1.0, probably a quirk **[Documented: repo ogx-ai/ogx@v0.4.4]**". The inventory already splits this fact; the column does not. Replace with two bullets:
   - `• OGX v0.4.4 moderation: category scores are only 0.0 or 1.0 and the safe object sets every category score to 1.0 **[Documented: repo ogx-ai/ogx@v0.4.4]**`
   - `• The all-1.0 scores on a safe result are probably a quirk of the code **[Inferred]**`

4. **LG4 R5 Summary (not entailed by its Detail).** "No numeric score is returned by the model itself" appears in no R5 Detail bullet (R5 Detail covers output lines and OGX only). Replace Summary with: `**Safe or unsafe with S14 code.** An unsafe verdict lists S14 on the second line, with other codes when applicable. The model returns text only; the 3-8B card derives a score from the first-token probability. **[Documented]**` and add the Detail bullet: `• 3-8B card: the first-token probability is used as the unsafe-class probability, then thresholded (see R4) **[Documented]**`

5. **LG1 R5 Summary and LG2 R5 Summary (over-generalise the score method).** Both say a score "is the first-token probability" for the whole family, but LG1 R5 Detail says no score method appears for 3-1B, INT4, 11B-Vision and LG4 ([Not disclosed]); only LG3-8B, 3-8B-INT8 and LG2 describe it.
   - LG1 R5 Summary: `**Verdict text, optionally a score.** First line is safe or unsafe; if unsafe a second line lists comma-separated S-codes. LG3-8B and its INT8 card derive a score from the first-token probability, with no stated threshold; LG3-1B, 11B-Vision and LG4 describe none. **[Documented]**` (41 words)
   - LG2 R5 Summary: `**Verdict text for the response.** First line safe or unsafe; if unsafe, a second line lists S-codes. The LG3-8B and LG2 cards describe a first-token-probability score; only LG2 gives a threshold (0.5). **[Documented]**`

6. **LG1 R4 Summary and LG2 R4 Summary (stale or unconfirmed serving options).**
   - LG1 R4 Summary ends "with INT8, INT4 and Llama API options". The Detail says Llama API doc pages now 404 and availability is [To be verified] (lg_changes section 4 item 6 kept it on purpose). Replace the last sentence with: `Served through Hugging Face transformers, with INT8 and INT4 variants.` (Llama API stays in Detail with its caveat.)
   - LG2 R4 Summary ends "...cookbook helper, OGX and NeMo." OGX was removed in 1.0 (Detail bullet says so). Replace the last sentence with: `Serving via Hugging Face transformers, INT8 or INT4, cookbook helper, OGX (to v0.4.4) and NeMo.`

7. **INT4 coverage versus column text (inventory 5 check).** Inventory (a) says LG3-1B-INT4 is covered by the Input-level and Output-level columns, but LG1 R1 "Versions covered" and LG2 R1 "Versions covered" omit INT4 (only LG1 R4 and LG2 R4 mention it).
   - LG1 R1: change the bullet to `• Versions covered: LG4 (12B), LG3-1B, LG3-1B-INT4 (mobile), LG3-8B, LG3-8B-INT8, and LG3-11B-Vision for multimodal prompts **[Documented]**`
   - LG2 R1: change the bullet to `• Versions covered: LG4 (12B), LG3-1B, LG3-1B-INT4 (mobile), LG3-8B, LG3-8B-INT8, LG3-11B-Vision (multimodal prompt plus text response) **[Documented]**`

8. **Inventory (a), Llama-Guard-3-8B-INT8 "Custom categories documented" cell.** It lists "Custom-policy classification" as covered but the cell gives no customisation route (only "same fixed template"). Decision on the 3-8B and INT8 question: keep Custom-policy coverage for both. Reason: the column is about prompt-level policy text, the LG5 column documents the 3-8B route (cookbook builder with policy text, and the customisation notebook uses 3-8B), and the INT8 card has the same prompt format. Only the "chat-template categories argument" is absent, and LG5 R4 and R7 say so. For INT8 the route is an inference, so append to the cell: `Custom text only through the cookbook builder, using the same prompt format as 3-8B [Inferred]`.

9. **Non-standard label in inventory (c), NeMo row, Caveats cell: `[Documented: develop/unreleased]`.** This is not one of the allowed forms. Replace with `[Documented: repo NVIDIA-NeMo/Guardrails@9f793de5]` (develop commit named in lg_changes.md section 3, row "NeMo, Versions, I/O...") and keep the words "develop, unreleased" in the plain text before the label.

## Optional suggestions

- LG4 R3 Summary is labelled [Documented] but draws on a [Not disclosed] fact ("the cards give no separate tool-call input"). Either label **[Documented]** stays (acceptable) or reword to "...the cards define no separate tool-call input" to signal the negative.
- LG2 R3 Summary says the check runs "before the answer is shown"; no Detail bullet states this (closest: LG4 card output filtering "censors only unsafe final output"). Suggest "Model response, with the user prompt as context."
- LG4 R4 bullet "Score: ... no threshold given **[Documented]**": the absence part is really [Not disclosed]; split or drop "no threshold given".
- LG5 R4 bullet "chat templates (tokenizer config, read through the Hugging Face metadata API)": for LG4 the template is in the `chat_template_jinja` field of the API config, not tokenizer_config (3-1B and 3-8B use tokenizer_config). Change to "(chat template field, read through the Hugging Face metadata API)".
- LG4 R7 OGX bullet and LG5 R7 OGX bullet: add "(v0.4.4 only)" as in fix 2.
- LG1 R5 says NeMo returns "an allowed/blocked outcome"; LG2 R5 says "an allowed flag". Harmonise to the same wording.
- OGX 1.0 release notes literally say "Content moderation is now served by the OpenAI-compatible /v1/moderations endpoint". The merged text paraphrases this as "moves to". Consider quoting the release-notes sentence once (LG1 R4) next to the blog's "standalone /v1/moderations endpoint ... has been removed" so a reader sees why both are true.
- LG3 R9 keeps both arxiv.org/abs and arxiv.org/html for 2411.10414; other columns use HTML only. Optional dedupe.
- Labels `[Documented: repo PurpleLlama@172c1074]` omit the org prefix while cookbook and OGX labels include it. Consistent with the brief's allowed forms, but harmonising to `meta-llama/PurpleLlama@172c1074` would be cleaner.

## 1. Unlogged differences (Check 1)

Method: Python, columns parsed into (column, row) lines; bullets normalised (labels, parenthetical source hints, case) and matched with difflib; a second pass compared labels and parenthetical content of matched bullets; inventory cells compared the same way (31 rows, all keys present in both versions).

- Column rows: 45 Summaries and all Detail bullets compared. Every added, removed or reworded bullet maps to an entry in lg_changes.md sections 1 and 2 (row-by-row, including the "identical rows" list, which I confirmed: LG1 R7, LG2 R7, LG3 R1, LG4 R5, LG5 R3, R5, R6 have no text change). Counts of R9 URLs in the log (28, 22, 12, 9, 14) match the file.
- No bullet changed label strength without a log entry. The only strength changes are the logged ones: LG4 R2 and LG4 R3 Inferred to Documented (T27, evidence checked in lg_resolutions_1), LG3 R4 OGX HF-id Inferred to Documented (T34), LG1 R4 llama-models Inferred to Documented (T51), "uncensored" to "non-safety-tuned" (log section 4 item 12, card wording confirmed at source).
- Minor wording changes not itemised in the log (cosmetic, no fact change; no action needed unless the log must be exhaustive):
  1. LG1 R5, NeMo bullet: "allowed flag" became "allowed/blocked outcome".
  2. LG4 R4, cookbook bullet: added "for every Llama Guard 3 model, including 3-1B and 3-11B-Vision" (supported by the crosswalk row and T54, but not named in the log row).
  3. LG1 R2 first bullet and LG2 R2, LG3 R2, LG5 R4 bullets: source hints such as "(arXiv 2411.10414)" added or moved (covered by the global hint rule).
  4. LG1 R8, LG3 R8, LG4 R8 bullets: short parentheticals ("needs testing", "checked ...") added; covered by the R8 entries for T1, T6, T7, T24.
- Inventory: all cells with substantive changes are covered by log section 3 (Release date, Base/size, Languages, Taxonomy, Custom, Score, Licence, Distribution, Headline eval, crosswalk Notes and Source, integration rows). Unlisted but trivial: label and hint normalisation in Score method cells of 3-8B, 3-1B and LG4 (quote marks removed, "(checked ...)" added).

Result: no substantive unlogged change.

## 2. Sourcing and label strength (Check 2)

- Every upgrade to [Documented] traces to a resolution entry with URL and verbatim quote (T9, T13, T14, T26, T27, T28, T30, T34, T35, T51, T52, T53 checked in lg_resolutions_1 and lg_resolutions_2) or to the original draft.
- Leftover scan over lg_two_level.md and lg_inventory_final.md for: "6% to 27%", "English only", "last message only", "checks the last", "tile size ... not stated", "not found", "[Not found]", "serves /v1/moderations", "uncensored", "summaris", "Reviewer notes". No hits.
  - PGD response at 8/255 is 22% everywhere (LG2 R2, LG3 R2); 21% to 70% for prompts.
  - 11B-V languages are "optimised for English, not stated as English-only".
  - OGX is "whole conversation in the prompt, instruction asks about the last message" in every place (LG1 R3, R4, LG2 R4, inventory).
  - LG4 336x336 tiles plus global tile are [Documented] (LG3 R4); LG4 custom categories are documented as read by the chat template (LG5, LG1 R8, LG2 R8, inventory).
  - OGX 1.0 is stated as removed, with the release-notes sentence and blog both reflected.
  - NeMo: the llama guard flows hard-code `llama_guard`; `llama_guard_2` is only on the content-safety page.
  - Latency: the INT4 phone figure is [Documented]; "no official figure" is limited to the other versions.
- Inferences labelled [Documented]: one found (fix 3). Weak spots left as optional: the LG4 R4 "no threshold given" bullet; the "Tool: <content>" claim in LG4 R3 is derived from `m.role.capitalize()` in code (acceptable as a code fact).
- Contradictions with the resolutions: none found.

## 3. Summary entailment and style (Check 3)

Mechanical (all 45 Summaries): bold lead present on R1 to R7; R8 starts "**Key open questions.**" with no label; R9 is a plain line with no bold and no label; no backtick, underscore or dollar sign in any Summary; word counts all within limits (max 43 for R7, max 42 for others, R9 lines 13 to 29); every non-R8/R9 Summary ends with a single bold label. Detail: every bullet in R1 to R7 ends with a bold label; no bullet in R8 or R9 has a label; no stray bold elsewhere (besides the "Minimum setup" lead).

Entailment findings: fixes 1, 4, 5, 6 above. LG3 R4 judgement: yes, the OGX clause is misleading as a current-state Summary; replacement text is in fix 1 (past tense, version-pinned, with the removal in Detail). All other Summaries are supported by their own Detail bullets and their labels match.

## 4. Spot-checks at source (Check 4)

Fetched with curl (github.com blob pages with ?plain=1, Hugging Face public API, arxiv.org/html, dev.meta.ai); WebFetch not needed.

| # | Fact checked (where in workbook) | Source URL | Verbatim or table text seen | Verdict |
|---|---|---|---|---|
| 1 | LG4 evaluation table (LG3 R5, LG2 R5) | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md | English 69% / 11% / 61% (deltas 4%, -3%, 8%); Multilingual 43% / 3% / 51%; Single-image 41% / 9% / 38% (+10%, 0%, +8%); Multi-image 61% / 9% / 52% (+20%, -1%, +17%); "Values are from output filtering"; "average over samples from safety categories S1 through S13"; "only the final image was input into Llama Guard 3-11B-vision" | MATCH |
| 2 | 11B-V eval (LG3 R5, LG1 R6) | .../Llama-Guard3/11B-vision/MODEL_CARD.md at 172c1074 | Prompt 0.891 / 0.623 / 0.733 / 0.052; Response 0.961 / 0.916 / 0.938 / 0.016; GPT-4o 0.544/0.843/0.661/0.485 and 0.579/0.788/0.667/0.243; GPT-4o mini 0.488/0.943/0.643/0.681 and 0.526/0.820/0.641/0.313; category extremes 0.698 and 0.995 present | MATCH |
| 3 | LG3-8B tool-use numbers (LG2 R2, LG4 R4, LG1 R6) | .../Llama-Guard3/8B/MODEL_CARD.md at 172c1074 | Table 3: LG3 search 0.856 / 0.938 / 0.174, code interpreter 0.885 / 0.967 / 0.125; LG2 0.749/0.794/0.284 and 0.683/0.677/0.670; GPT4 0.732/N/A/0.525. Table 5 Tool Use: prompt 0.920 (FPR 0.126) vs INT8 0.909 (0.134); response 0.825 (0.176) vs 0.827 (0.155). Prompt English P 0.952 R 0.943 F1 0.947 FPR 0.057 | MATCH |
| 4 | PGD and GCG numbers (LG1 R2, LG2 R2, LG3 R2) | https://arxiv.org/html/2411.10414 | Table 3: prompt 21% (0/255), 70% (8/255), 82%, 82%; response 6%, 22% (8/255), 27%, 27%. Table 4: GCG prompt 4% to 72%; response 16% to 30% (user prompt) and 75% (agent response). Text: "PGD ... evaluated on 100 harmful conversations"; GCG "another set of 100 text-only unsafe conversations"; "The adversary has full white-box access"; "optimize the attacks with knowledge of the unsafe generation" | MATCH |
| 5 | LG4 336x336 tiles (LG3 R4) | https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/ | "divides the input image into 336x336 pixel tiles. Additionally, a global tile (created by resizing the entire input image to 336x336 pixels) is appended after the local tiles"; also "drop-in replacement for Llama Guard 3 8B and 11B"; "optimized for English-language text"; no occurrence of "tool" | MATCH |
| 6 | 3-8B chat template ignores categories (LG5 R4, inventory) | https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B (config.tokenizer_config.chat_template) | Template hard-codes S1 to S14 text, role set by message-count parity, raises on non-alternating roles; contains no `categories` or `excluded_category_keys` variable. 3-8B-INT8 template is the same length (1412 characters) and text. 3-1B template has `for key in categories ... if key not in excluded_category_keys`. LG4 template (field chat_template_jinja) has `categories is not defined`, S1-S13 branch when an image is present, same for-loop | MATCH |
| 7 | OGX v0.4.4 llama_guard.py whole-conversation prompt (LG1 R3, LG2 R4) | https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py | `conversations_str = "\n\n".join([f"{m.role.capitalize()}: ..." for m in messages])`; template line "Provide your safety assessment for ONLY THE LAST $agent_type message"; `messages = messages[1:]` when first two are user; `temperature=0.0`; CANNED_RESPONSE_TEXT "I can't answer that. Can I help with something else?"; "TODO: Add Image based support for OpenAI Moderations"; "Llama Guard 4 uses the same categories as Llama Guard 3" mapped to the S1-S13 list | MATCH |
| 8 | NeMo v0.24.1 flows hard-code model name (LG1 R4, LG2 R4) | https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/flows.co | `LlamaGuardCheckInputAction(model_name="llama_guard")` and `LlamaGuardCheckOutputAction(model_name="llama_guard")` | MATCH |
| 9 | NeMo docs model types (LG1 R4, LG2 R4) | .../docs/configure-rails/guardrail-catalog/community/llama-guard.mdx and .../content-safety.mdx at v0.24.1 | llama-guard.mdx: "Add a model of type `llama_guard`" with `meta-llama/LlamaGuard-7b`; content-safety.mdx: `type: llama_guard_2`, `model: meta-llama/Meta-Llama-Guard-2-8B` | MATCH |
| 10 | Licence titles (inventory (a)) | https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE, .../llama3_2/LICENSE, .../llama4/LICENSE (HF LICENSE files are gated, 401) | "LLAMA 3.1 COMMUNITY LICENSE AGREEMENT" (July 23, 2024); "LLAMA 3.2 COMMUNITY LICENSE AGREEMENT" (September 25, 2024); "LLAMA 4 COMMUNITY LICENSE AGREEMENT" (April 5, 2025). Titles and dates match the inventory cells; the HF-hosted copies themselves could not be read | MATCH (via the official llama-models copies) |
| 11 | Crosswalk code mapping LG2 S5 to LG3 S6, and LG2 omissions (inventory (b)) | .../Llama-Guard2/MODEL_CARD.md and .../Llama-Guard3/8B/MODEL_CARD.md at 172c1074 | LG2: "S5: Specialized Advice", "S6: Privacy", ... "S11: Sexual Content"; "The Election and Defamation categories are not addressed by Llama Guard 2". LG3-8B: "S5: Defamation", "S6: Specialized Advice" | MATCH |
| 12 | OGX 1.0 removal (LG1 R4, LG2 R3 and R4, inventory (c)) | https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/releases/RELEASE_NOTES_1.0.md and .../docs/blog/2026-06-23-guardrails-responses-api.md | Release notes: "The standalone Safety API has been removed. Content moderation is now served by the OpenAI-compatible `/v1/moderations` endpoint." Blog: "seven safety providers (Llama Guard, ...), and a standalone `/v1/moderations` proxy endpoint ... All of that has been removed"; "URL of any OpenAI-compatible `/v1/moderations` endpoint". The "no route exists on main" tree/grep result in T28 was not independently re-run | MATCH (route-absence on main: UNVERIFIABLE by me, but the blog statement supports it) |
| 13 | INT4 speed figure (LG1 R4, LG2 R4, inventory) | https://arxiv.org/html/2411.17713 | "throughput of at least 30 tokens per second and a time-to-first-token of 2.5 seconds or less on a commodity Android mobile CPU"; body: "deployed the model to a Moto-Razor phone and observed >= 30 token/s and <=2.5s time-to-first-token"; "(440MB)" | MATCH |
| 14 | LG1 paper adaptability and Table 2 note (LG5 R4, inventory LG1) | https://arxiv.org/html/2312.06674 | Table 4: OpenAI Mod API 0.856, no adaptation 0.837, zero-shot (w/ OpenAI Mod categories) 0.847, few-shot 0.872; Table 2 AUPRC 0.945 / 0.847 / 0.626 / 0.953; "The reported Llama Guard results are with zero-shot prompting using the target taxonomy"; "We set every threshold to 0.5"; "sequence length of 4096" | MATCH |
| 15 | Llama 3 paper violation reduction (LG1 R2) | https://arxiv.org/html/2407.21783 | "-65% violations on average across our benchmarks ... comes at the cost of increased refusals to benign prompts" | MATCH |
| 16 | Protections page: 12 languages, /moderations (LG1 R4, R6) | https://dev.meta.ai/llama/llama-protections/ | "It supports 12 languages ..."; "Llama Guard 4 is now available through the /moderations endpoint in Llama API" | MATCH |
| 17 | 3-1B not optimised for S14; one image per prompt (LG4 R4, LG3 R3) | https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/ | "The new Llama Guard 3 1B model was not optimized for category S14 Code Interpreter Abuse. If you need to screen for this category, you should use the 8B model"; "the model evaluates only one image per prompt"; the page has no occurrence of "tool" | MATCH |
| 18 | HF metadata: 11B-V EU-disallowed flag, creation dates, language tag (inventory (a), LG3 R4) | https://huggingface.co/api/models/meta-llama/Llama-Guard-3-11B-Vision, .../Llama-Guard-4-12B, .../Llama-Guard-3-8B, ...-INT8, ...-1B | 11B-V JSON contains `extra_gated_eu_disallowed`; LG4 and 1B JSON do not; createdAt 2024-09-20 (11B-V, 1B), 2024-07-22 (8B), 2024-07-21 (INT8), 2025-04-23 (LG4); 11B-V tags en, de, fr, it, pt, hi, es, th; LG4 architectures Llama4ForConditionalGeneration | MATCH |

Tally: 18 checked, 18 MATCH, 0 MISMATCH, 0 UNVERIFIABLE at claim level (two sub-facts noted in rows 10 and 12 could not be read directly, the substance is supported by official copies). Also confirmed during these reads: LG1 R3 NeMo "sends only the user message" and the HF Hub field naming nit (optional suggestion 4).

## 5. Inventory consistency (Check 5)

- Variant rows: 8 (LG1, LG2, 3-1B, 3-1B-INT4, 3-8B, 3-8B-INT8, 3-11B-Vision, LG4), each with 16 cells. Pass.
- Crosswalk: 14 rows; LG3/LG4 codes S1 to S14 each once (14 distinct); LG2 codes S1 to S11 (11 distinct); LG1 codes O1 to O6 (6 distinct). Pass.
- Integration paths: 9 rows (matches the log), 9 cells each.
- Coverage values: every value, split on ";", is exactly one of the five headers (verified by string comparison against the headers in lg_two_level.md) or "— (legacy, not in Table 3)". LG1 and LG2 carry only the legacy value. Pass.
- Coverage versus column content:
  - 3-1B: Input, Output, Custom; not Code/tool-use, not Multimodal. Consistent (docs say not optimised for S14; LG4 R4).
  - 3-1B-INT4: Input, Output; no Custom. Consistent with the cell "not documented for INT4". Column text omits INT4 in the R1 version lists: required fix 7.
  - 3-8B and 3-8B-INT8: Input, Output, Code/tool-use, Custom. Code/tool-use consistent (own cards list 14 categories). Custom-policy: decision recorded in fix 8: keep for both, add the route to the INT8 cell; the template-ignores-categories finding (T13 and T14, verified in spot-check 6) is stated in LG5 R4, R7 and in the 3-8B cell, so coverage is justified through the cookbook builder rather than the chat template.
  - 3-11B-Vision: Input, Output, Multimodal, Custom; no Code/tool-use. Consistent (S1 to S13 only; template reads categories).
  - LG4: all five. Consistent with LG1 to LG5 content (multimodal, S14 text only, template reads categories though no Meta snippet shows it).
- No "**" and no backticks anywhere in lg_inventory_final.md. No stray "|": every table row has the expected number of separators (16, 7 and 9 cells per row type).
- Labels: only [Documented], [Documented: repo <repo>@<ref>] (PurpleLlama@172c1074, meta-llama/llama-cookbook@2f22a9eb, ogx-ai/ogx@v0.4.4, ogx-ai/ogx@f8051dd6, NVIDIA-NeMo/Guardrails@v0.24.1), [Inferred], [Not disclosed], [To be verified]; one non-allowed form, `[Documented: develop/unreleased]` (fix 9). In lg_two_level.md all labels are allowed forms (plus meta-llama/llama-models@0e0b8c51).

## Appendix: URLs (R9 bullets of all five columns plus lg_inventory_final.md, deduplicated)

139 occurrences, 54 distinct. All are well-formed (scheme, host, no spaces, no trailing punctuation, only legal characters); every R9 bullet is a bare URL. Format check only for items I did not fetch; the ones I fetched in the spot-checks returned content (except gated HF repos, which return 401 as expected).

```
http://web.archive.org/web/20250914135559/https://llama.developer.meta.com/docs/features/moderation
http://web.archive.org/web/20250914152244/https://llama.developer.meta.com/docs/api/moderations
https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/
https://ai.meta.com/blog/llamacon-llama-news/
https://ai.meta.com/blog/meta-llama-3-1/
https://ai.meta.com/blog/meta-llama-3/
https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/
https://api.llama.com/v1/moderations
https://arxiv.org/abs/2312.06674
https://arxiv.org/abs/2411.10414
https://arxiv.org/abs/2411.17713
https://arxiv.org/html/2312.06674
https://arxiv.org/html/2407.21783
https://arxiv.org/html/2411.10414
https://arxiv.org/html/2411.17713
https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/meta-llama-guard-2/
https://dev.meta.ai/llama/llama-protections/
https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/community/llama-guard.mdx
https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/content-safety.mdx
https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/actions.py
https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/flows.co
https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard/MODEL_CARD.md
https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard2/MODEL_CARD.md
https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/11B-vision/MODEL_CARD.md
https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/ET_INSTRUCTIONS.md
https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/8B/MODEL_CARD.md
https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/getting-started/responsible_ai/llama_guard/llama_guard_customization_via_prompting_and_fine_tuning.ipynb
https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/getting-started/responsible_ai/llama_guard/llama_guard_text_and_vision_inference.ipynb
https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/src/llama_cookbook/inference/prompt_format_utils.py
https://github.com/meta-llama/llama-cookbook/tree/2f22a9eb030f92d0e99227e57e9a1123af1f9532/getting-started/responsible_ai/llama_guard
https://github.com/meta-llama/llama-models/blob/0e0b8c519242d5833d8c11bffc1232b77ad7f301/models/sku_list.py
https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/blog/2026-06-23-guardrails-responses-api.md
https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/docs/providers/responses/inline_builtin.mdx
https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/releases/RELEASE_NOTES_1.0.md
https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/models/llama/sku_list.py
https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/models/llama/sku_types.py
https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py
https://huggingface.co/api/models/meta-llama/Llama-Guard-3-11B-Vision
https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B
https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B-INT8
https://huggingface.co/api/models/meta-llama/Llama-Guard-4-12B
https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
https://huggingface.co/meta-llama/Llama-Guard-3-1B
https://huggingface.co/meta-llama/Llama-Guard-3-1B-INT4
https://huggingface.co/meta-llama/Llama-Guard-3-8B
https://huggingface.co/meta-llama/Llama-Guard-3-8B-INT8
https://huggingface.co/meta-llama/Llama-Guard-4-12B
https://huggingface.co/meta-llama/LlamaGuard-7b
https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B
https://www.llama.com/llama4/use-policy/
```

Notes on the appendix: the 3-1B HF Hub API URL is used as a source in the LG5 text ("chat templates ... read through the Hugging Face metadata API") but only the 3-8B, 3-8B-INT8, LG4 and 11B-Vision API URLs are in R9 lists; the 3-1B template was read at https://huggingface.co/api/models/meta-llama/Llama-Guard-3-1B, so consider adding that URL to LG5 R9. The api.llama.com URL in the inventory is an endpoint description, not a source link.
