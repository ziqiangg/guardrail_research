# Llama Guard merge: change log

Inputs merged: lg_brief.md, lg_cols_a.md (LG1, LG2), lg_cols_b.md (LG3 to LG5), lg_inventory.md, lg_triage.md, lg_resolutions_1.md (agent 1, 29 items), lg_resolutions_2.md (agent 2, 18 items). Outputs: lg_two_level.md, lg_inventory_final.md, lg_changes.md (this file). No source file was modified. No new research was done; every added fact is in a resolution file.

Format of the entries below: location | before (short) | after (short) | reason.

## 1. Global changes (apply to every column)

| Scope | Before | After | Reason |
|---|---|---|---|
| All Detail bullets with a trailing source hint | label first, then hint in parentheses, e.g. "... **[Documented]** (HF cards)" | hint moved before the label so each bullet ends with its bold label | style |
| All bare repo labels | "[Documented: repo]", "[Documented: repo ogx-ai/ogx]", "[Documented: repo llama-cookbook@2f22a9eb]" | repo@ref forms: PurpleLlama@172c1074, meta-llama/llama-cookbook@2f22a9eb, ogx-ai/ogx@v0.4.4, ogx-ai/ogx@f8051dd6, NVIDIA-NeMo/Guardrails@v0.24.1, meta-llama/llama-models@0e0b8c51 | label hygiene, T28, T32, T51, T54 |
| "## Reviewer notes" sections in lg_cols_a.md and lg_cols_b.md | present in the column files | removed from lg_two_level.md, moved to section 6 of this file | instruction |
| "(summarising fetch)", "(summarised fetch)", "(via summarising fetch)" qualifiers | present in several bullets | removed where the fact was re-read raw (T40, T43, T52, T53) | T40, T43, T52, T53 |
| R9 bullets | short URLs, truncated NeMo flows URL, unpinned main URLs | full-SHA pinned blob URLs, repaired flows.co URL, added arXiv HTML, Wayback, HF Hub API and use-policy URLs | T28, T35, T38, T13, T14, T18, T19 |

## 2. Column and row changes

### LG1 (Input-level prompt)

| Location | Before | After | Reason |
|---|---|---|---|
| LG1 R1 Detail (5 bullets) | source hints after labels | hints before labels | style |
| LG1 R2 Detail, bullet on PGD/GCG | no sample size | added "each attack evaluated on 100 conversations" bullet | T40 |
| LG1 R2 Detail | no Llama 3 paper figure | added "Llama Guard 3 reduced violations by 65% on average, at the cost of more refusals" (arXiv 2407.21783 s5.4.7) | T46 |
| LG1 R3 Detail, OGX bullet | "run_shield checks the last message only" | split into run_shield (whole conversation in prompt, instruction asks about last message, first message dropped if first two are user) and run_moderation (each string a separate user message, asks about last one) | T30 |
| LG1 R3 Detail, cookbook bullet | llama-cookbook@2f22a9eb | meta-llama/llama-cookbook@2f22a9eb | label hygiene |
| LG1 R4 Detail, licence text | "Llama 3.1 Community License", "Llama 3.2" | "Llama 3.1 Community License Agreement", "Llama 3.2 Community License Agreement" | T57 |
| LG1 R4 Detail, INT8 bullet | one bullet (bitsandbytes plus 40% smaller) | split: HF INT8 card load code; 8B card 40% smaller | style (one fact per bullet) |
| LG1 R4 Detail, llama-models bullet | "Meta's docs say the llama-models repo has no template [Inferred] (absence not checked)" | repo has Llama Guard only as model-id entries, no template [Documented: repo meta-llama/llama-models@0e0b8c51]; Meta docs point to the llama-cookbook helper [Documented] | T51 |
| LG1 R4 Detail | none | added drop-in replacement statement from the LG4 docs page | T52 |
| LG1 R4 Detail, OGX LG4 bullet | S1-S13 conflict only | appended "added in commit ef26259209, PR 2579, July 2025; the PR gives no reason" | T29 |
| LG1 R4 Detail, OGX 1.0 bullet | "removed the standalone Safety API; moderation served by /v1/moderations; release notes do not mention Llama Guard" [Documented: repo ogx-ai/ogx] | OGX 1.0 removed Safety API and Llama Guard provider; release notes say moderation moves to an OpenAI-compatible endpoint, blog says OGX no longer serves it itself [Documented: repo ogx-ai/ogx@f8051dd6] | T28 (CORRECTION) |
| LG1 R4 Detail, NeMo bullet | "docs example uses model type llama_guard_2" | llama-guard docs page uses type llama_guard; llama_guard_2 only on the content-safety page (new bullet) | T35 (CORRECTION) |
| LG1 R4 Detail, Llama API | one bullet from the protections page | protections bullet kept; added archived-schema bullet [Documented] and "doc pages now 404, availability unconfirmed" [To be verified] | T38 |
| LG1 R4 Detail, latency | "No official latency figures found [Not disclosed]" | two bullets: INT4 phone figure [Documented]; no figure for other versions [Not disclosed] | T3 (CORRECTION) |
| LG1 R5 Detail, absence bullet | "give no threshold guidance ... (absence in fetched text) [Documented]" | "No numeric threshold or score method appears on the cards, docs pages or papers (full text searched) [Not disclosed]" | T1 (Contradiction 23) |
| LG1 R5 Detail | none | added LG2 card 0.5 threshold, LG1 card and paper 0.5, INT8 card repeats method, Llama API response schema | T1, T38 |
| LG1 R5 Detail, NeMo/OGX bullet | one bullet, bare "[Documented: repo]" | split into NeMo (v0.24.1) and OGX v0.4.4 bullets | T32 |
| LG1 R6 Detail, language bullets | one bullet "LG4 docs page says ... protections page says 12" | four bullets: DOCS4 Image Support sentence, PROT 12 languages without list, Llama 4 Scout 12 languages [To be verified], LG4 card 7-language evaluation average | T6 |
| LG1 R6 Detail, evaluation bullet | "cards do not label their numbers as prompt-only" [Documented] | split: LG4 output-filtering only [Documented]; 3-1B table unlabelled [Not disclosed]; 1B table probably response or prompt+response [Inferred] | T44 |
| LG1 R6 Detail | none | added Llama API 8K context window (archived page) | T38 bonus |
| LG1 R6 Detail, custom categories | "(HF card, summarised fetch)" | "(HF card)" | T53 |
| LG1 R8 Summary | "No documented decision threshold, unclear LG4 language coverage, no prompt-only numbers for LG3-1B or LG4, and no latency figures." | adds "(which 12 languages)" and "latency figures only for LG3-1B-INT4 on one phone" | T3, T6 |
| LG1 R8 Detail | 7 bullets | 9 bullets: added "checked X, not stated" wording for T1, T6, T7, T44; latency bullet changed; LG4 custom-category bullet changed; cut-off bullet kept as needs-testing | T1, T3, T6, T7, T13, T44, T2 (b), T4 (b), T56 (b) |
| LG1 R9 Summary and Detail | 18 URLs | Summary now names archived Llama API pages, papers, llama-models; 28 URLs (added LG1 and LG2 PL cards, Wayback x2, arXiv HTML x4, llama-models, OGX f8051dd6 release notes and blog, NeMo docs mdx x2; removed docs.nvidia.com page and unpinned OGX main) | T28, T35, T38, T51, T1, T3, T40, T46 |

### LG2 (Output-level response)

| Location | Before | After | Reason |
|---|---|---|---|
| LG2 R1 Detail | hints after labels | hints before labels | style |
| LG2 R2 Detail, PGD bullet | "PGD at 8/255 raised unsafe responses classified safe from 6% to 27%" | "6% (no attack) to 22% at 8/255 and 27% at 128/255 and 255/255" | T39 (CORRECTION) |
| LG2 R3 Detail, OGX bullet | "run_moderation wraps every string as a user message" | adds "a list input is judged on its last string only" | T30 |
| LG2 R3 Detail | none | added OGX 1.0 bullet: both paths removed, guardrails send flattened text with no role [Documented: repo ogx-ai/ogx@f8051dd6] | T33 |
| LG2 R4 Detail, OGX bullets | "checks the last message only"; one bullet mixed v0.4.4 and 1.0 facts | "whole conversation in the prompt, asks about last message only"; v0.4.4 facts and 1.0 removal split into separate bullets with correct refs | T30, T28 |
| LG2 R4 Detail, OGX LG4 bullet | S1-S13 conflict only | appended commit ef26259209 provenance | T29 |
| LG2 R4 Detail, NeMo bullet | "docs example uses type llama_guard_2" | llama-guard docs page uses llama_guard; extra bullet for llama_guard_2 on the content-safety page | T35 |
| LG2 R4 Detail, licences | "Llama 3.1 and Llama 3.2" | exact "Community License Agreement" names | T57 |
| LG2 R4 Detail, latency | "Official latency figures [Not disclosed]" | two bullets (INT4 phone figure; none for others) | T3 |
| LG2 R5 Detail | bare "[Documented: repo]" on NeMo/OGX bullet | split NeMo and OGX v0.4.4 bullets; added LG2 card 0.5 threshold bullet; LG3-8B English bullet now says "card Table 1, response classification" | T32, T1, T42 |
| LG2 R6 Summary | "... LG3-11B-Vision is English with one image." (31 words) | "LG3 text models cover eight languages; LG4 adds images and cites the same languages; LG3-11B-Vision is English-optimised with one image." | T8 |
| LG2 R6 Detail | LG4 conflict pointer "(see R8)" | DOCS4 Image Support sentence, protections page 12 languages, Llama 4 Scout 12 languages [To be verified]; Vietnamese and Indonesian bullet reworded for 1B and 8B | T6, T7 |
| LG2 R8 Summary | "... and no latency figures." | "... and latency figures only for LG3-1B-INT4 on one phone." | T3 |
| LG2 R8 Detail | 7 bullets | 7 bullets: OGX response-role bullet deleted (T33); LG4 custom-category bullet reworded (T13); latency bullet reworded (T3); "checked X, not stated" added for threshold, languages, Vietnamese and Indonesian; cut-off bullet added (needs testing) | T33, T13, T3, T1, T6, T7, T2 (b), T45 (b), T4 (b) |
| LG2 R9 | 18 URLs | 22 URLs (pinned, added arXiv HTML x2, LG2 PL card, OGX 1.0 pair at f8051dd6, NeMo docs mdx x2); Summary now says "Meta papers" | T28, T35, T39, T3 |

### LG3 (Multimodal)

| Location | Before | After | Reason |
|---|---|---|---|
| LG3 R2 Detail | no sample size | added "100 conversations per attack" and "GCG suffixes optimised with knowledge of the harmful response (worst case)" bullets | T40 |
| LG3 R3 Detail | "(seen on both pages through a summarising fetch)"; "(see Reviewer notes)" | qualifiers removed; "(see R8)"; DOCS4 sentence located in the Image Support section | T52, T6 |
| LG3 R4 Detail, tile size | "LG4 tile size 336 by 336 plus a global tile: not stated in any source read here [To be verified]" | "dynamic transformation into 336x336 tiles plus a global tile ... [Documented]" | T9 (CORRECTION) |
| LG3 R4 Detail | none | added worked-example bullet (two images in one user turn, verdict on last Agent message) | T11 |
| LG3 R4 Detail, serving bullet | processor example only | adds 11B-V loads with AutoModelForVision2Seq and AutoProcessor, config architecture MllamaForConditionalGeneration | T53 |
| LG3 R4 Detail, OGX HF-id bullet | "Whether the HF repo id reaches the vision branch depends on ... not read [Inferred]" | "branch runs only for the exact core id Llama-Guard-3-11B-Vision; HF repo id takes the text path, image becomes a placeholder string [Documented: repo ogx-ai/ogx@v0.4.4]" | T34 |
| LG3 R4 Detail | none | added three licence bullets: Llama 3.2 AUP multimodal EU clause, Llama 4 AUP same clause, applicability [To be verified] | T58 |
| LG3 R5 Detail | "(see Reviewer notes)" | note inline ("probably a quirk"); score bullet reworded with "checked cards, docs, papers" | style, T1 |
| LG3 R6 Detail | "Response is text only; image output is not classified [Inferred]" | three bullets: 11B-V classifies prompt or prompt+text response [Documented]; LG4 response image handling [Not disclosed]; generated images unsupported [Documented] | T12 |
| LG3 R7 Detail, OGX check | "send an image-bearing message ... confirm ignored" | adds "register the shield with the core id and with the HF id and compare" | T34 |
| LG3 R8 Summary | "LG4 tile size and its token layout, an official F1 or threshold for 3-11B-Vision at its default score, behaviour beyond about three images, and whether the OGX vision branch is reached by the Hugging Face id." | "No documented threshold for 3-11B-Vision or LG4, behaviour beyond about three images in LG4, which language rules apply to multimodal prompts, and whether Meta's multimodal EU licence clause covers the guard models." | T9, T34, T58, conflict rule (see section 4) |
| LG3 R8 Detail | 6 bullets | 5 bullets: tile-size, OGX HF-id and Complete Example bullets deleted; EU clause and LG4 response-image bullets added; threshold bullet "checked, not stated" | T9, T34, T11, T58, T12, T1 |
| LG3 R9 | 7 URLs | 12 URLs (added arXiv HTML, HF Hub API, Llama 4 use policy, OGX sku_types.py and sku_list.py at v0.4.4); Summary names licence pages | T40, T34, T58 |

### LG4 (Code-interpreter and tool-use)

| Location | Before | After | Reason |
|---|---|---|---|
| LG4 R1 Summary | "... The 3-8B model was also evaluated on search tool calls. There is no general function-call validation format." | second sentence removed (the format point moves to R6 Summary) | T23 |
| LG4 R1 Detail | "3-8B-INT8, same taxonomy per its card family" | "3-8B-INT8 (own card lists 14 categories)" | T26 |
| LG4 R2 Detail | "Search tool calls: no dedicated category; evaluation covers them under the 14-category taxonomy [Inferred]" | "8B card lists S1 to S14 and S14 is code-interpreter abuse [Documented: repo PurpleLlama@172c1074]" | T27 |
| LG4 R3 Summary | "... code interpreter completions from an uncensored model." | "... from a non-safety-tuned model." | accuracy (card wording) |
| LG4 R3 Detail | "So both the user prompt and the agent's code can be judged [Inferred]" | "8B card reports Tool Use results for both prompt and response classification [Documented: repo PurpleLlama@172c1074]" | T27 |
| LG4 R3 Detail | "Meta docs (via summarising fetch): no mention of tool ..." | raw docs: roles listed are user and assistant, words tool and function call absent [Documented]; no Meta source defines tool serialisation [Not disclosed] | T23, T52 |
| LG4 R3 Detail | none | added HF templates map only user and assistant [Inferred, offline render]; Llama API accepts tool messages [Documented]; OGX writes "Tool: ..." lines [Documented: repo ogx-ai/ogx@v0.4.4] | T23 |
| LG4 R4 Detail | LG4 card bullet; bare cookbook label; OGX LG4 bullet | quote added to the S1-S13 average bullet; cookbook label meta-llama/llama-cookbook@2f22a9eb with "same on main 2026-10-08"; commit provenance appended | T25, T54, T29 |
| LG4 R6 Summary | "... There is no documented tool-call or function-call schema. [Documented]" | "Conversation turns, with code in the agent turn ... Meta does not disclose a tool-call or tool-output format, so code would go in as plain text. [Inferred]" | T23 |
| LG4 R7 Detail | serialisation variants | adds Tool-label turn as OGX emits it | T23 |
| LG4 R8 Detail | 5 bullets | 4 bullets: INT8 S14 bullet deleted (T26); "Meta docs mention a tool role" bullet deleted (T23); serialisation bullet "checked ... none defines it"; OGX bullet "no rationale in the adding commit"; serialisation-reaction bullet added (needs testing) | T26, T23, T29, T24 (b) |
| LG4 R9 | 6 URLs | 9 URLs (added Wayback moderations page, HF Hub API for 3-8B template; cookbook and OGX pinned); Summary adds archived Llama API pages | T23, T38 |

### LG5 (Custom-policy)

| Location | Before | After | Reason |
|---|---|---|---|
| LG5 R1 Summary | "... Category replacement and exclusion are documented for 3-1B and 3-11B-Vision; none is documented for Llama Guard 4." | "The chat templates of 3-1B, 3-11B-Vision and Llama Guard 4 read optional custom and excluded category lists; the 3-8B template has a fixed list." | T13 (CORRECTION), T14 |
| LG5 R1 Detail | "(summarising fetch)" qualifiers; LG1 paper quote | qualifiers removed; docs quote taken from DOCS3 and DOCS4; paper quote "(arXiv HTML, read raw)" | T52, T43 |
| LG5 R2 Detail | "paper showed no zero-shot or custom results [Inferred]" | "no zero-shot, few-shot or custom results in the papers, Llama 3 paper section or cards (full text searched) [Not disclosed]"; added training category-dropping bullet | T20 |
| LG5 R4 Summary | "The Hugging Face chat template accepts categories and excluded category keys on the 3-1B and 3-11B-Vision cards; the cookbook builder stops at Llama Guard 3. ..." | resolution text: 3-1B, 3-11B-Vision and Llama Guard 4 templates take custom categories; the 3-8B template does not | T13, T14 |
| LG5 R4 Detail | "3-8B and LG4 HF pages: no snippet [Documented]" and "[To be verified] whether templates accept" | replaced by: templates read categories (1B, 11B-V, LG4); LG4 default S1-S14 text, S1-S13 with image; no Meta LG4 snippet [Not disclosed]; 3-8B and INT8 templates hard-code S1-S14; arguments ignored [Inferred] | T13, T14 |
| LG5 R4 Detail | cookbook notebook bullets ("has a Custom Categories section", "does not load LG4") | "read in full"; whole-repo statement "no file mentions LG4"; customisation notebook bullets (3-8B, builder, ToxicChat, PEFT, two caveats); 404 path note | T18, T19 |
| LG5 R4 Detail | LG1 paper bullets | added Table 2 note (zero-shot with target taxonomy) | T43 |
| LG5 R4 Detail, OGX LG4 bullet | S14 cannot be excluded | appended commit provenance | T29 |
| LG5 R7 Summary | "Llama Guard 4 as undocumented probe" | "Llama Guard 4 (template supports custom lists, untested)" | T13 |
| LG5 R7 Detail | LG4 bullet "try the same arguments and record whether the template errors, ignores them, or applies them" | LG4 template reads them; note typed-parts content; added 3-8B bullet | T13, T14 |
| LG5 R8 Summary | "Whether categories and excluded keys work in the 3-8B and LG4 chat templates, any LG4 custom-policy guidance, contents of the customization and fine-tuning notebook, and zero-shot quality for current models." | "Whether custom and excluded categories change verdicts as intended on the 3-1B, 3-11B-Vision and Llama Guard 4 templates, whether Meta documents any Llama Guard 4 custom-policy usage, and zero-shot quality for current models." | T13, T14, T18 |
| LG5 R8 Detail | 4 bullets | 5 bullets: template-support and notebook-path bullets deleted; added needs-testing bullets (verdict change, key formats, limits, zero-shot quality) | T13, T14, T18, T15 (b), T16 (b), T17 (b), T21 (b) |
| LG5 R9 | 9 URLs | 14 URLs (added HF Hub API for LG4, 3-8B, INT8 templates; arXiv HTML x2; both notebooks; cookbook pinned); Summary names chat templates | T13, T14, T18, T19 |

Rows with identical text before and after: LG1 R7, LG2 R7, LG3 R1, LG4 R5, LG5 R3, LG5 R5, LG5 R6.

## 3. Inventory changes (lg_inventory.md to lg_inventory_final.md)

Global: all non-standard labels normalised (about 114 occurrences in 52 forms: PL forms to "[Documented: repo PurpleLlama@172c1074]" with the card named after the bracket; HF, DOCS, PROT, arXiv and ai.meta.com forms to plain "[Documented]" with the source in parentheses; bare repo forms to repo@ref; "[Not found]" x4 resolved to [Documented] or [Not disclosed]); all 4 bold cells and all backticks removed; Self-check and Reviewer notes sections dropped (moved to this file); table-cell pipes checked (none other than separators); Source URLs pinned to full SHA where a repo is cited.

### (a) Variant table

| Row and cell | Before | After | Reason |
|---|---|---|---|
| LG1 Release date | "2023-12-07 [Documented: arXiv submission date] ... 2023-07-18 [To be verified]" | 2023-12-07 [Documented] (Meta post and arXiv); 2023-07-18 is the Llama 2 licence date; HF repo created 2023-12-05 | T47 |
| LG1 Base / size | seq length 4096 [summarised]; context [Not disclosed] | 4096 [Documented] (arXiv read raw); base Llama 2 7B 4k [Inferred] | T5, T43 |
| LG1 Languages | [Not disclosed] | adds HF metadata tag en (not a card statement) | T8 |
| LG1 Taxonomy | O1-O6 with "see Table (b)" | adds code order and sources: HF chat template, paper; PL card prose order differs | T50 |
| LG1 Custom, Score | AUPRC numbers [summarised]; "threshold, none given" | adds no adaptation 0.837 and Table 2 note; paper uses 0.5 | T43, T1 |
| LG1 Licence, Distribution, Headline | non-standard labels | exact title in capitals; labels normalised | T57, label hygiene |
| LG2 Release date | "2024-04-18 [HF licence date only]" | adds Meta Llama 3 launch post; HF created 2024-04-17 | T48 |
| LG2 Base, Languages, Taxonomy | context [Not disclosed] | adds base 8k [Inferred]; HF tag note; HF template confirms S1-S11 | T5, T8, T50 |
| LG2 Score method | threshold 0.5 [Documented: PL card] | label normalised | label hygiene |
| LG2 Headline eval | two result sets, "see Reviewer notes" | each set labelled with its test set, "do not conflict" | T42 |
| 3-1B Release date | "2024-09-25 [licence date only]" | adds Llama 3.2 post, HF created 2024-09-20 | T48 |
| 3-1B Base, Languages, Custom, Headline | context [Not disclosed]; "see Reviewer notes" | adds base 128k [Inferred]; Vietnamese and Indonesian also in arXiv 2411.17713 Table 1, support [Not disclosed]; chat template source; table unlabelled [Not disclosed] | T5, T7, T53, T44 |
| 3-1B-INT4 Release date | "2024-09-25 [HF licence date only]; paper 2024-11-18" | Meta Connect 2024 [Documented] (paper); same-day release [Inferred]; paper date; HF created | T48 |
| 3-1B-INT4 Base, Languages | context [Not disclosed] | base 128k [Inferred], inheritance undocumented; Vietnamese and Indonesian note | T5, T7 |
| 3-1B-INT4 Distribution | "(458 MB)", bold lead, [Documented: HF file listing, summarised] | 458,464,800 bytes, about 437 MiB; full file list; bold removed; "[Documented] (HF Hub file listing)" | T41, T53 |
| 3-1B-INT4 Headline eval | "440 MB vs 458 MB unexplained"; abstract "30 tokens/s" | paper TTFT 2.5 s and Moto-Razor phone; size explained as MiB [Inferred] | T3, T41 |
| 3-1B-INT4 Licence | name only | adds derivative duties under section 1.b | T59 |
| 3-8B Release date | "2024-07-23 [licence date only]" | adds Llama 3.1 post; HF created 2024-07-22 | T48 |
| 3-8B Custom | "categories= shown on the 1B card, not seen on the 8B card [To be verified]" | fixed S1-S14 template [Documented]; ignored arguments [Inferred]; cookbook builder route | T14 |
| 3-8B Base | context [Not disclosed] | base 128k [Inferred] | T5 |
| 3-8B-INT8 Release, Base | licence date only | adds post and HF created 2024-07-21; base 128k [Inferred] | T48, T5 |
| 3-8B-INT8 Taxonomy | "S1-S14 [Documented: HF intro, summarised]" | "[Documented] (INT8 HF card lists 14 categories; template lists S14)" | T26, T14 |
| 3-8B-INT8 Custom, Score | "Same generic statement"; "Card does not give a separate method [Not disclosed]" | same fixed template, identical file; INT8 card repeats the first-token method [Documented] | T14, T1 (CORRECTION) |
| 3-8B-INT8 Licence | name only | adds derivative duties | T59 |
| 3-11B-V Release, Base | licence date only; context [Not disclosed] | adds post and HF created 2024-09-20; fine-tune length 8192 [Documented]; base 128k [Inferred] | T48, T5 |
| 3-11B-V Languages | "English only" | optimised for English, not stated as English-only; DOCS3 sentence; HF tag note | T8 (CORRECTION) |
| 3-11B-V Score | "First-token probability is not stated on the 11B card; threshold [Not disclosed]" | no score method or threshold stated (sources checked) [Not disclosed] | T1 |
| 3-11B-V Licence | name only | adds AUP multimodal EU clause, HF EU-disallowed gating flag, applicability [To be verified] | T58 |
| 3-11B-V Distribution | MllamaForConditionalGeneration [cookbook notebook] | adds HF card AutoModelForVision2Seq and config architecture | T53 |
| LG4 Release date | "licence 2025-04-05; announcement 2025-04-29 [summarised]" | label normalised; adds HF created 2025-04-23 | T48, T49 |
| LG4 Base, Modality, Languages | context [Not disclosed]; "336x336 tiles [dev.meta.ai LG4 page]" | base 10M [Inferred]; tiles plus a global tile [Documented] (DOCS4); template default S1-S14 text, S1-S13 with image; DOCS4 and PROT language statements | T5, T9, T13, T6 |
| LG4 Custom | "categories= not shown ... [Not found]" | template reads optional categories and excluded keys [Documented]; no card, cookbook or docs snippet shows use [Not disclosed] | T13 (CORRECTION) |
| LG4 Licence, Distribution | name only; "also in Llama API /moderations [PL card, protections page]" | adds Llama 4 AUP clause, applicability [To be verified]; label split, availability [To be verified] | T58, T38 |
| LG4 Headline eval | numbers only | adds "output filtering only; no prompt-only numbers" | T44 |

### (b) Category crosswalk

| Row and cell | Before | After | Reason |
|---|---|---|---|
| Intro paragraph | "HF card prose lists the same six in a different order, see Reviewer notes" | PL LG1 card prose order differs (Criminal Planning last); HF template, paper and cookbook agree [Documented]; naming-drift sentence | T50, T55 |
| Rows 3, 4, 10 Notes | "Name in docs and cookbook is ...", "Docs and cookbook name ..." | card long form versus prompt-text short form stated as [Documented] | T55 |
| Row 6 (Specialized advice) LG3 cell | "S5 is Defamation; this concept is **S6**" | "S6" | label hygiene (bold removed, quirk fixed) |
| Row 10 LG1 cell | "O6 Self-Harm (HF/PL card prose names it ...)" | HF template says Self-Harm, paper says Suicide & Self-Harm | T50 |
| Row 14 (Code interpreter abuse) Notes | cookbook and OGX conflict sentence, unlabelled | labelled with repo@ref; cookbook verified at 2f22a9eb and main 2026-10-08; OGX commit provenance | T54, T29 |
| All Notes cells | [Inferred] and [Documented] mixed in a single trailing sentence | one label per fact | label hygiene |

Row count 14, LG1 codes 6 (order per T50), LG2 codes 11, LG3/LG4 codes 14: unchanged.

### (c) Integration paths

| Row and cell | Before | After | Reason |
|---|---|---|---|
| HF transformers, Versions | LG1 chat template [summarised] | HF Hub API source; 11B-V HF card AutoModelForVision2Seq | T50, T53 |
| HF transformers, Input/Output | "Role is chosen by the last message: user for input, assistant for output" | DOCS3 role rule; HF templates map user and assistant only, tool role unhandled, 3-8B needs string content [Inferred] | T23 |
| HF transformers, Categories | 8B / INT8 / LG4 "[Not found]" | 1B, 11B-V, LG4 read the arguments [Documented]; 8B and INT8 fixed list [Documented], ignored arguments [Inferred] | T13, T14 |
| HF transformers, Caveats | gated, bitsandbytes, max_new_tokens | adds EU-disallowed flag, template wording difference by model, LG4 backslash-n and typed-parts note [Inferred] | T58, T55, T13 |
| cookbook prompt_format_utils | 3 bare labels | meta-llama/llama-cookbook@2f22a9eb; "no file mentions LG4"; main unchanged 2026-10-08 | T54, T19 |
| cookbook notebooks | 5 bare or listing labels; "no LG4 example" | meta-llama/llama-cookbook@2f22a9eb; customisation notebook described (3-8B); whole-repo LG4 check; 404 of old llama-recipes path | T18, T19 |
| OGX provider, Input/Output | "Role comes from the last message, wrapped as User/Agent ..." | every turn capitalised role (User, Assistant, Tool), not Agent; whole conversation in prompt; vision branch only for exact core id | T31, T30, T34 (CORRECTION) |
| OGX provider, Status | bold "removed in 1.0"; "[... main, listing]"; "seven removed providers" | plain text; ogx-ai/ogx@f8051dd6; blog says six and seven; commit 5ad4753869 | T28 |
| OGX provider, Caveats | LG4 S1-S13 comment | adds commit ef26259209, PR 2579, no stated reason | T29 |
| OGX /v1/moderations, Input/Output, Output | bare labels; "every input string becomes a user message" | v0.4.4 label; "all in one prompt, asks about last one only"; "all-1.0 probably a quirk" [Inferred] | T32, T30 |
| OGX /v1/moderations, Status | bold "Contradictory, treat as [To be verified]" | resolved: removed from the 1.x server, route existed at v0.4.4, pinned f8051dd6 | T28 (CORRECTION) |
| OGX /v1/moderations, Source | main URLs | three URLs pinned to f8051dd655358415c6aee152c290622b607bf6ab | T28 |
| NeMo, Versions, I/O, Categories, Output, Caveats | bare "repo docs", "repo flows.co", "repo; effect Inferred" | NVIDIA-NeMo/Guardrails@v0.24.1; effect split to [Inferred]; two model types explained; develop 9f793de5 same [Documented: develop/unreleased]; "[INST]" template wording replaced | T35, label hygiene |
| ExecuTorch, Caveats | "[Documented: PL; judgement Inferred]"; "abstract gives at least 30 tokens/s" | split: bare string and download-link facts [Documented: repo PurpleLlama@172c1074]; "expects a message list" [Inferred]; paper TTFT 2.5 s and phone [Documented]; other versions [Not disclosed] | T37, T3 |
| Llama API, What, Versions, I/O, Categories, Output, Status, Caveats, Source | snippet-only [To be verified]; two [Not found]; Status "current" | schema from archived official page [Documented] (Wayback 2025-09-14); no custom-category parameter; response fields; context window 8K; Status "documented in 2025; availability [To be verified]"; live URLs 404; two Wayback URLs | T38 |
| OGX Responses guardrails | "[main docs]", two "[blog]" | ogx-ai/ogx@f8051dd6; adds "plain text with no User or Agent role" | T28, T33 |

Row counts: (a) 8, (b) 14, (c) 9.

## 4. Conflict decisions

1. LG3 R8 Summary, T34 versus resolutions_1 (T9). Resolutions_1 proposed "... and whether the OGX vision branch is reached by the Hugging Face id". T34 (lg_resolutions_2) resolved that question (the HF repo id does not reach the vision branch). Decision: T34 wins; the clause is dropped and the finding is stated in LG3 R4 Detail (and R7).
2. LG3 R8 Summary, resolutions_2 text versus T9. Resolutions_2's proposed Summary still lists "LG4 tile size and its token layout" as open, but T9 (resolutions_1, verbatim DOCS4 quotes) shows DOCS4 states the tile size. The more primary quote wins: tile clause dropped. The final Summary also adds the open language and EU-clause items (T6, T58), so it matches neither proposal word for word.
3. T28: release notes versus the 2026-06-23 blog. Both are verbatim from the repo at f8051dd6; combined as "release notes say moderation moves to an OpenAI-compatible endpoint; the blog says OGX no longer serves it; guardrails call an external endpoint". The apparent conflict is resolved by the code and the commit title, so the inventory row no longer carries [To be verified].
4. T30 versus the draft's "checks the last message only" (LG1 R3, R4; LG2 R4): the code quote (whole conversation in prompt, instruction asks about last message) is the more primary source and wins.
5. T35: LG1 R4 and LG2 R4 said the docs example uses llama_guard_2; resolutions_2 shows two different docs pages (llama-guard.mdx uses llama_guard; content-safety.mdx uses llama_guard_2). Both facts kept, each attached to its page.
6. T38 label rule: Wayback schema facts labelled [Documented] with the plain text "(archived official page, Wayback 2025-09-14)"; current availability kept [To be verified]. LG1 R4 Summary still says "Llama API options" (resolutions_2 said unchanged); the Detail carries the caveat.
7. T23 label for the raw-docs statement: resolutions_1 (T52) labelled "no tool wording on the docs pages" as [Not disclosed]; resolutions_2 (T23) labelled the observed roles and absent words [Documented] and the missing serialisation definition [Not disclosed]. Both quote raw pages; resolutions_2's split is more specific and was used.
8. T13 and T14 versus resolutions_1 T53 ("not on the 3-8B, 3-8B-INT8 and LG4 HF pages"): T53 only covers rendered card text; resolutions_2 read the chat templates themselves. The template (primary file) wins for "accepts or not"; the card-text absence is kept as "[Not disclosed] no Meta snippet".
9. T3 (resolutions_1) versus the shorter wording in T37 (resolutions_2, "paper abstract gives at least 30 tokens/s"): resolutions_1's text with the abstract quote (30 tokens/s, 2.5 s, Moto-Razor) was used everywhere.
10. T57 licence names: inventory draft used "LLAMA 2 Community License Agreement"; LICENSE titles are used verbatim (capitals) in the inventory. Column Detail uses "Community License Agreement" in title case.
11. T48: HF repo creation dates are given as extra facts but labelled "repo creation, not release"; the launch-post date stays the release date.
12. LG4 R3 Summary: "uncensored" changed to "non-safety-tuned" to match the card's quoted wording (not a resolution item).
13. Offline jinja2 renders (T13, T14, T23): kept [Inferred]; chat-template contents read from the HF Hub API kept [Documented] (HF meta-llama repo metadata).
14. T35 develop label: develop 9f793de5 is identical to v0.24.1 for the files read, so [Documented: develop/unreleased] appears once, only in the inventory NeMo caveat.
15. LG3 R4 Summary keeps "the OGX moderation endpoint ignores images" although OGX removed the route in 1.0; the Detail carries the v0.4.4 pin. Not changed because no resolution targets it.

## 5. Remaining open items

By Tn, with class from lg_triage.md.

| Tn | Status after merge | Class | Where kept |
|---|---|---|---|
| T2 | cut-off on own data, not answerable from docs | b | LG1 R8, LG2 R8 |
| T4 | measured latency on own hardware | b | LG1 R8, LG2 R8 |
| T5 | PARTLY RESOLVED: no guard card states a context length; config.json gated (401); only fine-tune lengths and base-card values (Inferred) | a | inventory (a) Base / size cells |
| T6 | PARTLY RESOLVED: which 12 languages PROT means; LG4 card, DOCS4 and PROT still disagree | a | LG1 R8, LG2 R8, LG3 R8 |
| T7 | STILL OPEN: Vietnamese and Indonesian support not stated (1B, INT4, 8B tables) | a | LG1 R8, LG2 R8, inventory (a) |
| T10 | LG4 behaviour above about three images | b | LG3 R8 |
| T12 | PARTLY RESOLVED: LG4 response image handling not stated | a | LG3 R6, LG3 R8 |
| T15 | do custom and excluded categories change verdicts on 3-1B, 3-11B-V, LG4 | b | LG5 R8 |
| T16 | custom key formats other than S1 style | b | LG5 R5, LG5 R8 |
| T17 | limits on number or length of custom categories | b | LG5 R6, LG5 R8 |
| T21 | zero-shot or few-shot quality on own taxonomy | b | LG5 R8 |
| T22 | INT4 custom prompts via edited prompt file | b | inventory (a) INT4 Custom [Inferred] |
| T23 | STILL OPEN (confirmed from raw sources): no tool-call or tool-output serialisation defined | a | LG4 R3, R6, R8 |
| T24 | which serialisation form the classifier reacts to; S14 on image plus code | b | LG4 R7, R8 |
| T29 | PARTLY RESOLVED: provenance found, intent not stated | a | LG4 R8 |
| T31 | PARTLY RESOLVED: columns correct, inventory fixed; Agent wording is Meta's | a | closed in text |
| T36 | NeMo violation parsing effect (S1,S2 as one item) only inferred; needs a run | b | inventory (c) NeMo [Inferred] |
| T37 | PARTLY RESOLVED: "sample looks incomplete" stays a judgement | a | inventory (c) ExecuTorch [Inferred] |
| T38 | PARTLY RESOLVED: current Llama API availability; live pages 404 | a | LG1 R4, inventory (c) |
| T44 | PARTLY RESOLVED: no prompt-only numbers for 3-1B or LG4 | a | LG1 R6, LG1 R8 |
| T45 | like-for-like response numbers across versions | b | LG2 R8 |
| T56 | behaviour on jailbreak and prompt-injection prompts | b | LG1 R8 |
| T58 | PARTLY RESOLVED: clause text found; applicability to 11B-V and LG4 not stated by Meta (not legal advice) | c | LG3 R4, R8, inventory (a) |
| T1 | RESOLVED (negative): no numeric threshold for 3-1B, INT4, 3-8B, INT8, 11B-V, LG4; open only as "not stated" wording | a | LG1 R5, R8 and other R8s |
| T3 | CORRECTION applied: only INT4 has a speed figure | a | R4, R8 |

Items resolved and applied with no residue: T8, T9, T11, T13, T14, T18, T19, T20, T25, T26, T27, T28, T30, T32, T33, T34, T35, T39, T40, T41, T42, T43, T46, T47, T48, T49, T50, T51, T52, T53, T54, T55, T57, T59.

## 6. Moved Reviewer notes

Reviewer notes from lg_cols_a.md, lg_cols_b.md and lg_inventory.md, with their status after the resolutions, plus notes from lg_resolutions_1.md and lg_resolutions_2.md.

From lg_cols_a.md
- Read raw at the pinned commits: LG4, LG3-8B, LG3-1B and LG3-11B-Vision MODEL_CARD.md, LG3-1B ET_INSTRUCTIONS.md, cookbook prompt_format_utils.py, OGX v0.4.4 llama_guard.py, NeMo v0.24.1 actions.py and flows.co. Status: still true. Since then the Meta docs, protections page, HF cards, arXiv HTML, OGX 1.0 notes and NeMo docs were re-read raw by the resolution agents (T52, T53, T40, T28, T35), so the "summarised fetch" caveat no longer applies to them.
- Contradiction, LG4 languages (card versus docs page versus protections page). Status: narrowed (T6): the docs sentence sits under Image Support and mirrors the LG3 wording; the protections page gives no list. Still open.
- Contradiction, LG3-1B languages (8-language list versus Vietnamese and Indonesian columns). Status: open (T7); also in the INT4 paper Table 1 and in the 3-8B row.
- Contradiction, OGX v0.4.4 LG4 categories S1-S13 while citing a card that lists S14. Status: open as intent (T29); provenance commit ef26259209 found.
- Brief correction, OGX moderation scores: safe result scores 1.0. Status: confirmed (T32); "probably a quirk" is [Inferred].
- Observation, OGX role label "Assistant" not "Agent". Status: confirmed (T31).
- Contrast, failure mode: OGX moderation fails open on unknown codes; NeMo blocks unparseable replies (fails closed). Status: unchanged.
- NeMo docs example uses llama_guard_2. Status: corrected (T35): llama-guard.mdx uses type llama_guard with LlamaGuard-7b; content-safety.mdx uses llama_guard_2 with Meta-Llama-Guard-2-8B; the llama guard flows hard-code llama_guard.
- ET instructions: 19193 and 39257 are argmax token ids, not probabilities. Status: unchanged.
- Brief says "11B-V English only"; card says "optimized for English language". Status: corrected (T8); brief should change.
- Taxonomy definitions on all cards begin "Responses that ...". Status: unchanged.
- Trade-off statements verified in spirit; Llama 3 paper numbers not checked. Status: checked (T46): -65% average violation reduction (arXiv 2407.21783 section 5.4.7).
- LG3-8B Table 5 figures are for 8B and 8B-INT8 only; 1B and LG4 tables are unlabelled. Status: partly resolved (T44): LG4 is output filtering only; 1B unlabelled.

From lg_cols_b.md
- CONTRADICTION (brief versus paper): PGD response misclassification at 8/255 is 22%, not 27%. Status: closed in favour of the paper (T39); fix the brief and lg_cols_a.md LG2 R2.
- CONTRADICTION, LG4 docs page versus card on text language. Status: see above (T6).
- CONTRADICTION, OGX LG4 S1-S13. Status: see above (T29).
- The brief says the 3-1B card documents categories and excluded keys; PL MODEL_CARD.md does not show them, the HF page does. Status: resolved (T53).
- OGX "checks the LAST message only": the code builds the prompt from the whole list and asks about the last message. Status: confirmed (T30); the columns now say so.
- OGX moderation scores. Status: see above (T32).
- 3-1B GitHub card table includes Vietnamese and Indonesian columns. Status: open (T7).
- LG3 docs fetch returned an unprompted "S14 is text-only" note. Status: confirmed spurious (T12): not on the LG3 or LG4 docs pages, only the LG4 card says it.
- "336 by 336 tiles plus global tile" claim was not found. Status: corrected (T9): DOCS4 states it. The 560 by 560 four-chunk statement for 3-11B-Vision stays verified.
- Cookbook template wording "according our" versus docs "according to our". Status: explained (T55): the split is by model template (3-8B, INT8, 3-1B, 11B-V and cookbook and OGX use "according our"; LG4 template uses "according to our"); build test prompts from the target model's own template.
- Docs, HF and arXiv pages were read through summarising fetches; cookbook notebook searched by pattern. Status: superseded (T52, T53, T19): raw re-reads, notebook read in full.
- Direct HTTP download was blocked for raw.githubusercontent.com. Status: unchanged; resolution agents used codeload tarballs and GitHub blob pages.
- The 8B-INT8 card was not read separately. Status: resolved (T26): its card and chat template list S14.

From lg_inventory.md
- LG1 code order. Status: closed (T50): cookbook, paper and HF chat template agree on O1 to O6 as used; PL card prose order differs and has no codes.
- OGX /v1/moderations contradiction. Status: closed (T28): standalone route removed in 1.x; release notes refer to an external OpenAI-compatible service.
- OGX "checks the LAST message only". Status: closed (T30).
- OGX LG4 categories. Status: open as intent (T29); commit ef26259209, PR 2579, July 2025, no rationale.
- 3-1B languages and card-versus-paper differences (Hindi 0.680 on the card versus 0.815 in the paper; Vietnamese 0.723/0.130 versus 0.819/0.099; Portuguese 0.763/0.114 versus 0.798/0.108; German 0.845/0.036 versus 0.851/0.06). Status: open (T7); cite the card for any 3-1B number.
- LG2 headline numbers on different sets. Status: closed (T42).
- 3-1B-INT4 size 440 MB versus 458 MB. Status: closed (T41): units; 458,464,800 bytes = 437.2 MiB; Meta post 438 MB; paper 0.4 GB.
- NeMo model type. Status: closed (T35).
- Cookbook LG3 list always 14 categories. Status: verified at 2f22a9eb, same on main on 2026-10-08 (T54).
- Naming drift. Status: closed (T55): cards use long names, prompt strings use short names; hazard prose uses card names, test prompts use the template strings.
- Summarised-fetch caveats (HF page facts, Meta docs, arXiv abstracts, LG1 paper numbers, LlamaCon date, Llama API request shape). Status: superseded: all re-read raw (T53, T52, T43, T47, T49); Llama API schema from Wayback (T38).
- Not-found list: context length (partly resolved, T5), score thresholds (T1, confirmed not disclosed), categories examples for 3-8B, INT8, LG4 (T13, T14), Llama API schema (T38), latency (T3), announcement dates (T47, T48, T49).

From lg_resolutions_1.md and lg_resolutions_2.md
- The arXiv HTML of 2411.10414 prints "date: August 24, 2026"; this is a build artefact; the abs page says submitted 15 Nov 2024.
- T46 uses the Llama 3 paper (arXiv 2407.21783), which is Meta-authored but outside the brief's paper list.
- HF config.json and raw README return 401 for all gated repos; no max_position_embeddings value exists in the evidence.
- HF chat templates were read from the HF metadata API (tokenizer_config), not raw repo files; "not shown on the card" claims rest on the PurpleLlama card mirror because the HF README was unreadable. Revisions: 3-8B 7327bd9f, INT8 951579e6, 3-1B acf7aafa, 11B-V 62d42755, LG4 87acb4b9.
- Offline jinja2 3.1.6 renders (T13, T14, T23) are agent experiments, labelled [Inferred]; HF's own renderer was not run.
- The LG4 chat template contains a literal backslash-n pair after each message text outside any Jinja string, so a rendered prompt may contain the two characters instead of newlines [Inferred]; worth a one-line check when testing.
- Archived Llama API pages (Wayback) are copies of Meta pages; the sheet decides whether to accept them as official. If not, relabel the T38 schema facts [To be verified].
- The OGX 1.0 release-notes sentence is ambiguous on its own; the blog, commit title and code settle it. The blog says "six" safety providers at one line and "seven" at another.
- Not checked: cookbook main beyond head 2f22a9eb; live docs.nvidia.com NeMo pages (repo docs at v0.24.1 used); OGX tags after v0.4.4 other than main (pinned f8051dd6).
- T58 and T59 give clause text only, not legal advice.
- This merge: where a resolution replaced a Summary (LG4 R1, LG4 R6, LG5 R1, R4, R7, R8, LG1 R8, LG2 R6, R8), the replacement text was used as given; the word counts below were rechecked against the limits.

## 7. Self-check

### 7a. Summary word counts (excluding the trailing bold label; limit 45, R7 60)

| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 |
|---|---|---|---|---|---|---|---|---|---|
| LG1 | 28 | 38 | 29 | 32 | 34 | 34 | 37 | 30 | 29 |
| LG2 | 26 | 38 | 24 | 26 | 33 | 36 | 42 | 26 | 25 |
| LG3 | 30 | 36 | 36 | 36 | 35 | 30 | 27 | 35 | 18 |
| LG4 | 32 | 32 | 36 | 34 | 29 | 37 | 30 | 32 | 13 |
| LG5 | 40 | 25 | 26 | 41 | 20 | 17 | 31 | 36 | 14 |

45 Summaries counted; maximum 42 words; Summaries over the limit: 0.

### 7b. Labels in lg_two_level.md (bold labels, Summaries and Detail)

| Label | Count |
|---|---|
| [Documented] | 221 |
| [Inferred] | 47 |
| [Documented: repo ogx-ai/ogx@v0.4.4] | 24 |
| [Documented: repo meta-llama/llama-cookbook@2f22a9eb] | 17 |
| [Not disclosed] | 14 |
| [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1] | 9 |
| [Documented: repo PurpleLlama@172c1074] | 7 |
| [To be verified] | 5 |
| [Documented: repo ogx-ai/ogx@f8051dd6] | 3 |
| [Documented: repo meta-llama/llama-models@0e0b8c51] | 1 |
| Total | 348 |

Labels on the 35 Summaries R1 to R7: [Documented] 29; [Inferred] 6. R8 and R9 Summaries carry no label.

### 7c. Inventory row counts (lg_inventory_final.md)

- (a) Variant table: 8 data rows, 16 columns
- (b) Category crosswalk: 14 data rows, 7 columns (14 LG3/LG4 codes, 11 LG2 codes, 6 LG1 codes)
- (c) Integration paths: 9 data rows, 9 columns
- Bold markers and backticks in lg_inventory_final.md: 0 and 0
- Labels outside the allowed forms in lg_inventory_final.md: 0
- Covered by Table 3 column cells: exact header strings or the legacy phrase in all 8 rows

### 7d. Python parse of lg_two_level.md

- 5 columns x 9 rows, each with one Summary line and at least one Detail bullet: pass
- Every line has balanced bold markers: pass
- No backtick, underscore or dollar sign in any Summary: pass
- R9 bullets are one URL each; R8 bullets carry no label; every other Detail bullet ends with a bold label: pass
- Column headings match the five required strings exactly: pass

## Verifier fixes

Source: lg_review.md "Required fixes". Optional suggestions not applied.

| Location | Before | After | Fix # |
|---|---|---|---|
| LG3 R4 Summary | "... the OGX moderation endpoint ignores images." | "... the OGX v0.4.4 moderation path ignored images and was removed in OGX 1.0." | 1 |
| LG3 R4 Detail | no OGX 1.0 bullet | added OGX 1.0 removal bullet [Documented: repo ogx-ai/ogx@f8051dd6] after the HF-id bullet | 1 |
| LG3 R9 | 12 URLs | 14 URLs (OGX 1.0 release notes and 2026-06-23 blog at f8051dd6) | 1 |
| LG3 R7 last Detail bullet | "OGX check: send an image-bearing message ..." | "OGX check (v0.4.4 only; the moderation route and shields were removed in OGX 1.0): ..." | 2 |
| LG3 R5 OGX bullet | one [Documented] bullet ending "probably a quirk" | split: scores fact [Documented: repo ogx-ai/ogx@v0.4.4]; "probably a quirk of the code" [Inferred] | 3 |
| LG4 R5 Summary | "No numeric score is returned by the model itself." | "The model returns text only; the 3-8B card derives a score from the first-token probability." | 4 |
| LG4 R5 Detail | 3 bullets | added 3-8B first-token-probability bullet [Documented] | 4 |
| LG1 R5 Summary | "A score is the first-token probability of unsafe, with a threshold left to the deployer." | "LG3-8B and its INT8 card derive a score from the first-token probability, with no stated threshold; LG3-1B, 11B-Vision and LG4 describe none." | 5 |
| LG2 R5 Summary | "A score is the first-token probability of unsafe; no threshold is documented except for earlier versions." | "The LG3-8B and LG2 cards describe a first-token-probability score; only LG2 gives a threshold (0.5)." | 5 |
| LG1 R4 Summary | "... with INT8, INT4 and Llama API options." | "... with INT8 and INT4 variants." | 6 |
| LG2 R4 Summary | "... cookbook helper, OGX and NeMo." | "... cookbook helper, OGX (to v0.4.4) and NeMo." | 6 |
| LG1 R1 Detail, Versions covered | LG4, LG3-1B, LG3-8B, ... | adds LG3-1B-INT4 (mobile) | 7 |
| LG2 R1 Detail, Versions covered | LG4, LG3-1B, LG3-8B, ... | adds LG3-1B-INT4 (mobile) | 7 |
| Inventory (a) 3-8B-INT8, Custom categories cell | "Same fixed template as 3-8B (identical file) [Documented]" | appended "Custom text only through the cookbook builder, using the same prompt format as 3-8B [Inferred]" | 8 |
| Inventory (c) NeMo row, Caveats | "The develop branch at 9f793de5 ... [Documented: develop/unreleased]" | "The develop branch has the same content for these files [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1] (develop 9f793de5 identical)" | 9 (coordinator override: no develop pin) |

Effects on earlier sections: the Summaries changed list now also includes LG1 R4, LG1 R5, LG2 R4, LG2 R5, LG3 R4 and LG4 R5 (20 in total). Conflict decision 6 (Llama API in LG1 R4 Summary) and item 15 (LG3 R4 Summary) are superseded by fixes 6 and 1. The label [Documented: develop/unreleased] no longer appears in the outputs; section 3 and conflict decision 14 refer to it as history only. Section 7 counts above were produced before these fixes; the post-fix self-check is run in the final report (R9 URL totals: LG3 14).
