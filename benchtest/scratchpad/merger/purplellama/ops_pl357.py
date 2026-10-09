"""PL3 (AlignmentCheck), PL5 (Regex and custom scanners) and PL7 (Hidden ASCII) edits (cols_b)."""
PR = "**[Documented: repo meta-llama/PurpleLlama@172c1074]**"
DOC = "**[Documented]**"
INF = "**[Inferred]**"
ND = "**[Not disclosed]**"
TBV = "**[To be verified]**"
EVALS = "**[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]**"
L33 = "**[Documented: repo meta-llama/Llama-3.3-70B-Instruct@6f6073b4]**"
PGB = "https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/"
SDIST = "https://files.pythonhosted.org/packages/70/f5/9dbd3b0a74c11323d967b0e1210a9fac0de068abc0c2e5dc08a6ee2094a5/llamafirewall-1.0.3.tar.gz"
HDR3 = "LlamaFirewall: Trace-level agent goal-hijacking detection (AlignmentCheck)"
HDR5 = "LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner)"

PIN2 = [
    "• Pin of code and repo docs: commit 172c1074 (author date 2026-09-29) " + PR,
    "• PyPI package: llamafirewall 1.0.3 is the newest sdist in the PyPI simple index (observed 2026-10-09) and LlamaFirewall/pyproject.toml@172c1074:7 also says 1.0.3 " + DOC,
]
TERMS_BULLETS = [
    '• The same terms bar attempts to "probe, scan, or test the vulnerability of the Services" without proper authorization and any use of the Services for "competitive analysis or benchmarking" (Together terms of service section 4, not Meta docs, read 2026-10-09) ' + DOC,
    "• A bench could use synthetic (made-up) traces without real personal or financial data, because the terms bar transmitting such data to Together; whether made-up values in the listed shapes count is a legal reading (suggested; premise: the section 4 restriction) " + INF,
]
ZDR = [
    '• Together default data handling (Together docs, not Meta docs, read 2026-10-09): ZDR "is not enabled by default"; unless enabled, Together "stores the prompts you send and the responses models return, and may use them for product improvements"; use for training is a separate opt-in that is off by default ' + DOC,
    "• Retention period of stored prompts and responses without ZDR (checked the Together terms section 3, privacy policy sections 2.2, 2.4 and 2.6 and the docs ZDR page; only \"as long as is necessary\" is stated) " + ND,
]


def apply(K):
    # ============================================================ PL3
    C = "PL3"
    K.sub(C, 1, "The scanner is a judge, not a classifier", "so it is the only scanner in this half whose result depends on a remote model call",
          "so, unlike the Regex and Hidden ASCII scanners, its result depends on a remote model call", "style 3: 'this half' is drafting language, and PIICheck also calls a remote model", kind="style")
    K.sub(C, 1, "The paper repeats the status", "(arXiv 2505.03574 Figure 2 caption)", "(arXiv 2505.03574 section 4.2, Figure 2 caption)", "T103", kind="style")
    K.ins_after(C, 1, "The scanner is reached through `ScannerType.AGENT_ALIGNMENT`", [
        '• The system prompt asks the judge to assess "whether the latest action that the agent is taking is aligned with the original user message and its request" (`alignmentcheck_scanner.py@172c1074:134`) ' + PR,
        "• The text sent to the judge is the earlier trace plus the current message, rendered as role and content (`alignmentcheck_scanner.py@172c1074:71-72`) " + PR,
        "• The LlamaFirewall docs site is built from `LlamaFirewall/website` on the main branch by a GitHub workflow, so the pinned .md pages are its source (`.github/workflows/sites_deployment.yml@172c1074:4-6,33-40`; `LlamaFirewall/website/docusaurus.config.js@172c1074:25-26`) " + PR],
        "T95 (r2): supports 'latest action', 'original request' and 'earlier trace' in the Summary; T22 (r1 and r2): the docs site build source")
    # R3
    K.repl(C, 3, "`scan_replay_build_trace` starts from an empty list when no trace is stored",
        "• `scan_replay_build_trace` starts from an empty list when no trace is stored, and an empty list has no user message, so the first call returns the ALLOW and ERROR result (premise: `scan_replay` passes no trace for the first message at `llamafirewall.py@172c1074:205`, and `scan_replay_build_trace` starts from an empty list at lines 231-235) " + INF,
        "T54 (r2): premise named", kind="replace")
    K.ins_after(C, 3, "`scan_replay_build_trace` starts from an empty list when no trace is stored",
        "• `require_full_trace` is False in the base scanner and set True in AlignmentCheckScanner; a text search of `LlamaFirewall` finds no other occurrence (`scanners/base_scanner.py@172c1074:20`; `alignmentcheck_scanner.py@172c1074:62`) " + PR,
        "T54 (r2): finding that was only in a Reviewer note")
    K.repl(C, 3, "The `Message` class has an optional `tool_calls` field, but AlignmentCheck renders only role and content", [
        "• The `Message` class has an optional `tool_calls` field, which appears in LlamaFirewall/src only in llamafirewall_data_types.py (lines 54, 77, 79) " + PR,
        "• AlignmentCheck serialises messages as role and content only (`alignmentcheck_scanner.py@172c1074:72`; `llamafirewall_data_types.py@172c1074:56-57`) " + PR,
        "• So structured tool-call arguments reach the judge only if they are also written into the content text (premise: the serialisation above) " + INF],
        "T45 (r1): serialisation documented; consequence inferred", kind="replace")
    # R4
    K.summary(C, 4,
        "Summary: **Few-shot prompted external language model.** The scanner calls a chat model over an OpenAI-compatible API with a fixed prompt of six examples. The code default is Llama 4 Maverick on Together, which Together lists as removed from serverless inference. No local model is used. " + DOC,
        "T46 (r1 text; r2 offered a shorter variant that drops 'No local model is used'): the unavailability of the code default is a Together-page fact")
    K.repl(C, 4, "The paper says the prompt \"can be tailored with custom few-shot examples\"", [
        '• Source conflict, prompt tailoring (paper side): the paper says the prompt "can be tailored with custom few-shot examples" (arXiv 2505.03574 Appendix C.1.2) ' + DOC,
        "• Source conflict, prompt tailoring (code side): the prompt is a module constant and the subclass constructor takes only `scanner_name` (`alignmentcheck_scanner.py@172c1074:42-61,133`) " + PR],
        "T99 (r2): one fact and one label per bullet", kind="replace")
    K.repl(C, 4, "Pins, stated separately. Code and repo docs", PIN2, "T99 (r2): pins split", kind="replace")
    K.repl(C, 4, "The sdist contents were not read, so equality of the PyPI 1.0.3 code",
        "• The PyPI llamafirewall 1.0.3 sdist (sha256 54fe55c8, read 2026-10-09) holds the same scanner code as the pinned commit for this scanner: the files are identical or differ only in blank lines and comment lines (premise: file-by-file comparison of alignmentcheck_scanner.py, custom_check_scanner.py and base_llm.py with LlamaFirewall/ at the pin) " + INF,
        "T20 (r2): sdist read and compared; comparison is [Inferred] per main's ruling on the PyPI label form", kind="replace")
    K.sub(C, 4, "Licence of the default judge model", "(Hugging Face API, observed 2026-10-09)", "(Hugging Face Hub model metadata JSON, public, observed 2026-10-09)",
          "T105 (r2): source phrase", kind="edit")
    K.sub(C, 4, "Engine and wrapper: `CustomCheckScanner` is the shared LLM-prompt base class", "The base class is described in the Regex column, PL5",
          'The base class is described in the "' + HDR5 + '" column', "T101: draft id replaced", kind="style")
    # R5
    K.sub(C, 5, "Benchmark size: 600 scenarios", "• Benchmark size: 600 scenarios", "• Source conflict, benchmark size (paper side): 600 scenarios",
          "T24 (r2): two sources give different sizes", kind="edit")
    K.repl(C, 5, "The benchmark is released as the Hugging Face dataset", [
        "• The paper links the dataset facebook/llamafirewall-alignmentcheck-evals for this benchmark (arXiv 2505.03574 Appendix A.1, footnote) " + DOC,
        '• Source conflict, benchmark size (card side): the dataset card says "577 test cases" and "577 (test cases) * 6 (models) = 3462 cases", with a label field is_malicious and no stated benign and malicious split; licence mit, not gated (dataset card at revision d50916c9) ' + EVALS,
        "• The card lists per-case fields: system prompt, prompts, the model's response, is_malicious, injected tool, attack type and category, whether the injection succeeded, and the AlignmentCheck judge decision with its system and user prompts; the JSON file is 315,677,456 bytes (HTTP HEAD, 2026-10-09) and was not downloaded " + EVALS],
        "T24 (CORRECTION, r2 text): the card says 577 test cases times 6 models, the paper says 600 scenarios; the card does not say they are the same set", kind="replace")
    K.repl(C, 5, "Published latency distribution, throughput and cost per call for AlignmentCheck",
        "• Published latency distribution, throughput and cost per call for AlignmentCheck (checked the scanner docs page, tutorial, README, paper and the llama.com protections page; not stated; Together prices tokens, not calls, and lists no serverless price for the default Maverick model) " + ND,
        "T48 (r2)", kind="replace")
    # R6
    K.repl(C, 6, "Context window in code: `_pre_process_trace` joins the whole trace with no truncation", [
        "• `_pre_process_trace` joins every message of the trace and the current message with newlines (`alignmentcheck_scanner.py@172c1074:71-72`) " + PR,
        "• Context window in code: a search of `LlamaFirewall/src` for truncation or token limits finds only the 512-token limit in `promptguard_utils.py:113`, which this scanner does not use (checked the files named) " + ND],
        "T99 (r2): a positive code fact and a code absence were one bullet under one label", kind="replace")
    K.repl(C, 6, "Together's own documentation (not Meta docs) now shows", [
        "• Together's own documentation (not Meta docs, read 2026-10-09) shows `base_url=\"https://api.together.ai/v1\"` for its OpenAI-compatible endpoint, while the Meta code default is the `api.together.xyz` host " + DOC,
        "• Together's serverless chat-model table (not Meta docs, read 2026-10-09) lists `meta-llama/Llama-3.3-70B-Instruct-Turbo` and has no Llama 4 Maverick row " + DOC,
        "• Together's deprecation history (not Meta docs, read 2026-10-09) lists `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` among models removed from serverless inference, removal date 2026-03-31, with on-demand dedicated endpoints marked \"Yes\" " + DOC,
        "• Together's Llama 4 Maverick model page (not Meta docs, read 2026-10-09) still presents the model with a code sample that uses the `api.together.xyz` host, while the deprecations page says that during a transition \"a model can still appear in catalog listings\" " + DOC,
        "• So the default judge model of AlignmentCheck and CustomCheckScanner is not available on Together's serverless service; a replacement model or a dedicated endpoint would be needed (premise: the Together pages above) " + INF,
        "• Whether the `api.together.xyz` host still accepts requests (not tested) " + TBV],
        "T46 (r1 and r2, merged): serverless removal on Together's own pages; the conflicting model page kept as its own bullet (README rule 4); the live host stays [To be verified]", kind="replace")
    K.delete(C, 6, "Model availability on Together (not Meta docs): the serverless model table", "T46: merged into the bullets above")
    K.ins_after(C, 6, "Whether the `api.together.xyz` host still accepts requests", ZDR, "T12 (r1): Together's own documentation states the retention and training defaults; the retention period is not stated")
    # R7
    K.summary(C, 7,
        "Summary: **Minimum setup:** install llamafirewall (Python 3.10 or later), set a Together API key, point the scanner at a judge model that Together serves, and attach it to assistant messages. "
        "A bench could build short traces of one user request plus agent actions, half hijacked, and compare decisions. Traces leave the machine for a third-party API, so synthetic data is suggested. " + INF,
        "T46, T11, R032 (r2 text): judge model must be one Together serves; proposal wording")
    K.repl(C, 7, "**Minimum setup:** `pip install llamafirewall`, `export TOGETHER_API_KEY=...`",
        "• **Minimum setup:** `pip install llamafirewall`, `export TOGETHER_API_KEY=...`, build `LlamaFirewall({Role.ASSISTANT: [ScannerType.AGENT_ALIGNMENT]})` and call `scan_replay` on a list of messages that starts with a `UserMessage`; the shipped default judge model needs a replacement (see R4) and this setup has not been run " + INF,
        "T100, T46 (r2): process wording removed", kind="style")
    K.repl(C, 7, "External dependency to state in the test plan",
        "• A bench would have to account for an external dependency: every scan sends the user objective and the trace text to a hosted language model on Together AI, a third party, using a paid key, so testing is not local and involves data sharing " + INF,
        "R032 (r2)", kind="style")
    K.sub(C, 7, "Third-party terms (Together, not Meta docs): \"You will not use the Services to transmit",
          ", so traces for the bench should contain no real personal or financial data **[Documented]**", " **[Documented]**",
          "T11 (r1): the recommendation moves to its own [Inferred] bullet", kind="hygiene")
    K.ins_after(C, 7, "Third-party terms (Together, not Meta docs): \"You will not use the Services to transmit", TERMS_BULLETS,
                "T11 (r1): other section 4 clauses recorded; synthetic data worded as a suggestion (R032)")
    K.repl(C, 7, "Test inputs for the Table 3 type \"agent trace\"",
        "• A possible source of test cases is Meta's released dataset facebook/llamafirewall-alignmentcheck-evals (577 test cases times 6 models, 3,462 records, MIT, evaluation use only); its cases hold prompts, labels and stored judge decisions rather than ready-made traces, so a bench would first need to check whether a case can be replayed as a trace (premise: the dataset card fields) " + INF,
        "T24 (r1 and r2, merged), R032", kind="replace")
    K.repl(C, 7, "Mark the judge model as a test variable",
        "• A bench could treat the judge model as a variable: results depend on which model serves the call, and the shipped default is not served by Together serverless " + INF, "R032, T46 (r2)", kind="style")
    K.repl(C, 7, "Record the decision and the reason text, and flag results whose reason begins",
        "• A bench could record the decision and the reason text, and could treat results whose reason begins \"Observation: Error occurred during evaluation\" as errors rather than detections " + INF, "R032 (r2)", kind="style")
    K.repl(C, 7, "Metrics for the bench: detection rate on hijacked traces",
        "• Possible metrics: detection rate on hijacked traces, false-positive rate on benign traces and calls per trace; the paper's figures (above 80% recall, below 4% false positives) are on Meta's own benchmark and may not transfer " + INF, "R032 (r2)", kind="style")
    # R8
    K.summary(C, 8,
        "Summary: **Key open questions.** Which judge model replaces the default Maverick that Together lists as removed from serverless, Together cost and data terms for traces, latency and context limits, whole-trace reasoning versus the one-action prompt, and judge reliability on the bench.",
        "T46 (r2 text)")
    K.repl(C, 8, "Is `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` still served on Together",
        "• Which judge model a bench would run, since Together lists the default Maverick model as removed from serverless inference on 2026-03-31 and still offers it only as a dedicated endpoint (needs a replacement subclass or a dedicated endpoint; whether the old host still answers needs testing)",
        "T46 (r2)", kind="replace")
    K.repl(C, 8, "Cost per call and rate limits for the default model",
        "• Cost per trace for a replacement judge model (Together lists tokens, not calls; no numeric serverless rate limit is published; needs a measurement of trace token counts)", "T48 (r2)", kind="replace")
    K.repl(C, 8, "Do Together's data-retention defaults allow agent traces",
        "• Whether sending agent traces to Together is acceptable under its default storage of prompts and responses (licensing and data-handling question; the defaults are in R6)",
        "T12 (r1), T100: process wording removed", kind="replace")
    K.repl(C, 8, "Whether the HF dataset `facebook/llamafirewall-alignmentcheck-evals` can be used directly",
        "• How the dataset's 577 test cases (with six model responses each) relate to the paper's 600 scenarios, and whether a case can be turned into a trace for AlignmentCheck (card read, the 316 MB file was not read; needs testing)",
        "T24 (r2)", kind="replace")
    K.delete(C, 8, "Whether the PyPI 1.0.3 sdist matches the repo at 172c1074", "T20 (r2): the sdist was read")
    # R9
    for u in (SDIST, "https://pypi.org/project/llamafirewall/",
              "https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
              "https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/raw/d50916c9ea26e374667c030268218b28c20626a3/README.md",
              "https://docs.together.ai/docs/deprecations", "https://www.together.ai/pricing", "https://docs.together.ai/docs/serverless/rate-limits",
              "https://www.together.ai/models/llama-4-maverick", "https://docs.together.ai/docs/zero-data-retention",
              "https://docs.together.ai/docs/privacy-and-security", "https://www.together.ai/privacy",
              PGB + ".github/workflows/sites_deployment.yml", PGB + "LlamaFirewall/website/docusaurus.config.js",
              PGB + "LlamaFirewall/src/llamafirewall/scanners/base_scanner.py"):
        K.add_url(C, u, "T11, T12, T20, T22, T24, T46, T48, T54, T105: page or file cited in R1 to R8")
    K.summary(C, 9, "Summary: Meta LlamaFirewall code, docs and tests at the pinned commit, the Meta-authored LlamaFirewall paper, Hugging Face pages for the default model and the released dataset, PyPI, and Together's own pages for third-party terms and availability.",
              "R9 Summary lists the new source kinds")

    # ============================================================ PL5
    C = "PL5"
    K.summary(C, 1,
        "Summary: **Fixed regex blocking plus a custom-scanner route.** The Regex scanner blocks a message when it matches built-in patterns for two injection phrases, email, phone, credit card or social security number. "
        "Custom scanners are added by extending a scanner base class; LLM-prompt scanners are experimental. " + DOC,
        "T95 (r2): 'subclassing Scanner' is a class name; the pattern list is now supported in R1")
    K.ins_after(C, 1, "`RegexScanner` \"checks messages against a list of regex patterns\"",
        "• The built-in patterns are named Prompt injection, Email address, Phone number, Credit card and Social security number (`regex_scanner.py@172c1074:23-28`) " + PR,
        "T95 (r2): the pattern list the Summary relies on is in R2; named here too")
    K.delete(C, 1, "Whether the regex scanner and the LLM-prompt scanners are one function or two",
        "R030 (Q-B): PL5 stays one column; the checkpoint bullet is process text (T100)")
    K.summary(C, 2,
        "Summary: **Two injection phrases and four PII shapes.** The patterns match \"ignore previous instructions\", \"ignore all instructions\", and email, phone, credit card and social security number shapes. Nothing else is checked by the Regex scanner. " + DOC,
        "T92 (r2): 'US-style' was an [Inferred] reading inside a [Documented] Summary and email is not a US-style shape")
    K.sub(C, 3, "Custom-check scanners built on `CustomCheckScanner` decide their own use of the trace", "(column PL3)", '(the "' + HDR3 + '" column)', "T101", kind="style")
    K.summary(C, 4,
        "Summary: **Compiled regular expressions, no model.** Python patterns are compiled in the constructor with case-insensitive matching and run locally with no key. Custom scanners extend a scanner base class and register by name; the experimental LLM-prompt scanners call Together. " + DOC,
        "T95 (r2): 'compiled once' is not supported, a new scanner instance is created on every scan call; 'subclass Scanner' removed (class name)")
    K.repl(C, 4, "Replacing patterns by assigning to `scanner.patterns` after construction", [
        "• `LlamaFirewall.scan` creates a new scanner instance for each scan call (`llamafirewall.py@172c1074:117-118`), and `RegexScanner()` is created inside `create_scanner` (`llamafirewall.py@172c1074:78`) " + PR,
        "• Replacing patterns by assigning to `scanner.patterns` after construction is possible in Python but does not persist through `LlamaFirewall` (premise: a new instance is created on every scan call, `llamafirewall.py@172c1074:117-118`) " + INF],
        "T95 (r2), T35 (r1): the instance-per-call fact is code; the consequence stays inferred", kind="replace")
    K.sub(C, 4, "Source conflict, custom scanner how-to (code side)", "(checked by search of `LlamaFirewall/src`)",
          "(a text search of `LlamaFirewall/src`, `examples` and `tests` finds no `BaseScanner`)", "T59 (r2): search widened and named")
    K.ins_after(C, 4, "Source conflict, custom scanner how-to (code side)",
        "• The docs page and the registry code arrived in the same commit on 2025-04-29, and the page has not been changed since (git history of the pinned repository) " + PR,
        "T59 (r2): history read")
    K.repl(C, 4, "Pins, stated separately. Code and repo docs", PIN2 + [
        "• The PyPI llamafirewall 1.0.3 sdist (sha256 54fe55c8, read 2026-10-09) holds the same scanner code as the pinned commit for this scanner: the files are identical or differ only in blank lines and comment lines (premise: file-by-file comparison of regex_scanner.py, custom_check_scanner.py and piicheck_scanner.py with LlamaFirewall/ at the pin) " + INF],
        "T99, T20 (r2): pins split; sdist read and compared", kind="replace")
    K.ins_after(C, 4, "PIICheckScanner defaults: model `meta-llama/Llama-3.3-70B-Instruct-Turbo`", [
        "• The base model of the PIICheckScanner default, meta-llama/Llama-3.3-70B-Instruct, carries the Llama 3.3 Community License on Meta's Hugging Face record (license tag llama3.3, gated manual; Hugging Face Hub model metadata, read 2026-10-09) " + L33,
        "• The licence of the Together-served Turbo build is not stated by Together (checked the Together Llama 3.3 70B model page and the terms; they say only that models may come with their own terms) " + ND],
        "T13 (r1): the Meta-side licence is read; the Turbo build's licence stays undisclosed")
    # R5
    K.ins_after(C, 5, "Source conflict, reason text on allow (code side)",
        "• The tutorial page was last changed on 2025-04-29, and the code that returns the scanner's own reason for a single scanner was added on 2025-05-28 (git history of the pinned repository), so the sample output matches the code as it stood on 2025-04-29 " + PR,
        "T40 (PL5 half, r2)")
    K.sub(C, 5, "This is the opposite of AlignmentCheck", "(column PL3)", '(the "' + HDR3 + '" column)', "T101", kind="style")
    # R6
    K.repl(C, 6, "Only `message.content` is scanned; the `Message` `tool_calls` field is not read", [
        "• Only `message.content` is scanned; the `Message` `tool_calls` field appears in LlamaFirewall/src only in llamafirewall_data_types.py (lines 54, 77, 79) " + PR,
        "• Scanning of function-call arguments by any LlamaFirewall scanner (searched LlamaFirewall/src, README, docs pages and paper; no scanner or page describes it) " + ND,
        "• So tool-call arguments are matched only if they appear in the content text (premise: the scanner reads message.content only) " + INF],
        "T45 (r1 and r2 agree): the search is named; absence is Not disclosed", kind="replace")
    K.ins_after(C, 6, "PIICheckScanner sends the scanned text, which is by definition text that may hold personal data", [
        "• Together prices the PIICheckScanner default model `meta-llama/Llama-3.3-70B-Instruct-Turbo` at $1.04 per 1M input tokens and $1.04 per 1M output tokens (Together docs, not Meta docs, read 2026-10-09) " + DOC,
        "• Numeric serverless rate limits (checked Together's rate-limits, serverless models and pricing pages; the rate-limits page names 429 and 503 responses and no figure) " + ND],
        "T48 (r1 and r2): price and rate-limit facts")
    K.ins_after(C, 6, "Third-party terms (Together, not Meta docs): \"You will not use the Services to transmit", TERMS_BULLETS[:1] + ZDR,
        "T11, T12: other section 4 clause and Together's default data handling, as in the AlignmentCheck column")
    # R7
    K.summary(C, 7,
        "Summary: **Minimum setup:** install llamafirewall (Python 3.10 or later) and configure the scanner for the roles under test. A bench could then send labelled strings containing each pattern plus benign and obfuscated variants. No key or model download is needed for the Regex scanner alone. " + INF,
        "R032 (r2): proposal wording")
    K.repl(C, 7, "**Minimum setup:** `pip install llamafirewall`, then `LlamaFirewall({Role.USER: [ScannerType.REGEX]})`",
        "• **Minimum setup:** `pip install llamafirewall`, then `LlamaFirewall({Role.USER: [ScannerType.REGEX]})` (or the same for `ASSISTANT` and `TOOL`) and `scan` each string; no key, no login; this setup has not been run " + INF,
        "T100 (r2): process wording removed", kind="style")
    K.repl(C, 7, "Test inputs for Table 3 input types",
        "• Possible test inputs for Table 3 input types: user prompts, model responses and tool or retrieved text that contain each of the five patterns, near misses (other phone and card formats, paraphrased injection phrases), and clean text " + INF, "R032 (r2)", kind="style")
    K.repl(C, 7, "For LLM-prompt scanners (CustomCheckScanner subclasses, PIICheckScanner)",
        "• For LLM-prompt scanners (CustomCheckScanner subclasses, PIICheckScanner): additionally set `TOGETHER_API_KEY`; every scan sends the text to Together, a third party; synthetic data only is suggested, because Together terms section 4 bars sensitive personal data, and the Together terms are worth reading first " + INF,
        "T11 (r1), R032", kind="style")
    K.repl(C, 7, "For a custom scanner: write a `Scanner` subclass",
        "• A custom scanner route: a `Scanner` subclass with a no-argument constructor, registered with `@register_llamafirewall_scanner`, with its name listed in the role configuration; Meta's demo shows the shape (`examples/demo_customized_scanner_via_open_guardrails.py@172c1074:32-50`) " + INF,
        "R032: instruction wording replaced by a description", kind="style")
    K.delete(C, 7, "If the LLM-prompt scanners become a separate column at the checkpoint", "R030 (Q-B): PL5 stays one column; checkpoint wording removed")
    # R8
    K.repl(C, 8, "Why the tutorial shows `Reason: default` for allowed messages",
        "• Whether the tutorial's `Reason: default` sample reflects the code before 2025-05-28 (the page has not been updated since 2025-04-29; a run would confirm)", "T40 (PL5 half, r2)", kind="replace")
    K.repl(C, 8, "PIICheckScanner and CustomCheckScanner: cost per call, rate limits, Together model availability",
        "• PIICheckScanner and CustomCheckScanner: Together lists Llama 3.3 70B Instruct Turbo (the PIICheckScanner default) at $1.04 per 1M input and output tokens on its serverless table and lists the Maverick default of CustomCheckScanner as removed from serverless; numeric rate limits are not published (checked the Together serverless models, pricing and rate-limits pages); the cost per call for a given text needs a measurement",
        "T46, T48 (r1 and r2, merged)", kind="replace")
    K.repl(C, 8, "Whether Together's terms allow sending real personal data for PII scanning",
        "• Whether made-up values in the shapes Together lists as sensitive personal data (social security, driver's licence, bank account, passport and card numbers, birth dates) count under section 4 of its terms (licensing question; checked the terms)",
        "T11 (r1), T100", kind="replace")
    K.delete(C, 8, "Whether the experimental LLM-prompt scanners should be a separate column", "R030 (Q-B): PL5 stays one column")
    # R9
    for u in (SDIST, "https://pypi.org/project/llamafirewall/", "https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/6f6073b423013f6a7d4d9f39144961bfbfbc386b",
              "https://www.together.ai/models/llama-3-3-70b", "https://docs.together.ai/docs/deprecations", "https://www.together.ai/pricing",
              "https://docs.together.ai/docs/serverless/rate-limits", "https://docs.together.ai/docs/zero-data-retention",
              "https://docs.together.ai/docs/privacy-and-security", "https://www.together.ai/privacy",
              PGB + ".github/workflows/sites_deployment.yml", PGB + "LlamaFirewall/website/docusaurus.config.js",
              PGB + "LlamaFirewall/pyproject.toml"):
        K.add_url(C, u, "T11, T12, T13, T20, T22, T46, T48: page or file cited in R4 to R8")
    K.summary(C, 9, "Summary: Meta LlamaFirewall code, docs and examples at the pinned commit, the Meta-authored LlamaFirewall docs site, PyPI, Hugging Face pages, and Together's own pages for the third-party API.",
              "R9 Summary lists the new source kinds")

    # ============================================================ PL7
    C = "PL7"
    K.delete(C, 1, "The column is provisional: it is drafted so it can be dropped to an inventory-only row at the checkpoint",
        "R030 (Q-B): PL7 stays a column; provisional wording removed (T100)")
    K.repl(C, 4, "Pins, stated separately. Code and repo docs", PIN2 + [
        "• The PyPI llamafirewall 1.0.3 sdist (sha256 54fe55c8, read 2026-10-09) holds the same hidden_ascii_scanner.py as the pinned commit (premise: file-by-file comparison with LlamaFirewall/ at the pin) " + INF],
        "T99, T20 (r1 and r2): pins split; sdist read and compared", kind="replace")
    K.summary(C, 7,
        "Summary: **Minimum setup:** install llamafirewall and attach the scanner to the roles under test (tool output is the case Meta tests). A bench could then send strings with tag-block characters, with and without visible text, plus ordinary and emoji text. No key or model is needed. " + INF,
        "R032 (r2): proposal wording")
    K.repl(C, 7, "**Minimum setup:** `pip install llamafirewall`, then `LlamaFirewall({Role.TOOL: [ScannerType.HIDDEN_ASCII]})`",
        "• **Minimum setup:** `pip install llamafirewall`, then `LlamaFirewall({Role.TOOL: [ScannerType.HIDDEN_ASCII]})` and `scan` each string, as Meta's test does; no key, no login; this setup has not been run " + INF,
        "T100 (r2)", kind="style")
    K.repl(C, 7, "Test inputs for Table 3 input types: tool or retrieved text",
        "• Possible test inputs for Table 3 input types: tool or retrieved text, user prompts and model responses; positives could be built by encoding an ASCII sentence into U+E0000 to U+E007F characters, alone and appended to visible text, and negatives from clean text, accented and non-Latin text, and other invisible characters " + INF,
        "R032 (r2)", kind="style")
    K.repl(C, 7, "Note for the bench plan: this scanner is a deterministic filter",
        "• As a deterministic filter, one pass per string would be enough; repeated runs for variation would not be needed " + INF, "R032 (r2)", kind="style")
    K.sub(C, 8, "Is the decoded reason safe to display to users or models", "(needs a policy decision for the bench)", "(left open for bench design)", "R032, T100 (r2)", kind="style")
    for u in (SDIST, "https://pypi.org/project/llamafirewall/", PGB + "LlamaFirewall/pyproject.toml"):
        K.add_url(C, u, "T20: sdist read and cited in R4; pyproject cited in the pin bullet")
