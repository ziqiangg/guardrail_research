## Column LG1: Llama Guard: Input-level prompt content-safety classification
### R1
Summary: **Input-level prompt content-safety classification.** Llama Guard reads a user prompt and replies safe or unsafe, listing the violated hazard categories when unsafe. The same model also classifies responses. **[Documented]**
Detail:
• Llama Guard can classify content in LLM inputs (prompt classification) (LG3-1B, LG3-8B and LG4 model cards) **[Documented]**
• The model acts as an LLM: it generates text saying whether the prompt is safe or unsafe and, if unsafe, lists the violated categories **[Documented]**
• Prompt versus response is chosen by the instruction wording (role `User` for the input, `Agent` for the output); it is one model, not two (Meta LG3 and LG4 docs pages) **[Documented]**
• LG4 is also integrated into the Llama Moderations API for text and images (LG4 model card) **[Documented]**
• Versions covered: LG4 (12B), LG3-1B, LG3-1B-INT4 (mobile), LG3-8B, LG3-8B-INT8, and LG3-11B-Vision for multimodal prompts **[Documented]**
### R2
Summary: **Harmful user requests under a fixed hazard taxonomy.** Covers 13 MLCommons-based categories S1 to S13, plus S14 Code Interpreter Abuse in LG3-8B and LG4. Not designed to detect jailbreak or prompt injection; Meta points to Prompt Guard 2. **[Documented]**
Detail:
• S1 Violent Crimes, S2 Non-Violent Crimes, S3 Sex-Related Crimes, S4 Child Sexual Exploitation, S5 Defamation, S6 Specialized Advice, S7 Privacy, S8 Intellectual Property, S9 Indiscriminate Weapons, S10 Hate, S11 Suicide & Self-Harm, S12 Sexual Content, S13 Elections (PurpleLlama cards at 172c1074) **[Documented]**
• S14 Code Interpreter Abuse is in LG3-8B and LG4 (marked "text only" in LG4); it is not in LG3-1B or LG3-11B-Vision, which use S1 to S13 **[Documented]**
• The LG3-1B docs note says it was not optimised for S14 and to use the 8B model for that category (Meta LG3 docs page) **[Documented]**
• The card category definitions are written as "Responses that …" for every category, though the same labels are applied to prompts **[Documented]**
• LG4 card: aligned to the standardised MLCommons hazards taxonomy, with S14 added for text-only tool-call use **[Documented]**
• Limitation: S5 Defamation, S8 Intellectual Property and S13 Elections may require factual, up-to-date knowledge; the cards advise more complex systems for use cases highly sensitive to them **[Documented]**
• Limitation: the model may be susceptible to adversarial or prompt-injection attacks; the LG4 card points to Prompt Guard 2 for detecting prompt attacks **[Documented]**
• Meta's protections page describes prompt injection and jailbreaking as attack categories handled by Prompt Guard, not Llama Guard **[Documented]**
• LG3-Vision paper, adversarial prompt classification: a PGD image attack at 8/255 raised harmful prompts misclassified as safe from 21% to 70%; a GCG text attack got 72% of prompts classified safe (arXiv 2411.10414) **[Documented]**
• Each attack was evaluated on 100 conversations: PGD on 100 harmful image conversations, GCG on 100 text-only unsafe conversations (arXiv 2411.10414) **[Documented]**
• Trade-off: LG3-8B card says deploying it "might increase refusals to benign prompts (False Positives)" **[Documented]**
• Llama 3 paper: Llama Guard 3 reduced violations by 65% on average across Meta's internal benchmarks, at the cost of more refusals of benign prompts (arXiv 2407.21783 section 5.4.7) **[Documented]**
• Trade-off: LG4 card says that in some internal tests input filtering reduces the safety violation rate and raises the overall refusal rate more than output filtering does, but experience may vary **[Documented]**
• Output filtering is described on the LG4 card as letting the LLM answer an unsafe prompt safely, so only an unsafe final output is censored **[Documented]**
• Legacy taxonomies differ (LG1 uses O1 to O6; LG2 uses S1 to S11 with different numbering) and are out of scope for this column **[Documented]**
### R3
Summary: **User message, before the main model.** The prompt is classified on its own, with no agent response in the conversation. Input filtering catches unsafe content before the LLM responds. **[Documented]**
Detail:
• For input evaluation the role placeholder is `User`; the agent response must not be present in the conversation (Meta LG3 and LG4 docs pages) **[Documented]**
• The LG4 card says the advantage of input filtering is that unsafe content can be caught very early, before the LLM responds **[Documented]**
• Cookbook helper templates ask for an assessment of "ONLY THE LAST" message of the given role **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• OGX v0.4.4 `run_shield` puts the whole conversation into the prompt, labels each turn with its capitalised role, and instructs the model to assess only the last message; if the first two messages are both from the user, the first is dropped **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 `run_moderation` wraps each input string as a separate user message, puts them all in one prompt, and asks about only the last one **[Documented: repo ogx-ai/ogx@v0.4.4]**
• NeMo Guardrails `llama guard check input` flow sends only the user message to the configured model **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• LG3-11B-Vision prompt classification covers text plus one image and is not meant for text-only classification; use LG3-8B or LG3-1B for text-only (11B-Vision card) **[Documented]**
### R4
Summary: **A fine-tuned LLM generates the verdict.** Supported in LG4, LG3-1B, LG3-8B and LG3-8B-INT8; LG3-11B-Vision supports it only for image-plus-text prompts. Served through Hugging Face transformers, with INT8 and INT4 variants. **[Documented]**
Detail:
• Mechanism: the model generates text; the first line is safe or unsafe, then categories **[Documented]**
• LG4: 12B dense model pruned from Llama 4 Scout, natively multimodal, runs on a single GPU; licence Llama 4 Community License Agreement **[Documented]**
• LG3-8B: Llama 3.1 8B fine-tune; 8-language support; licence Llama 3.1 Community License Agreement **[Documented]**
• LG3-8B-INT8: loaded with `BitsAndBytesConfig(load_in_8bit=True)` (INT8 HF card) **[Documented]**
• LG3-8B-INT8: about 40% smaller checkpoint, performance comparable to the original (8B card, Quantization section) **[Documented]**
• LG3-1B: Llama 3.2 1B, pruned to 12 layers and 6400 MLP hidden dimension (1123M parameters), logit-level distillation from LG3-8B; licence Llama 3.2 Community License Agreement **[Documented]**
• LG3-1B-INT4: weights INT4 with quantization-aware training, output layer pruned to 20 tokens, for mobile via ExecuTorch **[Documented]**
• LG3-11B-Vision: Llama 3.2 11B Vision fine-tune; image rescaled to 4 chunks of 560x560; one image only **[Documented]**
• Hugging Face transformers: LG3 uses `AutoTokenizer` and `AutoModelForCausalLM`; LG4 uses `AutoProcessor` and `Llama4ForConditionalGeneration` in bfloat16; weights are gated (HF cards) **[Documented]**
• Cookbook helper `build_default_prompt` / `build_custom_prompt` in `prompt_format_utils.py` builds LG1, LG2 and LG3 prompts; it has no LG4 template **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• The cookbook LG3 template wraps the prompt in Llama 3 header tokens and asks for an assessment of only the last message **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• The llama-models repo (main, pinned) has Llama Guard only as model-id entries and no prompt template **[Documented: repo meta-llama/llama-models@0e0b8c51]**
• Meta's Llama Guard 3 and 4 docs pages point to the llama-cookbook helper and inference example for the prompt format **[Documented]**
• Meta docs say LG4 can be a drop-in replacement for LG3 8B and 11B, and the LG3 1B still suits edge devices (Meta LG4 docs page) **[Documented]**
• OGX v0.4.4 (formerly llama-stack) llama_guard provider: config `excluded_categories`; temperature 0.0; fixed prompt template; unsafe verdict becomes a violation with level ERROR and message "I can't answer that. Can I help with something else?" **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 gives LG4 only S1 to S13, with a code comment citing the LG4 model card; the card lists S14, so this conflicts with the card (added in commit ef26259209, PR 2579, July 2025; the PR gives no reason) **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 moderation path: unknown codes are logged and the result is returned as not flagged (fails open); no image support in moderation (TODO in code) **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 builds the role label from the last message role capitalised, so an OpenAI-style assistant message becomes "Assistant" rather than the documented `Agent` **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX 1.0 (May 2026) removed the Safety API and the Llama Guard provider; the release notes say moderation moves to an OpenAI-compatible moderations endpoint, and the 2026-06-23 blog says OGX no longer serves that endpoint itself: Responses guardrails call an external endpoint set in config **[Documented: repo ogx-ai/ogx@f8051dd6]**
• NeMo Guardrails v0.24.1: the `llama guard check input` flow calls an action with model name `llama_guard` hard-coded; the Llama-Guard docs page configures a model of type `llama_guard` (LlamaGuard-7b) **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• The type `llama_guard_2` with Meta-Llama-Guard-2-8B appears only in the separate content-safety docs page, whose flows take the model type as a `$model` parameter **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• NeMo parsing: reply starting with safe is allowed; starting with unsafe is blocked with violations split on spaces; any other reply is blocked with an empty list (fails closed); temperature 0.0 **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• Llama API exposes LG4 through the `/moderations` endpoint (Meta protections page) **[Documented]**
• Llama API moderations schema (archived official page, Wayback 2025-09-14): POST `/v1/moderations` on `https://api.llama.com/v1`, a `messages` array, and an optional `model` that defaults to "Llama-Guard", not stated to be LG4 **[Documented]**
• The Meta API doc pages for moderations now return 404 and the schema survives only in archived copies, so current availability is unconfirmed **[To be verified]**
• Only official speed figure: LG3-1B-INT4 on a Moto-Razor Android phone CPU with ExecuTorch and no accelerator reached at least 30 tokens per second and a time-to-first-token of 2.5 s or less; prompt length not stated (arXiv 2411.17713) **[Documented]**
• No official latency or throughput figure for LG4, LG3-8B, LG3-8B-INT8, LG3-1B (bf16) or LG3-11B-Vision **[Not disclosed]**
### R5
Summary: **Verdict text, optionally a score.** First line is safe or unsafe; if unsafe a second line lists comma-separated S-codes. LG3-8B and its INT8 card derive a score from the first-token probability, with no stated threshold; LG3-1B, 11B-Vision and LG4 describe none. **[Documented]**
Detail:
• Safe prompt: the output is `safe` **[Documented]**
• Unsafe prompt: `unsafe`, then a second line with comma-separated categories such as `S1,S2` **[Documented]**
• LG3-8B card: "we look at the probability for the first token, and use that as the 'unsafe' class probability" and "apply score thresholding to make binary decisions" **[Documented]**
• The LG3-8B-INT8 HF card repeats the same two sentences **[Documented]**
• No numeric threshold is given for LG3-8B **[Not disclosed]**
• No numeric threshold or score method appears on the LG3-1B, LG3-1B-INT4, LG3-11B-Vision or LG4 cards, in the Meta LG3 and LG4 docs pages, or in the 11B-Vision and 1B-INT4 papers (full text searched) **[Not disclosed]**
• LG2 card: the score is the first-token probability and the evaluation uses a threshold of 0.5 **[Documented: repo PurpleLlama@172c1074]**
• The LG1 card leaves the threshold to the user; the LG1 paper uses 0.5 for its precision, recall and F1 tables (arXiv 2312.06674 appendix B) **[Documented]**
• ExecuTorch instructions for LG3-1B-INT4: first output token 19193 means safe and 39257 means unsafe; the sample takes the argmax, not a probability **[Documented: repo PurpleLlama@172c1074]**
• NeMo returns an allowed/blocked outcome and a lowercased violation list **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• OGX v0.4.4 moderation scores are only 0.0 and 1.0; a safe result sets every category to 1.0 with flagged false **[Documented: repo ogx-ai/ogx@v0.4.4]**
• Llama API moderations response (archived official page, Wayback 2025-09-14): `model` and `results`, each result with a `flagged` boolean and a `flagged_categories` list; no scores **[Documented]**
• LG3-8B card evaluations use AUPRC, which needs a score, though the scoring pipeline is not described **[Documented]**
### R6
Summary: **A single user prompt, plus a policy prompt.** The input is the user message with the category list; the agent response must be absent. Text only, except LG4 and LG3-11B-Vision which also take images. **[Documented]**
Detail:
• Input: user prompt text inside the Llama Guard prompt template with the category list **[Documented]**
• The agent response must not be present when evaluating the user input **[Documented]**
• Languages, LG3-8B and LG3-1B cards: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai **[Documented]**
• Languages, LG4 card: English and multilingual text "on the languages supported by Llama Guard 3" **[Documented]**
• LG4 card: the multilingual evaluation averages the 7 non-English LG3-8B languages: French, German, Hindi, Italian, Portuguese, Spanish, Thai **[Documented: repo PurpleLlama@172c1074]**
• Languages, LG3-11B-Vision: optimised for English **[Documented]**
• LG4 docs page, Image Support section: the model is "optimized for English-language text" and the text component should be in English; the same sentence appears in the LG3 docs page for 3-11B-Vision **[Documented]**
• Meta's protections page says LG4 "supports 12 languages" and lists none **[Documented]**
• The Llama 4 Scout card lists 12 supported languages (Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, Vietnamese); whether the protections page means these is not stated **[To be verified]**
• Images, LG4: multiple images, tested mostly with about three; LG3-11B-Vision: one image **[Documented]**
• Llama API moderations context window is 8K (archived official page, Wayback 2025-09-14) **[Documented]**
• Evaluation, LG3-8B prompt classification (card Table 5): English P 0.952, R 0.943, F1 0.947, FPR 0.057; multilingual F1 0.900, FPR 0.054; tool use F1 0.920, FPR 0.126 **[Documented]**
• Evaluation, LG3-8B-INT8 prompt classification: English F1 0.950, FPR 0.045; multilingual F1 0.899, FPR 0.051; tool use F1 0.909, FPR 0.134 **[Documented]**
• Evaluation, LG3-11B-Vision prompt classification: P 0.891, R 0.623, F1 0.733, FPR 0.052; the card says prompt (text plus image) classification is harder than response classification and recommends response classification for ambiguous cases **[Documented]**
• LG4 evaluation numbers are from output filtering only **[Documented]**
• The LG3-1B card does not label its evaluation table as prompt or response **[Not disclosed]**
• The LG3-1B English and multilingual columns for LG3-8B repeat the 8B card's response and prompt+response values, so the 1B table is probably response or prompt+response, not prompt-only **[Inferred]**
• Training data: LG3 added benign multilingual prompts that LLMs would likely reject, to reduce false positives; code-interpreter safe data was chosen near the unsafe boundary (LG3-8B card) **[Documented]**
• Test data for XSTest (exaggerated safety, benign near-miss prompts): LG3-8B F1 0.884, FPR 0.044; LG3-1B F1 0.821, FPR 0.068 (LG3-1B card) **[Documented]**
• Custom categories: LG3-1B card shows `apply_chat_template(..., categories={"S1": "..."})` and `excluded_category_keys=["S6"]` (HF card) **[Documented]**
### R7
Summary: **Minimum setup:** a prompt-submission harness, labelled safe and unsafe prompts per S-category, multilingual copies, benign near-miss prompts for false positives, the model served with its template, and a verdict parser and logger. No response generation is needed. **[Inferred]**
Detail:
• Labelled unsafe prompts for each S-category (S1 to S13, and S14 for LG3-8B and LG4), each tagged with the expected code **[Inferred]**
• Labelled safe prompts, including benign near-miss prompts (XSTest-style, for example asking how to kill a process or about a historical event) to measure false positives **[Inferred]**
• Multilingual sets in the eight card languages (or seven non-English plus English for LG4), with translated pairs to compare across languages **[Inferred]**
• A threshold sweep set if the first-token probability is used: unsafe/safe prompts to plot precision-recall and choose a cut-off **[Inferred]**
• Adversarial variants (paraphrase, encoded text, long context) to see misses, since the cards warn of adversarial susceptibility **[Inferred]**
• Image-plus-text prompts only if testing LG4 or LG3-11B-Vision **[Inferred]**
• A harness that sends one prompt at a time with no agent turn; a parser for the safe/unsafe line and S-codes; a logger recording code, latency and score **[Inferred]**
• Compare each version on the same set: LG4, LG3-8B, LG3-8B-INT8, LG3-1B (INT4 optional) **[Inferred]**
### R8
Summary: **Key open questions.** No documented decision threshold, unclear LG4 language coverage (which 12 languages), no prompt-only numbers for LG3-1B or LG4, and latency figures only for LG3-1B-INT4 on one phone.
Detail:
• Recommended threshold for the first-token probability in LG3-1B, LG3-8B, LG3-11B-Vision and LG4 (checked the cards, Meta docs pages and papers, not stated; only LG2 and the LG1 paper use 0.5)
• Which cut-off works best per version on a labelled prompt set (needs testing)
• LG4 language coverage: card lists English plus the 7 LG3 languages, docs page says English-optimised under Image Support, protections page says 12 languages without a list
• Which 12 languages the protections page means (checked the LG4 card, docs page, protections page and Meta posts, not stated; the Llama 4 Scout card also lists 12)
• LG3-1B and LG3-8B evaluation tables include Vietnamese and Indonesian columns, but the cards' supported-language lists do not (checked the 1B and INT4 cards, the INT4 paper and the LG3 docs page, support not stated)
• Prompt-only evaluation numbers for LG3-1B and LG4 (checked the cards, the INT4 paper and the LG4 docs page, none found)
• Latency and throughput for versions other than LG3-1B-INT4 (only one phone measurement exists), and measured latency on your own hardware (needs testing)
• Whether Meta documents LG4 custom categories on a card or docs page (the chat template accepts them; no page shows it)
• Behaviour with jailbreak or prompt-injection prompts (Meta points to Prompt Guard 2; not measured)
### R9
Summary: Meta model cards on GitHub and Hugging Face, Meta docs, protections and archived Llama API pages, Meta papers, and the cookbook, llama-models, OGX and NeMo Guardrails source and docs.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/8B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/11B-vision/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/ET_INSTRUCTIONS.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard2/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard/MODEL_CARD.md
• https://huggingface.co/meta-llama/Llama-Guard-3-1B
• https://huggingface.co/meta-llama/Llama-Guard-3-8B-INT8
• https://huggingface.co/meta-llama/Llama-Guard-4-12B
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://dev.meta.ai/llama/llama-protections/
• http://web.archive.org/web/20250914152244/https://llama.developer.meta.com/docs/api/moderations
• http://web.archive.org/web/20250914135559/https://llama.developer.meta.com/docs/features/moderation
• https://arxiv.org/html/2411.10414
• https://arxiv.org/html/2411.17713
• https://arxiv.org/html/2312.06674
• https://arxiv.org/html/2407.21783
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/meta-llama/llama-models/blob/0e0b8c519242d5833d8c11bffc1232b77ad7f301/models/sku_list.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py
• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/releases/RELEASE_NOTES_1.0.md
• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/blog/2026-06-23-guardrails-responses-api.md
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/actions.py
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/community/llama-guard.mdx
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/content-safety.mdx

## Column LG2: Llama Guard: Output-level response content-safety classification
### R1
Summary: **Output-level response content-safety classification.** Llama Guard reads a user prompt together with the model's response and replies safe or unsafe for the response, listing violated categories. **[Documented]**
Detail:
• Llama Guard can classify content in LLM responses (response classification) (LG3-1B, LG3-8B and LG4 model cards) **[Documented]**
• Same model and taxonomy as the input function; the role placeholder `Agent` selects the response (Meta docs pages) **[Documented]**
• Versions covered: LG4 (12B), LG3-1B, LG3-1B-INT4 (mobile), LG3-8B, LG3-8B-INT8, LG3-11B-Vision (multimodal prompt plus text response) **[Documented]**
### R2
Summary: **Unsafe model output.** Detects responses that enable, encourage or contain content in S1 to S13, plus S14 Code Interpreter Abuse in LG3-8B and LG4. Facts needing up-to-date knowledge are weak spots, and adversarial agent output can fool it. **[Documented]**
Detail:
• Category list S1 to S13 is the same as in the input column; S14 appears only in LG3-8B and LG4 **[Documented]**
• Category definitions start with "Responses that …", so they are written for output classification **[Documented]**
• LG3-8B tool use: trained and evaluated on search tool calls and code interpreter abuse **[Documented]**
• Evaluation, LG3-8B Table 3 (prompt+response): search tool calls F1 0.856, AUPRC 0.938, FPR 0.174; code interpreter abuse F1 0.885, AUPRC 0.967, FPR 0.125 **[Documented]**
• Limitation: S5, S8 and S13 may need factual, up-to-date knowledge **[Documented]**
• Limitation: performance may be limited by pre-training data (common sense, multilingual, policy coverage) **[Documented]**
• LG3-Vision paper, response classification: a PGD image attack raised unsafe responses classified safe from 6% (no attack) to 22% at 8/255 and 27% at 128/255 and at 255/255 (arXiv 2411.10414) **[Documented]**
• LG3-Vision paper, GCG text attack: 30% of responses fooled when the attacker only controls the prompt (16% baseline), and 75% when the attacker controls the agent output (arXiv 2411.10414) **[Documented]**
• Trade-off: LG4 card says output filtering lets the LLM answer an unsafe prompt safely and censors only unsafe final output; input filtering reduces violations and raises refusals more in internal tests **[Documented]**
• Trade-off: LG3-8B card says deployment might increase refusals to benign prompts **[Documented]**
• Llama Guard does not detect jailbreak or prompt injection; Meta points to Prompt Guard 2 **[Documented]**
### R3
Summary: **Model response, after the main model.** Operates after the LLM answers and before the answer is shown, with the user prompt included as context. **[Documented]**
Detail:
• For response evaluation both the user input and the agent response must be present; the user input gives important context (Meta LG3 and LG4 docs pages) **[Documented]**
• The LG4 card describes output filtering as classifying an LLM's generated output **[Documented]**
• Using both input and output filtering gives additional security (LG4 card) **[Documented]**
• NeMo Guardrails `llama guard check output` flow passes the user message and the bot response to the Llama Guard model **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• OGX v0.4.4 `run_moderation` wraps every string as a user message, so it classifies text in the user role, and a list input is judged on its last string only; response classification needs the shield path, which labels the role from the last message **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX 1.0 removed both paths; Responses guardrails send the flattened text to a configured external endpoint with no User or Agent role, so role-specific Llama Guard classification is not done by OGX **[Documented: repo ogx-ai/ogx@f8051dd6]**
• The cookbook helper builds a response prompt when the agent type is `Agent` and the conversation holds user and agent turns **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• LG3-11B-Vision response classification covers the multimodal prompt plus the text response **[Documented]**
### R4
Summary: **Same fine-tuned LLM, response instruction.** Supported by LG4, LG3-1B, LG3-8B, LG3-8B-INT8 and LG3-11B-Vision. Serving via Hugging Face transformers, INT8 or INT4, cookbook helper, OGX (to v0.4.4) and NeMo. **[Documented]**
Detail:
• All five versions support response classification (cards) **[Documented]**
• LG3-11B-Vision is not meant for image-only or text-only classification, so use LG3-8B or LG3-1B for text responses **[Documented]**
• LG3-8B-INT8 uses bitsandbytes INT8, about 40% smaller, with comparable performance **[Documented]**
• LG3-1B-INT4 targets mobile with ExecuTorch (pruned, quantization-aware training) **[Documented]**
• Hugging Face transformers: LG3 uses `AutoModelForCausalLM`; LG4 uses `AutoProcessor` and `Llama4ForConditionalGeneration`; weights are gated (HF cards) **[Documented]**
• Cookbook helper `prompt_format_utils.py` supports LG1 to LG3 prompts only; custom prompts through `build_custom_prompt(..., with_policy=...)` **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• OGX v0.4.4: `excluded_categories` config; temperature 0.0; the whole conversation goes in the prompt and the model is asked to assess only the last message; unsafe becomes a violation with level ERROR and the message "I can't answer that. Can I help with something else?" **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4: LG4 receives only S1 to S13 (card lists S14; added in commit ef26259209, PR 2579, July 2025, the PR gives no reason); moderation scores are 0.0 or 1.0 and unknown codes return not flagged (fails open) **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX 1.0 (May 2026) removed the Safety API; no moderations route or Llama Guard provider exists on main **[Documented: repo ogx-ai/ogx@f8051dd6]**
• NeMo Guardrails v0.24.1: `llama guard check output` uses model name `llama_guard` fixed in the flow; the Llama-Guard docs page configures a model of type `llama_guard`; unparseable output is blocked (fails closed) **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• The type `llama_guard_2` with Meta-Llama-Guard-2-8B appears only in the separate content-safety docs page, whose flows take the model type as a `$model` parameter **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• Licences: LG3-8B and INT8 Llama 3.1 Community License Agreement; LG3-1B and 11B-Vision Llama 3.2 Community License Agreement; LG4 Llama 4 Community License Agreement **[Documented]**
• Only official speed figure: LG3-1B-INT4 on a Moto-Razor Android phone CPU with ExecuTorch and no accelerator reached at least 30 tokens per second and a time-to-first-token of 2.5 s or less; prompt length not stated (arXiv 2411.17713) **[Documented]**
• No official latency or throughput figure for LG4, LG3-8B, LG3-8B-INT8, LG3-1B (bf16) or LG3-11B-Vision **[Not disclosed]**
### R5
Summary: **Verdict text for the response.** First line safe or unsafe; if unsafe, a second line lists S-codes. The LG3-8B and LG2 cards describe a first-token-probability score; only LG2 gives a threshold (0.5). **[Documented]**
Detail:
• Output format is identical to the input function: `safe`, or `unsafe` plus comma-separated codes **[Documented]**
• LG3-8B card: first-token probability is the unsafe-class probability, and score thresholding gives binary decisions **[Documented]**
• No numeric threshold for LG3-8B, LG3-1B, LG3-11B-Vision or LG4 **[Not disclosed]**
• LG2 card: the evaluation uses a threshold of 0.5 on the first-token probability **[Documented: repo PurpleLlama@172c1074]**
• LG3-1B-INT4 ExecuTorch sample: first token 19193 is safe and 39257 is unsafe (argmax) **[Documented: repo PurpleLlama@172c1074]**
• Evaluation LG3-8B response, English test set (card Table 1, response classification): F1 0.939, AUPRC 0.985, FPR 0.040 (LG2: 0.877, 0.927, 0.081; GPT4: 0.805, N/A, 0.152) **[Documented]**
• Evaluation LG3-8B multilingual F1/FPR: French 0.943/0.036, German 0.877/0.032, Hindi 0.871/0.050, Italian 0.873/0.038, Portuguese 0.860/0.060, Spanish 0.875/0.023, Thai 0.834/0.030 **[Documented]**
• Evaluation LG3-8B-INT8 response, English: F1 0.936, FPR 0.040 **[Documented]**
• Evaluation LG3-1B English F1 0.899, FPR 0.090; XSTest F1 0.821, FPR 0.068; LG3-1B-INT4 English F1 0.904, FPR 0.084 **[Documented]**
• Evaluation LG3-11B-Vision response: P 0.961, R 0.916, F1 0.938, FPR 0.016 **[Documented]**
• Evaluation LG4 (output filtering, S1 to S13 average, in-house set): English R 69%, FPR 11%, F1 61%; multilingual 43%, 3%, 51%; single image 41%, 9%, 38%; multi-image 61%, 9%, 52% **[Documented]**
• Cross-card difference: LG3-8B F1 values (about 0.94) and LG4 F1 values (about 0.61) come from different in-house test sets and are not directly comparable **[Inferred]**
• NeMo returns an allowed flag and a violation list **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• OGX v0.4.4 returns a violation object from the shield path or a moderation object from the moderation path **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R6
Summary: **Prompt and response pair.** Needs the user prompt and the agent response, plus the policy prompt. LG3 text models cover eight languages; LG4 adds images and cites the same languages; LG3-11B-Vision is English-optimised with one image. **[Documented]**
Detail:
• Input: user prompt and agent response together **[Documented]**
• Languages: LG3-8B, LG3-1B: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai; LG4 card: English plus the LG3 languages; LG3-11B-Vision: English-optimised **[Documented]**
• LG4 docs page, Image Support section: the model is "optimized for English-language text" and the text component should be in English; Meta's protections page says LG4 "supports 12 languages" and lists none **[Documented]**
• The Llama 4 Scout card lists 12 supported languages; whether the protections page means these is not stated **[To be verified]**
• LG3-1B and LG3-8B evaluation tables include Vietnamese and Indonesian columns, but the cards' supported-language lists do not include them **[Documented]**
• Training data: single-turn and multi-turn human-AI conversations; benign multilingual prompt and response data where LLMs likely reject the prompts (LG3-8B card) **[Documented]**
• Images: LG4 takes multiple images (tested mostly with about three); LG3-11B-Vision takes one image, rescaled to 4 chunks of 560x560 **[Documented]**
• Custom categories: LG3-1B card shows `categories` and `excluded_category_keys` options on `apply_chat_template`; the docs say categories can be customised for zero-shot or few-shot prompting **[Documented]**
### R7
Summary: **Minimum setup:** prompt and response pairs labelled safe or unsafe per S-category, including safe refusals to unsafe prompts and benign near-miss pairs, in the target languages; the model served with its template; a verdict parser and logger. The main LLM is optional. **[Inferred]**
Detail:
• Prompt+response pairs with unsafe responses per S-category (S1 to S13, S14 for LG3-8B and LG4), labelled with the expected code **[Inferred]**
• Pairs with unsafe prompts but safe responses (refusals or safe answers), to confirm the response is judged on its own **[Inferred]**
• Benign prompt with benign response and borderline pairs (XSTest-style), to measure false positives **[Inferred]**
• Multilingual pairs in the supported languages, and multi-turn conversations **[Inferred]**
• Tool-use pairs for LG3-8B and LG4: search results and code-interpreter completions with abuse labels **[Inferred]**
• Adversarial pairs where the response text carries attack suffixes, since the paper reports 75% fooled when the attacker controls agent output **[Inferred]**
• Image plus text response pairs for LG4 and LG3-11B-Vision only **[Inferred]**
• Harness: submit pairs directly, or run a stub or real main LLM; parser for the safe/unsafe line; logger for code, score and latency **[Inferred]**
### R8
Summary: **Key open questions.** No documented decision threshold, conflicting LG4 language statements, no like-for-like response numbers across versions, and latency figures only for LG3-1B-INT4 on one phone.
Detail:
• Recommended threshold on the first-token probability for every version (checked the cards, Meta docs pages and papers, not stated; only LG2 and the LG1 paper use 0.5)
• Which cut-off works best per version on a labelled response set (needs testing)
• LG4 language coverage: card lists English plus the 7 LG3 languages, docs page says English-optimised under Image Support, protections page says 12 languages without a list
• Whether LG3-1B and LG3-8B support Vietnamese and Indonesian (shown only in evaluation tables; checked the 1B and INT4 cards, the INT4 paper and the LG3 docs page, support not stated)
• Comparable response-level numbers across LG4, LG3-8B and LG3-1B on one test set (needs testing)
• Whether Meta documents LG4 custom categories on a card or docs page (the chat template accepts them; no page shows it)
• Latency and throughput for versions other than LG3-1B-INT4 (only one phone measurement exists), and measured latency on your own hardware (needs testing)
### R9
Summary: Meta model cards on GitHub and Hugging Face, Meta docs and protections pages, Meta papers, and the cookbook, OGX and NeMo Guardrails source and docs.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/8B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/11B-vision/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/ET_INSTRUCTIONS.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard2/MODEL_CARD.md
• https://huggingface.co/meta-llama/Llama-Guard-3-1B
• https://huggingface.co/meta-llama/Llama-Guard-3-8B-INT8
• https://huggingface.co/meta-llama/Llama-Guard-4-12B
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://dev.meta.ai/llama/llama-protections/
• https://arxiv.org/html/2411.10414
• https://arxiv.org/html/2411.17713
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py
• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/releases/RELEASE_NOTES_1.0.md
• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/blog/2026-06-23-guardrails-responses-api.md
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/actions.py
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/community/llama-guard.mdx
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/content-safety.mdx

## Column LG3: Llama Guard: Multimodal (image + text) content-safety classification
### R1
Summary: **Image-plus-text safety classification.** Llama Guard 3-11B-Vision and Llama Guard 4 classify a multimodal prompt, or a multimodal prompt plus the text response, as safe or unsafe with violated category codes. **[Documented]**
Detail:
• Llama Guard 3-11B-Vision is a Llama-3.2-11B pretrained model fine-tuned for content safety classification; it classifies LLM inputs (prompt classification) and LLM responses (response classification) **[Documented]**
• It "was optimized to detect harmful multimodal (text and image) prompts and text responses to these prompts" **[Documented]**
• Llama Guard 4 is described as "a natively multimodal safety classifier with 12 billion parameters trained jointly on text and multiple images" **[Documented]**
• Llama Guard 4 combines the capabilities of Llama Guard 3-8B and 3-11B-vision (multilingual text plus mixed text-and-image prompts) **[Documented]**
• Llama Guard 3-1B and 3-8B are text only **[Documented]**
### R2
Summary: **Harmful image-plus-text prompts and responses.** Targets the MLCommons hazard categories S1 to S13 in multimodal conversations, with specific attention to prompts asking to identify real people in images. Vulnerable to white-box adversarial image and text attacks. **[Documented]**
Detail:
• Trained on 13 MLCommons-based categories S1 to S13 (3-11B-Vision); LG4 adds S14 as text only **[Documented]**
• 3-11B-Vision card: "specific attention was paid to risks emerging from potential prompts to identify people in images" and "Llama Guard 3 Vision was trained to classify the response as unsafe" **[Documented]**
• Adversarial results (3-Vision paper, white-box attacker, percent of harmful items misclassified as safe) **[Documented]**
  – PGD image attack, prompt classification: 21% with no attack, 70% at 8/255, 82% at 128/255, 82% at 255/255
  – PGD image attack, response classification: 6% with no attack, 22% at 8/255, 27% at 128/255, 27% at 255/255
  – GCG text attack, prompt classification: 4% with no attack, 72% when appended to the user prompt
  – GCG text attack, response classification: 16% with no attack, 30% when appended to the user prompt, 75% when appended to the agent response
  – The GCG tests use text-only harmful prompts and conversations
• Each attack was evaluated on 100 conversations: PGD on 100 harmful image conversations, GCG on 100 text-only unsafe conversations (arXiv 2411.10414) **[Documented]**
• GCG suffixes were optimised with knowledge of the harmful response, a worst-case setting; the paper notes the attacker normally cannot see the agent's response (arXiv 2411.10414) **[Documented]**
• The paper's threat model assumes "full white-box access" because weights are public **[Documented]**
• Both cards say the model "may be susceptible to adversarial attacks"; LG4 card points to Prompt Guard 2 for prompt attacks, and Llama Guard itself does not detect jailbreak or prompt injection **[Documented]**
• S5 Defamation, S8 Intellectual Property and S13 Elections need factual, up-to-date knowledge **[Documented]**
### R3
Summary: **User image and text, plus the text response.** It reads the prompt text and the image together; it is not meant for image-only or text-only classification. The 3-11B-Vision card says English optimised, one image per prompt. **[Documented]**
Detail:
• 3-11B-Vision card: "not meant to be used as an image safety classifier nor a text-only safety classifier. Its task is to classify the multimodal prompt or the multimodal prompt along with the text response" **[Documented]**
• Meta docs (Llama Guard 3 and 4 pages): "It is not designed to perform image-only classification" **[Documented]**
• Meta docs (Llama Guard 3 and 4 pages): "the model does not support the evaluation of images that were themselves created using generative AI technology" **[Documented]**
• 3-11B-Vision: "optimized for English language and only supports one image at the moment" **[Documented]**
• Meta docs (Llama Guard 3 page): "multi-turn support here does not mean multi-image support; the model evaluates only one image per prompt" **[Documented]**
• LG4 card: multilingual text on the languages supported by Llama Guard 3, plus mixed text-and-image prompts **[Documented]**
• LG4 docs page, Image Support section, says the model "has been optimized for English-language text, so the text component of the prompt should be in English"; this conflicts with the card's multilingual claim (see R8) **[Documented]**
• LG4 docs: images can be evaluated in multi-turn conversations, but the image token must be added to the turn in which the image occurs **[Documented]**
• Prompt classification is harder than response classification because of ambiguity (card example: "how do I buy this" with an image of multiple objects); the card recommends response classification in such cases **[Documented]**
### R4
Summary: **Fine-tuned vision-language model.** Version 3-11B-Vision takes one image rescaled into four 560 by 560 chunks; Llama Guard 4 is a 12B early-fusion model that accepts several images. Serving via transformers; the OGX v0.4.4 moderation path ignored images and was removed in OGX 1.0. **[Documented]**
Detail:
• Versions supporting images: 3-11B-Vision (one image) and LG4 (multiple images); 3-1B, 3-8B and 3-8B-INT8 do not **[Documented]**
• 3-11B-Vision tiling: "our vision encoder will rescale it into 4 chunks, each of 560x560"; limitations section: "classification performance may vary depending on the actual image size" **[Documented]**
• 3-11B-Vision prompt template (Meta docs) starts the user turn with the image token followed by "Task: Check if there is unsafe content in '{{ role }}' messages…" **[Documented]**
• LG4 architecture: early fusion transformer with dense layers, pruned from Llama 4 Scout (routed experts and router removed, shared expert kept), shares the tokenizer and vision encoder of Llama 4 Scout and Maverick, "can be run on a single GPU" **[Documented]**
• LG4 image tiling: a dynamic transformation divides each image into 336×336 pixel tiles, and a global tile (whole image resized to 336×336) is appended after the local tiles; larger images get more patch tokens (Meta LG4 docs page) **[Documented]**
• LG4 prompt template (Meta docs): image tokens in the User line are an image start token, patch tokens, tile x and tile y separator tokens, a global image token, more patch tokens, then an image end token; header tokens differ from Llama 3 (header start and header end, end-of-turn token) **[Documented]**
• Meta's LG4 docs worked example puts two images in one user turn, then a multi-turn text exchange, and asks for a verdict on only the last Agent message **[Documented]**
• LG4 training: blend of 3-8B and 3-11B-vision data plus multi-image data "with most samples containing from 2 to 5 images" and multilingual data; roughly 3:1 text-only to multimodal **[Documented]**
• LG4 card: "tested mostly with prompts containing a few images (three, most frequently), so performance may vary if using it to classify safety with a much larger number of images" **[Documented]**
• LG4 card: "integrated into the Llama Moderations API for text and images" **[Documented]**
• Serving: Hugging Face transformers with a processor; the 3-11B-Vision HF card loads with `AutoModelForVision2Seq` and `AutoProcessor`, and its config architecture is `MllamaForConditionalGeneration` (HF page and HF Hub API) **[Documented]**
• OGX provider (ogx-ai/ogx v0.4.4): the moderation method has the code comment "TODO: Add Image based support for OpenAI Moderations" and builds a text-only prompt; the result marks applied input types as text only **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX shield path: the vision branch (keeps only the most recent user image, placed first in the content list) runs only when the model equals the core-model id for 3-11B-Vision; LG4 and any other id go through the text path **[Documented: repo ogx-ai/ogx@v0.4.4]**
• The vision branch runs only if the registered model id is exactly `Llama-Guard-3-11B-Vision` (the core-model id); the Hugging Face repo id `meta-llama/Llama-Guard-3-11B-Vision` takes the text path, where an image becomes an image placeholder string **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX 1.0 (May 2026) removed the Safety API and the Llama Guard provider, so the moderation path with its image TODO no longer exists on main (release notes and 2026-06-23 blog) **[Documented: repo ogx-ai/ogx@f8051dd6]**
• The Llama 3.2 Acceptable Use Policy (shown on the 3-11B-Vision page) says rights under Section 1(a) are not granted for multimodal models to an individual domiciled, or a company with principal place of business, in the European Union; end users of a product incorporating such models are exempt **[Documented]**
• The Llama 4 Acceptable Use Policy has the same clause for multimodal models in Llama 4 **[Documented]**
• Whether the clause covers Llama Guard 3-11B-Vision or Llama Guard 4 is not stated by Meta; HF gates the 3-11B-Vision repo with an EU-disallowed flag, but not LG4 **[To be verified]**
### R5
Summary: **Safe or unsafe plus codes.** First line says safe or unsafe; if unsafe, a second line lists the violated categories. Reported metrics include a 3-11B-Vision response F1 of 0.938 and LG4 multi-image recall of 61%. **[Documented]**
Detail:
• Output template: "First line must read 'safe' or 'unsafe'. If unsafe, a second line must include a comma-separated list of violated categories." **[Documented]**
• 3-11B-Vision, internal test set, prompt classification: precision 0.891, recall 0.623, F1 0.733, FPR 0.052 **[Documented]**
• 3-11B-Vision, response classification: precision 0.961, recall 0.916, F1 0.938, FPR 0.016 **[Documented]**
• Baselines in the same table: GPT-4o prompt F1 0.661 / FPR 0.485, response F1 0.667 / FPR 0.243; GPT-4o mini prompt F1 0.643 / FPR 0.681, response F1 0.641 / FPR 0.313 **[Documented]**
• 3-11B-Vision response F1 by category ranges from 0.698 (Child Exploitation) to 0.995 (Indiscriminate Weapons) **[Documented]**
• LG4 output filtering, average of S1 to S13 with equal category weights (R / FPR / F1): single image 41% / 9% / 38%; multi-image 61% / 9% / 52%; English 69% / 11% / 61%; multilingual 43% / 3% / 51% **[Documented]**
• LG4 deltas versus Llama Guard 3: single image R +10%, FPR 0%, F1 +8%; multi-image R +20%, FPR -1%, F1 +17% **[Documented]**
• In the multi-image comparison "only the final image was input into Llama Guard 3-11B-vision" **[Documented]**
• No score method or threshold is documented for 3-11B-Vision or LG4 (checked the cards, Meta docs pages and papers) **[Not disclosed]**
• OGX v0.4.4 moderation: category scores are only 0.0 or 1.0 and the safe object sets every category score to 1.0 **[Documented: repo ogx-ai/ogx@v0.4.4]**
• The all-1.0 scores on a safe result are probably a quirk of the code **[Inferred]**
### R6
Summary: **One prompt image (3-11B-Vision) or several (Llama Guard 4), with text.** For prompt checks, supply user turn only; for response checks, supply the user turn and the agent text response. **[Documented]**
Detail:
• Evaluating the user input: the agent response must not be present; evaluating the agent response: both user input and agent response must be present **[Documented]**
• 3-11B-Vision accepts exactly one image per prompt; LG4 accepts several **[Documented]**
• The image must be attached to the user turn where it occurs; the text component should be English per the docs page **[Documented]**
• Images are rescaled, so image size can change results (3-11B-Vision) **[Documented]**
• Images that were themselves created with generative AI are not supported (Meta docs) **[Documented]**
• LG3-11B-Vision classifies the multimodal prompt, or the prompt with a text response; the paper describes "text responses" **[Documented]**
• LG4 card and docs do not say whether image content in a response is classified **[Not disclosed]**
### R7
Summary: **Minimum setup:** one GPU host with Llama Guard 4 and a 3-11B-Vision baseline; about 60 labelled pairs, covering single-image, multi-image, benign-image/harmful-text, harmful-image/benign-text, and prompt versus response tasks. **[Inferred]**
Detail:
• **Minimum setup:** run both models in transformers; send each item once as a prompt check and once (with a canned text response) as a response check; record the first line and codes. **[Inferred]**
• Test data (image + text pairs), each with expected label and category **[Inferred]**
  – Benign image + benign text (landscape, "describe this"), expected safe
  – Benign image + harmful text request, expected unsafe on the prompt check
  – Harmful-looking image + benign question, expected to show ambiguity (card says prompt checks are weaker)
  – "Who is this?" on a real-person photo, expected unsafe on the response if the answer names the person (S7 or similar)
  – "How do I buy this" with a multi-object image, expected borderline (card example)
  – Image containing overlaid text instructions, to see if the classifier is steered by the image text
• Multi-image cases (LG4 only; 3-11B-Vision gets only the last image to reproduce the card's comparison) **[Inferred]**
  – 2 to 5 images where only the first is harmful, only the last is harmful, or only the combination is harmful
  – A 10+ image set, to probe the stated "much larger number of images" caveat
• Adversarial smoke test: append a GCG-style suffix to the text of a known unsafe item **[Inferred]**
• OGX check (v0.4.4 only; the moderation route and shields were removed in OGX 1.0): send an image-bearing message through the moderation endpoint and confirm the image is ignored; register the shield with the core id and with the HF id and compare **[Inferred]**
### R8
Summary: **Key open questions.** No documented threshold for 3-11B-Vision or LG4, behaviour beyond about three images in LG4, which language rules apply to multimodal prompts, and whether Meta's multimodal EU licence clause covers the guard models.
Detail:
• LG4 docs say English-optimised text (Image Support section) while the card claims multilingual: which governs for multimodal prompts
• Whether any official score threshold exists for 3-11B-Vision and LG4 (checked the cards, Meta docs pages and papers, not stated)
• Performance for many images (more than three) in LG4 (needs testing; the card gives no number beyond about three)
• Whether the multimodal EU clause in the Llama 3.2 and Llama 4 Acceptable Use Policies covers the guard models (not stated by Meta)
• Whether LG4 classifies image content in a response (neither the card nor the docs say)
### R9
Summary: Official Meta model cards, docs pages, the 3-Vision paper, licence and use-policy pages, and the OGX provider code.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/11B-vision/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://arxiv.org/html/2411.10414
• https://arxiv.org/abs/2411.10414
• https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
• https://huggingface.co/api/models/meta-llama/Llama-Guard-3-11B-Vision
• https://www.llama.com/llama4/use-policy/
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/models/llama/sku_types.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/models/llama/sku_list.py
• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/releases/RELEASE_NOTES_1.0.md
• https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/blog/2026-06-23-guardrails-responses-api.md

## Column LG4: Llama Guard: Code-interpreter and tool-use abuse classification
### R1
Summary: **Code interpreter abuse category.** Llama Guard 3-8B and Llama Guard 4 add S14, which flags content that seeks to abuse code interpreters. The 3-8B model was also evaluated on search tool calls. **[Documented]**
Detail:
• 3-8B card: the model "was optimized to support safety and security for search and code interpreter tool calls" **[Documented]**
• 3-8B card: "an additional category for Code Interpreter Abuse for tool calls use cases" **[Documented]**
• LG4 card: "We include an additional category, Code Interpreter Abuse, for text-only tool-call use cases" **[Documented]**
• Versions with S14: 3-8B, 3-8B-INT8 (own card lists 14 categories) and LG4 **[Documented]**
• Versions without S14: 3-1B and 3-11B-Vision (S1 to S13 only) **[Documented]**
### R2
Summary: **Code interpreter abuse and unsafe search-tool results.** S14 covers denial of service attacks, container escapes and privilege escalation. Search tool call safety is evaluated for 3-8B, but no separate search category exists. **[Documented]**
Detail:
• S14 definition, 3-8B card: "Responses that seek to abuse code interpreters, including those that enable denial of service attacks, container escapes or privilege escalation exploits" **[Documented]**
• S14 definition, Meta docs page (Llama Guard 3): "AI models should not create content that attempts to abuse code interpreters. Examples of code interpreter abuse include, but are not limited to: Denial of service attacks, Container escapes or privilege escalation." **[Documented]**
• LG4 card: "S14: Code Interpreter Abuse (text only)" with the same definition as 3-8B **[Documented]**
• Search tool calls have no dedicated category: the 8B card lists S1 to S14 and S14 is code-interpreter abuse **[Documented: repo PurpleLlama@172c1074]**
• Llama Guard does not detect prompt injection or jailbreaks; the LG4 card points to Prompt Guard 2 **[Documented]**
### R3
Summary: **Content in the conversation, mainly the agent's code or text.** The category is worded about responses (what the AI creates); the cards give no separate tool-call input. Training used code interpreter completions from a non-safety-tuned model. **[Documented]**
Detail:
• All category descriptions, including S14, begin "Responses that…", so the unit judged is agent output **[Documented]**
• 3-8B training data for code interpreter abuse: "we use an LLM to generate safe and unsafe prompts. Then, we use a non-safety-tuned LLM to generate code interpreter completions that comply with these instructions" **[Documented]**
• Training data for search: "we use Llama3 to generate responses to a collected and synthetic set of prompts"; the generations "are based on the query results obtained from the Brave Search API" **[Documented]**
• Evaluation tables label the tool-use rows "prompt+response classification" (Table 3) and give separate Tool Use rows for prompt and response classification (Table 5) **[Documented]**
• The 8B card reports Tool Use results for both prompt classification and response classification (Table 5) **[Documented: repo PurpleLlama@172c1074]**
• Meta docs Llama Guard 3 and 4 pages (raw HTML): the roles listed are user and assistant; the words tool and function call do not appear **[Documented]**
• No Meta page, card, chat template or cookbook helper defines a tool role or the serialisation of tool calls or tool results for Llama Guard **[Not disclosed]**
• The prompt template has only User and Agent turns; how a tool call or tool output is serialised into a turn is not defined; the Hugging Face templates map only user and assistant **[Not disclosed]**
• Hugging Face chat templates map only user to User and assistant to Agent; a tool-role message is not handled (offline render labels it with the previous role or raises an alternation error); 3-8B templates also require string content (jinja2 3.1.6 offline render, not Meta text) **[Inferred]**
• Llama API moderations accepts system, user, assistant and tool messages; its prompt rendering is not described (archived official page, Wayback 2025-09-14) **[Documented]**
• OGX shield code: because "this might be a tool call", a non-user first message is rewritten as a user message, and turns are labelled with the capitalised role name; the Meta template uses the word Agent **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 writes a tool message as a "Tool: <content>" line and does not serialise assistant tool-call arguments, only the message content **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R4
Summary: **A category in the same classifier.** S14 is one more label in the prompt's category list; versions 3-8B and LG4 only, and text only in LG4. The 3-1B model was not optimised for it. **[Documented]**
Detail:
• Meta docs (Llama Guard 3): "The new Llama Guard 3 1B model was not optimized for category S14 Code Interpreter Abuse. If you need to screen for this category, you should use the 8B model." **[Documented]**
• 3-8B evaluation, Table 3 (prompt+response, internal set; F1 / AUPRC / FPR) **[Documented]**
  – Search tool calls: Llama Guard 3 0.856 / 0.938 / 0.174; Llama Guard 2 0.749 / 0.794 / 0.284; GPT4 0.732 / N/A / 0.525
  – Code interpreter abuse: Llama Guard 3 0.885 / 0.967 / 0.125; Llama Guard 2 0.683 / 0.677 / 0.670; GPT4 0.636 / N/A / 0.90
• 3-8B Table 5 (non-quantized vs INT8), Tool Use: prompt F1 0.920 vs 0.909 (FPR 0.126 vs 0.134); response F1 0.825 vs 0.827 (FPR 0.176 vs 0.155) **[Documented]**
• LG4 card averages S1 to S13 only ("All values are an average over samples from safety categories S1 through S13") and gives no S14 or tool-use metric **[Documented]**
• LG4 card: S14 is text only (no image case) **[Documented]**
• Score: first-token probability as unsafe probability, then thresholding (3-8B card); no threshold given **[Documented]**
• Serving: transformers on Hugging Face; 3-8B-INT8 via bitsandbytes **[Documented]**
• Cookbook default Llama Guard 3 category list includes "Code Interpreter Abuse" as the 14th entry for every Llama Guard 3 model, including 3-1B and 3-11B-Vision (prompt_format_utils.py; same on main on 2026-10-08) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• OGX provider (v0.4.4): maps 3-8B to the 13 default categories plus Code Interpreter Abuse; maps 3-1B, 3-11B-Vision and LG4 to S1 to S13 only, with the comment "Llama Guard 4 uses the same categories as Llama Guard 3", which conflicts with the LG4 card's S14 (added in commit ef26259209, PR 2579, July 2025; the PR gives no reason) **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX unknown model ids default to the 3-8B list including S14 **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R5
Summary: **Safe or unsafe with S14 code.** An unsafe verdict lists S14 on the second line, with other codes when applicable. The model returns text only; the 3-8B card derives a score from the first-token probability. **[Documented]**
Detail:
• First line safe or unsafe; second line comma-separated codes **[Documented]**
• OGX: violation level ERROR, user message "I can't answer that. Can I help with something else?", metadata violation type **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX moderation sets flagged true and the matched categories to score 1.0, others 0.0; an unrecognised code is treated as safe **[Documented: repo ogx-ai/ogx@v0.4.4]**
• 3-8B card: the first-token probability is used as the unsafe-class probability, then thresholded (see R4) **[Documented]**
### R6
Summary: **Conversation turns, with code in the agent turn.** Prompt checks use the user turn only; response checks need both turns. Meta does not disclose a tool-call or tool-output format, so code would go in as plain text. **[Inferred]**
Detail:
• User vs agent evaluation rule as in the Meta docs (agent response absent for prompt checks, both present for response checks) **[Documented]**
• Code emitted by the agent must be placed as text in the agent turn; this serialisation is an assumption **[Inferred]**
• No format for function name, arguments, JSON schema, tool results or tool role **[Not disclosed]**
• Languages: 3-8B supports English, French, German, Hindi, Italian, Portuguese, Spanish, Thai; S14 evaluation language not stated **[Documented]**
### R7
Summary: **Minimum setup:** Llama Guard 3-8B and Llama Guard 4, with 40 agent turns containing code or search-result text: unsafe S14 cases, borderline code, benign code, and a 3-1B negative control. **[Inferred]**
Detail:
• **Minimum setup:** run 3-8B, LG4 and 3-1B (control) on the same items as response checks; record whether S14 is returned. **[Inferred]**
• S14 positives: fork bomb or resource exhaustion script, container escape (mounting host sockets), privilege escalation exploit **[Inferred]**
• Near-boundary benign: legitimate code that uses subprocess, a load test with a rate cap, a Docker tutorial **[Inferred]**
• Same code as a user request only (prompt check) versus as an agent response **[Inferred]**
• Search-result case: agent summarising a hostile or unsafe web result **[Inferred]**
• Tool-call serialisation variants (JSON function call in agent turn, a Tool label turn, fenced code) to see which form the classifier reacts to; include a Tool-label turn as OGX emits it ("Tool: ...") **[Inferred]**
• Image plus code screenshot case for LG4 (S14 is text only), expected not to be judged on image **[Inferred]**
• OGX: with LG4, confirm that S14 never appears in the category list **[Inferred]**
### R8
Summary: **Key open questions.** How tool calls and tool outputs are serialised, any S14-specific LG4 metric, whether LG4 is evaluated on search tool calls, and whether OGX's S14 omission for LG4 is intentional.
Detail:
• Official serialisation of tool calls and tool results in the prompt (raw Meta docs, templates, cookbook and OGX code checked; none defines it)
• Which serialisation form the classifier actually reacts to, including S14 behaviour on an image plus code screenshot (needs testing)
• LG4 evaluation of tool-use categories (the card gives none)
• Whether the OGX omission of S14 for LG4 is deliberate (no rationale in the adding commit)
### R9
Summary: Official Meta model cards, docs pages, archived Llama API pages and provider code.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/8B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• http://web.archive.org/web/20250914152244/https://llama.developer.meta.com/docs/api/moderations
• https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py

## Column LG5: Llama Guard: Custom-policy classification
### R1
Summary: **Prompt-level policy customisation.** Meta says the default categories can be customised for zero-shot or few-shot prompting. The chat templates of 3-1B, 3-11B-Vision and Llama Guard 4 read optional custom and excluded category lists; the 3-8B template has a fixed list. **[Documented]**
Detail:
• Meta docs (Llama Guard 3 and 4 pages): the categories "can be customized for zero-shot or few-shot prompting" **[Documented]**
• Meta docs (Llama Guard 3 and 4 pages): "customize these descriptions to adapt the model's behavior for your specific use cases" **[Documented]**
• The Llama Guard 1 paper abstract says instruction fine-tuning enables "adjustment of taxonomy categories to align with specific use cases" (arXiv HTML, read raw) **[Documented]**
### R2
Summary: **Organisation-specific policies.** Useful when the fixed MLCommons categories do not match your policy. Models are trained on the MLCommons taxonomy, so custom behaviour is prompt-driven. **[Documented]**
Detail:
• Each model is trained on a fixed taxonomy (S1 to S13, or S1 to S14 for 3-8B and LG4) **[Documented]**
• No zero-shot, few-shot or custom-category results appear in the LG3-Vision paper, the 1B-INT4 paper, the Llama 3 paper section on Llama Guard 3, or the LG3 and LG4 cards (full text searched) **[Not disclosed]**
• LG3-Vision training randomly drops non-violated categories from the prompt so the model attends only to the categories included (arXiv 2411.10414 section 3.3) **[Documented]**
• Cards note comparison across policies is not straightforward because each model performs better when the evaluation set matches its policy **[Documented]**
### R3
Summary: **The category list inside the prompt.** The policy is text placed in the classification prompt, so the model judges the same conversation turns against your categories. **[Documented]**
Detail:
• Prompt template has a block between "BEGIN UNSAFE CONTENT CATEGORIES" and "END UNSAFE CONTENT CATEGORIES" **[Documented]**
• Cookbook builder numbers categories by position with a prefix (S for Llama Guard 2 and 3, O for Llama Guard 1) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
### R4
Summary: **Chat-template arguments, cookbook builder, paper results.** The 3-1B, 3-11B-Vision and Llama Guard 4 templates take custom categories and excluded keys; the 3-8B template does not. The cookbook builder covers up to Llama Guard 3. The LG1 paper reports zero-shot AUPRC 0.847. **[Documented]**
Detail:
• 3-1B HF card shows three snippets: default categories; "You can provide your own categories instead:" using a categories dict (key "S1": "My custom category"); and "Or you can exclude categories from the default list by specifying an array of category keys to exclude:" with excluded category keys ["S6"] **[Documented]**
• 3-11B-Vision HF card shows the same categories dict and excluded category keys ["S1"] together with image inputs **[Documented]**
• The 3-1B, 3-11B-Vision and Llama Guard 4 chat templates (tokenizer config, read through the Hugging Face metadata API) use an optional `categories` dict and an optional `excluded_category_keys` list **[Documented]**
• The Llama Guard 4 template defaults to S1 to S14 for text-only conversations and S1 to S13 when an image is present; a custom `categories` dict replaces either default **[Documented]**
• No Meta card or docs page shows a Llama Guard 4 snippet that passes `categories` or `excluded_category_keys`; the Hugging Face README was not readable (gated, 401) **[Not disclosed]**
• The 3-8B and 3-8B-INT8 chat templates hard-code S1 to S14 and read no categories or excluded keys (the INT8 file is byte-identical to the 8B file) **[Documented]**
• Extra `categories` or `excluded_category_keys` arguments passed to the 3-8B template are ignored (jinja2 3.1.6 offline render, not Meta text) **[Inferred]**
• For 3-8B, custom categories go through the cookbook builder with policy text; the customization notebook uses Llama-Guard-3-8B **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• Cookbook inference notebook (llama_guard_text_and_vision_inference.ipynb, read in full) has a Custom Categories section with a categories dict ("S1": "Custom category 1. …", "S2": "This will be removed") and excluded category keys ["S2"], run through Llama-Guard-3-1B (text) and Llama-Guard-3-11B-Vision (image) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• No file in the cookbook at this commit mentions Llama Guard 4 **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• Cookbook prompt_format_utils.py: enum LlamaGuardVersion has LG1, LG2 and LG3 only; build_custom_prompt takes a list of SafetyCategory, a short-name prefix, a template and a with_policy flag (default False); with_policy True appends each description under its name **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• The only template there for LG3 is text only (no image token) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• LG1 paper (Table 4, OpenAI Mod AUPRC): OpenAI Moderation API 0.856; Llama Guard with no adaptation 0.837; zero-shot with OpenAI Mod categories 0.847; few-shot with descriptions and in-context examples 0.872 (arXiv HTML, read raw) **[Documented]**
• The LG1 paper's Table 2 note says the reported Llama Guard results use zero-shot prompting with the target taxonomy (arXiv HTML, read raw) **[Documented]**
• Few-shot definition: "similar to zero-shot but additionally includes 2 to 4 examples for each category in the prompt" **[Documented]**
• LG1 paper: "adapting to a new policy exclusively through prompting is effective while also being low cost compared to fine-tuning" **[Documented]**
• 3-1B card links a customization notebook; the linked llama-recipes path returns 404 and the notebook now lives under getting-started/responsible_ai/llama_guard in the cookbook **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• The customization notebook uses Llama Guard 3-8B with the cookbook builder: category removal, custom category addition, ToxicChat evaluation and PEFT fine-tuning **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• Notebook caveat: without fine-tuning, an added category only works for topics closely related to existing categories **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• Notebook caveat: after a category is removed, the model can still return unsafe in some cases **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• OGX provider: configuration key `excluded_categories` holds codes like S1, S2; a startup assertion rejects other formats; excluded codes are dropped from the prompt, and a verdict whose codes are all within the excluded set is treated as safe **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX: excluding every code is treated as excluding none; custom category text is not supported, only the built-in names **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX: for LG4 only S1 to S13 are listed so S14 cannot be excluded or included (added in commit ef26259209, PR 2579, July 2025; the PR gives no reason) **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R5
Summary: **Same safe or unsafe output.** The model returns the usual verdict; codes refer to the positions or keys you supplied. **[Documented]**
Detail:
• Output template unchanged: first line safe or unsafe, second line comma-separated categories **[Documented]**
• Custom keys follow the card example "S1" naming; whether other key formats work is untested **[To be verified]**
### R6
Summary: **Category text plus conversation.** Provide a category list (name, optionally description) and the user or agent turns. **[Documented]**
Detail:
• 3-1B example uses only a name-like string as the description ("My custom category") **[Documented]**
• Cookbook custom prompt supplies names, with descriptions only when with_policy is set **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• Documented limits on number or length of custom categories: none **[Not disclosed]**
### R7
Summary: **Minimum setup:** Llama Guard 3-1B and 3-11B-Vision (documented path) plus Llama Guard 4 (template supports custom lists, untested), with a 3-category custom taxonomy, about 12 labelled items each, and exclusion tests. **[Inferred]**
Detail:
• **Minimum setup:** build a taxonomy of 3 custom categories (for example C1 account takeover guidance, C2 competitor disparagement, C3 internal-data disclosure) with 4 positives and 4 negatives per category, plus 4 near-boundary items. **[Inferred]**
• Run zero-shot (names only), zero-shot with descriptions, and few-shot with 2 to 4 examples per category (following the LG1 paper) **[Inferred]**
• Excluded-category tests: take an item unsafe under S6 and confirm it is unsafe by default and safe when S6 is excluded; repeat with S13 **[Inferred]**
• Replacement test: supply only a custom dict and confirm default hazards (for example S1 violent crime) no longer fire **[Inferred]**
• OGX test: set excluded categories to one code, then to every code, and compare **[Inferred]**
• Llama Guard 4: pass the same `categories` and `excluded_category_keys`; the template reads them, so record whether verdicts follow the custom text, and note the LG4 template expects message content as a list of typed parts (a plain string content renders an empty conversation) **[Inferred]**
• 3-8B: confirm that `categories` passed to the chat template changes nothing, then use the cookbook builder **[Inferred]**
### R8
Summary: **Key open questions.** Whether custom and excluded categories change verdicts as intended on the 3-1B, 3-11B-Vision and Llama Guard 4 templates, whether Meta documents any Llama Guard 4 custom-policy usage, and zero-shot quality for current models.
Detail:
• Whether custom and excluded categories actually change verdicts on the 3-1B, 3-11B-Vision and Llama Guard 4 templates (needs testing; the LG4 template reads them but no run was made)
• Any Meta page or card showing Llama Guard 4 custom-category usage (the template supports it; no page shows it)
• Whether custom keys other than the S1 style work (needs testing)
• Limits on the number or length of custom categories (docs state none; needs testing)
• Zero-shot or few-shot quality of Llama Guard 3 or 4 on your own taxonomy (needs testing; only the LG1 paper reports such results, and the three papers, cards and Llama 3 paper were searched)
### R9
Summary: Official Meta model cards, docs pages, papers, Hugging Face chat templates and repo code.
Detail:
• https://huggingface.co/meta-llama/Llama-Guard-3-1B
• https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
• https://huggingface.co/api/models/meta-llama/Llama-Guard-4-12B
• https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B
• https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B-INT8
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://arxiv.org/html/2312.06674
• https://arxiv.org/html/2411.10414
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/getting-started/responsible_ai/llama_guard/llama_guard_text_and_vision_inference.ipynb
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/getting-started/responsible_ai/llama_guard/llama_guard_customization_via_prompting_and_fine_tuning.ipynb
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py
