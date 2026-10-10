"""Static text for lionguard_changes.md."""

INTRO = (
    "Inputs merged: lionguard_brief.md, lionguard_cols_a.md (LN1), lionguard_inventory.md, lionguard_triage.md (59 items), "
    "lionguard_resolutions_1.md (39 items: 34 class a, 5 class c), the rulings R005, R007, R009, R011, R015, R019, R020, R021, R031 (lionguard CP1) and R032 "
    "(bench content worded as proposals), and main's rulings in scratchpad/main/queue.md (rows starting 'lionguard': arXiv 2507.05980 official and added as the 11th row of inventory block (d); "
    "third-party facts limited to embedder identity plus gating, licence and terms, each marked 'not GovTech docs'; demo Space reference only with its data-flow fact in R5 and R7; "
    "the two licence texts kept as separate labelled bullets; R8 carries no labels). "
    "Outputs: lionguard_two_level.md, lionguard_inventory_final.md, lionguard_changes.md (this file), lionguard_summaries_preview.md. "
    "LionGuard has no evaluation-tooling sheet, so there is no lionguard_eval_tooling.md. "
    "No source file was modified and no new web or repository research was done; every added fact is in the resolutions file or in a ruling. "
    "Merged 2026-10-10 by gr-merger with the scripts in benchtest/scratchpad/merger/lionguard/.\n\n"
    "In this file bold markers are dropped from quoted text and long text is shortened. Reason codes: Tn = triage id (resolution in lionguard_resolutions_1.md), "
    "'style n' = triage Style issues in columns, 'hygiene' = triage Label hygiene or a merger-found hygiene fix, 'main P4 Qn' / 'main P5 Q-x' = main's rulings, 'Rnnn' = ruling. "
    "Kinds: summary, replace, edit, add, delete, url (R9 or Source URL cell), style. Format of the entries: location | before | after | reason."
)

GLOBAL = [
    ("Reviewer notes sections (column draft, inventory draft, inventory self-check)", "present in the drafts", "removed from lionguard_two_level.md and lionguard_inventory_final.md; kept verbatim in section 7", "README section 4"),
    ("Column set and header", "one column LN1 (CP1 default)", "one column LN1 'LionGuard: Localised harmful-content classification'; prefix 'LionGuard:'; variant differences stay as named per-variant bullets", "T1, T2 (R031 Q01, Q02; R009)"),
    ("Self-hosting framing and embedder dependencies", "R1 Summary 'you run it yourself from open Hugging Face weights'; R7 Summary 'no API key' for Lite", "R1 Summary says GovTech publishes the classifier and that two variants embed through OpenAI or Gemini; R7 Summary adds the Hugging Face login and the Gemma terms; the outside-service and gate dependencies are stated in R7 and inventory block (c)", "T3, T49, T51 (R031 Q03)"),
    ("Bench content worded as proposals (R032)", "R7 test plan in the imperative ('Add noisy variants', 'Sweep thresholds'), 'that is a data-handling decision for the bench', 'this is the plan for the bench', 'a bench-design choice for the user', 'Pinning a revision for the bench is advisable'", "'A bench could ...' / 'possible source' / 'would allow ... unlikely to suit' wording; the plan bullet deleted; R8 default-variant question ends 'left open'; inventory pinning note 'A bench could pin a revision'. Sweep of R7, R8 and the inventory for 'the bench will', 'we use', 'bench rule', 'this is the plan': 0 hits (section 8e)", "R032, T41, T43, T59"),
    ("Possible sources of evaluation data", "none in R7", "RabakBench public set (card intended use) and the seven public datasets mapped by the label notebook, as 'possible source' bullets with their own terms to be checked; no permitted-use claim", "T19, T8, R032"),
    ("Third-party embedder facts (main P4 Q2, R019)", "OpenAI, Google and EmbeddingGemma facts incl. a lifecycle sentence ('remains available', newer model gemini-embedding-2)", "kept: model identity, input limit, output dimension, gating, licence and terms, each attributed 'not GovTech docs'; lifecycle sentence dropped from inventory (c) and R8; the pricing-page remark in R7 does not name the newer model; the scope paragraph states this limit", "T14, T34, T12"),
    ("Terms pages read in P5", "R7 said the Gemma Appendix, the Gemini terms and the OpenAI terms were not read, while the inventory quoted them (cross-draft mismatch)", "Gemma Appendix lists EmbeddingGemma [Documented]; Gemma section 3.2, Prohibited Use Policy and Model Derivative text quoted; OpenAI data-controls page and Gemini Additional Terms quoted; the OpenAI policy pages are one HTTP 403 fact (usage policies and service terms stay [To be verified] in the inventory only and are an R8 open question); 9 URLs added to R9", "T9, T10, T11, T12, T13, T59 (R019, R021)"),
    ("Licence conflict (Q04)", "one bullet 'not obviously reconcilable and neither is a legal opinion' with 'see R7'; md5 comparison under a repo label; 'The cards' metadata' under one repo label", "LICENSE text and exclusion, three per-repo card-metadata bullets, the paper's ethics, contributions and conclusion statements as separate labelled bullets; one Not disclosed bullet for the relation (what was checked named) and one for the missing 'usage guidelines'; md5 as plain-text hint; no conclusion on permitted use", "T6, T7, T58, T57 (R031 Q04)"),
    ("arXiv 2507.05980 as an official source", "cited in R5 and R9, no inventory row", "inventory block (d) 11th row (GovTech-authored; authors and dates from the arXiv page); short name RB added; R5 source hint says html v2 of 2 Feb 2026", "T15 (main P4 Q1, main P5 Q-A)"),
    ("Demo Space", "data-flow fact only in inventory (d); live status [To be verified]", "data-flow facts (Google Sheet append, OpenAI chat and moderation) added to R5 with file and line; R7 proposal bullet to avoid the hosted demo for test text; inventory row says reference only and live status RUNNING [Documented] (Hub API)", "T5, T54 (main P4 T5)"),
    ("Playbook pin", "'staging branch' remark", "staging is the branch the site is built from (workflow), page file identical on main (md5): no unreleased label", "T16"),
    ("Sentinel cross-reference facts", "no read date", "'read 2026-10-09' on the Sentinel source hints (R3, R4, R6; inventory (e) rows 1, 2 and 4)", "T17"),
    ("Process wording in deliverable text", "'covered under the Sentinel column', 'see R7' (2), 'routed as a licensing item', '(R019)' (3), 'was not read/worked around', 'This is a licensing item for the user ...', 'Nothing was signed in to, requested or called ...'", "removed or reworded as sources checked; nothing in the finals names a ruling, checkpoint, triage id or session", "T59"),
    ("Code identifiers and package names in Summaries", "'The predict call' (R3), 'pass the vectors to predict' (R6), 'transformers', 'torch', 'sentence-transformers' (R7)", "'The classifier call', 'to the classifier', 'Hugging Face Transformers and PyTorch'", "style 2"),
    ("R9 list", "24 URLs", "31 URLs: 10 added so every page, file and pin cited in R1 to R8 is in R9 (one URL per bullet) and the 3 huggingface.co/api URLs removed in the P7 fix loop (the model-page tree URLs at the pinned revisions were already listed)", "T13 and the T-ids in section 2; P7 main ruling"),
    ("Inventory block (d) row count", "10 rows", "11 rows (arXiv 2507.05980); BLOCKS counts for the P8 config are 4/11/8/11/4", "T15, main P5 Q-A"),
]

CONFLICTS = [
    "**Licence texts (Q04, T6).** Sources: repo LICENSE (MIT subject to Singapore law and SIAC arbitration; exclusion for assets GovTech identifies as not licensed) and card metadata (license other, govtech-singapore) versus the paper's ethics statement ('exclusively for research and public interest purposes only') and the release statements in the paper, blog and playbook. All are GovTech sources. Decision: each text is its own labelled bullet ([Documented: repo ...] per repo, [Documented] for the paper), the relation is a single [Not disclosed] bullet naming what was checked; no conclusion on permitted use (R031, main P5 Q-C).",
    "**Table 1 versus Table 3 column order (T22).** Sources: arXiv 2507.15339 Table 1 header SS, ZH, MS, TA; Table 3 header SS, MS, ZH, TA, same LionGuard 2 values; the RabakBench paper Table 4 (GovTech-authored) and the 29 Jul 2025 blog support Table 1. Decision: both table facts stay [Documented]; the swap is one [Inferred] bullet with its premise in the column, and the inventory takes the same label (it had [To be verified]); the open question stays in R8.",
    "**Gemma section 3.2 bullet versus the earlier Gemma bullet (T10).** Sources: the draft bullet on the Gemma Terms of Use and the resolver's section 3.2 bullet quote the same sentence of the same page. Decision: one bullet (the resolver's quote), keeping the page's last-modified date in the source hint, so the fact is not stated twice.",
    "**Gemini pricing-page remark (T12 versus main P4 Q2).** Sources: the resolver's Not disclosed bullet says the pricing page lists only gemini-embedding-2; main ruled that the Google lifecycle sentence naming gemini-embedding-2 is dropped. Decision: the Not disclosed bullet keeps its absence ('the pricing page has no entry for gemini-embedding-001') without naming the newer model.",
    "**OpenAI usage-policy URL (T11).** Sources: the resolver says add the usage-policies URL 'only if the 403 fact is kept'. Decision: the HTTP-fact bullet in R7 and the inventory row both name /usage-policies, so the URL is added to R9 and to the inventory (c) OpenAI Source cell (HTTP 403 expected at the URL check, as for terms-of-use).",
    "**LICENSE has no research-only wording (hygiene).** Sources: the inventory labelled this absence [Documented: repo ...]; README section 3 rule 2 makes absences [Not disclosed]. Decision: relabelled [Not disclosed] with 'LICENSE read in full'; the column carries the same absence inside the relation bullet.",
    "**'No API was called' (hygiene).** Sources: the inventory scope said no API was called while citing the Hugging Face Hub API (public metadata JSON, read with plain GET requests). Decision: reworded to 'no model or embedding service was called; the public Hugging Face Hub metadata was read with plain GET requests'.",
    "**Embedder identity facts versus behaviour (T14).** Sources: brief scope (identity only) and main P4 Q2. Decision: input limits and output dimensions are identity-level facts and stay with 'not GovTech docs'; the Gemini lifecycle sentence and the R8 clause about gemini-embedding-2 are dropped.",
]

HANDLED = (
    "- Resolution items handled: 39 (T6 to T13, T14 to T22, T24 to T29, T31, T34, T43, T45 to T52, T55 to T59). "
    "Items with no text change by design: T18 (quotes re-read live, no differences), T46 (kept as written), T55 (Covered-by convention kept), T56 (FYI, section 6c); T47 is handled with T57."
)

URL_NOTE = (
    "Expected non-200 at the P9 URL check: openai.com/policies/terms-of-use and openai.com/policies/usage-policies (HTTP 403, an HTTP fact kept on purpose in R7 and inventory (c)). "
    "R9 and the inventory Source URL cells cite no huggingface.co/api path (P7 main ruling). huggingface.co/google/embeddinggemma-300m is a public page with gated files; "
    "huggingface.co/datasets/govtech/RabakBench-full (inventory (d) only) is gated manual and access was not requested. "
    "The Sentinel Onboarding Guide (HTTP 403 to a plain GET) is not cited anywhere."
)

OPEN = [
    ("T23", "Chinese and Malay column order in Tables 1 and 3", "b (honest gap)", "R5 Inferred bullet; R8", "paper, blog, RabakBench paper; only the authors or a rerun on the public RabakBench set settle it"),
    ("T30", "Latency, memory and GPU need for 2.1 and Lite", "b (honest gap)", "R6 Not disclosed; R8", "cards, playbook, paper (its hardware paragraph covers only decoder fine-tuning), three blogs"),
    ("T32", "Best threshold per variant and key; binary key versus maximum of the category keys", "b", "R5 Not disclosed; R8", "needs a labelled set; no install or API call during research (R019)"),
    ("T33", "Evaluation of Lite; 2.1 beyond one blog table", "b (honest gap)", "R5 Not disclosed; R8", "cards, playbook, paper, blogs, demo"),
    ("T35", "Behaviour on text over each embedder's limit", "b", "R8", "needs testing"),
    ("T36", "Jailbreak and prompt-injection coverage", "b", "R2 Not disclosed; R8", "documentation half closed: paper Appendix E.2 gives results by language, overall and category only; test half open"),
    ("T37", "Calibration beyond the 2.1 versus Jev comparison", "b (honest gap)", "R5 (one blog sentence)", "blog; none for 2 or Lite"),
    ("T38", "Whether a retrained LionGuard 2 will be published on Hugging Face", "b (honest gap)", "R4 Not disclosed; R8", "blog of 21 Aug 2026, playbook, repos (heads equal the pins on 2026-10-09)"),
    ("T39", "Whether Sentinel-hosted variants run the Hugging Face weights", "b (honest gap)", "R8", "Sentinel docs, playbook; hosted-API question stays under Sentinel"),
    ("T40", "Embedder drift and whether GovTech will retrain", "b (honest gap)", "R8 (lifecycle clause dropped)", "paper warning only"),
    ("T41", "First-pass default variant", "b (CP1 item, suggestion wording)", "R8 'left open'", "R032: not decided"),
    ("T42", "Whether the pinned requirements install together and run EmbeddingGemma", "b", "R6 Not disclosed (Python version)", "no install during research (R019)"),
    ("T44", "Training code and the two-minute retrain claim", "b (honest gap)", "R4 Not disclosed", "git ls-remote on four GitHub paths answered 'Repository not found'; Hub listing shows no training repo"),
    ("T53", "RabakBench-full: card absent, contents and terms", "b (honest gap)", "inventory (d) To be verified", "gated manual; access not requested"),
    ("T54", "Demo Space: sheet configuration", "b (partly closed)", "inventory (d)", "Hub API shows RUNNING; whether the live Space has the sheet configured is not visible from the repo"),
    ("T1 to T4", "CP1 decisions (column split, prefix, self-hosting framing, embedder terms and test text)", "b (closed by R031)", "applied; which test text may be sent stays open for before testing (R8)", "R031"),
    ("T5", "Demo Space as a test target", "b (main ruling)", "reference only; data flow in R5 and R7", "main P4 T5"),
]

RES = [
    ("T6", "How the LICENSE, card metadata and the paper's research-only statement relate", "c", "Not disclosed (R4 and inventory (a), (c)); R8 question", "LICENSE of four model repos and two datasets, three cards, paper (ethics, contributions, conclusion, html v1 and v2), three blogs, playbook, Hugging Face collection and organisation pages, Sentinel page"),
    ("T7", "Where the paper's 'clear usage guidelines that prohibit deployment for harmful applications' are published", "a", "Not disclosed (R4)", "LICENSE, three cards, playbook page, three blogs, collection page"),
    ("T8", "Terms of RabakBench-full and of the demo Space", "c", "Not disclosed (inventory (d))", "file lists, Hub metadata, HTTP 404 for LICENSE; gated terms need a login and were not requested"),
    ("T10", "Whether the Lite classifier is a Gemma Model Derivative; whether embedding harmful test text is a restricted use", "c", "Not disclosed (inventory (c)); terms quoted in R7", "Lite README, LICENSE, playbook; the application of the terms is a user judgement"),
    ("T11", "Whether OpenAI's usage policies or service terms restrict harmful or explicit embedding input", "c", "To be verified (inventory (c)); R8 question", "pages returned HTTP 403; not worked around (R021)"),
    ("T12", "Whether the Gemini terms treat an embedding call differently; free tier of gemini-embedding-001", "c", "Not disclosed (R7, inventory (c)); R8 question", "Gemini Additional Terms and pricing page"),
    ("T29", "Whether the paper's 'embedding call' is the hosted OpenAI request, and the CPU model", "a", "Not disclosed (R6, inventory (a)); R8 question", "paper sections 3 and 7.1 and the hardware paragraph"),
    ("T31", "Operating threshold", "a", "Not disclosed (R5, inventory (a))", "cards, dataset cards, label-mapping notebook, playbook, paper, blogs, demo README"),
]

FYI = [
    "T56: the frozen Sentinel final cites paper section 7.2 for the binary head; the paper html places the head description in section 4.2.2 and the mismatch discussion in section 7.2. Its 'Tamil 66.6 versus 66.5 in Table 8' claim is correct (verified by T24). No edit to frozen sheets (R001).",
    "T55: Covered-by convention. Block (d) rows keep the inventory-only marker although they source LN1 facts (they are references, not components of the function); block (c) third-party rows carry the LN1 header; block (e) lists no Sentinel header. Applied as the resolver recommended; main may log it as a precedent.",
    "T18: blog, Sentinel and playbook quotes were re-read live in P5 and match; the draft Reviewer notes that said they came from saved raw copies are superseded (section 7).",
    "T24: the brief's 'Tamil 66.6 versus 66.5 in Table 8' is true; the draft Reviewer note 6 saying it was not re-verified is superseded.",
    "Q-B (arXiv 2507.11966 translation paper, cited by the RabakBench card): not read and not added (main: optional suggestion dropped).",
    "Licence texts (T6): for the user's judgement at CP2 if the relation matters to the bench; the finals draw no conclusion (main P5 Q-C).",
]

NOTES_STATUS = (
    "Status of the moved notes after P5: column notes 6 and 9 and inventory notes 5 and 8 are superseded by T24, T18 and T19 (notebook now read; blog, Sentinel and playbook quotes re-read live). "
    "The parts of column note 8 and inventory note 5 on the unread Gemma Appendix and Gemini terms are superseded by T9, T12 and T13; the OpenAI HTTP 403 part stands."
)

KNOWN = [
    ("you run it yourself", "R1 Summary old wording"), ("open Hugging Face weights", "R1 Summary old wording"),
    ("publishes only the small classifier", "R4 Summary old wording"), ("Which header order is right", "old To be verified"),
    ("is advisable", "inventory advice wording"), ("remains available", "Google lifecycle sentence"),
    ("gemini-embedding-2", "Google lifecycle sentence (main P4 Q2)"), ("routed as", "process wording"),
    ("R019", "ruling id"), ("not obviously reconcilable", "inference inside a Not disclosed bullet"),
    ("the bench will", "decided-plan wording (R032)"), ("bench rule", "decided-plan wording (R032)"),
    ("we use", "decided-plan wording (R032)"), ("this is the plan", "decided-plan wording (R032)"),
    ("data-handling decision", "decided-plan wording (R032)"), ("a bench-design choice", "decided-plan wording (R032)"),
    ("Pick your own threshold", "old R7 Summary wording"), ("Reviewer notes", "reviewer notes"),
    ("not worked around", "process wording"), ("fetch tool", "reworded to a plain GET in the P7 fix loop (0 expected)"), ("huggingface.co/api", "main ruling: no API paths in R9 or Source URL cells (0 expected)"), ("open models", "scope paragraph wording removed in P7 fix 5"), ("choose a threshold yourself", "R7 instruction removed in P7 fix 2"), ("lionguard2.py@be4e38c9:152", "wrong line number (P7 fix 3)"),
]


VFIX_INTRO = (
    "Source: lionguard_review.md (gr-verifier, 2026-10-10), verdict PASS WITH FIXES, 5 required fixes, plus main's ruling (same as purplellama P5 Q4) that R9 and inventory Source URL cells must not cite huggingface.co/api paths, "
    "plus the optional suggestions, all accepted by main. Applied by gr-merger in the P7 fix loop; the finals were regenerated from the same scripts (ops_fix.py runs after ops_cols.py and ops_inv.py), "
    "so the edits also appear in sections 2 and 3 with the reason 'P7 ...'. Required: fix 1 (R1 Detail backs the R1 Summary), fix 2 (R7 minimum-setup wording), fix 3 (five wrong line numbers: R3 three bullets, R4 one, R5 one; the two optional R4 line-range touch-ups are included), "
    "fix 4 (inventory (e) 'Hosted API behaviour' split into per-repo Documented facts and one Inferred conclusion), fix 5 (scope paragraph: 'models', not 'open models'). No Summary changed except the one-word R9 edit; no headline number changed; BLOCKS stay 4/11/8/11/4."
)

VFIX_NOTES = (
    "Not done and why: the reviewer's optional note on the Table 1 Qwen3 row is recorded as an unlabelled R8 question only (the draft does not assert a typo in the paper); "
    "the scope paragraph sentence 'nothing was installed, run or downloaded ...' is kept as the read-date and method statement of the Presidio precedent (the two sentences the reviewer named, in the (c) intro and the demo row, were removed). "
    "R1 now has 12 top-level Detail bullets (was 9) and R4 52 (was 50), R8 14 (was 13), R9 31 (was 33); see section 8b."
)


POST_INTRO = (
    "Source: the P10 diagram verifier's question Q1 (benchtest/scratchpad/verifier/20261010_lionguard_diagram-review.md), routed by main. The 28 Sep 2026 blog says it used 'the same benchmarks used in our earlier LionGuard experiments' and calls the set 'the original LionGuard 2 Test set', which contradicts the [Inferred] claim that the 2.1 figure 0.7318 cannot be compared directly with the paper's 77.0. "
    "Neutral wording applied to the column and the inventory; the workbook was not touched. Both checks re-run on the regenerated finals (section 8f); BLOCKS stay 4/11/8/11/4."
)
