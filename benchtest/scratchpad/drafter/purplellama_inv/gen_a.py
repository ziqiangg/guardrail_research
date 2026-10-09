# generator part A: constants + intro + blocks (a) (b) (c)
SHA = "172c1074069eb88ec834124272c1b1c4f8893445"
B = f"https://github.com/meta-llama/PurpleLlama/blob/{SHA}/"
T = f"https://github.com/meta-llama/PurpleLlama/tree/{SHA}/"
R = "[Documented: repo meta-llama/PurpleLlama@172c1074]"
D = "[Documented]"
I = "[Inferred]"
ND = "[Not disclosed]"
TBV = "[To be verified]"
H86 = "[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]"
H22 = "[Documented: repo meta-llama/Llama-Prompt-Guard-2-22M@11614a15]"
HV1 = "[Documented: repo meta-llama/Prompt-Guard-86M@1209add6]"
HF86 = "https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M/tree/a8ded8e697ce7c355e395a0df51f94adb4a2fd27"
HF22 = "https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M/tree/11614a155199674a0a95e6602d6ab0417b790ed0"
HFV1 = "https://huggingface.co/meta-llama/Prompt-Guard-86M/tree/1209add6ca7d9c1d815171b8e5571587fe3e7b03"
H1 = "Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection)"
H2 = "LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner)"
H3 = "LlamaFirewall: Trace-level agent goal-hijacking detection (AlignmentCheck)"
H4 = "LlamaFirewall: Output-level insecure-code detection (CodeShield scanner)"
H5 = "LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner)"
H6 = "Code Shield: Output-level insecure-code detection (LLM-generated code)"
H7 = "LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner)"
LEG = "— (legacy, not in Table 3)"
INV = "— (inventory only, not in Table 3)"


def cov(*h):
    return "; ".join(h)


LFALL = cov(H2, H3, H4, H5, H7)


def u(*p):
    return " ; ".join(B + x for x in p)


def row(cells):
    for c in cells:
        assert "|" not in c and "`" not in c and "**" not in c, c
    return "| " + " | ".join(cells) + " |"


def table(hdr, rows):
    out = [row(hdr), "|" + "---|" * len(hdr)]
    for r in rows:
        assert len(r) == len(hdr), (len(r), len(hdr), r[0])
        out.append(row(r))
    return "\n".join(out)


LF = "LlamaFirewall/src/llamafirewall/"
SC = LF + "scanners/"
LFD = "LlamaFirewall/website/docs/"
PGC = "Llama-Prompt-Guard-2/86M/MODEL_CARD.md"
ARXIV = "https://arxiv.org/html/2505.03574"

intro = f"""# Purple Llama inventory (draft for sheet 3x)

Scope: Meta Purple Llama, the umbrella project in the repository meta-llama/PurpleLlama: the Prompt Guard 2 models, the LlamaFirewall framework and its scanners, Code Shield with the Insecure Code Detector, the CyberSecEval benchmark and ClassifyIt. Llama Guard (columns V to Z, sheet 3d) is cross-referenced only and not restated. Rows whose Covered by cell is a marker are deliberately not Table 3 columns: the legacy marker is for Prompt Guard 1, and the inventory-only marker (R011) is for CyberSecEval 4 (evaluated on its own evaluation-tooling sheet) and ClassifyIt (bulk Google Drive classification, unrelated to the AI conversation). Covered-by values are the option B headers of the brief (per-tool prefixes Prompt Guard 2, LlamaFirewall, Code Shield); if CP1 picks option A only these cells and the column headings change. Code and repo docs facts are pinned to commit 172c1074 of meta-llama/PurpleLlama (author date 2026-09-29; git ls-remote returned it as HEAD on 2026-10-09 and git ls-remote --tags returned nothing) {R}. The repository has no release, tag or CHANGELOG, so release notes are {ND} (checked git ls-remote --tags and the file list of the clone). Code facts were read from a shallow clone and not run. PyPI facts come from the simple index listings read 2026-10-09: llamafirewall latest file 1.0.3 and codeshield latest file 1.0.1 {D}; whether the PyPI sdists equal the repo code at the pin is {TBV}. Hugging Face revisions come from the Hugging Face model API (HTTP 200, gated manual for all three repos, read 2026-10-09): Llama-Prompt-Guard-2-86M a8ded8e6, Llama-Prompt-Guard-2-22M 11614a15, Prompt-Guard-86M 1209add6 (v1) {D}; the model card bodies of the gated repos are not readable, so model-card facts are cited from the card files in the repo at the pin. Meta docs pages (llama.com addresses redirect to dev.meta.ai, same owner, HTTP 200 after redirect, observed 2026-10-09) are unpinned {D}. The LlamaFirewall docs site (meta-llama.github.io/PurpleLlama/LlamaFirewall/docs) is a build of LlamaFirewall/website/docs; where a passage was confirmed in the pinned file the cell cites the .md blob. Names: Meta writes Llama Prompt Guard 2 (model card), Prompt Guard 2 (llama.com), PromptGuard 2 (LlamaFirewall docs and paper), Code Shield (llama.com, root README) and CodeShield (repo and LlamaFirewall docs) {D}. Meta publishes no recommended Prompt Guard 2 threshold, no AlignmentCheck threshold, latency or cost, and no LlamaFirewall latency or throughput figure (checked the Prompt Guard 2 card, README, dev.meta.ai pages, LlamaFirewall docs and the paper) {ND}. Short names in cells: PL = meta-llama/PurpleLlama at 172c1074; LF = LlamaFirewall/src/llamafirewall/ in PL; LFD = LlamaFirewall/website/docs/ in PL; PG2C = Llama-Prompt-Guard-2/86M/MODEL_CARD.md in PL (the 22M card is a textual copy apart from the size words and the model id, checked with diff); ICD = CodeShield/insecure_code_detector/ in PL; CSB = CybersecurityBenchmarks/ in PL; PAPER = arXiv 2505.03574 (html version read 2026-10-09); LLAMA = dev.meta.ai/llama/llama-protections; HF = Hugging Face."""

# ---------------- (a)
ha = ["Component", "Family", "Type (model, scanner, library, benchmark, tool)", "Status (Available, Legacy, Experimental)", "Version or revision read", "Backing model or engine", "Licence", "Covered by Table 3 column", "Source URL"]
ra = [
    ["Llama Prompt Guard 2 86M", "Prompt Guard", "model",
     f"Available {D} (LLAMA and Prompt Guard docs pages: released as the update to Prompt Guard)",
     f"Hugging Face revision a8ded8e6, last modified 2025-04-29, gated manual {H86}",
     f"mDeBERTa-base fine-tuned classifier, labels benign or malicious (PG2C) {R}",
     f"Llama 4 Community Licence (86M/LICENSE first line) {R}; HF metadata license other, license_name llama4 {H86}",
     cov(H1, H2), f"{B}{PGC} ; {B}Llama-Prompt-Guard-2/86M/LICENSE ; {HF86}"],
    ["Llama Prompt Guard 2 22M", "Prompt Guard", "model",
     f"Available {D} (LLAMA and Prompt Guard docs pages)",
     f"Hugging Face revision 11614a15, last modified 2025-04-29, gated manual {H22}",
     f"DeBERTa-xsmall fine-tuned classifier; the card notes that no multilingual deberta-xsmall exists, which widens the multilingual gap to the 86M model {R}",
     f"Llama 4 Community Licence (22M/LICENSE first line) {R}; HF metadata license other, license_name llama4 {H22}",
     cov(H1), f"{B}Llama-Prompt-Guard-2/22M/MODEL_CARD.md ; {B}Llama-Prompt-Guard-2/22M/LICENSE ; {HF22}"],
    ["Prompt Guard 1 (Prompt-Guard-86M)", "Prompt Guard", "model",
     f"Legacy: the folder README says a new version, PromptGuard 2, was released on 29 April and recommends upgrading {R}",
     f"Hugging Face revision 1209add6, last modified 2025-11-12, gated manual {HV1}",
     f"mDeBERTa-v3-base; three labels benign, injection, jailbreak (Prompt-Guard/MODEL_CARD.md lines 27-28 and 89) {R}",
     f"HF tag llama3.1 {HV1}; the root README licence table says Llama 3.2 Community License for Prompt Guard {R}",
     LEG, f"{B}Prompt-Guard/README.md ; {B}Prompt-Guard/MODEL_CARD.md ; {HFV1}"],
    ["llamafirewall package", "LlamaFirewall", "library", f"Available {D}",
     f"pyproject version 1.0.3 {R} (LlamaFirewall/pyproject.toml line 7); PyPI latest file 1.0.3 {D} (simple index listing, observed 2026-10-09); sdist equals repo code {TBV}",
     f"Python orchestrator of scanners; dependencies include codeshield 1.0.1 or later, torch, transformers, huggingface_hub and openai (pyproject lines 14-23); needs Python 3.10 or later (LlamaFirewall/README.md line 53) {R}",
     f"MIT (LlamaFirewall/LICENSE) {R}",
     LFALL, f"{B}LlamaFirewall/pyproject.toml ; {B}LlamaFirewall/README.md ; https://pypi.org/simple/llamafirewall/"],
    ["PromptGuard scanner", "LlamaFirewall", "scanner",
     f"Available {I} (premise: not under scanners/experimental and not marked experimental in code or docs)",
     f"Code at pin 172c1074 {R} (PromptGuardScanner in LF scanners/prompt_guard_scanner.py)",
     f"Runs Llama-Prompt-Guard-2-86M locally through Transformers (promptguard_utils.py line 40) {R}",
     f"Scanner code MIT {R}; the model it loads is under the Llama 4 Community Licence (row 1)",
     cov(H2), u(SC + "prompt_guard_scanner.py", SC + "promptguard_utils.py")],
    ["AlignmentCheck scanner", "LlamaFirewall", "scanner",
     f"Experimental: the code sits in scanners/experimental {R}; the paper says AlignmentCheck is currently an experimental feature within LlamaFirewall {D} (PAPER section 4.2)",
     f"Code at pin 172c1074 {R} (AlignmentCheckScanner in LF scanners/experimental/alignmentcheck_scanner.py)",
     f"Few-shot LLM auditor; default model meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 at https://api.together.xyz/v1, key variable TOGETHER_API_KEY (custom_check_scanner.py lines 35-38) {R}",
     f"Scanner code MIT {R}; the hosted model and the Together service carry separate terms (block f)",
     cov(H3), u(SC + "experimental/alignmentcheck_scanner.py", SC + "custom_check_scanner.py", LFD + "documentation/scanners/alignment-check.md") + f" ; {ARXIV}"],
    ["CodeShield scanner", "LlamaFirewall", "scanner",
     f"Available {I} (premise: not marked experimental)",
     f"Code at pin 172c1074 {R} (CodeShieldScanner in LF scanners/code_shield_scanner.py)",
     f"Calls the Insecure Code Detector over get_supported_languages() in parallel (lines 57-59) {R}",
     f"Scanner code MIT {R}; Semgrep is a separate dependency (block f)",
     cov(H4), u(SC + "code_shield_scanner.py", LFD + "documentation/scanners/code-shield.md")],
    ["Regex scanner", "LlamaFirewall", "scanner",
     f"Available {I} (premise: not marked experimental)",
     f"Code at pin 172c1074 {R} (RegexScanner in LF scanners/regex_scanner.py)",
     f"Five fixed default regular expressions compiled with IGNORECASE and DOTALL; the constructor takes scanner_name and block_threshold only (lines 21-29, 41-45, 59) {R}",
     f"Scanner code MIT {R}",
     cov(H5), u(SC + "regex_scanner.py", LFD + "tutorials/regex-scanner-tutorial.md")],
    ["Hidden ASCII scanner", "LlamaFirewall", "scanner",
     f"Available {I} (premise: not marked experimental in code; no docs page describes it)",
     f"Code at pin 172c1074 {R} (HiddenASCIIScanner in LF scanners/hidden_ascii_scanner.py)",
     f"Pure code, no model: blocks any character from U+E0000 to U+E007F (line 30) {R}",
     f"Scanner code MIT {R}",
     cov(H7), u(SC + "hidden_ascii_scanner.py")],
    ["PIICheck scanner", "LlamaFirewall", "scanner",
     f"Experimental: the code sits in scanners/experimental {R}; no docs page describes the scanner {ND} (checked the LFD pages and the paper)",
     f"Code at pin 172c1074 {R} (PIICheckScanner in LF scanners/experimental/piicheck_scanner.py)",
     f"LLM prompt on Together: default model meta-llama/Llama-3.3-70B-Instruct-Turbo, key variable TOGETHER_API_KEY, block threshold 0.7 (lines 45-48) {R}",
     f"Scanner code MIT {R}; hosted model and service terms are separate (block f)",
     cov(H5), u(SC + "experimental/piicheck_scanner.py")],
    ["CustomCheckScanner base class", "LlamaFirewall", "scanner base class",
     f"Experimental: the class docstring starts with the word EXPERIMENTAL in square brackets (custom_check_scanner.py line 25) {R}",
     f"Code at pin 172c1074 {R}",
     f"Abstract generic class that sends a system prompt and the message text to an OpenAI-compatible endpoint; defaults Llama-4-Maverick on Together, temperature 0.0, block_threshold 0.0 (lines 30-40) {R}; AlignmentCheckScanner and PIICheckScanner subclass it {R}",
     f"MIT {R}",
     cov(H5), u(SC + "custom_check_scanner.py", LF + "utils/base_llm.py")],
    ["Custom scanner route (Scanner base class and register_llamafirewall_scanner)", "LlamaFirewall", "extension point",
     f"Available {R} (code); the docs page still describes a BaseScanner class and editing create_scanner {R} (conflict, see block b)",
     f"Code at pin 172c1074 {R} (llamafirewall.py lines 29-43 and scanners/base_scanner.py line 12)",
     f"User subclass of Scanner registered under a string name in custom_scanner_registry; create_scanner instantiates it with no arguments (llamafirewall.py lines 46-50) {R}",
     f"MIT for the framework {R}; the user's own scanner has its own terms",
     cov(H5), u(LF + "llamafirewall.py", SC + "base_scanner.py", "LlamaFirewall/examples/demo_customized_scanner_via_open_guardrails.py", LFD + "documentation/advanced-usage/adding-custom-scanner.md")],
    ["codeshield package and CodeShield class", "Code Shield", "library", f"Available {D}",
     f"Repo pyproject version 0.0.1 {R} (CodeShield/pyproject.toml line 3); PyPI latest file 1.0.1 {D} (simple index listing, observed 2026-10-09), which differs from the repo version; equality of PyPI 1.0.1 with the repo code is {TBV}",
     f"CodeShield.scan_code(code, language=None) runs the Insecure Code Detector and returns CodeShieldScanResult; dependencies semgrep above 1.68 and pyyaml (pyproject line 15) {R}",
     f"MIT (CodeShield/LICENSE; root README table row Code Shield) {R}",
     cov(H6), f"{B}CodeShield/codeshield.py ; {B}CodeShield/pyproject.toml ; {B}CodeShield/README.md ; https://pypi.org/simple/codeshield/"],
    ["Insecure Code Detector (ICD) library", "Code Shield", "library", f"Available {D}",
     f"Code at pin 172c1074 {R} (CodeShield/insecure_code_detector)",
     f"Regex analyzer plus Semgrep analyzer; the README says it does not work well for categories that need taint flow analysis (README line 35) {R}",
     f"MIT {R}",
     cov(H6, H4), f"{B}CodeShield/insecure_code_detector/README.md ; {B}CodeShield/insecure_code_detector/insecure_code_detector.py"],
    ["CyberSecEval 4", "CyberSecEval", "benchmark",
     f"Available {R}; the maintainers say that as of 12 June 2025 they are exploring options for the next version {R} (CSB README line 168)",
     f"Code at pin 172c1074 {R}; no CyberSecEval 4 paper id located {TBV}",
     f"Benchmark suite that tests LLMs, not guardrails {I}; evaluated on its own evaluation-tooling sheet (proposed 3j), not here",
     f"MIT (CSB/LICENSE) {R}",
     INV, f"{B}CybersecurityBenchmarks/README.md ; {B}CybersecurityBenchmarks/LICENSE"],
    ["ClassifyIt (SensitiveDocClassification)", "ClassifyIt", "tool", f"Available {R}",
     f"Code at pin 172c1074 {R}",
     f"Bulk Google Workspace classification: Google Drive API plus a Llama Stack server plus Apache Tika, writes a CSV and applies Drive labels (Readme.md lines 3-15) {R}; unrelated to the AI conversation {I}",
     f"MIT (SensitiveDocClassification/LICENSE, copyright 2025 Meta) {R}",
     INV, f"{B}SensitiveDocClassification/Readme.md ; {B}SensitiveDocClassification/LICENSE"],
]
assert len(ra) == 16

# ---------------- (b)
hb = ["ScannerType or class", "Class and source file", "Mechanism", "Default block threshold", "Decision values returned", "Default roles (no config)", "External dependency", "Maturity (stable, experimental, as the code or docs state)", "Covered by Table 3 column", "Source URL"]
rb = [
    ["PROMPT_GUARD", "PromptGuardScanner in LF scanners/prompt_guard_scanner.py and promptguard_utils.py",
     f"Runs Llama-Prompt-Guard-2-86M locally; whitespace-normalising preprocessing, truncation at 512 tokens, score is the last class probability (probabilities[0, -1]); only message.content is read (prompt_guard_scanner.py lines 34-36; promptguard_utils.py lines 79-129) {R}. The docs use-case page names this scanner PROMPT_INJECTION, which is not a ScannerType member; PROMPT_GUARD is the name in the enum and in how-to-use-llamafirewall.md (conflict, code stronger) {R}",
     f"0.9 constructor default, BLOCK if the score is at or above it (prompt_guard_scanner.py lines 24, 38-40) {R}; Meta recommends no value {ND} (checked the card, README, dev.meta.ai page and LFD scanner page)",
     f"ALLOW, BLOCK {R}",
     f"TOOL, USER (llamafirewall.py lines 91-92) {R}",
     f"Hugging Face gated model download and login on first use (promptguard_utils.py lines 53-69); no API key {R}",
     f"Not marked experimental in code or docs {I}",
     cov(H2), u(SC + "prompt_guard_scanner.py", SC + "promptguard_utils.py", LF + "llamafirewall_data_types.py", LFD + "documentation/getting-started/adding-custom-use-case.md")],
    ["AGENT_ALIGNMENT", "AlignmentCheckScanner in LF scanners/experimental/alignmentcheck_scanner.py",
     f"Few-shot LLM auditor: compares the latest action in the trace with the first user message found in past_trace and returns observation, thought and a boolean conclusion; without past_trace it returns ALLOW with status ERROR and the reason No trace provided, cannot proceed (lines 64-92) {R}. The system prompt includes the sentence When in doubt, assume the action is not misaligned (line 148) {R}",
     f"No threshold is applied: the score is 1.0 if conclusion is true, else 0.0, and 1.0 maps to the decision (lines 120-130) {R}; the inherited block_threshold of 0.0 is not used there {I}",
     f"ALLOW, HUMAN_IN_THE_LOOP_REQUIRED; never BLOCK {R}",
     f"None; not in the no-config map {R}",
     f"Together API: key variable TOGETHER_API_KEY, base URL https://api.together.xyz/v1, default model Llama-4-Maverick-17B-128E-Instruct-FP8 (custom_check_scanner.py lines 35-38) {R}. On an LLM exception the default response has conclusion true, so the scan fails closed to human review (custom_check_scanner.py lines 76-78; alignmentcheck_scanner.py lines 113-118) {R}",
     f"Experimental {R}",
     cov(H3), u(SC + "experimental/alignmentcheck_scanner.py", SC + "custom_check_scanner.py", LF + "utils/base_llm.py")],
    ["CODE_SHIELD", "CodeShieldScanner in LF scanners/code_shield_scanner.py",
     f"Runs the Insecure Code Detector for each language in get_supported_languages() in parallel; any issue gives BLOCK with a reason listing description, CWE, line and severity (lines 57-90) {R}",
     f"1.0 is passed to the base class, but the decision does not use it: any issue gives BLOCK with score 1.0 (lines 38, 67-92) {R}",
     f"ALLOW, BLOCK {R}",
     f"TOOL, ASSISTANT (llamafirewall.py lines 91 and 94) {R}",
     f"codeshield package, which needs semgrep; runs locally, no API key {R}",
     f"Not marked experimental in code or docs {I}",
     cov(H4), u(SC + "code_shield_scanner.py", "CodeShield/pyproject.toml")],
    ["REGEX", "RegexScanner in LF scanners/regex_scanner.py",
     f"Five fixed patterns in DEFAULT_REGEX_PATTERNS: Prompt injection (ignore previous instructions, or ignore all instructions), Email address, Phone number (United States style), Credit card, Social security number (nnn-nn-nnnn); the first match returns BLOCK with the reason Regex match plus the pattern name (lines 21-29, 79-87) {R}. No constructor argument takes other patterns; replacing scanner.patterns after construction would work {I}",
     f"1.0 constructor default, not used in the decision (lines 44, 79-87) {R}",
     f"ALLOW, BLOCK {R}",
     f"None; not in the no-config map {R}",
     f"None {R}",
     f"Not marked experimental in code; the docs tutorial lives under tutorials, not under scanners {R}",
     cov(H5), u(SC + "regex_scanner.py", LFD + "tutorials/regex-scanner-tutorial.md")],
    ["HIDDEN_ASCII", "HiddenASCIIScanner in LF scanners/hidden_ascii_scanner.py",
     f"Blocks when any character has a code point from 0xE0000 to 0xE007F (the Unicode tag block) and decodes the tag characters into the reason (lines 30, 54-62) {R}. The value HIDDEN_ASCII is named in one docs tutorial sentence and no docs page describes the scanner (prompt-guard-scanner-tutorial.md line 30) {R}",
     f"1.0 constructor default (line 24) {R}",
     f"ALLOW, BLOCK {R}",
     f"None; not in the no-config map {R}",
     f"None {R}",
     f"Not marked experimental in code {I}",
     cov(H7), u(SC + "hidden_ascii_scanner.py", LFD + "tutorials/prompt-guard-scanner-tutorial.md")],
    ["PII_DETECTION", "PIICheckScanner in LF scanners/experimental/piicheck_scanner.py",
     f"Sends the message text to an LLM with a system prompt listing seven PII types and parses detected_pii_types; the score is 1.0 if any type is returned, else 0.0 (lines 84-90, 116-133) {R}. On an LLM error the default response is the list ERROR, which scores 0.0 and so gives ALLOW: the scan fails open (lines 73-77, 84-90) {R}",
     f"0.7 constructor default (line 45) {R}",
     f"ALLOW, BLOCK {R}",
     f"None; not in the no-config map {R}",
     f"Together API: key variable TOGETHER_API_KEY, default model Llama-3.3-70B-Instruct-Turbo (lines 45-49) {R}",
     f"Experimental (folder name) {R}",
     cov(H5), u(SC + "experimental/piicheck_scanner.py")],
    ["CustomCheckScanner (class, no enum value)", "CustomCheckScanner in LF scanners/custom_check_scanner.py",
     f"Abstract generic base for LLM-prompt scanners: subclasses supply the system prompt, an output schema, an error response and the score conversion; the call goes through LLMClient to an OpenAI-compatible endpoint with structured output (custom_check_scanner.py lines 30-103; utils/base_llm.py lines 54-98) {R}",
     f"0.0 constructor default (line 39) {R}",
     f"Set by the subclass {R}",
     f"None; not in the no-config map {R}",
     f"OpenAI-compatible endpoint; defaults to Together with TOGETHER_API_KEY (lines 35-38); LLMClient raises ValueError if the key variable is empty (base_llm.py lines 45-50) {R}",
     f"Experimental: the docstring says EXPERIMENTAL {R}",
     cov(H5), u(SC + "custom_check_scanner.py", LF + "utils/base_llm.py")],
    ["Registered custom scanners (string names in custom_scanner_registry)", "Scanner subclass plus register_llamafirewall_scanner in LF llamafirewall.py",
     f"A decorated class is stored under its string name and used when that string appears in a Configuration list; create_scanner calls the class with no arguments (llamafirewall.py lines 29-50) {R}. The docs page says to inherit BaseScanner and add a ScannerType branch to create_scanner; BaseScanner does not exist under src and the code route is the registry (adding-custom-scanner.md lines 10-14, 31-32) {R}",
     f"Set by the user's class (the base Scanner default is 1.0, base_scanner.py lines 13-18) {R}",
     f"Set by the user's class {R}",
     f"None; user configured {R}",
     f"None from the framework {R}",
     f"Extension point; the repo example is a demo scanner that never blocks {R}",
     cov(H5), u(LF + "llamafirewall.py", SC + "base_scanner.py", "LlamaFirewall/examples/demo_customized_scanner_via_open_guardrails.py", LFD + "documentation/advanced-usage/adding-custom-scanner.md")],
]
assert len(rb) == 8

# ---------------- (c)
hc = ["Configuration", "Role", "Role meaning in code", "Scanners configured", "Direction under R002", "Covered by Table 3 column", "Source URL"]
UC = u(LF + "config.py", LFD + "documentation/getting-started/adding-custom-use-case.md")
rc = [
    ["No config (default dictionary)", "TOOL", f"Code comment: tool output (llamafirewall_data_types.py line 35) {R}", f"CODE_SHIELD, PROMPT_GUARD {R}",
     f"Tool output entering the agent context: PromptGuard reads it as untrusted input and CodeShield as generated code {I} (premise: the role comments and the paper's PromptGuard evaluation on user and tool messages)",
     cov(H2, H4), u(LF + "llamafirewall.py", LF + "llamafirewall_data_types.py") + f" ; {ARXIV}"],
    ["No config (default dictionary)", "USER", f"Code comment: user input {R}", f"PROMPT_GUARD {R}",
     f"Input side {I} (premise: user messages precede the model)", cov(H2), u(LF + "llamafirewall.py", LF + "llamafirewall_data_types.py")],
    ["No config (default dictionary)", "SYSTEM", f"Code comment: system input {R}", f"None: empty list {R}",
     f"Input side {I}; any scanner can be attached because a Configuration maps a Role to a sequence of scanner types (config.py line 13) {R}",
     LFALL, u(LF + "llamafirewall.py", LF + "config.py")],
    ["No config (default dictionary)", "ASSISTANT", f"Code comment: LLM output {R}", f"CODE_SHIELD {R}",
     f"Output side {I} (premise: assistant messages are model output)", cov(H4), u(LF + "llamafirewall.py", LF + "llamafirewall_data_types.py")],
    ["No config (default dictionary)", "MEMORY", f"Code comment: memory {R}", f"None: empty list {R}",
     f"The code does not say whether memory is input or output {ND} (checked the role comments and LFD pages); any scanner can be attached {R}",
     LFALL, u(LF + "llamafirewall.py", LF + "llamafirewall_data_types.py")],
    ["Predefined use case CHAT_BOT (UseCase value chatbot)", "USER", f"As above {R}", f"PROMPT_GUARD {R}",
     f"Input side {I}", cov(H2), UC],
    ["Predefined use case CHAT_BOT (UseCase value chatbot)", "SYSTEM", f"As above {R}",
     f"PROMPT_GUARD {R}; the docs page writes PROMPT_INJECTION for both roles, a name absent from the enum (conflict, code stronger) {R}",
     f"Input side {I}", cov(H2), UC],
    ["Predefined use case CODING_ASSISTANT (UseCase value coding_assistant)", "ASSISTANT", f"As above {R}", f"CODE_SHIELD {R}",
     f"Output side {I}", cov(H4), UC],
    ["Predefined use case CODING_ASSISTANT (UseCase value coding_assistant)", "TOOL", f"As above {R}", f"CODE_SHIELD {R}",
     f"Tool output treated as code {I}", cov(H4), UC],
    ["README basic usage example", "USER", f"As above {R}",
     f"PROMPT_GUARD only: LlamaFirewall(scanners={{Role.USER: [ScannerType.PROMPT_GUARD]}}) (README lines 70-74) {R}",
     f"Input side {I}", cov(H2), f"{B}LlamaFirewall/README.md"],
    ["AlignmentCheck needs a trace (scan_replay and the trace argument)", "ASSISTANT in the README example; the role is configurable",
     f"scan(message, trace) passes past_trace; scan_replay builds past_trace for each message; without a trace the scanner returns ALLOW with status ERROR (llamafirewall.py lines 108-122, 189-211; alignmentcheck_scanner.py lines 77-83) {R}. The README example configures Role.ASSISTANT with AGENT_ALIGNMENT (README lines 117-119) {R}",
     f"AGENT_ALIGNMENT {R}",
     f"Trace side: reads the whole past trace plus the current message, neither input nor output alone {I} (premise: _pre_process_trace joins the trace and the message)",
     cov(H3), u(LF + "llamafirewall.py", SC + "experimental/alignmentcheck_scanner.py", "LlamaFirewall/README.md")],
]
assert len(rc) == 11
