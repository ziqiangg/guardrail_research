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
• The paper's threat model assumes "full white-box access" because weights are public **[Documented]**
• Both cards say the model "may be susceptible to adversarial attacks"; LG4 card points to Prompt Guard 2 for prompt attacks, and Llama Guard itself does not detect jailbreak or prompt injection **[Documented]**
• S5 Defamation, S8 Intellectual Property and S13 Elections need factual, up-to-date knowledge **[Documented]**
### R3
Summary: **User image and text, plus the text response.** It reads the prompt text and the image together; it is not meant for image-only or text-only classification. The 3-11B-Vision card says English optimised, one image per prompt. **[Documented]**
Detail:
• 3-11B-Vision card: "not meant to be used as an image safety classifier nor a text-only safety classifier. Its task is to classify the multimodal prompt or the multimodal prompt along with the text response" **[Documented]**
• Meta docs (Llama Guard 3 and 4 pages): "It is not designed to perform image-only classification" **[Documented]**
• Meta docs: "the model does not support the evaluation of images that were themselves created using generative AI technology" (seen on both pages through a summarising fetch) **[Documented]**
• 3-11B-Vision: "optimized for English language and only supports one image at the moment" **[Documented]**
• Meta docs (Llama Guard 3 page): "multi-turn support here does not mean multi-image support; the model evaluates only one image per prompt" **[Documented]**
• LG4 card: multilingual text on the languages supported by Llama Guard 3, plus mixed text-and-image prompts **[Documented]**
• LG4 docs page says the model "has been optimized for English-language text, so the text component of the prompt should be in English"; this conflicts with the card's multilingual claim (see Reviewer notes) **[Documented]**
• LG4 docs: images can be evaluated in multi-turn conversations, but the image token must be added to the turn in which the image occurs **[Documented]**
• Prompt classification is harder than response classification because of ambiguity (card example: "how do I buy this" with an image of multiple objects); the card recommends response classification in such cases **[Documented]**
### R4
Summary: **Fine-tuned vision-language model.** Version 3-11B-Vision takes one image rescaled into four 560 by 560 chunks; Llama Guard 4 is a 12B early-fusion model that accepts several images. Serving via transformers; the OGX moderation endpoint ignores images. **[Documented]**
Detail:
• Versions supporting images: 3-11B-Vision (one image) and LG4 (multiple images); 3-1B, 3-8B and 3-8B-INT8 do not **[Documented]**
• 3-11B-Vision tiling: "our vision encoder will rescale it into 4 chunks, each of 560x560"; limitations section: "classification performance may vary depending on the actual image size" **[Documented]**
• 3-11B-Vision prompt template (Meta docs) starts the user turn with the image token followed by "Task: Check if there is unsafe content in '{{ role }}' messages…" **[Documented]**
• LG4 architecture: early fusion transformer with dense layers, pruned from Llama 4 Scout (routed experts and router removed, shared expert kept), shares the tokenizer and vision encoder of Llama 4 Scout and Maverick, "can be run on a single GPU" **[Documented]**
• LG4 prompt template (Meta docs): image tokens in the User line are an image start token, patch tokens, tile x and tile y separator tokens, a global image token, more patch tokens, then an image end token; header tokens differ from Llama 3 (header start and header end, end-of-turn token) **[Documented]**
• LG4 training: blend of 3-8B and 3-11B-vision data plus multi-image data "with most samples containing from 2 to 5 images" and multilingual data; roughly 3:1 text-only to multimodal **[Documented]**
• LG4 card: "tested mostly with prompts containing a few images (three, most frequently), so performance may vary if using it to classify safety with a much larger number of images" **[Documented]**
• LG4 tile size 336 by 336 plus a global tile: not stated in any source read here **[To be verified]**
• LG4 card: "integrated into the Llama Moderations API for text and images" **[Documented]**
• Serving: Hugging Face transformers with a processor (example code on the 3-11B-Vision HF page passes text and images to the processor) **[Documented]**
• OGX provider (ogx-ai/ogx v0.4.4): the moderation method has the code comment "TODO: Add Image based support for OpenAI Moderations" and builds a text-only prompt; the result marks applied input types as text only **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX shield path: the vision branch (keeps only the most recent user image, placed first in the content list) runs only when the model equals the core-model id for 3-11B-Vision; LG4 and any other id go through the text path **[Documented: repo ogx-ai/ogx@v0.4.4]**
• Whether the Hugging Face repo id for 3-11B-Vision also reaches the vision branch depends on the value of the core-model id string, which was not read **[Inferred]**
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
• Score and threshold for these models: no threshold documented for 3-11B-Vision or LG4 **[Not disclosed]**
• OGX moderation: category scores are only 0.0 or 1.0 and the safe object sets every category score to 1.0 (see Reviewer notes) **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R6
Summary: **One prompt image (3-11B-Vision) or several (Llama Guard 4), with text.** For prompt checks, supply user turn only; for response checks, supply the user turn and the agent text response. **[Documented]**
Detail:
• Evaluating the user input: the agent response must not be present; evaluating the agent response: both user input and agent response must be present **[Documented]**
• 3-11B-Vision accepts exactly one image per prompt; LG4 accepts several **[Documented]**
• Image must be attached to the user turn where it occurs; text component should be English per the docs page **[Documented]**
• Images rescaled, so image size can change results (3-11B-Vision) **[Documented]**
• Generated images are not supported **[Documented]**
• Response is text only; image output is not classified **[Inferred]**
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
• OGX check: send an image-bearing message through the moderation endpoint and confirm the image is ignored **[Inferred]**
### R8
Summary: **Key open questions.** LG4 tile size and its token layout, an official F1 or threshold for 3-11B-Vision at its default score, behaviour beyond about three images, and whether the OGX vision branch is reached by the Hugging Face id.
Detail:
• LG4 image tiling: 336 by 336 tiles plus a global tile (from the brief) not found in the card or docs read
• LG4 docs say English-optimised text while the card claims multilingual: which governs for multimodal prompts
• Whether any official score threshold exists for 3-11B-Vision and LG4
• Performance for many images (more than three) in LG4
• Whether the 3-11B-Vision HF id triggers OGX's vision branch (value of the core-model id string)
• Full text of the LG4 docs "Complete Example" with multiple images (only a summary was returned)
### R9
Summary: Official Meta model cards, docs pages, the 3-Vision paper and the OGX provider code.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/11B-vision/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://arxiv.org/abs/2411.10414
• https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py

## Column LG4: Llama Guard: Code-interpreter and tool-use abuse classification
### R1
Summary: **Code interpreter abuse category.** Llama Guard 3-8B and Llama Guard 4 add S14, which flags content that seeks to abuse code interpreters. The 3-8B model was also evaluated on search tool calls. There is no general function-call validation format. **[Documented]**
Detail:
• 3-8B card: the model "was optimized to support safety and security for search and code interpreter tool calls" **[Documented]**
• 3-8B card: "an additional category for Code Interpreter Abuse for tool calls use cases" **[Documented]**
• LG4 card: "We include an additional category, Code Interpreter Abuse, for text-only tool-call use cases" **[Documented]**
• Versions with S14: 3-8B (and 3-8B-INT8, same taxonomy per its card family) and LG4 **[Documented]**
• Versions without S14: 3-1B and 3-11B-Vision (S1 to S13 only) **[Documented]**
### R2
Summary: **Code interpreter abuse and unsafe search-tool results.** S14 covers denial of service attacks, container escapes and privilege escalation. Search tool call safety is evaluated for 3-8B, but no separate search category exists. **[Documented]**
Detail:
• S14 definition, 3-8B card: "Responses that seek to abuse code interpreters, including those that enable denial of service attacks, container escapes or privilege escalation exploits" **[Documented]**
• S14 definition, Meta docs page (Llama Guard 3): "AI models should not create content that attempts to abuse code interpreters. Examples of code interpreter abuse include, but are not limited to: Denial of service attacks, Container escapes or privilege escalation." **[Documented]**
• LG4 card: "S14: Code Interpreter Abuse (text only)" with the same definition as 3-8B **[Documented]**
• Search tool calls: no dedicated category; the evaluation covers them under the 14-category taxonomy **[Inferred]**
• Llama Guard does not detect prompt injection or jailbreaks; the LG4 card points to Prompt Guard 2 **[Documented]**
### R3
Summary: **Content in the conversation, mainly the agent's code or text.** The category is worded about responses (what the AI creates); the cards give no separate tool-call input. Training used code interpreter completions from an uncensored model. **[Documented]**
Detail:
• All category descriptions, including S14, begin "Responses that…", so the unit judged is agent output **[Documented]**
• 3-8B training data for code interpreter abuse: "we use an LLM to generate safe and unsafe prompts. Then, we use a non-safety-tuned LLM to generate code interpreter completions that comply with these instructions" **[Documented]**
• Training data for search: "we use Llama3 to generate responses to a collected and synthetic set of prompts"; the generations "are based on the query results obtained from the Brave Search API" **[Documented]**
• Evaluation tables label the tool-use rows "prompt+response classification" (Table 3) and give separate Tool Use rows for prompt and response classification (Table 5) **[Documented]**
• So both the user prompt and the agent's code or answer can be judged **[Inferred]**
• Meta docs (Llama Guard 3 page, via summarising fetch): no mention of tool, function call, search tool or code interpreter roles in the prompt formats or examples **[Documented]**
• The prompt template has only User and Agent turns; how a tool call or tool output is serialised into a turn is not defined **[Not disclosed]**
• OGX shield code: because "this might be a tool call", a non-user first message is rewritten as a user message, and turns are labelled with the capitalised role name; the Meta template uses the word Agent **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R4
Summary: **A category in the same classifier.** S14 is one more label in the prompt's category list; versions 3-8B and LG4 only, and text only in LG4. The 3-1B model was not optimised for it. **[Documented]**
Detail:
• Meta docs (Llama Guard 3): "The new Llama Guard 3 1B model was not optimized for category S14 Code Interpreter Abuse. If you need to screen for this category, you should use the 8B model." **[Documented]**
• 3-8B evaluation, Table 3 (prompt+response, internal set; F1 / AUPRC / FPR) **[Documented]**
  – Search tool calls: Llama Guard 3 0.856 / 0.938 / 0.174; Llama Guard 2 0.749 / 0.794 / 0.284; GPT4 0.732 / N/A / 0.525
  – Code interpreter abuse: Llama Guard 3 0.885 / 0.967 / 0.125; Llama Guard 2 0.683 / 0.677 / 0.670; GPT4 0.636 / N/A / 0.90
• 3-8B Table 5 (non-quantized vs INT8), Tool Use: prompt F1 0.920 vs 0.909 (FPR 0.126 vs 0.134); response F1 0.825 vs 0.827 (FPR 0.176 vs 0.155) **[Documented]**
• LG4 card averages S1 to S13 only and gives no S14 or tool-use metric **[Documented]**
• LG4 card: S14 is text only (no image case) **[Documented]**
• Score: first-token probability as unsafe probability, then thresholding (3-8B card); no threshold given **[Documented]**
• Serving: transformers on Hugging Face; 3-8B-INT8 via bitsandbytes **[Documented]**
• Cookbook default Llama Guard 3 category list includes "Code Interpreter Abuse" as the 14th entry (repo meta-llama/llama-cookbook@2f22a9eb prompt_format_utils.py) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• OGX provider (v0.4.4): maps 3-8B to the 13 default categories plus Code Interpreter Abuse; maps 3-1B, 3-11B-Vision and LG4 to S1 to S13 only, with the comment "Llama Guard 4 uses the same categories as Llama Guard 3", which conflicts with the LG4 card's S14 **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX unknown model ids default to the 3-8B list including S14 **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R5
Summary: **Safe or unsafe with S14 code.** An unsafe verdict lists S14 on the second line, with other codes when applicable. No numeric score is returned by the model itself. **[Documented]**
Detail:
• First line safe or unsafe; second line comma-separated codes **[Documented]**
• OGX: violation level ERROR, user message "I can't answer that. Can I help with something else?", metadata violation type **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX moderation sets flagged true and the matched categories to score 1.0, others 0.0; an unrecognised code is treated as safe **[Documented: repo ogx-ai/ogx@v0.4.4]**
### R6
Summary: **A conversation with the agent turn containing code.** Prompt checks use the user turn only; response checks need the user turn and the agent turn. There is no documented tool-call or function-call schema. **[Documented]**
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
• Tool-call serialisation variants (JSON function call in agent turn, a Tool label turn, fenced code) to see which form the classifier reacts to **[Inferred]**
• Image plus code screenshot case for LG4 (S14 is text only), expected not to be judged on image **[Inferred]**
• OGX: with LG4, confirm that S14 never appears in the category list **[Inferred]**
### R8
Summary: **Key open questions.** How tool calls and tool outputs are serialised, any S14-specific LG4 metric, whether LG4 is evaluated on search tool calls, and whether OGX's S14 omission for LG4 is intentional.
Detail:
• Official serialisation of tool calls and tool results in the prompt
• LG4 evaluation of tool-use categories (card gives none)
• Whether 3-8B-INT8 supports S14 as documented (check its card)
• Whether the OGX omission of S14 for LG4 is deliberate
• Whether Meta docs mention a tool role (only a summarising fetch was available)
### R9
Summary: Official Meta model cards, docs pages and provider code.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/8B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py

## Column LG5: Llama Guard: Custom-policy classification
### R1
Summary: **Prompt-level policy customisation.** Meta says the default categories can be customised for zero-shot or few-shot prompting. Category replacement and exclusion are documented for 3-1B and 3-11B-Vision; none is documented for Llama Guard 4. **[Documented]**
Detail:
• Meta docs (Llama Guard 3 and 4 pages): the categories "can be customized for zero-shot or few-shot prompting" **[Documented]**
• Meta docs (Llama Guard 3): "you can customize these descriptions to adapt the model's behavior for your specific use cases" (summarising fetch) **[Documented]**
• The Llama Guard 1 paper states instruction fine-tuning enables "adjustment of taxonomy categories to align with specific use cases" (summarising fetch) **[Documented]**
### R2
Summary: **Organisation-specific policies.** Useful when the fixed MLCommons categories do not match your policy. Models are trained on the MLCommons taxonomy, so custom behaviour is prompt-driven. **[Documented]**
Detail:
• Each model is trained on a fixed taxonomy (S1 to S13, or S1 to S14 for 3-8B and LG4) **[Documented]**
• The 3-Vision paper trains on 13 hazard categories; the fetched content showed no zero-shot or custom-category results **[Inferred]**
• Cards note comparison across policies is not straightforward because each model performs better when the evaluation set matches its policy **[Documented]**
### R3
Summary: **The category list inside the prompt.** The policy is text placed in the classification prompt, so the model judges the same conversation turns against your categories. **[Documented]**
Detail:
• Prompt template has a block between "BEGIN UNSAFE CONTENT CATEGORIES" and "END UNSAFE CONTENT CATEGORIES" **[Documented]**
• Cookbook builder numbers categories by position with a prefix (S for Llama Guard 2 and 3, O for Llama Guard 1) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
### R4
Summary: **Chat-template arguments, cookbook builder, paper results.** The Hugging Face chat template accepts categories and excluded category keys on the 3-1B and 3-11B-Vision cards; the cookbook builder stops at Llama Guard 3. The LG1 paper reports zero-shot AUPRC 0.847. **[Documented]**
Detail:
• 3-1B HF card shows three snippets: default categories; "You can provide your own categories instead:" using a categories dict (key "S1": "My custom category"); and "Or you can exclude categories from the default list by specifying an array of category keys to exclude:" with excluded category keys ["S6"] **[Documented]**
• 3-11B-Vision HF card shows the same categories dict and excluded category keys ["S1"] together with image inputs **[Documented]**
• The 3-8B and LG4 HF pages (via summarising fetch): no categories or excluded category keys snippet; LG4 shows only a plain chat-template call **[Documented]**
• Whether the 3-8B or LG4 chat templates accept these arguments: not documented **[To be verified]**
• Cookbook notebook (llama_guard_text_and_vision_inference.ipynb) has a Custom Categories section with a categories dict ("S1": "Custom category 1. …", "S2": "This will be removed") and excluded category keys ["S2"], run through Llama-Guard-3-1B (text) and Llama-Guard-3-11B-Vision (image) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• The notebook does not load Llama Guard 4 **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• Cookbook prompt_format_utils.py: enum LlamaGuardVersion has LG1, LG2 and LG3 only; build_custom_prompt takes a list of SafetyCategory, a short-name prefix, a template and a with_policy flag (default False); with_policy True appends each description under its name **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• The only template there for LG3 is text only (no image token) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**
• LG1 paper (Table 4, OpenAI Mod AUPRC): OpenAI Moderation API 0.856; Llama Guard with no adaptation 0.837; zero-shot with OpenAI Mod categories 0.847; few-shot with descriptions and in-context examples 0.872 **[Documented]**
• Few-shot definition: "similar to zero-shot but additionally includes 2 to 4 examples for each category in the prompt" **[Documented]**
• LG1 paper: "adapting to a new policy exclusively through prompting is effective while also being low cost compared to fine-tuning" **[Documented]**
• 3-1B card: a customization notebook for "Taxonomy Customization, Zero/Few-shot prompting, Evaluation and Fine Tuning" is linked (llama-recipes path llama_guard_customization_via_prompting_and_fine_tuning.ipynb); its contents were not read **[Documented]**
• OGX provider: configuration key `excluded_categories` holds codes like S1, S2; a startup assertion rejects other formats; excluded codes are dropped from the prompt, and a verdict whose codes are all within the excluded set is treated as safe **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX: excluding every code is treated as excluding none; custom category text is not supported, only the built-in names **[Documented: repo ogx-ai/ogx@v0.4.4]**
• OGX: for LG4 only S1 to S13 are listed so S14 cannot be excluded or included **[Documented: repo ogx-ai/ogx@v0.4.4]**
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
Summary: **Minimum setup:** Llama Guard 3-1B and 3-11B-Vision (documented path), Llama Guard 4 as undocumented probe, with a 3-category custom taxonomy, about 12 labelled items each, and exclusion tests. **[Inferred]**
Detail:
• **Minimum setup:** build a taxonomy of 3 custom categories (for example C1 account takeover guidance, C2 competitor disparagement, C3 internal-data disclosure) with 4 positives and 4 negatives per category, plus 4 near-boundary items. **[Inferred]**
• Run zero-shot (names only), zero-shot with descriptions, and few-shot with 2 to 4 examples per category (following the LG1 paper) **[Inferred]**
• Excluded-category tests: take an item unsafe under S6 and confirm it is unsafe by default and safe when S6 is excluded; repeat with S13 **[Inferred]**
• Replacement test: supply only a custom dict and confirm default hazards (for example S1 violent crime) no longer fire **[Inferred]**
• OGX test: set excluded categories to one code, then to every code, and compare **[Inferred]**
• LG4: try the same arguments and record whether the template errors, ignores them, or applies them **[Inferred]**
### R8
Summary: **Key open questions.** Whether categories and excluded keys work in the 3-8B and LG4 chat templates, any LG4 custom-policy guidance, contents of the customization and fine-tuning notebook, and zero-shot quality for current models.
Detail:
• Support for categories and excluded category keys on 3-8B and LG4 chat templates
• Any documented LG4 custom-policy guidance or results (none found)
• Whether the linked llama-recipes notebook path still exists and what it reports
• Zero-shot or few-shot results for Llama Guard 3 or 4 (only the LG1 paper reports them)
### R9
Summary: Official Meta model cards, docs pages, papers and repo code.
Detail:
• https://huggingface.co/meta-llama/Llama-Guard-3-1B
• https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard3/1B/MODEL_CARD.md
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3/
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/
• https://arxiv.org/abs/2312.06674
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb/src/llama_cookbook/inference/prompt_format_utils.py
• https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb/getting-started/responsible_ai/llama_guard/llama_guard_text_and_vision_inference.ipynb
• https://github.com/ogx-ai/ogx/blob/v0.4.4/src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py

## Reviewer notes
• CONTRADICTION (brief vs paper): the brief says PGD at 8/255 raised response misclassification from 6% to 27%. The 3-Vision paper Table 3 (fetched via arXiv HTML, summarised) gives 22% at 8/255 and 27% at 128/255 and 255/255. The draft uses the paper values. Prompt: 21% to 70% at 8/255 matches.
• CONTRADICTION: LG4 docs page (summarised fetch) says the text component should be English; the LG4 card says English plus the 7 Llama Guard 3 languages. Not resolved.
• CONTRADICTION: OGX maps LG4 to S1 to S13 with the comment "same categories as Llama Guard 3", but the LG4 card lists S14 (text only).
• The brief says the 3-1B card documents categories and excluded category keys; the GitHub MODEL_CARD.md for 3-1B does not show them (it links a notebook). The code snippets come from the Hugging Face page via a summarising fetch.
• The brief says OGX "checks the LAST message only". The code builds a prompt of the whole message list and asks about the last message (as the template does); it is not a last-message-only input.
• OGX moderation scores: unflagged results set every category score to 1.0 (likely a quirk); flagged ones set matched categories to 1.0 and others to 0.0. The brief's "0/1" is only partly right.
• The 3-1B GitHub card evaluation table includes Vietnamese and Indonesian columns although the card lists 8 supported languages.
• LG3 docs fetch returned an unprompted note "S14 is text-only category"; the LG3 page and 8B card do not say this (only the LG4 card does). Ignored.
• The "336 by 336 tiles plus global tile" claim for LG4 was not found; the 560 by 560 four-chunk statement for 3-11B-Vision was verified verbatim.
• Cookbook template wording ("according our safety policy") differs slightly from the Meta docs ("according to our safety policy").
• Meta docs pages, HF pages and arXiv pages were read through a summarising fetch; the PurpleLlama model cards, the cookbook Python file and the OGX file were read raw through the GitHub API. The cookbook notebook was searched by pattern, not read in full.
• Direct HTTP download from this shell was blocked (connection reset), so raw GitHub content came from the GitHub MCP tool.
• The 8B-INT8 card was not read separately; the statement that it shares S14 relies on the Table 5 quantised figures in the 8B card.
