## Column LG1: Llama Guard: Input-level prompt content-safety classification
### R1
Summary: **Input-level prompt content-safety classification.** Llama Guard reads a user prompt and replies safe or unsafe, listing the violated hazard categories when unsafe. The same model also classifies responses. **[Documented]**
Detail:
• Llama Guard can classify content in LLM inputs (prompt classification) **[Documented]** (LG3-1B, LG3-8B and LG4 model cards)
• The model acts as an LLM: it generates text saying whether the prompt is safe or unsafe and, if unsafe, lists the violated categories **[Documented]**
• Prompt versus response is chosen by the instruction wording (role `User` for the input, `Agent` for the output); it is one model, not two **[Documented]** (Meta LG3 and LG4 docs pages)
• LG4 is also integrated into the Llama Moderations API for text and images **[Documented]** (LG4 model card)
• Versions covered: LG4 (12B), LG3-1B, LG3-8B, LG3-8B-INT8, and LG3-11B-Vision for multimodal prompts **[Documented]**
### R2
Summary: **Harmful user requests under a fixed hazard taxonomy.** Covers 13 MLCommons-based categories S1 to S13, plus S14 Code Interpreter Abuse in LG3-8B and LG4. Not designed to detect jailbreak or prompt injection; Meta points to Prompt Guard 2. **[Documented]**
Detail:
• S1 Violent Crimes, S2 Non-Violent Crimes, S3 Sex-Related Crimes, S4 Child Sexual Exploitation, S5 Defamation, S6 Specialized Advice, S7 Privacy, S8 Intellectual Property, S9 Indiscriminate Weapons, S10 Hate, S11 Suicide & Self-Harm, S12 Sexual Content, S13 Elections **[Documented]** (PurpleLlama cards @ 172c1074)
• S14 Code Interpreter Abuse is in LG3-8B and LG4 (marked "text only" in LG4); it is not in LG3-1B or LG3-11B-Vision, which use S1 to S13 **[Documented]**
• The LG3-1B docs note says it was not optimised for S14 and to use the 8B model for that category **[Documented]** (Meta LG3 docs page)
• The card category definitions are written as "Responses that …" for every category, though the same labels are applied to prompts **[Documented]**
• LG4 card: aligned to the standardised MLCommons hazards taxonomy, with S14 added for text-only tool-call use **[Documented]**
• Limitation: S5 Defamation, S8 Intellectual Property and S13 Elections may require factual, up-to-date knowledge; the cards advise more complex systems for use cases highly sensitive to them **[Documented]**
• Limitation: the model may be susceptible to adversarial or prompt-injection attacks; the LG4 card points to Prompt Guard 2 for detecting prompt attacks **[Documented]**
• Meta's protections page describes prompt injection and jailbreaking as attack categories handled by Prompt Guard, not Llama Guard **[Documented]**
• LG3-Vision paper, adversarial prompt classification: a PGD image attack at 8/255 raised harmful prompts misclassified as safe from 21% to 70%; a GCG text attack got 72% of prompts classified safe **[Documented]** (arXiv 2411.10414)
• Trade-off: LG3-8B card says deploying it "might increase refusals to benign prompts (False Positives)" **[Documented]**
• Trade-off: LG4 card says that in some internal tests input filtering reduces the safety violation rate and raises the overall refusal rate more than output filtering does, but experience may vary **[Documented]**
• Output filtering is described on the LG4 card as letting the LLM answer an unsafe prompt safely, so only an unsafe final output is censored **[Documented]**
• Legacy taxonomies differ (LG1 uses O1 to O6; LG2 uses S1 to S11 with different numbering) and are out of scope for this column **[Documented]**
### R3
Summary: **User message, before the main model.** The prompt is classified on its own, with no agent response in the conversation. Input filtering catches unsafe content before the LLM responds. **[Documented]**
Detail:
• For input evaluation the role placeholder is `User`; the agent response must not be present in the conversation **[Documented]** (Meta LG3 and LG4 docs pages)
• The LG4 card says the advantage of input filtering is that unsafe content can be caught very early, before the LLM responds **[Documented]**
• Cookbook helper templates ask for an assessment of "ONLY THE LAST" message of the given role **[Documented: repo llama-cookbook@2f22a9eb]**
• OGX v0.4.4 llama_guard provider: `run_shield` checks the last message only, and `run_moderation` wraps every input string as a user message **[Documented: repo ogx-ai/ogx@v0.4.4]**
• NeMo Guardrails `llama guard check input` flow sends only the user message to the configured model **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• LG3-11B-Vision prompt classification covers text plus one image and is not meant for text-only classification; use LG3-8B or LG3-1B for text-only **[Documented]** (11B-Vision card)
### R4
Summary: **A fine-tuned LLM generates the verdict.** Supported in LG4, LG3-1B, LG3-8B and LG3-8B-INT8; LG3-11B-Vision supports it only for image-plus-text prompts. Served through Hugging Face transformers, with INT8, INT4 and Llama API options. **[Documented]**
Detail:
• Mechanism: the model generates text; the first line is safe or unsafe, then categories **[Documented]**
• LG4: 12B dense model pruned from Llama 4 Scout, natively multimodal, runs on a single GPU; licence Llama 4 Community License Agreement **[Documented]**
• LG3-8B: Llama 3.1 8B fine-tune; 8-language support; licence Llama 3.1 Community License **[Documented]**
• LG3-8B-INT8: bitsandbytes INT8 (`BitsAndBytesConfig(load_in_8bit=True)`), about 40% smaller checkpoint, performance comparable to the original **[Documented]**
• LG3-1B: Llama 3.2 1B, pruned to 12 layers and 6400 MLP hidden dimension (1123M parameters), logit-level distillation from LG3-8B; licence Llama 3.2 **[Documented]**
• LG3-1B-INT4: weights INT4 with quantization-aware training, output layer pruned to 20 tokens, for mobile via ExecuTorch **[Documented]**
• LG3-11B-Vision: Llama 3.2 11B Vision fine-tune; image rescaled to 4 chunks of 560x560; one image only **[Documented]**
• Hugging Face transformers: LG3 uses `AutoTokenizer` and `AutoModelForCausalLM`; LG4 uses `AutoProcessor` and `Llama4ForConditionalGeneration` in bfloat16; weights are gated **[Documented]** (HF cards, summarised fetch)
• Cookbook helper `build_default_prompt` / `build_custom_prompt` in `prompt_format_utils.py` builds LG1, LG2 and LG3 prompts; it has no LG4 template **[Documented: repo llama-cookbook@2f22a9eb]**
• The cookbook LG3 template wraps the prompt in Llama 3 header tokens and asks for an assessment of only the last message **[Documented: repo llama-cookbook@2f22a9eb]**
• Meta's docs say the llama-models repo has no Llama Guard template; the model cards point to the docs pages for the prompt format **[Inferred]** (absence not checked directly)
• OGX v0.4.4 (formerly llama-stack) llama_guard provider: config `excluded_categories`; temperature 0.0; fixed prompt template; unsafe verdict becomes a violation with level ERROR and message "I can't answer that. Can I help with something else?" **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 gives LG4 only S1 to S13, with a code comment citing the LG4 model card; the card lists S14, so this conflicts with the card **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 moderation path: unknown codes are logged and the result is returned as not flagged (fails open); no image support in moderation (TODO in code) **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4 builds the role label from the last message role capitalised, so an OpenAI-style assistant message becomes "Assistant" rather than the documented `Agent` **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX 1.0 (May 2026) removed the standalone Safety API; moderation is served by the OpenAI-compatible `/v1/moderations` endpoint and the release notes do not mention Llama Guard **[Documented: repo ogx-ai/ogx]**
• NeMo Guardrails v0.24.1: flows `llama guard check input` call an action with model name `llama_guard` hard-coded in the flow; the NVIDIA docs example uses model type `llama_guard_2` **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• NeMo parsing: reply starting with safe is allowed; starting with unsafe is blocked with violations split on spaces; any other reply is blocked with an empty list (fails closed); temperature 0.0 **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• Llama API exposes LG4 through the `/moderations` endpoint **[Documented]** (Meta protections page)
• No official latency figures found **[Not disclosed]**
### R5
Summary: **Verdict text, optionally a score.** First line is safe or unsafe; if unsafe a second line lists comma-separated S-codes. A score is the first-token probability of unsafe, with a threshold left to the deployer. **[Documented]**
Detail:
• Safe prompt: the output is `safe` **[Documented]**
• Unsafe prompt: `unsafe`, then a second line with comma-separated categories such as `S1,S2` **[Documented]**
• LG3-8B card: "we look at the probability for the first token, and use that as the 'unsafe' class probability" and "apply score thresholding to make binary decisions" **[Documented]**
• No numeric threshold is given for LG3-8B **[Not disclosed]**
• LG3-1B and LG4 cards (HF fetch) give no threshold guidance; the LG4 docs page mentions no token probability, threshold or score **[Documented]** (absence in fetched text)
• ExecuTorch instructions for LG3-1B-INT4: first output token 19193 means safe and 39257 means unsafe; the sample takes the argmax, not a probability **[Documented: repo PurpleLlama@172c1074]**
• NeMo exposes an allowed flag and a lowercased violation list; OGX moderation returns per-category scores of only 0.0 and 1.0, with all categories scored 1.0 when safe **[Documented: repo]**
• LG3-8B card evaluations use AUPRC, which needs a score, though the scoring pipeline is not described **[Documented]**
### R6
Summary: **A single user prompt, plus a policy prompt.** The input is the user message with the category list; the agent response must be absent. Text only, except LG4 and LG3-11B-Vision which also take images. **[Documented]**
Detail:
• Input: user prompt text inside the Llama Guard prompt template with the category list **[Documented]**
• The agent response must not be present when evaluating the user input **[Documented]**
• Languages, LG3-8B and LG3-1B cards: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai **[Documented]**
• Languages, LG4 card: English and multilingual text "on the languages supported by Llama Guard 3" **[Documented]**
• Languages, LG3-11B-Vision: optimised for English **[Documented]**
• LG4 docs page says the model is optimised for English text and the text component should be in English; Meta's protections page says LG4 supports 12 languages **[Documented]**
• Images, LG4: multiple images, tested mostly with about three; LG3-11B-Vision: one image **[Documented]**
• Evaluation, LG3-8B prompt classification (card Table 5): English P 0.952, R 0.943, F1 0.947, FPR 0.057; multilingual F1 0.900, FPR 0.054; tool use F1 0.920, FPR 0.126 **[Documented]**
• Evaluation, LG3-8B-INT8 prompt classification: English F1 0.950, FPR 0.045; multilingual F1 0.899, FPR 0.051; tool use F1 0.909, FPR 0.134 **[Documented]**
• Evaluation, LG3-11B-Vision prompt classification: P 0.891, R 0.623, F1 0.733, FPR 0.052; the card says prompt (text plus image) classification is harder than response classification and recommends response classification for ambiguous cases **[Documented]**
• Evaluation, LG3-1B and LG4: the cards do not label their numbers as prompt-only; LG4 numbers are for output filtering only **[Documented]**
• Training data: LG3 added benign multilingual prompts that LLMs would likely reject, to reduce false positives; code-interpreter safe data was chosen near the unsafe boundary **[Documented]** (LG3-8B card)
• Test data for XSTest (exaggerated safety, benign near-miss prompts): LG3-8B F1 0.884, FPR 0.044; LG3-1B F1 0.821, FPR 0.068 **[Documented]** (LG3-1B card)
• Custom categories: LG3-1B card shows `apply_chat_template(..., categories={"S1": "..."})` and `excluded_category_keys=["S6"]` **[Documented]** (HF card, summarised fetch)
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
Summary: **Key open questions.** No documented decision threshold, unclear LG4 language coverage, no prompt-only numbers for LG3-1B or LG4, and no latency figures.
Detail:
• Recommended threshold for the first-token probability in LG3-1B, LG3-8B, LG3-11B-Vision and LG4
• LG4 language coverage: card says English plus the LG3 languages, docs page says English-optimised, protections page says 12 languages
• LG3-1B card table lists Vietnamese and Indonesian although its supported-language list does not
• Prompt-only evaluation numbers for LG3-1B and LG4
• Official latency and throughput figures
• Whether LG4 supports custom category text via the chat template (documented for LG3-1B, not found for LG4)
• Behaviour with jailbreak or prompt-injection prompts (Meta points to Prompt Guard 2)
### R9
Summary: Meta model cards on GitHub and Hugging Face, Meta docs and protections pages, the LG3-Vision paper, and the cookbook, OGX and NeMo Guardrails source and docs.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/8B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/11B-vision/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/ET_INSTRUCTIONS.md
• https://huggingface.co/meta-llama/Llama-Guard-3-1B
• https://huggingface.co/meta-llama/Llama-Guard-3-8B-INT8
• https://huggingface.co/meta-llama/Llama-Guard-4-12B
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://dev.meta.ai/llama/llama-protections/
• https://arxiv.org/abs/2411.10414
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py
• https://github.com/ogx-ai/ogx/blob/main/docs/releases/RELEASE_NOTES_1.0.md
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/actions.py
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/content-safety

## Column LG2: Llama Guard: Output-level response content-safety classification
### R1
Summary: **Output-level response content-safety classification.** Llama Guard reads a user prompt together with the model's response and replies safe or unsafe for the response, listing violated categories. **[Documented]**
Detail:
• Llama Guard can classify content in LLM responses (response classification) **[Documented]** (LG3-1B, LG3-8B and LG4 model cards)
• Same model and taxonomy as the input function; the role placeholder `Agent` selects the response **[Documented]** (Meta docs pages)
• Versions covered: LG4 (12B), LG3-1B, LG3-8B, LG3-8B-INT8, LG3-11B-Vision (multimodal prompt plus text response) **[Documented]**
### R2
Summary: **Unsafe model output.** Detects responses that enable, encourage or contain content in S1 to S13, plus S14 Code Interpreter Abuse in LG3-8B and LG4. Facts needing up-to-date knowledge are weak spots, and adversarial agent output can fool it. **[Documented]**
Detail:
• Category list S1 to S13 is the same as in the input column; S14 appears only in LG3-8B and LG4 **[Documented]**
• Category definitions start with "Responses that …", so they are written for output classification **[Documented]**
• LG3-8B tool use: trained and evaluated on search tool calls and code interpreter abuse **[Documented]**
• Evaluation, LG3-8B Table 3 (prompt+response): search tool calls F1 0.856, AUPRC 0.938, FPR 0.174; code interpreter abuse F1 0.885, AUPRC 0.967, FPR 0.125 **[Documented]**
• Limitation: S5, S8 and S13 may need factual, up-to-date knowledge **[Documented]**
• Limitation: performance may be limited by pre-training data (common sense, multilingual, policy coverage) **[Documented]**
• LG3-Vision paper, response classification: PGD at 8/255 raised unsafe responses classified safe from 6% to 27% **[Documented]**
• LG3-Vision paper, GCG text attack: 30% of responses fooled when the attacker only controls the prompt (16% baseline), and 75% when the attacker controls the agent output **[Documented]**
• Trade-off: LG4 card says output filtering lets the LLM answer an unsafe prompt safely and censors only unsafe final output; input filtering reduces violations and raises refusals more in internal tests **[Documented]**
• Trade-off: LG3-8B card says deployment might increase refusals to benign prompts **[Documented]**
• Llama Guard does not detect jailbreak or prompt injection; Meta points to Prompt Guard 2 **[Documented]**
### R3
Summary: **Model response, after the main model.** Operates after the LLM answers and before the answer is shown, with the user prompt included as context. **[Documented]**
Detail:
• For response evaluation both the user input and the agent response must be present; the user input gives important context **[Documented]** (Meta LG3 and LG4 docs pages)
• The LG4 card describes output filtering as classifying an LLM's generated output **[Documented]**
• Using both input and output filtering gives additional security **[Documented]** (LG4 card)
• NeMo Guardrails `llama guard check output` flow passes the user message and the bot response to the Llama Guard model **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• OGX v0.4.4 `run_moderation` wraps every string as a user message, so it classifies text in the user role; response classification needs the shield path, which labels the role from the last message **[Documented: repo ogx-ai/ogx@v0.4.4]**
• The cookbook helper builds a response prompt when the agent type is `Agent` and the conversation holds user and agent turns **[Documented: repo llama-cookbook@2f22a9eb]**
• LG3-11B-Vision response classification covers the multimodal prompt plus the text response **[Documented]**
### R4
Summary: **Same fine-tuned LLM, response instruction.** Supported by LG4, LG3-1B, LG3-8B, LG3-8B-INT8 and LG3-11B-Vision. Serving via Hugging Face transformers, INT8 or INT4, cookbook helper, OGX and NeMo. **[Documented]**
Detail:
• All five versions support response classification **[Documented]** (cards)
• LG3-11B-Vision is not meant for image-only or text-only classification, so use LG3-8B or LG3-1B for text responses **[Documented]**
• LG3-8B-INT8 uses bitsandbytes INT8, about 40% smaller, with comparable performance **[Documented]**
• LG3-1B-INT4 targets mobile with ExecuTorch (pruned, quantization-aware training) **[Documented]**
• Hugging Face transformers: LG3 uses `AutoModelForCausalLM`; LG4 uses `AutoProcessor` and `Llama4ForConditionalGeneration`; weights are gated **[Documented]** (HF cards, summarised fetch)
• Cookbook helper `prompt_format_utils.py` supports LG1 to LG3 prompts only; custom prompts through `build_custom_prompt(..., with_policy=...)` **[Documented: repo llama-cookbook@2f22a9eb]**
• OGX v0.4.4: `excluded_categories` config; temperature 0.0; checks the last message only; unsafe becomes a violation with level ERROR and the message "I can't answer that. Can I help with something else?" **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX v0.4.4: LG4 receives only S1 to S13 (card lists S14); moderation scores are 0.0 or 1.0 and unknown codes return not flagged (fails open); OGX 1.0 (May 2026) removed the Safety API for `/v1/moderations` **[Documented: repo ogx-ai/ogx]**
• NeMo Guardrails v0.24.1: `llama guard check output` uses model name `llama_guard` fixed in the flow; docs example uses type `llama_guard_2`; unparseable output is blocked (fails closed) **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**
• Licences: LG3-8B and INT8 Llama 3.1; LG3-1B and 11B-Vision Llama 3.2; LG4 Llama 4 Community License Agreement **[Documented]**
• Official latency figures **[Not disclosed]**
### R5
Summary: **Verdict text for the response.** First line safe or unsafe; if unsafe, a second line lists S-codes. A score is the first-token probability of unsafe; no threshold is documented except for earlier versions. **[Documented]**
Detail:
• Output format is identical to the input function: `safe`, or `unsafe` plus comma-separated codes **[Documented]**
• LG3-8B card: first-token probability is the unsafe-class probability, and score thresholding gives binary decisions **[Documented]**
• No numeric threshold for LG3-8B, LG3-1B, LG3-11B-Vision or LG4 **[Not disclosed]**
• LG3-1B-INT4 ExecuTorch sample: first token 19193 is safe and 39257 is unsafe (argmax) **[Documented: repo PurpleLlama@172c1074]**
• Evaluation LG3-8B response, English: F1 0.939, AUPRC 0.985, FPR 0.040 (LG2: 0.877, 0.927, 0.081; GPT4: 0.805, N/A, 0.152) **[Documented]**
• Evaluation LG3-8B multilingual F1/FPR: French 0.943/0.036, German 0.877/0.032, Hindi 0.871/0.050, Italian 0.873/0.038, Portuguese 0.860/0.060, Spanish 0.875/0.023, Thai 0.834/0.030 **[Documented]**
• Evaluation LG3-8B-INT8 response, English: F1 0.936, FPR 0.040 **[Documented]**
• Evaluation LG3-1B English F1 0.899, FPR 0.090; XSTest F1 0.821, FPR 0.068; LG3-1B-INT4 English F1 0.904, FPR 0.084 **[Documented]**
• Evaluation LG3-11B-Vision response: P 0.961, R 0.916, F1 0.938, FPR 0.016 **[Documented]**
• Evaluation LG4 (output filtering, S1 to S13 average, in-house set): English R 69%, FPR 11%, F1 61%; multilingual 43%, 3%, 51%; single image 41%, 9%, 38%; multi-image 61%, 9%, 52% **[Documented]**
• Cross-card difference: LG3-8B F1 values (about 0.94) and LG4 F1 values (about 0.61) come from different in-house test sets and are not directly comparable **[Inferred]**
• NeMo returns an allowed flag and a violation list; OGX returns a violation object or a moderation object **[Documented: repo]**
### R6
Summary: **Prompt and response pair.** Needs the user prompt and the agent response, plus the policy prompt. Eight languages for LG3 text models; LG4 adds images; LG3-11B-Vision is English with one image. **[Documented]**
Detail:
• Input: user prompt and agent response together **[Documented]**
• Languages: LG3-8B, LG3-1B: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai; LG4 card: English plus the LG3 languages; LG3-11B-Vision: English-optimised **[Documented]**
• LG4 docs page and protections page conflict with the card on language support (see R8) **[Documented]**
• LG3-1B card table also lists Vietnamese and Indonesian columns outside its supported-language list **[Documented]**
• Training data: single-turn and multi-turn human-AI conversations; benign multilingual prompt and response data where LLMs likely reject the prompts **[Documented]** (LG3-8B card)
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
Summary: **Key open questions.** No documented decision threshold, conflicting LG4 language statements, no like-for-like response numbers across versions, and no latency figures.
Detail:
• Recommended threshold on the first-token probability, for every version
• LG4 language coverage: card, docs page and protections page disagree
• Whether LG3-1B supports Vietnamese and Indonesian (shown only in an evaluation table)
• Comparable response-level numbers across LG4, LG3-8B and LG3-1B on one test set
• Whether LG4 supports custom category text through the chat template
• Official latency and throughput figures
• How OGX moderation handles response-role classification after the Safety API removal
### R9
Summary: Meta model cards on GitHub and Hugging Face, Meta docs and protections pages, the LG3-Vision paper, and the cookbook, OGX and NeMo Guardrails source and docs.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/8B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/11B-vision/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/ET_INSTRUCTIONS.md
• https://huggingface.co/meta-llama/Llama-Guard-3-1B
• https://huggingface.co/meta-llama/Llama-Guard-3-8B-INT8
• https://huggingface.co/meta-llama/Llama-Guard-4-12B
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://dev.meta.ai/llama/llama-protections/
• https://arxiv.org/abs/2411.10414
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py
• https://github.com/ogx-ai/ogx/blob/main/docs/releases/RELEASE_NOTES_1.0.md
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/flows.co
• https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/nemoguardrails/library/llama_guard/actions.py
• https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/content-safety

## Reviewer notes
• Read in full (raw card text via GitHub tool at the pinned commit): LG4, LG3-8B, LG3-1B and LG3-11B-Vision MODEL_CARD.md, LG3-1B ET_INSTRUCTIONS.md, cookbook `prompt_format_utils.py` @2f22a9eb, OGX v0.4.4 `llama_guard.py`, NeMo v0.24.1 `actions.py` and `flows.co`. All numbers from these are exact.
• Summarised WebFetch results (not raw): Meta LG3 and LG4 docs pages, protections page, Hugging Face cards (1B, 8B-INT8, 4-12B; licences and usage code), arXiv 2411.10414 adversarial numbers, OGX 1.0 release notes, NVIDIA content-safety page. Quotes were requested verbatim, but treat as summarised. The curl route to raw.githubusercontent.com failed (connection reset).
• Contradiction, LG4 languages: card says English plus the LG3 languages; docs page says optimised for English with the text component in English; protections page says 12 languages.
• Contradiction, LG3-1B: supported-language list has 8 languages; the card evaluation table adds Vietnamese and Indonesian.
• Contradiction, OGX v0.4.4 LG4 categories: code gives S1 to S13 while citing the LG4 card, which lists S14.
• Brief correction, OGX moderation scores: the code sets every category score to 1.0 for a safe result and 1.0/0.0 for unsafe, so "0/1 only" is right but a safe result scores 1.0.
• Observation, OGX role label: the prompt uses the capitalised last-message role ("Assistant" for OpenAI-style messages), not the documented `Agent`.
• Contrast, failure mode: OGX moderation fails open on unknown S-codes; NeMo blocks any reply that does not start with safe or unsafe (fails closed). NeMo's refusal for unparseable replies also applies to a rail outage only if the model returns text.
• NeMo docs example uses model type `llama_guard_2` while the flow hard-codes model name `llama_guard`; whether these are the same config key was not tested.
• ET instructions: 19193 and 39257 come from an argmax, so they are token ids, not probabilities. The 3-8B "first-token probability" statement is the only scoring method documented.
• The brief's statement "11B-V English only" is softer on the card: "optimized for English language".
• Taxonomy definitions on all cards begin "Responses that …" even where used for prompts.
• Trade-off verified verbatim in spirit: LG4 card (input filtering reduces violation rate and raises refusal rate more than output filtering, internal tests) and LG3-8B card (may increase refusals to benign prompts). Not checked: Llama 3 paper numbers the LG3 card cites.
• LG3-8B Table 5 prompt-classification figures are for 8B and 8B-INT8 only; the 1B and LG4 cards do not state whether their tables are prompt or response.
