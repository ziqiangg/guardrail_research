"""Evaluation-tooling edits (purplellama_eval_tooling.md, CyberSecEval). Resolutions 1 (r1) and 2 (r2)."""
import merge_lib as L

PRL = "**[Documented: repo meta-llama/PurpleLlama@172c1074]**"
DOC = "**[Documented]**"
INF = "**[Inferred]**"
ND = "**[Not disclosed]**"
CSB = "https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/CybersecurityBenchmarks/"
PGT = "https://github.com/meta-llama/PurpleLlama/tree/172c1074069eb88ec834124272c1b1c4f8893445/"
CSD = "https://github.com/CrowdStrike/CyberSOCEval_data/blob/ce7daa5bc7da51559ca97476d2277be02631783e/data/"

REUSE = [
    "• Possible source of attack examples for the prompt-attack columns (Prompt Guard 2 and the LlamaFirewall PromptGuard scanner): the 251 English injection cases and their `user_input` strings (196 direct, 55 indirect, 15 technique labels), and 1,004 machine-translated cases in 17 languages. Limits: the cases embed a secret-key style task rather than harmful content, the translations are machine made, and Prompt Guard 2 is documented to flag explicit override intent only. " + INF,
    "• Testing false alarms would need harmless messages that resemble the attack examples; Meta did not publish them for the injection cases (checked the repo datasets, the Hub datasets of the facebook organisation matching CyberSecEval and the paper text). " + ND,
    "• Possible sources of harmless look-alike messages, suggested and not chosen: the injected span removed from each of Meta's cases (the method the CyberSecEval 3 paper describes for its own negatives), the 750 MITRE false-refusal prompts (benign cyber-themed requests that Meta labels as not malicious), public benign text collections, or messages written for the bench. A bench that builds its own look-alikes would not be comparable with Meta's published figure. " + INF,
    "• Technique labels (`injection_variant`, `injection_type`, `risk_category`) could serve as a way to break results down by attack style for the two prompt-attack columns. Limit: the techniques were designed to test whether models follow injected text, not to defeat a classifier. " + INF,
    "• Possible insecure-code test material for the two Code Shield columns: the Instruct and Autocomplete prompts (1,916 each, 8 languages, 50 CWE ids) could make a model produce code to feed the scanners. Limits: the only ground truth in the suites is the Insecure Code Detector itself, which is Code Shield's engine, so agreement with it proves little; independent labels would be needed (the CyberSecEval 3 paper hand-labelled 50 completions per language); the language set matches only the 8 default Code Shield languages. " + INF,
    "• Meta's CyberSecEval 3 paper is a precedent for one possible design: it scores Prompt Guard (first generation) on this injection data at a selected threshold with matching negatives that are not published, and Code Shield against hand labels. A bench could follow a similar recipe for Prompt Guard 2, but that would be a new test, because no CyberSecEval material reports Prompt Guard 2. " + INF,
    "• Not likely to suit guardrail columns: vulnerability exploitation, spear phishing, autonomous operations, AutoPatch and both CyberSOCEval suites measure model capability or need cyber ranges, containers or terabytes of disk, and carry no guardrail-relevant labels. " + INF,
    "• The suites follow a fixed pipeline of prompt file, response file, judge file and stat file with per-bucket counts, which could serve as a template for result records; judge-based suites depend on a hosted judge model and its terms. " + INF,
    "• A possible concern for any bench that redistributes datasets: the CrowdStrike reports are CC BY-ND 4.0 and the Hybrid Analysis data CC BY-SA 4.0, and the Instruct and Autocomplete prompts derive from third-party repositories under mixed licences listed in `third-party.txt` (suggested to check before redistributing). " + INF,
    "• Sensitive content: MITRE, interpreter and injection sets contain attack-assistance text; storing it and sending it to third-party APIs (judge models, hosted guardrails) is a point a bench would need to consider (suggested). " + INF,
    "• Pinning the commit would be advisable if the data is reused, because the README says the team is exploring a next version and the README and the files already disagree on some counts. " + INF,
]


def apply(E):
    L._log("eval", "EV title line (not parsed)", "edit", "## Topic: Meta CyberSecEval 4 evaluation tooling (draft, reuse assessment for the test bench)",
           "## Topic: Meta CyberSecEval 4 evaluation tooling (reuse assessment for the test bench)", "T80: draft marker removed")
    # ---------------------------------------------------------------- Overview
    E.sub("Overview", "CyberSecEval is Meta's open-source benchmark suite for testing language models, not guardrails",
          "**[Documented]** **[Inferred]** (no guardrail mode)", INF, "T96 (r2): one label per Summary, the weakest fact (the no-guardrail-mode clause is an inference); the parenthesis is already in the first Detail bullets")
    E.sub("Overview", "No single CyberSecEval 4 paper was found", "an arXiv title search for CyberSecEval returned CSE1, CSE2, CSE3 and a third-party critique (arXiv 2411.08813)",
          "an arXiv search for CyberSecEval returned 11 results on 2026-10-09, among them CSE1, CSE2, CSE3, the CyberSOCEval paper and a third-party critique (arXiv 2411.08813)", "T81 (r2): the search size is recorded")
    E.repl("Overview", "Maintenance: \"As of June 12, 2025", [
        "• Maintenance note: \"As of June 12, 2025, our team is exploring options for the next version of our project\" and external feature PRs should start as an issue (CSB/README.md:168-170); the note was added on 2025-06-12 (commit 23510a3) " + PRL + " " + PGT + "CybersecurityBenchmarks",
        "• Since the note, the folder has had 98 commits from 2025-06-12 through 2026-09-29, from people and from automated maintenance (git history read 2026-10-09) " + INF + " (premise: counted from the git log) " + PGT + "CybersecurityBenchmarks"],
        "T84, T99 (r2): two facts, two labels; the pinned commit date is replaced by the history counted", kind="replace")
    E.sub("Overview", "docs-site landing page for CyberSecEval still carries", "(read 2026-10-09)",
          "(read 2026-10-09; the site is built from main by .github/workflows/sites_deployment.yml)", "T22 (r2): docs-site build source")
    # ---------------------------------------------------------------- Tools
    E.sub("Tools", "Row order follows the README benchmark list",
          "Any mapping to a Table 3 column is a reuse idea marked [Inferred], because no source says these suites evaluate guardrails. Table 3 headers used: PL1 = Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection); PL2 = LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner); PL4 = LlamaFirewall: Output-level insecure-code detection (CodeShield scanner); PL6 = Code Shield: Output-level insecure-code detection (LLM-generated code).",
          "Any mapping to a Table 3 column is a possible reuse marked [Inferred], because no source says these suites evaluate guardrails. Table 3 headers named: Prompt Guard 2: Input-level prompt-attack detection (jailbreak and injection); LlamaFirewall: Input-level prompt-attack detection (PromptGuard scanner); LlamaFirewall: Output-level insecure-code detection (CodeShield scanner); Code Shield: Output-level insecure-code detection (LLM-generated code).",
          "T101 (r2): draft ids replaced by the exact headers; R032 wording")
    E.sub("Tools", "Row order follows the README benchmark list", "Dataset sizes were counted by parsing the JSON files at the pin (item count of the top-level list).",
          "Dataset sizes were counted by parsing the JSON files at the pin (item count of the top-level list); they are counts made from the files, not figures stated by Meta.", "T98 (r2)", kind="hygiene")
    E.sub("Tools", "| MITRE (`--benchmark=mitre`)", "No PL column. Reuse idea: the prompts are malicious cyber-assistance requests that an input-side content classifier could be tested on [Inferred];",
          "No Table 3 column. A possible reuse: the prompts are malicious cyber-assistance requests that an input-side content classifier could be tested on [Inferred];", "T101, R032 (r2)")
    E.sub("Tools", "| MITRE False Refusal Rate", "No PL column. Reuse idea: a benign cyber-flavoured prompt set for measuring over-blocking by an input guardrail [Inferred].",
          "No Table 3 column. A possible source of harmless cyber-themed messages for false-alarm testing of an input guardrail [Inferred].", "T101, R032 (r2)")
    E.sub("Tools", "| Instruct (`--benchmark=instruct`)", "Reuse idea: prompts that elicit insecure code, and a labelled-by-detector output set, for PL4 and PL6 [Inferred];",
          "A possible reuse: prompts that elicit insecure code, and a labelled-by-detector output set, for the two Code Shield columns [Inferred];", "T101, R032 (r2)")
    E.sub("Tools", "| Instruct (`--benchmark=instruct`)", "(conflict, see Open questions)",
          "(the README note was added on 2025-01-14 together with a change that commented out the registration, and the registration was restored on 2025-01-29; the note is a leftover, git history read 2026-10-09)",
          "T85 (r2): the conflict is explained from the git history and moves out of Open questions")
    E.sub("Tools", "| Textual prompt injection (`--benchmark=prompt-injection`)",
          "Closest dataset to PL1 and PL2: the user_input strings are injection attempts. Reuse as positive test inputs for PL1 and PL2 is a reuse idea [Inferred]; no benign twin set is in the repo (fields checked, none is a label) [Not disclosed].",
          "Closest dataset to the two prompt-attack columns (Prompt Guard 2 and the LlamaFirewall PromptGuard scanner): the user_input strings are injection attempts. A possible source of attack examples for those columns [Inferred]; no harmless look-alike set is shipped (fields checked, none is a label) [Not disclosed].",
          "T5, T101, R032 (r2)")
    E.sub("Tools", "| Visual prompt injection", "No PL column takes images (Prompt Guard 2 is a text classifier); reuse would need an image-to-text step first [Inferred].",
          "No Table 3 column takes images (Prompt Guard 2 is a text classifier); a possible reuse would need an image-to-text step first [Inferred].", "T101, R032 (r2)")
    E.sub("Tools", "| Code interpreter abuse", "No PL column. Reuse idea: malicious-code requests as input-side test prompts [Inferred];",
          "No Table 3 column. A possible source of malicious-code requests as input-side test prompts [Inferred];", "T101, R032 (r2)")
    E.gsub("Tools", "no PL mapping", "no Table 3 mapping", "T101 (r2): draft id wording")
    # ---------------------------------------------------------------- Datasets
    E.sub("Datasets", "Sizes are item counts of the top-level JSON list", "parsed at the pin (code read, not run).",
          "parsed at the pin (code read, not run); they are counts made from the files, not figures stated by Meta.", "T98 (r2)", kind="hygiene")
    E.sub("Datasets", "| `third-party.txt` |", "| [Documented: repo meta-llama/PurpleLlama@172c1074] |",
          "| [Documented: repo meta-llama/PurpleLlama@172c1074]; line, licence-line and byte counts [Inferred] (premise: counted from the file) |", "T98 (r2): derived sizes are the drafter's counts", kind="hygiene")
    E.sub("Datasets", "| Hugging Face dataset `facebook/cyberseceval3-visual-prompt-injection`",
          "(HF card; the card header says size category under 1K while the Hub tag says 1K to 10K)",
          "(HF card; the card front matter says size category under 1K and the Hub tag says 1K to 10K; the card text says 1000, so the front matter understates the size)", "T89 (r2)")
    E.sub("Datasets", "| `autopatch/` case lists", "| [Documented: repo meta-llama/PurpleLlama@172c1074]; ARVO licence [Not disclosed] |",
          "| [Documented: repo meta-llama/PurpleLlama@172c1074]; ARVO-Meta repository: BSD 2-Clause [Documented: repo n132/ARVO-Meta@51cfeab5] (not Meta docs); the harness builds on prebuilt images docker.io/n132/arvo:<id>-vul and -fix [Documented: repo meta-llama/PurpleLlama@172c1074]; licences of the open-source projects inside those images [Not disclosed] (checked the ARVO-Meta LICENSE and the Meta dataset folder) |",
          "T15 (r1): ARVO licence read")
    E.sub("Datasets", "| `crwd_meta/malware_analysis/questions.json`", "https://github.com/CrowdStrike/CyberSOCEval_data |",
          CSD + "crowdstrike-reports/LICENSE.md ; " + CSD + "hybrid-analysis/LICENSE.md |", "T15 (r1): pinned licence files replace the repo root URL")
    E.sub("Datasets", "| `crwd_meta/malware_analysis/questions.json`", "| [Documented: repo meta-llama/PurpleLlama@172c1074]; data licence [To be verified] |",
          "| [Documented: repo meta-llama/PurpleLlama@172c1074]; report data in the CrowdStrike repository: CrowdStrike reports CC BY-ND 4.0 and Hybrid Analysis data CC BY-SA 4.0 [Documented: repo CrowdStrike/CyberSOCEval_data@ce7daa5b] (CrowdStrike's repo, not Meta docs) |",
          "T15 (r1)")
    E.sub("Datasets", "| `crwd_meta/threat_intel_reasoning/report_questions.json`", "| [Documented: repo meta-llama/PurpleLlama@172c1074]; report licences [To be verified] |",
          "| [Documented: repo meta-llama/PurpleLlama@172c1074]; licences of the IC3, CISA and NSA reports [To be verified] (agency pages not read); CrowdStrike reports are CC BY-ND 4.0 [Documented: repo CrowdStrike/CyberSOCEval_data@ce7daa5b] (CrowdStrike's repo, not Meta docs) |",
          "T15 (r1)")
    # ---------------------------------------------------------------- Published results
    E.sub("Published results", "| CSE2 prompt injection susceptibility",
          "\"All tested models showed between 26% and 41% successful prompt injections\"; the paper's conclusion says \"ranging from 13% to 47%\" (the two statements differ inside the same paper)",
          "\"All tested models showed between 26% and 41% successful prompt injections\" (abstract and results); the same paper's results give \"between 13% and 47%\" for compliance with requests to attack attached code interpreters, and its conclusion applies \"13% to 47%\" to prompt injection; the conclusion sentence appears to reuse the interpreter-abuse range [Inferred] (premise: the 13% to 47% figure appears in the interpreter-abuse results paragraph)",
          "T87 (r2): the two ranges are explained; the open question moves out")
    E.sub("Published results", "| CSE3 Prompt Guard (first generation)", "threshold \"selected\" by Meta",
          "threshold \"selected\" by Meta (the paper's text and appendix describe the negatives and print no threshold value)", "T82 (r2)")
    E.sub("Published results", "| CSE3 Code Shield and Insecure Code Detector", "\"7 programming languages\"",
          "\"7 programming languages\"; Figure 18 of the same paper shows eight languages on its axis", "T64 (r2)")
    E.sub("Published results", "| Hugging Face leaderboard Space", "last modified 2024-04-18; no figures copied",
          "last modified 2024-04-18, running (Hugging Face runtime stage RUNNING, read 2026-10-09); its page text links only the first and second CyberSecEval papers, so it shows no CSE3 or CSE4 results; no figures copied", "T83 (r2): answered; the open question is deleted")
    # ---------------------------------------------------------------- Red-teaming
    E.sub("Red-teaming", "CyberSecEval is a model-risk test suite, not a red-teaming library for guardrails",
          "**[Documented]** **[Inferred]** (not a guardrail attack library)", INF, "T96 (r2): one label per Summary")
    E.repl("Red-teaming", "Attack content that exists in the repo", [
        "• Attack content that exists in the repo: 15 prompt-injection variants (for example ignore_previous_instructions, token_smuggling, payload_splitting, many_shot_attack, repeated_token_attack), 500 interpreter-abuse prompts and 1,000 MITRE attack-assistance prompts " + PRL + " " + PGT + "CybersecurityBenchmarks/datasets",
        "• No adversarial-suffix generator, jailbreak library or mutation engine for guardrails was found (checked `benchmark/`, `datasets/` and the docs pages) " + ND + " " + PGT + "CybersecurityBenchmarks/datasets"],
        "T99 (r2): a documented fact and an absence were one bullet with two labels", kind="replace")
    E.ins_after("Red-teaming", "The visual prompt injection card says the dataset",
        "• The AlignmentCheck evals dataset card states the same two restrictions: evaluation purposes only, and not for harmful, unethical or malicious purposes **[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]** https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/raw/d50916c9ea26e374667c030268218b28c20626a3/README.md",
        "T16 (r1)")
    # ---------------------------------------------------------------- Engine coverage
    E.sub("Engine coverage", "The runner talks to hosted language-model APIs, and no guardrail sits in its loop",
          "**[Documented: repo meta-llama/PurpleLlama@172c1074]** **[Inferred]** (wrapping route)", INF, "T96 (r2): one label per Summary")
    E.repl("Engine coverage", "Pinned requirements include", [
        "• Pinned requirements include `openai==1.58.1`, `semgrep==1.51.0` and `paramiko==3.4.0`; the Code Shield package asks for `semgrep>1.68` " + PRL + " " + CSB + "requirements.txt",
        "• So one environment cannot satisfy both semgrep pins (premise: 1.51.0 is not greater than 1.68) " + INF + " " + CSB + "requirements.txt",
        "• README side: secure-code benchmarks are \"temporarily removed from the default list\" (CSB/README.md:226) " + PRL + " " + CSB + "README.md",
        "• Code side: `run.py:24,34` import and register `InstructOrAutoCompleteBenchmark`, restored by commit c6dee62 on 2025-01-29, after the note was added on 2025-01-14 " + PRL + " " + CSB + "benchmark/run.py",
        "• Docs-site command example `prompt_injection_multilingual.json` differs from the repo file `prompt_injection_multilingual_machine_translated.json` (website/docs/benchmarks/prompt_injection.md:36) " + PRL + " " + CSB + "website/docs/benchmarks/prompt_injection.md",
        "• The Hugging Face card of the visual injection set links https://meta-llama.github.io/PurpleLlama/docs/benchmarks/prompt_injection, HTTP 404; the working page has /CyberSecEval/ in its path (HTTP 200, observed 2026-10-09) " + DOC + " https://meta-llama.github.io/PurpleLlama/CyberSecEval/docs/benchmarks/prompt_injection"],
        "T75, T99, T85, T86 (r2): the pin conflict split into a fact and its inference; the README-versus-code and docs-versus-file conflicts moved out of Open questions into Detail",
        kind="replace")
    # ---------------------------------------------------------------- Reuse for the test bench
    old = list(E.secs["Reuse for the test bench"])
    E.secs["Reuse for the test bench"] = list(REUSE)
    L._log("eval", "EV Reuse for the test bench", "replace", "\n".join(old), "\n".join(REUSE),
           "T5, R030 (Q-D not decided), R032 (r2 text for the section; r1 text for the licensing and sensitive-content bullets): every bullet is a proposal or a report of possible sources; the CrowdStrike and Hybrid Analysis licences are quoted")
    # ---------------------------------------------------------------- Open questions
    E.sub("Open questions", "Is there a CyberSecEval 4 paper or announcement", "(none found on arXiv, the repo README or dev.meta.ai)",
          "(none found on arXiv, the repo README or dev.meta.ai; an arXiv search for CyberSecEval returned 11 results on 2026-10-09)", "T81 (r2)")
    E.sub("Open questions", "Are the negative (injection-removed) examples used in the CSE3 Prompt Guard evaluation published anywhere", "(not in the repo or the dataset cards checked)",
          "(not in the repo or the dataset cards checked; also checked the Hub datasets of the facebook organisation that match CyberSecEval, which return one, the visual injection set)", "T82 (r2)")
    E.sub("Open questions", "Does the first-generation Prompt Guard threshold Meta \"selected\"", "(checked the paper text, no number stated)",
          "(checked the paper text and appendix, no number stated; also checked the Hub datasets of the facebook organisation that match CyberSecEval)", "T82 (r2)")
    E.delete("Open questions", "Is the Hugging Face leaderboard Space maintained", "T83 (r2): answered in Published results (the Space is running, last modified 2024-04-18, no CSE3 or CSE4 results)")
    E.repl("Open questions", "Is the project still maintained after the 2025-06-12 note",
        "• Whether a next CyberSecEval version is planned (the README note of 2025-06-12 still says the team is exploring options; the folder kept receiving commits to 2026-09-29) " + ND,
        "T84 (r2): the maintenance question is answered from the git history; what remains is the plan", kind="replace")
    E.repl("Open questions", "Do the Instruct and Autocomplete suites run from this commit",
        "• Do the Instruct and Autocomplete suites run from this commit (code read; a run would confirm)? **[To be verified]**",
        "T85 (r2): the conflict itself moved to Engine coverage", kind="replace")
    for a in ("Do the docs and README agree with the files on dataset sizes", "Do the docs-site command examples match the files", "Which providers does the runner support in practice",
              "Does the CSE2 paper's prompt-injection range mean"):
        E.delete("Open questions", a, "T86, T87 (r2): README-versus-file and range conflicts are recorded in Detail or in the Tools and Published results tables; Open questions keep only [To be verified] and [Not disclosed] questions")
    E.repl("Open questions", "Licence of the CrowdStrike CyberSOCEval report data and of the ARVO crash collection",
        "• Licences of the IC3, CISA and NSA reports used for threat intelligence reasoning, of the open-source projects inside the ARVO images, and of the CAPTCHA images in the visual injection set (checked the dataset folders, READMEs, the CrowdStrike and ARVO-Meta licence files and the dataset card; not stated) " + ND,
        "T15 (r1): the CrowdStrike and ARVO licences were found; the rest is Not disclosed with what was checked", kind="replace")
