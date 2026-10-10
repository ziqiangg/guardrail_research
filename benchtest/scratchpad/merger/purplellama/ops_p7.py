"""P7 fix loop: required fixes 1 to 7 and the optional suggestions of purplellama_review.md. Reasons start with 'P7 fix n' or 'P7 opt n'."""
import merge_lib as L

PR = "**[Documented: repo meta-llama/PurpleLlama@172c1074]**"
DOC = "**[Documented]**"
INF = "**[Inferred]**"
G86 = "**[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**"
EVALS = "**[Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]**"


def apply_cols(K):
    # fix 1: PL7 R4 threshold bullet
    K.repl("PL7", 4, "The constructor takes `scanner_name` and `block_threshold` (default 1.0)", [
        "• The constructor takes `scanner_name` and `block_threshold` (default 1.0), and the scan returns `BLOCK` when the score is at or above the threshold (`hidden_ascii_scanner.py@172c1074:20-26,50-56`) " + PR,
        "• Because the score is only 1.0 or 0.0, any threshold above 0.0 and up to 1.0 behaves like the default, a threshold above 1.0 never blocks, and a threshold of 0.0 or below blocks every message (premise: the comparison score >= block_threshold at line 55) " + INF],
        "P7 fix 1: the drafted claim 'a threshold of 1.0 or lower behaves the same' was wrong (score >= threshold, so 0.0 or below blocks everything) and was an inference under a Documented label", kind="replace")
    # fix 2: PL3 R4 deprecation bullet
    K.ins_after("PL3", 4, "Hosting: the code points at Together AI",
        "• Together's deprecation history (not Meta docs, read 2026-10-09) lists `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` among models removed from serverless inference, removal date 2026-03-31; R6 gives the details " + DOC,
        "P7 fix 2: the R4 Summary clause 'which Together lists as removed from serverless inference' had no R4 bullet (the fact was only in R6)")
    # fix 5: PL1 R2 language conflict, R8 question, Summary
    K.ins_after("PL1", 2, "Languages evaluated:",
        '• Source conflict, language count (paper side): the paper\'s multilingual set is "the same dataset machine-translated into eight additional languages", one more than the seven non-English languages the card lists; the paper names none of them (arXiv 2505.03574 appendix A.2) ' + DOC,
        "P7 fix 5: unrecorded source conflict (README section 3 rule 4)")
    K.ins_after("PL1", 8, "The paper prints an 86M English AUC",
        "• Which languages the paper's \"eight additional languages\" are, given that the card lists seven besides English (checked the card and the paper; not stated)",
        "P7 fix 5")
    K.summary_text("PL1", 2, "and eight languages were evaluated.", "and the card lists eight evaluated languages.",
                   "P7 fix 5: the language count is no longer stated as settled (37 words)")
    # optional
    K.summary_text("PL1", 4, "**Small DeBERTa classifiers, run locally.**", "**Small DeBERTa classifiers, run locally (the 86M model is also on Hugging Face's hosted inference).**",
                   "P7 opt: the same row documents the hosted route for the 86M model")
    K.ins_after("PL1", 6, "Access: the weights are gated",
        "• Access is approved manually (\"manual\" gate in the Hub metadata) " + G86,
        "P7 opt: supports 'approved gated access' in the R6 Summary (the fact was only in R4)")
    K.ins_after("PL3", 5, "The card lists per-case fields",
        '• The dataset card says "This dataset should not be used to train models and should be for evaluation purposes only" (dataset card at revision d50916c9) ' + EVALS,
        "P7 opt: the restriction used in R7 and in the eval Red-teaming section now rests on a Detail bullet of the same column")
    K.sub("PL4", 4, "The PyPI 1.0.1 sdist differs from the pinned CodeShield folder in nine Python files",
          "file-by-file comparison of the unpacked sdist PyPI sdist codeshield-1.0.1, sha256 61866b92, read 2026-10-09 with the pin",
          "file-by-file comparison of the unpacked sdist (PyPI sdist codeshield-1.0.1, sha256 61866b92, read 2026-10-09) with the pin", "P7 opt: garbled wording", kind="style")
    for c in ("PL4", "PL6"):
        K.gsub(c, 2, "the CyberSecEval rule set gives 62 and all rule files 64", "the CyberSecEval rule set gives 62 for the eight default languages (64 over all its languages) and all rule files 64",
               "P7 opt: 62 is the count for the eight default languages; 64 over all its languages (T67)", kind="edit")
    K.sub("PL7", 5, "Result: `BLOCK`, score 1.0, status `SUCCESS`, reason \"Hidden ASCII", "172c1074:19,52-72", "172c1074:19,52-69",
          "P7 opt: the file has 69 lines", kind="edit")
    K.sub("PL2", 4, "The pinned code is newer than release 1.0.3", "and promptguard_utils.py changed on 2026-01-16 (e4c281b) and 2026-03-26 (9a3d175)",
          "and promptguard_utils.py changed on 2026-01-16 (e4c281b) and 2026-03-26 (9a3d175), among other commits", "P7 opt: the list of later changes is not exhaustive (a formatting commit e9983e6 also exists)", kind="edit")


def apply_inv(V):
    # fix 3
    V.sub("b", "REGEX", "Mechanism",
          "No constructor argument takes other patterns; replacing scanner.patterns after construction would work [Inferred]",
          "No constructor argument takes other patterns (lines 41-45) [Documented: repo meta-llama/PurpleLlama@172c1074]; replacing scanner.patterns on one instance does not persist through LlamaFirewall, which creates a new scanner on every scan call [Inferred] (premise: llamafirewall.py lines 117-118)",
          "P7 fix 3: contradicted PL5 R4 (new scanner per scan call)")
    # fix 4
    old = V.cell_get("g", "AlignmentCheck (paper)||Recall", "Benchmark and conditions")
    V.sub("g", "AlignmentCheck (paper)||Recall", "Benchmark and conditions", old,
          "In-house goal hijacking benchmark of 600 scenarios, 300 benign and 300 malicious [Documented] (PAPER Appendix A.1); the paper links the Hugging Face dataset facebook/llamafirewall-alignmentcheck-evals [Documented] (PAPER Appendix A.1); the dataset card says 577 test cases with six model responses each [Documented: repo facebook/llamafirewall-alignmentcheck-evals@d50916c9]; the two counts conflict and are recorded without picking one; AlignmentCheck is described as an experimental feature [Documented]",
          "P7 fix 4: the paper's 600, 300 and 300 were under the dataset repo label; one labelled fact per source (README section 3 rule 4)")
    V.url_add("g", "AlignmentCheck (paper)||Recall", ["https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/tree/d50916c9ea26e374667c030268218b28c20626a3"],
              "P7 fix 4: the repo label needs its pinned URL")
    # fix 7
    old = V.cell_get("b", "HIDDEN_ASCII", "Maturity")
    V.sub("b", "HIDDEN_ASCII", "Maturity", old,
          "Not marked experimental in code and not listed in the README components [Not disclosed] (searched LlamaFirewall/src, the README and the docs pages for experimental)",
          "P7 fix 7: an absence is [Not disclosed] (README section 3 rule 2), as block (a) already writes it")
    V.sub("e", "Hugging Face gated-access request", "Status", "(Hugging Face model API, observed 2026-10-09)", "(Hugging Face Hub model metadata, observed 2026-10-09)",
          "P7 fix 7: leftover of the 'HF API' phrase change")
    # optional
    V.sub("b", "AGENT_ALIGNMENT", "Default block threshold",
          "the inherited block_threshold of 0.0 is not used there [Inferred]",
          "the inherited block_threshold of 0.0 is not read by the scanner, whose decision tests score == 1.0 [Documented: repo meta-llama/PurpleLlama@172c1074] (custom_check_scanner.py line 39; alignmentcheck_scanner.py line 128)",
          "P7 opt: aligned with PL3 R5, which labels the same fact [Documented: repo]")
    V.sub("e", "Automatic model download", "Caveats", "offline use with a pre-populated folder [Not disclosed]",
          "the folder name and layout the code expects (meta-llama--Llama-Prompt-Guard-2-86M under HF_HOME) [Not disclosed]",
          "P7 opt: the README does document a preload route (T42), so the absence is about the layout")
    V.sub("f", "Prompt Guard 1 (legacy)", "Gating or acceptable-use terms", ". the Hugging Face repo file list", ". The Hugging Face repo file list", "P7 opt: capital letter", kind="style")


def apply_ev(E):
    # fix 6
    E.sub("Engine coverage", "README side: secure-code benchmarks", "(CSB/README.md:226)", "(CSB/README.md:227)", "P7 fix 6: the note is on line 227 at the pin")
    E.sub("Tools", "| Instruct (`--benchmark=instruct`)", "; the note is a leftover, git history read 2026-10-09)",
          ", git history read 2026-10-09); the note appears to be a leftover [Inferred]", "P7 opt: the judgement gets its own [Inferred] statement")
