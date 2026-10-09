## Column PL2: LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner)
### R1
Summary: **Input-level prompt-attack scanning in LlamaFirewall.** The PromptGuard scanner runs the Prompt Guard 2 86M model on a message's text and returns allow or block with a score. The block threshold defaults in code to 0.9, and the message role decides whether it runs. @@D@@
Detail:
• The scanner wraps the Prompt Guard 2 model: "PromptGuard 2 is a fine-tuned BERT-style model designed to detect direct jailbreak attempts in real-time" (LlamaFirewall/website/docs/documentation/scanners/prompt-guard-2.md@172c1074:4) @@L@@
• Code: class PromptGuardScanner, scanner name "Prompt Guard Scanner", block threshold parameter default 0.9 (prompt_guard_scanner.py@172c1074:19-28) @@L@@
• Decision rule: "ScanDecision.BLOCK if score >= self.block_threshold else ScanDecision.ALLOW" (prompt_guard_scanner.py@172c1074:39) @@L@@
• Selected in configuration by the scanner type PROMPT_GUARD (llamafirewall_data_types.py@172c1074:15) @@L@@
• Role of the wrapper versus the model: the wrapper adds role configuration, a decision with a reason and score, model download and aggregation with other scanners; the classification itself is the Prompt Guard 2 model described in column PL1 (premise: code files named in this column) @@I@@
• Framework description: "LlamaFirewall is a framework designed to detect and mitigate AI centric security risks, supporting multiple layers of inputs and outputs" (LlamaFirewall/README.md@172c1074:2) @@L@@
• Names: the README feature list says "PromptGuardScanner" (line 12) and its architecture section says "PromptGuard 2" (LlamaFirewall/README.md@172c1074:26) @@L@@
### R2
Summary: **Jailbreak and injection phrasing in text.** The scanner catches explicit instruction-override attempts in user prompts and untrusted content such as web data. Meta lists direct and indirect universal jailbreaks as covered risks. Goal hijacking is left to AlignmentCheck. @@D@@
Detail:
• Risks covered: "Direct Universal Jailbreak Prompt Injections" and "Indirect Universal Jailbreak Prompt Injections" (prompt-guard-2.md@172c1074:15-16) @@L@@
• Layered risk: PromptGuard 2 "along with other scanners, provides a layered defense against code-oriented prompt injection" (prompt-guard-2.md@172c1074:17) @@L@@
• Intended inputs: it "operates on user inputs and untrusted content such as web data" (LlamaFirewall/README.md@172c1074:27) @@L@@
• Scope wording differs: README "detects direct prompt injection attempts" (line 27), docs page "direct jailbreak attempts" (prompt-guard-2.md line 4), model card both injection and jailbreak (PL1 column) (LlamaFirewall/README.md@172c1074:27) @@L@@
• Narrow scope from the model card: a prompt is malicious only if it "explicitly attempts to override prior instructions" (Llama-Prompt-Guard-2/86M/MODEL_CARD.md@172c1074:22) @@L@@
• Goal hijacking is assigned to another scanner: AlignmentCheck "detect[s] goal hijacking, indirect prompt injections, and signs of agent misalignment" (LlamaFirewall/README.md@172c1074:33) @@L@@
• Docs mapping: "PromptGuard and Regex scanner detect jailbreak input" for direct and indirect universal jailbreaks (workflow-and-detection-components.md@172c1074:9) @@L@@
• Languages: the scanner always loads the 86M model, which is the multilingual one; the card lists eight evaluated languages (promptguard_utils.py@172c1074:40) @@L@@
• Out of scope: the scanner does not read tool-call arguments, only message content (premise: no scanner file reads the tool_calls field; grep of LlamaFirewall/src found it only in llamafirewall_data_types.py) @@I@@
• Block reasons include the full scanned text, so the blocked prompt is echoed in the result: reason string "Full text: \"{text}\"" (prompt_guard_scanner.py@172c1074:43) @@L@@
### R3
Summary: **Whatever text a configured role carries.** The scanner reads only the message content, ignores the trace, and can be attached to any role. Defaults scan USER and TOOL messages; the chat-bot use case adds SYSTEM. @@D@@
Detail:
• Reads one field: "text = message.content"; the past trace argument is accepted but unused (prompt_guard_scanner.py@172c1074:31-34) @@L@@
• Roles are an enum: TOOL (tool output), USER (user input), ASSISTANT (LLM output), MEMORY, SYSTEM (system input) (llamafirewall_data_types.py@172c1074:34-39) @@L@@
• A configuration maps each role to a list of scanner types: "Configuration: TypeAlias = Mapping[Role, Sequence[ScannerType | str]]" (config.py@172c1074:13) @@L@@
• No-config default: TOOL scans CODE_SHIELD and PROMPT_GUARD, USER scans PROMPT_GUARD, SYSTEM none, ASSISTANT scans CODE_SHIELD, MEMORY none (llamafirewall.py@172c1074:90-96) @@L@@
• CHAT_BOT use case: PROMPT_GUARD for USER and SYSTEM (config.py@172c1074:22-25) @@L@@
• README example attaches it to USER only (LlamaFirewall/README.md@172c1074:72) @@L@@
• Direction (R002): there is no separate input or output scanner; the same scanner can be attached to any role, so prompts, tool outputs, retrieved text in TOOL or MEMORY messages, and assistant text are all reachable by configuration (premise: config.py and llamafirewall.py) @@I@@
• Meta's own AgentDojo evaluation scanned only user and tool messages with it (arXiv 2505.03574 section 4.3) @@D@@
• Use on assistant output: no page recommends or evaluates it on the ASSISTANT role (checked the README, docs pages and paper) @@N@@
• The message type has an optional tool_calls field, but this scanner does not read it, so function-call arguments are not scanned (premise: prompt_guard_scanner.py reads message.content only) @@I@@
• The framework selects scanners by the message role: "scanners = self.scanners.get(input.role, [])" (llamafirewall.py@172c1074:113) @@L@@
• Name conflict: the custom use case page uses ScannerType.PROMPT_INJECTION for CHAT_BOT (adding-custom-use-case.md@172c1074:19-20) @@L@@
• Code and the how-to page use PROMPT_GUARD, and PROMPT_INJECTION is not in the ScannerType enum, so the live name is PROMPT_GUARD (llamafirewall_data_types.py@172c1074:13-19) @@L@@
### R4
Summary: **A Python wrapper around the 86M model, downloaded on first use.** The scanner loads Prompt Guard 2 86M through Transformers, cleans whitespace, truncates to 512 tokens and takes the last class probability as the score. It ships in the llamafirewall package. @@D@@
Detail:
• Model: "meta-llama/Llama-Prompt-Guard-2-86M" is the default and the scanner has no argument to pick the 22M model (promptguard_utils.py@172c1074:40) @@L@@
• Selecting the 22M model needs a code change (premise: the constructor of the scanner and of the PromptGuard class take no model argument) @@I@@
• Local copy: path is $HF_HOME joined with the model name with "/" replaced by "--"; HF_HOME defaults to "~/.cache/huggingface" if unset (promptguard_utils.py@172c1074:43-50) @@L@@
• If the folder is missing the code logs "We are downloading it from Hugging Face Hub. This may take a while..." and calls login() when no token is found (promptguard_utils.py@172c1074:54-61) @@L@@
• After download it saves the model and tokenizer to the local path for later runs (promptguard_utils.py@172c1074:63-69) @@L@@
• Runs on CUDA when available, otherwise CPU (promptguard_utils.py@172c1074:33-36) @@L@@
• Preprocessing: removes whitespace, re-tokenises and rebuilds the text before scoring; on an exception it returns the original text (promptguard_utils.py@172c1074:79-102) @@L@@
• Truncation: "padding=True, truncation=True, max_length=512" (promptguard_utils.py@172c1074:113) @@L@@
• Score: softmax of the logits at temperature 1.0 and "probabilities[0, -1].item()", the last class probability (promptguard_utils.py@172c1074:104-129) @@L@@
• The last class is taken to be "malicious" (premise: the card lists two labels, benign then malicious, and the Hugging Face config is not readable without approved access) @@I@@
• The framework builds a new scanner object for each scan call, which loads the model from disk each time (premise: create_scanner is called inside scan at llamafirewall.py line 118 and the scanner constructor builds PromptGuard); reuse of one loaded model is not shown @@I@@
• Package versions: llamafirewall 1.0.3 in the repo (LlamaFirewall/pyproject.toml@172c1074:7) @@L@@
• PyPI simple index lists llamafirewall 1.0.3 as the latest file (PyPI simple index, observed 2026-10-09) @@D@@
• Dependencies include torch>=2.4.1, transformers>=4.51.3 and huggingface_hub>=0.30.2 (LlamaFirewall/pyproject.toml@172c1074:15-22) @@L@@
• Python 3.10 or later is required (LlamaFirewall/README.md@172c1074:53) @@L@@
• LlamaFirewall code is MIT licensed; the model keeps its own Llama 4 licence, see column PL1 (LlamaFirewall/LICENSE@172c1074:1) @@L@@
• Release notes for llamafirewall (checked the repo at the pin: no tags and no CHANGELOG file; PyPI lists versions 1.0.2 and 1.0.3 without notes) @@N@@
### R5
Summary: **Allow or block with a reason and a probability score.** A score at or above the block threshold blocks. The default threshold of 0.9 is a code value. Model figures come from the Prompt Guard 2 card. @@D@@
Detail:
• Result object: ScanResult with fields decision, reason, score and status (llamafirewall_data_types.py@172c1074:43-47) @@L@@
• Decision values: ALLOW, HUMAN_IN_THE_LOOP_REQUIRED, BLOCK; this scanner returns only ALLOW or BLOCK (llamafirewall_data_types.py@172c1074:22-25) @@L@@
• Allow reason text is "No prompt injection detected"; the block reason names the probability and echoes the text (prompt_guard_scanner.py@172c1074:20,42-46) @@L@@
• Default block threshold 0.9 is a code default (prompt_guard_scanner.py@172c1074:24) @@L@@
• A Meta-recommended threshold for the scanner or model (checked the README, docs pages, tutorials, paper and model card; none gives one) @@N@@
• Single scanner on a role: the framework returns that scanner's result, with its own reason and score (llamafirewall.py@172c1074:134-140) @@L@@
• Several scanners on a role: BLOCK wins if any scanner blocks, otherwise the decision with the highest score; reasons are joined with "; " (llamafirewall.py@172c1074:142-167) @@L@@
• Async path: scan_async returns the first BLOCK or HUMAN_IN_THE_LOOP_REQUIRED result, else ALLOW with reason "default" and score 0.0 (llamafirewall.py@172c1074:174-187) @@L@@
• Docs sample output shows reason='default' and score=0.0 for a benign input, and reason='prompt_guard' and score=0.95 for a blocked one (how-to-use-llamafirewall.md@172c1074:86-89) @@L@@
• Code behaviour differs from that sample: for a single scanner the reason is the scanner's own text (for example "No prompt injection detected") and the benign score is the model probability (llamafirewall.py@172c1074:134-140) @@L@@
• Model numbers behind the scanner: AUC .998, recall at 1% FPR 97.5% and 92.4 ms on an A100 for the 86M model, on a private benchmark (Llama-Prompt-Guard-2/86M/MODEL_CARD.md@172c1074:74) @@L@@
• Paper, AgentDojo with Prompt Guard 2 86M on user and tool messages: attack success rate 17.6% to 7.5%, utility 47.7% to 47.0% (arXiv 2505.03574 section 4.3) @@D@@
• Scanner or framework latency and throughput (checked the README, which says only "Real-Time", the docs pages and the paper; no figure is given for this scanner) @@N@@
• The scanner reports the model probability directly with no calibration or confidence interval (premise: promptguard_utils.py takes the softmax value as the score) @@I@@
### R6
Summary: **A Message with role and text content, plus gated model access.** Weights are downloaded from Hugging Face on first use, with an interactive login if no token exists. Python 3.10 or later is needed, and text over 512 tokens is truncated. @@D@@
Detail:
• Input object: Message(role, content) with helper classes UserMessage, SystemMessage, AssistantMessage, ToolMessage and MemoryMessage (llamafirewall_data_types.py@172c1074:50-92) @@L@@
• Only content is scanned and truncated at 512 tokens, so any text after the window is not scored (premise: promptguard_utils.py line 113 truncates; no splitting code was found in LlamaFirewall/src) @@I@@
• The model card advises splitting long inputs into segments; the scanner does not do this (Llama-Prompt-Guard-2/86M/MODEL_CARD.md@172c1074:24) @@L@@
• Access: the Hugging Face repo is gated, and without a token the code calls login() which prompts interactively (promptguard_utils.py@172c1074:57-61) @@L@@
• Interactive login may block a headless test run unless a token is already set (premise: promptguard_utils.py line 61) @@I@@
• Setup helper: "llamafirewall configure" checks local models, offers to download them and checks API keys (LlamaFirewall/README.md@172c1074:147-154) @@L@@
• The configure helper's default model is "meta-llama/Llama-Prompt-Guard-2-86M" (LlamaFirewall/src/llamafirewall/cli/configure.py@172c1074:21) @@L@@
• Parallel use: set "export TOKENIZERS_PARALLELISM=true" (LlamaFirewall/README.md@172c1074:171) @@L@@
• Prerequisite text says "Access to HuggingFace Meta's Llama 3.1 models & evals", which does not name the Llama 4 licence that the model files carry (LlamaFirewall/README.md@172c1074:55) @@L@@
• The synchronous scan call uses asyncio.run, which fails inside a running event loop; use scan_async there (premise: llamafirewall.py line 122 and Python behaviour) @@I@@
• No scanner timeout or size limit is set in code beyond the 512-token truncation (premise: reading prompt_guard_scanner.py and promptguard_utils.py) @@I@@
### R7
Summary: **Minimum setup:** install llamafirewall, accept the Llama 4 licence on Hugging Face so the 86M model can download, configure a USER role with the PromptGuard scanner, and scan labelled strings. Set the threshold explicitly and test other roles for retrieved text and tool output. @@I@@
Detail:
• **Minimum setup:** pip install llamafirewall on Python 3.10 or later, get approved access to the 86M model on Hugging Face, run llamafirewall configure or log in so the first scan can download it, then call scan on UserMessage objects (premise: README and promptguard_utils.py) @@I@@
• Table 3 input type: prompts, plus retrieved passages and tool outputs wrapped as TOOL or MEMORY messages, each with a benign or attack label (premise: roles in llamafirewall_data_types.py) @@I@@
• Record the score for every case, not only the decision, so that thresholds from 0.5 to 0.99 can be compared with the 0.9 default (premise: the score field in ScanResult) @@I@@
• Compare scan on USER with the model run directly (column PL1) to confirm the wrapper adds no differences beyond whitespace cleaning and truncation (premise: preprocessing code) @@I@@
• Time the first scan separately from later scans, because model loading may happen on every call (premise: create_scanner inside scan) @@I@@
• No Together key is needed for this scanner; the key is for AlignmentCheck and the LLM-prompt scanners (premise: README setup text and scanner files) @@I@@
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
• Whether the docs sample output (reason 'prompt_guard', benign score 0.0) reflects an earlier code version (checked the pinned how-to page and code; they differ)
• Whether the README's Llama 3.1 access instruction is stale for the Llama 4 licensed model
• How a hosted or air-gapped deployment obtains the gated weights without an interactive login (checked README and code; not described)
### R9
Summary: LlamaFirewall source files, README and docs pages in the PurpleLlama repo, the PyPI index, the Prompt Guard 2 model card, and the LlamaFirewall paper.
Detail:
• @@B@@LlamaFirewall/src/llamafirewall/scanners/prompt_guard_scanner.py
• @@B@@LlamaFirewall/src/llamafirewall/scanners/promptguard_utils.py
• @@B@@LlamaFirewall/src/llamafirewall/llamafirewall.py
• @@B@@LlamaFirewall/src/llamafirewall/llamafirewall_data_types.py
• @@B@@LlamaFirewall/src/llamafirewall/config.py
• @@B@@LlamaFirewall/src/llamafirewall/cli/configure.py
• @@B@@LlamaFirewall/pyproject.toml
• @@B@@LlamaFirewall/LICENSE
• @@B@@LlamaFirewall/README.md
• @@B@@LlamaFirewall/website/docs/documentation/scanners/prompt-guard-2.md
• @@B@@LlamaFirewall/website/docs/documentation/getting-started/how-to-use-llamafirewall.md
• @@B@@LlamaFirewall/website/docs/documentation/getting-started/adding-custom-use-case.md
• @@B@@LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md
• @@B@@Llama-Prompt-Guard-2/86M/MODEL_CARD.md
• https://pypi.org/simple/llamafirewall/
• https://arxiv.org/html/2505.03574
