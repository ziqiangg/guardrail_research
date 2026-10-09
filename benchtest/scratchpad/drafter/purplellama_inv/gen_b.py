from gen_a import *

ICD = "CodeShield/insecure_code_detector/"
RULES = ICD + "rules/"
LLAMA_URL = "https://dev.meta.ai/llama/llama-protections"
PGDOC_URL = "https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard"
LFDOC = "https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/"

# ---------------- (d)
hd = ["Language (enum member)", "In default scan list (get_supported_languages)", "In LANGUAGE_ANALYZER_MAP and analyzers", "Regex rule file", "Semgrep rule folder", "Named in READMEs and docs", "Source URL"]
SRC_D = f"{B}{ICD}languages.py ; {B}{ICD}insecure_code_detector.py ; {B}{RULES}config.yaml"
NOTNAMED = f"Not named {ND} (checked CodeShield/README.md, the ICD README, the rules README, LlamaFirewall/README.md, LFD code-shield.md and the codeshield tutorial; no mention)"


def named(lang_text, test=None):
    s = f"Named in the ICD README Languages Supported list as {lang_text} (lines 22-31) {R}"
    if test:
        s += f"; unit test file {test} exists {R}"
    return s


def other(test):
    s = NOTNAMED
    if test:
        s += f"; unit test file {test} exists {R}"
    else:
        s += "; no unit test file found in tests/"
    return s


YES = f"Yes (languages.py lines 72-82) {R}"
NO = f"No (languages.py lines 72-82) {R}"
COUNT = "counted from the file"
rd = [
    ["C", YES, f"REGEX and SEMGREP (insecure_code_detector.py lines 37-40) {R}",
     f"regex/c.yaml, 15 patterns, 5 enabled for the codeshield use case in config.yaml ({COUNT}) {R}",
     f"semgrep/c, 20 yaml files; generated c_codeshield.json 16 rules and c_cyberseceval.json 19 rules ({COUNT}); the generated JSON is used when it exists (insecure_code_detector.py lines 314-330) {R}",
     named("C", "test_c_insecure_code_detector.py"), SRC_D],
    ["CPP", YES, f"REGEX and SEMGREP (lines 41-44) {R}",
     f"regex/cpp.yaml, 3 patterns, 2 enabled for codeshield; load() also adds the C rules (insecure_patterns.py lines 49-50) ({COUNT}) {R}",
     f"No cpp folder; generated cpp_codeshield.json holds 16 rules and cpp_cyberseceval.json 19 ({COUNT}) {R}; config.yaml lists an empty Semgrep rule list for cpp {R}",
     named("C++", "test_cpp_insecure_code_detector.py"), SRC_D],
    ["CSHARP", YES, f"REGEX and SEMGREP (lines 45-48) {R}",
     f"regex/csharp.yaml, 2 patterns, 2 enabled for codeshield ({COUNT}) {R}",
     f"semgrep/csharp, 20 yaml files; generated csharp_codeshield.json 20 rules ({COUNT}) {R}",
     named("C#", "test_csharp_insecure_code_detector.py"), SRC_D],
    ["HACK", NO, f"REGEX only (line 49) {R}",
     f"regex/hack.yaml is present and empty (loads as no patterns) ({COUNT}) {R}",
     f"None {R}",
     other(None), SRC_D],
    ["JAVA", YES, f"REGEX and SEMGREP (lines 50-53) {R}",
     f"regex/java.yaml, 23 patterns, 14 enabled for codeshield ({COUNT}) {R}",
     f"semgrep/java, 12 yaml files; generated java_codeshield.json 11 rules ({COUNT}) {R}",
     named("Java", "test_java_insecure_code_detector.py"), SRC_D],
    ["JAVASCRIPT", YES, f"REGEX and SEMGREP (lines 54-57) {R}",
     f"regex/javascript.yaml, 1 pattern, 1 enabled for codeshield ({COUNT}) {R}",
     f"semgrep/javascript, 15 yaml files; generated javascript_codeshield.json 13 rules ({COUNT}) {R}",
     named("Javascript", "test_javascript_insecure_code_detector.py"), SRC_D],
    ["KOTLIN", NO, f"REGEX and SEMGREP (lines 58-61) {R}",
     f"No kotlin.yaml in regex/; only the language-agnostic file is added by load() {I} (premise: insecure_patterns.py lines 43-62)",
     f"No kotlin folder; generated kotlin_codeshield.json and kotlin_cyberseceval.json hold 0 rules ({COUNT}) {R}",
     other("test_kotlin_insecure_code_detector.py"), SRC_D],
    ["OBJECTIVE_C", NO, f"REGEX only (line 62) {R}",
     f"regex/objective_c.yaml, 9 patterns, none enabled for codeshield (no objective_c entry in config.yaml) ({COUNT}); load() also adds the C rules {R}",
     f"None {R}",
     other("test_objective_c_code_detector.py"), SRC_D],
    ["OBJECTIVE_CPP", NO, f"Not in the map: no analyzer runs for this language {R}",
     f"No objective_cpp.yaml; load() would add the objective_c and cpp rules (insecure_patterns.py lines 53-55) {R}",
     f"None {R}",
     other(None), SRC_D],
    ["PHP", YES, f"REGEX only (line 63), although Semgrep rules exist for PHP; the Semgrep branch checks the map, so those rules are not run by analyze() {I} (premise: insecure_code_detector.py lines 132-134 check the map before running Semgrep)",
     f"regex/php.yaml, 22 patterns, 3 enabled for codeshield ({COUNT}) {R}",
     f"semgrep/php, 7 yaml files; generated php_codeshield.json 7 rules ({COUNT}) {R}",
     named("PHP", "test_php_insecure_code_detector.py"), SRC_D],
    ["PYTHON", YES, f"REGEX and SEMGREP (lines 64-67) {R}",
     f"regex/python.yaml, 3 patterns, 3 enabled for codeshield ({COUNT}) {R}",
     f"semgrep/python, 14 yaml files; generated python_codeshield.json 10 rules ({COUNT}) {R}",
     named("Python", "test_python_insecure_code_detector.py"), SRC_D],
    ["RUBY", NO, f"REGEX only (line 68) {R}",
     f"regex/ruby.yaml, 1 pattern, none enabled for codeshield (no ruby entry in config.yaml) ({COUNT}) {R}",
     f"None {R}",
     other("test_ruby_insecure_code_detector.py"), SRC_D],
    ["RUST", YES, f"REGEX only (line 69) {R}",
     f"regex/rust.yaml, 13 patterns, 0 enabled for codeshield (config.yaml lists an empty regex rule list for rust) ({COUNT}) {R}; the language-agnostic rules still apply {I} (premise: insecure_patterns.py lines 56-62)",
     f"None; config.yaml lists an empty Semgrep rule list for rust {R}",
     named("Rust", "test_rust_insecure_code_detector.py"), SRC_D],
    ["SWIFT", NO, f"REGEX only (line 70) {R}",
     f"regex/swift.yaml, 10 patterns, none enabled for codeshield (no swift entry in config.yaml) ({COUNT}) {R}",
     f"None {R}",
     other("test_swift_code_detector.py"), SRC_D],
    ["XML", NO, f"REGEX only (line 71) {R}",
     f"regex/xml.yaml, 3 patterns, none enabled for codeshield (no xml entry in config.yaml) ({COUNT}) {R}",
     f"None {R}",
     other("test_xml_insecure_code_detector.py"), SRC_D],
    ["LANGUAGE_AGNOSTIC", NO, f"Not in the map; not a language. Its regex file is loaded as an add-on for every language except C++, Objective-C and Objective-C++ (insecure_patterns.py lines 49-62) {R}",
     f"regex/language_agnostic.yaml, 8 patterns, 8 enabled for codeshield ({COUNT}) {R}",
     f"None {R}",
     f"Not named {ND} (checked the same six docs files)", SRC_D],
]
assert len(rd) == 16

d_intro = (
    f"The Language enum has 16 members (languages.py lines 14-30); get_supported_languages() returns 8 of them (C, C++, C#, Java, JavaScript, PHP, Python, Rust) and is the list the CodeShield scanner and CodeShield.scan_code(code) with no language scan {R}; LANGUAGE_ANALYZER_MAP has 14 entries {R}. "
    f"Documented language counts conflict: 8 languages in the ICD README line 3, in LlamaFirewall/README.md line 45 and in LFD code-shield.md line 4 (eight) {R}; 7 programming languages in CodeShield/README.md line 11 {R}, on the llama.com protections page {D}, and in the paper section 4.4 (seven), where the same paper also says 8 and eight {D}; Meta does not say which 7. The code returns 8, so 8 is the default scan list and the 7 figure is not supported by the code {I} (premise: the list in languages.py). "
    f"The 16-member enum and the 14-entry map are not documented as supported languages; passing another Language to CodeShield.scan_code would run its analyzers {I} (premise: scan_code lines 80-83). "
    f"Counts in this table were made from the files at the pin by listing yaml and JSON rule files; the codeshield use case is the one the CodeShield scanner and scan_code use (codeshield.py line 43) {R}."
)

# ---------------- (e)
he = ["Path", "What it is", "Needs", "Applies to (input, output, trace)", "Status", "Caveats", "Covered by Table 3 column", "Source URL"]
re_ = [
    ["Hugging Face Transformers use of Prompt Guard 2", f"Load the model with the text-classification pipeline or AutoModelForSequenceClassification and read the label (PG2C lines 29-56) {H86}",
     f"transformers and torch; the gated model files; Python {H86}", f"Input: any string passed to the classifier {I} (premise: the model has no direction flag)",
     f"Available {H86}", f"512-token context window; for longer inputs the card says to split into segments and scan in parallel (line 24) {H86}. The card examples print the label and do not show how to read the probability {I}",
     cov(H1), f"{B}{PGC} ; {HF86}"],
    ["Hugging Face gated-access request", f"Manual-approval gate on all three Prompt Guard repos; the gate page text reads Log in or Sign Up to review the conditions and access this model content {D} (86M gate page, observed 2026-10-09)",
     f"A Hugging Face account, acceptance of the Llama 4 Community Licence and its Acceptable Use Policy, and approval {D}", "Not applicable",
     f"gated manual for 86M, 22M and v1 {D} (Hugging Face model API, observed 2026-10-09)",
     f"Not requested during research (read-only rule); the gate page for 22M was read and carries the same licence line {D}. Approval time {ND} (checked the gate pages)",
     cov(H1, H2), "https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M ; https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M"],
    ["pip install llamafirewall", f"PyPI package of the framework; the README gives the command pip install llamafirewall (README line 60) {R}",
     f"Python 3.10 or later and pip (README line 53) {R}; the README also lists access to Hugging Face models as a prerequisite (line 55) {R}",
     f"Input, output and trace, by role {R}", f"Available {D} (PyPI index lists 1.0.3 as the latest file)",
     f"The prerequisite line links a Llama 3.1 collection, not the Prompt Guard 2 repo {R}; the package pulls torch and transformers (pyproject lines 14-23) {R}",
     LFALL, f"{B}LlamaFirewall/README.md ; {B}LlamaFirewall/pyproject.toml ; https://pypi.org/simple/llamafirewall/"],
    ["llamafirewall configure", f"Command line helper: checks for Llama-Prompt-Guard-2-86M locally, offers to download it, checks TOKENIZERS_PARALLELISM and checks for a Together key (cli/configure.py lines 142-200) {R}",
     f"Hugging Face login for the download; an interactive terminal {R}", "Setup step, no scanning",
     f"Available {R}", f"The helper accepts TOGETHER_API_KEY or TOGETHER_API_TOKEN as set (lines 123-128), but the LLM client reads only the variable named by api_key_env_var, TOGETHER_API_KEY by default (base_llm.py lines 45-50) {R}; so a lone TOGETHER_API_TOKEN would pass the check and still fail the scanner {I}",
     cov(H2, H3), f"{B}{LF}cli/configure.py ; {B}{LF}utils/base_llm.py ; {B}LlamaFirewall/README.md"],
    ["Automatic model download into HF_HOME", f"On first use the PromptGuard scanner downloads Llama-Prompt-Guard-2-86M from Hugging Face and saves it under HF_HOME, defaulting to ~/.cache/huggingface when unset (promptguard_utils.py lines 38-77) {R}",
     f"Hugging Face token or interactive login(); access to the gated repo {R}", "Input (setup step)",
     f"Available {R}", f"The saved folder name replaces / with -- (line 50); the code logs that no data is stored by LlamaFirewall during login (lines 58-60) {R}. Behaviour in offline or air-gapped use {ND} (checked the README and LFD pages)",
     cov(H2), u(SC + "promptguard_utils.py")],
    ["CodeShield.scan_code (Python library)", f"Async class method that scans a string for insecure code and returns CodeShieldScanResult with is_insecure, issues_found and recommended_treatment (codeshield.py lines 24-34, 47-94) {R}",
     f"The codeshield package and semgrep; no model, no API key {R}", "Output: model-generated code passed as a string",
     f"Available {R}", f"With no language argument it scans the 8 default languages; any exception is logged and the result is not insecure, so errors fail open (lines 70-86) {R}",
     cov(H6), f"{B}CodeShield/codeshield.py ; {B}CodeShield/README.md"],
    ["Code Shield through LlamaFirewall", f"CodeShieldScanner wraps the same detector and maps any issue to BLOCK; attached to ASSISTANT and TOOL by default and by the CODING_ASSISTANT use case {R}",
     f"pip install llamafirewall, which depends on codeshield 1.0.1 or later (pyproject line 15) {R}", f"Output and tool output {I}",
     f"Available {I}", f"Which codeshield version the PyPI 1.0.1 release contains relative to the repo code {TBV}",
     cov(H4), u(SC + "code_shield_scanner.py", "LlamaFirewall/pyproject.toml", LF + "config.py")],
    ["Together API (AlignmentCheck, PIICheck, CustomCheckScanner)", f"Scanners send text (for AlignmentCheck the whole trace plus the latest message) to an OpenAI-compatible endpoint, by default api.together.xyz with TOGETHER_API_KEY (custom_check_scanner.py lines 35-38; alignmentcheck_scanner.py lines 71-72) {R}",
     f"A Together account and key; outbound network access {R}", f"Trace (AlignmentCheck) and text (PIICheck, custom)",
     f"Experimental {R}", f"What Together does with submitted data is not stated in the Meta files {ND} (checked the LlamaFirewall README, docs pages and code comments); the Together terms of service are Together's, not Meta documentation, and state that models may carry their own terms and that zero data retention is a user setting {D} (Together terms of service, read 2026-10-09). Testing sends agent traces to a third party",
     cov(H3, H5), u(SC + "custom_check_scanner.py", SC + "experimental/alignmentcheck_scanner.py") + " ; https://www.together.ai/terms-of-service"],
    ["OpenAI Agents SDK guardrail demo", f"examples/demo_openai_guardrails.py defines an input guardrail (USER and SYSTEM with PROMPT_GUARD) and an output guardrail (ASSISTANT with CODE_SHIELD) around scan_async (lines 30-64) {R}",
     f"pip install openai-agents (README line 179) {R}", f"Input and output {R}",
     f"Example only {R}", f"The demo trips the OpenAI tripwire on any decision other than ALLOW (lines 45, 63) {R}; the behaviour of the OpenAI Agents SDK is OpenAI's, not shown here",
     cov(H2, H4), f"{B}LlamaFirewall/examples/demo_openai_guardrails.py ; {B}LlamaFirewall/README.md"],
    ["LangChain agent demos", f"examples/demo_langchain_agent.py and examples/langchain_agent.py wrap a LangChain agent with a default LlamaFirewall() instance (langchain_agent.py lines 51 and 112) and convert LangChain messages into Role.USER, ASSISTANT or TOOL messages (lines 115-133) {R}",
     f"pip install langchain_community langchain_openai langgraph (README line 193) {R}", f"Input, output and tool output; the default instance has no AlignmentCheck {I}",
     f"Example only {R}", f"The README says the example is langchain_agent.py but the command runs examples.demo_langchain_agent (README lines 198-202) {R}; demo_langchain_misaligned.py also exists {R}",
     cov(H2, H4), f"{B}LlamaFirewall/examples/langchain_agent.py ; {B}LlamaFirewall/examples/demo_langchain_agent.py ; {B}LlamaFirewall/README.md"],
    ["llama-cookbook tutorials and the Llama reference system", f"The Prompt Guard 2 README and card link a fine-tuning tutorial notebook and inference utilities in meta-llama/llama-cookbook {R}; the root README says the Llama reference system integrates a safety layer {R}; the llama.com page says a reference guide for LlamaFirewall usage is available with Llama {D}",
     "Not read beyond the links", "Input (Prompt Guard 2)",
     f"Links returned HTTP 200 on 2026-10-09 {D}", f"The cookbook files are in another Meta repository and were not read; their content {TBV}. The Prompt Guard 2 README also links facebookresearch/llama-recipes, which was not read {TBV}",
     cov(H1), f"{B}Llama-Prompt-Guard-2/README.md ; https://github.com/meta-llama/llama-cookbook/blob/main/getting-started/responsible_ai/prompt_guard/prompt_guard_tutorial.ipynb ; https://github.com/meta-llama/llama-cookbook/blob/main/getting-started/responsible_ai/prompt_guard/inference.py ; {LLAMA_URL}"],
    ["CyberSecEval command line", f"python3 -m CybersecurityBenchmarks.benchmark.run runs the benchmark suites against LLMs under test (CSB README lines 104-110) {R}; the run script has an --enable-lf flag described as enabling LlamaFirewall on all input and output layers (run.py lines 219-224) {R}",
     f"Python 3.10 and provider API keys for the models under test {R}", "Evaluation, not a guardrail path",
     f"Available {R}", f"The enable_lf value is stored in the benchmark config (benchmark.py lines 35, 62) and no other use of LlamaFirewall appears in the .py files {I} (premise: grep of CybersecurityBenchmarks for llamafirewall and enable_lf); see the evaluation-tooling sheet",
     INV, f"{B}CybersecurityBenchmarks/README.md ; {B}CybersecurityBenchmarks/benchmark/run.py ; {B}CybersecurityBenchmarks/benchmark/benchmark.py"],
]
assert len(re_) == 12
