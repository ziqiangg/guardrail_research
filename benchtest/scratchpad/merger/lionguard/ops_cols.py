"""Column edits for lionguard (LN1). Imported by merge_lionguard.py."""

C = "LN1"
R2L = "**[Documented: repo govtech/lionguard-2@be4e38c9]**"
R21 = "**[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**"
RLT = "**[Documented: repo govtech/lionguard-2-lite@d56c17a0]**"
RDEMO = "**[Documented: repo govtech/lionguard-demo@4ade46d1]**"
RRB = "**[Documented: repo govtech/RabakBench@3c02a5b8]**"
DOC = "**[Documented]**"
INF = "**[Inferred]**"
ND = "**[Not disclosed]**"
MD5 = "01aeb061dcdbf0bd0612ad2b76ac5b6c"


def apply(K):
    # ------------------------------------------------------------------ R1
    K.summary(C, 1,
        "Summary: **Localised harmful-content classification of one text string.** LionGuard is GovTech's classifier for Singapore's languages and context. "
        "It returns a probability for each harm category and severity level. GovTech publishes the classifier on Hugging Face; two variants embed text through OpenAI or Gemini, one locally. " + DOC,
        "T49 (R031): drops 'you run it yourself from open Hugging Face weights' (embedding step is hosted for 2 and 2.1; 'open' depends on the unresolved licence reading T6)")

    # ------------------------------------------------------------------ R2
    K.summary(C, 2,
        "Summary: **Six harm categories plus an overall flag, with severity levels.** Hateful, insults, sexual, physical violence, self-harm and all other misconduct; four have Level 1 and Level 2. "
        "Covers English, Singlish, Chinese, Malay and Tamil; the playbook and paper call Tamil partial or moderate. " + DOC,
        "T27: the Summary no longer picks the playbook's 'partial Tamil' alone; names the playbook and paper wording (43 words)")
    K.repl(C, 2, "The LionGuard 2 card taxonomy gives Hate Level 1", [
        '• The LionGuard 2 card taxonomy gives Hate Level 1 "Discriminatory" and Level 2 "Hate Speech"; Insults and Physical Violence have no sub-levels; Sexual Level 1 "Not appropriate for minors" and Level 2 "Not appropriate for all ages" ' + R2L,
        '• The same card taxonomy gives Self-Harm Level 1 "Ideation" and Level 2 "Action / Suicide", and All Other Misconduct Level 1 "Generally not socially accepted" and Level 2 "Illegal activities" ' + R2L],
        "style 4: bullet of 441 characters split in two; text and label unchanged", kind="style")
    K.ins_after(C, 2, "On the paper's native-speaker test set LionGuard 2 scores F1 41.1",
        "• This is a different test set from RabakBench, so the Tamil F1 of 41.1 here and 66.6 in Table 1 are not comparable (premise: Table 13 is the native-speaker set and Table 1 is RabakBench) " + INF,
        "T28: names the test set so the two Tamil figures are not read side by side")

    # ------------------------------------------------------------------ R3
    K.summary_text(C, 3, "The predict call takes only", "The classifier call takes only",
        "style 2: code identifier 'predict' removed from the Summary")
    K.sub(C, 3, "Cross-reference: the hosted Sentinel service lists its LionGuard guardrails as type Input/Output",
        "(Sentinel docs, hosted API; covered under the Sentinel column)", "(Sentinel docs, hosted API, read 2026-10-09)",
        "T59, T17: process wording 'covered under the Sentinel column' removed; read date added")

    # ------------------------------------------------------------------ R4
    K.summary(C, 4,
        "Summary: **Frozen embedder plus a small ordinal classifier.** The three variants differ in the embedder: OpenAI embeddings (LionGuard 2), Gemini embeddings (2.1) or local EmbeddingGemma (2 Lite). "
        "GovTech publishes the small classifier and its code on Hugging Face, not the embedder. " + DOC,
        "T50: 'publishes only the small classifier' replaced; GovTech also publishes the model code and a training-data subset (the 'no training code' fact stays a Not disclosed bullet)")
    K.repl(C, 4, 'A GovTech blog (21 Aug 2026) says "LionGuard 2 uses a shared representation', [
        '• A GovTech blog (21 Aug 2026) says "LionGuard 2 uses a shared representation feeding into 11 classification heads" (GovTech AI blog) ' + DOC,
        "• The code has seven head modules and eleven output keys, so the blog's 11 probably counts output keys (premise: `lionguard2.py@be4e38c9:172-177` gives eleven keys from seven heads) " + INF],
        "T57, T47: the inference 'counting output keys' moves out of the Documented bullet into an Inferred bullet with its premise", kind="replace")
    K.repl(C, 4, "LionGuard 2 classifier size: 848,942 float32 parameters", [
        "• LionGuard 2 classifier size: 848,942 float32 parameters and a `model.safetensors` of 3,398,496 bytes (Hugging Face API, read 2026-10-09) " + R2L,
        '• The paper says "The resulting classifier contains 0.85M parameters and occupies only 3.2 MB on disk" (arXiv 2507.15339 section 4.2.2) ' + DOC],
        "T58: the paper figure gets its own bullet and label (one label per source)", kind="replace")
    K.repl(C, 4, "Conflict: the `lionguard2.py` docstring says the input is encoded with OpenAI", [
        "• Conflict: the docstring of `lionguard2.py` in LionGuard 2 says the input is encoded with OpenAI's `text-embedding-3-small`, while the card, `inference.py` and `config.json` use `text-embedding-3-large` at 3072 dimensions (`lionguard2.py@be4e38c9:97`) " + R2L,
        "• The docstring of the LionGuard 2.1 model file names its own embedder, `gemini-embedding-001`, so the stale name occurs only in the LionGuard 2 file (`lionguard2.py@1c3a9ea7:97`) " + R21,
        "• The docstring of the LionGuard 2 Lite model file names its own embedder, `embeddinggemma-300m` (`lionguard2lite.py@d56c17a0:97`) " + RLT],
        "T45, T59: the stale docstring does not recur in 2.1 or Lite (code read at the pins); one label per repo", kind="replace")
    K.repl(C, 4, "A separate paper, card section or training description for LionGuard 2.1 or 2 Lite", [
        '• A separate paper, card section or training description for LionGuard 2.1 or 2 Lite (checked both cards, the playbook, html v1 and v2 of the LionGuard 2 paper, which name no Gemini or Gemma embedder, and the three blog posts; the blog of 28 Sep 2026 says only that embedding generation "can be run locally or through an API depending on the variant") ' + ND],
        "T48: checked list extended (paper html v1 and v2, blog of 28 Sep 2026)")

    # licence block (T6, T7, T58, T59)
    K.repl(C, 4, "The LionGuard 2.1 repository holds a LICENSE with identical content", [
        "• The LionGuard 2.1 repository holds a LICENSE file (md5 %s, the same as the LionGuard 2 file; checked 2026-10-09) " % MD5 + R21],
        "T6, T58: the md5 comparison becomes a plain-text hint; wording 'identical content' dropped")
    K.repl(C, 4, "The LionGuard 2 Lite repository holds a LICENSE with identical content", [
        "• The LionGuard 2 Lite repository holds a LICENSE file (md5 %s, the same as the LionGuard 2 file; checked 2026-10-09) " % MD5 + RLT,
        '• The LICENSE excludes "any asset or code identified by the Government Technology Agency ("GovTech") as not licensed to you" and GovTech and Singapore public-sector marks and images ' + R2L],
        "T6, T58: md5 comparison as plain-text hint; new bullet for the LICENSE exclusion (was only in the inventory)")
    K.repl(C, 4, "The cards' metadata reads `license: other`", [
        "• The LionGuard 2 card metadata reads `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` " + R2L,
        "• The LionGuard 2.1 card metadata reads `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` " + R21,
        "• The LionGuard 2 Lite card metadata reads `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` " + RLT],
        "T7 (iii), T58: plural 'cards' under one repo label becomes one bullet per repo", kind="replace")
    K.ins_after(C, 4, "Licence, paper:", [
        '• The paper\'s contributions say "We release the classifier weights and a portion of our training data to support future research in LLM safety" (arXiv 2507.15339 section 1) ' + DOC,
        '• The paper\'s conclusion says "By releasing our model weights and training data subset, we aim to support broader adoption of localisation-aware moderation strategies" (arXiv 2507.15339 section 8) ' + DOC],
        "T6: two further paper statements about the release")
    K.repl(C, 4, "The paper statement and the repository LICENSE are not obviously reconcilable", [
        '• The "clear usage guidelines that prohibit deployment for harmful applications" named in the paper\'s ethics section (checked the LICENSE, the three cards, the playbook page and the three blog posts; no such guidelines found) ' + ND,
        "• How the repository LICENSE, the card metadata and the paper's research-only statement relate (checked the LICENSE, the three cards, the playbook page, the three blog posts, the paper's ethics, contributions and conclusion, the Hugging Face collection and organisation pages; not stated) " + ND],
        "T6, T7 (i), T57, T59: the Not disclosed bullet is limited to the absence (the inference 'not obviously reconcilable ... neither is a legal opinion' and 'see R7' dropped); guideline text not located",
        kind="replace")
    K.repl(C, 4, "The three model repositories were last modified 2025-11-18", [
        "• The three model repositories were last modified 2025-11-18, and their head revisions on 2026-10-09 are the pinned ones (Hugging Face API, read 2026-10-09) " + DOC,
        "• No retrained model has therefore been published in those repositories (premise: no commit since 2025-11-18 and the blog says retrained models are for Sentinel users) " + INF],
        "T57: the conclusion 'so no retrained model is published there' becomes an Inferred bullet with its premise", kind="replace")
    K.sub(C, 4, "Cross-reference: Sentinel also serves the same three variants",
        '(Sentinel docs, "LionGuard Versions", hosted API)', '(Sentinel docs, "LionGuard Versions", hosted API, read 2026-10-09)',
        "T17: read date added")
    K.sub(C, 4, "Source conflict: the Sentinel docs write the OpenAI embedder",
        "(Sentinel docs, hosted API)", "(Sentinel docs, hosted API, read 2026-10-09)", "T17: read date added")

    # ------------------------------------------------------------------ R5
    K.sub(C, 5, "A recommended operating threshold or calibration guidance",
        "(checked the three cards, the playbook, the paper, the three blog posts and the demo Space README; only",
        "(checked the three cards, the two dataset cards, the label-mapping notebook, the playbook, the paper, the three blog posts and the demo Space README; only",
        "T31, T19: checked list extended (notebook read, code not run; dataset cards)")
    K.ins_after(C, 5, "The demo's chatbot route flags a message when the binary probability is above 0.5", [
        "• The demo's analysis route appends each submitted text, its binary score and per-category maxima to a Google Sheet, and its chat route logs the message and scores to a Google Sheet, in both cases only when a sheet URL and service-account credentials are configured (`services.py@4ade46d1:158-165`, `:338-341`) " + RDEMO,
        "• The demo's chat route also sends each message to OpenAI for a chat reply and for OpenAI moderation (`services.py@4ade46d1:199-223`) " + RDEMO],
        "T5 (main P4 ruling: demo Space is reference only): data-flow facts added from the code read at the pin")
    K.repl(C, 5, "The GovTech RabakBench paper Table 4 gives LlamaGuard 4 12B", [
        "• The GovTech RabakBench paper Table 4 gives LlamaGuard 4 12B Singlish 60.53, Chinese 54.20, Malay 65.92, Tamil 73.77, and AWS Bedrock Guardrail Chinese 0.59 and Malay 18.49, while Table 3 of the LionGuard 2 paper gives LlamaGuard 4 12B 60.6, 54.6, 65.2, 73.0 and AWS Bedrock 69.6, –, 21.1, – under SS, MS, ZH, TA (arXiv 2507.05980 Table 4, html v2 of 2 Feb 2026; arXiv 2507.15339 Table 3) " + DOC],
        "T22, T15, CORRECTION: the values are close to, not equal to, the RabakBench figures; AWS Bedrock row added as further evidence")
    K.sub(C, 5, "Table 3's Malay and Chinese labels are therefore probably swapped",
        "(premise: the RabakBench values match Table 3 only if the second column is Chinese)",
        "(premise: the RabakBench values match Table 3 only if the second column is Chinese, including the unsupported-language dash for AWS Bedrock)",
        "T22: premise names the Bedrock evidence")
    K.repl(C, 5, "RabakBench Singlish is 88.1 in Tables 1 and 3 and 87.1 in Table 5", [
        "• RabakBench Singlish is 88.1 in Tables 1 and 3 and 87.1 in Table 5, and RabakBench Tamil is 66.6 in Tables 1 and 3 and 66.5 in Table 8; no source explains the differences (arXiv 2507.15339 Tables 1, 3, 5 and 8) " + DOC],
        "T24: the Tamil 66.6 versus 66.5 difference (Table 8) re-read and added")
    K.repl(C, 5, "The 16 and 17 counts are compatible", [
        "• The counts fit together if the 13 localised datasets include the internal test set (premise: Table 3 has 13 columns including Test, and Table 4 adds 4 English sets, giving 17 in all, or 1 internal and 16 public) " + INF],
        "T26: reconciliation now carries a count")
    K.repl(C, 5, "The paper says about 4% of examples show the binary head", [
        '• The paper says "About 4% of examples … show disagreement between the binary head and category heads" (section 7.2); Table 11 gives an overall average of 4.19% over-predicted and 0.70% under-predicted over 43,075 samples, with RabakBench Singlish highest at 9.99% over-predict (arXiv 2507.15339 section 7.2, Appendix E.1, Table 11) ' + DOC,
        '• The paper says deriving the binary decision as the maximum of the category scores "removes the mismatch", and keeps the dedicated binary head because it boosts performance (arXiv 2507.15339 section 7.2) ' + DOC],
        "T25, CORRECTION: 'about 4%' is the over-prediction rate (4.19%), with 0.70% under-prediction; the max-of-categories remark added", kind="replace")
    K.sub(C, 5, "The original test split is private, so the 0.7318 figure",
        "(premise: the blog calls the split private; the paper's test set is not published)",
        '(premise: the blog calls its split "a held-out private LionGuard test split", and the paper does not say its internal test set is released)',
        "T21, CORRECTION: the paper does not state that its test set is unpublished; premise now quotes the blog")

    # ------------------------------------------------------------------ R6
    K.summary_text(C, 6, "then pass the vectors to predict.", "then pass the vectors to the classifier.",
        "style 2: code identifier 'predict' removed from the Summary")
    K.repl(C, 6, "LionGuard 2 Lite needs no API key (card:", [
        '• LionGuard 2 Lite needs no API key (card: "runs fully locally, with no external API calls") but downloads Google\'s gated embedder ' + RLT],
        "T51, T59: cross-reference '(see R7)' removed")
    K.ins_after(C, 6, "The classifier takes a fixed-size vector, so any length limit comes from the embedder", [
        "• LionGuard 2 embedder limit: OpenAI lists a max input of 8192 for text-embedding-3-large (OpenAI docs, not GovTech docs) " + DOC,
        "• LionGuard 2.1 embedder limit: Google lists an input token limit of 2,048 for gemini-embedding-001 (Google model page, not GovTech docs) " + DOC,
        "• LionGuard 2 Lite embedder limit: the Hugging Face page of EmbeddingGemma lists a maximum input context length of 2048 tokens (Google page, not GovTech docs) " + DOC],
        "T34, T14 (main P4 Q2): owners' input limits added, attributed 'not GovTech docs'")
    K.ins_after(C, 6, "Speed for LionGuard 2:",
        '• Whether the paper\'s "embedding call" is the hosted OpenAI request, and the CPU model used (checked the paper sections 3 and 7.1 and its hardware paragraph; not stated) ' + ND,
        "T29: hosted-versus-local question recorded as an absence")
    K.sub(C, 6, "Cross-reference: the hosted Sentinel service lists token limits",
        "(Sentinel docs, hosted API)", "(Sentinel docs, hosted API, read 2026-10-09)", "T17: read date added")

    # ------------------------------------------------------------------ R7
    K.summary(C, 7,
        "Summary: **Minimum setup:** Python with Hugging Face Transformers and PyTorch, loading each model with remote code enabled. "
        "LionGuard 2 Lite also needs a Hugging Face login and acceptance of Google's Gemma terms for its embedder, but no API key. "
        "LionGuard 2 needs an OpenAI key and 2.1 a Gemini key, so test text goes to those providers. No threshold ships. " + INF,
        "T51, style 2: Hugging Face login added for Lite; package names removed from the Summary; 'Pick your own threshold' reworded (59 words)")
    K.ins_after(C, 7, "**Minimum setup:** install",
        "• A bench could pin each model repository to a revision, because the README loads the repository code with `trust_remote_code=True` and no revision argument, so the repository's Python runs on load (premise: the README usage and the repos can change) " + INF,
        "T43 (R032 wording): pinning suggestion aligned with the inventory")
    K.repl(C, 7, "LionGuard 2 Lite path: install", [
        "• LionGuard 2 Lite path: install `sentence-transformers`, log in to Hugging Face and accept Google's conditions for `google/embeddinggemma-300m`, then the classifier and embedder run locally with no embedding API key (premise: the card says \"runs fully locally\" and the embedder page is gated) " + INF],
        "T51: Hugging Face login added")
    K.ins_after(C, 7, "The same page shows `License: gemma`",
        '• Accepting the conditions needs a Hugging Face login: "Log in or Sign Up to review the conditions and access this model content." (Hugging Face page of google/embeddinggemma-300m, not GovTech docs) ' + DOC,
        "T51: login fact from the embedder page")
    K.repl(C, 7, "Google's Gemma Terms of Use page reads", [
        '• Gemma Terms of Use section 3.2 says "You must not use any of the Gemma Services: for the restricted uses set forth in the Gemma Prohibited Use Policy" or "in violation of applicable laws and regulations" (Google page, last modified April 1, 2026, not GovTech docs) ' + DOC],
        "T10: section 3.2 quote replaces the shorter bullet on the same sentence (last-modified date kept in the hint)")
    K.repl(C, 7, "Whether the Gemma terms page covers EmbeddingGemma", [
        "• The Gemma Terms of Use Appendix lists EmbeddingGemma among the covered models (Google page, not GovTech docs; read 2026-10-09) " + DOC,
        '• The Gemma Prohibited Use Policy (last modified February 21, 2024) lists "Generating content that promotes or encourages hatred" and "Generate sexually explicit content", with a note that this "does not include content created for scientific, educational, documentary, or artistic purposes" (Google page, not GovTech docs) ' + DOC,
        '• The Gemma terms define Model Derivatives to include a model "created by transfer of patterns of the weights, parameters, operations, or Output of Gemma" and say "Outputs are not deemed Model Derivatives" (Google page, not GovTech docs) ' + DOC],
        "T9 (To be verified bullet resolved: the Appendix lists EmbeddingGemma), T10, T13")
    K.sub(C, 7, "LionGuard 2 path: an OpenAI API key is needed",
        "and every test text is sent to OpenAI; that is a data-handling decision for the bench (premise",
        "and each text to be classified is sent to OpenAI to be embedded (premise",
        "R032 rewording: 'data-handling decision for the bench' removed")
    K.sub(C, 7, "LionGuard 2.1 path: a Gemini API key is needed",
        "and every test text is sent to Google; same data-handling decision (premise",
        "and each text to be classified is sent to Google to be embedded (premise",
        "R032 rewording: 'same data-handling decision' removed")
    K.repl(C, 7, "OpenAI's terms page `https://openai.com/policies/terms-of-use` returned HTTP 403", [
        '• OpenAI\'s data-controls page says data sent to the OpenAI API "is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)" (OpenAI docs, not GovTech docs) ' + DOC,
        "• The same page lists `/v1/embeddings` with no training use, abuse-monitoring retention of 30 days, no application-state retention, and Zero Data Retention eligibility \"Yes\" (OpenAI docs, not GovTech docs; read 2026-10-09) " + DOC,
        "• https://openai.com/policies/terms-of-use, /service-terms and /usage-policies returned HTTP 403 to the fetch tool (observed 2026-10-09) " + DOC,
        "• platform.openai.com/docs/guides/your-data ends at developers.openai.com/api/docs/guides/your-data (final URL, HTTP 200, observed 2026-10-09) " + DOC],
        "T11, T13, T59: OpenAI data-controls page read; the HTTP facts are one fact per bullet; 'was not worked around' removed")
    K.repl(C, 7, "Whether OpenAI's and Google's service terms allow sending harmful", [
        '• Gemini API Additional Terms (effective March 23, 2026) say of unpaid quota: "Do not submit sensitive, confidential, or personal information to the Unpaid Services" (Google page, not GovTech docs) ' + DOC,
        '• The same terms say "Your access to Gemini API is a "Paid Service" only when accessing the API through a Cloud Project associated with an active billing account", and that for Paid Services Google "doesn\'t use your prompts … or responses to improve our products" (Google page, not GovTech docs) ' + DOC,
        '• Google\'s Generative AI Prohibited Use Policy (last modified December 17, 2024) says "Do not engage in sexually explicit, violent, hateful, or harmful activities" and allows exceptions "based on educational, documentary, scientific, or artistic considerations" (Google page, not GovTech docs) ' + DOC,
        "• Whether the Gemini terms treat an embedding call differently from other calls, and whether gemini-embedding-001 has a free tier (checked the terms and pricing pages; the terms do not mention embeddings and the pricing page has no entry for gemini-embedding-001) " + ND],
        "T12, T13 (To be verified bullet resolved or recast as Not disclosed; the OpenAI usage-policy half moves to R8); the pricing-page remark avoids naming gemini-embedding-2 (main P4 Q2: lifecycle facts dropped)")

    # test plan, R032 wording (proposals, not decided plans)
    tx = [
        ("Test texts: labelled safe and unsafe examples",
         "• A bench could use labelled safe and unsafe examples for each of the six categories and both levels, including Level 2 cases to check that Level 1 is also high " + INF),
        ("Include benign near-misses",
         "• A bench could add benign near-misses (for example matter-of-fact talk about sexuality, or news about violence) to measure false positives " + INF),
        ("Cover English, Singlish, Chinese, Malay and Tamil",
         "• A bench could cover English, Singlish, Chinese, Malay and Tamil, with translated pairs, and expect weaker Tamil results (premise: the paper's Tamil figures) " + INF),
        ("Add noisy variants",
         "• A bench could add noisy variants (casing, punctuation, misspellings) of a subset to repeat the paper's robustness check " + INF),
        ("Log the binary score and the category scores",
         "• A bench could log the binary score and the category scores to count disagreements, since the paper reports the binary head over-predicting in about 4% of examples " + INF),
        ("Sweep thresholds per key",
         "• A bench could sweep thresholds per key and score the same texts as prompts and as model responses, plus any retrieved text or tool output it uses " + INF),
        ("Run the same set through LionGuard 2, 2.1 and 2 Lite",
         "• A bench could run the same set through LionGuard 2, 2.1 and 2 Lite and time each embedding call separately from the classifier call " + INF),
    ]
    for anchor, new in tx:
        K.repl(C, 7, anchor, [new], "R032 rewording: bench content as a proposal ('a bench could'); T25 for the 4% wording in the logging bullet" if "4%" in new else "R032 rewording: bench content as a proposal ('a bench could')")
    K.repl(C, 7, "The dataset embeddings allow a head-only smoke test", [
        "• The dataset embeddings would allow a head-only smoke test with no external calls, but the set is Singlish and English only and about 2% unsafe, so it is unlikely to suit as an evaluation set (premise: dataset card statistics of 2,055 safe and 43 unsafe) " + INF,
        "• Possible source of evaluation data: the RabakBench public set (132 samples per language), whose card lists \"Benchmark moderation APIs / guardrails\" as an intended use " + RRB,
        "• The notebook `map_benchmark_labels.ipynb` maps seven public datasets (OpenAI moderation evaluation, BeaverTails, SimpleSafetyTests, RTP-LX, SORRY-Bench, SGHateCheck, SGToxicGuard) to the six-category taxonomy (code read, not run) " + R2L,
        "• Those seven datasets could serve as further possible sources of evaluation data, with their own terms to be checked (premise: GovTech's notebook maps their labels to this taxonomy) " + INF,
        "• A bench could avoid the hosted demo for test text, because its code may write submissions to a Google Sheet and sends chat messages to OpenAI (premise: `services.py@4ade46d1` behaviour above; whether the live Space has the sheet configured is not visible) " + INF],
        "R032 rewording (smoke-test bullet as 'would allow ... unlikely to suit'); T19, R032: possible sources of evaluation data added; T5 and main P4 ruling: demo Space is reference only",
        kind="replace")
    K.delete(C, 7, "Nothing is run during research", "T59: instruction-like process text and ruling id R019 removed from the deliverable")

    # ------------------------------------------------------------------ R8
    K.summary(C, 8,
        "Summary: **Key open questions.** Operating threshold per variant, any Lite or wider 2.1 evaluation, input length and latency, how the licence texts relate, embedder terms for test text, whether a retrained model is released, and jailbreak coverage.",
        "T13: 'the licence reading' and 'embedder terms' reworded as questions (36 words, no label)")
    K.repl(C, 8, "Whether the dedicated binary key or the maximum of the category keys", [
        "• Whether the dedicated binary key or the maximum of the category keys is the better verdict (the paper keeps the binary head because it boosts performance and says the maximum removes the mismatch; which works better per variant needs testing)"],
        "T25: question restated with the paper's own reasoning (the 'roughly 4%' wording dropped)")
    K.repl(C, 8, "Maximum input length for each variant, set by the embedder", [
        "• What happens on text longer than each embedder's limit, and whether Singlish, Chinese and Tamil token counts change the effective limit (the owners state the limits; GovTech states none; needs testing)"],
        "T34, T35: documentation half answered in R6; the open part is the test half")
    K.sub(C, 8, "Which of the paper's Table 1 and Table 3 column orders is right",
        "needs the authors or a rerun)", "needs the authors, or a rerun on the public RabakBench set)", "T23 (stays open), T22: a rerun on the public RabakBench set could settle it")
    K.sub(C, 8, "How the repository LICENSE (MIT subject to Singapore law and SIAC arbitration) relates",
        "(checked the LICENSE, card metadata, paper and blog; not stated; routed as a licensing item)",
        "(checked the LICENSE, card metadata, paper, blogs and playbook; not stated)",
        "T6, T59: 'routed as a licensing item' removed; checked list extended")
    K.repl(C, 8, "OpenAI and Gemini API terms for sending test text", [
        "• Whether OpenAI's usage policies and service terms (the pages returned HTTP 403) and Google's Gemini and Gemma terms allow sending harmful or explicit test text to the embedding services, and which account tier would apply (the owners' data-handling pages are quoted in R7; which test text may be sent is left to be decided before any testing; owners' pages only, not GovTech docs)"],
        "T13, T9, T11, T12, T4 (R031): the Gemma-appendix clause is gone (answered in R7); wording matches what was read")
    K.repl(C, 8, "Whether an embedder change would shift scores", [
        "• Whether an embedder change would shift scores: the paper warns an OpenAI embedding update may need retraining (whether GovTech will retrain is not stated)"],
        "T14 (main P4 Q2), T40: the Google lifecycle clause (gemini-embedding-2, 'remains available') dropped")
    K.repl(C, 8, "Which variant is the better default for the bench", [
        "• Which variant could serve as a first-pass default: the playbook recommends 2.1 for performance and Lite for local use, while 2 and 2.1 need an external key (left open)"],
        "T41, R032 rewording, T59: 'a bench-design choice for the user' replaced by 'left open'")

    # ------------------------------------------------------------------ R9
    for u, why in [
        ("https://developers.openai.com/api/docs/guides/your-data", "T11, T13: OpenAI data-controls page now cited in R7"),
        ("https://openai.com/policies/usage-policies", "T11: the HTTP 403 bullet names the usage-policies page"),
        ("https://ai.google.dev/gemini-api/terms", "T12, T13: Gemini API Additional Terms cited in R7"),
        ("https://ai.google.dev/gemma/prohibited_use_policy", "T10, T13: Gemma Prohibited Use Policy cited in R7"),
        ("https://policies.google.com/terms/generative-ai/use-policy", "T12, T13: Google Generative AI Prohibited Use Policy cited in R7"),
        ("https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001", "T34, T13: Google model page cited in R6"),
        ("https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/map_benchmark_labels.ipynb", "T19, T13: notebook cited in R5 and R7"),
        ("https://huggingface.co/datasets/govtech/RabakBench/tree/3c02a5b8574b0d0374d532704be6971e67532e22", "R032, T8: RabakBench pin cited in R7 (repo label needs an R9 URL)"),
        ("https://huggingface.co/spaces/govtech/lionguard-demo/blob/4ade46d19acee9c9088c711533a7c47fe24a8e3b/app/backend/services.py", "T5, T13: demo data-flow lines cited in R5 and R7"),
    ]:
        K.add_url(C, u, why)
