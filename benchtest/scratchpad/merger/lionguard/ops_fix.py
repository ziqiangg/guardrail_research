"""P7 verifier fixes (lionguard_review.md) plus main's ruling on huggingface.co/api URLs. Applied after ops_cols and ops_inv."""
C = "LN1"
R2L = "**[Documented: repo govtech/lionguard-2@be4e38c9]**"
R21 = "**[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**"
RPB = "**[Documented: repo govtech-responsibleai/playbook@45908b48]**"
DOC = "**[Documented]**"
INF = "**[Inferred]**"


def apply(K, V):
    # ---------------- required 1: R1 Summary entailment
    K.repl(C, 1, 'The playbook says "LionGuard assigns a risk score to each of the categories below"', [
        '• The playbook says "LionGuard assigns a risk score to each of the categories below. Some categories are further classified into severity levels, with Level 2 indicating higher severity than Level 1" ' + RPB],
        "P7 fix 1: R1 Summary (probability per category and severity level) now backed by an R1 bullet; quote extended to the severity-level sentence (27 words)")
    K.ins_after(C, 1, "The LionGuard 2 card says it is", [
        "• The LionGuard 2 card says it \"leverages OpenAI's `text-embedding-3-large` with a multi-head classifier\" " + R2L,
        '• The `predict` docstring of LionGuard 2 says "Predict the probabilities of each label being true" (`lionguard2.py@be4e38c9:148`) ' + R2L],
        "P7 fix 1: embedder (OpenAI) and 'probabilities' facts added to R1 so the Summary is entailed")
    K.ins_after(C, 1, "The LionGuard 2.1 card opens with the same sentence", [
        "• The LionGuard 2.1 card says it \"leverages Gemini's `gemini-embedding-001` with a multi-head classifier\" " + R21],
        "P7 fix 1: embedder (Gemini) fact added to R1 so the Summary is entailed")

    # ---------------- required 2: R7 instruction to the reader
    K.repl(C, 7, "**Minimum setup:** install", [
        "• **Minimum setup:** `transformers`, `torch` and `numpy` installed, the chosen model loaded with `trust_remote_code=True`, each test text embedded with that variant's embedder and passed to `predict`; no threshold ships, so a bench would need to choose one " + INF],
        "P7 fix 2: instruction to the reader ('choose a threshold yourself') reworded (README section 4, R032)")
    K.sub(C, 7, "LionGuard 2 Lite path:",
        "install `sentence-transformers`, log in to Hugging Face and accept Google's conditions for `google/embeddinggemma-300m`, then the classifier and embedder run locally",
        "`sentence-transformers` installed, a Hugging Face login and acceptance of Google's conditions for `google/embeddinggemma-300m`; the classifier and embedder then run locally",
        "P7 fix 2 (optional part): imperative wording removed")

    # ---------------- required 3: line numbers
    K.sub(C, 3, "The `predict` method of LionGuard 2 takes", "`lionguard2.py@be4e38c9:152`", "`lionguard2.py@be4e38c9:151`", "P7 fix 3: line number (text is on line 151)")
    K.sub(C, 3, "`lionguard2.py@1c3a9ea7:152`", "`lionguard2.py@1c3a9ea7:152`", "`lionguard2.py@1c3a9ea7:151`", "P7 fix 3: line number")
    K.sub(C, 3, "`lionguard2lite.py@d56c17a0:152`", "`lionguard2lite.py@d56c17a0:152`", "`lionguard2lite.py@d56c17a0:151`", "P7 fix 3: line number")
    K.sub(C, 4, "Code in LionGuard 2: shared layers", "`lionguard2.py@be4e38c9:119-139`", "`lionguard2.py@be4e38c9:118-138`", "P7 fix 3: layer code spans lines 118 to 138")
    K.sub(C, 4, "The seven heads follow the config", "`lionguard2.py@be4e38c9:172-177`", "`lionguard2.py@be4e38c9:171-176`", "P7 fix 3 (optional part): loop spans lines 171 to 176")
    K.sub(C, 4, "The code has seven head modules", "`lionguard2.py@be4e38c9:172-177`", "`lionguard2.py@be4e38c9:171-176`", "P7 fix 3 (optional part): same citation in the Inferred bullet")
    K.sub(C, 5, "After the averaging step", "`lionguard2.py@be4e38c9:194-196`", "`lionguard2.py@be4e38c9:193-195`", "P7 fix 3: conversion and return are lines 193 to 195")

    # ---------------- main ruling: no huggingface.co/api paths in R9; hints without the API
    for a, why in [("api/models/govtech/lionguard-2.1", "lionguard-2.1"), ("api/models/govtech/lionguard-2-lite", "lionguard-2-lite"), ("api/models/govtech/lionguard-2", "lionguard-2")]:
        K.delete(C, 9, a, "P7 main ruling (as purplellama P5 Q4): Hugging Face API path not cited; the public model page at the pinned revision (tree URL) is already in R9 (" + why + ")")
    for anchor in ["LionGuard 2 classifier size:", "LionGuard 2.1 classifier size:", "LionGuard 2 Lite classifier size:", "The three model repositories were last modified"]:
        K.sub(C, 4, anchor, "(Hugging Face API, read 2026-10-09)", "(Hugging Face Hub metadata of the pinned model page, read 2026-10-09)",
              "P7 main ruling: source hint no longer names the API path; facts and labels unchanged")
    K.sub(C, 7, "The same page shows `License: gemma`",
        "and the Hugging Face API reports `gated` as `manual` for that repository (Google's page and the Hugging Face API, not GovTech docs; read 2026-10-09)",
        "and the Hub metadata of that repository reports `gated` as `manual` (Google's page and Hugging Face Hub metadata, not GovTech docs; read 2026-10-09)",
        "P7 main ruling: source hint no longer names the API path")

    # ---------------- optional (accepted by main)
    K.repl(C, 5, "Category-level F1 in the paper is far lower than binary F1", [
        '• The paper says per-category F1 for all seven moderation systems ranges "from 30-70 %, reflecting the intrinsic difficulty of fine-grained safety labels" (arXiv 2507.15339 section 5.1, Appendix E.3) ' + DOC],
        "P7 optional: the drafter's comparison ('far lower than binary F1') replaced by the paper's own sentence")
    K.sub(C, 4, 'The paper says "LionGuard 2 replaces its predecessor"', "deployed on GovTech's AI Guardian platform",
        "deployed on \"the Singapore Government's AI Guardian platform\"", "P7 optional: the paper's wording, not 'GovTech's'")
    K.sub(C, 4, "The paper limitation says LionGuard 2", 'and that an update to it "may re-training and benchmarking" (arXiv 2507.15339 section 7.1)',
        'and that "Any future update to this embedding model would require may re-training and benchmarking" (as written; arXiv 2507.15339 section 7.1)',
        "P7 optional: full sentence quoted so the fragment does not read as a slip")
    K.sub(C, 5, "The demo's chatbot route flags a message", "(`services.py@4ade46d1:114`)", "(`app/backend/models.py@4ade46d1:12`)",
        "P7 optional: the default is declared in models.py line 12; services.py line 114 is only a fallback value")
    K.add_url(C, "https://huggingface.co/spaces/govtech/lionguard-demo/blob/4ade46d19acee9c9088c711533a7c47fe24a8e3b/app/backend/models.py",
        "P7 optional: models.py cited in R5")
    K.repl(C, 4, "The docstring of the LionGuard 2.1 model file names its own embedder", [
        "• The docstring of the LionGuard 2.1 model file names its own embedder, `gemini-embedding-001` (`lionguard2.py@1c3a9ea7:97`) " + R21],
        "P7 optional: the conclusion 'occurs only in the LionGuard 2 file' also rests on the Lite file, so it moves to its own Inferred bullet")
    K.ins_after(C, 4, "The docstring of the LionGuard 2 Lite model file names its own embedder", [
        "• The stale name therefore occurs only in the LionGuard 2 file (premise: the 2.1 and Lite docstrings at line 97 name their own embedders) " + INF],
        "P7 optional: Inferred bullet with its premise")
    K.sub(C, 4, "Training code or an inference repository on GitHub",
        "`git ls-remote` for govtech-responsibleai/lionguard and /lionguard-demo, both \"Repository not found\"",
        "`git ls-remote` for govtech-responsibleai/lionguard, /lionguard-demo, /lionguard2 and /LionGuard, each \"Repository not found\"",
        "P7 optional: the four GitHub paths checked, as in the inventory (d) intro")
    K.repl(C, 4, "Serving route: self-host from Hugging Face", [
        '• Serving route: the playbook says the versions are "open-sourced for self-hosting via Hugging Face" ' + RPB,
        '• A blog says embedding generation "can be run locally or through an API depending on the variant" (GovTech AI blog, 28 Sep 2026) ' + DOC],
        "P7 optional: playbook fact and blog fact split so each has its own label (the playbook half gets its repo label)")
    K.sub(C, 7, "returned HTTP 403 to the fetch tool", "returned HTTP 403 to the fetch tool", "returned HTTP 403 to a plain GET",
        "P7 optional: less process wording")
    K.sub(C, 8, "Whether OpenAI's usage policies and service terms", "the owners' data-handling pages are quoted in R7; ", "",
        "P7 optional: internal cross-reference 'quoted in R7' dropped")
    K.ins_after(C, 8, "Which of the paper's Table 1 and Table 3 column orders is right", [
        "• Table 1 of the LionGuard 2 paper prints Test 87.2 for Qwen3-Embedding-0.6B, above 77.0 for text-embedding-3-large, while section 4.2.1 says text-embedding-3-large \"achieved the highest binary F1\" (checked the paper html; not explained; needs the authors)"],
        "P7 optional: a clash between Table 1 and the section 4.2.1 claim, recorded as an R8 question (no label)")
    K.summary_text(C, 9, "model repos, dataset and demo Space", "model repos, datasets and demo Space", "P7 optional: R9 cites two datasets")

    # ---------------- inventory
    V.sub("e", "Hosted API behaviour", "What this sheet adds", V.cell_get("e", "Hosted API behaviour", "What this sheet adds"),
        "The README usage loads the classifier from Hugging Face and calls predict locally on embeddings that the user generates with their own OpenAI key [Documented: repo govtech/lionguard-2@be4e38c9] (README usage). "
        "The 2.1 card does the same with the user's own Gemini key [Documented: repo govtech/lionguard-2.1@1c3a9ea7] (README usage), and the Lite card with a local google/embeddinggemma-300m embedder [Documented: repo govtech/lionguard-2-lite@d56c17a0] (README usage). "
        "Self-hosted use therefore involves no Sentinel endpoint or Sentinel key; the embedder key or the gated Gemma download takes its place [Inferred] (premise: none of the three README usage blocks calls a Sentinel endpoint)",
        "P7 fix 4: the inference no longer sits under one repo's Documented label; one Documented fact per repo plus one Inferred conclusion with its premise")
    V.para_sub("published as open models on the Hugging Face org govtech", "published as models on the Hugging Face org govtech",
        "P7 fix 5: 'open' dropped (depends on the unresolved licence reading)")
    V.para_sub("are not GovTech docs. No embedding service was called and no weights were downloaded.", "are not GovTech docs.",
        "P7 optional: research-method sentence removed from a built block intro")
    V.sub("d", "govtech/lionguard-demo:", "Licence or access", "Reference only; no text was submitted to the hosted Space", "Reference only",
        "P7 optional: research-method statement removed from a built cell")
    V.sub("d", "arXiv 2507.15339 LionGuard 2:", "Artefact", "Data-Efficient and Localised", "Data-Efficient & Localised",
        "P7 optional: arXiv title verbatim ('&' is allowed in cells)")


def apply_post_p8(K, V):
    K.repl(C, 5, "The original test split is private, so the 0.7318 figure", [
        '• The blog says it used "the same benchmarks used in our earlier LionGuard experiments: a held-out private LionGuard test split and RabakBench", and elsewhere calls the set "the original LionGuard 2 Test set" and "our private LionGuard 2 Test dataset" (GovTech AI blog, 28 Sep 2026) ' + DOC,
        "• Whether the blog's held-out private test split is the test set behind the paper's 77.0 for LionGuard 2 (checked the blog, the paper and the playbook; not stated) **[Not disclosed]**"],
        "Post-P8 fix (P10 verifier Q1): the [Inferred] claim that 0.7318 'cannot be compared directly' with 77.0 is contradicted by the blog's own wording; replaced by the blog's description quoted [Documented] and a [Not disclosed] bullet")
    V.sub("a", "=LionGuard 2.1", "Operating threshold",
        "(B3 Moderation Performance table; comparator columns omitted).",
        "(B3 Moderation Performance table; comparator columns omitted). B3 says it used \"the same benchmarks used in our earlier LionGuard experiments\" and calls the set the original LionGuard 2 Test set [Documented] (B3). Whether that private split is the test set behind the paper's 77.0 for LionGuard 2 [Not disclosed] (B3, P2 and PB checked).",
        "Post-P8 fix (P10 verifier Q1): inventory aligned with the column; the blog's own description and a Not disclosed statement on whether the split is the paper's test set")
