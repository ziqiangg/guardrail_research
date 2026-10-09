"""PL6 (Code Shield engine) and PL4 (LlamaFirewall CodeShield scanner) edits. Mostly resolutions 2 (r2), plus r1 T14."""
PR = "**[Documented: repo meta-llama/PurpleLlama@172c1074]**"
DOC = "**[Documented]**"
INF = "**[Inferred]**"
ND = "**[Not disclosed]**"
SG = "**[Documented: repo semgrep/semgrep@v1.69.0]**"
CSB = "(PyPI sdist codeshield-1.0.1, sha256 61866b92, read 2026-10-09)"
PGB = "https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/"
HDR6 = "Code Shield: Output-level insecure-code detection (LLM-generated code)"
HDR4 = "LlamaFirewall: Output-level insecure-code detection (CodeShield scanner)"

LANG_BULLETS = [
    '• The Code Shield README says "across 7 programming languages" (CodeShield/README.md@172c1074:11) ' + PR,
    '• The Meta protections page says "7 programming languages" (dev.meta.ai llama-protections, read 2026-10-09) ' + DOC,
    '• The CyberSecEval 3 paper says "7 programming languages" (arXiv 2408.01605 section 5.2) ' + DOC,
    '• The LlamaFirewall paper says "seven programming languages" in section 4.4 and "8 programming languages" in its summary (arXiv 2505.03574) ' + DOC,
    '• The Insecure Code Detector README says "supports 8 different programming languages" and lists C, C++, C#, Java, Javascript, Python, PHP, Rust (insecure_code_detector/README.md@172c1074:3,22-31) ' + PR,
    '• The LlamaFirewall docs say "eight programming languages" (LlamaFirewall/website/docs/documentation/scanners/code-shield.md@172c1074:4) ' + PR,
    '• The LlamaFirewall README says "8 programming languages" (LlamaFirewall/README.md@172c1074:45) ' + PR,
    "• `get_supported_languages()` returns eight languages: C, C++, C#, Java, JavaScript, PHP, Python, Rust (languages.py@172c1074:72-83) " + PR,
]
FIG_BULLETS = [
    "• The per-language precision and recall figure in the CyberSecEval 3 paper (Figure 18) has eight languages on its axis: Rust, PHP, C, C++, C#, Python, Java, Javascript, although the text beside it says 7 (arXiv 2408.01605 section 5.2) " + DOC,
    "• The eight figure languages equal the eight languages the code scans (premise: comparison of the figure labels with languages.py@172c1074:72-82) " + INF,
    '• Which seven languages the "7" statements mean (checked the text of the CyberSecEval 3 paper section 5.2, the LlamaFirewall paper section 4.4, both READMEs and the docs page; no list of seven) ' + ND,
    '• CyberSecEval 3 paper: Code Shield "is capable of identifying around 190 patterns across 50 different CWEs with an accuracy of 90%" (arXiv 2408.01605 section 5.2, mitigation recommendations) ' + DOC,
]
LAT5 = ('• Latency, CyberSecEval 3 paper: first layer "within 60ms", second layer "approximately 300ms", "in 90% of cases, only the first layer is invoked, maintaining the latency under 70ms for the majority of scans" '
        '(arXiv 2408.01605 section 5.2) ' + DOC)
LATDIFF_ENGINE = ("• The statements differ between sources: the README, docs page and protections page give figures that disagree with each other and with the two papers, which agree with each other; each rests on Meta's own production observations, and no latency or timeout appears in the engine code (premise: search of CodeShield and LlamaFirewall/src for latency and timeout) " + INF)
LATDIFF_SCAN = ("• The statements differ between sources: the README, docs page and protections page give figures that disagree with each other and with the two papers, which agree with each other; each rests on Meta's own production observations, and no latency or timeout appears in the scanner or engine code (premise: search of CodeShield and LlamaFirewall/src for latency and timeout) " + INF)
CWE_PL6 = ("• A count of distinct cwe_id values in the rules enabled for the CODESHIELD use case gives 46 across the eight default languages, below the \"over 50\" claim; the CyberSecEval rule set gives 62 and all rule files 64 "
           "(premise: parsing the regex YAML files and the generated Semgrep JSON files; one rule, vulnerable-strcpy, has no cwe_id) " + INF)
CWE_PL4 = ("• A count of distinct cwe_id values in the rules enabled for this scanner use case gives 46 across the eight default languages, below the \"over 50\" claim; the CyberSecEval rule set gives 62 and all rule files 64 "
           "(premise: parsing the regex YAML files and the generated Semgrep JSON files; one rule, vulnerable-strcpy, has no cwe_id) " + INF)
PIN_BUL = ('• The CyberSecEval requirements pin "semgrep==1.51.0" while the Code Shield package asks for "semgrep>1.68", so both cannot be installed in one environment '
           "(CybersecurityBenchmarks/requirements.txt@172c1074:6; CodeShield/pyproject.toml@172c1074:15; premise: 1.51.0 is not greater than 1.68) " + INF)
TMP_BULLETS = [
    "• On the fast-mode early returns the function returns before the cleanup (insecure_code_detector.py@172c1074:128-129,136-137,150-151), and the temporary file is created with delete=False " + PR,
    "• So the temporary file may remain on disk after those scans (premise: the quoted order of statements; no other deletion in the file) " + INF,
]


def apply(K):
    # ============================================================ PL6
    C = "PL6"
    K.sub(C, 1, "Wrapper versus engine: LlamaFirewall's CodeShield scanner (column PL4)", "(column PL4)",
          '(the "' + HDR4 + '" column)', "T101: draft id replaced by the header text", kind="style")
    # R2
    K.summary(C, 2,
        "Summary: **Insecure coding practices, not exploitable vulnerabilities.** Rules flag risky calls and settings such as weak hashes, command injection and buffer-overflow functions, each with a CWE id. "
        "Meta's texts say seven languages or eight, and its evaluation figure shows eight. Taint-flow analysis is out of scope. " + DOC,
        "T64 (r2): the language clause now names the figure; T95: the buffer-overflow clause is supported by rule-message bullets")
    K.repl(C, 2, "Rule examples enabled for C by Semgrep", [
        "• Rule examples enabled for C by Semgrep: md5-usage, sha1-usage, potential-command-injection, vulnerable-strcpy, crypto-weak-prng (CodeShield/insecure_code_detector/rules/config.yaml@172c1074:1-30) " + PR,
        "• The generated C Semgrep rule vulnerable-strcpy has no cwe_id and severity WARNING (rules/semgrep/_generated_/c_codeshield.json@172c1074) " + PR,
        '• Rule messages enabled for C regex include "Potential buffer overflow due to insecure usage of scanf" (CWE-119) and "Potential buffer overflow risk due to use of strcat" (CWE-120) (rules/regex/c.yaml@172c1074:6-10,18-22; enabled in rules/config.yaml@172c1074:5-8) ' + PR,
        '• The generated C Semgrep rules include "The MD5 hash function is considered insecure" (CWE-328) and the rule id potential-command-injection (CWE-78) (rules/semgrep/_generated_/c_codeshield.json@172c1074) ' + PR],
        "T70, T95 (r2): vulnerable-strcpy has no cwe_id; two documented rule-message bullets support the Summary's examples", kind="replace")
    K.repl(C, 2, "Distinct CWE ids in the rules enabled for the CODESHIELD use case", CWE_PL6,
           "T67 (CORRECTION, r2): counts are 46, 62 and 64 (one rule has no cwe_id); first-person wording removed", kind="replace")
    K.repl(C, 2, "Languages, source A (7)", LANG_BULLETS + FIG_BULLETS,
           "T64, T66, T101, style 5 (r2): letter-labelled source bullets replaced by plain pairs; Figure 18 axis, 'which seven' and the 190-pattern statement added", kind="replace")
    for a in ("Languages, source B (7)", "Languages, source B2", "Languages, source C (8)", "Languages, source D (8)", "Languages, source D2 (8)", "Languages, source E (code)"):
        K.delete(C, 2, a, "style 5 (r2): merged into the plain pairs above")
    K.repl(C, 2, "Mismatch: the analyser map lists regex only for PHP and Rust",
        "• The analyser map lists regex only for PHP, so the PHP Semgrep rules are never run by analyze() (the Semgrep branch tests `Analyzer.SEMGREP in LANGUAGE_ANALYZER_MAP.get(language, [])`; insecure_code_detector.py@172c1074:63,132-134; the rules/semgrep/php folder holds 7 YAML files) " + PR,
        "T68 (r2): the code is explicit, so the label is Documented: repo", kind="replace")
    K.repl(C, 2, "In the CODESHIELD use case, config.yaml lists no regex or Semgrep rules of its own for Rust",
        "• In the CODESHIELD use case `config.yaml` lists no regex or Semgrep rules of its own for Rust, so Rust gets only the eight language-agnostic regex rules (rules/config.yaml@172c1074 rust entry with empty lists; insecure_patterns.py@172c1074:36-62 adds language_agnostic.yaml for every language except C++ and the Objective-C languages) " + PR,
        "T68 (r2)", kind="replace")
    # R4
    K.summary(C, 4,
        "Summary: **Regex and Semgrep rule engine, installed as the codeshield package.** Rules are YAML and JSON files enabled per use case. The package depends on Semgrep. The repo folder at the pin says version 0.0.1; PyPI 1.0.1 has the same rule files but different code. " + INF,
        "T19 (r2 text). Label Inferred, not Documented: the 'same rule files, different code' clause is a sdist-versus-pin comparison, which main's ruling labels Inferred")
    K.sub(C, 4, "Analyser map: C, C++, C#, Java, JavaScript, Kotlin and Python use regex and Semgrep", "(insecure_code_detector.py@172c1074:36-72)",
          "(at the pin; insecure_code_detector.py@172c1074:36-72)", "T19: the sdist's different Kotlin entry is its own bullet below, so the two sources are not under one label")
    K.sub(C, 4, "Rule counts from the repo", "(counted from CodeShield/", "(premise: counted by parsing CodeShield/", "T98: own counts are Inferred, method named", kind="hygiene")
    K.sub(C, 4, "Rule counts from the repo", " **[Documented: repo meta-llama/PurpleLlama@172c1074]**", " " + INF, "T98", kind="hygiene")
    K.ins_after(C, 4, "Rule counts from the repo",
        "• The Semgrep rules that run are the generated JSON file for the language and use case when it exists ({language}_{usecase}.json), so C++ runs the 16 rules in cpp_codeshield.json although config.yaml lists an empty Semgrep list for cpp; the enabled-rule lists of config.yaml are read only for regex rules (insecure_code_detector.py@172c1074:314-330; insecure_patterns.py@172c1074:139-150) " + PR,
        "T68 (r2): new bullet; C++ Semgrep path")
    K.delete(C, 4, "Equality of PyPI codeshield 1.0.1 with the repo code at the pin", "T19 (CORRECTION): the sdist was read; the open question is answered")
    K.ins_after(C, 4, "PyPI simple index lists codeshield 1.0.0 and 1.0.1", [
        "• PyPI sdist codeshield-1.0.1 " + CSB + " declares version \"1.0.1\" and the dependencies \"semgrep>1.68\" and \"pyyaml\" " + DOC,
        "• The PyPI 1.0.1 sdist is not a copy of the pinned folder: of 168 shared files 30 differ, including nine Python files, and the sdist lacks the two Kotlin generated Semgrep files (premise: file-by-file comparison of the unpacked sdist with CodeShield/ at the pin, line endings ignored) " + INF,
        "• The regex rule YAML files and rules/config.yaml in the sdist are identical to the pinned files, and the generated Semgrep JSON files hold the same rule counts per language (premise: the same comparison) " + INF,
        "• Kotlin analysers, PyPI 1.0.1: regex only (sdist insecure_code_detector.py:60) " + DOC,
        "• Kotlin analysers, pin: regex and Semgrep (insecure_code_detector.py@172c1074:58-61) " + PR,
        "• Semgrep job cap, PyPI 1.0.1: none; SEMGREP_COMMAND in the sdist oss.py has no jobs option " + DOC,
        "• Semgrep job cap, pin: --jobs limited to 16 (oss.py@172c1074:57-62,74) " + PR,
        "• Enum bases, PyPI 1.0.1: Severity and Treatment are string enums (sdist issues.py:20, codeshield.py:26) " + DOC,
        "• Enum bases, pin: plain enums (issues.py@172c1074:18, codeshield.py@172c1074:24) " + PR],
        "T19 (CORRECTION, r2): PyPI 1.0.1 differs from the pin; sdist facts [Documented] with hash and date in plain text, comparisons [Inferred]")
    K.repl(C, 4, "Semgrep is a third-party component installed as a dependency", [
        "• The Semgrep repository LICENSE is the GNU Lesser General Public License, Version 2.1, at tag v1.69.0 (the first tag above the semgrep>1.68 floor) and at v1.180.0, the newest tag on 2026-10-09 (Semgrep's own repository, not Meta docs) " + SG,
        "• Code Shield passes rule files from its own folder to Semgrep: the --config argument is a local path (insecure_code_detector.py@172c1074:314-329; oss.py@172c1074:24-25,65-75) " + PR,
        "• So Semgrep Registry rules are not loaded by this route (premise: the config argument is a local path) " + INF,
        '• Semgrep\'s separate rules licence says "You may use the rules only for your own internal business purposes." (semgrep.dev/legal/rules-license, not Meta docs, read 2026-10-09) ' + DOC],
        "T14 (r1): LGPL 2.1 pinned at tags; rule path and rules licence recorded; legal consequences stay open in R8", kind="replace")
    K.ins_before(C, 4, "Release notes (checked the repo at the pin: no tags and no CHANGELOG file)",
        "• The scanner and detector source files import only standard-library modules, PyYAML and each other (import lines of code_shield_scanner.py, insecure_code_detector.py, insecure_patterns.py and oss.py at the pin); the Semgrep binary is run as a subprocess " + PR,
        "T90, T95 (r2): documented import list")
    # R5
    K.summary(C, 5,
        "Summary: **Insecure flag, issue list and a recommended treatment.** Results carry an insecure flag, the issues found and a block, warn or ignore treatment. Meta reports 96% precision and 79% recall on a manual check, but its latency statements disagree. " + DOC,
        "T65 (r2): 'four' dropped; five sources now give latency statements")
    K.repl(C, 5, "Semgrep issues carry the raw severity string from Semgrep output", [
        "• Semgrep issues carry the raw severity string from the Semgrep output (insecure_code_detector.py@172c1074:282), while the treatment check compares with the Severity enum (codeshield.py@172c1074:90; issues.py@172c1074:18-22, value \"error\") " + PR,
        "• The generated Semgrep rule files use upper-case severities (for example 6 ERROR rules in java_codeshield.json), so a Semgrep finding of severity ERROR may never produce BLOCK (premise: Semgrep echoes the rule severity string, which was not read; the PyPI 1.0.1 package has the same comparison) " + INF],
        "T69 (r2): code lines documented, consequence inferred", kind="replace")
    K.sub(C, 5, "Under the CODESHIELD rules, the only enabled regex rule with severity Error", "(premise: count over regex YAML and config.yaml)",
          "(premise: count of regex rules with severity Error among the rules loaded for the CODESHIELD use case, parsing the YAML files and config.yaml)", "T69 (r2)")
    K.repl(C, 5, "The usage notebook compares `recommended_treatment` to the strings", [
        '• The usage notebook compares `recommended_treatment` with the strings "block" and "warn" (CodeShield/notebook/CodeShieldUsageDemo.ipynb@172c1074, cell 2) ' + PR,
        "• At the pin Treatment is a plain enum, so that comparison is false; in the PyPI 1.0.1 package Treatment is a string enum, so it is true (premise: the two class definitions quoted above) " + INF],
        "T70 (r2)", kind="replace")
    K.sub(C, 5, "Precision and recall: \"CodeShield achieved a precision of 96%", "(arXiv 2505.03574 section 4.4)",
          "(arXiv 2505.03574 section 4.4; first reported in the CyberSecEval 3 paper section 5.2, which the LlamaFirewall paper cites)", "T66 (r2)")
    K.ins_after(C, 5, "Precision and recall: \"CodeShield achieved a precision of 96%",
        "• Per-language precision and recall: the paper gives a bar chart with 90% confidence bars for eight languages and no table of values (arXiv 2408.01605 Figure 18; repeated as Figure 3 in arXiv 2505.03574) " + DOC,
        "T72 (r2, with main's ruling: values are not read off the chart; only the existence of the chart and its axis labels are recorded)")
    K.sub(C, 5, "Latency, statement 1 (Code Shield README)", "Latency, statement 1 (Code Shield README)", "Latency, Code Shield README", "style 5 (r2)", kind="style")
    K.sub(C, 5, "Latency, statement 2 (LlamaFirewall docs)", "Latency, statement 2 (LlamaFirewall docs)", "Latency, LlamaFirewall docs", "style 5 (r2)", kind="style")
    K.sub(C, 5, "Latency, statement 3 (paper)", "Latency, statement 3 (paper)", "Latency, LlamaFirewall paper", "style 5 (r2)", kind="style")
    K.ins_after(C, 5, "Latency, LlamaFirewall paper", LAT5, "T65, T66 (r2): fifth latency source, verbatim from CyberSecEval 3 section 5.2")
    K.sub(C, 5, "Latency, statement 4 (protections page)", "Latency, statement 4 (protections page)", "Latency, protections page", "style 5 (r2)", kind="style")
    K.repl(C, 5, "The four statements differ and are from Meta's internal production studies", LATDIFF_ENGINE, "T65 (r2)", kind="replace")
    # R6
    K.ins_after(C, 6, "Python 3.8 or later for the package; Semgrep above version 1.68", PIN_BUL, "T75 (r2): dependency pin clash")
    K.repl(C, 6, "On the fast-mode early returns the temporary file may be left behind", TMP_BULLETS, "T70 (r2): code lines documented, consequence inferred", kind="replace")
    # R7
    K.summary(C, 7,
        "Summary: **Minimum setup:** pip install codeshield, which pulls in Semgrep, then scan labelled snippets with the CodeShield scan function in each default language and compare the insecure flag with the label. "
        "No key, model or gated access is needed. A bench could also read the recommended treatment and issue list for each case. " + INF,
        "R032 (r2): proposal wording")
    K.repl(C, 7, "Include cases for every analyser path",
        "• A bench could include cases for every analyser path: regex-only languages (PHP, Rust), regex plus Semgrep languages, and snippets that trigger only Semgrep (premise: the analyser map) " + INF, "R032", kind="style")
    K.repl(C, 7, "Pass the language explicitly in one run and leave it out in another",
        "• One run could pass the language explicitly and another leave it out, to compare results and runtime (premise: `scan_code` branches) " + INF, "R032", kind="style")
    K.repl(C, 7, "Add comment-only matches, markdown-fenced code and prose-only text",
        "• Comment-only matches, markdown-fenced code and prose-only text could be added to test the comment filter and whole-message scanning (premise: engine code) " + INF, "R032", kind="style")
    K.repl(C, 7, "Build the labelled set from public code-completion or insecure-code datasets",
        "• A labelled set could be built from public code-completion or insecure-code datasets; CyberSecEval is the benchmark Meta cites for its precision and recall (premise: the paper's evaluation text) " + INF, "R032", kind="style")
    # R8
    K.summary(C, 8,
        "Summary: **Key open questions.** Which seven languages the seven-language statements mean, real latency by language, how the PyPI package behaves against the repo code, Rust and PHP rule coverage, and whether Semgrep findings can ever recommend blocking.",
        "T19, T64, T65 (r2): the language and PyPI questions are restated")
    K.repl(C, 8, "Which seven languages the \"7\" statements mean, and why the same documents also say eight",
        "• Which seven languages the \"7\" statements mean (checked the READMEs, docs page, both papers and the code; the paper figure shows eight, the code scans eight)",
        "T64 (r2)", kind="replace")
    K.repl(C, 8, "Whether PyPI codeshield 1.0.1 equals the repo code at the pin",
        "• Whether the PyPI 1.0.1 behaviour (Kotlin regex only, no Semgrep job cap, string enums) changes results compared with the pinned code (the sdist and the pin differ in 30 of 168 shared files; needs testing)",
        "T19 (r2)", kind="replace")
    K.repl(C, 8, "Whether Rust is meant to be in the default scan list",
        "• Whether Rust and PHP are meant to run as they do (Rust gets only the language-agnostic regex rules under CODESHIELD; PHP has Semgrep rules that the analyser map never runs; nothing in the repo states the intent; needs testing)",
        "T68 (r2): the two Rust and PHP bullets merged", kind="replace")
    K.delete(C, 8, "Whether PHP Semgrep rules are meant to run", "T68 (r2): merged into the bullet above")
    K.repl(C, 8, "Whether the \"over 50\" CWE claim holds for the CODESHIELD rules",
        "• Whether the \"over 50\" CWE claim holds for the CODESHIELD rules (a count of distinct cwe_id values in the enabled rules gives 46; a rule-by-rule check would confirm)",
        "T67 (r2): corrected count; first-person wording removed", kind="replace")
    K.repl(C, 8, "Semgrep's own licence and terms (third-party; a separate inventory row)",
        "• Whether the LGPL 2.1 licence of Semgrep has consequences for a bench that installs codeshield (licensing question)",
        "T14 (r1)", kind="replace")
    # R9
    for u in ("https://files.pythonhosted.org/packages/dd/0e/cb79d48ba05eda459a5a2e90b6056019cf7f41441cdee2a17e8dd63e5502/codeshield-1.0.1.tar.gz",
              "https://pypi.org/project/codeshield/",
              "https://arxiv.org/html/2408.01605",
              "https://github.com/semgrep/semgrep/blob/v1.69.0/LICENSE",
              "https://semgrep.dev/legal/rules-license",
              PGB + "CodeShield/insecure_code_detector/insecure_patterns.py",
              PGB + "CodeShield/insecure_code_detector/rules/regex/c.yaml",
              PGB + "CodeShield/insecure_code_detector/rules/semgrep/_generated_/c_codeshield.json",
              PGB + "CybersecurityBenchmarks/requirements.txt"):
        K.add_url(C, u, "T14, T19, T64, T68, T69, T75, T95: page or file cited in R2 to R6")
    K.summary(C, 9, "Summary: Code Shield README, source and rule files in the PurpleLlama repo, Meta docs and protections pages, the PyPI index and sdist, the two Meta papers, and the Semgrep licence pages.",
              "R9 Summary lists the new source kinds")

    # ============================================================ PL4
    C = "PL4"
    K.sub(C, 1, "Wrapper versus engine: the scanner adds the role configuration", "in column PL6", 'in the "' + HDR6 + '" column',
          "T101: draft id replaced by the header text", kind="style")
    # R2
    K.repl(C, 2, "Languages, source A (8)", [
        '• The LlamaFirewall README says "8 programming languages" (LlamaFirewall/README.md@172c1074:45) ' + PR,
        '• The LlamaFirewall docs say "eight programming languages" (code-shield.md@172c1074:4) ' + PR,
        "• The scanner scans the list from `get_supported_languages()`, which returns eight: C, C++, C#, Java, JavaScript, PHP, Python, Rust (languages.py@172c1074:72-83) " + PR,
        '• The Code Shield README says "across 7 programming languages, covering more than 50+ CWEs" (CodeShield/README.md@172c1074:11) ' + PR,
        '• The Meta protections page says "7 programming languages" (dev.meta.ai llama-protections, read 2026-10-09) ' + DOC,
        '• The CyberSecEval 3 paper says "7 programming languages" (arXiv 2408.01605 section 5.2) ' + DOC] + FIG_BULLETS,
        "T64, T66, T101, style 5 (r2): letter-labelled source bullets replaced by plain pairs; CyberSecEval 3 statement, Figure 18 axis, 'which seven' and the 190-pattern statement added", kind="replace")
    for a in ("Languages, source A2 (8)", "Languages, source B (code)", "Languages, source C (7)", "Languages, source D (7)"):
        K.delete(C, 2, a, "style 5 (r2): merged into the plain pairs above")
    K.repl(C, 2, "Distinct CWE ids in the rules enabled for this scanner use case", CWE_PL4, "T67 (CORRECTION, r2): counts 46, 62, 64", kind="replace")
    K.sub(C, 2, "Rules enabled for the CODESHIELD use case: config.yaml lists 38 regex rule ids",
          "**[Documented: repo meta-llama/PurpleLlama@172c1074]**", "**[Inferred]**", "T98: a count of a list is the drafter's own count", kind="hygiene")
    K.sub(C, 2, "Rules enabled for the CODESHIELD use case: config.yaml lists 38 regex rule ids",
          "(CodeShield/insecure_code_detector/rules/config.yaml@172c1074:1-407)", "(premise: counted by parsing CodeShield/insecure_code_detector/rules/config.yaml@172c1074:1-407)", "T98", kind="hygiene")
    # R3
    K.summary(C, 3,
        "Summary: **Assistant and tool text, as plain strings.** The scanner reads only the message content and scans it as code in all default languages. It is attached to the assistant and tool roles by default and by the coding-assistant use case. " + DOC,
        "T45, style 2 (r2): the claim 'tool-call arguments are not read' was labelled Documented on an inference and is dropped; capitalised role names removed")
    K.repl(C, 3, "The message type has an optional `tool_calls` field that this scanner does not read", [
        "• The `Message` class has an optional `tool_calls` field (llamafirewall_data_types.py@172c1074:54) " + PR,
        "• No scanner in the package reads `tool_calls` (checked with a text search of the whole repository at the pin: matches only the field definitions in llamafirewall_data_types.py and a docs tutorial that passes tool calls to a chat API) " + ND,
        "• So code placed in function-call arguments is not scanned unless it also appears in the message content (premise: this scanner reads `message.content` only, code_shield_scanner.py@172c1074:56) " + INF],
        "T45 (r1 and r2 agree)", kind="replace")
    # R4
    K.summary(C, 4,
        "Summary: **Regex and Semgrep rules run through the installed codeshield package.** The scanner imports the Insecure Code Detector from the codeshield package and falls back to the repo copy. The detector's own imports are standard-library modules and PyYAML, and it needs the Semgrep dependency. " + DOC,
        "T90 (r2): 'no model, key or network access' rested on an inference; the new Summary draws on the documented import list")
    K.sub(C, 4, "So an installed codeshield package, not the repo folder, normally supplies the rules and the language list", "(premise: try/except ImportError order)",
          "(premise: try/except ImportError order; the installed PyPI 1.0.1 package differs from the repo folder, see the Code Shield column)", "T74 (r2)")
    K.repl(C, 4, "The repo CodeShield folder declares version \"0.0.1\"", [
        "• The repo CodeShield folder declares version \"0.0.1\" (CodeShield/pyproject.toml@172c1074:3) " + PR,
        "• The PyPI 1.0.1 sdist differs from the pinned CodeShield folder in nine Python files and the Kotlin generated files, with identical rule YAML and config files (see the Code Shield column, R4; premise: file-by-file comparison of the unpacked sdist " + CSB.strip("()") + " with the pin) " + INF],
        "T19 (r2)", kind="replace")
    K.delete(C, 4, "Equality of PyPI codeshield 1.0.1 with the repo code at the pin", "T19 (CORRECTION): the sdist was read; the open question is answered")
    K.ins_before(C, 4, "No backing model: the scanner and engine files import no machine-learning library",
        "• The scanner and detector source files import only standard-library modules, PyYAML and each other (import lines of code_shield_scanner.py, insecure_code_detector.py, insecure_patterns.py and oss.py at the pin); the Semgrep binary is run as a subprocess " + PR,
        "T90 (r2): documented import list; the 'so no model' inference stays below")
    # R5
    K.summary(C, 5,
        "Summary: **Block with score 1.0, or allow with 0.0.** The reason lists each issue with its description, CWE, line and severity. The scanner never returns warn or human review. Meta's latency figures differ by source; precision is 96% and recall 79% on a manual check. " + DOC,
        "T65 (r2): 'four' dropped")
    K.repl(C, 5, "The block threshold of 1.0 is passed to the base class but the scan code never compares",
        "• The block threshold of 1.0 is passed to the base class (code_shield_scanner.py@172c1074:38) and the file has no other use of `block_threshold`, so the scan code never compares against it " + PR,
        "T70 (r2): code facts documented", kind="replace")
    K.ins_after(C, 5, "The engine's own block, warn or ignore treatment is not used", [
        "• Semgrep issues carry the raw severity string from the Semgrep output (insecure_code_detector.py@172c1074:282), while the engine's treatment check compares with the Severity enum (codeshield.py@172c1074:90; see the Code Shield column, R5) " + PR,
        "• The generated Semgrep rule files use upper-case severities, so the engine's treatment for a Semgrep finding may never be BLOCK (premise: Semgrep echoes the rule severity string, which was not read) " + INF,
        '• The block reason is built as "(CWE-{issue.cwe_id})" (code_shield_scanner.py@172c1074:78-79) and rule files store ids such as "CWE-120" (rules/regex/c.yaml@172c1074:12), so the printed text may read "CWE-CWE-120" (premise: the two quoted lines) ' + INF,
        "• Two data oddities in the generated C Semgrep file: potential-command-injection (CWE-78) carries the message of the weak-PRNG rule, and vulnerable-strcpy has no cwe_id (_generated_/c_codeshield.json@172c1074) " + PR],
        "T69, T70 (r2): pointer bullets and the CWE prefix observation")
    K.sub(C, 5, "Precision and recall: \"CodeShield achieved a precision of 96% and a recall of 79%\"", "(arXiv 2505.03574 section 4.4)",
          "(arXiv 2505.03574 section 4.4; first reported in the CyberSecEval 3 paper section 5.2, which the LlamaFirewall paper cites)", "T66 (r2)")
    K.repl(C, 5, "Per-language precision and recall: the paper shows a figure",
        "• Per-language precision and recall: the paper gives a bar chart with 90% confidence bars for eight languages and no table of values (arXiv 2408.01605 Figure 18; repeated as Figure 3 in arXiv 2505.03574) " + DOC,
        "T72 (r2, with main's ruling: no by-eye values; the chart's existence and axis labels only)", kind="replace")
    K.sub(C, 5, "Latency, statement 1 (Code Shield README)", "Latency, statement 1 (Code Shield README)", "Latency, Code Shield README", "style 5 (r2)", kind="style")
    K.sub(C, 5, "Latency, statement 2 (LlamaFirewall docs)", "Latency, statement 2 (LlamaFirewall docs)", "Latency, LlamaFirewall docs", "style 5 (r2)", kind="style")
    K.sub(C, 5, "Latency, statement 3 (paper)", "Latency, statement 3 (paper)", "Latency, LlamaFirewall paper", "style 5 (r2)", kind="style")
    K.ins_after(C, 5, "Latency, LlamaFirewall paper", LAT5, "T65, T66 (r2): fifth latency source")
    K.sub(C, 5, "Latency, statement 4 (protections page)", "Latency, statement 4 (protections page)", "Latency, protections page", "style 5 (r2)", kind="style")
    K.repl(C, 5, "The four statements differ and each comes from Meta's internal production experience", LATDIFF_SCAN, "T65 (r2)", kind="replace")
    # R6
    K.summary(C, 6,
        "Summary: **A string of code, with the codeshield package and Semgrep installed.** The scanner needs Python 3.10 or later, scans eight languages by default and writes each scan to a temporary file. " + DOC,
        "T91 (r2): 'needs no key or model' and 'no size limit or timeout is set in code' rested on inferences and absences; the new Summary draws on documented bullets only")
    K.ins_after(C, 6, "codeshield dependencies: \"semgrep>1.68\" and \"pyyaml\"", PIN_BUL, "T75 (r2): dependency pin clash")
    K.repl(C, 6, "On the early-return paths in fast mode the temporary file may not be deleted", TMP_BULLETS, "T70 (r2)", kind="replace")
    # R7
    K.summary(C, 7,
        "Summary: **Minimum setup:** pip install llamafirewall, which pulls in codeshield and Semgrep, attach the Code Shield scanner type to the assistant role, and scan labelled snippets in the eight default languages. "
        "No key, model or gated access is needed. A bench could also check the language list and fast-mode behaviour on the installed codeshield version. " + INF,
        "R032 (r2): proposal wording")
    K.repl(C, 7, "Cover every default language with a case from each rule family",
        "• A bench could cover every default language with a case from each rule family, including Rust and PHP cases whose rule coverage differs (premise: the engine's analyser map) " + INF, "R032, T101", kind="style")
    K.repl(C, 7, "Include non-code prose, fenced code inside markdown",
        "• A bench could also include non-code prose, fenced code inside markdown, code inside a tool message and an insecure pattern only in a comment, to check the comment filter (premise: engine code) " + INF, "R032", kind="style")
    K.repl(C, 7, "Record the installed codeshield version and compare with the repo code",
        "• A bench could record the installed codeshield version, because the scanner imports the installed package first and the PyPI 1.0.1 package differs from the repo folder (premise: import order) " + INF, "R032, T74 (r2)", kind="style")
    K.repl(C, 7, "Expect the first scans to be slower where Semgrep runs",
        "• The first scans may be slower where Semgrep runs, and regex-only and Semgrep paths could be timed separately (premise: two-tier design) " + INF, "R032", kind="style")
    # R8
    K.summary(C, 8,
        "Summary: **Key open questions.** Which seven languages the seven-language statements mean, real latency by language, how the PyPI package behaves against the repo code, Rust and PHP rule coverage, and whether Semgrep findings can ever recommend blocking.",
        "T19, T64, T65 (r2)")
    K.repl(C, 8, "Which seven languages the \"7\" statements mean, and why the same documents also say eight",
        "• Which seven languages the \"7\" statements mean (checked the READMEs, docs page, both papers and the code; the paper figure shows eight, the code scans eight)", "T64 (r2)", kind="replace")
    K.repl(C, 8, "Whether PyPI codeshield 1.0.1 equals the repo code at the pin",
        "• Whether the PyPI 1.0.1 behaviour differs from the pinned code in ways that change scanner results (needs testing)", "T19 (r2)", kind="replace")
    K.repl(C, 8, "Rust is in the default scan list but the CODESHIELD use case enables no Rust rules of its own",
        "• Whether Rust and PHP are meant to run as they do (Rust gets only the language-agnostic regex rules under CODESHIELD; PHP has Semgrep rules that the analyser map never runs; nothing in the repo states the intent; needs testing)", "T68 (r2)", kind="replace")
    K.repl(C, 8, "Whether the \"over 50\" CWE claim holds for the rules enabled in this scanner's use case",
        "• Whether the \"over 50\" CWE claim holds for the rules enabled in this scanner's use case (a count of distinct cwe_id values in the enabled rules gives 46; a rule-by-rule check would confirm)", "T67 (r2)", kind="replace")
    # R9
    for u in ("https://files.pythonhosted.org/packages/dd/0e/cb79d48ba05eda459a5a2e90b6056019cf7f41441cdee2a17e8dd63e5502/codeshield-1.0.1.tar.gz",
              "https://pypi.org/project/codeshield/",
              "https://arxiv.org/html/2408.01605",
              PGB + "CodeShield/codeshield.py",
              PGB + "CodeShield/insecure_code_detector/insecure_patterns.py",
              PGB + "CodeShield/insecure_code_detector/rules/regex/c.yaml",
              PGB + "CodeShield/insecure_code_detector/rules/semgrep/_generated_/c_codeshield.json",
              PGB + "CybersecurityBenchmarks/requirements.txt"):
        K.add_url(C, u, "T19, T64, T66, T69, T70, T75: page or file cited in R2 to R6")
    K.summary(C, 9, "Summary: LlamaFirewall and Code Shield source files, README and docs pages in the PurpleLlama repo, the PyPI index and sdist, the Meta protections page, and the two Meta papers.",
              "R9 Summary lists the new source kinds")
