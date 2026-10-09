"""Inventory edits (purplellama_inventory.md, blocks a to h)."""
import re
import merge_lib as L

PRL = "[Documented: repo meta-llama/PurpleLlama@172c1074]"
DOC = "[Documented]"
INF = "[Inferred]"
ND = "[Not disclosed]"
TBV = "[To be verified]"
G86 = "[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]"
PGB = "https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/"
CBB = "https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb030f92d0e99227e57e9a1123af1f9532/getting-started/responsible_ai/prompt_guard/"
CSDIST = "https://files.pythonhosted.org/packages/dd/0e/cb79d48ba05eda459a5a2e90b6056019cf7f41441cdee2a17e8dd63e5502/codeshield-1.0.1.tar.gz"
LFDIST = "https://files.pythonhosted.org/packages/70/f5/9dbd3b0a74c11323d967b0e1210a9fac0de068abc0c2e5dc08a6ee2094a5/llamafirewall-1.0.3.tar.gz"
TOGO = "Together lists this default model as removed from serverless inference (2026-03-31) [Documented] (Together deprecations page, not Meta docs, read 2026-10-09)"
CSEARCH = "(searched LlamaFirewall/src, the README and the docs pages for experimental)"
CS_PREM = "[Inferred] (premise: counted by parsing the file)"
CS_PREMS = "[Inferred] (premise: counted by parsing the files)"


def header_sub(V, blk, old, new, reason):
    s, e = V.block_range(blk)
    i = next(i for i in range(s, e) if V.lines[i].startswith("|"))
    assert old in V.lines[i]
    before = V.lines[i]
    V.lines[i] = before.replace(old, new)
    L._log("inv", "INV (%s) table header" % blk, "edit", old, new, reason)


def setcell(V, blk, key, col, new, reason, kind="edit"):
    old = V.cell_get(blk, key, col)
    V.sub(blk, key, col, old, new, reason, kind=kind)


def apply(V):
    S = V.sub
    # ------------------------------------------------------------ title, scope paragraph
    V.para_sub("# Purple Llama inventory (draft for sheet 3x)", "# Purple Llama inventory (final, sheet 3x)",
               "T80: draft marker removed; the letter is assigned at P8")
    V.para_sub("Covered-by values are the option B headers of the brief (per-tool prefixes Prompt Guard 2, LlamaFirewall, Code Shield); if CP1 picks option A only these cells and the column headings change.",
               "Covered-by values are the exact Table 3 headers (per-tool prefixes Prompt Guard 2, LlamaFirewall, Code Shield).",
               "T1 (closed): the prefix choice is made; the CP1 alternative is not carried")
    V.para_sub("the inventory-only marker (R011) is for", "the inventory-only marker is for", "style 3: ruling id removed")
    V.para_sub("(checked git ls-remote --tags and the file list of the clone)", "(checked git ls-remote --tags and the repository file list)",
               "style 3: session wording")
    V.para_sub("Code facts were read from a shallow clone and not run.", "Code facts were read at the pinned commit and not run.", "style 3: session wording")
    V.para_sub("whether the PyPI sdists equal the repo code at the pin is [To be verified].",
               "the llamafirewall 1.0.3 sdist and the codeshield 1.0.1 sdist were compared with the pin and differ from it (block a) [Inferred] (premise: file-by-file comparison of the unpacked sdists, read 2026-10-09); sdist facts in the cells are [Documented] with the sdist name, sha256 and read date in plain text.",
               "T19, T20 (r1 and r2); main ruling on the label form of PyPI sdist facts")
    V.para_sub("Hugging Face revisions come from the Hugging Face model API (HTTP 200, gated manual for all three repos, read 2026-10-09)",
               "Hugging Face revisions come from public Hugging Face Hub model metadata (HTTP 200, gated manual for all three repos, read 2026-10-09)",
               "T105: source phrase (main ruling: public vendor-org metadata is allowed evidence)")
    V.para_sub("the model card bodies of the gated repos are not readable, so model-card facts are cited from the card files in the repo at the pin.",
               "model-card facts are cited from the card files in the repo at the pin; the public gate pages of the 86M and 22M repos show the same card text [Inferred] (premise: sentence-level comparison of the gate page text with the repo card, 2026-10-09).",
               "Supplementary 1 (CORRECTION, r1): the card text is readable on the public gate page")
    V.para_sub("The LlamaFirewall docs site (meta-llama.github.io/PurpleLlama/LlamaFirewall/docs) is a build of LlamaFirewall/website/docs; where a passage was confirmed in the pinned file the cell cites the .md blob.",
               "The LlamaFirewall docs site (meta-llama.github.io/PurpleLlama/LlamaFirewall/docs) is built from LlamaFirewall/website by .github/workflows/sites_deployment.yml on every push to main [Documented: repo meta-llama/PurpleLlama@172c1074]; passages of seven pages read on 2026-10-09 match the pinned .md files, so the site is cited at the pin through those files [Documented]. The CyberSecEval site is built the same way from CybersecurityBenchmarks/website [Documented: repo meta-llama/PurpleLlama@172c1074].",
               "T22 (r1 and r2): deploy source found in the pinned repo")
    V.para_sub("Names: Meta writes Llama Prompt Guard 2 (model card)",
               "Pages of Together, Semgrep, CrowdStrike, ARVO, Python and Hugging Face documentation are third-party sources, cited only for availability, licence and terms facts and marked not Meta docs where used. Names: Meta writes Llama Prompt Guard 2 (model card)",
               "R007 item 1, R019: third-party sources are attributed once in the scope paragraph")

    # ------------------------------------------------------------ (a) components
    a = "a"
    S(a, "llamafirewall package", "Version or revision read",
      "PyPI latest file 1.0.3 [Documented] (simple index listing, observed 2026-10-09); sdist equals repo code [To be verified]",
      "PyPI latest file 1.0.3 of 13 releases [Documented] (simple index listing, observed 2026-10-09); the PyPI sdist llamafirewall-1.0.3 (sha256 54fe55c8, read 2026-10-09) has promptguard_utils.py with HfFolder.get_token and no fix_mistral_regex [Documented]; the pin uses get_token and fix_mistral_regex=True [Documented: repo meta-llama/PurpleLlama@172c1074]; the sdist differs from the pin in promptguard_utils.py, cli/configure.py and scanners/__init__.py, and in five files by blank lines or comments only [Inferred] (premise: file-by-file comparison of the unpacked sdist with the pin); the version string 1.0.3 was set on 2025-05-28 and the pin is later code [Documented: repo meta-llama/PurpleLlama@172c1074]",
      "T20 (r1 and r2): sdist read and compared; sdist facts [Documented] with plain-text hint, comparison [Inferred] (main ruling)")
    V.url_add(a, "llamafirewall package", ["https://pypi.org/project/llamafirewall/", LFDIST], "T20: sdist and project page cited")
    S(a, "PromptGuard scanner", "Status",
      "Available [Inferred] (premise: not under scanners/experimental and not marked experimental in code or docs)",
      "Available [Documented: repo meta-llama/PurpleLlama@172c1074] (LlamaFirewall/README.md line 30: Fast, production-ready, easy to update with new patterns); not marked experimental [Not disclosed] (searched LlamaFirewall/src, the README and the docs pages for experimental; only the experimental folder, the CustomCheckScanner docstring and the AlignmentCheck pages match)",
      "T76 (r1 search, r2 README quote): premise replaced by what the README states and what was searched")
    V.append(a, "AlignmentCheck scanner", "Backing model or engine", TOGO, "T46 (r1 and r2)")
    S(a, "AlignmentCheck scanner", "Status", "(PAPER section 4.2)", "(PAPER section 4.2, Figure 2 caption)", "T103: locator of the quoted text", kind="style")
    S(a, "CodeShield scanner", "Status", "Available [Inferred] (premise: not marked experimental)",
      "Available [Documented: repo meta-llama/PurpleLlama@172c1074] (listed as a primary component, LlamaFirewall/README.md line 44); no maturity statement [Not disclosed] (checked the README, docs pages and code docstrings)",
      "T76 (r2)")
    S(a, "Regex scanner", "Status", "Available [Inferred] (premise: not marked experimental)",
      "Available [Documented: repo meta-llama/PurpleLlama@172c1074] (listed as a primary component, LlamaFirewall/README.md line 38); no maturity statement [Not disclosed] (checked the README, docs pages and code docstrings)",
      "T76 (r2)")
    S(a, "Hidden ASCII scanner", "Status", "Available [Inferred] (premise: not marked experimental in code; no docs page describes it)",
      "Available [Inferred] (premise: in the scanners package, not under scanners/experimental, tested in tests/test_hidden_ascii_scanner.py; not listed in the README components); not marked experimental [Not disclosed] " + CSEARCH,
      "T76 (r1 and r2)")
    S(a, "codeshield package", "Version or revision read",
      "; equality of PyPI 1.0.1 with the repo code is [To be verified]",
      "; the PyPI sdist codeshield-1.0.1 (sha256 61866b92, read 2026-10-09) differs from the pinned folder in nine Python files (for example Kotlin regex only, no Semgrep job cap, string enums) while the rule YAML files and config.yaml are identical [Inferred] (premise: file-by-file comparison of the unpacked sdist with the pin)",
      "T19 (CORRECTION, r2)")
    V.url_add(a, "codeshield package", [CSDIST], "T19: sdist cited")
    S(a, "CyberSecEval 4", "Version or revision read",
      "no CyberSecEval 4 paper id located [To be verified]",
      "no CyberSecEval 4 paper located (checked an arXiv search for CyberSecEval with 11 results, the repo README, the docs-site intro and the dev.meta.ai page) [Not disclosed]; 98 commits to the folder since 2025-06-12 [Inferred] (premise: counted from the git history)",
      "T81 (r2): one label for the same fact across files; T84 (r2)")
    S(a, "CyberSecEval 4", "Backing model or engine", "evaluated on its own evaluation-tooling sheet (proposed 3j), not here",
      "evaluated on the CyberSecEval evaluation-tooling sheet, not here", "T80: sheet letter wording")

    # ------------------------------------------------------------ (b) scanner catalogue
    b = "b"
    S(b, "PROMPT_GUARD", "Mechanism", "(conflict, code stronger)", "(conflict, code stronger; pinned file and live docs page both read 2026-10-09)", "T43 (r1)")
    S(b, "PROMPT_GUARD", "Default block threshold", "(checked the card, README, dev.meta.ai page and LFD scanner page)",
      "(checked the card, README, dev.meta.ai page, LFD scanner page, paper and the llama-cookbook files)", "T26 (r1)")
    S(b, "PROMPT_GUARD", "Maturity", "Not marked experimental in code or docs [Inferred]",
      "Described as production-ready in the README [Documented: repo meta-llama/PurpleLlama@172c1074]; not marked experimental [Not disclosed] " + CSEARCH, "T76 (r1 and r2)")
    V.append(b, "AGENT_ALIGNMENT", "External dependency", TOGO, "T46 (r2)")
    S(b, "CODE_SHIELD", "Maturity", "Not marked experimental in code or docs [Inferred]",
      "Listed as a primary component; no maturity statement [Not disclosed] (checked the README, docs pages and docstrings)", "T76 (r2)")
    S(b, "REGEX", "Maturity", "Not marked experimental in code; the docs tutorial lives under tutorials, not under scanners",
      "Listed as a primary component in the README [Documented: repo meta-llama/PurpleLlama@172c1074] (README line 38); no maturity statement [Not disclosed] (checked the README, docs pages and docstrings); the docs tutorial lives under tutorials, not under scanners",
      "T76 (r2)")
    S(b, "HIDDEN_ASCII", "Maturity", "Not marked experimental in code [Inferred]",
      "Not marked experimental in code; not listed in the README [Inferred] (premise: searched LlamaFirewall/src, the README and the docs pages for experimental)", "T76 (r2)")
    V.append(b, "CustomCheckScanner (class", "External dependency", TOGO, "T46 (r2)")
    V.append(b, "Registered custom scanners", "Mechanism",
             "The docs page has had no commit since the 2025-04-29 release commit that also added the registry [Documented: repo meta-llama/PurpleLlama@172c1074]", "T59 (r2)")

    # ------------------------------------------------------------ (c) roles
    c = "c"
    header_sub(V, c, "Direction under R002", "Direction (input, output or trace side)", "style 3: ruling id removed from a column heading")
    V.para_sub("Default (CP1 question Q-C): one column per scanner with the roles listed here in Detail; the same scanner class can be attached to any role [Inferred]",
               "Each scanner has one Table 3 column and the roles listed here are where it can be attached; the same scanner class can be attached to any role [Inferred]",
               "T4 (closed), style 3: checkpoint wording removed")
    V.para_sub("Message.tool_calls exists, but no scanner reads it, so tool-call arguments are not scanned [Inferred] (premise: grep of src for tool_calls).",
               "Message.tool_calls exists and appears in src only in llamafirewall_data_types.py (lines 54, 77, 79) [Documented: repo meta-llama/PurpleLlama@172c1074]; scanning of tool-call arguments [Not disclosed] (searched the whole repository at the pin, the README, docs pages and paper; only the field definitions and one docs tutorial match); so tool-call arguments are not scanned unless they appear in the content [Inferred].",
               "T45 (r1 and r2): the search is named; the absence is Not disclosed")
    setcell(V, c, "No config (default dictionary)||SYSTEM", "Covered by",
            "LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner); LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner); LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner)",
            "T77 (r2): list a header only where that column's Detail names the role (PromptGuard, Regex, Hidden ASCII name SYSTEM; AlignmentCheck and CodeShield do not)", kind="covered")
    setcell(V, c, "No config (default dictionary)||MEMORY", "Covered by",
            "LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner); LlamaFirewall: Output-level insecure-code detection (CodeShield scanner); LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner); LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner)",
            "T77 (r2): PromptGuard, CodeShield, Regex and Hidden ASCII name MEMORY; AlignmentCheck names it only as an empty default", kind="covered")
    S(c, "Predefined use case CHAT_BOT||SYSTEM", "Scanners configured", "(conflict, code stronger)", "(conflict, code stronger; pinned file and live docs page both read 2026-10-09)", "T43 (r1)")

    # ------------------------------------------------------------ (d) language matrix
    d = "d"
    V.para_sub("Meta does not say which 7.",
               "Meta's texts do not say which 7 [Not disclosed] (searched every .md and .mdx file under LlamaFirewall/website/docs and CodeShield/, the text of both papers and the protections page; no list of seven).",
               "T64 (r2)")
    V.para_sub("on the llama.com protections page [Documented], and in the paper section 4.4 (seven), where the same paper also says 8 and eight [Documented]",
               "on the llama.com protections page [Documented], in the CyberSecEval 3 paper section 5.2 [Documented] and in the LlamaFirewall paper section 4.4 (seven), where the same paper also says 8 and eight [Documented]; the per-language chart in the CyberSecEval 3 paper (Figure 18) and in the LlamaFirewall paper (Figure 3) has eight language labels [Documented]",
               "T64, T66 (r2)")
    V.para_sub("Counts in this table were made from the files at the pin by listing yaml and JSON rule files; the codeshield use case is",
               "Counts in this table were made by parsing the files at the pin and are labelled [Inferred]; the codeshield use case is", "T98 (r2)")
    V.para_sub("(codeshield.py line 43) [Documented: repo meta-llama/PurpleLlama@172c1074].",
               "(codeshield.py line 43) [Documented: repo meta-llama/PurpleLlama@172c1074]. The analyzer map described here is the pinned one; the PyPI 1.0.1 sdist maps Kotlin to regex only [Documented] (PyPI sdist codeshield-1.0.1, read 2026-10-09).",
               "T19 (r2)")

    keys = ["=C", "=CPP", "=CSHARP", "=HACK", "=JAVA", "=JAVASCRIPT", "=KOTLIN", "=OBJECTIVE_C", "=OBJECTIVE_CPP", "=PHP", "=PYTHON", "=RUBY", "=RUST", "=SWIFT", "=XML", "=LANGUAGE_AGNOSTIC"]
    manual = {
        ("=HACK", "Regex rule file"): "regex/hack.yaml is present [Documented: repo meta-llama/PurpleLlama@172c1074]; it holds no patterns (loads as none) " + CS_PREM,
        ("=CPP", "Regex rule file"): "regex/cpp.yaml is present [Documented: repo meta-llama/PurpleLlama@172c1074]; 3 patterns, 2 enabled for codeshield " + CS_PREM + "; load() also adds the C rules (insecure_patterns.py lines 49-50) [Documented: repo meta-llama/PurpleLlama@172c1074]",
        ("=CPP", "Semgrep rule folder"): "No cpp folder [Documented: repo meta-llama/PurpleLlama@172c1074]; generated cpp_codeshield.json holds 16 rules and cpp_cyberseceval.json 19 " + CS_PREMS + "; the generated cpp_codeshield.json is the file Semgrep uses for C++ (insecure_code_detector.py lines 314-330) [Documented: repo meta-llama/PurpleLlama@172c1074]; config.yaml lists an empty Semgrep rule list for cpp [Documented: repo meta-llama/PurpleLlama@172c1074]",
        ("=KOTLIN", "Semgrep rule folder"): "No kotlin folder [Documented: repo meta-llama/PurpleLlama@172c1074]; generated kotlin_codeshield.json and kotlin_cyberseceval.json hold 0 rules " + CS_PREMS,
        ("=KOTLIN", "Regex rule file"): "No kotlin.yaml in regex/; only the language-agnostic file is added by load() [Documented: repo meta-llama/PurpleLlama@172c1074] (insecure_patterns.py lines 36-62)",
        ("=RUST", "Regex rule file"): "regex/rust.yaml is present [Documented: repo meta-llama/PurpleLlama@172c1074]; 13 patterns, 0 enabled for codeshield (config.yaml lists an empty regex rule list for rust) " + CS_PREM + "; the language-agnostic rules still apply [Documented: repo meta-llama/PurpleLlama@172c1074] (insecure_patterns.py lines 36-62)",
        ("=PHP", "In LANGUAGE_ANALYZER_MAP"): "REGEX only (line 63), although Semgrep rules exist for PHP; the Semgrep branch checks the map, so those rules are not run by analyze() [Documented: repo meta-llama/PurpleLlama@172c1074] (insecure_code_detector.py lines 63 and 132-134)",
    }
    for k in keys:
        for col in ("Regex rule file", "Semgrep rule folder"):
            cur = V.cell_get(d, k, col)
            if (k, col) in manual:
                new = manual[(k, col)]
            else:
                new = cur
                new = new.replace(" (counted from the file) [Documented: repo meta-llama/PurpleLlama@172c1074]", " " + CS_PREM)
                new = new.replace("(counted from the file)", CS_PREMS if col == "Semgrep rule folder" else CS_PREM)
                m = re.match(r"^(regex/[a-z_]+\.yaml), (.*)$", new)
                if m:
                    new = "%s is present [Documented: repo meta-llama/PurpleLlama@172c1074]; %s" % (m.group(1), m.group(2))
                m = re.match(r"^(semgrep/[a-z]+), (\d+ yaml files;.*)$", new)
                if m:
                    new = "%s is a folder [Documented: repo meta-llama/PurpleLlama@172c1074]; %s" % (m.group(1), m.group(2))
            if new != cur:
                V.sub(d, k, col, cur, new, "T98 (r2): own counts are [Inferred] (counted by parsing the file); existence stays [Documented: repo]" if (k, col) not in manual else
                      "T98, T68 (r2): counts [Inferred]; code-explicit facts [Documented: repo]", kind="hygiene")
    cur = V.cell_get(d, "=PHP", "In LANGUAGE_ANALYZER_MAP")
    if cur != manual[("=PHP", "In LANGUAGE_ANALYZER_MAP")]:
        V.sub(d, "=PHP", "In LANGUAGE_ANALYZER_MAP", cur, manual[("=PHP", "In LANGUAGE_ANALYZER_MAP")],
              "T68 (r2): the code is explicit (map entry and branch condition), so the label is Documented: repo", kind="edit")
    V.append(d, "=KOTLIN", "In LANGUAGE_ANALYZER_MAP",
             "PyPI 1.0.1 sdist: REGEX only (insecure_code_detector.py line 60) [Documented] (PyPI sdist codeshield-1.0.1, read 2026-10-09)", "T19 (r2)")
    OLDN = "(checked CodeShield/README.md, the ICD README, the rules README, LlamaFirewall/README.md, LFD code-shield.md and the codeshield tutorial; no mention)"
    NEWN = "(searched every .md and .mdx file under LlamaFirewall/website/docs and CodeShield/; no mention)"
    for k in ("=HACK", "=KOTLIN", "=OBJECTIVE_C", "=OBJECTIVE_CPP", "=RUBY", "=SWIFT", "=XML"):
        S(d, k, "Named in READMEs and docs", OLDN, NEWN, "T78 (r2): the search covers every docs file, not six", kind="edit")
    S(d, "=LANGUAGE_AGNOSTIC", "Named in READMEs and docs", "(checked the same six docs files)", "(searched the same files; no mention)", "T78 (r2)")
    for k in ("=HACK", "=OBJECTIVE_CPP"):
        S(d, k, "Named in READMEs and docs", "; no unit test file found in tests/",
          "; no unit test for this language [Not disclosed] (checked the 16-file tests/ listing and searched it for HACK and OBJECTIVE_CPP)", "T78 (r2): unlabelled remark labelled")

    # ------------------------------------------------------------ (e) integration paths
    e = "e"
    S(e, "Hugging Face gated-access request", "Caveats",
      "Not requested during research (read-only rule); the gate page for 22M was read and carries the same licence line [Documented]. Approval time [Not disclosed] (checked the gate pages)",
      "The gate page for 22M was read and carries the same licence line [Documented]. The form asks for first and last name, date of birth, country, affiliation and job title, with instruction text asking for the full legal name, date of birth and full organisation name with all corporate identifiers " + G86 + ". Approval time [Not disclosed] (checked the gate pages and the metadata of the 86M, 22M and v1 repos)",
      "T10, T100 (r1): form fields read from the Hub metadata; process wording removed")
    S(e, "pip install llamafirewall", "Caveats",
      "The prerequisite line links a Llama 3.1 collection, not the Prompt Guard 2 repo [Documented: repo meta-llama/PurpleLlama@172c1074]",
      "The prerequisite line links a Llama 3.1 collection, not the Prompt Guard 2 repo [Documented: repo meta-llama/PurpleLlama@172c1074]; that collection was last updated Dec 13, 2024 and lists Prompt-Guard-86M [Documented] (collection page, read 2026-10-09)",
      "T41 (r1)")
    S(e, "Automatic model download", "Caveats",
      "Behaviour in offline or air-gapped use [Not disclosed] (checked the README and LFD pages)",
      "The README's manual setup says to preload the model to the local cache directory or to log in [Documented: repo meta-llama/PurpleLlama@172c1074]; offline use with a pre-populated folder [Not disclosed] (checked the README and LFD pages for any description of the folder layout)",
      "T42 (CORRECTION, r1)")
    S(e, "Code Shield through LlamaFirewall", "Caveats",
      "Which codeshield version the PyPI 1.0.1 release contains relative to the repo code [To be verified]",
      "After pip install the PyPI codeshield 1.0.1 code runs, not the repo folder; it differs from the pin in nine Python files [Inferred] (premise: sdist read and compared; import order in code_shield_scanner.py lines 9-19)",
      "T19 (r2)")
    S(e, "Together API", "Caveats",
      "the Together terms of service are Together's, not Meta documentation, and state that models may carry their own terms and that zero data retention is a user setting [Documented] (Together terms of service, read 2026-10-09). Testing sends agent traces to a third party",
      "Together's terms of service (not Meta docs, read 2026-10-09) state that models may carry their own terms [Documented]; section 4 bars sending financial or medical information or sensitive personal data (for example social security numbers, driver's licence numbers, birth dates, bank account, passport or visa numbers and card numbers) [Documented]; zero data retention is an organisation setting that is not enabled by default, without it Together stores prompts and responses and may use them for product improvements, and training use is a separate opt-in, off by default [Documented] (Together docs, not Meta docs, read 2026-10-09). Together lists the default Llama 4 Maverick model as removed from serverless inference; the Llama 3.3 70B Instruct Turbo default of PIICheck is on its serverless table at $1.04 per 1M input and output tokens [Documented] (Together docs, not Meta docs, read 2026-10-09). Testing sends agent traces and scanned text to a third party [Documented: repo meta-llama/PurpleLlama@172c1074]",
      "T11, T12, T46, T48 (r1 and r2, merged): clauses quoted from Together's own pages; the old cell omitted section 4 and the defaults")
    S(e, "llama-cookbook tutorials", "Needs", "Not read beyond the links",
      "Read at llama-cookbook@2f22a9eb: inference.py (chunked scoring, maximum chunk score), prompt_guard_tutorial.ipynb and the folder README [Documented: repo meta-llama/llama-cookbook@2f22a9eb]", "T23 (r1)")
    S(e, "llama-cookbook tutorials", "Caveats",
      "The cookbook files are in another Meta repository and were not read; their content [To be verified]. The Prompt Guard 2 README also links facebookresearch/llama-recipes, which was not read [To be verified]",
      "The Prompt Guard 2 README links facebookresearch/llama-recipes, which redirects (HTTP 301) to meta-llama/llama-cookbook [Documented] (observed 2026-10-09). The docs page example matches the tutorial helper, not inference.py [Documented: repo meta-llama/llama-cookbook@2f22a9eb]", "T23 (r1)")
    S(e, "llama-cookbook tutorials", "Source URL",
      "https://github.com/meta-llama/llama-cookbook/blob/main/getting-started/responsible_ai/prompt_guard/prompt_guard_tutorial.ipynb ; https://github.com/meta-llama/llama-cookbook/blob/main/getting-started/responsible_ai/prompt_guard/inference.py",
      CBB + "prompt_guard_tutorial.ipynb ; " + CBB + "inference.py", "T104 (r1): blob/main URLs replaced by pinned URLs")

    # ------------------------------------------------------------ (f) licences
    f = "f"
    V.append(f, "Prompt Guard 2 (86M and 22M)", "Licence as stated",
             "Additional Commercial Terms apply above 700 million monthly active users on the Llama 4 release date (86M/LICENSE line 22) " + PRL, "T7 (r1)")
    S(f, "Prompt Guard 2 (86M and 22M)", "Gating or acceptable-use terms",
      "the gate asks for a full legal name, date of birth and full organisation name with corporate identifiers [Documented] (86M gate page, observed 2026-10-09)",
      "the gate asks for first and last name, date of birth, country, affiliation and job title, with instruction text asking for the full legal name, date of birth and full organisation name with all corporate identifiers " + G86,
      "T10 (r1)")
    V.append(f, "Prompt Guard 2 (86M and 22M)", "Gating or acceptable-use terms",
             "Section 1 item h of the AUP bars intentionally circumventing or removing usage restrictions or other safety measures (86M/USE_POLICY.md line 37) " + PRL + ". No clause names testing, evaluation or red-teaming [Not disclosed] (searched the licence and policy text)",
             "T6 (r1): clause recorded; the legal question stays open in the columns")
    S(f, "Prompt Guard 2 (86M and 22M)", "Conflict or note", "Which text governs a given download is a legal question [To be verified]",
      "The gate pages of both repos display the Llama 4 Community License Agreement [Documented] (gate pages, observed 2026-10-09). Which text prevails when the README link and the folder files differ [Not disclosed] (checked the README, the root licence table and the gate pages)",
      "T8 (r1)")
    V.append(f, "Prompt Guard 1 (legacy)", "Gating or acceptable-use terms",
             "the Hugging Face repo file list does include USE_POLICY.md [Documented: repo meta-llama/Prompt-Guard-86M@1209add6] (Hub metadata, observed 2026-10-09)", "T9 (r1)")
    S(f, "LlamaFirewall", "Gating or acceptable-use terms",
      "None for the code. The default PromptGuard scanner downloads the gated Prompt Guard 2 86M model, so the Llama 4 terms apply to that model [Inferred] (premise: promptguard_utils.py line 40 names the gated repo)",
      "None for the code. The default PromptGuard scanner downloads meta-llama/Llama-Prompt-Guard-2-86M (promptguard_utils.py line 40) [Documented: repo meta-llama/PurpleLlama@172c1074]; that repo is under the Llama 4 Community License (license_name llama4) " + G86 + "; so a default install combines MIT code with a Llama 4 licensed model [Inferred] (premise: the two facts). Meta states the combined licence terms nowhere [Not disclosed] (checked LlamaFirewall/README.md, the PyPI package metadata and the root README licence table)",
      "T17 (r1)")
    S(f, "CyberSecEval (Cyber", "Conflict or note", "whose terms are the providers' own [Inferred]",
      "whose terms are the providers' own; those terms were not read for OpenAI, Anthropic and Google [To be verified]", "T16 (r1)")
    V.append(f, "CyberSecEval (Cyber", "Conflict or note",
             "CybersecurityBenchmarks/website/docs/LICENSE.md holds the Meta Llama 3 Community License Agreement (Version Release Date April 18, 2024) and the docs site publishes it, while CybersecurityBenchmarks/LICENSE is MIT " + PRL +
             "; CyberSOCEval report data is CC BY-ND 4.0 and Hybrid Analysis data CC BY-SA 4.0 [Documented: repo CrowdStrike/CyberSOCEval_data@ce7daa5b] (CrowdStrike's repo, not Meta docs); the ARVO-Meta repository is BSD 2-Clause [Documented: repo n132/ARVO-Meta@51cfeab5] (not Meta docs); the datasets also hold CAPTCHA images whose source licence is not stated [Not disclosed] (checked the dataset card)",
             "T15, T16 (r1): licence facts for the third-party data")
    V.url_add(f, "CyberSecEval (Cyber", [PGB + "CybersecurityBenchmarks/website/docs/LICENSE.md", "https://meta-llama.github.io/PurpleLlama/CyberSecEval/docs/LICENSE",
                                       "https://github.com/CrowdStrike/CyberSOCEval_data/blob/ce7daa5bc7da51559ca97476d2277be02631783e/data/crowdstrike-reports/LICENSE.md",
                                       "https://github.com/CrowdStrike/CyberSOCEval_data/blob/ce7daa5bc7da51559ca97476d2277be02631783e/data/hybrid-analysis/LICENSE.md",
                                       "https://github.com/n132/ARVO-Meta/blob/51cfeab5/LICENSE"], "T15 (r1): licence files cited")
    S(f, "Semgrep (dependency", "Licence as stated",
      "The Semgrep repository LICENSE file on its develop branch is the GNU Lesser General Public License, Version 2.1 [Documented] (Semgrep's own repository, not Meta docs; read 2026-10-09, unpinned)",
      "The Semgrep repository LICENSE is the GNU Lesser General Public License, Version 2.1 at tag v1.69.0 [Documented: repo semgrep/semgrep@v1.69.0] and at v1.180.0, the newest tag on 2026-10-09 [Documented: repo semgrep/semgrep@v1.180.0] (Semgrep's own repository, not Meta docs)",
      "T14 (r1): pinned at release tags")
    S(f, "Semgrep (dependency", "Gating or acceptable-use terms",
      "Not Meta terms; Semgrep's own terms for its rules and registry are not read here [To be verified]",
      "Not Meta terms. Code Shield passes rule files from its own folder to Semgrep (insecure_code_detector.py lines 314-329; oss.py lines 24-25, 65-75), so Semgrep Registry rules are not loaded [Inferred] (premise: the config argument is a local path). Semgrep's separate rules licence says You may use the rules only for your own internal business purposes [Documented] (semgrep.dev/legal/rules-license, not Meta docs, read 2026-10-09)",
      "T14 (r1)")
    S(f, "Semgrep (dependency", "Conflict or note",
      "whether the LGPL has consequences for a test bench that installs codeshield is a licensing question [To be verified]",
      "whether the LGPL has consequences for a test bench that installs codeshield is a licensing question for the project owner [Not disclosed] (neither Meta nor Semgrep addresses it in the files checked); CyberSecEval's requirements pin semgrep==1.51.0 [Documented: repo meta-llama/PurpleLlama@172c1074] (CybersecurityBenchmarks/requirements.txt line 6)",
      "T14 (r1), T75 (r2)")
    S(f, "Semgrep (dependency", "Source URL", "https://github.com/semgrep/semgrep/blob/develop/LICENSE",
      "https://github.com/semgrep/semgrep/blob/v1.69.0/LICENSE ; https://github.com/semgrep/semgrep/blob/v1.180.0/LICENSE ; https://semgrep.dev/legal/rules-license ; " + PGB + "CybersecurityBenchmarks/requirements.txt", "T14, T75 (r1, r2): pinned URL; rules licence and requirements added")
    S(f, "Together-hosted models", "Licence as stated",
      "the Llama 4 Maverick and Llama 3.3 model licences are separate Llama licences and were not read here [To be verified]",
      "Meta's Hugging Face records give the Llama 4 Community License for Llama-4-Maverick-17B-128E-Instruct-FP8 (license_name llama4) [Documented: repo meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8@94125d2b] and the Llama 3.3 Community License for Llama-3.3-70B-Instruct [Documented: repo meta-llama/Llama-3.3-70B-Instruct@6f6073b4]; both gate pages carry a 700 million monthly-active-user clause [Documented]. The licence of the Together-served builds (the Turbo build is not a Meta Hub repo) [Not disclosed] (checked the Together model page and terms)",
      "T13 (r1)")
    S(f, "Together-hosted models", "Gating or acceptable-use terms",
      "Together terms: a user setting can enable Zero Data Retention, under which data and outputs are not stored, retained, or used for model training [Documented] (Together terms of service, not Meta docs). Meta files do not mention it [Not disclosed] (checked README, docs pages and code)",
      "Zero Data Retention is an organisation setting that is not enabled by default; without it Together stores prompts and responses and may use them for product improvements; training use is a separate opt-in, off by default [Documented] (Together docs, not Meta docs, read 2026-10-09). Section 4 of the Together terms bars sending financial or medical information or sensitive personal data (for example social security numbers, driver's licence numbers, birth dates, bank account, passport or visa numbers and card numbers) [Documented] (Together terms of service, not Meta docs, read 2026-10-09). Meta files do not mention these terms [Not disclosed] (checked README, docs pages and code)",
      "T11, T12 (r1): the old cell omitted section 4 and the account defaults")
    S(f, "Together-hosted models", "Conflict or note", "data-protection implications for the bench are a decision for the project owner",
      "a bench could use synthetic data only (suggested)", "T11 (r1), R032: proposal wording")
    V.url_add(f, "Together-hosted models", ["https://docs.together.ai/docs/zero-data-retention", "https://docs.together.ai/docs/privacy-and-security",
                                           "https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8", "https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct"],
              "T11, T12, T13 (r1): pages cited")

    # ------------------------------------------------------------ (g) metrics
    g = "g"
    V.para_sub("The latency statements below are four different statements, not one figure.",
               "The CodeShield latency statements below come from five Meta sources in four rows (the two papers give the same figures) and do not agree, so Meta gives no single latency figure.",
               "T65 (r2): CSE3 merged into statement 3; the block keeps 12 rows (main ruling)")
    V.append(g, "=Prompt Guard 2 86M", "Value", "The card text on the Hugging Face page also prints .998 [Documented] (HF 86M page, observed 2026-10-09)", "T28 (r1)")
    S(g, "=Prompt Guard 1 (comparator only)", "Benchmark and conditions", "comparator rows are not Summary material", "comparator row only", "style 3: drafting remark", kind="style")
    S(g, "AlignmentCheck (paper)||Recall", "Benchmark and conditions",
      "(the paper points to a Hugging Face dataset named facebook/llamafirewall-alignmentcheck-evals, not read) [Documented]",
      "(the paper links the Hugging Face dataset facebook/llamafirewall-alignmentcheck-evals [Documented]; its card says 577 test cases, six model responses each, while the paper says 600 scenarios, 300 benign and 300 malicious [Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9])",
      "T24 (CORRECTION, r1 and r2)")
    S(g, "CodeShield latency statement 3", "Component", "CodeShield latency statement 3: LlamaFirewall paper",
      "CodeShield latency statement 3: LlamaFirewall paper and CyberSecEval 3 paper", "T65 (r2): the two papers give identical figures; one row keeps the block at 12 rows (main ruling)")
    V.append(g, "CodeShield latency statement 3", "Value",
             "the CyberSecEval 3 paper section 5.2 gives the same figures: first layer within 60ms, second layer approximately 300ms, 90% of cases only the first layer, under 70ms for the majority, 10% of queries over 300ms [Documented]", "T65 (r2)")
    V.url_add(g, "CodeShield latency statement 3", ["https://arxiv.org/html/2408.01605"], "T65 (r2)")
    S(g, "CodeShield latency statement 4", "Benchmark and conditions", "the four statements differ and none is Meta's single figure",
      "the statements differ between sources and none is Meta's single figure", "T65 (r2)")

    # ------------------------------------------------------------ (h) adjacent
    h = "h"
    S(h, "=CyberSecEval", "Relationship to Table 3", "some test data may seed guardrail tests {I} (premise: the suite includes prompt injection and secure-code data)",
      "some test data could serve as possible sources for guardrail tests [Inferred] (premise: the suite includes prompt injection and secure-code data)", "T97 (r1 and r2), R032: non-standard label form")
    S(h, "=CyberSecEval", "Where covered", "Evaluation-tooling sheet for CyberSecEval (proposed 3j) and block (a) row CyberSecEval 4",
      "The CyberSecEval evaluation-tooling sheet and block (a) row CyberSecEval 4", "T80")
    V.append(h, "=CyberSecEval", "What it is", "The docs site is built from main by .github/workflows/sites_deployment.yml " + PRL, "T22 (r2)")
    V.url_add(h, "=CyberSecEval", [PGB.replace("/blob/", "/tree/") + "CybersecurityBenchmarks/website/docs"], "T22 (r1): pinned folder URL")
