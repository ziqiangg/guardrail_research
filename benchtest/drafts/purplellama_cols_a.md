## Column PL1: Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection)
### R1
Summary: **Input-level prompt-attack classification.** Prompt Guard 2 is a small BERT-style model that labels a text string benign or malicious, aimed at prompt injection and jailbreak attempts. It ships in 86M and 22M sizes under the Llama 4 licence. **[Documented]**
Detail:
• Both Llama Prompt Guard 2 models "detect both prompt injection and jailbreaking attacks, trained on a large corpus of known vulnerabilities" (86M/MODEL_CARD.md@172c1074:11) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta docs page wording: "Both models detect prompt injection and jailbreaking attacks, and are trained on a large corpus of known vulnerabilities." (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Protections page wording: "Prompt Guard is a powerful tool for protecting LLM powered applications from malicious prompts to ensure their security and integrity." (dev.meta.ai llama-protections, read 2026-10-09) **[Documented]**
• Two models: Llama Prompt Guard 2 86M (base model mDeBERTa-base) and a smaller 22M (DeBERTa-xsmall) (86M/MODEL_CARD.md@172c1074:4,63) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta presents version 2 as a replacement: "can be used as a drop-in replacement for Prompt Guard for all use cases", and "Developers should migrate to Llama Prompt Guard 2" (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Model type: "Llama Prompt Guard 2 are BERT models that output only labels; unlike Llama Guard, Llama Prompt Guard 2 doesn't need a specific prompt structure or configuration." (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Meta writes the name three ways: "Llama Prompt Guard 2" (model card and docs page), "Prompt Guard 2" (protections page) and "PromptGuard 2" (LlamaFirewall docs and paper) (pages named, read 2026-10-09) **[Documented]**
### R2
Summary: **Explicit instruction-override attempts.** The model flags prompts that explicitly try to override earlier instructions, whether jailbreaks or injected instructions in untrusted text, regardless of harm. There is no injection sub-label, and eight languages were evaluated. **[Documented]**
Detail:
• Attack types: prompt injections "manipulate untrusted third-party and user data in the context window to make a model execute unintended instructions"; jailbreaks are "malicious instructions designed to override the safety and security features directly built into a model" (86M/MODEL_CARD.md@172c1074:8-9) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Scope: "classify prompts as 'malicious' if the prompt explicitly attempts to override prior instructions embedded into or seen by an LLM" (86M/MODEL_CARD.md@172c1074:22) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Intent only: the classification "considers only the intent to supersede developer or user instructions, regardless of whether the prompt is potentially harmful or the attack is likely to succeed" (86M/MODEL_CARD.md@172c1074:22) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• No injection sub-label: "we don't include a specific 'injection' label to detect prompts that may cause unintentional instruction-following" (86M/MODEL_CARD.md@172c1074:23) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Paper: Prompt Guard 2 is "designed to detect explicit jailbreaking techniques in LLM inputs"; Prompt Guard 1 "attempted broader goal hijacking detection", which caused "excessive false positives" (arXiv 2505.03574 section 4.1 and appendix B) **[Documented]**
• Wording differs by source: the LlamaFirewall README calls it a detector of "direct prompt injection attempts" and the LlamaFirewall docs page says "direct jailbreak attempts", while the model card says both injection and jailbreak (LlamaFirewall/README.md@172c1074:27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Examples named by the card: "variants of 'ignore previous instructions'" and DAN prompts (86M/MODEL_CARD.md@172c1074:98-99) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages evaluated: "English, French, German, Hindi, Italian, Portuguese, Spanish, and Thai"; the 86M model "uses a multilingual base model and is trained to detect both English and non-English injections and jailbreaks" (86M/MODEL_CARD.md@172c1074:25) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• 22M is weaker on other languages: "There is no version of deberta-xsmall with multilingual pretraining available" (86M/MODEL_CARD.md@172c1074:106) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta advice on language fit: "Developers in resource constrained environments and focused only on English text will likely prefer the 22M model" (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Adversarial tokenisation is addressed: the tokenizer was refined "to mitigate adversarial tokenization attacks, such as whitespace manipulations and fragmented tokens" (86M/MODEL_CARD.md@172c1074:17) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Stated limitations: "adversaries may develop sophisticated attacks specifically to bypass detection", and some attacks "are highly application-dependent" (86M/MODEL_CARD.md@172c1074:104-105) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Not a harmful-content classifier: the card positions it beside "harmful content guardrails", and the intent-only scope above excludes harm judgement (premise: 86M/MODEL_CARD.md@172c1074:99). Harmful-content classification is the Llama Guard columns V to Z **[Inferred]**
• Training languages and an attack taxonomy beyond the two categories (checked the model card, the Prompt Guard docs page, the protections page and paper appendix B; only the evaluation languages are listed) **[Not disclosed]**
### R3
Summary: **A single text string, with no direction setting.** The model receives one string and labels it. Meta describes it as meant for user prompts and untrusted data such as web content. **[Documented]**
Detail:
• Input: "The input is a string that the model labels as 'benign' or 'malicious'." (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• The card's usage passes one string to the classifier or tokenizer, with no message roles or conversation structure (86M/MODEL_CARD.md@172c1074:35,48-49) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Intended inputs: it "operates on user inputs and untrusted content such as web data" (LlamaFirewall/README.md@172c1074:27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Same scope in the paper: it "operates in real-time on user prompts and untrusted data sources" (arXiv 2505.03574 section 1) **[Documented]**
• Retrieved and tool text: the paper's AgentDojo test scanned messages with role user or tool: "For PromptGuard, we analyze only messages with the role of user or tool" (arXiv 2505.03574 section 4.3) **[Documented]**
• The model has no input-or-output flag and takes no system prompt or other context, so it applies to any text passed to it, such as prompts, retrieved passages, tool outputs or memory text (premise: the card and docs page describe a string-in, label-out model) **[Inferred]**
• Scanning model responses with Prompt Guard 2: no page describes it (checked the model card, Llama-Prompt-Guard-2 README, Prompt Guard docs page, protections page, LlamaFirewall README, docs and paper) **[Not disclosed]**
• Contrast with Llama Guard (columns V to Z): Prompt Guard 2 "doesn't need a specific prompt structure or configuration" (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Long inputs must be split by the caller: "For longer inputs, split prompts into segments and scan them in parallel to ensure violations are detected." (86M/MODEL_CARD.md@172c1074:24) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R4
Summary: **Small DeBERTa classifiers, run locally.** Two fine-tuned models, 86M on mDeBERTa-base and 22M on DeBERTa-xsmall, trained with an energy-based loss. Training used a mix of open-source and synthetic data. **[Documented]**
Detail:
• Base models: "mDeBERTa-base for the base version of Llama Prompt Guard 2 86M, and DeBERTa-xsmall as the base model for Llama Prompt Guard 2 22M. Both are open-source, MIT-licensed models from Microsoft." (86M/MODEL_CARD.md@172c1074:63) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Paper confirms the families: "mDeBERTa-base (86M parameters) and DeBERTa-xsmall (22M parameters)" (arXiv 2505.03574 section 4.1) **[Documented]**
• Training objective: "a modified energy-based loss function"; the card describes a penalty "for large negative energy predictions on benign prompts" (86M/MODEL_CARD.md@172c1074:61) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Training data: a "mix of open-source datasets" plus "our own synthetic injections and data from red-teaming earlier versions of Prompt Guard" (86M/MODEL_CARD.md@172c1074:60) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Training data sizes, dataset names and class balance (checked the model card, docs page and paper appendix B; not given) **[Not disclosed]**
• Parameter counts: the card lists "Backbone Parameters" 86M and 22M; the Hugging Face metadata lists 278,810,882 F32 parameters for the 86M repo (86M revision a8ded8e6, HF API, read 2026-10-09) **[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**
• The 22M repo metadata lists 70,830,722 F32 parameters (22M revision 11614a15, HF API, read 2026-10-09) **[Documented: repo meta-llama/Llama-Prompt-Guard-2-22M@11614a15]**
• The gap between card and metadata counts is not explained on any page read; the likely cause is that the card counts only the transformer backbone and the metadata counts the embedding tables too (premise: the card column is headed "Backbone Parameters") **[Inferred]**
• Serving route: load locally with the Transformers pipeline ("text-classification") or with `AutoTokenizer` and `AutoModelForSequenceClassification`; the card's example prints the predicted label from model.config.id2label (86M/MODEL_CARD.md@172c1074:29-56) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Docs page example calls a helper named `get_jailbreak_score` from the llama-cookbook inference utilities (source file inference.py not read) (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Hosted endpoint: the Hugging Face metadata marks the 86M repo as served by an inference provider (inference "warm") (86M revision a8ded8e6, HF API, read 2026-10-09) **[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**
• The 22M page shows "This model isn't deployed by any Inference Provider." (HF 22M page, read 2026-10-09) **[Documented]**
• A Meta-run hosted Prompt Guard 2 endpoint (checked the Prompt Guard docs page, protections page, repo README and LlamaFirewall docs; none names one) **[Not disclosed]**
• Pin kinds are separate. Repo commit 172c1074069eb88ec834124272c1b1c4f8893445, author date 2026-09-29 (git, read 2026-10-09) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Hugging Face revision a8ded8e697ce7c355e395a0df51f94adb4a2fd27 for the 86M repo, last modified 2025-04-29, access "manual" (HF API, read 2026-10-09) **[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**
• Hugging Face revision 11614a155199674a0a95e6602d6ab0417b790ed0 for the 22M repo, last modified 2025-04-29, access "manual" (HF API, read 2026-10-09) **[Documented: repo meta-llama/Llama-Prompt-Guard-2-22M@11614a15]**
• Release notes or changelog for Prompt Guard 2 (checked the repo at the pin: no tags and no CHANGELOG file; the card has a "Summary of Changes from Prompt Guard 1" only) **[Not disclosed]**
• Licence: "The same license as Llama 4 applies: see the LICENSE file, as well as our accompanying Acceptable Use Policy" (Llama-Prompt-Guard-2/README.md@172c1074:45) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The 86M and 22M LICENSE files are the Llama 4 Community License Agreement (Version Effective Date April 5, 2025) and contain an "Additional Commercial Terms" clause at 700 million monthly active users (86M/LICENSE@172c1074:22) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Hugging Face metadata: licence "other" with name "llama4"; the gate page shows "License: llama4" (86M revision a8ded8e6, HF API, read 2026-10-09) **[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**
• Gate: access is "manual"; the form asks for "your full legal name, date of birth, and full organization name with all corporate identifiers" (HF 86M gate page, read 2026-10-09) **[Documented]**
• Fine-tuning is recommended: "For optimal results, we recommend a methodology of fine-tuning the model on application-specific data." (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Engine and wrapper: the LlamaFirewall PromptGuard scanner (column PL2) loads "meta-llama/Llama-Prompt-Guard-2-86M" by default (promptguard_utils.py@172c1074:40) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R5
Summary: **A benign or malicious label with a score.** Meta publishes AUC, recall at 1% false positives and A100 latency from a private benchmark. The 86M model reports 97.5% recall and 92.4 ms; the 22M model 88.7% and 19.3 ms. **[Documented]**
Detail:
• Labels: the model labels prompts "benign" or "malicious"; "Both Prompt Guard 2 models focus on detecting explicit, known attack patterns" (86M/MODEL_CARD.md@172c1074:18) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The card's example prints "MALICIOUS" from model.config.id2label (86M/MODEL_CARD.md@172c1074:54-55) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The docs page example prints a jailbreak score of 0.001 for a benign text and 1.000 for an injection text (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Recommended decision threshold or score cut-off (checked the model card, Llama-Prompt-Guard-2 README, Prompt Guard docs page, protections page, LlamaFirewall README, docs pages and paper; none gives one) **[Not disclosed]**
• Operating point used by Meta: the card reports "Recall @ 1% FPR"; the paper picks "a threshold for each model that produces a fixed, minimal utility reduction (3%)" on AgentDojo, and does not print the threshold values (arXiv 2505.03574 section 4.1) **[Documented]**
• Benchmark conditions: "a private benchmark built with datasets distinct from those used in training" (86M/MODEL_CARD.md@172c1074:69) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Benchmark size and class balance (checked the card and paper appendix A.2; not given beyond an English set and a machine-translated multilingual set) **[Not disclosed]**
• 86M row: AUC English .998, recall at 1% FPR English 97.5%, AUC multilingual .995, latency 92.4 ms per classification (A100 GPU, 512 tokens) (86M/MODEL_CARD.md@172c1074:74) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• 22M row: AUC English .995, recall at 1% FPR English 88.7%, AUC multilingual .942, latency 19.3 ms (A100 GPU, 512 tokens) (86M/MODEL_CARD.md@172c1074:75) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict: the paper's table prints the 86M English AUC as ".98" (card: ".998"); the other cells match the card (arXiv 2505.03574 section 4.1) **[Documented]**
• Multilingual set: "the same dataset machine-translated into eight additional languages" (arXiv 2505.03574 appendix A.2) **[Documented]**
• AgentDojo attack prevention rate at 3% utility reduction: 81.2% for 86M and 78.4% for 22M (86M/MODEL_CARD.md@172c1074:86-87) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Paper, 86M alone on AgentDojo: attack success rate "17.6%" without defences, "7.5%, a 57% drop" with Prompt Guard 2 86M, utility 47.7% to 47.0% (arXiv 2505.03574 section 4.3) **[Documented]**
• Paper, 22M: "a 41% drop in ASR with no utility degradation" (arXiv 2505.03574 appendix B.2) **[Documented]**
• Comparators (Detail only): Prompt Guard 1 has AUC .987, recall 21.2%, 92.4 ms and APR 67.6%; ProtectAI 22.2%, Deepset 13.5% and LLM Warden 12.9% APR (86M/MODEL_CARD.md@172c1074:73,85,88-90) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Latency on a CPU or on other GPUs (checked the card, docs pages and paper; the paper says only that it "can be easily deployed locally on both CPU and GPU") **[Not disclosed]**
### R6
Summary: **One string of up to 512 tokens.** Longer text must be split by the caller and scored in parallel. Using the weights needs approved gated access on Hugging Face plus Transformers and PyTorch. **[Documented]**
Detail:
• Window: "Both Llama Prompt Guard 2 models support a 512-token context window." (86M/MODEL_CARD.md@172c1074:24) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Docs page: "We recommend splitting longer prompts into segments and scanning each in parallel to detect the presence of violations anywhere in the longer prompts." (dev.meta.ai Prompt Guard page, read 2026-10-09) **[Documented]**
• Meta points to inference utilities "for efficiently running Prompt Guard in parallel on long inputs, such as extended strings and documents" in the llama-cookbook repo (not read) (86M/MODEL_CARD.md@172c1074:118) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Libraries in the card's examples: transformers (pipeline, `AutoTokenizer`, `AutoModelForSequenceClassification`) and torch; versions are not stated (86M/MODEL_CARD.md@172c1074:31-56) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Access: the weights are gated, "Log in or Sign Up to review the conditions and access this model content" (HF 86M gate page, read 2026-10-09) **[Documented]**
• The gate requires accepting the Llama 4 Community License Agreement, which incorporates the Acceptable Use Policy by reference (HF 86M gate page, read 2026-10-09) **[Documented]**
• Hardware: the published latency is for an A100 GPU at 512 tokens; the paper says the models run locally "on both CPU and GPU" (86M/MODEL_CARD.md@172c1074:71) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Input language: the evaluated set is English, French, German, Hindi, Italian, Portuguese, Spanish and Thai (86M/MODEL_CARD.md@172c1074:25) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Memory footprint and batch throughput (checked the card, docs page and paper; not given) **[Not disclosed]**
• The Llama-Prompt-Guard-2 README download section is empty and its examples point to a "facebookresearch/llama-recipes" repo (Llama-Prompt-Guard-2/README.md@172c1074:7,20) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R7
Summary: **Minimum setup:** request gated access to the 22M or 86M model on Hugging Face, load it with the Transformers text-classification pipeline, and score a labelled set of benign prompts, jailbreaks and injected retrieved text. No API key or service is needed once the weights are local. **[Inferred]**
Detail:
• **Minimum setup:** accept the Llama 4 licence on Hugging Face for the 22M model (English) or 86M (multilingual), install transformers and torch, load with the text-classification pipeline, and run each test string through it (premise: the card's usage section and the gate page) **[Inferred]**
• Test set for Table 3: a prompt-attack set with benign prompts, jailbreaks, explicit override instructions and injected passages inside retrieved text or tool output, labelled malicious only when they try to override instructions (premise: the card's intent-only scope) **[Inferred]**
• Cover the evaluated languages and add long inputs above 512 tokens, scored whole and split into segments, to measure the window effect (premise: the card's 512-token guidance) **[Inferred]**
• Compare both sizes on the same set and sweep a score cut-off to read recall at a fixed false-positive rate, since Meta gives no cut-off (premise: the card's 1% FPR operating point) **[Inferred]**
• Negative controls: harmful but non-override prompts should score benign if the intent-only scope holds (premise: the card's scope text) **[Inferred]**
• Everything runs locally after the download; no Together or Meta service is called, so no test data leaves the machine (premise: the card's local Transformers usage) **[Inferred]**
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
• Whether the Prompt Guard docs page example helper `get_jailbreak_score` matches the cookbook inference file, which was not read
### R9
Summary: Meta Prompt Guard model cards and licence files in the PurpleLlama repo, Meta docs pages, Hugging Face gate pages and metadata, and the LlamaFirewall paper.
Detail:
• https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard
• https://dev.meta.ai/llama/llama-protections
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/86M/MODEL_CARD.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/86M/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/promptguard_utils.py
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M/tree/a8ded8e697ce7c355e395a0df51f94adb4a2fd27
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M/tree/11614a155199674a0a95e6602d6ab0417b790ed0
• https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-86M
• https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-22M
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
• https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M
• https://arxiv.org/html/2505.03574
## Column PL2: LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner)
### R1
Summary: **Input-level prompt-attack scanning in LlamaFirewall.** The PromptGuard scanner runs the Prompt Guard 2 86M model on a message's text and returns allow or block with a score. The block threshold defaults in code to 0.9, and the message role decides whether it runs. **[Documented]**
Detail:
• The scanner wraps the Prompt Guard 2 model: "PromptGuard 2 is a fine-tuned BERT-style model designed to detect direct jailbreak attempts in real-time" (LlamaFirewall/website/docs/documentation/scanners/prompt-guard-2.md@172c1074:4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Code: class `PromptGuardScanner`, scanner name "Prompt Guard Scanner", block threshold parameter default 0.9 (prompt_guard_scanner.py@172c1074:19-28) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Decision rule: "`ScanDecision`.`BLOCK` if score >= self.`block_threshold` else `ScanDecision`.`ALLOW`" (prompt_guard_scanner.py@172c1074:39) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Selected in configuration by the scanner type `PROMPT_GUARD` (llamafirewall_data_types.py@172c1074:15) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Role of the wrapper versus the model: the wrapper adds role configuration, a decision with a reason and score, model download and aggregation with other scanners; the classification itself is the Prompt Guard 2 model described in column PL1 (premise: code files named in this column) **[Inferred]**
• Framework description: "LlamaFirewall is a framework designed to detect and mitigate AI centric security risks, supporting multiple layers of inputs and outputs" (LlamaFirewall/README.md@172c1074:2) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Names: the README feature list says "`PromptGuardScanner`" (line 12) and its architecture section says "PromptGuard 2" (LlamaFirewall/README.md@172c1074:26) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R2
Summary: **Jailbreak and injection phrasing in text.** The scanner catches explicit instruction-override attempts in user prompts and untrusted content such as web data. Meta lists direct and indirect universal jailbreaks as covered risks. Goal hijacking is left to AlignmentCheck. **[Documented]**
Detail:
• Risks covered: "Direct Universal Jailbreak Prompt Injections" and "Indirect Universal Jailbreak Prompt Injections" (prompt-guard-2.md@172c1074:15-16) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Layered risk: PromptGuard 2 "along with other scanners, provides a layered defense against code-oriented prompt injection" (prompt-guard-2.md@172c1074:17) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Intended inputs: it "operates on user inputs and untrusted content such as web data" (LlamaFirewall/README.md@172c1074:27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Scope wording differs: README "detects direct prompt injection attempts" (line 27), docs page "direct jailbreak attempts" (prompt-guard-2.md line 4), model card both injection and jailbreak (PL1 column) (LlamaFirewall/README.md@172c1074:27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Narrow scope from the model card: a prompt is malicious only if it "explicitly attempts to override prior instructions" (Llama-Prompt-Guard-2/86M/MODEL_CARD.md@172c1074:22) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Goal hijacking is assigned to another scanner: AlignmentCheck "detect[s] goal hijacking, indirect prompt injections, and signs of agent misalignment" (LlamaFirewall/README.md@172c1074:33) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Docs mapping: "PromptGuard and Regex scanner detect jailbreak input" for direct and indirect universal jailbreaks (workflow-and-detection-components.md@172c1074:9) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages: the scanner always loads the 86M model, which is the multilingual one; the card lists eight evaluated languages (promptguard_utils.py@172c1074:40) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Out of scope: the scanner does not read tool-call arguments, only message content (premise: no scanner file reads the `tool_calls` field; grep of LlamaFirewall/src found it only in llamafirewall_data_types.py) **[Inferred]**
• Block reasons include the full scanned text, so the blocked prompt is echoed in the result: reason string "Full text: \"{text}\"" (prompt_guard_scanner.py@172c1074:43) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R3
Summary: **Whatever text a configured role carries.** The scanner reads only the message content, ignores the trace, and can be attached to any role. Defaults scan USER and TOOL messages; the chat-bot use case adds SYSTEM. **[Documented]**
Detail:
• Reads one field: "text = message.content"; the past trace argument is accepted but unused (prompt_guard_scanner.py@172c1074:31-34) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Roles are an enum: `TOOL` (tool output), `USER` (user input), `ASSISTANT` (LLM output), `MEMORY`, `SYSTEM` (system input) (llamafirewall_data_types.py@172c1074:34-39) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• A configuration maps each role to a list of scanner types: "Configuration: TypeAlias = Mapping[Role, Sequence[`ScannerType` | str]]" (config.py@172c1074:13) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• No-config default: `TOOL` scans `CODE_SHIELD` and `PROMPT_GUARD`, `USER` scans `PROMPT_GUARD`, `SYSTEM` none, `ASSISTANT` scans `CODE_SHIELD`, `MEMORY` none (llamafirewall.py@172c1074:90-96) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• `CHAT_BOT` use case: `PROMPT_GUARD` for `USER` and `SYSTEM` (config.py@172c1074:22-25) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• README example attaches it to `USER` only (LlamaFirewall/README.md@172c1074:72) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Direction (R002): there is no separate input or output scanner; the same scanner can be attached to any role, so prompts, tool outputs, retrieved text in `TOOL` or `MEMORY` messages, and assistant text are all reachable by configuration (premise: config.py and llamafirewall.py) **[Inferred]**
• Meta's own AgentDojo evaluation scanned only user and tool messages with it (arXiv 2505.03574 section 4.3) **[Documented]**
• Use on assistant output: no page recommends or evaluates it on the `ASSISTANT` role (checked the README, docs pages and paper) **[Not disclosed]**
• The message type has an optional `tool_calls` field, but this scanner does not read it, so function-call arguments are not scanned (premise: prompt_guard_scanner.py reads message.content only) **[Inferred]**
• The framework selects scanners by the message role: "scanners = self.scanners.get(input.role, [])" (llamafirewall.py@172c1074:113) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Name conflict: the custom use case page uses `ScannerType`.`PROMPT_INJECTION` for `CHAT_BOT` (adding-custom-use-case.md@172c1074:19-20) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Code and the how-to page use `PROMPT_GUARD`, and `PROMPT_INJECTION` is not in the `ScannerType` enum, so the live name is `PROMPT_GUARD` (llamafirewall_data_types.py@172c1074:13-19) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R4
Summary: **A Python wrapper around the 86M model, downloaded on first use.** The scanner loads Prompt Guard 2 86M through Transformers, cleans whitespace, truncates to 512 tokens and takes the last class probability as the score. It ships in the llamafirewall package. **[Documented]**
Detail:
• Model: "meta-llama/Llama-Prompt-Guard-2-86M" is the default and the scanner has no argument to pick the 22M model (promptguard_utils.py@172c1074:40) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Selecting the 22M model needs a code change (premise: the constructor of the scanner and of the PromptGuard class take no model argument) **[Inferred]**
• Local copy: path is $`HF_HOME` joined with the model name with "/" replaced by "--"; `HF_HOME` defaults to "~/.cache/huggingface" if unset (promptguard_utils.py@172c1074:43-50) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• If the folder is missing the code logs "We are downloading it from Hugging Face Hub. This may take a while..." and calls login() when no token is found (promptguard_utils.py@172c1074:54-61) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• After download it saves the model and tokenizer to the local path for later runs (promptguard_utils.py@172c1074:63-69) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Runs on CUDA when available, otherwise CPU (promptguard_utils.py@172c1074:33-36) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Preprocessing: removes whitespace, re-tokenises and rebuilds the text before scoring; on an exception it returns the original text (promptguard_utils.py@172c1074:79-102) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Truncation: "padding=True, truncation=True, `max_length`=512" (promptguard_utils.py@172c1074:113) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Score: softmax of the logits at temperature 1.0 and "probabilities[0, -1].item()", the last class probability (promptguard_utils.py@172c1074:104-129) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The last class is taken to be "malicious" (premise: the card lists two labels, benign then malicious, and the Hugging Face config is not readable without approved access) **[Inferred]**
• The framework builds a new scanner object for each scan call, which loads the model from disk each time (premise: `create_scanner` is called inside scan at llamafirewall.py line 118 and the scanner constructor builds PromptGuard); reuse of one loaded model is not shown **[Inferred]**
• Package versions: llamafirewall 1.0.3 in the repo (LlamaFirewall/pyproject.toml@172c1074:7) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PyPI simple index lists llamafirewall 1.0.3 as the latest file (PyPI simple index, observed 2026-10-09) **[Documented]**
• Dependencies include torch>=2.4.1, transformers>=4.51.3 and `huggingface_hub`>=0.30.2 (LlamaFirewall/pyproject.toml@172c1074:15-22) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Python 3.10 or later is required (LlamaFirewall/README.md@172c1074:53) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• LlamaFirewall code is MIT licensed; the model keeps its own Llama 4 licence, see column PL1 (LlamaFirewall/LICENSE@172c1074:1) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Release notes for llamafirewall (checked the repo at the pin: no tags and no CHANGELOG file; PyPI lists versions 1.0.2 and 1.0.3 without notes) **[Not disclosed]**
### R5
Summary: **Allow or block with a reason and a probability score.** A score at or above the block threshold blocks. The default threshold of 0.9 is a code value. Model figures come from the Prompt Guard 2 card. **[Documented]**
Detail:
• Result object: `ScanResult` with fields decision, reason, score and status (llamafirewall_data_types.py@172c1074:43-47) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Decision values: `ALLOW`, `HUMAN_IN_THE_LOOP_REQUIRED`, `BLOCK`; this scanner returns only `ALLOW` or `BLOCK` (llamafirewall_data_types.py@172c1074:22-25) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Allow reason text is "No prompt injection detected"; the block reason names the probability and echoes the text (prompt_guard_scanner.py@172c1074:20,42-46) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Default block threshold 0.9 is a code default (prompt_guard_scanner.py@172c1074:24) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• A Meta-recommended threshold for the scanner or model (checked the README, docs pages, tutorials, paper and model card; none gives one) **[Not disclosed]**
• Single scanner on a role: the framework returns that scanner's result, with its own reason and score (llamafirewall.py@172c1074:134-140) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Several scanners on a role: `BLOCK` wins if any scanner blocks, otherwise the decision with the highest score; reasons are joined with "; " (llamafirewall.py@172c1074:142-167) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Async path: `scan_async` returns the first `BLOCK` or `HUMAN_IN_THE_LOOP_REQUIRED` result, else `ALLOW` with reason "default" and score 0.0 (llamafirewall.py@172c1074:174-187) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Docs sample output shows reason='default' and score=0.0 for a benign input, and reason='`prompt_guard`' and score=0.95 for a blocked one (how-to-use-llamafirewall.md@172c1074:86-89) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Code behaviour differs from that sample: for a single scanner the reason is the scanner's own text (for example "No prompt injection detected") and the benign score is the model probability (llamafirewall.py@172c1074:134-140) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Model numbers behind the scanner: AUC .998, recall at 1% FPR 97.5% and 92.4 ms on an A100 for the 86M model, on a private benchmark (Llama-Prompt-Guard-2/86M/MODEL_CARD.md@172c1074:74) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Paper, AgentDojo with Prompt Guard 2 86M on user and tool messages: attack success rate 17.6% to 7.5%, utility 47.7% to 47.0% (arXiv 2505.03574 section 4.3) **[Documented]**
• Scanner or framework latency and throughput (checked the README, which says only "Real-Time", the docs pages and the paper; no figure is given for this scanner) **[Not disclosed]**
• The scanner reports the model probability directly with no calibration or confidence interval (premise: promptguard_utils.py takes the softmax value as the score) **[Inferred]**
### R6
Summary: **A Message with role and text content, plus gated model access.** Weights are downloaded from Hugging Face on first use, with an interactive login if no token exists. Python 3.10 or later is needed, and text over 512 tokens is truncated. **[Documented]**
Detail:
• Input object: Message(role, content) with helper classes `UserMessage`, `SystemMessage`, `AssistantMessage`, `ToolMessage` and `MemoryMessage` (llamafirewall_data_types.py@172c1074:50-92) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Only content is scanned and truncated at 512 tokens, so any text after the window is not scored (premise: promptguard_utils.py line 113 truncates; no splitting code was found in LlamaFirewall/src) **[Inferred]**
• The model card advises splitting long inputs into segments; the scanner does not do this (Llama-Prompt-Guard-2/86M/MODEL_CARD.md@172c1074:24) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Access: the Hugging Face repo is gated, and without a token the code calls login() which prompts interactively (promptguard_utils.py@172c1074:57-61) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Interactive login may block a headless test run unless a token is already set (premise: promptguard_utils.py line 61) **[Inferred]**
• Setup helper: "llamafirewall configure" checks local models, offers to download them and checks API keys (LlamaFirewall/README.md@172c1074:147-154) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The configure helper's default model is "meta-llama/Llama-Prompt-Guard-2-86M" (LlamaFirewall/src/llamafirewall/cli/configure.py@172c1074:21) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Parallel use: set "export `TOKENIZERS_PARALLELISM`=true" (LlamaFirewall/README.md@172c1074:171) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Prerequisite text says "Access to HuggingFace Meta's Llama 3.1 models & evals", which does not name the Llama 4 licence that the model files carry (LlamaFirewall/README.md@172c1074:55) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The synchronous scan call uses asyncio.run, which fails inside a running event loop; use `scan_async` there (premise: llamafirewall.py line 122 and Python behaviour) **[Inferred]**
• No scanner timeout or size limit is set in code beyond the 512-token truncation (premise: reading prompt_guard_scanner.py and promptguard_utils.py) **[Inferred]**
### R7
Summary: **Minimum setup:** install llamafirewall, accept the Llama 4 licence on Hugging Face so the 86M model can download, configure a USER role with the PromptGuard scanner, and scan labelled strings. Set the threshold explicitly and test other roles for retrieved text and tool output. **[Inferred]**
Detail:
• **Minimum setup:** pip install llamafirewall on Python 3.10 or later, get approved access to the 86M model on Hugging Face, run llamafirewall configure or log in so the first scan can download it, then call scan on `UserMessage` objects (premise: README and promptguard_utils.py) **[Inferred]**
• Table 3 input type: prompts, plus retrieved passages and tool outputs wrapped as `TOOL` or `MEMORY` messages, each with a benign or attack label (premise: roles in llamafirewall_data_types.py) **[Inferred]**
• Record the score for every case, not only the decision, so that thresholds from 0.5 to 0.99 can be compared with the 0.9 default (premise: the score field in `ScanResult`) **[Inferred]**
• Compare scan on `USER` with the model run directly (column PL1) to confirm the wrapper adds no differences beyond whitespace cleaning and truncation (premise: preprocessing code) **[Inferred]**
• Time the first scan separately from later scans, because model loading may happen on every call (premise: `create_scanner` inside scan) **[Inferred]**
• No Together key is needed for this scanner; the key is for AlignmentCheck and the LLM-prompt scanners (premise: README setup text and scanner files) **[Inferred]**
### R8
Summary: **Key open questions.** No recommended threshold, unknown scanner latency, model reloading per call, silent truncation of long text, and a docs sample output that differs from the code.
Detail:
• Recommended block threshold, and how the 0.9 default relates to the model's 1% false-positive operating point (checked the README, docs pages, paper and card; not stated)
• Scanner latency and throughput with and without a GPU, including cost of model loading on each scan call (needs testing)
• Whether long inputs above 512 tokens lose detections in the truncated tail (needs testing)
• Whether the last class probability is the malicious class in the gated model config (config not readable without access; needs testing)
• Effect of the whitespace-removing preprocessing on non-English and code text (needs testing)
• Detection quality on tool outputs, memory text and assistant text, which Meta lists for configuration but only evaluates on user and tool messages (needs testing)
• Whether a model-card claim of "adversarial-attack resistant tokenization" holds through the wrapper's preprocessing (needs testing)
• Whether the docs sample output (reason '`prompt_guard`', benign score 0.0) reflects an earlier code version (checked the pinned how-to page and code; they differ)
• Whether the README's Llama 3.1 access instruction is stale for the Llama 4 licensed model
• How a hosted or air-gapped deployment obtains the gated weights without an interactive login (checked README and code; not described)
### R9
Summary: LlamaFirewall source files, README and docs pages in the PurpleLlama repo, the PyPI index, the Prompt Guard 2 model card, and the LlamaFirewall paper.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/prompt_guard_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/promptguard_utils.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall_data_types.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/config.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/cli/configure.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/pyproject.toml
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/scanners/prompt-guard-2.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/getting-started/how-to-use-llamafirewall.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/getting-started/adding-custom-use-case.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/86M/MODEL_CARD.md
• https://pypi.org/simple/llamafirewall/
• https://arxiv.org/html/2505.03574
## Column PL6: Code Shield: Output-level insecure-code detection (LLM-generated code)
### R1
Summary: **Output-level insecure-code filtering.** Code Shield is a Python library that runs regex and Semgrep rules from the Insecure Code Detector over LLM-generated code. It reports whether the code is insecure, the issues found, and a recommended block, warn or ignore treatment. **[Documented]**
Detail:
• Meta: "CodeShield is a robust inference time filtering tool engineered to prevent the introduction of insecure code generated by LLMs into production systems." (CodeShield/README.md@172c1074:7) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Engine: "CodeShield leverages a static analysis library, the Insecure Code Detector (ICD), to identify insecure code." (CodeShield/README.md@172c1074:11) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Protections page: "Code Shield provides support for inference-time filtering of insecure code produced by LLMs." (dev.meta.ai llama-protections, read 2026-10-09) **[Documented]**
• Use: CodeShield can fortify "any code-producing LLMs by either adding a warning message or completely blocking the response" (CodeShield/README.md@172c1074:17) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Entry point: class CodeShield with the async classmethod `scan_code`(code, language=None) (CodeShield/codeshield.py@172c1074:37-50) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Names: "Code Shield" on the protections page and root README, "CodeShield" in the repo and LlamaFirewall docs, and a typo "Code Sheild" in the protections page body (dev.meta.ai llama-protections, read 2026-10-09) **[Documented]**
• Wrapper versus engine: LlamaFirewall's CodeShield scanner (column PL4) calls this engine but ignores the recommended treatment and blocks on any issue (premise: code_shield_scanner.py reads the issue list only) **[Inferred]**
### R2
Summary: **Insecure coding practices, not exploitable vulnerabilities.** Rules flag risky calls and settings such as weak hashes, command injection and buffer-overflow functions, each with a CWE id. Meta says seven languages in some places and eight in others. Taint-flow analysis is out of scope. **[Documented]**
Detail:
• Purpose: "Insecure coding practices refer to any coding style or practice that requires detailed attention from the developer to ensure it is written securely." (CodeShield/insecure_code_detector/README.md@172c1074:16) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Non-goal: ICD "is not designed to serve as a comprehensive static analysis tool for identifying vulnerabilities" (CodeShield/insecure_code_detector/README.md@172c1074:16) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Limit: "doesn't work well for vulnerability categories which require taint flow analysis for high accuracy" (CodeShield/insecure_code_detector/README.md@172c1074:35) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Limit: ICD "operates on a 'best guess' basis" and can give false positives (CodeShield/insecure_code_detector/README.md@172c1074:36) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Rule examples enabled for C by Semgrep: md5-usage, sha1-usage, potential-command-injection, vulnerable-strcpy, crypto-weak-prng (CodeShield/insecure_code_detector/rules/config.yaml@172c1074:1-30) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• CWE coverage claim: "covering more than 50+ CWEs" (CodeShield/README.md@172c1074:11) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Distinct CWE ids in the rules enabled for the CODESHIELD use case come to about 47 across the eight default languages, and about 63 for the CyberSecEval rule set (premise: a count of `cwe_id` values in the regex YAML files and generated Semgrep JSON files) **[Inferred]**
• Languages, source A (7): the README says "across 7 programming languages" (CodeShield/README.md@172c1074:11) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source B (7): the protections page says "7 programming languages" (dev.meta.ai llama-protections, read 2026-10-09) **[Documented]**
• Languages, source B2: the paper says "seven programming languages" in section 4.4 and "8 programming languages" in its summary (arXiv 2505.03574) **[Documented]**
• Languages, source C (8): the ICD README says "supports 8 different programming languages" and lists C, C++, C#, Java, Javascript, Python, PHP, Rust (CodeShield/insecure_code_detector/README.md@172c1074:3,22-31) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source D (8): the LlamaFirewall docs say "eight programming languages" (LlamaFirewall/website/docs/documentation/scanners/code-shield.md@172c1074:4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source D2 (8): the LlamaFirewall README says "8 programming languages" (LlamaFirewall/README.md@172c1074:45) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source E (code): `get_supported_languages()` returns 8: C, C++, C#, Java, JavaScript, PHP, Python, Rust (languages.py@172c1074:72-83) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The Language enum has 16 members and the analyser map has 14 entries, adding Hack, Kotlin, Objective-C, Ruby, Swift and XML; no Meta text lists these as supported (languages.py@172c1074:14-30) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Using them: `scan_code` accepts any Language value, so these may work when passed explicitly (premise: codeshield.py lines 80-83 pass the language through) **[Inferred]**
• Rule files: 14 regex YAML files (c, cpp, csharp, hack, java, javascript, `language_agnostic`, `objective_c`, php, python, ruby, rust, swift, xml) and Semgrep folders for c, csharp, java, javascript, php and python (directory listing of CodeShield/`insecure_code_detector`/rules at 172c1074) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Mismatch: the analyser map lists regex only for PHP and Rust, so the PHP Semgrep rules are never run by the engine (premise: `LANGUAGE_ANALYZER_MAP` at insecure_code_detector.py lines 36-72 and the rules/semgrep/php folder) **[Inferred]**
• In the CODESHIELD use case, config.yaml lists no regex or Semgrep rules of its own for Rust, so Rust gets only the language-agnostic regex rules (premise: config.yaml rust entry with empty lists) **[Inferred]**
• Matches on comment lines are dropped (insecure_code_detector.py@172c1074:158-166,179-180) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R3
Summary: **A code string passed by the caller.** The library receives text and, if no language is given, tries all eight default languages. It has no role, prompt or conversation input. Meta presents it as a filter on model output. **[Documented]**
Detail:
• Direction: the README figure caption describes "the flow of how CodeShield should be used for output scanning from LLM before the suggestions are propagated" (CodeShield/README.md@172c1074:21) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Use cases: AI coding assistants in IDEs, where it can "block insecure code suggestions", and chatbots used for code snippets (CodeShield/README.md@172c1074:16-17) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Input: `scan_code` takes code and an optional language; with none, it runs over `get_supported_languages()` in parallel (CodeShield/codeshield.py@172c1074:70-79) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• With a language it scans only that language (CodeShield/codeshield.py@172c1074:80-83) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The library receives a string and has no prompt versus response flag, so it can scan code in any text such as tool output or retrieved code, not only model output (premise: `scan_code` signature) **[Inferred]**
• Code context is not passed: `scan_code` calls the engine with the code and use case only, so code before or after the snippet is not considered (CodeShield/codeshield.py@172c1074:42-44) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Messages with prose and fenced code are passed whole; no extraction of code blocks is done in the library (premise: `scan_code` and analyze take the text as is) **[Inferred]**
• Scope of risk: the LlamaFirewall docs add "Malicious Code via Prompt Injection" as a risk the engine helps cover with other scanners (LlamaFirewall/website/docs/documentation/scanners/code-shield.md@172c1074:18) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Evaluation data: 50 LLM-generated code completions per language from CyberSecEval 3 (arXiv 2505.03574 section 4.4) **[Documented]**
### R4
Summary: **Regex and Semgrep rule engine, installed as the codeshield package.** Rules are YAML and JSON files enabled per use case. The package depends on Semgrep. It has no model. The MIT-licensed code at the pin is version 0.0.1 while PyPI lists 1.0.1. **[Documented]**
Detail:
• Analysers: "ICD comprises of a set of analyzers which independently assess the security of the input code snippet based on static analysis rules"; regex and Semgrep (CodeShield/insecure_code_detector/README.md@172c1074:20) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Design principles: robustness for incomplete code, speed, extensibility (CodeShield/insecure_code_detector/README.md@172c1074:6-12) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Analyser map: C, C++, C#, Java, JavaScript, Kotlin and Python use regex and Semgrep; Hack, Objective-C, PHP, Ruby, Rust, Swift and XML use regex only (insecure_code_detector.py@172c1074:36-72) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Use cases: CODESHIELD and CYBERSECEVAL; `scan_code` always uses CODESHIELD, the engine's analyze defaults to CYBERSECEVAL (usecases.py@172c1074:11-13) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• In CODESHIELD mode regex runs first and returns on any match; Semgrep runs only if a quick regex pre-scan recommends it (insecure_code_detector.py@172c1074:126-137) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The pre-scan regex comes from the rule's `prescan_regex` metadata; with none, Semgrep runs (insecure_code_detector.py@172c1074:295-306) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Semgrep command: the semgrep-core binary through a symlink named osemgrep, with "--metrics off" and a job cap of 16 (oss.py@172c1074:28-76) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Rule files: regex YAML per language, Semgrep YAML folders, generated Semgrep JSON per language and use case, and config.yaml listing enabled rule ids (CodeShield/insecure_code_detector/rules/README.md@172c1074:3-8) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Rule counts from the repo: generated CODESHIELD Semgrep JSON holds 16 rules for C, 16 for C++, 20 for C#, 11 for Java, 13 for JavaScript, 7 for PHP and 10 for Python, 0 for Kotlin (counted from CodeShield/`insecure_code_detector`/rules/semgrep/_generated_ files at 172c1074) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Two-layer scan per Meta: the first layer uses "lightweight pattern matching and static analysis" and the second "a more comprehensive static analysis layer" (LlamaFirewall/website/docs/documentation/scanners/code-shield.md@172c1074:11) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Dependencies: "semgrep>1.68" and "pyyaml"; "requires-python = \">=3.8\"" (CodeShield/pyproject.toml@172c1074:10,15) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The wheel build maps codeshield.py to codeshield/cs.py and the detector folder to codeshield/`insecure_code_detector` (CodeShield/pyproject.toml@172c1074:34-36) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Install: "pip3 install codeshield", or "pip install ." from the PurpleLlama/CodeShield folder (CodeShield/notebook/CodeShieldUsageDemo.ipynb@172c1074) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Versions: the repo pyproject says version "0.0.1" (CodeShield/pyproject.toml@172c1074:3) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PyPI simple index lists codeshield 1.0.0 and 1.0.1 (PyPI simple index, observed 2026-10-09) **[Documented]**
• Equality of PyPI codeshield 1.0.1 with the repo code at the pin (checked the PyPI index and the repo; the sdist contents were not read) **[To be verified]**
• Origin: "Initially released as part of the Llama 3 launch" (LlamaFirewall/website/docs/documentation/scanners/code-shield.md@172c1074:4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Licence: MIT, "Copyright (c) Meta Platforms, Inc. and affiliates." (CodeShield/LICENSE@172c1074:1-3) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Semgrep is a third-party component installed as a dependency; its own licence is not Meta documentation and is not read here (CodeShield/pyproject.toml@172c1074:15) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Release notes (checked the repo at the pin: no tags and no CHANGELOG file) **[Not disclosed]**
### R5
Summary: **Insecure flag, issue list and a recommended treatment.** Results carry an insecure flag, the issues found and a block, warn or ignore treatment. Meta reports 96% precision and 79% recall on a manual check, but its four latency statements disagree. **[Documented]**
Detail:
• Result type: `CodeShieldScanResult` with `is_insecure` (bool), `issues_found` (list of Issue or none) and `recommended_treatment` (CodeShield/codeshield.py@172c1074:30-35) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Treatment values: block, warn, ignore (CodeShield/codeshield.py@172c1074:24-27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Rule: `BLOCK` if any issue has severity ERROR, otherwise `WARN`; no issues gives `IGNORE` (CodeShield/codeshield.py@172c1074:64-68,87-93) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Issue fields: description, `cwe_id`, severity, rule, line, path, char, name, original, replacement, analyzer, `pattern_id` (issues.py@172c1074:43-55) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Severity levels: error, warning, advice, disabled (issues.py@172c1074:18-22) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• There is no confidence score in the result (premise: the `CodeShieldScanResult` and Issue definitions have none) **[Inferred]**
• Semgrep issues carry the raw severity string from Semgrep output, while the treatment check compares against the Severity enum, so Semgrep findings may never produce `BLOCK` (premise: insecure_code_detector.py line 282 and codeshield.py line 90) **[Inferred]**
• Under the CODESHIELD rules, the only enabled regex rule with severity Error is the C rule bugprone-gets (premise: count over regex YAML and config.yaml) **[Inferred]**
• Errors are swallowed: on an exception `scan_code` logs it and returns not insecure with treatment `IGNORE` (CodeShield/codeshield.py@172c1074:84-86) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The usage notebook compares `recommended_treatment` to the strings "block" and "warn" (CodeShield/notebook/CodeShieldUsageDemo.ipynb@172c1074) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Precision and recall: "CodeShield achieved a precision of 96% and a recall of 79% in identifying insecure code", on 50 manually labelled completions per language from CyberSecEval 3 (arXiv 2505.03574 section 4.4) **[Documented]**
• Latency, statement 1 (Code Shield README): "approximately 99% of cases, requests are processed within a swift 70ms window"; "the p90 latency is 450ms" for the rest (CodeShield/README.md@172c1074:27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Latency, statement 2 (LlamaFirewall docs): first tier "under 100 milliseconds", second layer "around 300 milliseconds", about 90% resolved by the first layer (code-shield.md@172c1074:11-13) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Latency, statement 3 (paper): first tier "approximately 60 milliseconds", second layer around 300 ms, "approximately 90% of inputs are fully resolved by the first layer" (arXiv 2505.03574 section 4.4) **[Documented]**
• Latency, statement 4 (protections page): "an average latency of 200ms" (dev.meta.ai llama-protections, read 2026-10-09) **[Documented]**
• The four statements differ and are from Meta's internal production studies; no timeout or latency appears in the engine code (premise: grep of CodeShield python files) **[Inferred]**
• Hardware, input size and language mix behind any latency figure (checked the README, docs, paper and protections page; not given) **[Not disclosed]**
### R6
Summary: **A code string and an optional language.** The caller awaits an async function. The package needs Semgrep and writes each scan to a temporary file. **[Documented]**
Detail:
• Call: "await CodeShield.`scan_code`(code)" in an async function; the demo uses asyncio.run (CodeShield/example.py@172c1074:19-33) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Parameters: code (str), language (Language or none) (CodeShield/codeshield.py@172c1074:48-50) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Python 3.8 or later for the package; Semgrep above version 1.68 and pyyaml are installed with it (CodeShield/pyproject.toml@172c1074:10,15) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Importing the engine needs the Semgrep core binary: it raises "Failed to find semgrep-core in PATH or in the semgrep package." if missing (oss.py@172c1074:42-44) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Each engine call writes the text to a temporary file with the language's file extension and deletes it after the run (insecure_code_detector.py@172c1074:98-107,149-153) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• On the fast-mode early returns the temporary file may be left behind (premise: the returns at insecure_code_detector.py lines 129 and 137 come before the os.remove at line 151) **[Inferred]**
• Semgrep runs as a subprocess with up to 16 jobs; its output is parsed as JSON (oss.py@172c1074:61-76; insecure_code_detector.py lines 261-292) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Rules are configurable: add or edit entries in the YAML file for the language, and enable them in config.yaml (CodeShield/insecure_code_detector/rules/README.md@172c1074:3-8) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The notebook example 3 installs the llama-recipes package and an external LLM token to generate code; scanning itself needs none (CodeShield/notebook/CodeShieldUsageDemo.ipynb@172c1074) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Maximum input size, timeout and concurrency limits for `scan_code` (checked the READMEs, docs pages and code; none set) **[Not disclosed]**
• Operating system: the code symlinks the Semgrep binary, which may fail on systems without symlink rights (premise: oss.py lines 48-54 call os.symlink) **[Inferred]**
### R7
Summary: **Minimum setup:** pip install codeshield, which pulls in Semgrep, then scan labelled snippets with the CodeShield scan function in each default language and compare the insecure flag with the label. No key, model or gated access is needed. Read the recommended treatment and issue list for each case. **[Inferred]**
Detail:
• **Minimum setup:** pip install codeshield (Python 3.8 or later), run `scan_code` under asyncio on each snippet, and record `is_insecure`, `recommended_treatment` and the issues (premise: example.py and the pyproject) **[Inferred]**
• Table 3 input type: model-output code with insecure or clean labels and an expected rule or CWE, one set per default language (premise: the Issue fields) **[Inferred]**
• Include cases for every analyser path: regex-only languages (PHP, Rust), regex plus Semgrep languages, and snippets that trigger only Semgrep (premise: the analyser map) **[Inferred]**
• Pass the language explicitly in one run and leave it out in another to compare results and runtime (premise: `scan_code` branches) **[Inferred]**
• Add comment-only matches, markdown-fenced code and prose-only text to test the comment filter and whole-message scanning (premise: engine code) **[Inferred]**
• Build the labelled set from public code-completion or insecure-code datasets, noting that CyberSecEval is the benchmark Meta cites for its precision and recall (premise: the paper's evaluation text) **[Inferred]**
### R8
Summary: **Key open questions.** The language count (seven or eight), four conflicting latency figures, whether PyPI matches the repo, Rust and PHP rule coverage, and whether Semgrep findings can ever recommend blocking.
Detail:
• Which seven languages the "7" statements mean, and why the same documents also say eight (checked both READMEs, the docs page, the paper and the code; the code scans eight)
• Actual latency by language, with regex-only and Semgrep paths (needs testing)
• Precision and recall per language on the bench's own set; Meta's figure rests on 50 manual completions per language (needs testing)
• Whether PyPI codeshield 1.0.1 equals the repo code at the pin
• Whether Rust is meant to be in the default scan list when the CODESHIELD use case enables no Rust rules of its own (checked config.yaml; needs testing)
• Whether PHP Semgrep rules are meant to run, since the analyser map lists regex only (needs testing)
• Whether a Semgrep finding can yield a `BLOCK` recommendation, given the string-versus-enum severity comparison (needs testing)
• Whether temporary files are left behind on fast-mode early returns (needs testing)
• Whether the usage notebook's string comparison of `recommended_treatment` works with the Treatment enum (needs testing)
• Whether the "over 50" CWE claim holds for the CODESHIELD rules (checked config.yaml and the rule files; my count is about 47, needs a rule-by-rule check)
• Semgrep's own licence and terms (third-party; a separate inventory row)
### R9
Summary: Code Shield README, source and rule files in the PurpleLlama repo, Meta docs and protections pages, the PyPI index, and the LlamaFirewall paper.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/codeshield.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/example.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/pyproject.toml
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/notebook/CodeShieldUsageDemo.ipynb
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/insecure_code_detector.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/languages.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/usecases.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/issues.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/oss.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/rules/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/rules/config.yaml
• https://github.com/meta-llama/PurpleLlama/tree/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/rules
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/scanners/code-shield.md
• https://pypi.org/simple/codeshield/
• https://dev.meta.ai/llama/llama-protections
• https://arxiv.org/html/2505.03574
## Column PL4: LlamaFirewall: Output-level insecure-code detection (CodeShield scanner)
### R1
Summary: **Output-level insecure-code scanning in LlamaFirewall.** The CodeShield scanner runs the Code Shield static-analysis engine over a message's text and blocks it, with score 1.0, when any insecure-code issue is found. By default it runs on assistant and tool messages. **[Documented]**
Detail:
• Meta describes CodeShield in LlamaFirewall as "a static analysis engine that examines LLM-generated code for security issues in real time" (LlamaFirewall/README.md@172c1074:45) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Docs page: "CodeShield is an advanced online static-analysis engine designed to enhance the security of LLM-generated code." (LlamaFirewall/website/docs/documentation/scanners/code-shield.md@172c1074:4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Code: class `CodeShieldScanner`, scanner name "Code Shield Scanner", constructed with a threshold of 1.0 (code_shield_scanner.py@172c1074:32-38) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Decision: any issue returns `BLOCK` with score 1.0; no issue returns `ALLOW` with score 0.0 (code_shield_scanner.py@172c1074:67-92) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Wrapper versus engine: the scanner adds the role configuration, a block-or-allow decision and a formatted reason; the rules, languages and analysers are the Code Shield engine in column PL6 (premise: the scanner calls `insecure_code_detector`.analyze) **[Inferred]**
• Selected by scanner type `CODE_SHIELD` (llamafirewall_data_types.py@172c1074:14) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Previously released "as part of the Llama 3 launch, CodeShield is now integrated into the LlamaFirewall framework" (code-shield.md@172c1074:4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R2
Summary: **Insecure coding patterns in LLM-generated code.** The engine flags risky code practices with CWE identifiers across eight languages by default, though Meta also says seven and claims over 50 CWEs. It is not a taint-flow analyser. **[Documented]**
Detail:
• Risks: "Insecure Coding Practices" and "Malicious Code via Prompt Injection" as part of layered defence (code-shield.md@172c1074:17-18) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Coverage: "offering coverage for over 50 Common Weakness Enumerations (CWEs)" (code-shield.md@172c1074:4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source A (8): the LlamaFirewall README says "8 programming languages" (LlamaFirewall/README.md@172c1074:45) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source A2 (8): the LlamaFirewall docs say "eight programming languages" (code-shield.md@172c1074:4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source B (code): the scanner scans the list from `get_supported_languages()`, which returns eight: C, C++, C#, Java, JavaScript, PHP, Python, Rust (languages.py@172c1074:72-83) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source C (7): the Code Shield README says "across 7 programming languages, covering more than 50+ CWEs" (CodeShield/README.md@172c1074:11) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages, source D (7): the protections page says "7 programming languages" (dev.meta.ai llama-protections, read 2026-10-09) **[Documented]**
• The paper states both: "8 programming languages" in its summary and "seven programming languages" in section 4.4 (arXiv 2505.03574 sections 1 and 4.4) **[Documented]**
• Enum members beyond the eight: the Language enum has 16 members including Hack, Kotlin, Objective-C, Objective-C++, Ruby, Swift, XML and `LANGUAGE_AGNOSTIC`, none of them in the default scan (languages.py@172c1074:14-30) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The engine's README names the eight languages: C, C++, C#, Java, Javascript, Python, PHP, Rust (CodeShield/insecure_code_detector/README.md@172c1074:22-31) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Not a vulnerability finder: ICD "is not designed to serve as a comprehensive static analysis tool for identifying vulnerabilities" (CodeShield/insecure_code_detector/README.md@172c1074:16) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Limit: "doesn't work well for vulnerability categories which require taint flow analysis for high accuracy" (CodeShield/insecure_code_detector/README.md@172c1074:35) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Limit: ICD "operates on a 'best guess' basis" and "can lead to false positives" (CodeShield/insecure_code_detector/README.md@172c1074:36) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Paper limit: CodeShield "is not comprehensive and may miss nuanced or context-dependent vulnerabilities" (arXiv 2505.03574 section 4.4) **[Documented]**
• Rules enabled for the CODESHIELD use case: config.yaml lists 38 regex rule ids (8 of them language-agnostic) and 77 Semgrep rule ids for the eight default languages; Rust lists none of its own (CodeShield/insecure_code_detector/rules/config.yaml@172c1074:1-407) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Distinct CWE ids in the rules enabled for this scanner use case come to about 47 across the eight languages by a count of the rule files, below the "over 50" claim; the larger CyberSecEval rule set gives about 63 (premise: a count of `cwe_id` values in the regex YAML files and generated Semgrep JSON files) **[Inferred]**
### R3
Summary: **Assistant and tool text, as plain strings.** The scanner reads only the message content and scans it as code in all default languages. It is attached to the ASSISTANT and TOOL roles by default and by the coding-assistant use case. Tool-call arguments are not read. **[Documented]**
Detail:
• Reads one field: "text = message.content" (code_shield_scanner.py@172c1074:56) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Runs the engine over every language from `get_supported_languages()` in parallel with asyncio.gather (code_shield_scanner.py@172c1074:57-59) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• No-config default: `ASSISTANT` scans `CODE_SHIELD` and `TOOL` scans `CODE_SHIELD` and `PROMPT_GUARD` (llamafirewall.py@172c1074:90-96) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• `CODING_ASSISTANT` use case: `CODE_SHIELD` for `ASSISTANT` and `TOOL` (config.py@172c1074:26-29) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Docs: "setting a `ScannerType`.`CODE_SHIELD` for both the `ASSISTANT` and `TOOL` roles" (adding-custom-use-case.md@172c1074:26-27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Direction (R002): the same scanner can be attached to any role, so it can also scan `USER` or `MEMORY` text; Meta documents it for LLM output (premise: Configuration maps any Role to scanner types) **[Inferred]**
• Docs example: a coding agent's code diff is statically analysed and "CodeShield statically analyzes the code diff" and, if SQL injection risk is detected, "the patch is rejected" (workflow-and-detection-components.md@172c1074:68) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Messages are scanned whole, including prose around code; the engine does not extract fenced code blocks (premise: the scanner passes the entire text to `insecure_code_detector`.analyze) **[Inferred]**
• Code context is not supplied: the scanner passes `code_before`, `code_after` and path as None (code_shield_scanner.py@172c1074:43-50) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The message type has an optional `tool_calls` field that this scanner does not read, so code inside function-call arguments is not scanned (premise: only message.content is read) **[Inferred]**
• Trace and previous messages are ignored by this scanner (code_shield_scanner.py@172c1074:53-56) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
### R4
Summary: **Regex and Semgrep rules run through the installed codeshield package.** The scanner imports the Insecure Code Detector from the codeshield package and falls back to the repo copy. It needs the Semgrep dependency but no model, key or network access. **[Documented]**
Detail:
• Import order: first "codeshield.`insecure_code_detector`" (the PyPI package), else "CodeShield.`insecure_code_detector`" from the repo (code_shield_scanner.py@172c1074:9-19) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• So an installed codeshield package, not the repo folder, normally supplies the rules and the language list (premise: try/except ImportError order) **[Inferred]**
• Docs: CodeShield "supports both Semgrep and regex-based rules, providing syntax-aware pattern matching" (code-shield.md@172c1074:21) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• llamafirewall 1.0.3 in the repo requires "codeshield>=1.0.1" (LlamaFirewall/pyproject.toml@172c1074:7,15) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PyPI simple index lists codeshield up to 1.0.1 and llamafirewall up to 1.0.3 (PyPI simple index, observed 2026-10-09) **[Documented]**
• The repo CodeShield folder declares version "0.0.1", so whether PyPI codeshield 1.0.1 equals the code at the pin is unconfirmed (CodeShield/pyproject.toml@172c1074:3) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Equality of PyPI codeshield 1.0.1 with the repo code at the pin (checked the PyPI index and the repo; the sdist contents were not read) **[To be verified]**
• Use case: the scanner calls the engine with UseCase.CODESHIELD, the fast mode (code_shield_scanner.py@172c1074:49) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• In that mode regex runs first and returns on any match, and Semgrep runs only if a quick regex pre-scan recommends it (insecure_code_detector.py@172c1074:126-137) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Two-tier design per Meta: "The first tier utilizes lightweight pattern matching and static analysis, completing scans in under 100 milliseconds" (code-shield.md@172c1074:11) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Semgrep is invoked as a subprocess of a symlinked "osemgrep" binary found in the semgrep package (oss.py@172c1074:28-76) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The llamafirewall package requires torch, transformers, `huggingface_hub`, openai and others (LlamaFirewall/pyproject.toml@172c1074:14-23) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Licence: LlamaFirewall is MIT licensed (LlamaFirewall/LICENSE@172c1074:1) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Licence: the CodeShield folder is MIT licensed (CodeShield/LICENSE@172c1074:1) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Release notes for codeshield and llamafirewall (checked the repo at the pin: no tags and no CHANGELOG file) **[Not disclosed]**
• No backing model: the scanner and engine files import no machine-learning library and run regex and Semgrep rules (premise: code_shield_scanner.py and insecure_code_detector.py imports) **[Inferred]**
### R5
Summary: **Block with score 1.0, or allow with 0.0.** The reason lists each issue with its description, CWE, line and severity. The scanner never returns warn or human review. Meta quotes four different latency figures, and precision 96% with recall 79% from a manual check. **[Documented]**
Detail:
• Result: `ScanResult` with decision, reason, score and status; this scanner returns only `ALLOW` or `BLOCK`, always with status SUCCESS (code_shield_scanner.py@172c1074:67-92) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Allow reason "No unsafe function call detected" with score 0.0 (code_shield_scanner.py@172c1074:33,67-73) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Block reason: "{n} unsafe function call detected:" followed by one line per issue with description, "(CWE-id)", "at line n" and "[Severity: s]" (code_shield_scanner.py@172c1074:75-91) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The block threshold of 1.0 is passed to the base class but the scan code never compares against it (premise: code_shield_scanner.py contains no use of `block_threshold`) **[Inferred]**
• The engine's own block, warn or ignore treatment is not used, so low-severity findings also block (premise: the scanner reads the issue list only) **[Inferred]**
• Several scanners on a role: `BLOCK` wins if any scanner blocks (llamafirewall.py@172c1074:142-167) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Precision and recall: "CodeShield achieved a precision of 96% and a recall of 79%" on "50 LLM-generated code completions per language across several languages", labelled manually in CyberSecEval 3 (arXiv 2505.03574 section 4.4) **[Documented]**
• Per-language precision and recall: the paper shows a figure; the values were not read as text (arXiv 2505.03574 section 4.4) **[To be verified]**
• Latency, statement 1 (Code Shield README): "approximately 99% of cases, requests are processed within a swift 70ms window", p90 450 ms for the rest (CodeShield/README.md@172c1074:27) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Latency, statement 2 (LlamaFirewall docs): first tier "under 100 milliseconds", second layer "around 300 milliseconds", about 90% resolved by the first layer under 70 ms (code-shield.md@172c1074:11-13) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Latency, statement 3 (paper): first tier "approximately 60 milliseconds", second layer around 300 ms, "approximately 90% of inputs are fully resolved by the first layer" (arXiv 2505.03574 section 4.4) **[Documented]**
• Latency, statement 4 (protections page): "an average latency of 200ms" (dev.meta.ai llama-protections, read 2026-10-09) **[Documented]**
• The four statements differ and each comes from Meta's internal production experience; no latency or timeout appears in the scanner or engine code (premise: grep of CodeShield and LlamaFirewall/src for latency and timeout) **[Inferred]**
• Scanner latency measured through LlamaFirewall (checked the README, docs and paper; none gives one) **[Not disclosed]**
### R6
Summary: **A string of code, with the codeshield package and Semgrep installed.** The scanner needs no key or model. It scans eight languages by default and writes each scan to a temporary file. No size limit or timeout is set in code. **[Documented]**
Detail:
• Input: Message content text; all eight default languages are tried on every message (code_shield_scanner.py@172c1074:56-59) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Python 3.10 or later for LlamaFirewall (LlamaFirewall/README.md@172c1074:53) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The codeshield package declares "requires-python = \">=3.8\"" (CodeShield/pyproject.toml@172c1074:10) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• codeshield dependencies: "semgrep>1.68" and "pyyaml" (CodeShield/pyproject.toml@172c1074:15) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Importing the engine needs the Semgrep core binary: it raises "Failed to find semgrep-core in PATH or in the semgrep package" if missing (oss.py@172c1074:42-44) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Each engine call writes the text to a temporary file with the language's file extension and deletes it afterwards (insecure_code_detector.py@172c1074:98-107,149-153) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• On the early-return paths in fast mode the temporary file may not be deleted (premise: the returns at insecure_code_detector.py lines 129 and 137 come before the os.remove at line 151) **[Inferred]**
• Semgrep jobs are capped at 16 workers (oss.py@172c1074:61-62) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Rules can be edited: regex rules live in rules/regex YAML files and Semgrep rules in rules/semgrep, enabled per use case in config.yaml (CodeShield/insecure_code_detector/rules/README.md@172c1074:3-8) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Comment filtering: a regex match on a line that starts with "#", "//" or "/*", or ends with "*/", is dropped (insecure_code_detector.py@172c1074:158-166,179-180) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Maximum input size, timeout and concurrency limits (checked the READMEs, docs pages and code; none is set) **[Not disclosed]**
• No API key, Hugging Face login or network call is used by this scanner (premise: code_shield_scanner.py imports only the engine) **[Inferred]**
### R7
Summary: **Minimum setup:** pip install llamafirewall, which pulls in codeshield and Semgrep, attach the Code Shield scanner type to the assistant role, and scan labelled snippets in the eight default languages. No key, model or gated access is needed. Check the language list and fast-mode behaviour on the installed codeshield version. **[Inferred]**
Detail:
• **Minimum setup:** pip install llamafirewall (Python 3.10 or later), configure LlamaFirewall with Role.`ASSISTANT` mapped to `ScannerType`.`CODE_SHIELD`, then call scan on `AssistantMessage` objects holding code snippets (premise: README and the demo script) **[Inferred]**
• Table 3 input type: model-output text containing code, labelled insecure or clean, with the CWE or rule it should trigger (premise: block reason carries CWE ids) **[Inferred]**
• Cover every default language with a case from each rule family; include Rust and PHP cases, whose rule coverage differs from the others (premise: the engine's analyser map, see column PL6) **[Inferred]**
• Include non-code prose, fenced code inside markdown, code inside a tool message and an insecure pattern only in a comment, to check the comment filter (premise: engine code) **[Inferred]**
• Record the installed codeshield version and compare with the repo code because the scanner imports the installed package first (premise: import order) **[Inferred]**
• Expect the first scans to be slower where Semgrep runs; time regex-only and Semgrep paths separately (premise: two-tier design) **[Inferred]**
### R8
Summary: **Key open questions.** The language count (seven or eight), four conflicting latency figures, whether the installed package matches the repo, and how rules behave for Rust and PHP.
Detail:
• Which seven languages the "7" statements mean, and why the same documents also say eight (checked the READMEs, docs page, paper and code; the code scans eight)
• Latency through LlamaFirewall on the bench, including the cold start of Semgrep (needs testing)
• Precision and recall per language on the bench's own labelled set, since Meta's figure rests on 50 manual completions per language (needs testing)
• Whether PyPI codeshield 1.0.1 equals the repo code at the pin
• Rust is in the default scan list but the CODESHIELD use case enables no Rust rules of its own, and PHP rules are regex only because the analyser map lists no Semgrep for PHP; whether this is intended (checked config.yaml and the analyser map; needs testing)
• Whether the "over 50" CWE claim holds for the rules enabled in this scanner's use case (my count is about 47; needs a rule-by-rule check)
• Whether temporary files are left behind on early-return paths (needs testing)
• Whether blocking every finding, including low-severity ones, is the intended policy compared with the engine's own warn treatment
• Whether code placed in message fields other than content, such as tool-call arguments, should be scanned
### R9
Summary: LlamaFirewall and Code Shield source files, README and docs pages in the PurpleLlama repo, the PyPI index, the Meta protections page, and the LlamaFirewall paper.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/code_shield_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall_data_types.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/config.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/pyproject.toml
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/scanners/code-shield.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/getting-started/adding-custom-use-case.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/pyproject.toml
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/insecure_code_detector.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/languages.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/oss.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/rules/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/insecure_code_detector/rules/config.yaml
• https://pypi.org/simple/codeshield/
• https://pypi.org/simple/llamafirewall/
• https://dev.meta.ai/llama/llama-protections
• https://arxiv.org/html/2505.03574
## Reviewer notes
Method: code read at the pinned clone (172c1074069eb88ec834124272c1b1c4f8893445, HEAD verified equal), not run. Live pages read with fetch_text.py (verbatim): dev.meta.ai Prompt Guard page, llama.com/llama-protections (redirects to dev.meta.ai, HTTP 200), HF gate pages for 86M and 22M (HTTP 200), HF API metadata for both repos, arXiv 2505.03574 html, PyPI simple index for llamafirewall and codeshield. WebFetch was not used. Quotes have straight quotation marks where the source uses curly ones.
1. Paper versus card (PL1 R5): the paper's table prints the 86M English AUC as ".98"; the card prints ".998". Both written as bullets; the other cells match.
2. Parameter counts (PL1 R4): HF safetensors totals 278,810,882 (86M) and 70,830,722 (22M) versus the card's "86M" and "22M" backbone parameters. The embedding-table explanation is [Inferred].
3. Language count (PL4 R2, PL6 R2): conflict C1 written as separate bullets (7: CodeShield README, protections page, paper section 4.4; 8: ICD README, LlamaFirewall README and docs, paper summary, code). The 16-member enum and 14-entry analyser map are reported as not documented as supported.
4. Latency (PL4 R5, PL6 R5): four statements (C2) kept as four bullets, none chosen.
5. Scanner name (PL2 R3): docs use PROMPT_INJECTION (adding-custom-use-case.md) but the enum has PROMPT_GUARD only (C3); two bullets.
6. Docs sample output (PL2 R5): how-to page prints reason 'prompt_guard' and benign reason 'default' with score 0.0; the single-scanner code path returns the scanner's own reason and score. New finding, not in the brief.
7. Code observations labelled [Inferred] and needing the bench to confirm (code read, not run): (a) PL2 builds a new scanner, and so reloads the model, on each scan call (llamafirewall.py:118); (b) PL6 Semgrep issues carry a raw severity string, so scan_code's BLOCK check (Severity.ERROR) may never fire for Semgrep findings (insecure_code_detector.py:282; codeshield.py:90); (c) temporary files are not removed on the fast-mode early returns (insecure_code_detector.py:129,137 before 151); (d) PHP Semgrep rules unreachable because the analyser map lists PHP as regex only; (e) Rust has no CODESHIELD rules of its own in config.yaml; (f) LlamaFirewall imports codeshield from the installed package first (code_shield_scanner.py:9-19), so PyPI codeshield 1.0.1 rather than the repo folder normally supplies the rules.
8. CWE counts (PL4 R2, PL6 R2): 47 (CODESHIELD rules, eight default languages), 63 (CyberSecEval rules, eight languages), 65 (all enum languages) are my counts of distinct CWE-nnn strings in cwe_id fields of regex YAML and generated Semgrep JSON (script in scratchpad/drafter/purplellama_cols_a/cwe_count.py). They are derived data; labelled [Inferred]. Rule counts (38 regex ids, 77 Semgrep ids in config.yaml; generated JSON rule counts) are plain counts of the files and labelled [Documented: repo].
9. Not read: Hugging Face card bodies (gated, HTTP 401), so card facts come from the repo MODEL_CARD.md files; equality with the HF body is [To be verified] (R8). The llama-cookbook inference.py and prompt_guard_tutorial were not read. PyPI sdists were not read. The per-language precision and recall figure in the paper is an image. The Code Shield notebook output cells were not examined.
10. Docs-site pages are cited through their pinned .md files only (five pages matched in P0). No live docs-site page was relied on for a quote in these four columns.
11. Header prefixes follow option B (per-tool). The checker may warn that several prefixes appear in one file; that is expected.
12. AUP (PL1 R8): the whole Llama 4 USE_POLICY.md was grepped for test, security, circumvent; only item 2.8 (line 37) is close. This is a licensing question for CP1/CP2, not a conclusion.
13. Cross-reference to Llama Guard (columns V to Z) appears in one Detail sentence each in PL1 R2 and R3 only, not in any Summary.
