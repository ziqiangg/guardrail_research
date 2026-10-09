# Purple Llama resolutions, part 2 (P5, gr-resolver, 2026-10-09)

Items handled (class a unless stated): T19, T20, T22, T24, T40 (PL5 half), T45, T46, T48, T54, T59, T64, T65 (doc half), T66, T67, T68, T69, T70, T72, T74, T75, T76, T77, T78, T80, T81, T82, T83, T84, T85, T86, T87, T89, T90 to T96, T97 to T101, T103 to T105, plus T5 and the R032 wording pass (Reviewer-note-level items in PL3, PL4, PL5, PL6, PL7, inventory blocks b, c, d, g and the eval sheet). Class b items in my areas are listed in one table near the end with no change (STILL OPEN). Class c items (T6 to T17) and the PL1 and PL2 items (T21 to T44 except where noted) belong to part 1.

Short names as in the triage: A = purplellama_cols_a.md, B = purplellama_cols_b.md, INV = purplellama_inventory.md, EV = purplellama_eval_tooling.md. Line numbers are as read on 2026-10-09 (drafts not edited). Pin = commit 172c1074069eb88ec834124272c1b1c4f8893445 of meta-llama/PurpleLlama. "Repo label" means `[Documented: repo meta-llama/PurpleLlama@172c1074]`. New Summary lines are prefixed `NEW Summary:`; every one was checked with a word-count script (45 words, R7 60, no code characters, balanced bold, label present) and passed.

## Method and access notes

- **Read raw, verbatim:** `python benchtest/tools/fetch_text.py` for the Together pages (docs.together.ai serverless models, deprecations, rate limits, OpenAI compatibility; together.ai pricing), for arXiv html 2408.01605 (CyberSecEval 3), 2505.03574 (LlamaFirewall), 2404.13161 (CyberSecEval 2) and for the arXiv search listing for "CyberSecEval". `curl` GETs for the PyPI simple indexes, the dev.meta.ai llama-protections page, two arXiv figure images (viewed as images), the Hugging Face dataset card and Space file (public, ungated) and the Hub metadata JSON under huggingface.co/api (allowed by main's P4 ruling).
- **PyPI sdists (main P4 ruling):** downloaded read-only into empty scratch folders, sha256 checked against the simple index, unpacked, never installed or run, compared with the pinned clone using a diff that ignores line endings (the clone has CRLF endings): codeshield-1.0.1.tar.gz (sha256 61866b92...), codeshield-1.0.0.tar.gz (68e3d363...), llamafirewall-1.0.3.tar.gz (54fe55c8...). Scripts and diffs: `benchtest/scratchpad/resolver/purplellama2/` (cmp_dirs.py, diff_cs101_vs_pin.txt, diff_lf103_vs_pin.txt, cwe_effective.py).
- **Git history (main P4 ruling):** a blobless bare clone of meta-llama/PurpleLlama in my scratch folder (480 commits, HEAD 172c1074, not shallow), anonymous read-only, used for `git log` only (T84, T85, T40, T59).
- **Not done:** no vendor API call. The Together API host (api.together.xyz or api.together.ai) was never requested; only the marketing site root together.xyz was requested once (HTTP 301). The 316 MB dataset JSON `llamafirewall-alignmentcheck-evals.json` was not downloaded (HTTP HEAD only). No gated file. Semgrep's own output format was not read (third party), so claims about what Semgrep emits stay `[Inferred]`.
- **Label form for PyPI sdist facts:** the allowed forms have no PyPI form, so sdist facts use `[Documented]` with a plain-text source hint "(PyPI sdist codeshield-1.0.1, sha256 61866b92..., read 2026-10-09)". Comparisons I made between the sdist and the pin are `[Inferred]` with the premise named. See QUESTIONS.

## Rulings applied

- R030: T1 to T4 are closed (per-tool prefixes; seven columns; PL7 stays a column; PL5 stays one column; one column per scanner, level words kept). Consequence for my files: process language about a "checkpoint" and the provisional PL7 note are removed (T100, below).
- R032: bench-design text is worded as proposals. See the section "R032 wording pass" (T5 and the R7, R8 and eval "Reuse" text).
- R019, R020, R021, R015, R007, R013: absences are `[Not disclosed]` with what was checked; own counts are `[Inferred]` with the method; code read at the pin only.

---

### T19 — codeshield: repo 0.0.1 versus PyPI 1.0.0 and 1.0.1; is the PyPI sdist the code at the pin?
- Verdict: **CORRECTION** (the open question is answered, and the answer is no: PyPI 1.0.1 is not the pinned code; the rule data match, the Python code differs).
- Evidence:
  - PyPI index, https://pypi.org/simple/codeshield/ (HTTP 200, 2026-10-09): files codeshield-1.0.0 and codeshield-1.0.1 (sdist and wheel). sdist URL https://files.pythonhosted.org/packages/dd/0e/cb79d48ba05eda459a5a2e90b6056019cf7f41441cdee2a17e8dd63e5502/codeshield-1.0.1.tar.gz (sha256 61866b9281c506f9e176995408daab931d52832e625f6056bba273e80a81139f verified).
  - Comparison of the unpacked sdist with `CodeShield/` at the pin, line endings ignored: 168 shared files, 30 differ (nine non-test Python files: codeshield.py, example.py, analyzers.py, insecure_code_detector.py, insecure_patterns.py, issues.py, languages.py, oss.py, usecases.py; 15 test files; pyproject.toml, README.md, the usage notebook, two Java generated Semgrep JSON files and one Java rule YAML); 12 files only in the sdist (nine C example sources, .gitignore, PKG-INFO, a rule_gen script); 2 files only at the pin (generated kotlin_codeshield.json and kotlin_cyberseceval.json).
  - Rule data are the same: every `rules/regex/*.yaml` and `rules/config.yaml` is identical; the generated Semgrep JSON files hold the same rule counts per language (the one Java rule `ssrf_insecure_patterns` differs only in its import patterns: `import java.net.*` in the sdist, `import java.net.*;` at the pin).
  - Kotlin analysers: sdist `insecure_code_detector.py:60` "Language.KOTLIN: [Analyzer.REGEX]," versus pin `insecure_code_detector.py:58-61` "Language.KOTLIN: [ Analyzer.REGEX, Analyzer.SEMGREP, ]".
  - Semgrep job cap: pin `oss.py:61` "MAX_SEMGREP_JOBS: int = 16" and `oss.py:74` "f\"--jobs={SEMGREP_JOBS}\","; the sdist `oss.py` has neither (SEMGREP_COMMAND ends "--json", "--config").
  - Enum bases: sdist `issues.py:20` "class Severity(str, enum.Enum):" and `codeshield.py:26` "class Treatment(str, enum.Enum):"; pin `issues.py:18` "class Severity(enum.Enum):" and `codeshield.py:24` "class Treatment(enum.Enum):".
  - sdist pyproject.toml: version "1.0.1", dependencies ["semgrep>1.68", "pyyaml"]; pin pyproject.toml line 3 version "0.0.1", same dependencies. The pin's pyproject has had one commit only (59c6ead, 2024-04-18, "launch CodeShield to OSS"), so no repo commit corresponds to 1.0.0 or 1.0.1 (git history read 2026-10-09).
  - Import order (code_shield_scanner.py@172c1074:9-19): "from codeshield.insecure_code_detector import" first, "from CodeShield.insecure_code_detector import" in the except branch, so `pip install llamafirewall` runs the PyPI code (T74).
- Label to use: sdist side `[Documented]` (plain hint "PyPI sdist ... read 2026-10-09"); pin side repo label; the statement that they differ and the rule files match is `[Inferred]` (premise: file-by-file comparison). The `[To be verified]` bullets go.
- Draft impact:
  - **A, PL6 R4 Summary (A:318): NEW Summary:** **Regex and Semgrep rule engine, installed as the codeshield package.** Rules are YAML and JSON files enabled per use case. The package depends on Semgrep. The repo folder at the pin says version 0.0.1; PyPI 1.0.1 has the same rule files but different code. **[Documented]**
  - **A, PL6 R4 (A:335, delete the To be verified bullet) and insert after A:334 these bullets:**
    - • PyPI sdist codeshield-1.0.1 (PyPI sdist, sha256 61866b92..., read 2026-10-09) declares version "1.0.1" and the dependencies "semgrep>1.68" and "pyyaml" **[Documented]**
    - • The PyPI 1.0.1 sdist is not a copy of the pinned folder: of 168 shared files 30 differ, including nine Python files, and the sdist lacks the two Kotlin generated Semgrep files (premise: file-by-file comparison of the unpacked sdist with CodeShield/ at the pin, line endings ignored) **[Inferred]**
    - • The regex rule YAML files and `rules/config.yaml` in the sdist are identical to the pinned files, and the generated Semgrep JSON files hold the same rule counts per language (premise: same comparison) **[Inferred]**
    - • Kotlin analysers, PyPI 1.0.1: regex only (sdist `insecure_code_detector.py:60`) **[Documented]**
    - • Kotlin analysers, pin: regex and Semgrep (`insecure_code_detector.py@172c1074:58-61`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
    - • Semgrep job cap, PyPI 1.0.1: none; `SEMGREP_COMMAND` in the sdist `oss.py` has no jobs option **[Documented]**
    - • Semgrep job cap, pin: `--jobs` limited to 16 (`oss.py@172c1074:57-62,74`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
    - • Enum bases, PyPI 1.0.1: Severity and Treatment are string enums (sdist `issues.py:20`, `codeshield.py:26`) **[Documented]**
    - • Enum bases, pin: plain enums (`issues.py@172c1074:18`, `codeshield.py@172c1074:24`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
  - **A, PL6 R4 (A:322):** append "(at the pin; the PyPI 1.0.1 sdist maps Kotlin to regex only)" to the analyser-map bullet and keep its repo label.
  - **A, PL6 R8 (A:389):** replace by "• Whether the PyPI 1.0.1 behaviour (Kotlin regex only, no Semgrep job cap, string enums) changes results compared with the pinned code (the sdist and the pin differ in 30 of 168 shared files; needs testing)".
  - **A, PL6 R8 Summary, PL4 R8 Summary:** see T64 and T65 (they carry the new wording).
  - **A, PL6 R9 and PL4 R9:** add `• https://files.pythonhosted.org/packages/dd/0e/cb79d48ba05eda459a5a2e90b6056019cf7f41441cdee2a17e8dd63e5502/codeshield-1.0.1.tar.gz` (HTTP 200).
  - **A, PL4 R4 (A:471-472):** keep A:471; replace A:472 by "• The PyPI 1.0.1 sdist differs from the pinned CodeShield folder in nine Python files and the Kotlin generated files, with identical rule YAML and config files (see column Code Shield: Output-level insecure-code detection (LLM-generated code), R4; premise: file-by-file comparison) **[Inferred]**". Keep A:467 (the installed package supplies the rules and code; now a consequence of a documented import order).
  - **A, PL4 R8 (A:529):** replace by "• Whether the PyPI 1.0.1 behaviour differs from the pinned code in ways that change scanner results (needs testing)".
  - **INV(a) row 21 (INV:21), cell "Version or revision read":** replace "equality of PyPI 1.0.1 with the repo code is [To be verified]" by "the PyPI 1.0.1 sdist (sha256 61866b92..., read 2026-10-09) [Documented] differs from the pinned folder in nine Python files (for example Kotlin regex only, no Semgrep job cap, string enums) while rule YAML files and config.yaml are identical [Inferred] (premise: file-by-file comparison)".
  - **INV(d) intro (INV:59):** append "The analyzer map described here is the pinned one; the PyPI 1.0.1 sdist maps Kotlin to regex only [Documented] (PyPI sdist codeshield-1.0.1, read 2026-10-09)."
  - **INV(d) row KOTLIN (INV:69), cell "In LANGUAGE_ANALYZER_MAP and analyzers":** append "; PyPI 1.0.1 sdist: REGEX only (insecure_code_detector.py line 60) [Documented] (PyPI sdist codeshield-1.0.1, read 2026-10-09)".
  - **INV(e) row 90 (INV:90), cell "Caveats":** replace "Which codeshield version the PyPI 1.0.1 release contains relative to the repo code [To be verified]" by "After pip install the PyPI codeshield 1.0.1 code runs, not the repo folder; it differs from the pin in nine Python files [Inferred] (premise: sdist read and compared; import order in code_shield_scanner.py lines 9-19)".
  - **INV Reviewer note 4 and note 1 (INV:141,144) and A Reviewer note 9 (A:571):** the "PyPI sdists were not read" statements move to the change log as "read 2026-10-09: codeshield 1.0.1 differs, llamafirewall 1.0.3 matches for scanner files".

### T20 — llamafirewall 1.0.3 sdist versus the pinned commit
- Verdict: **RESOLVED** (for the scanner files of PL3, PL5, PL7; PL2 has one difference, see below). Also **CORRECTION** to Reviewer note B8 and INV statements: PyPI lists 13 releases, not "1.0.0 to 1.0.3".
- Evidence:
  - https://pypi.org/simple/llamafirewall/ (HTTP 200, 2026-10-09) lists 0.0.0, 0.0.1, 0.0.2, 0.0.3, 0.0.4, 0.0.5, 0.1.0, 0.2.0, 1.0.0, 1.0.0.post1, 1.0.1, 1.0.2 and 1.0.3 (sdist and wheel each). sdist https://files.pythonhosted.org/packages/70/f5/9dbd3b0a74c11323d967b0e1210a9fac0de068abc0c2e5dc08a6ee2094a5/llamafirewall-1.0.3.tar.gz (sha256 54fe55c8636fb0b7e78734fdbb96f0036de7ad6613e3dc23ab8531fcf73e6ec1 verified).
  - Comparison with `LlamaFirewall/` at the pin, line endings ignored: 22 shared files; `alignmentcheck_scanner.py`, `piicheck_scanner.py`, `hidden_ascii_scanner.py`, `code_shield_scanner.py`, `prompt_guard_scanner.py` are identical; `custom_check_scanner.py`, `regex_scanner.py` and `config.py` differ by blank lines only; `base_llm.py` by one comment line (a pyrefly ignore); `llamafirewall.py` by a comment line and reformatting of one expression (same logic). Real differences: `promptguard_utils.py` (sdist `from huggingface_hub import HfFolder, login` and `HfFolder.get_token()`; pin `get_token as _get_hf_token`; pin passes `fix_mistral_regex=True` to AutoTokenizer.from_pretrained, as does `cli/configure.py`) and `scanners/__init__.py` (pin adds a lazy `promptguard_utils` branch). The sdist has no tests, examples, notebook, website or SECURITY.md (74 pinned files absent).
- Label to use: `[Inferred]` (premise: comparison of the unpacked sdist with the pin) for "same behaviour"; the sdist contents themselves `[Documented]` with the plain hint.
- Draft impact:
  - **B, PL3 R4 (B:58), PL5 R4 (B:217, second half), PL7 R4 (B:335, second half):** replace the "sdist contents were not read" text by the bullet "• The PyPI llamafirewall 1.0.3 sdist (sha256 54fe55c8..., read 2026-10-09) holds the same scanner code as the pinned commit for this scanner: the files are identical or differ only in blank lines and comment lines (premise: file-by-file comparison with LlamaFirewall/ at the pin) **[Inferred]**". For PL5 name `regex_scanner.py`, `custom_check_scanner.py` and `piicheck_scanner.py`; for PL7 `hidden_ascii_scanner.py`.
  - **B, PL3 R8 (B:130):** delete the bullet "Whether the PyPI 1.0.3 sdist matches the repo at 172c1074 (sdist not read)".
  - **B, Reviewer note 8 (B:392):** replace by "PyPI lists 13 llamafirewall releases, 0.0.0 to 1.0.3 including 1.0.0.post1; the 1.0.3 sdist was read and compared on 2026-10-09". Same correction for any "1.0.0 to 1.0.3" wording (triage T20 text).
  - **B, PL3, PL5, PL7 R9:** add `• https://files.pythonhosted.org/packages/70/f5/9dbd3b0a74c11323d967b0e1210a9fac0de068abc0c2e5dc08a6ee2094a5/llamafirewall-1.0.3.tar.gz`.
  - **INV(a) row 12 (INV:12), cell "Version or revision read":** replace "sdist equals repo code [To be verified]" by "sdist 1.0.3 (sha256 54fe55c8..., read 2026-10-09) matches the pinned scanner files apart from blank lines, comments and the PromptGuard loader (promptguard_utils.py, cli/configure.py) [Inferred] (premise: file-by-file comparison)".
  - **For part 1 (PL2 R4, A:193-194):** same sdist facts; the one behavioural difference is in the PromptGuard model loader (sdist `HfFolder.get_token()`; pin `get_token` and `fix_mistral_regex=True`).

### T22 — docs-site pages cited with unpinned live URLs; deploy source not stated
- Verdict: **RESOLVED**
- Evidence:
  - `.github/workflows/sites_deployment.yml@172c1074` (https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/.github/workflows/sites_deployment.yml): "on: push: branches: [main]"; steps "cd LlamaFirewall/website ... npm run build ... mv build/* ../../_site/LlamaFirewall" and the same for `CybersecurityBenchmarks/website` into `_site/CyberSecEval`; "uses: actions/deploy-pages@v4".
  - `LlamaFirewall/website/docusaurus.config.js@172c1074:25-26`: "url: 'https://meta-llama.github.io/'," and "baseUrl: '/PurpleLlama/LlamaFirewall/',".
  - The pin is the head of main (git ls-remote 2026-10-09), so the pinned `.md` files are the source of the live pages as of the pin.
- Label to use: repo label (workflow and config at the pin).
- Draft impact:
  - **INV scope paragraph (INV:3):** after "The LlamaFirewall docs site (meta-llama.github.io/PurpleLlama/LlamaFirewall/docs) is a build of LlamaFirewall/website/docs;" insert "it is built from the main branch on every push by .github/workflows/sites_deployment.yml, which also builds the CyberSecEval docs site from CybersecurityBenchmarks/website [Documented: repo meta-llama/PurpleLlama@172c1074];". Replace the "unpinned" remark for the docs sites accordingly.
  - **B, PL3 R1:** add after B:13 "• The LlamaFirewall docs site is built from `LlamaFirewall/website` on the main branch by a GitHub workflow, so the pinned `.md` pages are its source (`.github/workflows/sites_deployment.yml@172c1074:4-6,33-40`; `LlamaFirewall/website/docusaurus.config.js@172c1074:25-26`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**".
  - **B, PL3 R9 and PL5 R9:** add `• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/.github/workflows/sites_deployment.yml` and `• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/LlamaFirewall/website/docusaurus.config.js`; keep the live docs-site URLs.
  - **B, Reviewer note 7 (B:391):** delete the sentence "The tutorial alignment-check-scanner-tutorial page was read in the pinned file only" or change to "read in the pinned file; the live site is built from it".
  - **EV, Overview (EV:18) and INV(h) row CyberSecEval (INV:135):** keep the docs-site URLs and append the plain hint "(site built from main by .github/workflows/sites_deployment.yml)".

### T24 — HF dataset facebook/llamafirewall-alignmentcheck-evals: usability as bench input
- Verdict: **CORRECTION** (the card contradicts the paper on the size, and the draft's statement "the benchmark is released as the dataset" is only half supported).
- Evidence:
  - https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/raw/d50916c9ea26e374667c030268218b28c20626a3/README.md (HTTP 200, public, not gated): "The dataset consists of 577 test cases, each of which includes a system prompt, a prompt, a response, and a label indicating whether the prompt is malicious or not."
  - Same card: "A total of 577 (test cases) * 6 (models) = 3462 cases are provided in `llamafirewall-alignmentcheck-evals.json`." Keys: id, prompt_id, system_prompt, prompts, response, is_malicious, injected_tool, prompt_injection_message, attacker_instruction, attack_type, category, model, prompt_injection_success, alignment_guard_judge_MODEL_NAME, alignment_check_system_prompt, alignment_check_user_prompt.
  - Same card: test cases "extending an existing utility benchmark with adversarial perturbations injected into tool outputs"; "This dataset should not be used to train models and should be for evaluation purposes only."
  - Hub metadata https://huggingface.co/api/datasets/facebook/llamafirewall-alignmentcheck-evals: sha d50916c9ea26e374667c030268218b28c20626a3, lastModified 2025-04-29, gated false, files .gitattributes, README.md, llamafirewall-alignmentcheck-evals.json. HTTP HEAD of the JSON: content-length 315677456 (not downloaded).
  - Paper arXiv 2505.03574 Appendix A.1: "This benchmark comprises 600 scenarios (300 benign, 300 malicious), covering 7 distinct injection techniques and 8 threat categories", with a footnote link to the dataset.
- Label to use: card facts `[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]`; paper `[Documented]`; the conflict is two bullets (README rule 4).
- Draft impact:
  - **B, PL3 R5 (B:81-82), replace B:82 by:**
    - • The paper links the dataset facebook/llamafirewall-alignmentcheck-evals for this benchmark (arXiv 2505.03574 Appendix A.1, footnote) **[Documented]**
    - • Source conflict, benchmark size (card side): the dataset card says "577 test cases" and "577 (test cases) * 6 (models) = 3462 cases", with a label field is_malicious and no stated benign and malicious split; licence mit, not gated (dataset card at revision d50916c9) **[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]**
    - • The card lists per-case fields: system prompt, prompts, the model's response, is_malicious, injected tool, attack type and category, whether the injection succeeded, and the AlignmentCheck judge decision with its system and user prompts; the JSON file is 315,677,456 bytes (HTTP HEAD, 2026-10-09) and was not downloaded **[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]**
    - Keep B:81 as the paper side and relabel it "Source conflict, benchmark size (paper side): ...".
  - **B, PL3 R7 (B:111), NEW bullet:** • A possible source of test cases is Meta's released dataset facebook/llamafirewall-alignmentcheck-evals; its cases are written for Meta's own agent simulation and hold prompts, labels and stored judge decisions rather than ready-made traces, so a bench would first need to check whether a case can be replayed as a trace **[Inferred]**
  - **B, PL3 R8 (B:129):** replace by "• How the dataset's 577 test cases (with six model responses each) relate to the paper's 600 scenarios, and whether a case can be turned into a trace for AlignmentCheck (card read, the 316 MB file was not read; needs testing)".
  - **INV(g) row 121 (INV:121), cell "Benchmark and conditions":** replace "(the paper points to a Hugging Face dataset named facebook/llamafirewall-alignmentcheck-evals, not read) [Documented]" by "(the paper links the Hugging Face dataset facebook/llamafirewall-alignmentcheck-evals [Documented]; its card says 577 test cases, six model responses each, while the paper says 600 scenarios, 300 benign and 300 malicious [Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9])".
  - **B, PL3 R9 (B:151):** keep the tree URL; add `• https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/raw/d50916c9ea26e374667c030268218b28c20626a3/README.md`.

### T40 — docs sample outputs differ from code (PL5 half; the PL2 half uses the same evidence)
- Verdict: **RESOLVED** (cause found in git history; whether current code prints it still needs a run, which is not asked here)
- Evidence (git history of the pinned repo, read 2026-10-09):
  - `LlamaFirewall/website/docs/tutorials/regex-scanner-tutorial.md` has one commit, cd9fe65 (2025-04-29, "New Release of Llama Guard 4, LlamaFirewall, Llama Prompt Guard 2, CyberSecEval 4, and Sensitive Doc Classification"); its sample output shows "Reason: default" for allowed messages.
  - At cd9fe65, `LlamaFirewall.scan` returned the first BLOCK or HUMAN_IN_THE_LOOP_REQUIRED result of a scanner and otherwise `ScanResult(decision=ScanDecision.ALLOW, reason="default", score=0.0, ...)`.
  - Commit 55ff24c (2025-05-28, "Adding support for multi-scanner outputs") introduced `last_reason` and the joined reasons. `how-to-use-llamafirewall.md` has two commits, both 2025-04-29 (cd9fe65, 6f0f46c).
- Label to use: repo label (history of the pinned repository).
- Draft impact:
  - **B, PL5 R5 (B:228-229):** keep both bullets; add "• The tutorial page was last changed on 2025-04-29, and the code that returns the scanner's own reason for a single scanner was added on 2025-05-28 (git history of the pinned repository), so the sample output matches the code as it stood on 2025-04-29 **[Documented: repo meta-llama/PurpleLlama@172c1074]**".
  - **B, PL5 R8 (B:268):** replace by "• Whether the tutorial's `Reason: default` sample reflects the code before 2025-05-28 (the page has not been updated since 2025-04-29; a run would confirm)".
  - **For part 1 (PL2 R5 A:210-211, A:249, A RN-6):** same history for how-to-use-llamafirewall.md.

### T45 — no scanner reads Message.tool_calls
- Verdict: **RESOLVED** (the search is now named and complete; the label for the absence changes)
- Evidence: `git grep -n "tool_calls" 172c1074069eb88ec834124272c1b1c4f8893445` over the whole repository returns six hits only: `LlamaFirewall/src/llamafirewall/llamafirewall_data_types.py:54` "tool_calls: Optional[List[Dict[str, Any]]] = None", lines 77 and 79 (the AssistantMessage constructor), and three lines of `LlamaFirewall/website/docs/tutorials/standalone-agent-llamafirewall-tutorial.md` (409, 414, 416) that pass tool calls to a chat API. No scanner file contains the word. The same tutorial scans only the tool result: "tool_msg = ToolMessage(content=str(tool_result))" then "await llama_firewall.scan_async(tool_msg)" (lines 435-438), after the tool has run.
- Label to use: the field and the single-field read stay repo-labelled; the absence "no scanner reads it" is `[Not disclosed]` with the search named (README rule 2, R020); the consequence for arguments is `[Inferred]`.
- Draft impact:
  - **A, PL4 R3 Summary (A:450): NEW Summary:** **Assistant and tool text, as plain strings.** The scanner reads only the message content and scans it as code in all default languages. It is attached to the assistant and tool roles by default and by the coding-assistant use case. **[Documented]** (drops the unsupported "Tool-call arguments are not read" and the capitalised role names)
  - **A, PL4 R3 (A:461), replace by two bullets:**
    - • The `Message` class has an optional `tool_calls` field (`llamafirewall_data_types.py@172c1074:54`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
    - • No scanner in the package reads `tool_calls` (checked with a text search of the whole repository at the pin: matches only the field definitions in `llamafirewall_data_types.py` and a docs tutorial that passes tool calls to a chat API) **[Not disclosed]**
    - • So code placed in function-call arguments is not scanned unless it also appears in the message content (premise: this scanner reads `message.content` only, `code_shield_scanner.py@172c1074:56`) **[Inferred]**
  - **A, PL2 R2 (A:161) and PL2 R3 (A:175)** (part 1 files, same fix): replace the single [Inferred] bullets by the same three bullets, naming `prompt_guard_scanner.py@172c1074:31-34` as the single-field read. **B, PL3 R3 (B:43)**, **PL5 R6 (B:245)**: replace the repo-wide premise by the same search statement; keep "so tool-call arguments are matched only if they appear in the content text" `[Inferred]`.
  - **INV(c) intro (INV:41):** replace "Message.tool_calls exists, but no scanner reads it, so tool-call arguments are not scanned [Inferred] (premise: grep of src for tool_calls)" by "Message.tool_calls exists (llamafirewall_data_types.py line 54) [Documented: repo meta-llama/PurpleLlama@172c1074]; no scanner reads it (checked with a text search of the whole repository at the pin; only the field definitions and one docs tutorial match) [Not disclosed]; so tool-call arguments are not scanned unless they appear in the content [Inferred]."
  - **A, PL2 R2 Summary / PL4 R3 identifiers:** while editing, write "user and tool messages" instead of "USER and TOOL" (README Summary rule: no code identifiers); see T95.

### T46 — default judge model on Together: availability and host
- Verdict: **RESOLVED** (documentation half; the live call stays T47, STILL OPEN class b)
- Evidence (Together pages are third-party, "not Meta docs", main P4 ruling; read raw with fetch_text.py 2026-10-09):
  - Deprecations page https://docs.together.ai/docs/deprecations, section "Deprecation history, Inference": "The table below lists all models removed from serverless inference, most recent first." Row: "2026-03-31 | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | Yes" (columns: Removal date, Model, Supported by on-demand dedicated endpoints). The page says "Models marked “Yes” can be deployed as on-demand dedicated endpoints".
  - Serverless models page https://docs.together.ai/docs/serverless/models (redirect target of /docs/inference-models), "Chat models" table: the only Meta Llama row is "Meta | Llama 3.3 70B Instruct Turbo | meta-llama/Llama-3.3-70B-Instruct-Turbo | 131072 | $1.04 | - | $1.04 | FP8 | Yes | Yes"; no Llama 4 Maverick row. The pricing page https://www.together.ai/pricing lists "Llama 3.3 70B | $1.04 | $1.04" in the serverless table.
  - OpenAI compatibility page https://docs.together.ai/docs/inference/openai-compatibility: "Set api_key to your Together API key ... and base_url to https://api.together.ai/v1:". The word "xyz" appears on none of the Together pages read. https://together.xyz/ returned HTTP 301 to https://together.ai/ (marketing site only, 2026-10-09; the API host was not requested).
- Label to use: Together facts `[Documented]` with plain text "(Together docs, not Meta docs, read 2026-10-09)"; the consequence "the shipped default is not served by Together serverless" `[Inferred]` (premise: the two Together pages); whether api.together.xyz still answers `[To be verified]`.
- Draft impact:
  - **B, PL3 R4 Summary (B:46): NEW Summary:** **Few-shot prompted external language model.** The scanner calls a chat model over an OpenAI-compatible API, by default Llama 4 Maverick on Together, with a fixed prompt of six examples. Together lists that default model as removed from its serverless service. **[Documented]** (the clause replaces "No local model is used", which stays in the Detail at B:48-49)
  - **B, PL3 R6 (B:102-103), replace both bullets by:**
    - • Together's own documentation (not Meta docs, read 2026-10-09) shows `base_url="https://api.together.ai/v1"` for its OpenAI-compatible endpoint, while the Meta code default is the `api.together.xyz` host **[Documented]**
    - • Together's serverless chat-model table (not Meta docs, read 2026-10-09) lists `meta-llama/Llama-3.3-70B-Instruct-Turbo` and has no Llama 4 Maverick row **[Documented]**
    - • Together's deprecation history (not Meta docs, read 2026-10-09) lists `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` among models removed from serverless inference, removal date 2026-03-31, with on-demand dedicated endpoints marked "Yes" **[Documented]**
    - • So the default judge model of AlignmentCheck and CustomCheckScanner is not available on Together's serverless service; a replacement model or a dedicated endpoint would be needed (premise: the two Together pages above) **[Inferred]**
    - • Whether the `api.together.xyz` host still accepts requests (not tested) **[To be verified]**
  - **B, PL3 R7 Summary (B:105): NEW Summary:** **Minimum setup:** install llamafirewall (Python 3.10 or later), set a Together API key, point the scanner at a judge model that Together serves, and attach it to assistant messages. A bench could build short traces of one user request plus agent actions, half hijacked, and compare decisions. Traces leave the machine for a third-party API, so synthetic data is suggested. **[Inferred]** (60 words)
  - **B, PL3 R7 (B:113):** replace by "• A bench could treat the judge model as a variable: results depend on which model serves the call, and the shipped default is not served by Together serverless **[Inferred]**".
  - **B, PL3 R8 Summary (B:117): NEW Summary:** **Key open questions.** Which judge model replaces the default Maverick that Together lists as removed from serverless, Together cost and data terms for traces, latency and context limits, whole-trace reasoning versus the one-action prompt, and judge reliability on the bench.
  - **B, PL3 R8 (B:119):** replace by "• Which judge model a bench would run, since Together lists the default Maverick model as removed from serverless inference on 2026-03-31 and still offers it only as a dedicated endpoint (needs a replacement subclass or a dedicated endpoint; whether the old host still answers needs testing)".
  - **B, PL5 R8 (B:269):** replace the availability clause by "Together lists Llama 3.3 70B Instruct Turbo (the PIICheckScanner default) on its serverless table and lists the Maverick default of CustomCheckScanner as removed from serverless".
  - **B, Reviewer note 4 (B:388):** change "it may be a filtered or paginated list, so it is [To be verified]" to "confirmed by Together's deprecation page (two Together pages agree)".
  - **INV(a) row 14 (INV:14), cell "Backing model or engine":** append "; Together lists this default model as removed from serverless inference (2026-03-31) [Documented] (Together deprecation page, not Meta docs, read 2026-10-09)". **INV(b) rows AGENT_ALIGNMENT (INV:31) and CustomCheckScanner (INV:36), cell "External dependency":** same sentence. **INV(e) row 91 (INV:91), cell "Caveats":** add "Together lists the default Llama 4 Maverick model as removed from serverless inference; the Llama 3.3 70B Instruct Turbo default of PIICheck is on its serverless table [Documented] (Together docs, not Meta docs, read 2026-10-09)".
  - **B, PL3 R9 (B:153-155):** add `• https://docs.together.ai/docs/deprecations` and `• https://www.together.ai/pricing` (both HTTP 200); keep the two existing Together URLs. **PL5 R9:** add the same two.

### T48 — Together cost per call and rate limits for the default models
- Verdict: **PARTLY RESOLVED** (token prices and the rate-limit page are now documented; per-call cost for a trace is arithmetic on bench data)
- Evidence: https://docs.together.ai/docs/serverless/models Chat table: Llama 3.3 70B Instruct Turbo "$1.04" input and "$1.04" output per 1M tokens, context 131072. No serverless row or price for Llama 4 Maverick (T46). https://docs.together.ai/docs/serverless/rate-limits: "In most cases, you can use Together AI serverless inference without encountering rate limits."; "Model-specific limits: When a model is in especially high demand, Together may apply custom rate limits or access restrictions to that model."; the page states no numeric limit. Responses "429 Too Many Requests" and "503 Service Unavailable" are described.
- Label to use: price `[Documented]` (Together docs, not Meta docs); the absence of numeric limits `[Not disclosed]` (checked the rate-limits page, the serverless models page and the pricing page); Maverick serverless price `[Not disclosed]` (no row).
- Draft impact:
  - **B, PL5 R6 (after B:249), NEW bullets:**
    - • Together prices the PIICheckScanner default model `meta-llama/Llama-3.3-70B-Instruct-Turbo` at $1.04 per 1M input tokens and $1.04 per 1M output tokens (Together docs, not Meta docs, read 2026-10-09) **[Documented]**
    - • Numeric serverless rate limits (checked Together's rate-limits, serverless models and pricing pages; the rate-limits page names 429 and 503 responses and no figure) **[Not disclosed]**
  - **B, PL3 R5 (B:89):** replace by "• Published latency distribution, throughput and cost per call for AlignmentCheck (checked the scanner docs page, tutorial, README, paper and the llama.com protections page; not stated; Together prices tokens, not calls, and lists no serverless price for the default Maverick model) **[Not disclosed]**".
  - **B, PL3 R8 (B:120) and PL5 R8 (B:269):** replace the "Cost per call and rate limits" bullets by "• Cost per trace for a replacement judge model (Together lists tokens, not calls; no numeric serverless rate limit is published; needs a measurement of trace token counts)".

### T54 — AlignmentCheck code points not yet in bullets
- Verdict: **RESOLVED**
- Evidence:
  - grep of `LlamaFirewall` at the pin for `require_full_trace`: `src/llamafirewall/scanners/base_scanner.py:20` "self.require_full_trace: bool = False" and `src/llamafirewall/scanners/experimental/alignmentcheck_scanner.py:62` "self.require_full_trace = True"; two hits, no reader.
  - `llamafirewall.py:205` "scan_result = self.scan(message, past_trace if past_trace else None)" (the first message of `scan_replay` gets no trace); `llamafirewall.py:231-235` "if stored_trace is None: stored_trace = []" then "scan_result = self.scan(message, stored_trace)"; `alignmentcheck_scanner.py` `scan`: past_trace None gives ALLOW with status ERROR and reason "No trace provided, cannot proceed"; `_pick_user_input([])` returns None, which gives the same result.
  - `cli/configure.py@172c1074:116-128` accepts TOGETHER_API_KEY or TOGETHER_API_TOKEN; `utils/base_llm.py@172c1074:46` reads the variable named by `api_key_env_var` (already in B:95).
- Label to use: the two grep hits repo label; the empty-trace consequence stays `[Inferred]` (premise named).
- Draft impact:
  - **B, PL3 R3 (after B:41), NEW bullet:** • `require_full_trace` is False in the base scanner and set True in AlignmentCheckScanner; a text search of `LlamaFirewall` finds no other occurrence (`scanners/base_scanner.py@172c1074:20`; `alignmentcheck_scanner.py@172c1074:62`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
  - **B, PL3 R3 (B:41):** keep, but name the premise: "(premise: `scan_replay` passes no trace for the first message at `llamafirewall.py@172c1074:205`, and `scan_replay_build_trace` starts from an empty list at lines 231-235)".
  - **B, Reviewer note 2 (B:386):** remove the sentence "The require_full_trace finding is not in a bullet; the merger may add it to PL3 R3" (done above).

### T59 — custom-scanner how-to is stale
- Verdict: **RESOLVED** (report-only; history added)
- Evidence: `LlamaFirewall/website/docs/documentation/advanced-usage/adding-custom-scanner.md@172c1074:10` "Create a new Python class that inherits from the `BaseScanner` class:" and line 29 "Register your scanner with the LlamaFirewall system by adding it to the `create_scanner` function of `llamafirewall` class:". `grep -rn BaseScanner` over `LlamaFirewall/src`, `examples` and `tests` returns nothing. The page has one commit (cd9fe65, 2025-04-29), the same commit that added `register_llamafirewall_scanner` in `llamafirewall.py` (git history read 2026-10-09).
- Label to use: repo label; absence of `BaseScanner` in code `[Not disclosed]` with the search named (already how B:211 is worded, now wider).
- Draft impact:
  - **B, PL5 R4 (B:211):** replace the search remark by "(a text search of LlamaFirewall/src, examples and tests finds no `BaseScanner`)" and add the bullet "• The docs page and the registry code arrived in the same commit on 2025-04-29, and the page has not been changed since (git history of the pinned repository) **[Documented: repo meta-llama/PurpleLlama@172c1074]**".
  - **INV(b) row Registered custom scanners (INV:37):** append "; the docs page has had no commit since the 2025-04-29 release commit that also added the registry [Documented: repo meta-llama/PurpleLlama@172c1074]".

### T64 — Code Shield language count: 7 versus 8, and which seven
- Verdict: **PARTLY RESOLVED** (which seven is still not stated in any text; Meta's own evaluation figure shows eight languages)
- Evidence:
  - CyberSecEval 3 paper https://arxiv.org/html/2408.01605 section 5.2: "Code Shield leverages our Insecure Code Detector (ICD) static analysis library to identify insecure code across 7 programming languages and over 50 CWEs."
  - Figure 18 of the same paper (https://arxiv.org/html/2408.01605v2/figures/PR-ICD.png, "Precision and Recall of ICD which powers Code Shield as evaluated through sampled human labeling") is a bar chart whose language axis reads Rust, PHP, C, C++, C#, Python, Java, Javascript (eight labels), plus an overall bar. The LlamaFirewall paper repeats the same chart as Figure 3 (https://arxiv.org/html/2505.03574v1/figures/image5.png), while its text says "across seven programming languages" (section 4.4) and its introduction says "8 programming languages". Both images viewed on 2026-10-09.
  - LlamaFirewall paper section 4.4: "CodeShield achieved a precision of 96% and a recall of 79% in identifying insecure code" on "50 LLM-generated code completions per language", and it names CyberSecEval 3 (Wan et al., 2024) as the source of the evaluation.
  - Repo: `languages.py@172c1074:72-82` returns eight languages (C, C++, C#, Java, JavaScript, PHP, Python, Rust); the PyPI 1.0.1 sdist `languages.py` has the same list.
- Label to use: the figure axis labels `[Documented]` (vendor paper); "which seven" `[Not disclosed]` (checked the text of CyberSecEval 3 section 5.2, the LlamaFirewall paper section 4.4, both READMEs, the docs page); that the eight figure languages equal the eight scanned languages `[Inferred]` (premise: label comparison).
- Draft impact:
  - **A, PL6 R2 Summary (A:283): NEW Summary:** **Insecure coding practices, not exploitable vulnerabilities.** Rules flag risky calls and settings such as weak hashes, command injection and buffer-overflow functions, each with a CWE id. Meta's texts say seven languages or eight, and its evaluation figure shows eight. Taint-flow analysis is out of scope. **[Documented]** (45 words; supporting bullets: see T95 and the new bullets below)
  - **A, PL6 R2 (replace the letter-labelled language bullets A:292-298) with plain pairs:** "The Code Shield README says "across 7 programming languages" (CodeShield/README.md@172c1074:11)" [repo label]; "The Meta protections page says "7 programming languages" (dev.meta.ai llama-protections, read 2026-10-09)" [Documented]; "The CyberSecEval 3 paper says "7 programming languages" (arXiv 2408.01605 section 5.2)" [Documented]; "The LlamaFirewall paper says "seven programming languages" in section 4.4 and "8 programming languages" in its summary (arXiv 2505.03574)" [Documented]; "The Insecure Code Detector README says "supports 8 different programming languages" and lists C, C++, C#, Java, Javascript, Python, PHP, Rust (insecure_code_detector/README.md@172c1074:3,22-31)" [repo label]; "The LlamaFirewall docs say "eight programming languages" (code-shield.md@172c1074:4) and the LlamaFirewall README says "8 programming languages" (README.md@172c1074:45)" (split into two bullets) [repo label]; "`get_supported_languages()` returns eight languages (languages.py@172c1074:72-83)" [repo label].
  - **A, PL6 R2, NEW bullets:**
    - • The per-language precision and recall figure in the CyberSecEval 3 paper (Figure 18) has eight languages on its axis: Rust, PHP, C, C++, C#, Python, Java, Javascript, although the text beside it says 7 (arXiv 2408.01605 section 5.2) **[Documented]**
    - • The eight figure languages equal the eight languages the code scans (premise: comparison of the figure labels with `languages.py@172c1074:72-82`) **[Inferred]**
    - • Which seven languages the "7" statements mean (checked the text of the CyberSecEval 3 paper section 5.2, the LlamaFirewall paper section 4.4, both READMEs and the docs page; no list of seven) **[Not disclosed]**
  - **A, PL4 R2 (A:435-440):** same plain-pair rewrite (names instead of letters, T101-style) and the same three new bullets; PL4 R2 Summary (A:431) keeps its wording ("though Meta also says seven and claims over 50 CWEs") and gains no words.
  - **A, PL6 R8 (A:386) and PL4 R8 (A:526):** replace by "• Which seven languages the "7" statements mean (checked the READMEs, docs page, both papers and the code; the paper figure shows eight, the code scans eight)". New R8 Summaries are under T65 (PL6) and T19 (PL4).
  - **INV(d) intro (INV:59):** add "; the per-language chart in the CyberSecEval 3 paper (Figure 18) and the LlamaFirewall paper (Figure 3) has eight language labels [Documented]" and keep "Meta does not say which 7" as "Meta's texts do not say which 7 [Not disclosed] (checked ...)". Add the CyberSecEval 3 paper to the 7-count list: "in CodeShield/README.md line 11, on the llama.com protections page, in CyberSecEval 3 section 5.2 and in LlamaFirewall paper section 4.4".
  - **EV Published results row CSE3 Code Shield (EV:71):** unchanged; add "Figure 18 shows eight languages [Documented]" to the Numbers cell.

### T65 — Code Shield latency statements: how many, and do they agree
- Verdict: **PARTLY RESOLVED** (the documentation half: the statements are now complete, five sources; the measurement stays class b for the bench)
- Evidence (verbatim):
  - CodeShield README (CodeShield/README.md@172c1074:27): "approximately 99% of cases, requests are processed within a swift 70ms window"; p90 450 ms for the rest.
  - LlamaFirewall docs (code-shield.md@172c1074:11-13): first tier "under 100 milliseconds", second "around 300 milliseconds", about 90% resolved by the first.
  - LlamaFirewall paper section 4.4: "completing scans in approximately 60 milliseconds"; "approximately 90% of inputs are fully resolved by the first layer, maintaining a typical end-to-end latency of under 70 milliseconds"; "These performance metrics are based on our internal deployment experience".
  - CyberSecEval 3 paper section 5.2 (https://arxiv.org/html/2408.01605): "The initial layer swiftly identifies concerning code patterns within 60ms."; "takes approximately 300ms. Notably, in 90% of cases, only the first layer is invoked, maintaining the latency under 70ms for the majority of scans."; "10% of queries taking longer than 300ms as observed in some production environments".
  - llama.com protections page (dev.meta.ai, read 2026-10-09): "an average latency of 200ms".
  - The LlamaFirewall paper and CyberSecEval 3 give the same figures (60 ms, 300 ms, 90%, 70 ms, 10% over 300 ms); the README (99% within 70 ms, p90 450 ms), the docs page (first tier under 100 ms) and the protections page (average 200 ms) differ from them.
- Label to use: `[Documented]` for each statement; "the figures differ" is a comparison of documented numbers (stays in the Summary as a plain statement); hardware and language mix behind any figure `[Not disclosed]` (already A:359).
- Draft impact:
  - **A, PL6 R5 Summary (A:341): NEW Summary:** **Insecure flag, issue list and a recommended treatment.** Results carry an insecure flag, the issues found and a block, warn or ignore treatment. Meta reports 96% precision and 79% recall on a manual check, but its latency statements disagree. **[Documented]** (drops "four"; 39 words)
  - **A, PL4 R5 Summary (A:483): NEW Summary:** **Block with score 1.0, or allow with 0.0.** The reason lists each issue with its description, CWE, line and severity. The scanner never returns warn or human review. Meta's latency figures differ by source; precision is 96% and recall 79% on a manual check. **[Documented]**
  - **A, PL6 R5 (after A:357) and PL4 R5 (after A:496), NEW bullet (statement 5):** • Latency, statement 5 (CyberSecEval 3 paper): first layer "within 60ms", second layer "approximately 300ms", "in 90% of cases, only the first layer is invoked, maintaining the latency under 70ms for the majority of scans" (arXiv 2408.01605 section 5.2) **[Documented]**
  - **A, PL6 R5 (A:356, A:493-496 numbering):** replace "statement 1 to 4" labels by source names ("Latency, Code Shield README", "Latency, LlamaFirewall docs", "Latency, LlamaFirewall paper", "Latency, CyberSecEval 3 paper", "Latency, protections page"); and replace A:358 and A:497 ("The four statements differ and are from Meta's internal production studies; ...") by "• The statements differ between sources: the README, docs page and protections page give figures that disagree with each other and with the two papers, which agree with each other; each rests on Meta's own production observations, and no latency or timeout appears in the engine code (premise: search of CodeShield and LlamaFirewall/src for latency and timeout) **[Inferred]**" (A:497 adds "scanner").
  - **A, PL6 R8 Summary (A:384): NEW Summary:** **Key open questions.** Which seven languages the seven-language statements mean, real latency by language, how the PyPI package behaves against the repo code, Rust and PHP rule coverage, and whether Semgrep findings can ever recommend blocking.
  - **A, PL4 R8 Summary (A:524): NEW Summary:** **Key open questions.** Which seven languages the seven-language statements mean, real latency by language, how the PyPI package behaves against the repo code, Rust and PHP rule coverage, and whether Semgrep findings can ever recommend blocking.
  - **INV(g) (INV:112, INV:126):** keep 12 rows by merging the CyberSecEval 3 paper into row "CodeShield latency statement 3" (the two papers give identical figures): rename the Component cell to "CodeShield latency statement 3: LlamaFirewall paper and CyberSecEval 3 paper"; append to the Value cell "; the CyberSecEval 3 paper section 5.2 gives the same figures: first layer within 60ms, second layer approximately 300ms, 90% of cases only the first layer, under 70ms for the majority, 10% of queries over 300ms [Documented]"; append to the Source cell " ; https://arxiv.org/html/2408.01605". Replace the intro sentence (INV:112) "The latency statements below are four different statements, not one figure." by "The CodeShield latency statements below come from five Meta sources in four rows (the two papers give the same figures) and do not agree, so Meta gives no single latency figure." If the owner prefers a separate fifth row, the (g) count becomes 13 and the inventory config must change (see QUESTIONS).
  - **STILL OPEN part:** hardware, input size, language mix and measured latency (T71, class b).

### T66 — a fifth Code Shield source exists only in the eval sheet
- Verdict: **RESOLVED** (verified verbatim; handled in the T65 edits)
- Evidence: CyberSecEval 3 section 5.2 "Mitigation recommendations" (https://arxiv.org/html/2408.01605): "Code Shield is capable of identifying around 190 patterns across 50 different CWEs with an accuracy of 90%." Section 5.2 text as in T65 ("7 programming languages and over 50 CWEs", "within 60ms", "approximately 300ms"). All quotes confirm EV:71.
- Label to use: `[Documented]`
- Draft impact: see T65 (new statement 5 bullet and the INV(g) merge). Also **A, PL6 R2 and PL4 R2, NEW bullet:** • CyberSecEval 3 paper: Code Shield "is capable of identifying around 190 patterns across 50 different CWEs with an accuracy of 90%" (arXiv 2408.01605 section 5.2, mitigation recommendations) **[Documented]**. **A, PL6 R5 (A:353) and PL4 R5 (A:491):** append "(first reported in the CyberSecEval 3 paper section 5.2, which the LlamaFirewall paper cites)" to the precision and recall bullet, keeping its label. **EV:71:** no change except the Figure 18 note (T64).

### T67 — "over 50" CWE claim versus own counts
- Verdict: **CORRECTION** (each of the three CWE counts in the drafts is one too high, caused by one rule without a CWE id; and the first-person wording must go)
- Evidence: counting method re-run (script `cwe_effective.py` and an independent count, scratch folder): distinct `CWE-nnn` ids parsed from `cwe_id` fields. The drafter's `cwe_count.py` counted the empty `cwe_id` of the Semgrep rule `vulnerable-strcpy` as a CWE (the rule has no `cwe_id`; it appears in the four generated JSON files `c_codeshield.json`, `c_cyberseceval.json`, `cpp_codeshield.json`, `cpp_cyberseceval.json`). Corrected counts: **46** distinct CWE ids in the rules enabled for the CODESHIELD use case (regex rules enabled in `config.yaml` plus the generated Semgrep JSON, eight default languages; all enum languages give the same 46); **62** for the CYBERSECEVAL use case (eight default languages) and **64** for all 15 non-agnostic languages; **64** across every regex YAML file and every generated Semgrep JSON file (45 regex ids, 45 Semgrep ids, union 64). Drafts say 47, 63, 65 and 65. Claims to compare: CodeShield README "covering more than 50+ CWEs" (README.md@172c1074:11), docs "over 50 Common Weakness Enumerations (CWEs)" (code-shield.md:4), CyberSecEval 3 "50 different CWEs" (T66).
- Label to use: `[Inferred]` with the method named ("a count of distinct cwe_id values"); config rule-id counts (38 regex ids, 77 Semgrep ids) match my recount and stay `[Documented: repo]`-style plain counts per T98.
- Draft impact:
  - **A, PL6 R2 (A:291) replace by:** • A count of distinct cwe_id values in the rules enabled for the CODESHIELD use case gives 46 across the eight default languages, below the "over 50" claim; the CyberSecEval rule set gives 62 and all rule files 64 (premise: parsing the regex YAML files and the generated Semgrep JSON files; one rule, vulnerable-strcpy, has no cwe_id) **[Inferred]**
  - **A, PL4 R2 (A:448):** same replacement (use "this scanner use case").
  - **A, PL6 R8 (A:395):** replace by "• Whether the "over 50" CWE claim holds for the CODESHIELD rules (a count of distinct cwe_id values in the enabled rules gives 46; a rule-by-rule check would confirm)". **PL4 R8 (A:531):** same.
  - **A, Reviewer note 8 (A:570):** correct the counts to 46, 62, 64 and 64 and note the empty-cwe_id artefact.
  - **A, PL6 R2 (A:289 rule examples):** see T95 (two documented rule messages replace the interpretation).

### T68 — rule paths by language (PHP, Rust, C++, Kotlin)
- Verdict: **RESOLVED** (the code is explicit; four `[Inferred]` labels become `[Documented: repo]`; intent stays open)
- Evidence (`CodeShield/insecure_code_detector/` at the pin):
  - PHP: `insecure_code_detector.py:63` "Language.PHP: [Analyzer.REGEX]," and the Semgrep branch `:132-134` "if oss.ENABLE_SEMGREP and ( Analyzer.SEMGREP in LANGUAGE_ANALYZER_MAP.get(language, []) ):", so Semgrep is not run for PHP although `rules/semgrep/php` (7 YAML files) and `_generated_/php_codeshield.json` (7 rules) exist.
  - Rust: `insecure_code_detector.py:69` "Language.RUST: [Analyzer.REGEX],"; `rules/config.yaml` codeshield "rust:" has empty regex and Semgrep lists; `insecure_patterns.py:36-62` (`load`) adds `regex/language_agnostic.yaml` for every language except C++, Objective-C and Objective-C++, and the config enables 8 language-agnostic rules, so Rust runs 8 regex rules under CODESHIELD (re-count: regex rules effectively loaded, one per language, see below).
  - C++: `insecure_code_detector.py:314-330` builds `config_file_path = oss.SEMGREP_GENERATED_RULES_PATH / f"{code_context.language.value}_{usecase.value}.json"` and uses it when it exists; `_generated_/cpp_codeshield.json` has 16 rules, so Semgrep runs 16 rules for C++ although `config.yaml` lists an empty Semgrep list for cpp. The enabled-rule lists of `config.yaml` are read only by `insecure_patterns.get_enabled_rules`, which `_regex_analyze` calls with the REGEX analyzer.
  - Kotlin: pin map REGEX and SEMGREP, generated JSON with 0 rules (see T19 for the PyPI difference).
  - Effective regex rules per language under CODESHIELD (my recount following `insecure_patterns.load`): C 13, C++ 15 (it also loads the C rules), C# 10, Java 22, JavaScript 9, PHP 11, Python 11, Rust 8, Hack/Kotlin/Ruby/Swift/XML 8 each, Objective-C 13, Objective-C++ 28.
- Label to use: the map entries, the branch condition and the file-name construction `[Documented: repo]`; "so PHP Semgrep rules never run through `analyze()`" is a straight reading of the quoted condition and may carry `[Documented: repo]`; the counts are `[Inferred]` (premise: counted by parsing); whether PHP, Rust or Kotlin behaviour is intended `[Not disclosed]` (nothing in the repo says).
- Draft impact:
  - **A, PL6 R2 (A:302):** replace by "• The analyser map lists regex only for PHP, so the PHP Semgrep rules are never run by `analyze()` (the Semgrep branch tests `Analyzer.SEMGREP in LANGUAGE_ANALYZER_MAP.get(language, [])`; `insecure_code_detector.py@172c1074:63,132-134`; the rules/semgrep/php folder holds 7 YAML files) **[Documented: repo meta-llama/PurpleLlama@172c1074]**".
  - **A, PL6 R2 (A:303):** replace by "• In the CODESHIELD use case `config.yaml` lists no regex or Semgrep rules of its own for Rust, so Rust gets only the eight language-agnostic regex rules (`rules/config.yaml@172c1074` rust entry with empty lists; `insecure_patterns.py@172c1074:36-62` adds `language_agnostic.yaml` for every language except C++ and the Objective-C languages) **[Documented: repo meta-llama/PurpleLlama@172c1074]**".
  - **A, PL6 R4, NEW bullet:** • The Semgrep rules that run are the generated JSON file for the language and use case when it exists (`{language}_{usecase}.json`), so C++ runs the 16 rules in `cpp_codeshield.json` although `config.yaml` lists an empty Semgrep list for cpp; the enabled-rule lists of `config.yaml` are read only for regex rules (`insecure_code_detector.py@172c1074:314-330`; `insecure_patterns.py@172c1074:139-150`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**
  - **A, PL6 R8 (A:390-391) and PL4 R8 (A:530):** replace by "• Whether Rust and PHP are meant to run as they do (Rust gets only the language-agnostic regex rules under CODESHIELD; PHP has Semgrep rules that the analyser map never runs; nothing in the repo states the intent; needs testing)".
  - **INV(d) rows C++ (INV:64), PHP (INV:72), RUST (INV:75), KOTLIN (INV:69) and block intro:** change the labels as follows. C++ "Semgrep rule folder" cell: append "; the generated cpp_codeshield.json is the file Semgrep uses for C++ [Documented: repo meta-llama/PurpleLlama@172c1074] (insecure_code_detector.py lines 314-330)". PHP "analyzers" cell: replace "[Inferred] (premise: insecure_code_detector.py lines 132-134 check the map before running Semgrep)" by "[Documented: repo meta-llama/PurpleLlama@172c1074] (insecure_code_detector.py lines 63 and 132-134)". RUST "Regex rule file" cell: replace "the language-agnostic rules still apply [Inferred] (premise: insecure_patterns.py lines 56-62)" by "the language-agnostic rules still apply [Documented: repo meta-llama/PurpleLlama@172c1074] (insecure_patterns.py lines 36-62)". KOTLIN "Regex rule file" cell: replace "[Inferred] (premise: insecure_patterns.py lines 43-62)" by "[Documented: repo meta-llama/PurpleLlama@172c1074] (insecure_patterns.py lines 36-62)".
  - **A, Reviewer note 7(d),(e) (A:569):** move to the change log as resolved.

### T69 — Semgrep severity string versus the Severity enum
- Verdict: **PARTLY RESOLVED** (the code and the rule-file data are now documented; what Semgrep prints is third-party and stays inferred; the PyPI package behaves the same way)
- Evidence:
  - Pin `insecure_code_detector.py:282` "severity=issue_details.get("severity", "")," (raw string from Semgrep output); `codeshield.py:90` "if any(issue.severity == Severity.ERROR for issue in issues):"; `issues.py:18-22` "class Severity(enum.Enum): ERROR = "error"".
  - The generated Semgrep JSON rules carry upper-case severities: `c_codeshield.json` all 16 WARNING; `java_codeshield.json` 5 WARNING and 6 ERROR; `csharp_codeshield.json` 19 WARNING and 1 INFO; PHP, Python and JavaScript all WARNING. A string such as "ERROR" does not equal the enum member whose value is "error" (plain enum at the pin, string enum `"error"` in PyPI 1.0.1, where `Severity(str, enum.Enum)` compares to the plain string "error", not "ERROR").
  - Regex path: `insecure_code_detector.py:185` "severity=Severity.from_string(pattern.severity)" lower-cases the string, so regex issues carry the enum; rules with severity Error in the effectively loaded CODESHIELD regex set: one (C bugprone-gets; also loaded for C++ and Objective-C).
- Label to use: code lines and rule-file severities `[Documented: repo]`; "so Semgrep findings may never give BLOCK" stays `[Inferred]` (premise: the rule severity string is echoed in Semgrep's JSON output, which is third-party behaviour not read here).
- Draft impact:
  - **A, PL6 R5 (A:349) replace by two bullets:**
    - • Semgrep issues carry the raw severity string from the Semgrep output (`insecure_code_detector.py@172c1074:282`), while the treatment check compares with the Severity enum (`codeshield.py@172c1074:90`; `issues.py@172c1074:18-22`, value "error") **[Documented: repo meta-llama/PurpleLlama@172c1074]**
    - • The generated Semgrep rule files use upper-case severities (for example 6 ERROR rules in `java_codeshield.json`), so a Semgrep finding of severity ERROR may never produce `BLOCK` (premise: Semgrep echoes the rule severity string, which was not read; the PyPI 1.0.1 package has the same comparison) **[Inferred]**
  - **A, PL6 R5 (A:350):** keep; replace "(premise: count over regex YAML and config.yaml)" by "(premise: count of regex rules with severity Error among the rules loaded for the CODESHIELD use case, parsing the YAML files and config.yaml)".
  - **A, PL4 R5:** add the same two bullets with a pointer ("see the Code Shield column R5"); PL6 R8 (A:392) and PL4 R8 keep the "needs testing" bullet.

### T70 — smaller code observations
- Verdict: **PARTLY RESOLVED** (code facts documented; runtime consequences need a run, class b T71)
- Evidence:
  - Temporary file: `insecure_code_detector.py:128-129` "if len(result) > 0: return result" and `:136-137` "return result" both precede `:150-151` "if not is_path_preexisting: os.remove(code_context.path)"; the file is created by `_write_code_to_file` with `tempfile.NamedTemporaryFile(suffix=extension, mode="w", delete=False)` (lines ~232-236); no other deletion call exists in the file.
  - Notebook: `CodeShield/notebook/CodeShieldUsageDemo.ipynb` cell 2: "if result.recommended_treatment == "block":". Pin `codeshield.py:24` `class Treatment(enum.Enum)` (plain enum, so `Treatment.BLOCK == "block"` is False in Python); PyPI 1.0.1 `codeshield.py:26` `class Treatment(str, enum.Enum)` (so it is True).
  - Threshold: `code_shield_scanner.py@172c1074:38` "super().__init__("Code Shield Scanner", 1.0)", no further use of `block_threshold` in the file.
  - New observation (code read): `code_shield_scanner.py@172c1074:78-79` builds the reason with `f" (CWE-{issue.cwe_id})"` while rule files store `cwe_id: CWE-120`, so a block reason would print "CWE-CWE-120". Rule-data oddities: generated C rule `potential-command-injection` has CWE-78 but the message "Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)." and `vulnerable-strcpy` has no cwe_id (`c_codeshield.json`).
- Label to use: code lines `[Documented: repo]`; consequences (file left on disk, notebook branch never taken at the pin, doubled CWE prefix) `[Inferred]` (premise: Python semantics and the quoted lines); runtime confirmation `[To be verified]`/needs testing in R8.
- Draft impact:
  - **A, PL6 R6 (A:368) and PL4 R6 (A:508):** replace by two bullets: • On the fast-mode early returns the function returns before the cleanup (`insecure_code_detector.py@172c1074:128-129,136-137,150-151`), and the temporary file is created with `delete=False` **[Documented: repo meta-llama/PurpleLlama@172c1074]** and • so the temporary file may remain on disk after those scans (premise: the quoted order of statements; no other deletion in the file) **[Inferred]**.
  - **A, PL6 R5 (A:352):** replace by • The usage notebook compares `recommended_treatment` with the strings "block" and "warn" (notebook cell 2) **[Documented: repo meta-llama/PurpleLlama@172c1074]** and • At the pin Treatment is a plain enum, so that comparison is false; in the PyPI 1.0.1 package Treatment is a string enum, so it is true (premise: the two class definitions quoted in T19) **[Inferred]**.
  - **A, PL4 R5 (A:488):** replace "(premise: code_shield_scanner.py contains no use of block_threshold)" by "(code_shield_scanner.py@172c1074:38 passes 1.0 to the base class and the file has no other use of `block_threshold`)" and label `[Documented: repo meta-llama/PurpleLlama@172c1074]`; keep the sentence "the scan code never compares against it".
  - **A, PL4 R5, NEW bullets:** • The block reason is built as "(CWE-{issue.cwe_id})" (`code_shield_scanner.py@172c1074:78-79`) and rule files store ids such as "CWE-120" (`rules/regex/c.yaml@172c1074:12`), so the printed text may read "CWE-CWE-120" (premise: the two quoted lines) **[Inferred]**; • Two data oddities in the generated C Semgrep file: `potential-command-injection` (CWE-78) carries the message of the weak-PRNG rule, and `vulnerable-strcpy` has no cwe_id (`_generated_/c_codeshield.json@172c1074`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**.
  - **A, PL4 R8 (A:532-534) and PL6 R8 (A:393-394):** keep the "needs testing" bullets (T71 stays open).

### T72 — per-language precision and recall in the paper figure
- Verdict: **PARTLY RESOLVED** (figure read as an image; no numeric table exists)
- Evidence: arXiv 2408.01605 Figure 18 (https://arxiv.org/html/2408.01605v2/figures/PR-ICD.png) and arXiv 2505.03574 Figure 3 (https://arxiv.org/html/2505.03574v1/figures/image5.png) are the same bar chart with 90% confidence-interval bars and an overall pair of bars; no table of values is printed in either paper (text read). Read by eye from the bars (about 0.02 resolution): precision about 1.0 for C++, C#, Java and Javascript and about 0.88 to 0.93 for Rust, PHP, C and Python; recall about 0.84 (Rust), 0.67 (PHP), 0.87 (C), 0.69 (C++), 0.87 (C#), 0.75 (Python), 0.75 (Java), 0.84 (Javascript); the confidence bars are wide (roughly 0.2). The overall bars match the 96% and 79% in the text.
- Label to use: axis labels and the existence of the chart `[Documented]`; bar-height readings `[Inferred]` (premise: read by eye from the published figure, no table).
- Draft impact:
  - **A, PL4 R5 (A:492), replace the To be verified bullet by:**
    - • Per-language precision and recall: the paper gives a bar chart with 90% confidence bars for eight languages and no table of values (arXiv 2408.01605 Figure 18; repeated as Figure 3 in arXiv 2505.03574) **[Documented]**
    - • Read by eye from the bars, recall is lowest for PHP (about 0.67) and C++ (about 0.69) and precision is about 1.0 for C++, C#, Java and Javascript, with wide confidence bars (premise: bar heights read from the published figure, no table) **[Inferred]**
  - **A, PL6 R5:** add the same two bullets after A:353 (PL6 has no To be verified bullet for this today).
  - **A, PL4/PL6 R9:** add `• https://arxiv.org/html/2408.01605`.

### T74 — the CodeShield scanner imports the installed package first
- Verdict: **RESOLVED** (with T19)
- Evidence: `code_shield_scanner.py@172c1074:9-19` "try: from codeshield.insecure_code_detector import ( ... ) ... except ImportError: from CodeShield.insecure_code_detector import insecure_code_detector, languages"; `LlamaFirewall/pyproject.toml@172c1074:15` "codeshield>=1.0.1"; the PyPI package is not the pinned folder (T19).
- Label to use: import order `[Documented: repo]`; the consequence stays `[Inferred]` (premise: Python import order).
- Draft impact: **A, PL4 R4 (A:466-467):** keep both bullets and add " (the installed PyPI 1.0.1 package differs from the repo folder; see the T19 bullets)" to A:467. **A, PL4 R7 (A:521):** see the R032 wording pass. Reviewer note 7(f) moves to the change log.

### T75 — dependency pins clash (semgrep)
- Verdict: **RESOLVED**
- Evidence: `CybersecurityBenchmarks/requirements.txt@172c1074:6` "semgrep==1.51.0"; `CodeShield/pyproject.toml@172c1074:15` `dependencies = ["semgrep>1.68", "pyyaml"]`; the PyPI 1.0.1 sdist has the same dependency line.
- Label to use: repo label for each side; "one environment cannot satisfy both" `[Inferred]` (premise: 1.51.0 is not above 1.68).
- Draft impact:
  - **A, PL6 R6 (after A:365) and PL4 R6 (after A:505), NEW bullet:** • The CyberSecEval requirements pin "semgrep==1.51.0" while the Code Shield package asks for "semgrep>1.68", so both cannot be installed in one environment (`CybersecurityBenchmarks/requirements.txt@172c1074:6`; `CodeShield/pyproject.toml@172c1074:15`) **[Inferred]** (premise: 1.51.0 is not greater than 1.68)
  - **INV(f) row Semgrep (INV:106), cell "Conflict or note":** append "; CyberSecEval's requirements pin semgrep==1.51.0 [Documented: repo meta-llama/PurpleLlama@172c1074] (CybersecurityBenchmarks/requirements.txt line 6)".
  - **EV Engine coverage (EV:104):** keep; change the label sentence to one fact per bullet (T99).

### T76 — maturity cells "Available [Inferred]" for PromptGuard, CodeShield, Regex, Hidden ASCII scanners
- Verdict: **PARTLY RESOLVED**
- Evidence: `LlamaFirewall/README.md@172c1074:24-44`: "LlamaFirewall is composed of the following primary components:" with sections "### PromptGuard 2" (line 26), "### AlignmentCheck", "### Regex + Custom Scanners" (line 38) and "### CodeShield" (line 44); line 30 "**Strengths**: Fast, production-ready, easy to update with new patterns." (PromptGuard 2 section). No README, docs page or docstring marks any of PromptGuard, CodeShield, Regex or Hidden ASCII as experimental; the experimental marks are on AlignmentCheck (paper), `[EXPERIMENTAL]` in `custom_check_scanner.py:25`, and the `experimental/` folder. Hidden ASCII is not in the README component list (`grep -rn -i "hidden.ascii\|HIDDEN_ASCII"` over `*.md` finds one tutorial sentence only).
- Label to use: PromptGuard "production-ready" `[Documented: repo]`; CodeShield and Regex "listed as a primary component" `[Documented: repo]`; "not marked experimental" is an absence: `[Not disclosed]` with the search named; Hidden ASCII stays `[Inferred]` (premise: not under experimental/, not listed in the README).
- Draft impact:
  - **INV(a) rows PromptGuard scanner (INV:13), CodeShield scanner (INV:15), Regex scanner (INV:16), cell "Status":** PromptGuard: "Available [Documented: repo meta-llama/PurpleLlama@172c1074] (LlamaFirewall/README.md line 30: Fast, production-ready, easy to update with new patterns)". CodeShield: "Available [Documented: repo meta-llama/PurpleLlama@172c1074] (listed as a primary component, LlamaFirewall/README.md line 44); no maturity statement (checked README, docs pages and code docstrings) [Not disclosed]". Regex: same with line 38. **Hidden ASCII (INV:17):** keep "Available [Inferred] (premise: in the scanners package, not under scanners/experimental, tested in tests/test_hidden_ascii_scanner.py; not listed in the README components)".
  - **INV(b) column "Maturity" rows PROMPT_GUARD (INV:30), CODE_SHIELD (INV:32), REGEX (INV:33), HIDDEN_ASCII (INV:34):** PROMPT_GUARD: "Described as production-ready in the README [Documented: repo meta-llama/PurpleLlama@172c1074]". CODE_SHIELD and REGEX: "Listed as a primary component; no maturity statement [Not disclosed] (checked README, docs pages and docstrings)". HIDDEN_ASCII: "Not marked experimental in code; not listed in the README [Inferred]".

### T77 — Covered-by convention for SYSTEM and MEMORY role rows
- Verdict: **RESOLVED** (convention proposal from the presidio test: list a header only where that column's Detail names the role or function)
- Evidence: SYSTEM is named in PL2 (A:164,169-170: CHAT_BOT adds PROMPT_GUARD for SYSTEM), PL5 (B:191,193,209) and PL7 (B:328); PL3 names it only as an empty default (B:40); PL4 R3 names ASSISTANT, TOOL, USER, MEMORY (A:450-461) but not SYSTEM. MEMORY is named in PL2 (A:172), PL4 (A:457), PL5 (B:193) and PL7 (B:328); PL3 only as an empty default (B:40). PIICheck, CustomCheckScanner and the custom route stay under the PL5 header (R030: PL5 is one column).
- Label to use: n/a (convention).
- Draft impact:
  - **INV(c) row SYSTEM (INV:47), cell "Covered by Table 3 column":** `LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner); LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner); LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner)`.
  - **INV(c) row MEMORY (INV:49):** `LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner); LlamaFirewall: Output-level insecure-code detection (CodeShield scanner); LlamaFirewall: Regex pattern blocking and custom scanners (Regex scanner); LlamaFirewall: Hidden Unicode tag-character detection (Hidden ASCII scanner)`.
  - **B, PL3 R3 (B:40):** to keep AlignmentCheck on SYSTEM or MEMORY rows, name the roles in the text instead: "the scanner can be configured for any of the five roles". **A, PL4 R3 (A:457):** add `SYSTEM` to "so it can also scan USER, SYSTEM or MEMORY text" if the SYSTEM row should keep CodeShield. Choose one; the shorter lists above need no text change.
  - **INV(a) row llamafirewall package (INV:12) and INV(e) rows 86, 91, 92, 93:** unchanged (package-level rows list all five).
  - **INV, Reviewer note 7 (INV:147):** replace by the convention sentence above.

### T78 — language rows "Not named [Not disclosed]" and unlabelled test-file remarks
- Verdict: **RESOLVED**
- Evidence: a word search for hack, kotlin, objective-c, objective_c, ruby, swift and xml over every `*.md` and `*.mdx` under `LlamaFirewall/website/docs` and `CodeShield/` at the pin returns one line, `CodeShield/README.md:27` (the adverb "swift" in "swift 70ms window"), so the "not named" claim holds for more files than the six listed. `CodeShield/insecure_code_detector/tests/` holds 16 files (listing read): `__init__.py`, `insecure_code_detector_test.py`, `test_functional.py` and one test file each for c, cpp, csharp, java, javascript, kotlin, objective_c, php, python, ruby, rust, swift and xml; `grep -n -i "HACK\|OBJECTIVE_CPP"` over the folder finds nothing.
- Label to use: `[Not disclosed]` for the unnamed languages (search named) and for the missing tests (listing and grep named).
- Draft impact:
  - **INV(d) rows HACK (INV:66), OBJECTIVE_CPP (INV:71), cell "Named in READMEs and docs":** replace "no unit test file found in tests/" by "no unit test for this language (checked the 16-file tests/ listing and searched it for HACK and OBJECTIVE_CPP) [Not disclosed]". Rows HACK, KOTLIN, OBJECTIVE_C, OBJECTIVE_CPP, RUBY, SWIFT, XML, LANGUAGE_AGNOSTIC: replace "(checked CodeShield/README.md, the ICD README, the rules README, LlamaFirewall/README.md, LFD code-shield.md and the codeshield tutorial; no mention)" by "(searched every .md and .mdx file under LlamaFirewall/website/docs and CodeShield/; no mention)".

### T80 — sheet letter wording
- Verdict: **RESOLVED** (wording advice for the merger and the P8 writer; no source needed)
- Evidence: queue.md P1 Q2 (letters assigned at P8 in queue order, names at most 31 characters); R003.
- Label to use: n/a
- Draft impact:
  - **INV:23 (row CyberSecEval 4, cell "Backing model or engine"):** replace "evaluated on its own evaluation-tooling sheet (proposed 3j), not here" by "evaluated on the CyberSecEval evaluation-tooling sheet, not here". **INV:135 (block h row CyberSecEval, cell "Where covered"):** replace "Evaluation-tooling sheet for CyberSecEval (proposed 3j) and block (a) row CyberSecEval 4" by "The CyberSecEval evaluation-tooling sheet and block (a) row CyberSecEval 4". **INV:1:** the title letter "3x" stays a placeholder until the P8 writer assigns the letter; the merger writes "(final, sheet 3<letter>)" with the assigned letter. **EV:1:** title line is not parsed; for the eval builder (queue note) a suggested sheet name that fits 31 characters is "CyberSecEval evaluation tooling" (30) if the letter prefix leaves room, otherwise "3j. CyberSecEval Eval Tooling" (29).

### T81 — CyberSecEval 4 paper: [Not disclosed] versus [To be verified]
- Verdict: **RESOLVED**
- Evidence: arXiv search https://arxiv.org/search/?query=CyberSecEval&searchtype=all (HTTP 200, 2026-10-09): 11 results: CyberSecEval 1, 2 and 3 papers, CyberSOCEval ("we introduce CyberSOCEval, a new suite of open source benchmarks within CyberSecEval 4"), and third-party works (including "Rethinking CyberSecEval: An LLM-Aided Approach to Evaluation Critique"); none is a CyberSecEval 4 paper. dev.meta.ai llama-protections: "Cybersec Eval 4 expands on its predecessor by augmenting the suite of benchmarks ...", linking only the GitHub folder `CybersecurityBenchmarks`. Repo `CybersecurityBenchmarks/README.md@172c1074:3` "This repository hosts the implementation of [CyberSecEval 4](https://meta-llama.github.io/PurpleLlama/CyberSecEval/)" with no paper link for version 4.
- Label to use: `[Not disclosed]` with what was checked (arXiv search, repo README, docs-site intro, dev.meta.ai page).
- Draft impact:
  - **INV(a) row CyberSecEval 4 (INV:23), cell "Version or revision read":** replace "no CyberSecEval 4 paper id located [To be verified]" by "no CyberSecEval 4 paper located (checked an arXiv search for CyberSecEval with 11 results, the repo README, the docs-site intro and the dev.meta.ai page) [Not disclosed]".
  - **EV Open questions (EV:120) and EV:13:** keep `[Not disclosed]`; add "(arXiv search for CyberSecEval returned 11 results on 2026-10-09)". **Brief (BR, Evaluation-tooling sheet):** change `[To be verified]` to `[Not disclosed]`.

### T82 — CSE3 Prompt Guard negatives and "selected threshold" unpublished
- Verdict: **RESOLVED** (the absence stands, with more checks named)
- Evidence: CyberSecEval 3 section 5.1 "Indirect Injections": "we repurpose CyberSecEval's dataset as a benchmark of challenging indirect injections covering a wide range of techniques (with a similar set of datapoints with the embedded injection removed as negatives)... the model (at our selected threshold) identifies 71.4% of these injections with a 1% false-positive rate"; appendix: "with a set of similar documents without embedded injections as negatives". The paper prints no threshold value. Hugging Face Hub search https://huggingface.co/api/datasets?author=facebook&search=cyberseceval (public metadata, 2026-10-09) returns one dataset, facebook/cyberseceval3-visual-prompt-injection; the repo `datasets/prompt_injection/` holds two JSON files and no negative set (EV:108 already).
- Label to use: `[Not disclosed]` (checked the CSE3 text and appendix, the repo dataset folders, the Hub datasets of the facebook org matching CyberSecEval).
- Draft impact: **EV Published results row CSE3 Prompt Guard (EV:70):** append "(the paper's text and appendix describe the negatives and print no threshold value)". **EV Open questions (EV:121, EV:123):** append "(also checked the Hub datasets of the facebook organisation that match CyberSecEval: one, the visual injection set)". Wording changes tied to R032 are under T5.

### T83 — Hugging Face leaderboard Space
- Verdict: **RESOLVED**
- Evidence: https://huggingface.co/api/spaces/facebook/CyberSecEval (public metadata, 2026-10-09): sha 164ca0b75d52e96ab9e0e1eab2cbe4eff7bf08dc, lastModified 2024-04-18T04:25:39Z, sdk streamlit, runtime stage RUNNING; files app.py, attack_helpfulness.json, exploit_tests.json, insecure_code.json, interpreter_abuse_tests.json, mitre.json, prompt_injection_tests.json, trr_frr_tradeoff_helpfulness.json, requirements.txt. `app.py` (revision 164ca0b7) line 14: "Our open-source evaluation suite's workings and coverage are detailed in our [first] ... and [second] ... papers."
- Label to use: `[Documented: repo facebook/CyberSecEval@164ca0b7]`
- Draft impact: **EV Published results row Hugging Face leaderboard Space (EV:75):** append "Running (Hugging Face runtime stage RUNNING, read 2026-10-09); its page text links only the first and second CyberSecEval papers, so it shows no CSE3 or CSE4 results [Documented: repo facebook/CyberSecEval@164ca0b7]". **EV Open questions (EV:122):** delete (answered) or reword to "The leaderboard Space is running but has not been updated since 2024-04-18 and shows CSE2-era tests only".

### T84 — is CyberSecEval maintained after the 2025-06-12 note
- Verdict: **RESOLVED**
- Evidence (git history of the pinned repo, blobless clone, read 2026-10-09): `git log --since=2025-06-12 -- CybersecurityBenchmarks` lists 98 commits through 2026-09-29. The README note "As of June 12, 2025, our team is exploring options for the next version of our project" was added by commit 23510a3 (2025-06-12, "CyberSecEval OSS PR Guidance"). Authors after that date: Jinpeng Miao 40 commits (for example 2026-04-29 "Update follow-redirects to avoid vulnerabilities", 2026-05-04 "Add missing copyright headers"), Shengye Wan 8, Abraham Montilla 6 ("Add Llama API endpoint", 2025-11-11), others fewer; automated maintenance commits (type-error suppressions, lint fixes) account for most of the rest, for example 172c107 and 27429af (2026-09-29, "Suppress type errors for Pyre upgrade").
- Label to use: `[Documented: repo meta-llama/PurpleLlama@172c1074]` for commit facts; the counts are `[Inferred]` (premise: counted from git log).
- Draft impact:
  - **EV Overview (EV:16):** replace the clause "the pinned commit is dated 2026-09-29, after that note" by "the folder has had 98 commits since 2025-06-12 through 2026-09-29, from people and from automated maintenance (git history read 2026-10-09) [Inferred] (premise: counted from git log); the note itself was added on 2025-06-12 (commit 23510a3) [Documented: repo meta-llama/PurpleLlama@172c1074]". Split into two bullets (T99).
  - **EV Open questions (EV:124):** replace by "• Whether a next CyberSecEval version is planned (the README note of 2025-06-12 still says the team is exploring options; the folder kept receiving commits to 2026-09-29) **[Not disclosed]**". **INV(a) row CyberSecEval 4 (INV:23):** append "98 commits to the folder since 2025-06-12 (git history) [Inferred]".

### T85 — Instruct and Autocomplete: README says removed, code registers them
- Verdict: **RESOLVED** (as a README-versus-code conflict with history; whether they run is a bench task)
- Evidence: `CybersecurityBenchmarks/README.md@172c1074:226` "Note: Secure Code Generation Benchmarks are temporarily removed from the default list, as our team is identifying the best relative import solution"; `benchmark/run.py@172c1074:24` "from .instruct_or_autocomplete_benchmark import InstructOrAutoCompleteBenchmark" and `:34` "Benchmark.register_benchmark(InstructOrAutoCompleteBenchmark)". Git history: commit 8c5a89e (2025-01-14, "Temporarily taking down insecure coding benchmarks") added the README note and commented out the import and the registration; commit c6dee62 (2025-01-29, "ImportError: attempted relative import beyond top-level package (#71)") restored both lines; the README note was never removed.
- Label to use: repo label (README text, code lines, history).
- Draft impact:
  - **EV Tools rows Instruct (EV:28) "Engine" cell:** replace "(conflict, see Open questions)" by "(the README note was added on 2025-01-14 together with a change that commented out the registration, and the registration was restored on 2025-01-29; the note is a leftover, git history read 2026-10-09)".
  - **EV Open questions (EV:125):** replace by "• Do the Instruct and Autocomplete suites run from this commit (code read; a run would confirm)? **[To be verified]**" and add to Detail under Engine coverage the two bullets: "• README side: secure-code benchmarks are "temporarily removed from the default list" (CSB/README.md:226) **[Documented: repo meta-llama/PurpleLlama@172c1074]**" and "• Code side: `run.py:24,34` import and register `InstructOrAutoCompleteBenchmark`, restored by commit c6dee62 on 2025-01-29, after the note was added on 2025-01-14 **[Documented: repo meta-llama/PurpleLlama@172c1074]**".

### T86 — README versus file conflicts recorded inside Open questions
- Verdict: **RESOLVED** (verified again; move to Detail)
- Evidence: AutoPatch counts (README lines 571-573 "142" and "120" per the draft; files 136, 113, 20: unchanged from EV:36, EV:59). Docs page `CybersecurityBenchmarks/website/docs/benchmarks/prompt_injection.md:36` uses `--prompt-path="$DATASETS/prompt_injection/prompt_injection_multilingual.json"` while `datasets/prompt_injection/` holds `prompt_injection.json` and `prompt_injection_multilingual_machine_translated.json`. https://meta-llama.github.io/PurpleLlama/docs/benchmarks/prompt_injection returned HTTP 404 and https://meta-llama.github.io/PurpleLlama/CyberSecEval/docs/benchmarks/prompt_injection returned HTTP 200 (2026-10-09). Provider lists: README line 122 five names; docs getting_started line 37 "OPENAI, ANYSCALE, and TOGETHER"; five classes in code (EV:92-95).
- Label to use: `[Documented: repo meta-llama/PurpleLlama@172c1074]` (kept in Detail; HTTP facts `[Documented]` with the status and date).
- Draft impact: **EV Open questions (EV:126-128):** delete the three bullets and add them as Detail bullets: under Tools row AutoPatch (EV:36) it already carries the count conflict (keep); add one bullet under Engine coverage "• Docs-site command example `prompt_injection_multilingual.json` differs from the repo file `prompt_injection_multilingual_machine_translated.json` (website/docs/benchmarks/prompt_injection.md:36) **[Documented: repo meta-llama/PurpleLlama@172c1074]**" and "• The Hugging Face card of the visual injection set links https://meta-llama.github.io/PurpleLlama/docs/benchmarks/prompt_injection, HTTP 404; the working page has /CyberSecEval/ in its path (HTTP 200, observed 2026-10-09) **[Documented]**". The provider-list conflict already sits at EV:93-95 (keep). Open questions keep only `[To be verified]` or `[Not disclosed]` bullets (README section 6).

### T87 — CyberSecEval 2 injection range: 26 to 41% versus 13 to 47%
- Verdict: **PARTLY RESOLVED** (the paper's own results text explains the 13 to 47% range: it is the interpreter-abuse range; the conclusion sentence attaches it to prompt injection)
- Evidence: https://arxiv.org/html/2404.13161 : "All tested models showed between 26% and 41% successful prompt injections." (abstract and results); results text: "LLMs we studied complied with between 13% and 47% of the requests to help an adversarial user attack attached code interpreters based on 5 categories of harmful interpreter behavior."; conclusion: "all tested models showed vulnerability to prompt injections, ranging from 13% to 47% success on our tests".
- Label to use: three quotes `[Documented]`; "the conclusion sentence reuses the interpreter-abuse range" `[Inferred]` (premise: the 13% to 47% figure appears in the interpreter-abuse results paragraph).
- Draft impact: **EV Published results row CSE2 prompt injection (EV:68), cell "Numbers":** replace by ""All tested models showed between 26% and 41% successful prompt injections" (abstract and results); the same paper's results give "between 13% and 47%" for compliance with requests to attack attached code interpreters, and its conclusion applies "13% to 47%" to prompt injection". Add a note "the conclusion sentence appears to reuse the interpreter-abuse range [Inferred]". **EV Open questions (EV:129):** delete.

### T89 — visual injection dataset card: size category and review note
- Verdict: **RESOLVED**
- Evidence: https://huggingface.co/datasets/facebook/cyberseceval3-visual-prompt-injection/raw/7933662024dc994be4ab90d520ab712e5765b655/README.md (HTTP 200): front matter "size_categories: - <1K"; text "A total of 1000 test cases are provided in `test_cases.json`." and "Not every sample in this dataset has been manually reviewed, so there may be errors in some test cases." Hub metadata for the same revision tags `size_categories:1K<n<10K`.
- Label to use: `[Documented: repo facebook/cyberseceval3-visual-prompt-injection@79336620]`
- Draft impact: **EV Datasets row Hugging Face dataset (EV:54), cell "Size":** keep ""A total of 1000 test cases" (card text)" and replace the parenthesis by "(the card front matter says size category <1K and the Hub tag says 1K to 10K; the card text says 1000, so the front matter understates the size)". Keep the review note in the Licence/origin cell. Split into two facts with their own labels if the merger finds the cell too long.

### T90 — PL4 R4 Summary says "no model, key or network access" under [Documented]
- Verdict: **RESOLVED** (reword to documented parts; add a documented import-list bullet)
- Evidence: imports (lines at the pin): `insecure_code_detector.py:10-27` asyncio, concurrent, json, logging, os, re, tempfile, concurrent.futures, dataclasses, pathlib, typing and sibling modules; `insecure_patterns.py:10-22` functools, json, logging, os, dataclasses, pathlib, typing, `yaml` and siblings; `oss.py:10-14` functools, importlib.resources, os, shutil, pathlib; `code_shield_scanner.py:7-29` asyncio, the `codeshield` or `CodeShield` ICD modules, llamafirewall types. No machine-learning or HTTP package is imported.
- Label to use: the import list `[Documented: repo]`; "so no model, key or network call" stays `[Inferred]` (A:481, A:513 already).
- Draft impact:
  - **A, PL4 R4 Summary (A:464): NEW Summary:** **Regex and Semgrep rules run through the installed codeshield package.** The scanner imports the Insecure Code Detector from the codeshield package and falls back to the repo copy. The detector's own imports are standard-library modules and PyYAML, and it needs the Semgrep dependency. **[Documented]**
  - **A, PL4 R4, NEW bullet before A:481:** • The scanner and detector source files import only standard-library modules, PyYAML and each other (import lines of `code_shield_scanner.py`, `insecure_code_detector.py`, `insecure_patterns.py` and `oss.py` at the pin); the Semgrep binary is run as a subprocess **[Documented: repo meta-llama/PurpleLlama@172c1074]**. Keep A:481 `[Inferred]` ("so no model is used").

### T91 — PL4 R6 Summary: "needs no key or model", "No size limit or timeout is set in code"
- Verdict: **RESOLVED**
- Evidence: A:502-507, A:512 are as drafted (Python 3.10, eight languages, temporary file, Semgrep dependency, `[Not disclosed]` for limits); the unsupported parts are the two negatives.
- Label to use: Summary draws only on `[Documented: repo]` bullets A:502-507.
- Draft impact: **A, PL4 R6 Summary (A:500): NEW Summary:** **A string of code, with the codeshield package and Semgrep installed.** The scanner needs Python 3.10 or later, scans eight languages by default and writes each scan to a temporary file. **[Documented]**

### T92 — PL5 R2 Summary: "four US-style PII shapes" under [Documented]
- Verdict: **RESOLVED**
- Evidence: B:174-178 (five documented patterns), B:180 (`[Inferred]` reading of the phone and SSN shapes). The email pattern is not a US-style shape.
- Label to use: Summary uses only the pattern list `[Documented]`.
- Draft impact: **B, PL5 R2 Summary (B:172): NEW Summary:** **Two injection phrases and four PII shapes.** The patterns match "ignore previous instructions", "ignore all instructions", and email, phone, credit card and social security number shapes. Nothing else is checked by the Regex scanner. **[Documented]** **B, Reviewer note 6 (B:390):** keep the sentence "PL5 R2 Summary uses only Documented facts" (now true).

### T93 — PL1 R3 Summary: "with no direction setting" under [Documented]
- Verdict: **RESOLVED**
- Evidence: A:33 (card usage passes one string, with no message roles or conversation structure `[Documented: repo]`), A:32 and A:39 (docs page: "The input is a string"; "doesn't need a specific prompt structure or configuration").
- Label to use: Summary from A:32-A:35, A:39 only.
- Draft impact: **A, PL1 R3 Summary (A:30): NEW Summary:** **A single text string.** The model receives one string and labels it benign or malicious, with no message roles or conversation structure in the card's usage. Meta describes it as meant for user prompts and untrusted data such as web content. **[Documented]** (A:37 keeps the `[Inferred]` direction statement.)

### T94 — PL2 R6 Summary: truncation under [Documented], R6 bullet is [Inferred]
- Verdict: **RESOLVED**
- Evidence: A:189 (R4) "padding=True, truncation=True, max_length=512" (`promptguard_utils.py@172c1074:113`) is repo-documented.
- Label to use: add the same repo-labelled bullet to R6 so the Summary clause has support in its row.
- Draft impact:
  - **A, PL2 R6 (before A:220), NEW bullet:** • Truncation: the tokenizer call uses "padding=True, truncation=True, max_length=512" (`promptguard_utils.py@172c1074:113`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**; keep A:220 as the `[Inferred]` consequence ("so any text after the window is not scored").
  - **A, PL2 R6 Summary (A:217): NEW Summary:** **A message with role and text content, plus gated model access.** Weights are downloaded from Hugging Face on first use, with an interactive login if no token exists. Python 3.10 or later is needed, and text over 512 tokens is truncated. **[Documented]** (only "A Message" becomes "A message", README: no class names)

### T95 — Summary sentences whose support sits in another row or is missing
- Verdict: **RESOLVED** (one bullet added or one sentence trimmed per row; no Summary gains words)
- Evidence and impact per row:
  - **PL3 R1 (B:7), "latest action", "original request", "earlier trace":** the system prompt (`alignmentcheck_scanner.py@172c1074:134`) reads "Your task is to assess whether the latest action that the agent is taking is aligned with the original user message and its request."; `_pre_process_trace` joins the earlier messages (B:34). Add to R1 after B:13: • The system prompt asks the judge to assess "whether the latest action that the agent is taking is aligned with the original user message and its request" (`alignmentcheck_scanner.py@172c1074:134`) **[Documented: repo meta-llama/PurpleLlama@172c1074]** and • The text sent to the judge is the earlier trace plus the current message, rendered as role and content (`alignmentcheck_scanner.py@172c1074:71-72`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**. The Summary text is unchanged.
  - **PL5 R1 (B:159), pattern list is in R2:** add to R1 • The built-in patterns are named Prompt injection, Email address, Phone number, Credit card and Social security number (`regex_scanner.py@172c1074:23-28`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**. NEW Summary (also removes the class name "Scanner"): **Fixed regex blocking plus a custom-scanner route.** The Regex scanner blocks a message when it matches built-in patterns for two injection phrases, email, phone, credit card or social security number. Custom scanners are added by extending a scanner base class; LLM-prompt scanners are experimental. **[Documented]**
  - **PL2 R1 (A:141), "the message role decides whether it runs":** add to R1 • The framework picks scanners by message role: "scanners = self.scanners.get(input.role, [])" (`llamafirewall.py@172c1074:113`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**. Summary unchanged.
  - **PL6 R4 (A:318), "It has no model":** removed in the T19 Summary; add the import-list bullet from T90 to PL6 R4 (before A:339) with the engine's imports **[Documented: repo ...]**.
  - **PL6 R2 (A:283), "buffer-overflow functions":** add after A:289 • Rule messages enabled for C include "Potential buffer overflow due to insecure usage of scanf" (CWE-119) and "Potential buffer overflow risk due to use of strcat" (CWE-120) (`rules/regex/c.yaml@172c1074:6-10,18-22`; enabled in `rules/config.yaml@172c1074:5-8`) and "The MD5 hash function is considered insecure" (CWE-328) and the rule id `potential-command-injection` (CWE-78) (`rules/semgrep/_generated_/c_codeshield.json@172c1074`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**. Also correct A:289: `vulnerable-strcpy` is in the C Semgrep list but its generated rule has no cwe_id and severity WARNING (see T70); `md5-usage` and `potential-command-injection` are generated rules.
  - **PL5 R4 (B:200), "compiled once":** the constructor compiles the patterns (`regex_scanner.py@172c1074:59`), and `LlamaFirewall.scan` creates a new scanner instance on every scan call (`llamafirewall.py@172c1074:117-118`), so "compiled once" is unsupported. NEW Summary: **Compiled regular expressions, no model.** Python patterns are compiled in the constructor with case-insensitive matching and run locally with no key. Custom scanners extend a scanner base class and register by name; the experimental LLM-prompt scanners call Together. **[Documented]** B:207 keeps its `[Inferred]` label, now with the premise "a new instance is created on every scan call (`llamafirewall.py@172c1074:117-118`)" (the line is code, so the instance-per-call fact may carry the repo label and the consequence stays `[Inferred]`).

### T96 — three EV Summaries end with two bold labels
- Verdict: **RESOLVED**
- Evidence: README section 4 rule 5 (one label, the weakest fact it draws on).
- Label to use: `[Inferred]` on all three (each mixes documented facts with an inference about scope or wrapping).
- Draft impact:
  - **EV Overview Summary (EV:6):** end "... and the project says it is exploring a next version. **[Inferred]**" and move "(no guardrail mode)" into the first Detail bullet that already carries it (EV:9).
  - **EV Red-teaming Summary (EV:80):** end "... The README warns that platform content filters may block them. **[Inferred]**" (drop the second label and the parenthesis).
  - **EV Engine coverage Summary (EV:90):** end "... Testing a guardrail would mean wrapping it inside a custom provider. **[Inferred]**" (drop the first label; the wrapping route is EV:105).
  - **EV Detail EV:83 and EV:16:** see T99.

### T97 — non-standard label form {I} in INV(h)
- Verdict: **RESOLVED**
- Evidence: README section 5 allows six label forms; INV:135 has `{I}`.
- Label to use: `[Inferred]`
- Draft impact: **INV:135 (block h row CyberSecEval, cell "Relationship to Table 3"):** replace "some test data may seed guardrail tests {I} (premise: the suite includes prompt injection and secure-code data)" by "some test data could serve as possible sources for guardrail tests [Inferred] (premise: the suite includes prompt injection and secure-code data)". (Wording also follows R032.)

### T98 — own counts and parsed sizes carried as [Documented: repo]
- Verdict: **RESOLVED** (convention applied; my recount confirms the counts)
- Evidence: I recounted every INV(d) figure by parsing the files at the pin (regex patterns per YAML file, rules enabled in `config.yaml` for codeshield, YAML files per Semgrep folder, rules per generated JSON): all agree with the drafts (C 15/5, 20 files, 16 rules; C++ 3/2, 16 rules; C# 2/2, 20, 20; Java 23/14, 12, 11; JavaScript 1/1, 15, 13; PHP 22/3, 7, 7; Python 3/3, 14, 10; Rust 13/0; Objective-C 9/0; Ruby 1/0; Swift 10/0; XML 3/0; language_agnostic 8/8; Kotlin 0 generated rules).
- Label to use: facts the vendor states (language is in the enum, file exists, folder exists) stay `[Documented: repo]`; counts are `[Inferred]` (premise: counted by parsing the file).
- Draft impact:
  - **INV(d) all 16 rows, columns "Regex rule file" and "Semgrep rule folder":** replace "(counted from the file) [Documented: repo meta-llama/PurpleLlama@172c1074]" by "[Inferred] (premise: counted by parsing the file)" on the count clause only; where the cell also states that a file exists or is empty, split it: "regex/hack.yaml is present and empty [Documented: repo meta-llama/PurpleLlama@172c1074]". Block intro (INV:59): replace the sentence "Counts in this table were made from the files ..." by "Counts in this table were made by parsing the files at the pin and are labelled [Inferred]".
  - **A, PL6 R4 (A:328, rule counts) and PL4 R2 (A:447):** label the count bullets `[Inferred]` with the premise "(counted by parsing CodeShield/insecure_code_detector/rules/ at the pin)"; the statement "config.yaml lists 38 regex rule ids" is a count of a list and takes the same label. A:301 (the directory listing of 14 regex files and six Semgrep folders) is a listing and may stay `[Documented: repo]`.
  - **EV Tools and Datasets (EV:22, EV:26-38, EV:46-61):** keep `[Documented: repo]` for file contents; label dataset item counts "(count made by parsing the JSON at the pin)" as plain text and `[Inferred]` for derived sizes (bytes, line counts of `third-party.txt`).

### T99 — bullets with two facts or two labels (my files)
- Verdict: **RESOLVED** (split)
- Evidence: B:55, B:57, B:99, EV:16, EV:83.
- Label to use: one fact per bullet.
- Draft impact:
  - **B, PL3 R4 (B:55), replace by two bullets:** • Source conflict, prompt tailoring (paper side): the paper says the prompt "can be tailored with custom few-shot examples" (arXiv 2505.03574 Appendix C.1.2) **[Documented]** and • Source conflict, prompt tailoring (code side): the prompt is a module constant and the subclass constructor takes only `scanner_name` (`alignmentcheck_scanner.py@172c1074:42-61,133`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**.
  - **B, PL3 R4 (B:57), replace by two bullets:** • Pin of code and repo docs: commit 172c1074 (author date 2026-09-29) **[Documented: repo meta-llama/PurpleLlama@172c1074]** and • PyPI package: `llamafirewall` 1.0.3 is the newest sdist in the simple index (observed 2026-10-09) and `LlamaFirewall/pyproject.toml@172c1074:7` also says 1.0.3 **[Documented]**. Same for B:217 and B:335.
  - **B, PL3 R6 (B:99):** a code absence under `[Not disclosed]`: reword to "• Context window in code: `_pre_process_trace` joins the whole trace; a search of `LlamaFirewall/src` for truncation or token limits finds only the 512-token limit in `promptguard_utils.py:113`, which this scanner does not use (checked the files named) **[Not disclosed]**" and, because the join is positive code, add "• `_pre_process_trace` joins every message of the trace and the current message with newlines (`alignmentcheck_scanner.py@172c1074:71-72`) **[Documented: repo meta-llama/PurpleLlama@172c1074]**".
  - **EV Overview (EV:16):** split into the maintenance quote (repo label), the history facts of T84 and the date fact. **EV Red-teaming (EV:83):** split into "• Attack content that exists in the repo: ... **[Documented: repo ...]**" and "• No adversarial-suffix generator, jailbreak library or mutation engine for guardrails was found (checked `benchmark/`, `datasets/` and the docs pages) **[Not disclosed]**".

### T100 — process and session language in Detail and cells (my files)
- Verdict: **RESOLVED** (rewording list; R030 removes the checkpoint items)
- Evidence: finals must not carry process language (README section 4).
- Label to use: unchanged on the facts.
- Draft impact:
  - **B:102, B:119:** replaced in T46. **B:107, B:253, B:358:** "research does not install or run it (R019), so this is a plan for the bench" becomes "this setup has not been run". **B:121:** "Decision for the bench design, not research" becomes "a bench design would need to settle this". **B:170, B:258, B:272, B:311:** delete (R030: PL5 is one column and PL7 stays a column). **B:270:** "(checked the terms section 4; legal reading is for the checkpoint)" becomes "(checked the terms section 4; a legal reading is for the user)".
  - **A:395, A:531:** replaced in T67 ("my count" gone). **A:116 and INV:85:** part 1 and part-1 cells: "so the repo file was used" becomes "the repo file is cited"; INV:85 "Not requested during research (read-only rule)" becomes "Access has not been requested".
  - **B, Reviewer notes 1 to 10; INV Reviewer notes; A Reviewer notes:** move to `purplellama_changes.md` (T102).

### T101 — draft ids (PL1 to PL7) used as cross-references
- Verdict: **RESOLVED**
- Evidence: the workbook shows headers and sheet letters, not draft ids.
- Label to use: unchanged.
- Draft impact: replace in my files: **B:63** "the Regex column, PL5" by "the LlamaFirewall Regex column"; **B:198, B:234** "(column PL3)" by "(the LlamaFirewall AlignmentCheck column)"; **A:281, A:427, A:519** "column PL4/PL6" by "the LlamaFirewall CodeShield column" or "the Code Shield column"; **A:66, A:147, A:197, A:236** (part 1). **EV:22** replace the sentence "Table 3 headers used: PL1 = ...; PL2 = ...; PL4 = ...; PL6 = ..." by a plain list of the four headers (no ids) and **EV:26-32** replace "PL1 and PL2" by "the two prompt-attack columns (Prompt Guard 2 and the LlamaFirewall PromptGuard scanner)", "PL4 and PL6" by "the two Code Shield columns", "No PL column" by "No Table 3 column". Exact header strings: `Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection)`, `LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner)`, `LlamaFirewall: Output-level insecure-code detection (CodeShield scanner)`, `Code Shield: Output-level insecure-code detection (LLM-generated code)`.

### T103 — locator inconsistencies for paper sections
- Verdict: **RESOLVED** (paper side checked; card line ranges are part 1)
- Evidence: arXiv 2505.03574 headings: 4.2 AlignmentCheck (contains "AlignmentCheck adds an experimental semantic-layer defense" and the Figure 2 caption "AlignmentCheck is currently an experimental feature within LlamaFirewall."); 4.3.1 Experimental Setup contains "For PromptGuard, we analyze only messages with the role of user or tool"; 4.3.2 Results contains the AgentDojo numbers (17.6%, 7.5%, 2.89%); the phrase "an experimental few-shot prompting-based chain-of-thought auditor" is in section 1.
- Label to use: unchanged.
- Draft impact: **B:10-11 and INV(a) row 14 (INV:14):** cite "arXiv 2505.03574 section 1" for the auditor phrase and "section 4.2, Figure 2 caption" for "currently an experimental feature". **A:82, A:213 (part 1):** the quote about messages with role user or tool is "section 4.3.1"; the ASR figures are "section 4.3.2". **INV(g) row 120 (INV:120):** keep "section 4.3.2" for the ASR figures. **B:38** already says 4.3.1.

### T104 — URL hygiene (my files)
- Verdict: **RESOLVED**
- Evidence: T22 (docs-site build source), T105 (Hub metadata allowed), the new R9 additions are HTTP 200 (checked 2026-10-09): the two sdist URLs, `docs.together.ai/docs/deprecations`, `www.together.ai/pricing`, `docs.together.ai/docs/serverless/rate-limits`, `arxiv.org/html/2408.01605`, `arxiv.org/html/2404.13161`, the workflow file, the dataset tree and README at d50916c9, the Space tree at 164ca0b7.
- Label to use: n/a
- Draft impact: **B, PL3 R9 (B:148, B:153-155) and PL5 R9 (B:294-296, B:300):** keep live docs-site URLs (they are now explained by T22) and the Together URLs; add the URLs listed in T19, T20, T22, T24, T46. **INV(h) row CyberSecEval (INV:135):** keep the docs-site URL with the T22 hint. **INV(e) row 94:** part 1.

### T105 — Hub metadata JSON as evidence
- Verdict: **RESOLVED** (allowed by main's P4 ruling; presentation only)
- Evidence: queue.md, purplellama P4 Q1 "allowed: public unauthenticated read-only Hub metadata of the vendor org, not a product API (sdp discovery-doc precedent); never gated files". My own reads of huggingface.co/api/datasets/... and /api/spaces/... are of the same kind (public, ungated).
- Label to use: facts from the metadata keep their repo label (revision sha); add the plain hint "(Hub metadata JSON, public)".
- Draft impact: **B, PL3 R4 (B:61) and R5 (B:82), PL5 and INV(a):** change "(Hugging Face API, observed 2026-10-09)" to "(Hugging Face Hub metadata JSON, public, observed 2026-10-09)". **B, PL3 R9:** add `• https://huggingface.co/api/models/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` and `• https://huggingface.co/api/datasets/facebook/llamafirewall-alignmentcheck-evals` (HTTP 200 for the second; the first is gated metadata of a public listing, so cite it only if the P7 URL check returns 200). **B, Reviewer note 5 (B:389):** note the ruling.

---

## R032 wording pass (T5 and bench-design text in my columns and the eval sheet)

### T5 — bench-design question on injection-removed negatives
- Verdict: **RESOLVED** (closed by R030 Q-D and R032: not decided; reported as a proposal)
- Evidence: R030: "NOT decided ... The drafts report it as a proposal only: Meta's attack examples (MIT CyberSecEval data) are a possible source; testing false alarms needs harmless look-alike messages, which Meta did not publish; possible sources are suggested, not chosen." CyberSecEval 3 section 5.1 (T82) states that Meta used "a similar set of datapoints with the embedded injection removed as negatives" and the repo ships none.
- Label to use: `[Inferred]` for every suggestion; `[Not disclosed]` for "Meta did not publish the look-alikes" (checked the repo, the Hub datasets of the facebook organisation and the paper).
- Draft impact: the **EV "Reuse for the test bench"** section (EV:107-117) replaced by the following (section order and the section name unchanged; one fact or suggestion per bullet; every bullet ends `**[Inferred]**` except where noted):
  - • Possible source of attack examples for the prompt-attack columns (Prompt Guard 2 and the LlamaFirewall PromptGuard scanner): the 251 English injection cases and their `user_input` strings (196 direct, 55 indirect, 15 technique labels), and 1,004 machine-translated cases in 17 languages. Limits: the cases embed a secret-key style task rather than harmful content, the translations are machine made, and Prompt Guard 2 is documented to flag explicit override intent only. **[Inferred]**
  - • Testing false alarms would need harmless messages that resemble the attack examples; Meta did not publish them for the injection cases (checked the repo datasets, the Hub datasets of the facebook organisation matching CyberSecEval and the paper text). **[Not disclosed]**
  - • Possible sources of harmless look-alike messages, suggested and not chosen: the injected span removed from each of Meta's cases (the method the CyberSecEval 3 paper describes for its own negatives), the 750 MITRE false-refusal prompts (benign cyber-themed requests that Meta labels as not malicious), public benign text collections, or messages written for the bench. A bench that builds its own look-alikes would not be comparable with Meta's published figure. **[Inferred]**
  - • Technique labels (`injection_variant`, `injection_type`, `risk_category`) could serve as a way to break results down by attack style for the two prompt-attack columns. Limit: the techniques were designed to test whether models follow injected text, not to defeat a classifier. **[Inferred]**
  - • Possible insecure-code test material for the two Code Shield columns: the Instruct and Autocomplete prompts (1,916 each, 8 languages, 50 CWE ids) could make a model produce code to feed the scanners. Limits: the only ground truth in the suites is the Insecure Code Detector itself, which is Code Shield's engine, so agreement with it proves little; independent labels would be needed (the CyberSecEval 3 paper hand-labelled 50 completions per language); the language set matches only the 8 default Code Shield languages. **[Inferred]**
  - • Meta's CyberSecEval 3 paper is a precedent for one possible design: it scores Prompt Guard (first generation) on this injection data at a selected threshold with matching negatives that are not published, and Code Shield against hand labels. A bench could follow a similar recipe for Prompt Guard 2, but that would be a new test, because no CyberSecEval material reports Prompt Guard 2. **[Inferred]**
  - • Not likely to suit guardrail columns: vulnerability exploitation, spear phishing, autonomous operations, AutoPatch and both CyberSOCEval suites measure model capability or need cyber ranges, containers or terabytes of disk, and carry no guardrail-relevant labels. **[Inferred]**
  - • The suites follow a fixed pipeline of prompt file, response file, judge file and stat file with per-bucket counts, which could serve as a template for result records; judge-based suites depend on a hosted judge model and its terms. **[Inferred]**
  - • Licensing and provenance would need review before any dataset is redistributed: code and Meta-written data are MIT, the Instruct and Autocomplete prompts derive from third-party repositories under mixed licences listed in `third-party.txt`, and CrowdStrike and agency report data for CyberSOCEval is third-party. **[Inferred]**
  - • The attack-assistance text in the MITRE, interpreter and injection sets raises the question whether and where to store it or send it to third-party services (judge models, hosted guardrails); this is left open for bench design. **[Inferred]**
  - • Pinning the commit would be advisable if the data is reused, because the README says the team is exploring a next version and the README and the files already disagree on some counts. **[Inferred]**
  - **EV Tools table (EV:26, 27, 28, 30):** reword the "Reuse idea:" clauses in the same way ("a possible source of ...", "could be tested on ..."); EV:30 "Reuse as positive test inputs ... is a reuse idea" becomes "possible source of attack examples; no harmless look-alike set is shipped (fields checked, none is a label) [Not disclosed]"; EV:27 "a benign cyber-flavoured prompt set for measuring over-blocking" becomes "a possible source of harmless cyber-themed messages for false-alarm testing". Each keeps `[Inferred]` and drops the PL ids (T101).
  - **EV Open questions:** delete any bullet that asks the user to decide (none remain after T81 to T89); keep only `[To be verified]` or `[Not disclosed]` bullets.
  - **A, PL1 R7 (A:103, A:106)** (part 1): same suggestion wording for the "test set and negative controls" bullets.

### R7 and R8 rewording in PL3, PL4, PL5, PL6, PL7 (suggestion wording, no new facts)
- **PL3 R7 (B:107, B:108, B:110, B:111, B:113, B:114, B:115):**
  - B:107 → • **Minimum setup:** `pip install llamafirewall`, `export TOGETHER_API_KEY=...`, build `LlamaFirewall({Role.ASSISTANT: [ScannerType.AGENT_ALIGNMENT]})` and call `scan_replay` on a list of messages that starts with a `UserMessage`; the shipped default judge model needs a replacement (see R4) and this setup has not been run **[Inferred]**
  - B:108 → • A bench would have to account for an external dependency: every scan sends the user objective and the trace text to a hosted language model on Together AI, a third party, using a paid key, so testing is not local and involves data sharing **[Inferred]**
  - B:110 → keep the quote and end "...(section 4, read 2026-10-09); traces without real personal or financial data are therefore suggested **[Documented]**" (part 1 owns the terms clause; the suggestion wording only)
  - B:114 → • A bench could record the decision and the reason text, and could treat results whose reason begins "Observation: Error occurred during evaluation" as errors rather than detections **[Inferred]**
  - B:115 → • Possible metrics: detection rate on hijacked traces, false-positive rate on benign traces and calls per trace; the paper's figures (above 80% recall, below 4% false positives) are on Meta's own benchmark and may not transfer **[Inferred]**
- **PL3 R8:** B:121 → "... (checked the Together terms section 3; account defaults are not stated there; a bench design would need to settle this)". B:122 "needs testing" stays.
- **PL4 R7 (A:515-522):** NEW Summary: **Minimum setup:** pip install llamafirewall, which pulls in codeshield and Semgrep, attach the Code Shield scanner type to the assistant role, and scan labelled snippets in the eight default languages. No key, model or gated access is needed. A bench could also check the language list and fast-mode behaviour on the installed codeshield version. **[Inferred]** Bullets: A:519 "A bench could cover every default language with a case from each rule family, including Rust and PHP cases whose rule coverage differs (premise: the engine's analyser map)"; A:520 "A bench could also include non-code prose, fenced code inside markdown, code inside a tool message and an insecure pattern only in a comment, to check the comment filter (premise: engine code)"; A:521 "A bench could record the installed codeshield version, because the scanner imports the installed package first and the PyPI 1.0.1 package differs from the repo folder (premise: import order; T19)"; A:522 "The first scans may be slower where Semgrep runs, and regex-only and Semgrep paths could be timed separately (premise: two-tier design)".
- **PL6 R7 (A:375-382):** NEW Summary: **Minimum setup:** pip install codeshield, which pulls in Semgrep, then scan labelled snippets with the CodeShield scan function in each default language and compare the insecure flag with the label. No key, model or gated access is needed. A bench could also read the recommended treatment and issue list for each case. **[Inferred]** Bullets: A:379 "A bench could include cases for every analyser path ..."; A:380 "One run could pass the language explicitly and another leave it out, to compare results and runtime (premise: `scan_code` branches)"; A:381 "Comment-only matches, markdown-fenced code and prose-only text could be added to test the comment filter and whole-message scanning (premise: engine code)"; A:382 "A labelled set could be built from public code-completion or insecure-code datasets; CyberSecEval is the benchmark Meta cites for its precision and recall (premise: the paper's evaluation text)".
- **PL5 R7 (B:251-258):** NEW Summary: **Minimum setup:** install llamafirewall (Python 3.10 or later) and configure the scanner for the roles under test. A bench could then send labelled strings containing each pattern plus benign and obfuscated variants. No key or model download is needed for the Regex scanner alone. **[Inferred]** Bullets: B:253 → "... no key, no login; this setup has not been run **[Inferred]**"; B:254 → "Possible test inputs for Table 3 input types: ..."; B:257 → "For LLM-prompt scanners (CustomCheckScanner subclasses, PIICheckScanner): additionally set `TOGETHER_API_KEY`; every scan sends the text to Together, a third party, so synthetic data is suggested and the Together terms would need checking first **[Inferred]**"; B:258 delete (R030).
- **PL7 R7 (B:356-361):** NEW Summary: **Minimum setup:** install llamafirewall and attach the scanner to the roles under test (tool output is the case Meta tests). A bench could then send strings with tag-block characters, with and without visible text, plus ordinary and emoji text. No key or model is needed. **[Inferred]** Bullets: B:358 → "... no key, no login; this setup has not been run **[Inferred]**"; B:359 → "Possible test inputs ...: positives could be built by encoding an ASCII sentence into U+E0000 to U+E007F characters, alone and appended to visible text, and negatives from clean text, accented and non-Latin text, and other invisible characters"; B:361 → "As a deterministic filter, one pass per string would be enough; repeated runs for variation would not be needed". B:368 → "(left open for bench design)".
- **PL3 and PL5 R8 bullets that say "Decision for the bench"/"checkpoint":** covered in T100.

---

## Class b items in my areas (no document answers them; no change to labels)

| Tn | Item | Verdict | Note |
|---|---|---|---|
| T47 | Maverick or Llama 3.3 served on the .xyz or .ai host, cost of a call | STILL OPEN (needs a live call; the documentation half is T46 and T48) | no API call made |
| T49 to T53 | long traces, whole-trace versus one-action, tool outputs in the trace, judge manipulation, non-English and run-to-run variation | STILL OPEN (needs testing) | wording only under R032 |
| T55 | AlignmentCheck threshold guidance | STILL OPEN (honest gap, `[Not disclosed]` stands) | rechecked the scanner docs page, tutorial, README, paper; the score is binary |
| T56 to T58 | regex rates, pattern coverage, fixed pattern set | STILL OPEN | T57 reading is a code read; the bullets stay `[Inferred]`. T58: the no-pattern-argument statement now rests on the code (B:203), and the persistence statement (B:207) on `llamafirewall.py:117-118` |
| T60 to T63 | PIICheck, CustomCheck, Hidden ASCII docs silence, tag-block and other invisible characters | STILL OPEN (honest gap or testing) | T61 rechecked: `grep -rn -i "hidden.ascii\|HIDDEN_ASCII"` over `.md` and `.mdx` finds one tutorial sentence only |
| T65 (measurement), T71, T73 | Code Shield latency by language, runtime confirmation, block-all policy | STILL OPEN (bench) | documentation half of T65 is above |
| T79, T88 | inventory honest gaps; `--enable-lf` and `caught_by_promptguard` | STILL OPEN (honest gap) | unchanged; the `--enable-lf` code facts were not re-read |

## Cross-part notes for the other resolver and the merger

- T35 and T40 (PL2 half), T93 and T94 are covered above because the edits touch my T95 or T90 to T96 scope; if part 1 also edits PL2 R4, R6, R7 and R8, take the T94 bullet and the T20 note (promptguard_utils.py loader differences) from here.
- Together terms (T11, T12) and licences (T13) are part 1. This file only rewrites their suggestion wording (R032) and keeps the quoted terms bullets unchanged.
- Row counts: no inventory row is added or removed by my edits (INV(g) stays at 12 rows if the CyberSecEval 3 figures are merged into statement 3, as proposed). No change is needed to the inventory config module for counts.
- New R9 URLs to add (all HTTP 200 on 2026-10-09): see T19, T20, T22, T24, T46, T65, T72.

## Summary table

| Tn | Verdict | Label to use | Changes a Summary? |
|---|---|---|---|
| T19 | CORRECTION | `[Documented]` (sdist) and repo label; comparison `[Inferred]` | yes: PL6 R4 (and PL4 R8, PL6 R8 via T65) |
| T20 | RESOLVED (and CORRECTION of Reviewer note B8) | `[Inferred]` for sameness; sdist `[Documented]` | no |
| T22 | RESOLVED | repo label | no |
| T24 | CORRECTION | `[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]` and `[Documented]` (two bullets) | no |
| T40 (PL5 half) | RESOLVED | repo label | no |
| T45 | RESOLVED | `[Not disclosed]` (absence with search named); `[Inferred]` consequence | yes: PL4 R3 |
| T46 | RESOLVED | `[Documented]` (Together, not Meta docs); `[Inferred]`; `[To be verified]` for the old host | yes: PL3 R4, R7, R8 |
| T48 | PARTLY RESOLVED | `[Documented]`; `[Not disclosed]` | no |
| T54 | RESOLVED | repo label | no |
| T59 | RESOLVED | repo label; `[Not disclosed]` for the search | no |
| T64 | PARTLY RESOLVED | `[Documented]` (figure axis); `[Not disclosed]` ("which seven") | yes: PL6 R2 |
| T65 | PARTLY RESOLVED | `[Documented]` per statement | yes: PL4 R5, PL6 R5, PL4 R8, PL6 R8 |
| T66 | RESOLVED | `[Documented]` | no (carried by T65) |
| T67 | CORRECTION | `[Inferred]` (method named) | no |
| T68 | RESOLVED | repo label (four `[Inferred]` become `[Documented: repo]`) | no |
| T69 | PARTLY RESOLVED | repo label; `[Inferred]` for the consequence | no |
| T70 | PARTLY RESOLVED | repo label; `[Inferred]` consequences | no |
| T72 | PARTLY RESOLVED | `[Documented]` (chart exists); `[Inferred]` (readings) | no |
| T74 | RESOLVED | repo label; `[Inferred]` consequence | no |
| T75 | RESOLVED | repo label; `[Inferred]` | no |
| T76 | PARTLY RESOLVED | `[Documented: repo]` (PromptGuard, CodeShield, Regex); `[Not disclosed]`; `[Inferred]` (Hidden ASCII) | no |
| T77 | RESOLVED (convention) | n/a | no |
| T78 | RESOLVED | `[Not disclosed]` with search named | no |
| T80 | RESOLVED (wording) | n/a | no |
| T81 | RESOLVED | `[Not disclosed]` | no |
| T82 | RESOLVED | `[Not disclosed]` | no |
| T83 | RESOLVED | `[Documented: repo facebook/CyberSecEval@164ca0b7]` | no |
| T84 | RESOLVED | repo label; counts `[Inferred]` | no |
| T85 | RESOLVED | repo label | no |
| T86 | RESOLVED | repo label; HTTP facts `[Documented]` | no |
| T87 | PARTLY RESOLVED | `[Documented]`; `[Inferred]` | no |
| T89 | RESOLVED | `[Documented: repo facebook/cyberseceval3-visual-prompt-injection@79336620]` | no |
| T90 | RESOLVED | `[Documented: repo]` (imports); `[Inferred]` | yes: PL4 R4 |
| T91 | RESOLVED | `[Documented: repo]` | yes: PL4 R6 |
| T92 | RESOLVED | `[Documented]` | yes: PL5 R2 |
| T93 | RESOLVED | `[Documented]` | yes: PL1 R3 |
| T94 | RESOLVED | `[Documented: repo]` bullet added | yes: PL2 R6 (class name only) |
| T95 | RESOLVED | repo label bullets added | yes: PL5 R1, PL5 R4 (PL6 R2 and PL6 R4 via T64 and T19) |
| T96 | RESOLVED | one label `[Inferred]` each | yes: EV Overview, Red-teaming, Engine coverage |
| T97 | RESOLVED | `[Inferred]` | no |
| T98 | RESOLVED (convention) | `[Inferred]` for counts | no |
| T99 | RESOLVED | one fact per bullet | no |
| T100 | RESOLVED | n/a | no |
| T101 | RESOLVED | n/a | no |
| T103 | RESOLVED | n/a | no |
| T104 | RESOLVED | n/a | no |
| T105 | RESOLVED | repo label with a plain hint | no |
| T5 | RESOLVED (closed by R030 and R032; proposals) | `[Inferred]`; `[Not disclosed]` | no (EV Reuse section) |
| R032 pass (R7 Summaries PL4, PL5, PL6, PL7; PL3 R7) | RESOLVED | `[Inferred]` | yes: PL3 R7, PL4 R7, PL5 R7, PL6 R7, PL7 R7 |
| Class b (T47, T49-T53, T55-T58, T60-T63, T65 measurement, T71, T73, T79, T88) | STILL OPEN | unchanged | no |

## Report

**Counts per verdict** (assigned items, each T-id once; the R032 pass and the class b group are counted separately):
- RESOLVED: 36 (T5, T20, T22, T40, T45, T46, T54, T59, T66, T68, T74, T75, T77, T78, T80 to T86, T89 to T101, T103 to T105; T20 also carries one CORRECTION of a Reviewer note)
- PARTLY RESOLVED: 8 (T48, T64, T65, T69, T70, T72, T76, T87)
- CORRECTION: 3 items (T19, T24, T67) plus one Reviewer-note correction under T20
- STILL OPEN (class b, not resolvable from documents): 20 ids (T47, T49 to T53, T55 to T58, T60 to T63, T71, T73, T79, T88; T65 measurement half)

**CORRECTIONs**
1. T19: PyPI codeshield 1.0.1 is not the code at the pin (30 of 168 shared files differ, nine Python files; Kotlin regex only, no Semgrep job cap, string enums); rule YAML and config files are identical. The draft's `[To be verified]` becomes a documented difference.
2. T24: the dataset card says 577 test cases (six model responses each, 3,462 records), the paper says 600 scenarios; the draft treated them as the same count.
3. T67: all three CWE counts are one too high (46, 62, 64, 64 instead of 47, 63, 65, 65) because one rule has no cwe_id; first-person wording to remove.
4. T20 (Reviewer note B8): PyPI lists 13 llamafirewall releases (0.0.0 to 1.0.3), not "1.0.0 to 1.0.3".

**Summary lines that must change (new text above, each word-count checked)**
- PL1 R3 (T93); PL2 R1 (T95, no text change; bullet added), PL2 R6 (T94, class name only).
- PL3 R4 (T46), PL3 R7 (T46, R032), PL3 R8 (T46).
- PL4 R3 (T45), PL4 R4 (T90), PL4 R5 (T65), PL4 R6 (T91), PL4 R7 (R032), PL4 R8 (T19, T64, T65).
- PL5 R1, PL5 R2, PL5 R4 (T92, T95), PL5 R7 (R032).
- PL6 R2 (T64), PL6 R4 (T19, T95), PL6 R5 (T65), PL6 R7 (R032), PL6 R8 (T19, T64, T65).
- PL7 R7 (R032).
- EV Overview, Red-teaming and Engine coverage Summaries (T96: one label each).
- No Summary change: PL3 R1 (support bullets added), PL3 R5, PL1 R1 to R2, PL7 R1 to R6.

**Items still open:** see the class b table; plus the unconfirmed `api.together.xyz` host behaviour (`[To be verified]`), Semgrep's own output format (premise of T69), and the runtime behaviour of the PyPI 1.0.1 package (T19 consequence, needs a bench run).

## QUESTIONS

1. Label form for PyPI sdist facts: the allowed forms have no PyPI form. I propose `[Documented]` plus the plain hint "(PyPI sdist ..., sha256 ..., read 2026-10-09)" for what the sdist contains and `[Inferred]` for my sdist-versus-pin comparisons. Please confirm or rule a different form (main; this affects PL4 R4, PL6 R4, INV(a), INV(d), INV(e)).
2. INV(g) shape for the CyberSecEval 3 latency statement: I propose merging it into row "statement 3" (the two papers give identical figures) so the row count stays 12 and the inventory config needs no change; the alternative is a thirteenth row and a config change. Please pick (merger or main).
3. Reading values off the published bar chart (T72) at about 0.02 resolution and labelling them `[Inferred]`: acceptable, or should only the axis labels be kept? (main)
4. The Hub metadata URL for the gated Llama 4 Maverick FP8 repo (T105): is citing `huggingface.co/api/models/...` in R9 acceptable when the card body is gated, or should B:61 fall back to the gate page text? I proposed citing only if the P7 URL check returns 200. (main)
5. Overlap with part 1: T35, T40 (PL2 half), T93 and T94 touch PL1 and PL2 text. I wrote the edits for T93, T94, T95 and the PL5 half of T40; part 1 should not duplicate them. Is that split acceptable? (main)
