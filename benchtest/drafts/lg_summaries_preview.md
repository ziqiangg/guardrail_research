# Llama Guard — Summary preview (Checkpoint 2)


## Llama Guard: Input-level prompt content-safety classification

- **R1** (28w, 5 bullets): **Input-level prompt content-safety classification.** Llama Guard reads a user prompt and replies safe or unsafe, listing the violated hazard categories when unsafe. The same model also classifies responses. **[Documented]**
- **R2** (38w, 15 bullets): **Harmful user requests under a fixed hazard taxonomy.** Covers 13 MLCommons-based categories S1 to S13, plus S14 Code Interpreter Abuse in LG3-8B and LG4. Not designed to detect jailbreak or prompt injection; Meta points to Prompt Guard 2. **[Documented]**
- **R3** (29w, 7 bullets): **User message, before the main model.** The prompt is classified on its own, with no agent response in the conversation. Input filtering catches unsafe content before the LLM responds. **[Documented]**
- **R4** (30w, 27 bullets): **A fine-tuned LLM generates the verdict.** Supported in LG4, LG3-1B, LG3-8B and LG3-8B-INT8; LG3-11B-Vision supports it only for image-plus-text prompts. Served through Hugging Face transformers, with INT8 and INT4 variants. **[Documented]**
- **R5** (41w, 13 bullets): **Verdict text, optionally a score.** First line is safe or unsafe; if unsafe a second line lists comma-separated S-codes. LG3-8B and its INT8 card derive a score from the first-token probability, with no stated threshold; LG3-1B, 11B-Vision and LG4 describe none. **[Documented]**
- **R6** (34w, 20 bullets): **A single user prompt, plus a policy prompt.** The input is the user message with the category list; the agent response must be absent. Text only, except LG4 and LG3-11B-Vision which also take images. **[Documented]**
- **R7** (37w, 8 bullets): **Minimum setup:** a prompt-submission harness, labelled safe and unsafe prompts per S-category, multilingual copies, benign near-miss prompts for false positives, the model served with its template, and a verdict parser and logger. No response generation is needed. **[Inferred]**
- **R8** (30w, 9 bullets): **Key open questions.** No documented decision threshold, unclear LG4 language coverage (which 12 languages), no prompt-only numbers for LG3-1B or LG4, and latency figures only for LG3-1B-INT4 on one phone.
- **R9** (29w, 28 bullets): Meta model cards on GitHub and Hugging Face, Meta docs, protections and archived Llama API pages, Meta papers, and the cookbook, llama-models, OGX and NeMo Guardrails source and docs.

## Llama Guard: Output-level response content-safety classification

- **R1** (26w, 3 bullets): **Output-level response content-safety classification.** Llama Guard reads a user prompt together with the model's response and replies safe or unsafe for the response, listing violated categories. **[Documented]**
- **R2** (38w, 11 bullets): **Unsafe model output.** Detects responses that enable, encourage or contain content in S1 to S13, plus S14 Code Interpreter Abuse in LG3-8B and LG4. Facts needing up-to-date knowledge are weak spots, and adversarial agent output can fool it. **[Documented]**
- **R3** (24w, 8 bullets): **Model response, after the main model.** Operates after the LLM answers and before the answer is shown, with the user prompt included as context. **[Documented]**
- **R4** (28w, 14 bullets): **Same fine-tuned LLM, response instruction.** Supported by LG4, LG3-1B, LG3-8B, LG3-8B-INT8 and LG3-11B-Vision. Serving via Hugging Face transformers, INT8 or INT4, cookbook helper, OGX (to v0.4.4) and NeMo. **[Documented]**
- **R5** (32w, 14 bullets): **Verdict text for the response.** First line safe or unsafe; if unsafe, a second line lists S-codes. The LG3-8B and LG2 cards describe a first-token-probability score; only LG2 gives a threshold (0.5). **[Documented]**
- **R6** (36w, 8 bullets): **Prompt and response pair.** Needs the user prompt and the agent response, plus the policy prompt. LG3 text models cover eight languages; LG4 adds images and cites the same languages; LG3-11B-Vision is English-optimised with one image. **[Documented]**
- **R7** (42w, 8 bullets): **Minimum setup:** prompt and response pairs labelled safe or unsafe per S-category, including safe refusals to unsafe prompts and benign near-miss pairs, in the target languages; the model served with its template; a verdict parser and logger. The main LLM is optional. **[Inferred]**
- **R8** (26w, 7 bullets): **Key open questions.** No documented decision threshold, conflicting LG4 language statements, no like-for-like response numbers across versions, and latency figures only for LG3-1B-INT4 on one phone.
- **R9** (25w, 22 bullets): Meta model cards on GitHub and Hugging Face, Meta docs and protections pages, Meta papers, and the cookbook, OGX and NeMo Guardrails source and docs.

## Llama Guard: Multimodal (image + text) content-safety classification

- **R1** (30w, 5 bullets): **Image-plus-text safety classification.** Llama Guard 3-11B-Vision and Llama Guard 4 classify a multimodal prompt, or a multimodal prompt plus the text response, as safe or unsafe with violated category codes. **[Documented]**
- **R2** (36w, 13 bullets): **Harmful image-plus-text prompts and responses.** Targets the MLCommons hazard categories S1 to S13 in multimodal conversations, with specific attention to prompts asking to identify real people in images. Vulnerable to white-box adversarial image and text attacks. **[Documented]**
- **R3** (36w, 9 bullets): **User image and text, plus the text response.** It reads the prompt text and the image together; it is not meant for image-only or text-only classification. The 3-11B-Vision card says English optimised, one image per prompt. **[Documented]**
- **R4** (43w, 18 bullets): **Fine-tuned vision-language model.** Version 3-11B-Vision takes one image rescaled into four 560 by 560 chunks; Llama Guard 4 is a 12B early-fusion model that accepts several images. Serving via transformers; the OGX v0.4.4 moderation path ignored images and was removed in OGX 1.0. **[Documented]**
- **R5** (35w, 11 bullets): **Safe or unsafe plus codes.** First line says safe or unsafe; if unsafe, a second line lists the violated categories. Reported metrics include a 3-11B-Vision response F1 of 0.938 and LG4 multi-image recall of 61%. **[Documented]**
- **R6** (30w, 7 bullets): **One prompt image (3-11B-Vision) or several (Llama Guard 4), with text.** For prompt checks, supply user turn only; for response checks, supply the user turn and the agent text response. **[Documented]**
- **R7** (27w, 13 bullets): **Minimum setup:** one GPU host with Llama Guard 4 and a 3-11B-Vision baseline; about 60 labelled pairs, covering single-image, multi-image, benign-image/harmful-text, harmful-image/benign-text, and prompt versus response tasks. **[Inferred]**
- **R8** (35w, 5 bullets): **Key open questions.** No documented threshold for 3-11B-Vision or LG4, behaviour beyond about three images in LG4, which language rules apply to multimodal prompts, and whether Meta's multimodal EU licence clause covers the guard models.
- **R9** (18w, 14 bullets): Official Meta model cards, docs pages, the 3-Vision paper, licence and use-policy pages, and the OGX provider code.

## Llama Guard: Code-interpreter and tool-use abuse classification

- **R1** (32w, 5 bullets): **Code interpreter abuse category.** Llama Guard 3-8B and Llama Guard 4 add S14, which flags content that seeks to abuse code interpreters. The 3-8B model was also evaluated on search tool calls. **[Documented]**
- **R2** (32w, 5 bullets): **Code interpreter abuse and unsafe search-tool results.** S14 covers denial of service attacks, container escapes and privilege escalation. Search tool call safety is evaluated for 3-8B, but no separate search category exists. **[Documented]**
- **R3** (36w, 12 bullets): **Content in the conversation, mainly the agent's code or text.** The category is worded about responses (what the AI creates); the cards give no separate tool-call input. Training used code interpreter completions from a non-safety-tuned model. **[Documented]**
- **R4** (34w, 12 bullets): **A category in the same classifier.** S14 is one more label in the prompt's category list; versions 3-8B and LG4 only, and text only in LG4. The 3-1B model was not optimised for it. **[Documented]**
- **R5** (35w, 4 bullets): **Safe or unsafe with S14 code.** An unsafe verdict lists S14 on the second line, with other codes when applicable. The model returns text only; the 3-8B card derives a score from the first-token probability. **[Documented]**
- **R6** (37w, 4 bullets): **Conversation turns, with code in the agent turn.** Prompt checks use the user turn only; response checks need both turns. Meta does not disclose a tool-call or tool-output format, so code would go in as plain text. **[Inferred]**
- **R7** (30w, 8 bullets): **Minimum setup:** Llama Guard 3-8B and Llama Guard 4, with 40 agent turns containing code or search-result text: unsafe S14 cases, borderline code, benign code, and a 3-1B negative control. **[Inferred]**
- **R8** (32w, 4 bullets): **Key open questions.** How tool calls and tool outputs are serialised, any S14-specific LG4 metric, whether LG4 is evaluated on search tool calls, and whether OGX's S14 omission for LG4 is intentional.
- **R9** (13w, 9 bullets): Official Meta model cards, docs pages, archived Llama API pages and provider code.

## Llama Guard: Custom-policy classification

- **R1** (40w, 3 bullets): **Prompt-level policy customisation.** Meta says the default categories can be customised for zero-shot or few-shot prompting. The chat templates of 3-1B, 3-11B-Vision and Llama Guard 4 read optional custom and excluded category lists; the 3-8B template has a fixed list. **[Documented]**
- **R2** (25w, 4 bullets): **Organisation-specific policies.** Useful when the fixed MLCommons categories do not match your policy. Models are trained on the MLCommons taxonomy, so custom behaviour is prompt-driven. **[Documented]**
- **R3** (26w, 2 bullets): **The category list inside the prompt.** The policy is text placed in the classification prompt, so the model judges the same conversation turns against your categories. **[Documented]**
- **R4** (41w, 23 bullets): **Chat-template arguments, cookbook builder, paper results.** The 3-1B, 3-11B-Vision and Llama Guard 4 templates take custom categories and excluded keys; the 3-8B template does not. The cookbook builder covers up to Llama Guard 3. The LG1 paper reports zero-shot AUPRC 0.847. **[Documented]**
- **R5** (20w, 2 bullets): **Same safe or unsafe output.** The model returns the usual verdict; codes refer to the positions or keys you supplied. **[Documented]**
- **R6** (17w, 3 bullets): **Category text plus conversation.** Provide a category list (name, optionally description) and the user or agent turns. **[Documented]**
- **R7** (31w, 7 bullets): **Minimum setup:** Llama Guard 3-1B and 3-11B-Vision (documented path) plus Llama Guard 4 (template supports custom lists, untested), with a 3-category custom taxonomy, about 12 labelled items each, and exclusion tests. **[Inferred]**
- **R8** (36w, 5 bullets): **Key open questions.** Whether custom and excluded categories change verdicts as intended on the 3-1B, 3-11B-Vision and Llama Guard 4 templates, whether Meta documents any Llama Guard 4 custom-policy usage, and zero-shot quality for current models.
- **R9** (14w, 14 bullets): Official Meta model cards, docs pages, papers, Hugging Face chat templates and repo code.
