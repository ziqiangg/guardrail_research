from gen_b import *

# ---------------- (f)
hf_ = ["Component", "Licence as stated", "Gating or acceptable-use terms", "Conflict or note", "Source URL"]
rf = [
    ["Prompt Guard 2 (86M and 22M)",
     f"Llama 4 Community Licence: the folder LICENSE files begin LLAMA 4 COMMUNITY LICENSE AGREEMENT, Version Effective Date April 5, 2025 (86M/LICENSE and 22M/LICENSE) {R}; HF metadata license other, license_name llama4 {H86}; the gate page shows License: llama4 {D}",
     f"Llama 4 Acceptable Use Policy (86M/USE_POLICY.md and 22M/USE_POLICY.md) {R}. Hugging Face gated manual; the gate asks for a full legal name, date of birth and full organisation name with corporate identifiers {D} (86M gate page, observed 2026-10-09)",
     f"The Prompt Guard 2 README says The same license as Llama 4 applies and links ../LICENSE, which is the root file and is the Llama 3.2 agreement, while the folder LICENSE files are Llama 4 {R}. The root README licence table has no Prompt Guard 2 row {R}. Which text governs a given download is a legal question {TBV}",
     f"{B}Llama-Prompt-Guard-2/README.md ; {B}Llama-Prompt-Guard-2/86M/LICENSE ; {B}Llama-Prompt-Guard-2/86M/USE_POLICY.md ; {B}Llama-Prompt-Guard-2/22M/LICENSE ; {B}LICENSE ; https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M"],
    ["Prompt Guard 1 (legacy)",
     f"Hugging Face tag license:llama3.1 and the gate page shows LLAMA 3.1 COMMUNITY LICENSE AGREEMENT {D}; the Prompt-Guard README says The same license as Llama 3 applies {R}; the root README licence table says Llama 3.2 Community License for Prompt Guard {R}",
     f"Hugging Face gated manual {HV1}; the folder README points to a USE_POLICY.md that is not in the Prompt-Guard folder {R} (file list of the folder: README.md, MODEL_CARD.md, image)",
     f"Three licence versions for one model: Llama 3 (folder README), Llama 3.1 (Hugging Face tag and gate page) and Llama 3.2 (root README table and root LICENSE); recorded without picking one",
     f"{B}Prompt-Guard/README.md ; {B}README.md ; {B}LICENSE ; https://huggingface.co/meta-llama/Prompt-Guard-86M"],
    ["LlamaFirewall",
     f"MIT: LlamaFirewall/LICENSE begins MIT License, Copyright (c) Meta Platforms, Inc. and affiliates {R}",
     f"None for the code. The default PromptGuard scanner downloads the gated Prompt Guard 2 86M model, so the Llama 4 terms apply to that model {I} (premise: promptguard_utils.py line 40 names the gated repo)",
     f"No row for LlamaFirewall in the root README licence table {R}; that table lists Evals/Benchmarks, Safeguard Llama Guard and Prompt Guard, and Code Shield only",
     f"{B}LlamaFirewall/LICENSE ; {B}README.md"],
    ["Code Shield (CodeShield and Insecure Code Detector)",
     f"MIT: CodeShield/LICENSE begins MIT License {R}; the root README licence table lists Code Shield as MIT {R}",
     f"None stated {ND} (checked CodeShield/README.md, the ICD README and LICENSE)",
     f"The package pins semgrep above 1.68 (CodeShield/pyproject.toml line 15) {R}; see the Semgrep row",
     f"{B}CodeShield/LICENSE ; {B}README.md ; {B}CodeShield/pyproject.toml"],
    ["CyberSecEval (CybersecurityBenchmarks)",
     f"MIT: CybersecurityBenchmarks/LICENSE begins MIT License {R}; the root README says evals and benchmarks are licensed under the MIT license while any models use the corresponding Llama Community license {R}",
     f"None stated for the code {ND} (checked the README and LICENSE). Datasets carry third-party provenance: datasets/third-party.txt lists third-party repositories used for benchmarking with their licences {R}",
     f"The benchmark runs against provider APIs (OpenAI, Anthropic, Together and others) whose terms are the providers' own {I}",
     f"{B}CybersecurityBenchmarks/LICENSE ; {B}CybersecurityBenchmarks/datasets/third-party.txt ; {B}README.md"],
    ["Semgrep (dependency of codeshield; third-party)",
     f"The Semgrep repository LICENSE file on its develop branch is the GNU Lesser General Public License, Version 2.1 {D} (Semgrep's own repository, not Meta docs; read 2026-10-09, unpinned)",
     f"Not Meta terms; Semgrep's own terms for its rules and registry are not read here {TBV}",
     f"Meta's pyproject requires semgrep above 1.68 and the Insecure Code Detector invokes the semgrep-core binary (oss.py lines 48-74, 84-96) {R}; whether the LGPL has consequences for a test bench that installs codeshield is a licensing question {TBV}",
     f"{B}CodeShield/pyproject.toml ; {B}CodeShield/insecure_code_detector/oss.py ; https://github.com/semgrep/semgrep/blob/develop/LICENSE"],
    ["Together-hosted models behind AlignmentCheck, PIICheck and CustomCheckScanner (third-party service)",
     f"The Together terms of service (Together's page, not Meta docs) say models may come with their own terms and conditions: Such models may come with their own terms and conditions {D} (read 2026-10-09); the Llama 4 Maverick and Llama 3.3 model licences are separate Llama licences and were not read here {TBV}",
     f"Together terms: a user setting can enable Zero Data Retention, under which data and outputs are not stored, retained, or used for model training {D} (Together terms of service, not Meta docs). Meta files do not mention it {ND} (checked README, docs pages and code)",
     f"Testing AlignmentCheck sends agent traces, and PIICheck sends message text, to the Together API by default {R}; data-protection implications for the bench are a decision for the project owner",
     f"https://www.together.ai/terms-of-service ; {B}{SC}custom_check_scanner.py ; {B}{SC}experimental/piicheck_scanner.py"],
    ["Llama Guard 1, 2, 3 and 4 (cross-reference)",
     "Not restated here: licences, gating and terms for Llama Guard are recorded on sheet 3d and in columns V to Z",
     "See sheet 3d",
     "The Purple Llama root README licence table lists Llama Guard versions with their Llama Community Licence versions (root README lines 37-41)",
     f"{B}README.md"],
]
assert len(rf) == 8

# ---------------- (g)
hg = ["Component", "Metric", "Value", "Benchmark and conditions", "Source URL"]
CARD = f"{B}{PGC}"
rg = [
    ["Prompt Guard 2 86M",
     "AUC (English); recall at 1% FPR (English); AUC (multilingual); latency per classification",
     f".998; 97.5%; .995; 92.4 ms (PG2C table, lines 71-74) {R}. The paper table prints .98 for the 86M English AUC and the same values for the other cells (PAPER section 4.1) {D}; conflict, the card figure is the one quoted here",
     f"Private benchmark built with datasets distinct from the training data (card line 69) {R}; latency on an A100 GPU at 512 tokens {R}. Benchmark size and class balance {ND} (checked the card and paper Appendix A.2)",
     f"{CARD} ; {ARXIV}"],
    ["Prompt Guard 2 22M",
     "AUC (English); recall at 1% FPR (English); AUC (multilingual); latency per classification",
     f".995; 88.7%; .942; 19.3 ms (22M card, same table row) {R}",
     f"Same private benchmark and A100 conditions {R}; the card says the 22M model reduces latency and compute costs by 75% with minimal performance trade-offs (line 16) {R}",
     f"{B}Llama-Prompt-Guard-2/22M/MODEL_CARD.md ; {ARXIV}"],
    ["Prompt Guard 2 86M and 22M",
     "Attack prevention rate (APR) at 3% utility reduction on AgentDojo",
     f"86M 81.2%; 22M 78.4% (card lines 83-87) {R}",
     f"AgentDojo agentic environment; the paper says a threshold is chosen for each model that produces a fixed, minimal utility reduction (3%) {D} (PAPER section 4.1)",
     f"{CARD} ; {ARXIV}"],
    ["Prompt Guard 1 (comparator only)",
     "Same four metrics and APR from the same card table",
     f"AUC English .987; recall at 1% FPR 21.2%; AUC multilingual .983; 92.4 ms; APR 67.6% (card lines 73 and 85) {R}",
     f"Same private benchmark and conditions as the Prompt Guard 2 rows; comparator rows are not Summary material {R}",
     f"{CARD}"],
    ["PromptGuard V2 86M and 22M (paper)",
     "AgentDojo attack success rate (ASR) and utility",
     f"No defence: ASR 17.6%, utility 47.7%. PromptGuard V2 86M: ASR 7.5% (a 57% drop), utility 47.0% {D} (PAPER section 4.3.2). 22M: a 41% drop in ASR with no utility degradation {D} (PAPER Appendix B.2)",
     f"Static replays of ten agent models from the AgentDojo paper; the paper notes AgentDojo mainly targets important instructions attacks and PromptGuard alone may not suffice elsewhere {D}",
     f"{ARXIV}"],
    ["AlignmentCheck (paper)",
     "Recall and false positive rate on Meta's indirect goal hijacking benchmark",
     f"Over 80% recall with a false positive rate below 4% for Llama 4 Maverick and Llama 3.3 70B without fine-tuning {D} (PAPER section 4.2); Llama 4 Maverick over 83% detection with a false positive rate of 2.5% {D} (PAPER Appendix C.2)",
     f"In-house goal hijacking benchmark (the paper points to a Hugging Face dataset named facebook/llamafirewall-alignmentcheck-evals, not read) {D}; AlignmentCheck is described as an experimental feature {D}",
     f"{ARXIV}"],
    ["AlignmentCheck (paper)",
     "AgentDojo ASR and utility with Llama 4 Maverick as the auditor",
     f"ASR 2.89% (an 84% drop from 17.6%) at the cost of lower utility (43.1%) and significantly higher latency; PromptGuard plus AlignmentCheck ASR 1.75% with utility 42.7% {D} (PAPER section 4.3.2)",
     f"Same AgentDojo replays as the Prompt Guard row; no AlignmentCheck latency figure is given {ND} (checked the paper, README, docs pages and code)",
     f"{ARXIV}"],
    ["CodeShield (paper)",
     "Precision and recall of insecure-code detection",
     f"Precision 96% and recall 79% {D} (PAPER section 4.4)",
     f"Evaluated in CyberSecEval 3 on manual labels of 50 LLM-generated code completions per language across several languages; the languages are not listed in that sentence {D}",
     f"{ARXIV}"],
    ["CodeShield latency statement 1: CodeShield README",
     "Share of traffic and latency",
     f"Over 98% of traffic is classified as benign; in approximately 99% of cases requests are processed within 70ms; for the remaining traffic the p90 latency is 450ms (CodeShield/README.md line 27) {R}",
     f"Described as studies in production environments, with modern production server environments for the p90 figure; no latency or timeout value appears in the code {ND} (grep of CodeShield and LlamaFirewall/src Python files)",
     f"{B}CodeShield/README.md"],
    ["CodeShield latency statement 2: LlamaFirewall docs page",
     "Two-tier latency",
     f"First tier under 100 milliseconds; second layer around 300 milliseconds; approximately 90% of inputs fully resolved by the first layer with typical end-to-end latency under 70 milliseconds; the remaining 10% can exceed 300 milliseconds (code-shield.md lines 11 and 13) {R}",
     f"Internal production deployments {R}; confirmed in the pinned file and on the docs site page documentation/scanners/code-shield",
     f"{B}{LFD}documentation/scanners/code-shield.md ; {LFDOC}documentation/scanners/code-shield"],
    ["CodeShield latency statement 3: LlamaFirewall paper",
     "Two-tier latency",
     f"First tier approximately 60 milliseconds; second layer around 300 milliseconds; approximately 90% resolved by the first layer, typical end-to-end latency under 70 milliseconds; remaining 10% can exceed 300 milliseconds {D} (PAPER section 4.4)",
     f"Internal production deployments {D}; differs from statement 2 on the first-tier figure (approximately 60 versus under 100)",
     f"{ARXIV}"],
    ["CodeShield latency statement 4: llama.com protections page",
     "Average latency",
     f"Code Shield provides support for inference-time filtering of insecure code produced by LLMs for 7 programming languages with an average latency of 200ms {D} (LLAMA page, read 2026-10-09)",
     f"Conditions not stated {ND} (checked the page); the four statements differ and none is Meta's single figure, so latency on the bench needs testing",
     f"{LLAMA_URL}"],
]
assert len(rg) == 12

# ---------------- (h)
hh = ["Item", "What it is", "Relationship to Table 3", "Where covered", "Source URL"]
rh = [
    ["Llama Guard 3 and 4",
     f"Meta's input and output safety classifiers in the Llama-Guard3 and Llama-Guard4 folders of this repository {R}",
     "Cross-referenced only; they have Table 3 columns of their own",
     "Table 3 columns V to Z, sheet 3d and the diagram llama-guard-explained.html",
     f"{T}Llama-Guard3 ; {T}Llama-Guard4"],
    ["Llama Guard 1, 2 and 3 folders (legacy versions)",
     f"Earlier Llama Guard releases kept in the repository (folders Llama-Guard, Llama-Guard2, Llama-Guard3) {R}",
     "Legacy versions of a product that already has columns; not restated",
     "Sheet 3d",
     f"{T}Llama-Guard ; {T}Llama-Guard2 ; {T}Llama-Guard3"],
    ["CyberSecEval",
     f"Benchmark suite for LLM cybersecurity risks and defensive capabilities; CyberSecEval 4 is the current version in the repo {R}",
     "Not a guardrail and not a Table 3 column; some test data may seed guardrail tests {I} (premise: the suite includes prompt injection and secure-code data)",
     "Evaluation-tooling sheet for CyberSecEval (proposed 3j) and block (a) row CyberSecEval 4",
     f"{B}CybersecurityBenchmarks/README.md ; https://meta-llama.github.io/PurpleLlama/CyberSecEval/"],
    ["CyberSecEval docs-site Prompt Guard pages",
     f"CybersecurityBenchmarks/website/docs/prompt_guard/model_card.md is byte-identical to Prompt-Guard/MODEL_CARD.md (cmp), and overview.md carries the Prompt Guard 1 quick-start text {R}",
     "Stale copy of the legacy Prompt Guard 1 card; not evidence for Prompt Guard 2",
     "Block (a) row Prompt Guard 1 (legacy)",
     f"{B}CybersecurityBenchmarks/website/docs/prompt_guard/model_card.md ; {B}CybersecurityBenchmarks/website/docs/prompt_guard/overview.md ; {B}Prompt-Guard/MODEL_CARD.md"],
    ["Purple Llama root README",
     f"Umbrella statement: Purple Llama is an umbrella project that over time will bring together tools and evals to help the community build responsibly with open generative AI models; it holds the licence table and the Prompt Guard, Code Shield and CyberSecEval summaries {R}",
     f"Frames the project; it does not mention LlamaFirewall or Prompt Guard 2 {ND} (searched the file for Firewall and for Prompt Guard 2)",
     "Block (f) licences; block (a) family names",
     f"{B}README.md"],
]
assert len(rh) == 5

# ---------------- assemble
BLOCKS = [
    ("## (a) Components and variants", None, ha, ra),
    ("## (b) LlamaFirewall scanner catalogue", None, hb, rb),
    ("## (c) Roles, use cases and default scanner map", f"A LlamaFirewall Configuration maps each Role to a list of scanner types or registered names (config.py line 13) {R}. Default (CP1 question Q-C): one column per scanner with the roles listed here in Detail; the same scanner class can be attached to any role {I} (premise: scan() looks up scanners by input.role and create_scanner builds the class, llamafirewall.py lines 108-122). Message.tool_calls exists, but no scanner reads it, so tool-call arguments are not scanned {I} (premise: grep of src for tool_calls). scan() chooses BLOCK if any scanner returned BLOCK, otherwise the decision with the highest score (lines 143-155); scan_async returns the first BLOCK or HUMAN_IN_THE_LOOP_REQUIRED (lines 174-181) {R}.", hc, rc),
    ("## (d) Code Shield language and analyzer matrix", d_intro, hd, rd),
    ("## (e) Integration and access paths", None, he, re_),
    ("## (f) Licences, gating and terms", None, hf_, rf),
    ("## (g) Published metrics and latency statements", f"All numbers are quoted from the card file at the pin, the Meta pages or the paper; none is a Meta recommendation for a decision threshold {ND} (checked the card, README, dev.meta.ai pages and the paper). The latency statements below are four different statements, not one figure.", hg, rg),
    ("## (h) Adjacent and cross-reference items", None, hh, rh),
]
out = [intro, ""]
for title, note, hdr, rows in BLOCKS:
    out.append(title)
    out.append("")
    if note:
        out.append(note)
        out.append("")
    out.append(table(hdr, rows))
    out.append("")
out.append("""## Reviewer notes

1. Source conflicts recorded in the cells, each side with its own label: Code Shield language count 8 (code, ICD README, LlamaFirewall README and docs page) versus 7 (CodeShield README, llama.com, paper section 4.4), and the paper also says 8 and eight (block d intro); four CodeShield latency statements (block g); PROMPT_INJECTION (docs use-case page) versus PROMPT_GUARD (enum) (blocks b and c); BaseScanner (docs) versus Scanner (code) (block b); Prompt Guard 2 86M English AUC .998 (card) versus .98 (paper table) (block g); Prompt Guard 1 and 2 licence statements (block f); codeshield version 0.0.1 in the repo versus 1.0.1 on PyPI (block a); the Prompt Guard 2 README licence link target (block f).
2. Findings beyond the brief: PHP has Semgrep rules but the analyzer map lists only the regex analyzer for PHP, so those rules do not run through analyze() (block d, labelled Inferred); Rust has a 13-pattern regex file but config.yaml enables none for the codeshield use case; PIICheck fails open on an LLM error while AlignmentCheck fails closed (block b); llamafirewall configure accepts TOGETHER_API_TOKEN but the client reads TOGETHER_API_KEY (block e); the CyberSecEval --enable-lf flag is stored but not used in the .py files (block e).
3. Row counts: (a) 16, (b) 8, (c) 11, (d) 16, (e) 12, (f) 8, (g) 12, (h) 5; each equals the brief target, so the owner of the inventory config module needs no change to the counts in the brief.
4. Not read or not reachable: the Hugging Face card bodies of the three gated repos (HTTP 401 for raw files; the 86M and 22M gate pages and the v1 gate page were read); the sdists of the PyPI releases; the llama-cookbook notebook and inference script (links returned 200 but content was not read); facebookresearch/llama-recipes; the Together model pages for the Llama 4 Maverick and Llama 3.3 licences; Semgrep's rule licences. The Hugging Face connector disconnected during the run, so revisions were read from the public model API with fetch_text.py.
5. Pages read with fetch_text.py: llama.com protections (redirects to dev.meta.ai), the Prompt Guard docs page (redirect), arXiv html 2505.03574, the three Hugging Face gate pages and API records, PyPI simple indexes, the Together terms of service and the Semgrep LICENSE raw file. No fact comes from a summarising fetch. Repository facts were read from the shallow clone at 172c1074 and checked with grep and small counting scripts; nothing was run or installed.
6. Counts in block d (patterns per regex file, enabled rules per config.yaml, yaml files per Semgrep folder, rules per generated JSON) were produced by a short script over the pinned files; they are mechanical counts, labelled as counted.
7. Judgement calls: SYSTEM and MEMORY rows in block c list the five LlamaFirewall scanner headers in Covered by because any scanner can be attached; ClassifyIt and CyberSecEval 4 use the inventory-only marker; the Llama Guard row in block f is plain text with no label; Semgrep is labelled Documented because it is the owner's repository file read unpinned on the develop branch.
""")
open("C:/Users/cys-c/Desktop/gzqr/gitubrepo/misc/researchrail/guardrail_research/benchtest/drafts/purplellama_inventory.md", "w", encoding="utf-8").write("\n".join(out))
print("written", {t.split(')')[0]: len(r) for t, _, _, r in BLOCKS})
