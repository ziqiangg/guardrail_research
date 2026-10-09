# Llama Guard research brief (shared by all drafting agents)

## Scope (user-decided)
- Llama Guard ONLY. Table 3 covers **Llama Guard 4 (12B)** and the **Llama Guard 3 family** (3-1B, 3-8B, 3-8B-INT8, 3-11B-Vision). Version differences go in Detail bullets.
- LG1 (LlamaGuard-7b) and LG2 (Meta-Llama-Guard-2-8B) are legacy. They appear only in the sheet 3d inventory and the category crosswalk.
- Out of scope: Prompt Guard / Prompt Guard 2, LlamaFirewall, Code Shield, CyberSecEval. You may mention, in R2 and R8 only, that Llama Guard does not detect jailbreak or prompt injection and that Meta points to Prompt Guard 2 for that.

## The 5 Table 3 columns (exact headers)
1. `Llama Guard: Input-level prompt content-safety classification`
2. `Llama Guard: Output-level response content-safety classification`
3. `Llama Guard: Multimodal (image + text) content-safety classification`
4. `Llama Guard: Code-interpreter and tool-use abuse classification`
5. `Llama Guard: Custom-policy classification`

## Official sources only
- Hugging Face model cards (meta-llama org): Llama-Guard-4-12B, Llama-Guard-3-8B, Llama-Guard-3-8B-INT8, Llama-Guard-3-1B, Llama-Guard-3-11B-Vision, Meta-Llama-Guard-2-8B, LlamaGuard-7b.
- Meta docs:
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
  - .../llama-guard-4/ (also on developer.meta.com/ai/docs/...)
  - .../meta-llama-guard-2/
  - https://dev.meta.ai/llama/llama-protections/
- Meta papers:
  - LG1 https://arxiv.org/abs/2312.06674 (html: /html/2312.06674)
  - LG3-Vision https://arxiv.org/abs/2411.10414
  - LG3-1B-INT4 https://arxiv.org/abs/2411.17713
  - The user-supplied LG1 PDF on fbcdn is the same paper. Cite arXiv instead.
- GitHub:
  - meta-llama/PurpleLlama @ 172c1074069eb88ec834124272c1b1c4f8893445. Folders: Llama-Guard3/{1B,8B,11B-vision}/MODEL_CARD.md, Llama-Guard4/12B/MODEL_CARD.md, Llama-Guard3/1B/ET_INSTRUCTIONS.md.
  - meta-llama/llama-cookbook @ 2f22a9eb: src/llama_cookbook/inference/prompt_format_utils.py, and the notebook getting-started/responsible_ai/llama_guard/llama_guard_text_and_vision_inference.ipynb.
  - ogx-ai/ogx (formerly meta-llama/llama-stack). Tag v0.4.4: src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py. Also docs/releases/RELEASE_NOTES_1.0.md.
  - NVIDIA-NeMo/Guardrails v0.24.1: nemoguardrails/library/llama_guard/. This is NeMo's integration.
- Context7: /meta-llama/purplellama, /meta-llama/llama-cookbook.
- Tools: load them via ToolSearch "select:WebFetch,WebSearch,mcp__github__get_file_contents,mcp__github__search_code,mcp__context7__query-docs".
  - WebFetch summarises pages. For any number or quote you rely on, ask for VERBATIM text, or read the raw GitHub file instead.
  - Hugging Face pages may be gated; the PurpleLlama MODEL_CARD.md files mirror most card content.

## Exploration findings to RE-VERIFY (do not copy blindly)
- **Prompts and responses.** Every version classifies both. It is one model, and the instruction wording selects which: `role` = User for input, Agent for output. When evaluating the user input, the agent response must not be present. When evaluating the response, both the user input and the response must be present (LG3 docs).
- **Output format.** First line `safe` or `unsafe`. If unsafe, the second line lists comma-separated S-codes.
- **Score.** Use the first-token probability as the "unsafe" probability, then threshold it. LG2 documents 0.5; LG3-8B says "apply score thresholding". The 1B ExecuTorch doc gives first-token ids 19193 = safe and 39257 = unsafe. No threshold is documented for 3-1B, 11B-V or LG4.
- **Taxonomy for LG3/LG4.**
  - S1 Violent Crimes
  - S2 Non-Violent Crimes
  - S3 Sex-Related Crimes
  - S4 Child Sexual Exploitation
  - S5 Defamation
  - S6 Specialized Advice
  - S7 Privacy
  - S8 Intellectual Property
  - S9 Indiscriminate Weapons
  - S10 Hate
  - S11 Suicide & Self-Harm
  - S12 Sexual Content
  - S13 Elections
  - S14 Code Interpreter Abuse. S14 is in 3-8B and LG4 only, and is text-only in LG4.
  - 3-1B and 11B-V use S1–S13.
- **LG2 taxonomy.** S1–S11 with different numbering: S5 Specialized Advice, S6 Privacy, S7 IP, S8 Weapons, S9 Hate, S10 Self-Harm, S11 Sexual Content. It omits Elections and Defamation.
- **LG1 taxonomy.** O1–O6: Violence & Hate, Sexual Content, Guns & Illegal Weapons, Regulated or Controlled Substances, Suicide & Self Harm, Criminal Planning.
- **Languages.** LG3-8B and 3-1B: EN, FR, DE, HI, IT, PT, ES, TH. 11B-V: English only. LG4: English plus the same 7.
- **Images.** 11B-V takes one image per prompt, rescaled to 4 tiles of 560×560. LG4 takes multiple images (tested with about 3), as 336×336 tiles plus a global tile.
- **Tool use.** LG3-8B covers "search tool calls and code interpreter abuse". Evaluations: search F1 0.856 / AUPRC 0.938 / FPR 0.174; code interpreter F1 0.885 / 0.967 / 0.125. 3-1B is not optimised for S14; its card says to use the 8B for it. No version documents a general function-call format.
- **Custom policy.**
  - The docs say the default categories "can be customized for zero-shot or few-shot prompting".
  - `apply_chat_template(..., categories={...}, excluded_category_keys=[...])` appears on the 3-1B card and in the cookbook notebook. It is not documented for LG4.
  - The cookbook has `build_custom_prompt(with_policy=...)`, which stops at LG3.
  - LG1 paper: zero-shot AUPRC 0.847 vs OpenAI API 0.856 on OpenAI Mod; few-shot 0.872.
  - 3-Vision paper: no zero-shot results.
- **Evaluations.**
  - LG3-8B English response: F1 0.939, AUPRC 0.985, FPR 0.040. LG2 on the same set: 0.877 / 0.927 / 0.081. GPT-4: 0.805 / – / 0.152.
  - LG3-8B multilingual F1/FPR: FR 0.943/0.036, DE 0.877/0.032, HI 0.871/0.050, IT 0.873/0.038, PT 0.860/0.060, ES 0.875/0.023, TH 0.834/0.030.
  - 8B-INT8: English F1 0.936, FPR 0.040.
  - 3-1B: English F1 0.899 / FPR 0.090; XSTest F1 0.821 / FPR 0.068.
  - 3-1B-INT4: 0.904 / 0.084.
  - 11B-V: prompt P 0.891, R 0.623, F1 0.733, FPR 0.052; response P 0.961, R 0.916, F1 0.938, FPR 0.016.
  - LG4, output filtering, S1–S13 averaged: English R 69%, FPR 11%, F1 61%. Multilingual 43% / 3% / 51%. Single image 41% / 9% / 38%. Multi-image 61% / 9% / 52%.
  - LG1 AUPRC: internal prompt 0.945 / response 0.953; OpenAI Mod 0.847; ToxicChat 0.626.
- **Adversarial results (3-Vision paper).**
  - PGD image attack at ε=8/255: prompt misclassified safe rose from 21% to 70%; response from 6% to 27%.
  - GCG text attack: prompt fooled 72%. Response fooled 30% when the attacker controls only the prompt, and 75% when the attacker controls the agent output.
- **Limitations (cards).**
  - Limited by training data.
  - S5 Defamation, S8 IP and S13 Elections need up-to-date facts.
  - Vulnerable to adversarial / prompt-injection attacks.
  - Input filtering lowers violations but raises false refusals.
  - 11B-V is not for image-only or text-only classification.
- **Licences.** LG1: Llama 2 Community License. LG2: Meta Llama 3 Community License. LG3-8B/INT8: Llama 3.1. 3-1B/11B-V: Llama 3.2. LG4: Llama 4 Community License Agreement.
- **Serving.**
  - HF transformers, gated.
  - 8B-INT8 via bitsandbytes.
  - 1B pruned + INT4 for ExecuTorch.
  - No official latency figures.
  - The llama-models repo has no Llama Guard prompt template.
- **llama-stack / OGX.**
  - Last Llama Guard provider at v0.4.4: `excluded_categories` config; checks the LAST message only; temperature 0. It returns a violation with level ERROR, user_message "I can't answer that. Can I help with something else?", and metadata violation_type.
  - Its moderation endpoint returns scores of only 0/1, does not support images, and treats an unknown code as safe (fails open).
  - It gives LG4 only S1–S13, which conflicts with the LG4 card.
  - OGX 1.0 (May 2026) removed the Safety API and shields in favour of /v1/moderations.
- **NeMo integration.** NeMo Guardrails v0.24.1 `llama guard check input` / `llama guard check output` flows. The model type is hard-coded as `llama_guard`; the NeMo docs example uses `llama_guard_2`.

## Labels
- **[Documented]**: an official Meta page (HF meta-llama card, Meta docs page, or Meta-authored paper).
- **[Documented: repo <repo>@<ref>]**: official code repo content.
- **[Inferred]**, **[To be verified]**, **[Not disclosed]**.
- Never label something [Documented] unless you read it in that source.

## Format: exactly like drafts/two_level_v2.md
```
## Column LGn: Llama Guard: <exact header>
### R1
Summary: **Bold lead.** 1–3 plain sentences. **[Label]**
Detail:
• one fact … **[Label]**
  – sub-item
### R2 … ### R9
```
- **Rows.** R1 function · R2 threat/condition · R3 what it inspects and where it operates · R4 mechanism (must state which versions support it, and serving/integration notes) · R5 output · R6 input and context required · R7 minimum test setup ("**Minimum setup:** …" with **[Inferred]**) · R8 open items (no labels; comma or bullet list) · R9 sources (one URL per bullet; Summary is a plain line with no bold lead and no label).
- **Summary.** ≤45 words (R7 ≤60). No code identifiers, underscores, backticks or `$`. Each label must match the facts the summary draws on. R8 Summary is "**Key open questions.** …" with no label.
- **Detail.** One fact per `• ` bullet, each ending with its bold label. Keep config keys and model ids inline in backticks.
- Add an `## Reviewer notes` section at the end: contradictions between sources, anything you were unsure of, and facts that came from summarised fetches.
