## Column PL1: Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection)
### R1
Summary: **Input-level prompt-attack classification.** Prompt Guard 2 is a small BERT-style model that labels a text string benign or malicious, aimed at prompt injection and jailbreak attempts. It ships in 86M and 22M sizes under the Llama 4 licence. @@D@@
Detail:
• Both Llama Prompt Guard 2 models "detect both prompt injection and jailbreaking attacks, trained on a large corpus of known vulnerabilities" (86M/MODEL_CARD.md@172c1074:11) @@L@@
• Meta docs page wording: "Both models detect prompt injection and jailbreaking attacks, and are trained on a large corpus of known vulnerabilities." (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Protections page wording: "Prompt Guard is a powerful tool for protecting LLM powered applications from malicious prompts to ensure their security and integrity." (dev.meta.ai llama-protections, read 2026-10-09) @@D@@
• Two models: Llama Prompt Guard 2 86M (base model mDeBERTa-base) and a smaller 22M (DeBERTa-xsmall) (86M/MODEL_CARD.md@172c1074:4,63) @@L@@
• Meta presents version 2 as a replacement: "can be used as a drop-in replacement for Prompt Guard for all use cases", and "Developers should migrate to Llama Prompt Guard 2" (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Model type: "Llama Prompt Guard 2 are BERT models that output only labels; unlike Llama Guard, Llama Prompt Guard 2 doesn't need a specific prompt structure or configuration." (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Meta writes the name three ways: "Llama Prompt Guard 2" (model card and docs page), "Prompt Guard 2" (protections page) and "PromptGuard 2" (LlamaFirewall docs and paper) (pages named, read 2026-10-09) @@D@@
### R2
Summary: **Explicit instruction-override attempts.** The model flags prompts that explicitly try to override earlier instructions, whether jailbreaks or injected instructions in untrusted text, regardless of harm. There is no injection sub-label, and eight languages were evaluated. @@D@@
Detail:
• Attack types: prompt injections "manipulate untrusted third-party and user data in the context window to make a model execute unintended instructions"; jailbreaks are "malicious instructions designed to override the safety and security features directly built into a model" (86M/MODEL_CARD.md@172c1074:8-9) @@L@@
• Scope: "classify prompts as 'malicious' if the prompt explicitly attempts to override prior instructions embedded into or seen by an LLM" (86M/MODEL_CARD.md@172c1074:22) @@L@@
• Intent only: the classification "considers only the intent to supersede developer or user instructions, regardless of whether the prompt is potentially harmful or the attack is likely to succeed" (86M/MODEL_CARD.md@172c1074:22) @@L@@
• No injection sub-label: "we don't include a specific 'injection' label to detect prompts that may cause unintentional instruction-following" (86M/MODEL_CARD.md@172c1074:23) @@L@@
• Paper: Prompt Guard 2 is "designed to detect explicit jailbreaking techniques in LLM inputs"; Prompt Guard 1 "attempted broader goal hijacking detection", which caused "excessive false positives" (arXiv 2505.03574 section 4.1 and appendix B) @@D@@
• Wording differs by source: the LlamaFirewall README calls it a detector of "direct prompt injection attempts" and the LlamaFirewall docs page says "direct jailbreak attempts", while the model card says both injection and jailbreak (LlamaFirewall/README.md@172c1074:27) @@L@@
• Examples named by the card: "variants of 'ignore previous instructions'" and DAN prompts (86M/MODEL_CARD.md@172c1074:98-99) @@L@@
• Languages evaluated: "English, French, German, Hindi, Italian, Portuguese, Spanish, and Thai"; the 86M model "uses a multilingual base model and is trained to detect both English and non-English injections and jailbreaks" (86M/MODEL_CARD.md@172c1074:25) @@L@@
• 22M is weaker on other languages: "There is no version of deberta-xsmall with multilingual pretraining available" (86M/MODEL_CARD.md@172c1074:106) @@L@@
• Meta advice on language fit: "Developers in resource constrained environments and focused only on English text will likely prefer the 22M model" (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Adversarial tokenisation is addressed: the tokenizer was refined "to mitigate adversarial tokenization attacks, such as whitespace manipulations and fragmented tokens" (86M/MODEL_CARD.md@172c1074:17) @@L@@
• Stated limitations: "adversaries may develop sophisticated attacks specifically to bypass detection", and some attacks "are highly application-dependent" (86M/MODEL_CARD.md@172c1074:104-105) @@L@@
• Not a harmful-content classifier: the card positions it beside "harmful content guardrails", and the intent-only scope above excludes harm judgement (premise: 86M/MODEL_CARD.md@172c1074:99). Harmful-content classification is the Llama Guard columns V to Z @@I@@
• Training languages and an attack taxonomy beyond the two categories (checked the model card, the Prompt Guard docs page, the protections page and paper appendix B; only the evaluation languages are listed) @@N@@
### R3
Summary: **A single text string, with no direction setting.** The model receives one string and labels it. Meta describes it as meant for user prompts and untrusted data such as web content. @@D@@
Detail:
• Input: "The input is a string that the model labels as 'benign' or 'malicious'." (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• The card's usage passes one string to the classifier or tokenizer, with no message roles or conversation structure (86M/MODEL_CARD.md@172c1074:35,48-49) @@L@@
• Intended inputs: it "operates on user inputs and untrusted content such as web data" (LlamaFirewall/README.md@172c1074:27) @@L@@
• Same scope in the paper: it "operates in real-time on user prompts and untrusted data sources" (arXiv 2505.03574 section 1) @@D@@
• Retrieved and tool text: the paper's AgentDojo test scanned messages with role user or tool: "For PromptGuard, we analyze only messages with the role of user or tool" (arXiv 2505.03574 section 4.3) @@D@@
• The model has no input-or-output flag and takes no system prompt or other context, so it applies to any text passed to it, such as prompts, retrieved passages, tool outputs or memory text (premise: the card and docs page describe a string-in, label-out model) @@I@@
• Scanning model responses with Prompt Guard 2: no page describes it (checked the model card, Llama-Prompt-Guard-2 README, Prompt Guard docs page, protections page, LlamaFirewall README, docs and paper) @@N@@
• Contrast with Llama Guard (columns V to Z): Prompt Guard 2 "doesn't need a specific prompt structure or configuration" (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Long inputs must be split by the caller: "For longer inputs, split prompts into segments and scan them in parallel to ensure violations are detected." (86M/MODEL_CARD.md@172c1074:24) @@L@@
### R4
Summary: **Small DeBERTa classifiers, run locally.** Two fine-tuned models, 86M on mDeBERTa-base and 22M on DeBERTa-xsmall, trained with an energy-based loss. Training used a mix of open-source and synthetic data. @@D@@
Detail:
• Base models: "mDeBERTa-base for the base version of Llama Prompt Guard 2 86M, and DeBERTa-xsmall as the base model for Llama Prompt Guard 2 22M. Both are open-source, MIT-licensed models from Microsoft." (86M/MODEL_CARD.md@172c1074:63) @@L@@
• Paper confirms the families: "mDeBERTa-base (86M parameters) and DeBERTa-xsmall (22M parameters)" (arXiv 2505.03574 section 4.1) @@D@@
• Training objective: "a modified energy-based loss function"; the card describes a penalty "for large negative energy predictions on benign prompts" (86M/MODEL_CARD.md@172c1074:61) @@L@@
• Training data: a "mix of open-source datasets" plus "our own synthetic injections and data from red-teaming earlier versions of Prompt Guard" (86M/MODEL_CARD.md@172c1074:60) @@L@@
• Training data sizes, dataset names and class balance (checked the model card, docs page and paper appendix B; not given) @@N@@
• Parameter counts: the card lists "Backbone Parameters" 86M and 22M; the Hugging Face metadata lists 278,810,882 F32 parameters for the 86M repo (86M revision a8ded8e6, HF API, read 2026-10-09) @@H86@@
• The 22M repo metadata lists 70,830,722 F32 parameters (22M revision 11614a15, HF API, read 2026-10-09) @@H22@@
• The gap between card and metadata counts is not explained on any page read; the likely cause is that the card counts only the transformer backbone and the metadata counts the embedding tables too (premise: the card column is headed "Backbone Parameters") @@I@@
• Serving route: load locally with the Transformers pipeline ("text-classification") or with AutoTokenizer and AutoModelForSequenceClassification; the card's example prints the predicted label from model.config.id2label (86M/MODEL_CARD.md@172c1074:29-56) @@L@@
• Docs page example calls a helper named get_jailbreak_score from the llama-cookbook inference utilities (source file inference.py not read) (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Hosted endpoint: the Hugging Face metadata marks the 86M repo as served by an inference provider (inference "warm") (86M revision a8ded8e6, HF API, read 2026-10-09) @@H86@@
• The 22M page shows "This model isn't deployed by any Inference Provider." (HF 22M page, read 2026-10-09) @@D@@
• A Meta-run hosted Prompt Guard 2 endpoint (checked the Prompt Guard docs page, protections page, repo README and LlamaFirewall docs; none names one) @@N@@
• Pin kinds are separate. Repo commit 172c1074069eb88ec834124272c1b1c4f8893445, author date 2026-09-29 (git, read 2026-10-09) @@L@@
• Hugging Face revision a8ded8e697ce7c355e395a0df51f94adb4a2fd27 for the 86M repo, last modified 2025-04-29, access "manual" (HF API, read 2026-10-09) @@H86@@
• Hugging Face revision 11614a155199674a0a95e6602d6ab0417b790ed0 for the 22M repo, last modified 2025-04-29, access "manual" (HF API, read 2026-10-09) @@H22@@
• Release notes or changelog for Prompt Guard 2 (checked the repo at the pin: no tags and no CHANGELOG file; the card has a "Summary of Changes from Prompt Guard 1" only) @@N@@
• Licence: "The same license as Llama 4 applies: see the LICENSE file, as well as our accompanying Acceptable Use Policy" (Llama-Prompt-Guard-2/README.md@172c1074:45) @@L@@
• The 86M and 22M LICENSE files are the Llama 4 Community License Agreement (Version Effective Date April 5, 2025) and contain an "Additional Commercial Terms" clause at 700 million monthly active users (86M/LICENSE@172c1074:22) @@L@@
• Hugging Face metadata: licence "other" with name "llama4"; the gate page shows "License: llama4" (86M revision a8ded8e6, HF API, read 2026-10-09) @@H86@@
• Gate: access is "manual"; the form asks for "your full legal name, date of birth, and full organization name with all corporate identifiers" (HF 86M gate page, read 2026-10-09) @@D@@
• Fine-tuning is recommended: "For optimal results, we recommend a methodology of fine-tuning the model on application-specific data." (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Engine and wrapper: the LlamaFirewall PromptGuard scanner (column PL2) loads "meta-llama/Llama-Prompt-Guard-2-86M" by default (promptguard_utils.py@172c1074:40) @@L@@
### R5
Summary: **A benign or malicious label with a score.** Meta publishes AUC, recall at 1% false positives and A100 latency from a private benchmark. The 86M model reports 97.5% recall and 92.4 ms; the 22M model 88.7% and 19.3 ms. @@D@@
Detail:
• Labels: the model labels prompts "benign" or "malicious"; "Both Prompt Guard 2 models focus on detecting explicit, known attack patterns" (86M/MODEL_CARD.md@172c1074:18) @@L@@
• The card's example prints "MALICIOUS" from model.config.id2label (86M/MODEL_CARD.md@172c1074:54-55) @@L@@
• The docs page example prints a jailbreak score of 0.001 for a benign text and 1.000 for an injection text (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Recommended decision threshold or score cut-off (checked the model card, Llama-Prompt-Guard-2 README, Prompt Guard docs page, protections page, LlamaFirewall README, docs pages and paper; none gives one) @@N@@
• Operating point used by Meta: the card reports "Recall @ 1% FPR"; the paper picks "a threshold for each model that produces a fixed, minimal utility reduction (3%)" on AgentDojo, and does not print the threshold values (arXiv 2505.03574 section 4.1) @@D@@
• Benchmark conditions: "a private benchmark built with datasets distinct from those used in training" (86M/MODEL_CARD.md@172c1074:69) @@L@@
• Benchmark size and class balance (checked the card and paper appendix A.2; not given beyond an English set and a machine-translated multilingual set) @@N@@
• 86M row: AUC English .998, recall at 1% FPR English 97.5%, AUC multilingual .995, latency 92.4 ms per classification (A100 GPU, 512 tokens) (86M/MODEL_CARD.md@172c1074:74) @@L@@
• 22M row: AUC English .995, recall at 1% FPR English 88.7%, AUC multilingual .942, latency 19.3 ms (A100 GPU, 512 tokens) (86M/MODEL_CARD.md@172c1074:75) @@L@@
• Source conflict: the paper's table prints the 86M English AUC as ".98" (card: ".998"); the other cells match the card (arXiv 2505.03574 section 4.1) @@D@@
• Multilingual set: "the same dataset machine-translated into eight additional languages" (arXiv 2505.03574 appendix A.2) @@D@@
• AgentDojo attack prevention rate at 3% utility reduction: 81.2% for 86M and 78.4% for 22M (86M/MODEL_CARD.md@172c1074:86-87) @@L@@
• Paper, 86M alone on AgentDojo: attack success rate "17.6%" without defences, "7.5%, a 57% drop" with Prompt Guard 2 86M, utility 47.7% to 47.0% (arXiv 2505.03574 section 4.3) @@D@@
• Paper, 22M: "a 41% drop in ASR with no utility degradation" (arXiv 2505.03574 appendix B.2) @@D@@
• Comparators (Detail only): Prompt Guard 1 has AUC .987, recall 21.2%, 92.4 ms and APR 67.6%; ProtectAI 22.2%, Deepset 13.5% and LLM Warden 12.9% APR (86M/MODEL_CARD.md@172c1074:73,85,88-90) @@L@@
• Latency on a CPU or on other GPUs (checked the card, docs pages and paper; the paper says only that it "can be easily deployed locally on both CPU and GPU") @@N@@
### R6
Summary: **One string of up to 512 tokens.** Longer text must be split by the caller and scored in parallel. Using the weights needs approved gated access on Hugging Face plus Transformers and PyTorch. @@D@@
Detail:
• Window: "Both Llama Prompt Guard 2 models support a 512-token context window." (86M/MODEL_CARD.md@172c1074:24) @@L@@
• Docs page: "We recommend splitting longer prompts into segments and scanning each in parallel to detect the presence of violations anywhere in the longer prompts." (dev.meta.ai Prompt Guard page, read 2026-10-09) @@D@@
• Meta points to inference utilities "for efficiently running Prompt Guard in parallel on long inputs, such as extended strings and documents" in the llama-cookbook repo (not read) (86M/MODEL_CARD.md@172c1074:118) @@L@@
• Libraries in the card's examples: transformers (pipeline, AutoTokenizer, AutoModelForSequenceClassification) and torch; versions are not stated (86M/MODEL_CARD.md@172c1074:31-56) @@L@@
• Access: the weights are gated, "Log in or Sign Up to review the conditions and access this model content" (HF 86M gate page, read 2026-10-09) @@D@@
• The gate requires accepting the Llama 4 Community License Agreement, which incorporates the Acceptable Use Policy by reference (HF 86M gate page, read 2026-10-09) @@D@@
• Hardware: the published latency is for an A100 GPU at 512 tokens; the paper says the models run locally "on both CPU and GPU" (86M/MODEL_CARD.md@172c1074:71) @@L@@
• Input language: the evaluated set is English, French, German, Hindi, Italian, Portuguese, Spanish and Thai (86M/MODEL_CARD.md@172c1074:25) @@L@@
• Memory footprint and batch throughput (checked the card, docs page and paper; not given) @@N@@
• The Llama-Prompt-Guard-2 README download section is empty and its examples point to a "facebookresearch/llama-recipes" repo (Llama-Prompt-Guard-2/README.md@172c1074:7,20) @@L@@
### R7
Summary: **Minimum setup:** request gated access to the 22M or 86M model on Hugging Face, load it with the Transformers text-classification pipeline, and score a labelled set of benign prompts, jailbreaks and injected retrieved text. No API key or service is needed once the weights are local. @@I@@
Detail:
• **Minimum setup:** accept the Llama 4 licence on Hugging Face for the 22M model (English) or 86M (multilingual), install transformers and torch, load with the text-classification pipeline, and run each test string through it (premise: the card's usage section and the gate page) @@I@@
• Test set for Table 3: a prompt-attack set with benign prompts, jailbreaks, explicit override instructions and injected passages inside retrieved text or tool output, labelled malicious only when they try to override instructions (premise: the card's intent-only scope) @@I@@
• Cover the evaluated languages and add long inputs above 512 tokens, scored whole and split into segments, to measure the window effect (premise: the card's 512-token guidance) @@I@@
• Compare both sizes on the same set and sweep a score cut-off to read recall at a fixed false-positive rate, since Meta gives no cut-off (premise: the card's 1% FPR operating point) @@I@@
• Negative controls: harmful but non-override prompts should score benign if the intent-only scope holds (premise: the card's scope text) @@I@@
• Everything runs locally after the download; no Together or Meta service is called, so no test data leaves the machine (premise: the card's local Transformers usage) @@I@@
### R8
Summary: **Key open questions.** No recommended threshold, a private benchmark, no CPU latency, untested behaviour on tool and retrieved text, and whether the Llama 4 use policy affects attack-prompt testing.
Detail:
• Recommended decision threshold for the benign or malicious score (checked the card, README, docs pages, protections page and paper; not stated)
• How well the model works on retrieved text, tool output and memory text, which Meta calls "untrusted data" but does not evaluate separately (needs testing)
• Detection of paraphrased, encoded, obfuscated or very long jailbreaks beyond "explicit" override intent (needs testing)
• Actual 22M versus 86M gap on non-English prompts, since only the 22M multilingual weakness is stated in words and the card gives AUC .942 against .995 (needs testing)
• CPU latency, memory use and throughput (needs testing)
• Whether the Hugging Face model card body equals the repo MODEL_CARD.md; the card body returns HTTP 401 without approved access, so the repo file was used
• The paper prints an 86M English AUC of ".98" and the card prints ".998"; which is correct is not stated
• Why the Hugging Face parameter totals (278.8M and 70.8M) exceed the card's 86M and 22M backbone figures (checked the card and paper; no explanation)
• Whether the Llama 4 Acceptable Use Policy limits using attack and jailbreak prompts to test the model: it bars using Llama 4 to "intentionally circumvent or remove usage restrictions or other safety measures" (USE_POLICY.md line 37), and no clause names security testing (licensing question)
• Whether the 700 million monthly-active-user clause in the Llama 4 licence matters for the bench owner's organisation (licensing question)
• Whether the Prompt Guard docs page example helper get_jailbreak_score matches the cookbook inference file, which was not read
### R9
Summary: Meta Prompt Guard model cards and licence files in the PurpleLlama repo, Meta docs pages, Hugging Face gate pages and metadata, and the LlamaFirewall paper.
Detail:
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard
• https://dev.meta.ai/llama/llama-protections
• @@B@@Llama-Prompt-Guard-2/86M/MODEL_CARD.md
• @@B@@Llama-Prompt-Guard-2/README.md
• @@B@@Llama-Prompt-Guard-2/86M/LICENSE
• @@B@@LlamaFirewall/README.md
• @@B@@LlamaFirewall/src/llamafirewall/scanners/promptguard_utils.py
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M/tree/a8ded8e697ce7c355e395a0df51f94adb4a2fd27
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M/tree/11614a155199674a0a95e6602d6ab0417b790ed0
• https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-86M
• https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-22M
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M
• https://arxiv.org/html/2505.03574
