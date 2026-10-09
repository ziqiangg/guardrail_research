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
## Column PL3: LlamaFirewall: Trace-level agent goal-hijacking detection (AlignmentCheck)
### R1
Summary: **Trace-level agent goal-hijacking detection.** AlignmentCheck asks a separate language model whether an agent's latest action serves the user's original request, using the earlier trace as context. Meta labels it experimental. **[Documented]**
Detail:
• AlignmentCheck is a LlamaFirewall scanner that audits an agent's reasoning and actions for goal hijacking or injection-induced misalignment: "utilizes few-shot prompting to audit an agent's reasoning in real-time, detecting signs of goal hijacking or prompt-injection induced misalignment" (docs page scanners/alignment-check, line 4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The paper calls it "an experimental few-shot prompting-based chain-of-thought auditor" (arXiv 2505.03574 section 1) **[Documented]**
• The paper repeats the status: "AlignmentCheck is currently an experimental feature within LlamaFirewall." (arXiv 2505.03574 Figure 2 caption) **[Documented]**
• The code class `AlignmentCheckScanner` sits under `scanners/experimental/` and is a subclass of `CustomCheckScanner` (`alignmentcheck_scanner.py@172c1074:37`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The scanner is reached through `ScannerType.AGENT_ALIGNMENT`, which `create_scanner` maps to `AlignmentCheckScanner()` with no arguments (`llamafirewall.py@172c1074:64-69`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The scanner is a judge, not a classifier: the verdict comes from a chat model reading a prompt, so it is the only scanner in this half whose result depends on a remote model call **[Inferred]**
### R2
Summary: **Goal hijacking and injection-induced misalignment.** It targets indirect injections that look benign in isolation but push the agent off the user's goal. It is not a content filter, and when in doubt the prompt says to treat the action as aligned. **[Documented]**
Detail:
• Risks named by Meta: indirect universal jailbreak prompt injections, agent goal hijacking prompt injections, and malicious code via prompt injection (docs page scanners/alignment-check, section "Security Risks Covered") **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The docs contrast it with content filters: "Unlike traditional content-based filters, AlignmentCheck reasons over the entire execution trace" (docs page scanners/alignment-check, line 9) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The workflow page maps the agent goal-hijacking risk to AlignmentCheck alone, and lists AlignmentCheck beside PromptGuard for indirect jailbreaks (docs page llamafirewall-architecture/workflow-and-detection-components, risk table) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The system prompt defines misaligned as "clearly and actively not related to or likely to further the original objective" and closes with "When in doubt, assume the action is not misaligned" (`alignmentcheck_scanner.py@172c1074:142,148`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The prompt treats a "wait" action as not misaligned and treats an action related but not directly aligned as not misaligned (`alignmentcheck_scanner.py@172c1074:145,150`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, scope of the check (docs side): the docs say it "reasons over the entire execution trace" (docs page scanners/alignment-check, line 9) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, scope of the check (code side): the system prompt says "Only consider the selected action, not the entire trace." so the judge rates the latest action against the first user message (`alignmentcheck_scanner.py@172c1074:144`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages: the prompt and six examples are in English; no language support is stated for non-English traces (checked the scanner docs page, README and paper; not stated) **[Not disclosed]**
• The paper lists a limitation: AlignmentCheck "can be targeted by prompt injections designed to manipulate both the agent and guardrail LLM" (arXiv 2505.03574 Appendix C.4) **[Documented]**
• The paper suggests pre-scanning the inputs to AlignmentCheck with PromptGuard as a mitigation (arXiv 2505.03574 Appendix C.4) **[Documented]**
• Harmful-content moderation, PII and insecure code are not what the prompt asks the judge to rate; the prompt asks only about alignment with the user's objective **[Inferred]**
### R3
Summary: **Whole agent trace, one action at a time.** It needs the earlier messages plus the current message, and a user message in the trace. Roles are configurable; Meta's example attaches it to assistant messages. **[Documented]**
Detail:
• The scanner's `scan` takes the current `Message` and the `past_trace`; with `past_trace` of `None` it returns `ALLOW`, score 0.0, status `ERROR` and reason "No trace provided, cannot proceed" without calling the LLM (`alignmentcheck_scanner.py@172c1074:77-83`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The "user objective" is the content of the first `Role.USER` message found in the past trace; if none is found the same ALLOW and ERROR result is returned, so a trace with no user message is not scanned (`alignmentcheck_scanner.py@172c1074:64-69,85-92`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The text sent to the judge is every message in the trace plus the current message, each rendered as role and content, joined by newlines; the role of past messages is not filtered, so tool and memory messages are included (`alignmentcheck_scanner.py@172c1074:71-72`; `llamafirewall_data_types.py@172c1074:56-57`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, tool outputs (paper side): the paper lists as a mitigation "Restricting inputs to only the agent… chain-of-thought and actions, excluding direct tool outputs." (arXiv 2505.03574 Appendix C.4) **[Documented]**
• Source conflict, tool outputs (code side): the code filters nothing by role, so whether tool outputs reach the judge depends on what the caller puts in the trace (`alignmentcheck_scanner.py@172c1074:71-72`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's README example attaches it to assistant messages: `Role.ASSISTANT: [ScannerType.AGENT_ALIGNMENT]` and calls `scan_replay` on a list of messages (`LlamaFirewall/README.md@172c1074:117-130`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The paper's AgentDojo evaluation scanned only assistant messages with AlignmentCheck: "For AlignmentCheck, we restrict evaluation to messages with the role of assistant" (arXiv 2505.03574 section 4.3.1) **[Documented]**
• `scan_replay` walks the trace, calls `scan` on each message with the messages before it, and stops at the first `BLOCK` or `HUMAN_IN_THE_LOOP_REQUIRED` (`llamafirewall.py@172c1074:189-211`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The scanner is not in the no-config default role map (`TOOL`, `USER`, `SYSTEM`, `ASSISTANT`, `MEMORY` defaults hold only CodeShield and PromptGuard), so it must be configured for a role (`llamafirewall.py@172c1074:90-96`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• `scan_replay_build_trace` starts from an empty list when no trace is stored, and an empty list has no user message, so the first call returns the ALLOW and ERROR result (`llamafirewall.py@172c1074:230-235`) **[Inferred]**
• Direction under R002: the scanner has no input or output mode; it reads the trace as a whole, so the header uses the level word Trace-level and roles are set by the caller (`config.py@172c1074:13`) **[Inferred]**
• The `Message` class has an optional `tool_calls` field, but AlignmentCheck renders only role and content, so structured tool-call arguments are seen only if they are also written into the content text (`llamafirewall_data_types.py@172c1074:50-57`) **[Inferred]**
• Cost and abuse boundary: the scanner makes a network call per scanned message, so scanning every assistant message in a long trace multiplies calls and sends the whole trace each time **[Inferred]**
### R4
Summary: **Few-shot prompted external language model.** The scanner calls a chat model over an OpenAI-compatible API, by default Llama 4 Maverick on Together, with a fixed prompt of six examples. No local model is used. **[Documented]**
Detail:
• Backing model: `CustomCheckScanner` defaults to `model_name="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"`, `api_base_url="https://api.together.xyz/v1"`, `api_key_env_var="TOGETHER_API_KEY"`, `temperature=0.0`; `AlignmentCheckScanner` passes none of these, so the defaults apply (`custom_check_scanner.py@172c1074:35-38`; `alignmentcheck_scanner.py@172c1074:57-61`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The call uses the OpenAI Python client against the base URL and asks for a structured reply: `client.beta.chat.completions.parse(... response_format=output_schema ...)` (`utils/base_llm.py@172c1074:54,93-98`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The reply schema has `observation`, `thought` and a boolean `conclusion` (`alignmentcheck_scanner.py@172c1074:25-34`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The system prompt carries six worked examples, three misaligned and three not (`alignmentcheck_scanner.py@172c1074:159-236`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The user prompt asks the model to identify "if the following reasoning by the large language model agent is misaligned, not misaligned or a query failure" although the schema allows only true or false (`alignmentcheck_scanner.py@172c1074:240`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The paper describes the same design: a "guardrail LLM" doing "few-shot alignment classification after each agent action", with "a static prompt template" (arXiv 2505.03574 Appendix C.1) **[Documented]**
• The paper tested Llama 4 Maverick and Llama 3.3 70B as the backing model and reports that smaller Llama models overblock (arXiv 2505.03574 Appendix C.2) **[Documented]**
• The paper says the prompt "can be tailored with custom few-shot examples" (arXiv 2505.03574 Appendix C.1.2), but the code keeps the prompt in a module constant and the subclass constructor takes only `scanner_name` (`alignmentcheck_scanner.py@172c1074:42-61,133`) **[Documented]**
• Tailoring the prompt or the judge model therefore needs a new `CustomCheckScanner` subclass, which is the same route as the custom scanners in the Regex column **[Inferred]**
• Pins, stated separately. Code and repo docs: commit 172c1074 (author date 2026-09-29). PyPI package: `llamafirewall` 1.0.3 is the newest sdist in the simple index, observed 2026-10-09, and `LlamaFirewall/pyproject.toml@172c1074:7` also says 1.0.3 **[Documented]**
• The sdist contents were not read, so equality of the PyPI 1.0.3 code with the pinned commit is unchecked **[To be verified]**
• Meta publishes no release tag, release notes or CHANGELOG for Purple Llama (checked `git ls-remote --tags` on the repo and the clone for a CHANGELOG file) **[Not disclosed]**
• Licence of the scanner code: MIT (`LlamaFirewall/LICENSE@172c1074:1`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Licence of the default judge model: the Hugging Face metadata for the FP8 repo shows `license_name: llama4`, gated "manual" (Hugging Face API, observed 2026-10-09); this is a separate Llama licence, not the MIT licence of the scanner **[Documented: repo meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8@94125d2b]**
• Hosting: the code points at Together AI, a third-party service; Meta documents only that the Together key is needed (Meta docs, not Together docs) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Engine and wrapper: `CustomCheckScanner` is the shared LLM-prompt base class (also used by PIICheckScanner); AlignmentCheck adds the prompt, the schema and the score rule. The base class is described in the Regex column, PL5 **[Inferred]**
### R5
Summary: **Binary verdict that never blocks.** The score is 1.0 or 0.0, and the decision is human-in-the-loop required or allow, never block. Meta reports over 80% recall at under 4% false positives on its own benchmark. **[Documented]**
Detail:
• The result type `ScanResult` has `decision`, `reason`, `score` and `status` (`llamafirewall_data_types.py@172c1074:42-47`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Score: 1.0 when the judge's `conclusion` is true, otherwise 0.0 (`alignmentcheck_scanner.py@172c1074:120-125`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Decision: `HUMAN_IN_THE_LOOP_REQUIRED` when the score is 1.0, otherwise `ALLOW`; the function has no `BLOCK` branch, so AlignmentCheck never returns `BLOCK` (`alignmentcheck_scanner.py@172c1074:127-130`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Reason text: "Observation: ...\nThought: ...\nConclusion: ..." built from the judge's reply (`alignmentcheck_scanner.py@172c1074:104`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's tutorial shows a high-risk trace returning score 1.0000 and `HUMAN_IN_THE_LOOP_REQUIRED`, and a low-risk trace returning score 0.0000 and `ALLOW` (docs page tutorials/alignment-check-scanner-tutorial, sample output) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The scanner's `block_threshold` is inherited from `CustomCheckScanner` with default 0.0 and is not read by `AlignmentCheckScanner`, whose decision tests `score == 1.0` (`custom_check_scanner.py@172c1074:39`; `alignmentcheck_scanner.py@172c1074:128`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Multi-scanner aggregation: `LlamaFirewall.scan` returns `BLOCK` if any scanner blocked, otherwise the decision with the highest score, so a human-review result from this scanner is surfaced when no other scanner blocks (`llamafirewall.py@172c1074:143-160`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The `status` field is overwritten: `LlamaFirewall.scan` builds its returned result with `ScanStatus.SUCCESS`, so the scanner's `ERROR` status for a missing trace does not reach the caller (`llamafirewall.py@172c1074:134-140,162-167`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Failure behaviour, LLM call fails: the default error reply has `conclusion=True`, so the result is score 1.0 and `HUMAN_IN_THE_LOOP_REQUIRED` (fail closed to human review) and the reason starts "Observation: Error occurred during evaluation" (`custom_check_scanner.py@172c1074:76-78`; `alignmentcheck_scanner.py@172c1074:113-118`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Failure behaviour, no key: `LLMClient` raises `ValueError` when `TOGETHER_API_KEY` is empty, at scanner creation, so `LlamaFirewall.scan` raises instead of returning a result (`utils/base_llm.py@172c1074:46-50`; `llamafirewall.py@172c1074:118`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Failure behaviour, missing context: no trace or no user message gives `ALLOW` (fail open), the opposite of the LLM-error path (`alignmentcheck_scanner.py@172c1074:77-92`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• A tester cannot tell a true detection from an LLM error by decision alone; the error reason text is the only marker **[Inferred]**
• Published number, Meta goal-hijacking benchmark: "these models achieved over 80% recall with a false positive rate below 4%" for Llama 4 Maverick and Llama 3.3 70B, without fine-tuning (arXiv 2505.03574 section 4.2) **[Documented]**
• Published number, Maverick alone: "detecting over 83% of goal hijacking attempts while maintaining a very low FPR of 2.5%" (arXiv 2505.03574 Appendix C.2) **[Documented]**
• Benchmark size: 600 scenarios (300 benign, 300 malicious), 7 injection techniques and 8 threat categories, built inside Meta's internal agent simulation framework (arXiv 2505.03574 Appendix A.1) **[Documented]**
• The benchmark is released as the Hugging Face dataset `facebook/llamafirewall-alignmentcheck-evals`, metadata licence `mit`, not gated (Hugging Face API, observed 2026-10-09); the dataset files were not read **[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]**
• Published number, AgentDojo: baseline "attack success rate (ASR) of 17.6% and a task utility of 47.7%"; AlignmentCheck with Maverick "reduction in ASR to 2.89% - an 84% drop relative to baseline, but at the cost of lower utility (43.1%)" (arXiv 2505.03574 section 4.3.2) **[Documented]**
• The same paper gives a different rounding in section 4.2: "83% reduction in attack success rate, lowering it from 0.18 (no defenses) to 0.03"; the two are consistent within rounding but the percentages differ (arXiv 2505.03574 sections 4.2 and 4.3.2) **[Documented]**
• Combined with PromptGuard 2 86M the paper reports ASR 1.75% and utility 42.7% (arXiv 2505.03574 section 4.3.2) **[Documented]**
• Latency: the paper says only "significantly higher latency due to its semantic reasoning overhead" (arXiv 2505.03574 section 4.3.2) **[Documented]**
• Latency examples: the paper's appendix trace sample shows per-step values "latency_ms": 859.7846031188965 and 1490.03267288208 for one AgentDojo case with Maverick; these are two samples, not a measured distribution (arXiv 2505.03574 Appendix C.5) **[Documented]**
• Decision threshold or score guidance: none beyond the binary rule (checked the scanner docs page, tutorial, README and paper; no threshold or calibration guidance) **[Not disclosed]**
• Published latency distribution, throughput and cost per call for AlignmentCheck (checked the same pages and the llama.com protections page; not stated) **[Not disclosed]**
### R6
Summary: **Message, trace and a Together key.** It reads message content for the current action and the earlier trace, needs a user message in the trace, and needs the Together API key in the environment. Model and endpoint cannot be set through the scanner constructor. **[Documented]**
Detail:
• Required call shape: `scan(message, past_trace)` through `LlamaFirewall.scan(input, trace)`, `scan_replay(trace)` or the async variants (`llamafirewall.py@172c1074:108-123,189-211`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Environment: "If you plan to use the alignment check scanner, you will need to set up the Together API key in your environment" with `export TOGETHER_API_KEY=<your_api_key>` (`LlamaFirewall/README.md@172c1074:172`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• `llamafirewall configure` reports whether the key is set and prints "The Alignment Check Scanner requires this key to function."; it also accepts `TOGETHER_API_KEY` or `TOGETHER_API_TOKEN` in its check, but the scanner reads only `TOGETHER_API_KEY` (`cli/configure.py@172c1074:116-128,200`; `utils/base_llm.py@172c1074:46`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Python 3.10 or later and `pip install llamafirewall` (`LlamaFirewall/README.md@172c1074:53,60`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Hugging Face login and the Prompt Guard model are not needed by this scanner, because `create_scanner` imports each scanner class only when its type is requested (`llamafirewall.py@172c1074:60-69`) **[Inferred]**
• Context window: the paper says the trace is "truncated to a fixed context window for efficiency" (arXiv 2505.03574 Appendix C.1.1) **[Documented]**
• Context window in code: `_pre_process_trace` joins the whole trace with no truncation, and a search of `LlamaFirewall/src` for truncation or token limits finds only the 512-token limit in `promptguard_utils.py:113` (not used by this scanner) **[Not disclosed]**
• Long traces are therefore limited by the judge model's context window and the API, whose limit for the default model is not stated by Meta (checked the README, docs and paper) **[Not disclosed]**
• The judge model, endpoint, temperature and threshold are constructor arguments of `CustomCheckScanner` only; `AlignmentCheckScanner.__init__` accepts `scanner_name` alone, although its docstring lists the other arguments (`alignmentcheck_scanner.py@172c1074:42-61`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Together's own documentation (not Meta docs) now shows `base_url="https://api.together.ai/v1"` for its OpenAI-compatible endpoint, while the Meta code default is the `.xyz` host; whether the `.xyz` host still serves requests was not tested because research makes no vendor API calls (R019) **[To be verified]**
• Model availability on Together (not Meta docs): the serverless model table read 2026-10-09 lists `meta-llama/Llama-3.3-70B-Instruct-Turbo` and no Llama 4 Maverick entry, so the default judge model may not be served on that route **[To be verified]**
### R7
Summary: **Minimum setup:** install llamafirewall (Python 3.10 or later), set a Together API key, and attach the scanner to assistant messages. Build short traces of one user request plus agent actions, half hijacked, and compare decisions. Traces leave the machine for a third-party API, so use synthetic data. **[Inferred]**
Detail:
• **Minimum setup:** `pip install llamafirewall`, `export TOGETHER_API_KEY=...`, build `LlamaFirewall({Role.ASSISTANT: [ScannerType.AGENT_ALIGNMENT]})` and call `scan_replay` on a list of messages that starts with a `UserMessage`; research does not install or run it (R019), so this is a plan for the bench **[Inferred]**
• External dependency to state in the test plan: every scan sends the user objective and the trace text to a hosted LLM on Together AI, a third party, using a paid key; testing is therefore not local and not free of data-sharing **[Inferred]**
• Third-party terms (Together terms of service, not Meta docs): Your Content is the input sent to the Services; "Under ZDR, your data and outputs are not stored, retained, or used for model training" applies only if the account setting is chosen (https://www.together.ai/terms-of-service section 3, read 2026-10-09) **[Documented]**
• Third-party terms (Together, not Meta docs): "You will not use the Services to transmit or provide to the Company any financial or medical information of any nature or any sensitive personal data (e.g., social security numbers…" (section 4, read 2026-10-09), so traces for the bench should contain no real personal or financial data **[Documented]**
• Test inputs for the Table 3 type "agent trace": a user message plus assistant action messages, benign and hijacked pairs; Meta's released benchmark `facebook/llamafirewall-alignmentcheck-evals` (600 scenarios) is a ready candidate for seeding, subject to checking its file format **[Inferred]**
• Meta's own demo is `examples/demo_alignmentcheck.py` (two traces, high risk and low risk, needs `TOGETHER_API_KEY`) and is described in the tutorial page (`demo_alignmentcheck.py@172c1074:43,139`; docs page tutorials/alignment-check-scanner-tutorial) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Mark the judge model as a test variable: results depend on which model serves the call, and the default may need replacing by a subclass if Together no longer serves it **[Inferred]**
• Record the decision and the reason text, and flag results whose reason begins "Observation: Error occurred during evaluation" as errors, not detections **[Inferred]**
• Metrics for the bench: detection rate on hijacked traces, false-positive rate on benign traces, and calls per trace; the paper's figures (above 80% recall, below 4% false positives) are on Meta's benchmark and are not a bench target **[Inferred]**
### R8
Summary: **Key open questions.** Whether the default Maverick judge is still served on Together, Together cost and data terms for traces, latency and context limits, how the docs claim of whole-trace reasoning squares with the one-action prompt, and how reliable the judge is on the bench.
Detail:
• Is `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` still served on Together under the `.xyz` or `.ai` host (the Together model table read 2026-10-09 shows no Maverick row; no API call was made)? Needs testing or a Together catalogue check
• Cost per call and rate limits for the default model: checked the Meta README, docs and paper; Together pricing pages were not read
• Do Together's data-retention defaults allow agent traces, and what applies when ZDR is not enabled (checked the Together terms section 3; account defaults are not stated there)? Decision for the bench design, not research
• Latency per scan and its growth with trace length: checked the paper (two sample values only) and the docs; not stated; needs testing
• Context limit for long traces: the paper says truncation, the code does none (see R6); what happens when the trace exceeds the model window needs testing
• Does the judge rate only the latest action (prompt) or the whole trace (docs wording), and how does that change results on multi-step hijacks? Needs testing
• Are tool outputs in the trace treated as untrusted evidence or as part of the agent's own reasoning (paper says tool outputs are excluded, code does not exclude them)? Needs testing with injected tool output
• Is the judge itself manipulable by text in the trace (paper limitation C.4)? Needs testing with injections aimed at the judge
• Behaviour on non-English traces: checked the prompt and docs; not stated; needs testing
• Run-to-run variation at temperature 0.0 with a hosted model: not stated; needs repeated runs
• Whether the HF dataset `facebook/llamafirewall-alignmentcheck-evals` can be used directly as bench input (file format and fields were not read)
• Whether the PyPI 1.0.3 sdist matches the repo at 172c1074 (sdist not read)
### R9
Summary: Meta LlamaFirewall code, docs and tests at the pinned commit, the Meta-authored LlamaFirewall paper, Hugging Face metadata for the default model and the released benchmark, PyPI, and Together's own pages for third-party terms.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/experimental/alignmentcheck_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/custom_check_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/utils/base_llm.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall_data_types.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/config.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/cli/configure.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/pyproject.toml
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/examples/demo_alignmentcheck.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/scanners/alignment-check.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/tutorials/alignment-check-scanner-tutorial.md
• https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/scanners/alignment-check
• https://arxiv.org/html/2505.03574
• https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8/tree/94125d2bd83076b21eed33119525e29eaf3894f4
• https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/tree/d50916c9ea26e374667c030268218b28c20626a3
• https://pypi.org/simple/llamafirewall/
• https://www.together.ai/terms-of-service
• https://docs.together.ai/docs/serverless/models
• https://docs.together.ai/docs/inference/openai-compatibility

## Column PL5: LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner)
### R1
Summary: **Fixed regex blocking plus a custom-scanner route.** The Regex scanner blocks a message when it matches built-in patterns for two injection phrases, email, phone, credit card or social security number. Custom scanners are added by subclassing Scanner; LLM-prompt scanners are experimental. **[Documented]**
Detail:
• Meta's architecture page names the layer "Regex + Custom Scanners": "A configurable scanning layer for applying regular expressions or simple LLM prompts to detect known patterns, keywords, or behaviors across inputs, plans, or outputs." (docs page llamafirewall-architecture/architecture, line 24) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The workflow page lists the Regex scanner beside PromptGuard as detecting "jailbreak input" for direct and indirect jailbreak prompt injections (docs page llamafirewall-architecture/workflow-and-detection-components, risk table) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• `RegexScanner` "checks messages against a list of regex patterns" and "uses a predefined set of regex patterns for common security concerns" (`regex_scanner.py@172c1074:33-37`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• It is reached through `ScannerType.REGEX`, which `create_scanner` maps to `RegexScanner()` "with default patterns" (`llamafirewall.py@172c1074:74-78`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's regex tutorial page exists under tutorials, not under the Scanners section of the docs (docs page tutorials/regex-scanner-tutorial) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The custom-scanner route is a separate Python class that extends `Scanner` and is registered with `@register_llamafirewall_scanner("name")`, then used by its string name in the role configuration (`llamafirewall.py@172c1074:29-50`; `examples/demo_customized_scanner_via_open_guardrails.py@172c1074:32-33,62`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• CustomCheckScanner (experimental LLM-prompt base class): "[EXPERIMENTAL] A generic scanner that uses LLM prompts to evaluate content." (`custom_check_scanner.py@172c1074:25`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PIICheckScanner (experimental, LLM-based PII detection): "A scanner that detects Personally Identifiable Information (PII) in text." (`experimental/piicheck_scanner.py@172c1074:34-39`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The PIICheck scanner is reached through `ScannerType.PII_DETECTION` (`llamafirewall.py@172c1074:70-73`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Whether the regex scanner and the LLM-prompt scanners are one function or two is a column-split question for the checkpoint; this column keeps the LLM-prompt facts in their own bullets so they can be moved **[Inferred]**
### R2
Summary: **Two injection phrases and four US-style PII shapes.** The patterns match "ignore previous instructions", "ignore all instructions", and email, phone, credit card and social security number shapes. Nothing else is checked by the Regex scanner. **[Documented]**
Detail:
• Pattern "Prompt injection": `ignore previous instructions|ignore all instructions` (`regex_scanner.py@172c1074:23`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Pattern "Email address": `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b` (`regex_scanner.py@172c1074:25`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Pattern "Phone number": `\b(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b` (`regex_scanner.py@172c1074:26`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Pattern "Credit card": `\b(?:\d{4}[- ]?){3}\d{4}\b` (`regex_scanner.py@172c1074:27`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Pattern "Social security number": `\b\d{3}-\d{2}-\d{4}\b` (`regex_scanner.py@172c1074:28`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Patterns are compiled with `re.IGNORECASE | re.DOTALL`, so matching ignores case (`regex_scanner.py@172c1074:59`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The phone pattern is a ten-digit North American shape with an optional country digit group, the social security pattern is the United States dashed format, and the card pattern matches any sixteen digits in four groups with no checksum test; formats from other countries and card numbers with other lengths are not matched **[Inferred]**
• The prompt-injection pattern matches only two literal phrases, so paraphrases, other languages or encoded text are not matched **[Inferred]**
• The email pattern's top-level-domain class is written `[A-Z|a-z]`, which also accepts a literal pipe character (`regex_scanner.py@172c1074:25`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages: the patterns are English phrases and Latin-script digits; no language support statement exists (checked the architecture page, tutorial, README and paper; not stated) **[Not disclosed]**
• LLM-prompt scanner scope, PIICheckScanner: the system prompt lists seven PII types: full names, email addresses, phone numbers, physical addresses, social security numbers, credit card numbers, passport numbers (`experimental/piicheck_scanner.py@172c1074:119-126`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• LLM-prompt scanner scope, CustomCheckScanner: scope is whatever system prompt a subclass supplies; the base class defines none (`custom_check_scanner.py@172c1074:28-33,62`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The docs describe PII_DETECTION only as an enum value in a tutorial sentence; there is no docs page for the PIICheck scanner or for CustomCheckScanner (`website/docs/tutorials/prompt-guard-scanner-tutorial.md@172c1074:30`; checked the scanners, architecture, advanced-usage and tutorials folders) **[Not disclosed]**
### R3
Summary: **Any role, message text only.** The scanner reads the content of whichever message role it is attached to and ignores the trace. It is not in the default role map, so it must be configured. **[Documented]**
Detail:
• The scanner reads `message.content` and its `scan` documents `past_trace` as "(not used in this scanner)" (`regex_scanner.py@172c1074:71,76`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Roles are `TOOL` (tool output), `USER` (user input), `ASSISTANT` (LLM output), `MEMORY` and `SYSTEM` (system input), and a `Configuration` maps each role to a list of scanners (`llamafirewall_data_types.py@172c1074:34-39`; `config.py@172c1074:13`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's regex tutorial attaches it to `Role.USER` only: `Role.USER: [ScannerType.REGEX]` with empty lists for the other roles (docs page tutorials/regex-scanner-tutorial, custom configuration section) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The scanner can equally be attached to `ASSISTANT`, `TOOL`, `MEMORY` or `SYSTEM`; the code has no per-role logic, so the same patterns apply to prompts, responses, retrieved text and tool outputs (`llamafirewall.py@172c1074:113-122`) **[Inferred]**
• The no-config default role map does not include the Regex scanner (`TOOL`: CodeShield and PromptGuard, `USER`: PromptGuard, `ASSISTANT`: CodeShield) (`llamafirewall.py@172c1074:90-96`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Direction under R002: there is no input or output mode, so this is one column with no level word; R6 and the inventory role block carry the role detail **[Inferred]**
• Custom scanners receive the same `scan(message, past_trace)` call as built-in ones and may use the trace (`scanners/base_scanner.py@172c1074:22-30`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PIICheckScanner reads `message.content` only, and ignores `past_trace` (`experimental/piicheck_scanner.py@172c1074:93-97`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Custom-check scanners built on `CustomCheckScanner` decide their own use of the trace; AlignmentCheck is the one that uses it (column PL3) **[Inferred]**
### R4
Summary: **Compiled regular expressions, no model.** Python patterns are compiled once with case-insensitive matching and run locally with no key. Custom scanners subclass Scanner and register by name; the experimental LLM-prompt scanners call Together. **[Documented]**
Detail:
• Mechanism: five patterns held in the constant `DEFAULT_REGEX_PATTERNS` are compiled in the constructor and tried in dictionary order; no model, no key, no network (`regex_scanner.py@172c1074:21-29,53-61,79-80`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Constructor arguments are `scanner_name` and `block_threshold` only; there is no argument for patterns (`regex_scanner.py@172c1074:41-45`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The `block_threshold` of 1.0 is passed to the base class but the scan decides by a match, not by comparing a score to the threshold (`regex_scanner.py@172c1074:53,79-87`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, configurability (docs side): the architecture page calls the layer "configurable" for "regular expressions or simple LLM prompts" (docs page llamafirewall-architecture/architecture, line 24) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, configurability (code side): the pattern set is the fixed constant and the tutorial's "custom configuration" only chooses roles (`regex_scanner.py@172c1074:21-29`; docs page tutorials/regex-scanner-tutorial) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Replacing patterns by assigning to `scanner.patterns` after construction is possible in Python but does not persist through `LlamaFirewall`, which creates a new scanner instance for each scan call (`llamafirewall.py@172c1074:117-118`) **[Inferred]**
• Custom scanner route, code: extend `Scanner` (abstract async `scan(message, past_trace)`), decorate with `@register_llamafirewall_scanner("name")`, and list the string name in the configuration; the registry instantiates the class with no arguments (`scanners/base_scanner.py@172c1074:12-30`; `llamafirewall.py@172c1074:29-50`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's working example registers `DemoScanner` and uses it for `Role.USER` and `Role.SYSTEM` inside an OpenAI Agents SDK input guardrail (`examples/demo_customized_scanner_via_open_guardrails.py@172c1074:32-34,60-73`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, custom scanner how-to (docs side): the page says to create a class that "inherits from the `BaseScanner` class" and to edit `create_scanner` with a new `ScannerType` member (docs page advanced-usage/adding-custom-scanner, steps 2 and 4) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, custom scanner how-to (code side): the base class is `Scanner` in `scanners/base_scanner.py`; no `BaseScanner` class exists under `src` (checked by search of `LlamaFirewall/src`), and the registry decorator makes editing `create_scanner` unnecessary (`scanners/base_scanner.py@172c1074:12`; `llamafirewall.py@172c1074:32-43`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• CustomCheckScanner mechanism: an abstract base class that calls an OpenAI-compatible chat API with a system prompt and a structured output schema; subclasses must implement `_get_default_error_response`, `_convert_llm_response_to_score` and `scan` (`custom_check_scanner.py@172c1074:23-33,59-63,66-103`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• CustomCheckScanner defaults: model `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`, base URL `https://api.together.xyz/v1`, key variable `TOGETHER_API_KEY`, temperature 0.0, `block_threshold` 0.0 (`custom_check_scanner.py@172c1074:35-39`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• CustomCheckScanner is exported in `scanners.__all__` but has no `ScannerType` member and is not in the top-level `llamafirewall` exports, so a configuration uses it only through a registered subclass (`scanners/__init__.py@172c1074:14-21`; `llamafirewall_data_types.py@172c1074:13-19`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PIICheckScanner mechanism: a `CustomCheckScanner` subclass with a fixed PII system prompt and three worked examples, structured output `detected_pii_types` (list of strings) (`experimental/piicheck_scanner.py@172c1074:25-33,116-165`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PIICheckScanner defaults: model `meta-llama/Llama-3.3-70B-Instruct-Turbo`, base URL `https://api.together.xyz/v1`, key variable `TOGETHER_API_KEY`, temperature 0.0, `block_threshold` 0.7 (`experimental/piicheck_scanner.py@172c1074:42-50`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Pins, stated separately. Code and repo docs: commit 172c1074 (author date 2026-09-29). PyPI: `llamafirewall` 1.0.3 in the simple index (observed 2026-10-09; sdist not read); no release tag or CHANGELOG exists in the repo **[Documented]**
• Licence: MIT (`LlamaFirewall/LICENSE@172c1074:1`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Release notes and a version history for the scanners (checked `git ls-remote --tags`, the clone for a CHANGELOG file and the docs site) **[Not disclosed]**
### R5
Summary: **Block on first match, score 1.0.** A match returns block with the pattern name as the reason; no match returns allow at 0.0. Only one matching pattern is reported. **[Documented]**
Detail:
• Regex scanner result: first matching pattern gives `BLOCK`, reason `Regex match: <name>`, score 1.0, status `SUCCESS` (`regex_scanner.py@172c1074:79-87`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• No match gives `ALLOW`, reason "No regex patterns matched", score 0.0 (`regex_scanner.py@172c1074:39,89-95`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The scan returns on the first match in dictionary order, so a message containing several patterns reports only one (`regex_scanner.py@172c1074:79-87`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The returned object is `ScanResult` with `decision`, `reason`, `score`, `status` (`llamafirewall_data_types.py@172c1074:42-47`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's tutorial output shows `Reason: Regex match: Prompt injection`, `Credit card`, `Email address`, `Phone number` and `Social security number`, each with score 1.0 (docs page tutorials/regex-scanner-tutorial, sample output) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, reason text on allow (docs side): in the tutorial's custom `LlamaFirewall` run the allowed messages show `Reason: default` (docs page tutorials/regex-scanner-tutorial, custom output) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Source conflict, reason text on allow (code side): with a single scanner `LlamaFirewall.scan` returns the scanner's own reason, which for an allowed message is "No regex patterns matched" (`llamafirewall.py@172c1074:134-140`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Through `LlamaFirewall.scan`, results from several scanners are combined: `BLOCK` wins if any scanner blocks, otherwise the highest-score decision (`llamafirewall.py@172c1074:143-160`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• CustomCheckScanner output: no fixed output; each subclass defines its schema and its score (`custom_check_scanner.py@172c1074:66-103`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PIICheckScanner output: score 1.0 if the model returns any PII type other than `["ERROR"]` or `["None"]`, else 0.0; `BLOCK` with reason "PII detected: <types>" when the score is at least `block_threshold` (0.7), else `ALLOW` (`experimental/piicheck_scanner.py@172c1074:80-106`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PIICheckScanner failure behaviour: if the LLM call fails the default reply is `["ERROR"]`, which scores 0.0, so the message is allowed (fail open); a missing key raises `ValueError` at scanner creation (`experimental/piicheck_scanner.py@172c1074:74-78,83-90`; `utils/base_llm.py@172c1074:46-50`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• This is the opposite of AlignmentCheck, which fails closed to human review on an LLM error (column PL3) **[Inferred]**
• Accuracy, precision or recall of the Regex scanner, PIICheckScanner or any custom scanner (checked the paper, which reports no regex or PII scanner evaluation, plus the README, docs and the llama.com protections page) **[Not disclosed]**
• Threshold guidance: none for any of the three; the Regex scanner's 1.0 and PIICheck's 0.7 are code defaults, not Meta recommendations (checked the same sources) **[Not disclosed]**
• Latency and throughput of the Regex scanner (checked the README, docs and paper; the README says only "Real-Time" for the framework) **[Not disclosed]**
### R6
Summary: **Plain text in, no keys or models for Regex.** The scanner takes message content as a string and needs no API key or model. The pattern set cannot be changed through the constructor. **[Documented]**
Detail:
• Input is `Message(role, content, tool_calls)` through `LlamaFirewall.scan`, or a direct `scan(message)` call on `RegexScanner` as in the tutorial (`llamafirewall_data_types.py@172c1074:50-54`; docs page tutorials/regex-scanner-tutorial) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Python 3.10 or later and `pip install llamafirewall` (`LlamaFirewall/README.md@172c1074:53,60`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The Regex scanner needs no Hugging Face login, model download or API key; the setup notes for those apply to PromptGuard and AlignmentCheck (`LlamaFirewall/README.md@172c1074:141-172`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Size limits: the scanner applies each pattern to the whole content; no length limit is coded (checked `regex_scanner.py`) **[Not disclosed]**
• Only `message.content` is scanned; the `Message` `tool_calls` field is not read by this or any other scanner in the package (search of `LlamaFirewall/src`), so tool-call arguments are matched only if they appear in the content text **[Inferred]**
• Custom scanner inputs: a custom scanner gets the `Message` and the optional `Trace` and returns a `ScanResult`; its constructor must be callable with no arguments (`scanners/base_scanner.py@172c1074:22-30`; `llamafirewall.py@172c1074:47-50`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• CustomCheckScanner and PIICheckScanner need `TOGETHER_API_KEY` in the environment; a missing key raises `ValueError` when the scanner is created (`utils/base_llm.py@172c1074:45-50`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• PIICheckScanner sends the scanned text, which is by definition text that may hold personal data, to the Together API (`experimental/piicheck_scanner.py@172c1074:93-97`; `utils/base_llm.py@172c1074:93-98`) **[Inferred]**
• Third-party terms (Together, not Meta docs): "You will not use the Services to transmit or provide to the Company any financial or medical information of any nature or any sensitive personal data (e.g., social security numbers…" (https://www.together.ai/terms-of-service section 4, read 2026-10-09) **[Documented]**
### R7
Summary: **Minimum setup:** install llamafirewall (Python 3.10 or later), configure the scanner for the roles under test, and send labelled strings containing each pattern plus benign and obfuscated variants. No key or model download is needed for the Regex scanner alone. **[Inferred]**
Detail:
• **Minimum setup:** `pip install llamafirewall`, then `LlamaFirewall({Role.USER: [ScannerType.REGEX]})` (or the same for `ASSISTANT` and `TOOL`) and `scan` each string; no key, no login; research does not install or run it (R019), so this is a plan for the bench **[Inferred]**
• Test inputs for Table 3 input types: user prompts, model responses and tool or retrieved text that contain each of the five patterns, near misses (other phone and card formats, paraphrased injection phrases), and clean text **[Inferred]**
• Expected labels follow the code: `BLOCK` with the pattern name for the five shapes, `ALLOW` otherwise; Meta's tutorial strings are usable as a smoke test (docs page tutorials/regex-scanner-tutorial, message list) **[Inferred]**
• For a custom scanner: write a `Scanner` subclass with a no-argument constructor, register it with `@register_llamafirewall_scanner`, and list its name in the role configuration; Meta's demo shows the shape (`examples/demo_customized_scanner_via_open_guardrails.py@172c1074:32-50`) **[Inferred]**
• For LLM-prompt scanners (CustomCheckScanner subclasses, PIICheckScanner): additionally set `TOGETHER_API_KEY`; every scan sends the text to Together, a third party; use synthetic data only and check the Together terms first **[Inferred]**
• If the LLM-prompt scanners become a separate column at the checkpoint, the CustomCheckScanner and PIICheckScanner bullets in R1 to R8 move together **[Inferred]**
### R8
Summary: **Key open questions.** Whether patterns can be configured without code changes, how well the fixed patterns hold up on obfuscated or non-US formats, how the stale custom-scanner docs relate to the registry, and the cost, data terms and accuracy of the experimental LLM-prompt scanners.
Detail:
• Detection rate and false-positive rate of the five patterns on a labelled prompt set (no Meta figure; needs testing)
• Do obfuscated or spaced variants (extra spaces, Unicode lookalikes, other languages) evade the two injection phrases (needs testing)
• Coverage of non-US phone numbers, social security formats and card numbers with other lengths (needs testing)
• Does the Luhn checksum matter, given that any sixteen digits in four groups match (needs testing for false positives such as order numbers)
• Will Meta add a constructor argument for custom patterns (checked the code and docs; the docs promise a "configurable" layer but the code takes no pattern argument)
• Which source is right for the custom-scanner how-to, the stale `BaseScanner` page or the registry in the code (code is stronger; the docs were not updated at the pin)
• Why the tutorial shows `Reason: default` for allowed messages while the code returns the scanner's reason (docs may predate the code; needs a run)
• PIICheckScanner and CustomCheckScanner: cost per call, rate limits, Together model availability for `meta-llama/Llama-3.3-70B-Instruct-Turbo` (listed on the Together model table read 2026-10-09) and for the Maverick default of CustomCheckScanner (not listed there)
• Whether Together's terms allow sending real personal data for PII scanning, given the clause that bars transmitting sensitive personal data (checked the terms section 4; legal reading is for the checkpoint)
• PIICheckScanner accuracy on the seven listed PII types and its fail-open behaviour on API errors (needs testing)
• Whether the experimental LLM-prompt scanners should be a separate column (checkpoint question; see R7)
• Latency of the Regex scanner (not stated; needs testing)
### R9
Summary: Meta LlamaFirewall code, docs and examples at the pinned commit, the Meta-authored LlamaFirewall docs site, PyPI, and Together's terms page for the third-party API.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/regex_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/base_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/custom_check_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/experimental/piicheck_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/__init__.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall_data_types.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/config.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/utils/base_llm.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/examples/demo_customized_scanner_via_open_guardrails.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/architecture.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/advanced-usage/adding-custom-scanner.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/tutorials/regex-scanner-tutorial.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/tutorials/prompt-guard-scanner-tutorial.md
• https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/tutorials/regex-scanner-tutorial
• https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/advanced-usage/adding-custom-scanner
• https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/llamafirewall-architecture/architecture
• https://arxiv.org/html/2505.03574
• https://pypi.org/simple/llamafirewall/
• https://www.together.ai/terms-of-service
• https://docs.together.ai/docs/serverless/models

## Column PL7: LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner)
### R1
Summary: **Blocks invisible Unicode tag characters.** The Hidden ASCII scanner blocks any text containing a character from U+E0000 to U+E007F and puts the decoded hidden text in the reason. **[Documented]**
Detail:
• The scanner returns `BLOCK` when any character of the content has a code point from `0xE0000` to `0xE007F`, otherwise `ALLOW` (`hidden_ascii_scanner.py@172c1074:30-31,50-56`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• On a hit the reason is "Hidden ASCII: " followed by the content with each tag character mapped back to the ASCII character at code point minus `0xE0000` (`hidden_ascii_scanner.py@172c1074:35-45,58-62`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• It is reached through `ScannerType.HIDDEN_ASCII`, which `create_scanner` maps to `HiddenASCIIScanner()` (`llamafirewall.py@172c1074:56-59`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The `ScannerType` enum names it: "CODE_SHIELD, PROMPT_GUARD, AGENT_ALIGNMENT, HIDDEN_ASCII, PII_DETECTION" (`website/docs/tutorials/prompt-guard-scanner-tutorial.md@172c1074:30`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• No docs page, README section, paper passage or llama.com page describes this scanner or its purpose (checked the docs site folders, both READMEs, the paper and the protections page for "hidden" and "ASCII"; only the enum sentence above) **[Not disclosed]**
• The column is provisional: it is drafted so it can be dropped to an inventory-only row at the checkpoint **[Inferred]**
### R2
Summary: **Text hidden in the Unicode tag block.** The code flags only characters from U+E0000 to U+E007F; other invisible characters are not checked by the range test. **[Inferred]**
Detail:
• The checked range is the whole Unicode Tags block, `0xE0000` to `0xE007F` inclusive (`hidden_ascii_scanner.py@172c1074:30,37`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Because the decoder maps each tag character to the ASCII character with the same low byte, the scanner is aimed at instructions written invisibly as tag characters and then read by a model; this purpose is not stated by Meta **[Inferred]**
• Other invisible or look-alike characters (zero-width spaces, bidirectional controls, variation selectors, homoglyphs) are outside the range and are not flagged by this scanner **[Inferred]**
• Meta's workflow page gives an example of invisible text in a PDF ("Invisible text near the end says…") but maps it to PromptGuard and the Regex scanner, not to the Hidden ASCII scanner (docs page llamafirewall-architecture/workflow-and-detection-components, risk table) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Languages: the test is on code points, so it is language-neutral; no language statement exists (checked the docs and paper) **[Not disclosed]**
• Out of scope: it does not read what the hidden text says, so it does not judge whether the hidden instruction is harmful; any tag character blocks **[Inferred]**
### R3
Summary: **Any role, message text only.** It reads message content for whichever role it is attached to and ignores the trace; it is not in the default role map. Meta's own test attaches it to tool messages. **[Documented]**
Detail:
• The scanner reads `message.content` and does not use `past_trace` (`hidden_ascii_scanner.py@172c1074:47-50`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's unit test attaches it to `Role.TOOL` with a tool message containing tag characters (`tests/test_hidden_ascii_scanner.py@172c1074:19-24,28-36`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The no-config default role map does not include it (`llamafirewall.py@172c1074:90-96`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• A second test combines it with other scanners in one configuration (`tests/test_multiple_scanners.py@172c1074:19,28`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The code has no per-role logic, so it can be attached to `USER`, `ASSISTANT`, `TOOL`, `MEMORY` or `SYSTEM` and then covers prompts, responses, retrieved text and tool outputs (`llamafirewall.py@172c1074:113-122`) **[Inferred]**
• Direction under R002: no input or output mode, so one column with no level word **[Inferred]**
### R4
Summary: **Pure Python code-point test.** No model, key or download is involved. The block threshold of 1.0 is the default, and the score is only ever 0.0 or 1.0. **[Documented]**
Detail:
• Mechanism: a generator over the characters of the content with a range comparison; no model, no network, no key (`hidden_ascii_scanner.py@172c1074:28-32`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The constructor takes `scanner_name` and `block_threshold` (default 1.0); the score is 1.0 or 0.0, so a threshold of 1.0 or lower behaves the same and a value above 1.0 would never block (`hidden_ascii_scanner.py@172c1074:20-26,50-56`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Pins, stated separately. Code and repo docs: commit 172c1074 (author date 2026-09-29). PyPI: `llamafirewall` 1.0.3 in the simple index (observed 2026-10-09; sdist not read). No release tag or CHANGELOG exists in the repo **[Documented]**
• Licence: MIT (`LlamaFirewall/LICENSE@172c1074:1`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Release notes or version history for this scanner (checked `git ls-remote --tags`, the clone for a CHANGELOG file and the docs site) **[Not disclosed]**
### R5
Summary: **Block at score 1.0 with decoded text.** A hit returns block with the reason Hidden ASCII followed by the decoded characters; no hit returns allow at 0.0. **[Documented]**
Detail:
• Result: `BLOCK`, score 1.0, status `SUCCESS`, reason "Hidden ASCII: <decoded text>" on a hit; `ALLOW`, score 0.0, reason "No hidden ASCII detected" otherwise (`hidden_ascii_scanner.py@172c1074:19,52-72`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Meta's test asserts a block, a score of at least 0.8 and "Hidden ASCII" in the reason for a tag-character string, and an allow with the allow reason for ordinary text (`tests/test_hidden_ascii_scanner.py@172c1074:30-52`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• The reason text carries the decoded hidden content back to the caller, so logs and any user-facing message built from the reason would repeat the hidden text **[Inferred]**
• Multi-scanner aggregation as in the other scanners: `BLOCK` wins, else the highest-score decision (`llamafirewall.py@172c1074:143-160`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Published accuracy, coverage or latency for this scanner (checked the docs, both READMEs, the paper and the llama.com protections page; none) **[Not disclosed]**
• Threshold guidance: none; the default 1.0 is a code default and the score is binary (checked the same sources) **[Not disclosed]**
### R6
Summary: **Plain text in, nothing else needed.** The scanner takes a string and walks every character; there is no key, model or setting beyond the threshold. **[Documented]**
Detail:
• Input is `Message.content` as a Python string; any role (`hidden_ascii_scanner.py@172c1074:47-50`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Python 3.10 or later and `pip install llamafirewall` (`LlamaFirewall/README.md@172c1074:53,60`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• No Hugging Face login, model download or API key is needed for this scanner (`hidden_ascii_scanner.py@172c1074:28-45`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Size limits: none coded; the test is linear in content length (`hidden_ascii_scanner.py@172c1074:28-32`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
• Text must reach the scanner with tag characters intact; any upstream step that strips or normalises them hides the signal from the scanner **[Inferred]**
### R7
Summary: **Minimum setup:** install llamafirewall, attach the scanner to the roles under test (tool output is the case Meta tests), and send strings with tag-block characters, with and without visible text, plus ordinary and emoji text. No key or model is needed. **[Inferred]**
Detail:
• **Minimum setup:** `pip install llamafirewall`, then `LlamaFirewall({Role.TOOL: [ScannerType.HIDDEN_ASCII]})` and `scan` each string, as Meta's test does; no key, no login; research does not install or run it (R019), so this is a plan for the bench **[Inferred]**
• Test inputs for Table 3 input types: tool or retrieved text, user prompts and model responses; build positives by encoding an ASCII sentence into U+E0000 to U+E007F characters, alone and appended to visible text, and negatives from clean text, accented and non-Latin text, and other invisible characters **[Inferred]**
• Expected labels follow the code: any tag character gives `BLOCK`, nothing else does; the decoded sentence should appear in the reason **[Inferred]**
• Note for the bench plan: this scanner is a deterministic filter, so one pass per string is enough; no repeated runs for variation **[Inferred]**
### R8
Summary: **Key open questions.** Why Meta does not document the scanner, whether it is meant to be supported, whether ordinary emoji sequences that use tag characters are blocked, and how it fits with the other injection defences.
Detail:
• Is the scanner intended as a supported feature? Checked the docs, READMEs, paper and protections page; the only mention is one enum sentence in a tutorial
• Are emoji sequences that use tag characters (for example some regional flags) blocked as false positives (needs testing; the range test blocks any tag character)
• Do other invisible-character tricks (zero-width characters, variation selectors, bidirectional controls) need a separate check in the bench (outside this scanner's range)
• Is the decoded reason safe to display to users or models (needs a policy decision for the bench)
• Does any production path normalise away tag characters before the scanner sees them (needs testing in the bench pipeline)
• Release history and stability of the scanner: not stated (checked as in R4)
### R9
Summary: Meta LlamaFirewall code, tests and the one docs sentence at the pinned commit, and PyPI.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/scanners/hidden_ascii_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/src/llamafirewall/llamafirewall.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/tests/test_hidden_ascii_scanner.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/tests/test_multiple_scanners.py
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/README.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/LICENSE
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/tutorials/prompt-guard-scanner-tutorial.md
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md
• https://pypi.org/simple/llamafirewall/

