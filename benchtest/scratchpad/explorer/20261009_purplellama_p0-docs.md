# Purple Llama P0 note, DOCS half (20261009)

Explorer: gr-explorer (docs, papers, licences). The code and models half is separate (`_p0-code.md`). Quotes were taken with `fetch_text.py` (verbatim) on 2026-10-09. Raw fetches were kept outside the repo.

## 1. Header
- Product: Meta Purple Llama umbrella (Prompt Guard 2, LlamaFirewall, Code Shield, CyberSecEval; Llama Guard cross-ref only per R004).
- Canonical repo: `meta-llama/PurpleLlama` (github.com/meta-llama/PurpleLlama returned HTTP 200, no redirect observed). The code explorer owns the release-tag pin.
- Docs read at ref `172c1074069eb88ec834124272c1b1c4f8893445`. This is the ref the GitHub MCP resolved when no ref was given; the baseline Llama Guard research pinned the same SHA. Whether it is the latest tag or HEAD is for the code half to confirm.
- Docs-site pin check: five pages of the LlamaFirewall docs site (about-llamafirewall, how-to-use-llamafirewall, scanners/code-shield, scanners/prompt-guard-2, scanners/alignment-check) match the files under `LlamaFirewall/website/docs/documentation/` at that SHA. The site is a Docusaurus build of that folder, so those pages may carry `[Documented: repo meta-llama/PurpleLlama@172c1074]`.
- Official domains used: `www.llama.com` (redirects to `dev.meta.ai/llama/...`), `dev.meta.ai`, `meta-llama.github.io/PurpleLlama/` (docs sites for LlamaFirewall and CyberSecEval), `github.com/meta-llama`, `raw.githubusercontent.com/meta-llama/PurpleLlama`, `arxiv.org` (Meta-authored papers), `ai.meta.com/research`, `huggingface.co/meta-llama` (gated; the gate page text is readable).
- Ownership and redirect findings: `https://www.llama.com/llama-protections/` redirects to `https://dev.meta.ai/llama/llama-protections`, and `https://www.llama.com/docs/model-cards-and-prompt-formats/prompt-guard/` redirects to `https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard` (HTTP 200 after redirect, observed 2026-10-09). Same owner (Meta); no transfer to record. `https://meta-llama.github.io/PurpleLlama/` itself only says "Redirecting to CyberSecEval...".
- Names as Meta writes them: "Llama Prompt Guard 2" (docs, card), "PromptGuard 2" (LlamaFirewall docs, paper), "LlamaFirewall", "CodeShield" (repo, LlamaFirewall docs), "Code Shield" (llama.com, root README), "AlignmentCheck", "CyberSecEval" (repo) and "Cybersec Eval" (llama.com).

## 2. Function list (proposed)
Direction follows R002. A library that only receives a string is undifferentiated. LlamaFirewall does expose per-role configuration (USER, SYSTEM, ASSISTANT, TOOL), which is the product's own surface for direction (see Q02).

Prefix choice (Q01, CP1):
- Option A: one prefix `Purple Llama:` with the tool named in the function part.
- Option B: per-tool prefixes `Prompt Guard 2:`, `LlamaFirewall:`, `Code Shield:`.
- Both headers are given below. Recommendation: B, because the header rule says the prefix is the product's own name as its owner writes it (NeMo Guardrails, Llama Guard, GovTech Sentinel). A keeps all six columns under the R004 umbrella name.

| ID | Header, option A | Header, option B | One line | Direction | Evidence |
|---|---|---|---|---|---|
| PL1 | Purple Llama: Input-level prompt-attack detection (Prompt Guard 2) | Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection) | BERT-style classifier labels a string benign or malicious for jailbreak or injection intent. 86M multilingual and 22M variants. | Input (a string: user prompts and untrusted data) | E1-E5, E21, E22 |
| PL2 | Purple Llama: Input-level prompt-attack scanning in LlamaFirewall (PromptGuard scanner) | LlamaFirewall: Input-level prompt-attack scanning (PromptGuard scanner) | The PromptGuard 2 model wrapped as a LlamaFirewall scanner, configured per role, returning allow or block with a score. Same model as PL1; the column differs in orchestration, roles and result type. | Input (role-configured) | E6, E8-E10, E22 |
| PL3 | Purple Llama: Agent goal-hijacking detection over the execution trace (AlignmentCheck) | LlamaFirewall: Agent goal-hijacking detection over the execution trace (AlignmentCheck) | Few-shot LLM auditor reads the agent trace and compares actions with the user goal. Needs an external LLM (docs: Together API key). Experimental per the paper. | Trace of agent reasoning and actions (Role.ASSISTANT); neither pure input nor output (Q02) | E6, E9, E12, E13, E23 |
| PL4 | Purple Llama: Output-level insecure-code detection in LlamaFirewall (CodeShield scanner) | LlamaFirewall: Output-level insecure-code detection (CodeShield scanner) | CodeShield engine called as a scanner on assistant and tool messages (CODING_ASSISTANT use case). | Output (Role.ASSISTANT, Role.TOOL) | E6, E11, E14, E15, E16 |
| PL5 | Purple Llama: Configurable regex and LLM-prompt custom scanning in LlamaFirewall | LlamaFirewall: Configurable regex and custom scanning | User-written regex scanners and "simple LLM prompts", plus a BaseScanner subclass route. | Role-configured (inputs, plans or outputs) | E7, E17, E18, E36 (thin; Q03) |
| PL6 | Purple Llama: Output-level insecure-code filtering (Code Shield) | Code Shield: Output-level insecure-code filtering | Standalone inference-time filter over LLM-generated code using the Insecure Code Detector (Semgrep and regex rules). Same engine as PL4. | Output (code text) | E15, E19, E20 (code half owns the API) |

Not proposed as columns (inventory only): Prompt Guard 1 (`Prompt-Guard`, legacy per R004); CyberSecEval (eval sheet); Llama Guard 3/4 (cross-ref to V-Z and 3d; no PL IDs). Llama Guard is not re-researched.

R-row coverage (docs half): R1 E1, E3, E6, E14. R2 E2, E5, E6, E12, E14. R3 E3, E5, E10, E11. R4 E4, E5, E13, E15. R5 E8, E21-E24. R6 E4 (512 tokens), E8, E18. R7 E7, E9, E18, E33 (Python 3.10, pip, HF login, Together key). R8 section 5. R9 section 7. Gaps per row are in section 5; PL5 has no dedicated documentation, PL3 has no threshold, PL6 has a languages conflict.

## 3. Proposed inventory blocks (sheet 3x "3x. Purple Llama Inventory", per R003)
Short names for source cells: DOCS-LF = LlamaFirewall docs site, PL = repo, PG2C = PG2 model card.
- (a) Component and variant catalogue. Columns: Component ID | Family | Type (model, scanner, library, benchmark) | Status (Available, Legacy, Experimental) | Input/Output | Backing model or engine | Licence | Covered by Table 3 column | Source URL. About 14 rows: Prompt Guard 1 86M (legacy marker), Llama Prompt Guard 2 86M, 22M, LlamaFirewall package, scanners PROMPT_GUARD, AGENT_ALIGNMENT, CODE_SHIELD, regex, custom, CodeShield standalone, Insecure Code Detector, CyberSecEval 4 (needs an eval-sheet marker), Llama Guard 3/4 cross-ref rows (covered by the LG columns).
- (b) Role-to-scanner mapping and predefined use cases. Columns: Use case | Role | Scanner type | What is checked | Source URL. About 6 rows (CHAT_BOT: USER and SYSTEM; CODING_ASSISTANT: ASSISTANT and TOOL; the README examples USER with PROMPT_GUARD, ASSISTANT with AGENT_ALIGNMENT). Note conflict C3.
- (c) Threat-to-scanner coverage (from the LlamaFirewall workflow page). Columns: Security risk | Example | Scanners claimed | Source URL. 5 rows. A code-set validator would need risk codes, suggest R1 to R5.
- (d) Integration and access paths. Columns: Path | How | Needs | Source URL. About 8 rows: HF Transformers pipeline, cookbook inference utilities, `pip install llamafirewall` and `llamafirewall configure`, CodeShield notebook, LlamaFirewall tutorials site, CyberSecEval CLI, Llama reference system (named on llama.com; code half to confirm).
- (e) Licences, gating and acceptable use. Columns: Component | Licence as stated | Gating or AUP | Conflict note | Source URL. About 8 rows (PG1 Llama 3.2; PG2 Llama 4 plus AUP; LlamaFirewall MIT; CodeShield MIT; CyberSecEval MIT; Llama Guard cross-ref).
- (f, optional) Published metrics catalogue. Columns: Component | Metric | Value | Benchmark | Source URL. About 10 rows (PG2 AUC, recall and APR; AlignmentCheck recall and FPR; AgentDojo ASR; CodeShield precision, recall and latency).

## 3b. Proposed evaluation-tooling sheet for CyberSecEval (R003)
The builder owner must set SECTION_ORDER; the default parser order is Overview, Tools, Datasets, Published results, Red-teaming, Engine coverage, Reuse for the test bench, Open questions.
- Overview: CyberSecEval 4 as the current suite; v1 to v3 history and papers (E25-E28, E31). One Summary plus about 5 bullets.
- Tools: one row per benchmark family in the repo README (E29): MITRE and MITRE FRR; Instruct and Autocomplete secure code generation; Textual and Visual prompt injection; Code interpreter abuse; Vulnerability exploitation; Spear phishing; Autonomous offensive cyber operations; AutoPatchBench; CyberSOCEval (Malware analysis, Threat intelligence reasoning). About 11 rows. "Evaluates (Table 3 columns)": prompt-injection tests to PL1 and PL2 as a target, secure-code tests to PL4 and PL6 (E24 shows CodeShield was evaluated in CyberSecEval 3), MITRE and FRR to Llama Guard columns by cross-ref only. The sources do not say these suites evaluate guardrails directly, so the mapping is `[Inferred]`.
- Datasets: `CybersecurityBenchmarks/datasets`; threat-intelligence reports are downloaded separately (README heading "Download Threat Intelligence Report Data").
- Published results: repo README sections MITRE, Instruct and Autocomplete, Prompt Injection, MITRE FRR, Code Interpreter Abuse, Vulnerability Exploitation, Spear Phishing, AutoPatch. Not copied at P0.
- Red-teaming: offensive-capability suites (vulnerability exploitation, spear phishing, autonomous cyber operations). They test models, not guardrails.
- Engine coverage: providers OPENAI, GOOGLE, ANTHROPIC, LLAMA, TOGETHER, self-hosted models, custom base URL (E30).
- Reuse for the test bench: which parts can supply guardrail test inputs (prompt-injection datasets for PL1 and PL2, insecure-code tests for PL4 and PL6) and which are model-capability suites that cannot.
- Open questions: CyberSecEval 4 paper not located (gap 7); the docs site landing page text at `meta-llama.github.io/PurpleLlama/CyberSecEval/` still describes Prompt Guard.

## 4. Sources table
Quotes are verbatim, under 40 words, whitespace normalised. "@172c1074" means `[Documented: repo meta-llama/PurpleLlama@172c1074]`.

| ID | URL | Verbatim quote | Label | Rows |
|---|---|---|---|---|
| E1 | https://dev.meta.ai/llama/llama-protections (from https://www.llama.com/llama-protections/, HTTP 200 after redirect) | "Prompt Guard is a powerful tool for protecting LLM powered applications from malicious prompts to ensure their security and integrity." | [Documented] | PL1 R1 |
| E2 | https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard | "Both models detect prompt injection and jailbreaking attacks, and are trained on a large corpus of known vulnerabilities." | [Documented] | PL1 R1, R2 |
| E3 | https://dev.meta.ai/llama/llama-protections | "LlamaFirewall can orchestrate across guard models and work with our suite of protection tools to detect and prevent risks such as prompt injection, insecure code and risky tool interactions." | [Documented] | PL2-PL5 R1, R2 |
| E4 | https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard | "Llama Prompt Guard 2 are BERT models that output only labels" ; "The PromptGuard model has a context window of 512 tokens." | [Documented] | PL1 R4, R6 |
| E5 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/86M/MODEL_CARD.md | "Both Prompt Guard 2 models have been evaluated for attack detection in English, French, German, Hindi, Italian, Portuguese, Spanish, and Thai." ; "classify prompts as 'malicious' if the prompt explicitly attempts to override prior instructions" | @172c1074 | PL1 R2, R3 |
| E6 | https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/about-llamafirewall | "Combines multiple scanners—PromptGuard 2, AlignmentCheck, CodeShield, and customizable regex filters—for comprehensive protection across the agent’s lifecycle." | @172c1074 (page matches about-llamafirewall.md) | PL2-PL5 R1, R2 |
| E7 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/architecture.md | "A configurable scanning layer for applying regular expressions or simple LLM prompts to detect known patterns, keywords, or behaviors across inputs, plans, or outputs." | @172c1074 | PL5 R1, R3 |
| E8 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/getting-started/how-to-use-llamafirewall.md | "The result of each scan is a ScanResult object including information about the decision of the scan, the reason for the decision, and a trustworthiness score for that decision." | @172c1074 | PL2-PL5 R5 |
| E9 | same file as E8 | "If you plan to use the alignment check scanner, you will need to set up the Together API key in your environment" ; "Python 3.10 or later" | @172c1074 | PL2, PL3 R7 |
| E10 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/getting-started/adding-custom-use-case.md | "The CHAT_BOT use case which focuses in protecting against prompt injection attacks. This is achieved by scanning for PROMPT_INJECTION attacks for both the USER and SYSTEM roles" | @172c1074 | PL2 R3 |
| E11 | same file as E10 | "the CODING_ASSISTANT use case is designed for instances where there is a needs to protect against malicious code attacks" ; "setting a ScannerType.CODE_SHIELD for both the ASSISTANT and TOOL roles" | @172c1074 | PL4 R3 |
| E12 | https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/scanners/alignment-check | "AlignmentCheck is a pioneering, open-source guardrail that utilizes few-shot prompting to audit an agent's reasoning in real-time, detecting signs of goal hijacking or prompt-injection induced misalignment." | @172c1074 (matches scanners/alignment-check.md) | PL3 R1, R2, R4 |
| E13 | https://arxiv.org/html/2505.03574 (Meta-authored; abstract page https://arxiv.org/abs/2505.03574, submitted 6 May 2025) | "AlignmentCheck, an experimental few-shot prompting-based chain-of-thought auditor that inspects agent reasoning for signs of goal hijacking or prompt-injection induced misalignment." | [Documented] | PL3 R1, R4 |
| E14 | https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/scanners/code-shield | "It supports both Semgrep and regex-based rules, providing syntax-aware pattern matching across eight programming languages." | @172c1074 (matches scanners/code-shield.md) | PL4, PL6 R1, R2, R4 |
| E15 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/README.md | "ICD uses a suite of static analysis tools to perform the analysis across 7 programming languages, covering more than 50+ CWEs." | @172c1074 | PL4, PL6 R2, R4 |
| E16 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md | "CodeShield, a static analysis engine detects insecure coding practices" | @172c1074 | PL4 R2 |
| E17 | same file as E16 | "PromptGuard and Regex scanner detect jailbreak input" | @172c1074 | PL5 R2 |
| E18 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docs/documentation/advanced-usage/adding-custom-scanner.md | "Create a new Python class that inherits from the BaseScanner class" | @172c1074 | PL5 R4, R6, R7 |
| E19 | https://dev.meta.ai/llama/llama-protections | "Code Shield provides support for inference-time filtering of insecure code produced by LLMs. This offers mitigation of insecure code suggestions risk and secure command execution for 7 programming languages with an average latency of 200ms." | [Documented] | PL6 R1, R2, R5 |
| E20 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CodeShield/README.md | "Codeshield is able to fortify any code-producing LLMs by either adding a warning message or completely blocking the response" | @172c1074 | PL6 R3, R5 |
| E21 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/86M/MODEL_CARD.md | "Llama Prompt Guard 2 86M | .998 | 97.5% | .995 | 92.4 ms | 86M | mdeberta-v3" and "Llama Prompt Guard 2 22M | .995 | 88.7% | .942 | 19.3 ms | 22M | deberta-v3-xsmall" (AUC English, Recall at 1% FPR English, AUC multilingual, latency A100 512 tokens, parameters, base model) | @172c1074 | PL1 R5 |
| E22 | same file as E21 | "Llama Prompt Guard 2 86M | 81.2%" and "Llama Prompt Guard 2 22M | 78.4%" (APR at 3% utility reduction, AgentDojo) | @172c1074 | PL1, PL2 R5 |
| E23 | https://arxiv.org/html/2505.03574 | "these models achieved over 80% recall with a false positive rate below 4%" (AlignmentCheck, Llama 4 Maverick and Llama 3.3 70B, Meta goal-hijacking benchmark) ; "reduced the ASR to 7.5%, a 57% drop" (PromptGuard V2 86M, AgentDojo, baseline ASR 17.6%) | [Documented] | PL2, PL3 R5 |
| E24 | https://arxiv.org/html/2505.03574 | "CodeShield achieved a precision of 96% and a recall of 79% in identifying insecure code" | [Documented] | PL4, PL6 R5 |
| E25 | https://arxiv.org/abs/2312.04724 | "Purple Llama CyberSecEval: A Secure Coding Benchmark for Language Models" (submitted 7 Dec 2023) | [Documented] | eval Overview |
| E26 | https://arxiv.org/abs/2404.13161 | "CyberSecEval 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models" (submitted 19 Apr 2024) | [Documented] | eval Overview |
| E27 | https://arxiv.org/abs/2408.01605 | "CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models" (v1 2 Aug 2024, v2 6 Sep 2024) | [Documented] | eval Overview |
| E28 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CybersecurityBenchmarks/README.md | "This repository hosts the implementation of CyberSecEval 4, which builds upon and extends the functionalities of its predecessors" | @172c1074 | eval Overview |
| E29 | same file as E28 | "Prompt Injection Tests: These tests assess an LLM’s susceptibility to “prompt injection attacks”" ; "CyberSOCEval Tests: These tests, created in partnership with Crowdstrike, assess defensive capabilities" | @172c1074 | eval Tools |
| E30 | same file as E28 | "We currently support APIs from OPENAI, GOOGLE, ANTHROPIC, LLAMA and TOGETHER." | @172c1074 | eval Engine coverage |
| E31 | https://dev.meta.ai/llama/llama-protections | "Cybersec Eval 4 expands on its predecessor by augmenting the suite of benchmarks to measure not only the risks, but also the defensive cybersecurity capabilities of AI systems." | [Documented] | eval Overview |
| E32 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/README.md | "evals and benchmarks are licensed under the MIT license while any models use the corresponding Llama Community license" ; table rows "Safeguard | Code Shield | MIT" and "Safeguard | Prompt Guard | Llama 3.2 Community License" | @172c1074 | licence block |
| E33 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/README.md | "The same license as Llama 4 applies: see the LICENSE file, as well as our accompanying Acceptable Use Policy" ; also HF gate page https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M shows "License: llama4" (HTTP 200) | @172c1074 | PL1 R7, licence block |
| E34 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/LICENSE (and .../CodeShield/LICENSE) | "MIT License" ; "Copyright (c) Meta Platforms, Inc. and affiliates." (both files) | @172c1074 | licence block |
| E35 | https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Prompt-Guard-2/86M/USE_POLICY.md | "Llama 4 Acceptable Use Policy" (title line) | @172c1074 | AUP (R019) |
| E36 | https://ai.meta.com/research/publications/llamafirewall-an-open-source-guardrail-system-for-building-secure-ai-agents/ | "customizable scanners that make it possible for any developer who can write a regular expression or an LLM prompt to quickly update an agent’s security guardrails." | [Documented] | PL5 R1 |

## 5. Gaps (checked X, Y: not stated)
1. PL5 regex scanner: checked the docs site navigation (Scanners lists only AlignmentCheck, CodeShield, PromptGuard 2), the architecture, workflow and custom-scanner pages, and the root and LlamaFirewall READMEs. No regex scanner page, config format or pattern syntax. `[Not disclosed]` at docs level; the code half may resolve it. One function or two: Q03.
2. PG2 decision threshold: checked the model card, PG2 README, the dev.meta.ai prompt-guard page and the LlamaFirewall PromptGuard 2 page. The card gives recall at 1% FPR and an operating point at 3% utility loss but no recommended score cut-off. `[Not disclosed]`.
3. AlignmentCheck default model, prompt, timeout and latency: checked the scanner page, how-to and paper. Only the Together key requirement and two example traces (latency_ms 859 and 1490) are given. Default model name: code half.
4. Cost and terms of the Together-hosted LLM behind AlignmentCheck: not stated in Meta sources.
5. PG2 22M HF gate page not read; the 86M gate page was read.
6. LlamaFirewall has no row in the root README licence table; its folder LICENSE says MIT (E34). An omission, not a conflict.
7. CyberSecEval 4 paper: checked the README links (CyberSOCEval on ai.meta.com, CyberSecEval 1 to 3) and the llama.com page. No CyberSecEval 4 arXiv id located. `[To be verified]`. The llama.com page mentions an AutoPatchBench blog post (not fetched).
8. CodeShield named language list: the docs and paper say "eight" without naming them; the CodeShield README says 7. The named list is in `CodeShield/insecure_code_detector` (code half).
9. PG2 on retrieved or tool text: the LlamaFirewall page says "user prompts and untrusted data sources"; the model has no direction flag.
10. No price, rate limit or SLA pages (all components are local libraries or models), except the Together-backed AlignmentCheck.
11. Llama Guard: out of scope, not researched.

## 6. Conflicts between official sources
- C1 CodeShield language count: "7 programming languages" (llama.com E19; CodeShield README E15) versus "eight programming languages" (LlamaFirewall docs E14; paper; LlamaFirewall README "8 programming languages").
- C2 CodeShield latency: llama.com "average latency of 200ms" (E19); CodeShield README "approximately 99% of cases, requests are processed within a swift 70ms window" with "the p90 latency is 450ms" for the rest; LlamaFirewall docs and paper "approximately 90% of inputs are fully resolved by the first layer" at "under 70 milliseconds", second layer "around 300 milliseconds", first tier "under 100 milliseconds" (docs) versus "approximately 60 milliseconds" (paper).
- C3 Scanner enum name: `ScannerType.PROMPT_GUARD` (how-to E8, README) versus `ScannerType.PROMPT_INJECTION` (custom-use-case page E10).
- C4 PG2 scope wording: the card says both models "detect prompt injection and jailbreaking attacks" yet "No injection sub-labels" and only explicit override intent is malicious; LlamaFirewall docs say it detects "direct jailbreak attempts". Give both in R2.
- C5 PG2 licence: PG2 README and HF header say the Llama 4 licence; the root README licence table lists only "Prompt Guard | Llama 3.2 Community License" (no PG2 row) and the root LICENSE file is the Llama 3.2 agreement.
- C6 The LlamaFirewall architecture page links the PromptGuard 2 README as `.../blob/main/Prompt-Guard/README.md` (the PG1 folder); PG2 lives in `Llama-Prompt-Guard-2/`.
- C7 Naming: "Code Sheild" typo on the llama.com page body; "Code Shield" versus "CodeShield" across pages.

## 7. URLs visited (HTTP status)
200 (all read 2026-10-09):
- https://www.llama.com/llama-protections/ (final https://dev.meta.ai/llama/llama-protections)
- https://www.llama.com/docs/model-cards-and-prompt-formats/prompt-guard/ (final dev.meta.ai)
- https://meta-llama.github.io/PurpleLlama/ ; /LlamaFirewall/ ; /CyberSecEval/
- https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/about-llamafirewall ; .../scanners/code-shield ; .../scanners/prompt-guard-2 ; .../scanners/alignment-check ; .../getting-started/how-to-use-llamafirewall
- https://arxiv.org/abs/2505.03574 ; https://arxiv.org/html/2505.03574 ; https://arxiv.org/abs/2312.04724 ; https://arxiv.org/abs/2404.13161 ; https://arxiv.org/abs/2408.01605
- https://ai.meta.com/research/publications/llamafirewall-an-open-source-guardrail-system-for-building-secure-ai-agents/
- https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M (gate page text)
- https://github.com/meta-llama/PurpleLlama
- raw.githubusercontent.com/meta-llama/PurpleLlama/172c1074.../: README.md, LICENSE, LlamaFirewall/README.md, LlamaFirewall/LICENSE, the five LlamaFirewall docs md files, Llama-Prompt-Guard-2/README.md, 86M/MODEL_CARD.md, 22M/MODEL_CARD.md, 86M/USE_POLICY.md, CodeShield/README.md, CodeShield/LICENSE, CybersecurityBenchmarks/README.md

404 (guessed slugs, discarded): .../docs/documentation/overview, getting-started, scanners/prompt-guard, scanners/agent-alignment, scanners/regex, scanners/custom-scanner, concepts/llamafirewall, concepts/scanners, scanners/promptguard-2, scanners/alignmentcheck, llamafirewall-architecture/... and advanced-usage/... (wrong slugs); raw Llama-Prompt-Guard-2/MODEL_CARD.md (cards live under 86M/ and 22M/).

Other: GitHub MCP get_file_contents on `LlamaFirewall/website/docs/documentation` and `.../scanners` (returned ref 172c1074). Three directory listings (architecture, advanced-usage, getting-started folders) were read with a plain GitHub contents listing, not a product API. Fetch count about 45, over the 40 cap because of 404 guesses.

## 8. QUESTIONS (details in q-files)
- Q01 Header prefix, `Purple Llama:` versus per-tool prefixes (CP1).
- Q02 Same model or engine in two wrappers (PL1 and PL2; PL4 and PL6), and the direction label for AlignmentCheck under R002.
- Q03 Regex and custom scanners: one column or two, given thin documentation.
- Q04 AlignmentCheck needs an external hosted LLM: Table 3 column or inventory only (R011), and R019 terms.
- Q05 To the code explorer or a resolver: conflicts C1, C2, C3 (CodeShield languages and latency, scanner enum).
