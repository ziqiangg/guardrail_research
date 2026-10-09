## Column PL4: LlamaFirewall: Output-level insecure-code detection (CodeShield scanner)
### R1
Summary: **Output-level insecure-code scanning in LlamaFirewall.** The CodeShield scanner runs the Code Shield static-analysis engine over a message's text and blocks it, with score 1.0, when any insecure-code issue is found. By default it runs on assistant and tool messages. @@D@@
Detail:
• Meta describes CodeShield in LlamaFirewall as "a static analysis engine that examines LLM-generated code for security issues in real time" (LlamaFirewall/README.md@172c1074:45) @@L@@
• Docs page: "CodeShield is an advanced online static-analysis engine designed to enhance the security of LLM-generated code." (LlamaFirewall/website/docs/documentation/scanners/code-shield.md@172c1074:4) @@L@@
• Code: class CodeShieldScanner, scanner name "Code Shield Scanner", constructed with a threshold of 1.0 (code_shield_scanner.py@172c1074:32-38) @@L@@
• Decision: any issue returns BLOCK with score 1.0; no issue returns ALLOW with score 0.0 (code_shield_scanner.py@172c1074:67-92) @@L@@
• Wrapper versus engine: the scanner adds the role configuration, a block-or-allow decision and a formatted reason; the rules, languages and analysers are the Code Shield engine in column PL6 (premise: the scanner calls insecure_code_detector.analyze) @@I@@
• Selected by scanner type CODE_SHIELD (llamafirewall_data_types.py@172c1074:14) @@L@@
• Previously released "as part of the Llama 3 launch, CodeShield is now integrated into the LlamaFirewall framework" (code-shield.md@172c1074:4) @@L@@
### R2
Summary: **Insecure coding patterns in LLM-generated code.** The engine flags risky code practices with CWE identifiers across eight languages by default, though Meta also says seven and claims over 50 CWEs. It is not a taint-flow analyser. @@D@@
Detail:
• Risks: "Insecure Coding Practices" and "Malicious Code via Prompt Injection" as part of layered defence (code-shield.md@172c1074:17-18) @@L@@
• Coverage: "offering coverage for over 50 Common Weakness Enumerations (CWEs)" (code-shield.md@172c1074:4) @@L@@
• Languages, source A (8): the LlamaFirewall README says "8 programming languages" (LlamaFirewall/README.md@172c1074:45) @@L@@
• Languages, source A2 (8): the LlamaFirewall docs say "eight programming languages" (code-shield.md@172c1074:4) @@L@@
• Languages, source B (code): the scanner scans the list from get_supported_languages(), which returns eight: C, C++, C#, Java, JavaScript, PHP, Python, Rust (languages.py@172c1074:72-83) @@L@@
• Languages, source C (7): the Code Shield README says "across 7 programming languages, covering more than 50+ CWEs" (CodeShield/README.md@172c1074:11) @@L@@
• Languages, source D (7): the protections page says "7 programming languages" (dev.meta.ai llama-protections, read 2026-10-09) @@D@@
• The paper states both: "8 programming languages" in its summary and "seven programming languages" in section 4.4 (arXiv 2505.03574 sections 1 and 4.4) @@D@@
• Enum members beyond the eight: the Language enum has 16 members including Hack, Kotlin, Objective-C, Objective-C++, Ruby, Swift, XML and LANGUAGE_AGNOSTIC, none of them in the default scan (languages.py@172c1074:14-30) @@L@@
• The engine's README names the eight languages: C, C++, C#, Java, Javascript, Python, PHP, Rust (CodeShield/insecure_code_detector/README.md@172c1074:22-31) @@L@@
• Not a vulnerability finder: ICD "is not designed to serve as a comprehensive static analysis tool for identifying vulnerabilities" (CodeShield/insecure_code_detector/README.md@172c1074:16) @@L@@
• Limit: "doesn't work well for vulnerability categories which require taint flow analysis for high accuracy" (CodeShield/insecure_code_detector/README.md@172c1074:35) @@L@@
• Limit: ICD "operates on a 'best guess' basis" and "can lead to false positives" (CodeShield/insecure_code_detector/README.md@172c1074:36) @@L@@
• Paper limit: CodeShield "is not comprehensive and may miss nuanced or context-dependent vulnerabilities" (arXiv 2505.03574 section 4.4) @@D@@
• Rules enabled for the CODESHIELD use case: config.yaml lists 38 regex rule ids (8 of them language-agnostic) and 77 Semgrep rule ids for the eight default languages; Rust lists none of its own (CodeShield/insecure_code_detector/rules/config.yaml@172c1074:1-407) @@L@@
• Distinct CWE ids in the rules enabled for this scanner use case come to about 47 across the eight languages by a count of the rule files, below the "over 50" claim; the larger CyberSecEval rule set gives about 63 (premise: a count of cwe_id values in the regex YAML files and generated Semgrep JSON files) @@I@@
### R3
Summary: **Assistant and tool text, as plain strings.** The scanner reads only the message content and scans it as code in all default languages. It is attached to the ASSISTANT and TOOL roles by default and by the coding-assistant use case. Tool-call arguments are not read. @@D@@
Detail:
• Reads one field: "text = message.content" (code_shield_scanner.py@172c1074:56) @@L@@
• Runs the engine over every language from get_supported_languages() in parallel with asyncio.gather (code_shield_scanner.py@172c1074:57-59) @@L@@
• No-config default: ASSISTANT scans CODE_SHIELD and TOOL scans CODE_SHIELD and PROMPT_GUARD (llamafirewall.py@172c1074:90-96) @@L@@
• CODING_ASSISTANT use case: CODE_SHIELD for ASSISTANT and TOOL (config.py@172c1074:26-29) @@L@@
• Docs: "setting a ScannerType.CODE_SHIELD for both the ASSISTANT and TOOL roles" (adding-custom-use-case.md@172c1074:26-27) @@L@@
• Direction (R002): the same scanner can be attached to any role, so it can also scan USER or MEMORY text; Meta documents it for LLM output (premise: Configuration maps any Role to scanner types) @@I@@
• Docs example: a coding agent's code diff is statically analysed and "CodeShield statically analyzes the code diff" and, if SQL injection risk is detected, "the patch is rejected" (workflow-and-detection-components.md@172c1074:68) @@L@@
• Messages are scanned whole, including prose around code; the engine does not extract fenced code blocks (premise: the scanner passes the entire text to insecure_code_detector.analyze) @@I@@
• Code context is not supplied: the scanner passes code_before, code_after and path as None (code_shield_scanner.py@172c1074:43-50) @@L@@
• The message type has an optional tool_calls field that this scanner does not read, so code inside function-call arguments is not scanned (premise: only message.content is read) @@I@@
• Trace and previous messages are ignored by this scanner (code_shield_scanner.py@172c1074:53-56) @@L@@
### R4
Summary: **Regex and Semgrep rules run through the installed codeshield package.** The scanner imports the Insecure Code Detector from the codeshield package and falls back to the repo copy. It needs the Semgrep dependency but no model, key or network access. @@D@@
Detail:
• Import order: first "codeshield.insecure_code_detector" (the PyPI package), else "CodeShield.insecure_code_detector" from the repo (code_shield_scanner.py@172c1074:9-19) @@L@@
• So an installed codeshield package, not the repo folder, normally supplies the rules and the language list (premise: try/except ImportError order) @@I@@
• Docs: CodeShield "supports both Semgrep and regex-based rules, providing syntax-aware pattern matching" (code-shield.md@172c1074:21) @@L@@
• llamafirewall 1.0.3 in the repo requires "codeshield>=1.0.1" (LlamaFirewall/pyproject.toml@172c1074:7,15) @@L@@
• PyPI simple index lists codeshield up to 1.0.1 and llamafirewall up to 1.0.3 (PyPI simple index, observed 2026-10-09) @@D@@
• The repo CodeShield folder declares version "0.0.1", so whether PyPI codeshield 1.0.1 equals the code at the pin is unconfirmed (CodeShield/pyproject.toml@172c1074:3) @@L@@
• Equality of PyPI codeshield 1.0.1 with the repo code at the pin (checked the PyPI index and the repo; the sdist contents were not read) @@T@@
• Use case: the scanner calls the engine with UseCase.CODESHIELD, the fast mode (code_shield_scanner.py@172c1074:49) @@L@@
• In that mode regex runs first and returns on any match, and Semgrep runs only if a quick regex pre-scan recommends it (insecure_code_detector.py@172c1074:126-137) @@L@@
• Two-tier design per Meta: "The first tier utilizes lightweight pattern matching and static analysis, completing scans in under 100 milliseconds" (code-shield.md@172c1074:11) @@L@@
• Semgrep is invoked as a subprocess of a symlinked "osemgrep" binary found in the semgrep package (oss.py@172c1074:28-76) @@L@@
• The llamafirewall package requires torch, transformers, huggingface_hub, openai and others (LlamaFirewall/pyproject.toml@172c1074:14-23) @@L@@
• Licence: LlamaFirewall is MIT licensed (LlamaFirewall/LICENSE@172c1074:1) @@L@@
• Licence: the CodeShield folder is MIT licensed (CodeShield/LICENSE@172c1074:1) @@L@@
• Release notes for codeshield and llamafirewall (checked the repo at the pin: no tags and no CHANGELOG file) @@N@@
• No backing model: the scanner and engine files import no machine-learning library and run regex and Semgrep rules (premise: code_shield_scanner.py and insecure_code_detector.py imports) @@I@@
### R5
Summary: **Block with score 1.0, or allow with 0.0.** The reason lists each issue with its description, CWE, line and severity. The scanner never returns warn or human review. Meta quotes four different latency figures, and precision 96% with recall 79% from a manual check. @@D@@
Detail:
• Result: ScanResult with decision, reason, score and status; this scanner returns only ALLOW or BLOCK, always with status SUCCESS (code_shield_scanner.py@172c1074:67-92) @@L@@
• Allow reason "No unsafe function call detected" with score 0.0 (code_shield_scanner.py@172c1074:33,67-73) @@L@@
• Block reason: "{n} unsafe function call detected:" followed by one line per issue with description, "(CWE-id)", "at line n" and "[Severity: s]" (code_shield_scanner.py@172c1074:75-91) @@L@@
• The block threshold of 1.0 is passed to the base class but the scan code never compares against it (premise: code_shield_scanner.py contains no use of block_threshold) @@I@@
• The engine's own block, warn or ignore treatment is not used, so low-severity findings also block (premise: the scanner reads the issue list only) @@I@@
• Several scanners on a role: BLOCK wins if any scanner blocks (llamafirewall.py@172c1074:142-167) @@L@@
• Precision and recall: "CodeShield achieved a precision of 96% and a recall of 79%" on "50 LLM-generated code completions per language across several languages", labelled manually in CyberSecEval 3 (arXiv 2505.03574 section 4.4) @@D@@
• Per-language precision and recall: the paper shows a figure; the values were not read as text (arXiv 2505.03574 section 4.4) @@T@@
• Latency, statement 1 (Code Shield README): "approximately 99% of cases, requests are processed within a swift 70ms window", p90 450 ms for the rest (CodeShield/README.md@172c1074:27) @@L@@
• Latency, statement 2 (LlamaFirewall docs): first tier "under 100 milliseconds", second layer "around 300 milliseconds", about 90% resolved by the first layer under 70 ms (code-shield.md@172c1074:11-13) @@L@@
• Latency, statement 3 (paper): first tier "approximately 60 milliseconds", second layer around 300 ms, "approximately 90% of inputs are fully resolved by the first layer" (arXiv 2505.03574 section 4.4) @@D@@
• Latency, statement 4 (protections page): "an average latency of 200ms" (dev.meta.ai llama-protections, read 2026-10-09) @@D@@
• The four statements differ and each comes from Meta's internal production experience; no latency or timeout appears in the scanner or engine code (premise: grep of CodeShield and LlamaFirewall/src for latency and timeout) @@I@@
• Scanner latency measured through LlamaFirewall (checked the README, docs and paper; none gives one) @@N@@
### R6
Summary: **A string of code, with the codeshield package and Semgrep installed.** The scanner needs no key or model. It scans eight languages by default and writes each scan to a temporary file. No size limit or timeout is set in code. @@D@@
Detail:
• Input: Message content text; all eight default languages are tried on every message (code_shield_scanner.py@172c1074:56-59) @@L@@
• Python 3.10 or later for LlamaFirewall (LlamaFirewall/README.md@172c1074:53) @@L@@
• The codeshield package declares "requires-python = \">=3.8\"" (CodeShield/pyproject.toml@172c1074:10) @@L@@
• codeshield dependencies: "semgrep>1.68" and "pyyaml" (CodeShield/pyproject.toml@172c1074:15) @@L@@
• Importing the engine needs the Semgrep core binary: it raises "Failed to find semgrep-core in PATH or in the semgrep package" if missing (oss.py@172c1074:42-44) @@L@@
• Each engine call writes the text to a temporary file with the language's file extension and deletes it afterwards (insecure_code_detector.py@172c1074:98-107,149-153) @@L@@
• On the early-return paths in fast mode the temporary file may not be deleted (premise: the returns at insecure_code_detector.py lines 129 and 137 come before the os.remove at line 151) @@I@@
• Semgrep jobs are capped at 16 workers (oss.py@172c1074:61-62) @@L@@
• Rules can be edited: regex rules live in rules/regex YAML files and Semgrep rules in rules/semgrep, enabled per use case in config.yaml (CodeShield/insecure_code_detector/rules/README.md@172c1074:3-8) @@L@@
• Comment filtering: a regex match on a line that starts with "#", "//" or "/*", or ends with "*/", is dropped (insecure_code_detector.py@172c1074:158-166,179-180) @@L@@
• Maximum input size, timeout and concurrency limits (checked the READMEs, docs pages and code; none is set) @@N@@
• No API key, Hugging Face login or network call is used by this scanner (premise: code_shield_scanner.py imports only the engine) @@I@@
### R7
Summary: **Minimum setup:** pip install llamafirewall, which pulls in codeshield and Semgrep, attach the Code Shield scanner type to the assistant role, and scan labelled snippets in the eight default languages. No key, model or gated access is needed. Check the language list and fast-mode behaviour on the installed codeshield version. @@I@@
Detail:
• **Minimum setup:** pip install llamafirewall (Python 3.10 or later), configure LlamaFirewall with Role.ASSISTANT mapped to ScannerType.CODE_SHIELD, then call scan on AssistantMessage objects holding code snippets (premise: README and the demo script) @@I@@
• Table 3 input type: model-output text containing code, labelled insecure or clean, with the CWE or rule it should trigger (premise: block reason carries CWE ids) @@I@@
• Cover every default language with a case from each rule family; include Rust and PHP cases, whose rule coverage differs from the others (premise: the engine's analyser map, see column PL6) @@I@@
• Include non-code prose, fenced code inside markdown, code inside a tool message and an insecure pattern only in a comment, to check the comment filter (premise: engine code) @@I@@
• Record the installed codeshield version and compare with the repo code because the scanner imports the installed package first (premise: import order) @@I@@
• Expect the first scans to be slower where Semgrep runs; time regex-only and Semgrep paths separately (premise: two-tier design) @@I@@
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
• @@B@@LlamaFirewall/src/llamafirewall/scanners/code_shield_scanner.py
• @@B@@LlamaFirewall/src/llamafirewall/llamafirewall.py
• @@B@@LlamaFirewall/src/llamafirewall/llamafirewall_data_types.py
• @@B@@LlamaFirewall/src/llamafirewall/config.py
• @@B@@LlamaFirewall/pyproject.toml
• @@B@@LlamaFirewall/LICENSE
• @@B@@LlamaFirewall/README.md
• @@B@@LlamaFirewall/website/docs/documentation/scanners/code-shield.md
• @@B@@LlamaFirewall/website/docs/documentation/getting-started/adding-custom-use-case.md
• @@B@@LlamaFirewall/website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md
• @@B@@CodeShield/README.md
• @@B@@CodeShield/pyproject.toml
• @@B@@CodeShield/LICENSE
• @@B@@CodeShield/insecure_code_detector/README.md
• @@B@@CodeShield/insecure_code_detector/insecure_code_detector.py
• @@B@@CodeShield/insecure_code_detector/languages.py
• @@B@@CodeShield/insecure_code_detector/oss.py
• @@B@@CodeShield/insecure_code_detector/rules/README.md
• @@B@@CodeShield/insecure_code_detector/rules/config.yaml
• https://pypi.org/simple/codeshield/
• https://pypi.org/simple/llamafirewall/
• https://dev.meta.ai/llama/llama-protections
• https://arxiv.org/html/2505.03574
