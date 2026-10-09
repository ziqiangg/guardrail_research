# Purple Llama column drafts, half B (PL3, PL5, PL7), P2 draft

Written 2026-10-09 by gr-drafter. Code facts are read from the shallow clone of meta-llama/PurpleLlama at 172c1074069eb88ec834124272c1b1c4f8893445 (code read, not run). Header prefix is the brief's default option B.

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

## Reviewer notes
1. **Source conflicts logged (each as two labelled bullets):** (a) AlignmentCheck scope, docs "entire execution trace" versus prompt "Only consider the selected action" (PL3 R2); (b) paper mitigation "excluding direct tool outputs" versus code that filters nothing by role (PL3 R3); (c) paper "can be tailored with custom few-shot examples" versus a module-constant prompt (PL3 R4, one bullet with both sides under one Documented label; the merger may split it); (d) paper "truncated to a fixed context window" versus no truncation in code (PL3 R6, second side is Not disclosed by absence); (e) paper 83% versus 84% ASR drop wording (PL3 R5); (f) docs "configurable" regex layer versus fixed pattern constant (PL5 R4); (g) docs `BaseScanner` how-to versus `Scanner` plus registry (PL5 R4, brief C6); (h) tutorial `Reason: default` on allow versus code (PL5 R5).
2. **Not in the brief:** the AlignmentCheck status overwrite to SUCCESS in `LlamaFirewall.scan` (llamafirewall.py:134-140,162-167); the missing-key `ValueError` at scanner creation; the fail-open path on missing trace or user message versus fail-closed on LLM error; PIICheck fail-open on LLM error; `require_full_trace` is set True in AlignmentCheck but read nowhere (search of `src`); `configure.py` accepts `TOGETHER_API_TOKEN` but the scanner reads only `TOGETHER_API_KEY`. The `require_full_trace` finding is not in a bullet; the merger may add it to PL3 R3.
3. **Brief correction (C4):** Hidden ASCII and PII_DETECTION are named in one docs tutorial sentence (prompt-guard-scanner-tutorial.md:30), confirmed; nothing else in docs, README, paper or protections page.
4. **Together facts are third-party (R019):** the terms page (www.together.ai/terms-of-service, sections 3 and 4) and the serverless model table (docs.together.ai/docs/serverless/models, redirected from /docs/inference-models) were read with fetch_text.py on 2026-10-09; no API call was made. The Maverick absence is from a table read as text; it may be a filtered or paginated list, so it is `[To be verified]`. The terms page has no visible effective date in the extracted text.
5. **Hugging Face:** model and dataset metadata were read from the public `huggingface.co/api/...` JSON (status 200); card bodies and dataset files were not read. The Hugging Face MCP connector was unavailable late in the task; fetch_text.py was used instead.
6. **Summaries drawn from mixed labels:** PL3 R5 and PL5 R2 Summaries use only Documented facts (the Inferred or Not disclosed material sits in other bullets). PL7 R2 is `[Inferred]` because its second clause is an inference from the range test.
7. **Docs-site pinning:** passages on the architecture, workflow, alignment-check, regex-tutorial and adding-custom-scanner pages were confirmed in the pinned `.md` files and in the live pages (fetch_text.py). The tutorial `alignment-check-scanner-tutorial` page was read in the pinned file only.
8. **PyPI:** `https://pypi.org/simple/llamafirewall/` lists sdists 1.0.0 to 1.0.3; sdist contents not read. The PL3 R4 bullet "newest sdist" is from this listing order.
9. **Quotes with typographic apostrophes** (paper Appendix C.4) were shortened with an ellipsis to keep the file ASCII.
10. **Reserved PL8:** the CustomCheckScanner and PIICheckScanner bullets sit in PL5 R1, R2, R3, R4, R5, R6, R7 and R8 and can be lifted into a PL8 column by copying; they are not duplicated here.
