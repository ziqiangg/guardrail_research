# LionGuard resolutions 1 (P5, gr-resolver, 2026-10-09)

Items handled: all 34 class (a) items (T7, T9, T13 to T22, T24 to T29, T31, T34, T43, T45 to T52, T55 to T59) and all 5 class (c) items (T6, T8, T10, T11, T12). H items first (T6, T9, T21, T27, T49, T50, T51), then M, then L. The 20 class (b) items are not resolved (they stay open or were closed by R031); a closing note per item is in "Class (b) and CP1 items" at the end, with the documentation checks made on the way. Rulings applied: R031 (single column LN1, prefix `LionGuard:`, keep all variants and state the outside-service and gate dependencies, read the reachable OpenAI and Google terms pages so the test-text question is decided later), R032 (bench content is proposals; rewordings are listed under T59 and "R032 rewording"), R019, R020, R021, and main's P4 rulings in `scratchpad/main/queue.md` (arXiv 2507.05980 official; third-party facts only for embedder identity, gating, licence and terms; demo Space reference only, data-flow fact added to LN1 R5 and R7; Q04 stays two labelled bullets unless an official page reconciles them). Nothing was edited in the drafts. Line references `A:n` are lines of `lionguard_cols_a.md`, `INV` means `lionguard_inventory.md`, both as read at the start of this run.

## Method and access notes

- All reads were read-only GETs with `python benchtest/tools/fetch_text.py` (raw text), plus plain `curl` for md5 sums and the public unauthenticated Hugging Face Hub metadata JSON (`huggingface.co/api/...`, per the P4 ruling on Hub metadata) and GitHub raw files and `git ls-remote`. Raw copies: `benchtest/scratchpad/resolver/lionguard1/`.
- Read raw today (2026-10-09): `LICENSE`, `README.md`, `lionguard2.py` / `lionguard2lite.py` and `map_benchmark_labels.ipynb` of the model repos at the pinned shas; arXiv html v1 and v2 of 2507.15339; arXiv html and abs of 2507.05980; the three blog posts; the playbook page at the pin and at `main`, and the live site page; the Sentinel Guardrails page; the Gemma terms and Prohibited Use Policy; the Gemini API Additional Terms and Google's Generative AI Prohibited Use Policy; Gemini embeddings, models and pricing pages; OpenAI embeddings, data-controls and safety pages; the Hugging Face pages of `google/embeddinggemma-300m` and `BAAI/bge-large-en-v1.5`; dataset cards and the demo Space code.
- Not readable: `openai.com/policies/terms-of-use`, `/policies/service-terms`, `/policies/usage-policies`, `/policies/business-terms`, `/policies/row-terms-of-use` and `/policies/` all returned HTTP 403 to the fetch tool on 2026-10-09. No workaround was tried (R021). `aiguardian.gov.sg/docs/wiki/Sentinel-Onboarding-Guide` returned HTTP 403 to a plain GET.
- No sign-in, no form submission, no API call to any vendor (OpenAI, Google, Hugging Face inference), no weights download, no gated file requested. The GitHub API was used once, for the public file listing of `.github/workflows` of the playbook repo.
- Pins unchanged: on 2026-10-09 the Hub head revisions are still `lionguard-2` be4e38c9, `lionguard-2.1` 1c3a9ea7, `lionguard-2-lite` d56c17a0, `lionguard-v1` 92cc0491, Space 4ade46d1, `lionguard-2-synthetic-instruct` 8aa43f61, `RabakBench` 3c02a5b8, `RabakBench-full` 2cbe90c9. Playbook `staging` is still 45908b48 and `main` 97338569 (git ls-remote).

## Resolutions

### T6 — Q04 licence conflict (class c, H)
- Verdict: STILL OPEN as a source conflict (checked the LICENSE of four model repos and two datasets, the three card headers, the paper's contributions, ethics and conclusion text in html v1 and v2, the three blog posts, the playbook page, the Hugging Face collection and org pages, the Sentinel Guardrails page; no GovTech page states how the texts relate). Evidence collection is complete and adds three facts the drafts lack. No conclusion on permitted use is drawn.
- Evidence:
  - LICENSE, `govtech/lionguard-2@be4e38c9` (the same file, md5 01aeb061dcdbf0bd0612ad2b76ac5b6c, is in lionguard-2.1, lionguard-2-lite, lionguard-v1, lionguard-2-synthetic-instruct and RabakBench): "the contents of this repository are provided under the MIT License SUBJECT FURTHER TO THE FOLLOWING" (https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/LICENSE). Clause (1): the Terms "shall be governed by the laws of Singapore" with SIAC arbitration. Exclusion: "any asset or code identified by the Government Technology Agency ("GovTech") as not licensed to you".
  - Card header at the pin: `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` (README.md of lionguard-2, lionguard-2.1 and lionguard-2-lite, lines 3 to 5 each).
  - Paper ethics (html v1 line 514, v2 line 530): "Our model weights are published on Hugging Face exclusively for research and public interest purposes only, with clear usage guidelines that prohibit deployment for harmful applications." (https://arxiv.org/html/2507.15339).
  - Paper contributions (new): "We release the classifier weights and a portion of our training data to support future research in LLM safety." Paper conclusion (new): "By releasing our model weights and training data subset, we aim to support broader adoption of localisation-aware moderation strategies".
  - Blog 29 Jul 2025: "LionGuard 2 is open-sourced, including model weights and part of the training data." Playbook at 45908b48: "All three versions are open-sourced for self-hosting via Hugging Face".
  - Absence: none of the cards (the card text ends after the Usage section), the playbook, the blogs, the collection page or the org page contains a licence reconciliation or the "usage guidelines".
- Label to use: each text keeps its own label (LICENSE and card metadata `[Documented: repo ...]` per repo; paper, blog `[Documented]`); the relation `[Not disclosed]` with what was checked.
- Draft impact:
  - LN1 R1 Summary: remove "open" (see T49).
  - LN1 R4, replace A:86 to A:90 with the bullets below (md5 comparison becomes a plain-text hint, per-repo card metadata, the exclusion, two new paper bullets, ND bullet limited to the absence; the old A:90 inference "not obviously reconcilable and neither is a legal opinion" is dropped, see T57):
    - `• The LionGuard 2.1 repository holds a LICENSE file (md5 01aeb061dcdbf0bd0612ad2b76ac5b6c, the same as the LionGuard 2 file; checked 2026-10-09) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**`
    - `• The LionGuard 2 Lite repository holds a LICENSE file (md5 01aeb061dcdbf0bd0612ad2b76ac5b6c, the same as the LionGuard 2 file; checked 2026-10-09) **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**`
    - `• The LICENSE excludes "any asset or code identified by the Government Technology Agency ("GovTech") as not licensed to you" and GovTech and Singapore public-sector marks and images **[Documented: repo govtech/lionguard-2@be4e38c9]**`
    - `• The LionGuard 2 card metadata reads license: other, license_name: govtech-singapore, license_link: LICENSE **[Documented: repo govtech/lionguard-2@be4e38c9]**` (and two identical bullets for 2.1 and 2 Lite with their own labels, see T58)
    - after A:89: `• The paper's contributions say "We release the classifier weights and a portion of our training data to support future research in LLM safety" (arXiv 2507.15339 section 1) **[Documented]**` and `• The paper's conclusion says "By releasing our model weights and training data subset, we aim to support broader adoption of localisation-aware moderation strategies" (arXiv 2507.15339 section 8) **[Documented]**`
    - replace A:90 with `• How the repository LICENSE, the card metadata and the paper's research-only statement relate (checked the LICENSE, the three cards, the playbook page, the three blog posts, the paper's ethics, contributions and conclusion, the Hugging Face collection and organisation pages; not stated) **[Not disclosed]**`
  - LN1 R8 A:186: replace the end "; routed as a licensing item" with nothing: `... (checked the LICENSE, card metadata, paper, blogs and playbook; not stated)`.
  - INV(c) licence row (Access terms cell): replace the last two sentences "The two sources are not reconciled in any GovTech page read [Not disclosed] (...). This is a licensing item for the user and no conclusion on permitted use is drawn here" with "How the LICENSE, the card metadata and the paper's research-only statement relate [Not disclosed] (LICENSE, cards, PB, B1 to B3, the paper's contributions, ethics and conclusion, and the Hugging Face collection page checked; not stated)". Also add "The LICENSE excludes any asset or code identified by GovTech as not licensed to you [Documented: repo govtech/lionguard-2@be4e38c9] (LICENSE)" if not already in the cell.
  - INV(a) rows 11 to 14 Licence cells: no change except in the LionGuard 2 row, last sentence, add the same "paper contributions and conclusion" to the list of pages checked.
  - Summary change: R1 only (T49).

### T9 — Gemma Terms of Use cover EmbeddingGemma (class a, H)
- Verdict: RESOLVED.
- Evidence (https://ai.google.dev/gemma/terms, read 2026-10-09, not GovTech docs): "The terms below apply to Gemma models listed in the Appendix at bottom of this page." "Last modified: April 1, 2026". The Appendix list reads "Gemma 1 … FunctionGemma, EmbeddingGemma, PaliGemma …". Card of the embedder (https://huggingface.co/google/embeddinggemma-300m): "License: gemma"; Hub API `gated: manual`, `license:gemma`.
- Label to use: `[Documented]` (Google page, not GovTech docs).
- Draft impact:
  - LN1 R7 A:163, replace the `[To be verified]` bullet with: `• The Gemma Terms of Use Appendix lists EmbeddingGemma among the covered models (Google page, not GovTech docs; read 2026-10-09) **[Documented]**`
  - LN1 R8 A:187: delete the clause "and whether the Gemma terms cover EmbeddingGemma ... the Gemma appendix not read" (see T13 for the whole bullet).
  - INV(c) Gemma row: no change (already states "lists EmbeddingGemma in its Appendix [Documented]"); add the quote above to the Access terms cell if a verbatim hint is wanted.
  - LN1 R9: no new URL (https://ai.google.dev/gemma/terms already listed).
  - Summary change: none (the R7 Summary change comes from T51).

### T21 — R5 Summary headline number 77.0 (class a, H)
- Verdict: RESOLVED. Value confirmed in Table 1 and Table 3, html v1 (21 Jul 2025) and v2.
- Evidence (https://arxiv.org/html/2507.15339 and /2507.15339v1): Table 1 columns "Embeddings | Test | RabakBench | SS | ZH | MS | TA", row "text-embedding-3-large 3,072d … | 77.0 | 88.1 | 87.8 | 78.4 | 66.6". Table 3 row "LionGuard 2 | 77.0 | 88.1 | 87.8 | 78.4 | 66.6 | 98.8 | 92.1 | 97.4 | 64.5 | 99.7 | 98.2 | 99.2 | 71.5". Section 5.1: "we report binary F1 at a 0.5 threshold. For LionGuard 2, the score is taken from its dedicated safe/unsafe head". The "Test" column is the internal test set ("1 internal test set and 16 public benchmarks", section 5.1). The paper does not say the internal test set is released ("our complete training dataset remains private", ethics). The 28 Sep 2026 blog calls its split "a held-out private LionGuard test split and RabakBench".
- Label to use: `[Documented]` for the number; the premise in A:126 must name its real support (below).
- Draft impact:
  - R5 Summary: unchanged (77.0, 0.5 point and "own test set" are supported by A:108 and A:112).
  - LN1 R5 A:126, replace the premise: `• The original test split is private, so the 0.7318 figure for LionGuard 2.1 cannot be compared directly with the paper's 77.0 for LionGuard 2 (premise: the blog calls its split "a held-out private LionGuard test split", and the paper does not say its internal test set is released) **[Inferred]**`
  - Optional wording in A:112 and the Summary: "internal test set" instead of "own test set" (the paper's term).
  - Summary change: none.

### T27 — R2 Summary picks "partial Tamil" (class a, H)
- Verdict: RESOLVED (drafting fix; no new source needed).
- Evidence: card (https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/README.md): "tuned for English/Singlish, Chinese, Malay, and Tamil". Playbook: "Support for English, Singlish, Chinese, Malay, and partial Tamil." Paper abstract: "supporting English, Chinese, Malay, and partial Tamil"; section 5.3: "its Tamil performance remains moderate". Both the playbook and the paper (abstract) say partial, so the Summary can say "the playbook and paper call Tamil partial or moderate" without picking the card's side silently.
- Label to use: `[Documented]` (three sources named; the Detail keeps the three bullets A:28 to A:30).
- Draft impact:
  - LN1 R2 Summary, replace by (43 words before the label):
    `Summary: **Six harm categories plus an overall flag, with severity levels.** Hateful, insults, sexual, physical violence, self-harm and all other misconduct; four have Level 1 and Level 2. Covers English, Singlish, Chinese, Malay and Tamil; the playbook and paper call Tamil partial or moderate. **[Documented]**`
  - INV(a) rows 12 to 14 Languages cells: no change.
  - Summary change: R2 (new text above).

### T49 — R1 Summary "you run it yourself from open Hugging Face weights" (class a, H)
- Verdict: RESOLVED (drafting fix after R031 and T6).
- Evidence: Lite card: "LionGuard 2 Lite runs fully locally, with no external API calls". LionGuard 2 card usage comment: "Get OpenAI embeddings (users to input their own OpenAI API key)"; 2.1: "users to input their own Gemini API key" (README.md at the pins). Licence wording is unresolved (T6), so "open" should not be asserted in a Summary.
- Label to use: `[Documented]` (cards, playbook; the "embed text through" statement is the usage code in the cards).
- Draft impact:
  - LN1 R1 Summary, replace by (44 words before the label):
    `Summary: **Localised harmful-content classification of one text string.** LionGuard is GovTech's classifier for Singapore's languages and context. It returns a probability for each harm category and severity level. GovTech publishes the classifier on Hugging Face; two variants embed text through OpenAI or Gemini, one locally. **[Documented]**`
  - LN1 R1 A:12 and A:17 stay as quoted facts (playbook "open-sourced for self-hosting"; blog "open-sourced"), each with its own label.
  - Summary change: R1 (new text above).

### T50 — R4 Summary "publishes only the small classifier" (class a, H)
- Verdict: RESOLVED (drafting fix).
- Evidence: the model repos hold the code: `lionguard2.py` (LionGuard2Model class), `inference.py`, `config.json` (Hub file lists at the pins); the dataset card says "This dataset is a subset of the LionGuard 2 training corpus." The embedders are the owners' models (card: "leverages OpenAI's `text-embedding-3-large`", "Gemini's `gemini-embedding-001`", "Google's `embeddinggemma-300m`"); `model.safetensors` is 3,398,496 bytes (2, 2.1) and 1,039,200 bytes (Lite) per the Hub API.
- Label to use: `[Documented]`.
- Draft impact:
  - LN1 R4 Summary, replace by (40 words before the label):
    `Summary: **Frozen embedder plus a small ordinal classifier.** The three variants differ in the embedder: OpenAI embeddings (LionGuard 2), Gemini embeddings (2.1) or local EmbeddingGemma (2 Lite). GovTech publishes the small classifier and its code on Hugging Face, not the embedder. **[Documented]**`
  - The "no training code" fact stays as the `[Not disclosed]` bullet A:82 (Detail only).
  - Summary change: R4 (new text above).

### T51 — R7 Summary "no API key" for Lite omits the Hugging Face login (class a, H)
- Verdict: RESOLVED.
- Evidence (https://huggingface.co/google/embeddinggemma-300m, not GovTech docs): "This repository is publicly accessible, but you have to accept the conditions to access its files and content." and "Log in or Sign Up to review the conditions and access this model content." Hub API: `gated: manual`. Lite card usage: `SentenceTransformer("google/embeddinggemma-300m")` with no token argument (README.md@d56c17a0:63).
- Label to use: `[Documented]` for the login and gate; `[Inferred]` for the setup statement (premise named).
- Draft impact:
  - LN1 R7 Summary, replace by (59 words before the label; R032 wording, no package names):
    `Summary: **Minimum setup:** Python with Hugging Face Transformers and PyTorch, loading each model with remote code enabled. LionGuard 2 Lite also needs a Hugging Face login and acceptance of Google's Gemma terms for its embedder, but no API key. LionGuard 2 needs an OpenAI key and 2.1 a Gemini key, so test text goes to those providers. No threshold ships. **[Inferred]**`
  - LN1 R7 A:159, replace by: `• LionGuard 2 Lite path: install sentence-transformers, log in to Hugging Face and accept Google's conditions for google/embeddinggemma-300m, then the classifier and embedder run locally with no embedding API key (premise: the card says "runs fully locally" and the embedder page is gated) **[Inferred]**`
  - LN1 R7, after A:161 add: `• Accepting the conditions needs a Hugging Face login: "Log in or Sign Up to review the conditions and access this model content." (Hugging Face page of google/embeddinggemma-300m, not GovTech docs) **[Documented]**`
  - LN1 R6 A:143: change to `• LionGuard 2 Lite needs no API key (card: "runs fully locally, with no external API calls") but downloads Google's gated embedder **[Documented: repo govtech/lionguard-2-lite@d56c17a0]**` (drops "(see R7)").
  - INV(c) EmbeddingGemma row: already carries the login fact; no change.
  - Summary change: R7 (new text above).

### T13 — Column and inventory disagree on what was read (class a, M)
- Verdict: RESOLVED (after T9, T11, T12).
- Evidence: see T9 (Gemma Appendix read), T12 (Gemini Additional Terms read) and T11 (OpenAI data-controls page read; OpenAI policy pages HTTP 403).
- Label to use: as in T9, T11, T12.
- Draft impact:
  - LN1 R7 A:166 and A:167 and R8 A:187: replace as in T11 and T12 below.
  - LN1 R9: add after A:219 (one URL per bullet, no commentary): `https://developers.openai.com/api/docs/guides/your-data`, `https://ai.google.dev/gemini-api/terms`, `https://ai.google.dev/gemma/prohibited_use_policy`, `https://policies.google.com/terms/generative-ai/use-policy`, `https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001`, `https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/map_benchmark_labels.ipynb`, `https://huggingface.co/datasets/govtech/RabakBench/tree/3c02a5b8574b0d0374d532704be6971e67532e22`, `https://huggingface.co/spaces/govtech/lionguard-demo/blob/4ade46d19acee9c9088c711533a7c47fe24a8e3b/app/backend/services.py`, `https://github.com/govtech-responsibleai/playbook/blob/97338569d8711ae4c7a6615a34deb92a720beba8/.github/workflows/pages-staging.yml` (only the ones that the final text cites).
  - INV(c) rows 40 and 41 Source URL cells: add `https://developers.openai.com/api/docs/guides/your-data` is already there; add `https://openai.com/policies/usage-policies` only if the 403 fact is kept (T11).
  - Summary change: none.

### T14 — Third-party embedder behaviour facts in cells (class a, M)
- Verdict: RESOLVED by main's P4 ruling (keep only model identity, max input, output dimension, gating, licence and terms, each attributed "not GovTech docs"; drop other third-party behaviour). No source needed.
- Evidence: queue.md, "lionguard P4 Q2". Applying it to the draft text:
  - Keep: A:139 (OpenAI default dimension), A:141 (Google default dimension), A:160 to A:162 (gating, licence, terms), INV(c) rows 40 (8192, 3072), 42 (2048, 768), INV(a) row 13 (Google default 3072), INV(e) row 75 (OpenAI 8192).
  - Drop (lifecycle, not identity): the Gemini sentences "For text-only use cases, gemini-embedding-001 remains available" and "a newer model gemini-embedding-2" (INV(c) row 41 and A:191).
  - Keep, as terms: OpenAI "not used to train" and abuse-monitoring retention; Gemini paid and unpaid data terms.
- Label to use: unchanged.
- Draft impact:
  - INV(c) Gemini row (line 41), delete the sentence `Google docs say "For text-only use cases, gemini-embedding-001 remains available" and name a newer model gemini-embedding-2 [Documented] (GEM, not GovTech docs).` and add the input limit and dimension (T34): `Google's model page gives an input token limit of 2,048 and an output dimension of 128 to 3072 for gemini-embedding-001 [Documented] (Google model page, not GovTech docs)`.
  - LN1 R8 A:191, replace by: `• Whether an embedder change would shift scores: the paper warns an OpenAI embedding update may need retraining (whether GovTech will retrain is not stated)`.
  - INV(c) rows 40 to 42: no other change.
  - Summary change: none.

### T15 — arXiv 2507.05980 as an official source (class a, M)
- Verdict: RESOLVED (main ruled yes). Authorship checked.
- Evidence (https://arxiv.org/abs/2507.05980): "Authors:Gabriel Chua, Leanne Tan, Ziyu Ge, Roy Ka-Wei Lee"; html v2 author lines "Affiliation: GovTech, Singapore" (two authors also list Singapore University of Technology and Design); "Submitted on 8 Jul 2025 (v1), last revised 2 Feb 2026 (this version, v2)". Title "Lost in Localization: Building RabakBench with Human-in-the-Loop Validation to Measure Multilingual Safety Gaps". Table 4 (html v2) row "LlamaGuard 4 12B | 60.53 | 54.20 | 65.92 | 73.77 | 63.61" under Singlish, Chinese, Malay, Tamil, Average.
- Label to use: `[Documented]` (vendor-authored paper).
- Draft impact:
  - Brief official-source list: add arXiv 2507.05980 (main to log).
  - INV(d): add an 11th row (block (d) count 10 to 11; tell the owner of the config module `build_lionguard_inventory.py`):
    `| arXiv 2507.05980 Lost in Localization: Building RabakBench with Human-in-the-Loop Validation to Measure Multilingual Safety Gaps [Documented] (arXiv abstract page). Authors Gabriel Chua, Leanne Tan, Ziyu Ge, Roy Ka-Wei Lee [Documented] (arXiv abstract page) | Paper (vendor-authored; RabakBench) | GovTech authors, with two co-authors also listing SUTD | Submitted 8 Jul 2025 (v1), last revised 2 Feb 2026 (v2) [Documented] (arXiv abs) | Open on arXiv [Documented] (HTTP 200 observed 2026-10-09) | — (inventory only, not in Table 3) | https://arxiv.org/abs/2507.05980 ; https://arxiv.org/html/2507.05980 |`
  - LN1 R5 A:115: add "(html v2 of 2 Feb 2026)" to the source hint; see T22 for the changed wording of the numbers.
  - Summary change: none.

### T16 — Playbook pin on `staging` (class a, M)
- Verdict: RESOLVED. The site is built from `staging`, and the page text is identical on `main`, so no `[Documented: develop/unreleased]` label is needed.
- Evidence: workflow `pages-staging.yml` at main@97338569 and staging@45908b48 (https://github.com/govtech-responsibleai/playbook/blob/97338569d8711ae4c7a6615a34deb92a720beba8/.github/workflows/pages-staging.yml): name "Deploy Docusaurus (staging)", line 5 `branches: ["staging"]`, lines 21 and 22 `DOCUSAURUS_SITE_URL: https://govtech-responsibleai.github.io`, `DOCUSAURUS_BASE_URL: /playbook/`. `website/docs/tools/lionguard.md` has md5 2f55a48a2403b4fb7f80ff2d9c8ef501 at both 45908b48 and 97338569. The live page https://govtech-responsibleai.github.io/playbook/tools/lionguard/ shows "partial Tamil" and "open-sourced for self-hosting" (same text) and "Last updated on Jul 28, 2026". `main` has only this one Pages workflow.
- Label to use: unchanged, `[Documented: repo govtech-responsibleai/playbook@45908b48]`.
- Draft impact:
  - INV scope paragraph, replace "(staging branch; page footer reads Last updated on Jul 28, 2026)" with "(the branch the playbook site is built from; the same page text is on main at 97338569; page footer reads Last updated on Jul 28, 2026)".
  - INV(d) playbook row, Revision cell: replace "Staging branch commit 45908b48 (main is at 97338569, git ls-remote 2026-10-09) [Documented: repo govtech-responsibleai/playbook@45908b48]" with "Commit 45908b48 on staging, the branch the site is built from (workflow pages-staging.yml); the page file is identical at main 97338569 (md5 compared 2026-10-09) [Documented: repo govtech-responsibleai/playbook@45908b48]".
  - LN1 R9: no change needed for this fact (the workflow URL need not be cited in R1 to R8).
  - Summary change: none.

### T19 — `map_benchmark_labels.ipynb` not read (class a, M)
- Verdict: RESOLVED. The notebook maps benchmark labels to the LionGuard taxonomy; it holds no threshold, calibration or model call.
- Evidence (code read, not run; https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/map_benchmark_labels.ipynb, 37 cells): cell 0 "This notebook standardizes safety labels across multiple benchmark datasets by mapping their original category systems to a unified taxonomy." It maps seven datasets: "mmathys/openai-moderation-api-evaluation", "PKU-Alignment/BeaverTails", "Bertievidgen/SimpleSafetyTests", "ToxicityPrompts/RTP-LX", "sorry-bench/sorry-bench-202406", "SGHateCheck", "SGToxicGuard". No cell contains "threshold", "0.5", "predict", "calibrat" or a call to the model.
- Label to use: `[Documented: repo govtech/lionguard-2@be4e38c9]`.
- Draft impact:
  - INV(a) LionGuard 2 row, "HF repo and revision" cell: replace "(notebook not read)" with "(the notebook maps the labels of seven public benchmark datasets to the six-category taxonomy and holds no threshold or model call; code read, not run)".
  - LN1 R5 A:107 ND bullet: add "the label-mapping notebook" to the list of what was checked.
  - LN1 R7: add two bullets as possible evaluation data sources (R032 wording, see "R032 rewording" below).
  - Summary change: none.

### T22 — Table 1 versus Table 3 order for Chinese and Malay (class a, M)
- Verdict: RESOLVED as a source conflict that stays carried (two bullets, no silent pick); label convention aligned; extra supporting evidence found.
- Evidence (html v1 and v2): Table 1 header "SS | ZH | MS | TA"; Table 3 header "SS | MS | ZH | TA"; both give LionGuard 2 "77.0 | 88.1 | 87.8 | 78.4 | 66.6". RabakBench paper Table 4 (https://arxiv.org/html/2507.05980) columns "Singlish | Chinese | Malay | Tamil": "AWS Bedrock Guardrail | 66.50 | 0.59 | 18.49 | 0.57" and "LlamaGuard 4 12B | 60.53 | 54.20 | 65.92 | 73.77". In LionGuard 2 Table 3 (header SS, MS, ZH, TA) the AWS Bedrock row is "57.1 | 69.6 | – | 21.1 | –" (the "–" under MS marks an unsupported language) and the LlamaGuard 4 12B row is "26.5 | 60.6 | 54.6 | 65.2 | 73.0". So the values under Table 3's "MS" label sit close to RabakBench's Chinese values (0.59 unsupported, 54.20) and those under "ZH" close to RabakBench's Malay (18.49, 65.92). Blog 29 Jul 2025: "Performance remains robust for Chinese (88%) and Malay (78%)".
- Label to use: the two table facts `[Documented]`; the swap `[Inferred]` (premise: the AWS Bedrock "–" position and the LlamaGuard 4 values match RabakBench Table 4 only if Table 3's second column is Chinese). Use `[Inferred]` in both files.
- Draft impact:
  - LN1 R5 A:115, replace by: `• The GovTech RabakBench paper Table 4 gives LlamaGuard 4 12B Singlish 60.53, Chinese 54.20, Malay 65.92, Tamil 73.77, and AWS Bedrock Guardrail Chinese 0.59 and Malay 18.49, while Table 3 of the LionGuard 2 paper gives LlamaGuard 4 12B 60.6, 54.6, 65.2, 73.0 and AWS Bedrock 69.6, –, 21.1, – under SS, MS, ZH, TA (arXiv 2507.05980 Table 4, html v2; arXiv 2507.15339 Table 3) **[Documented]**`
  - LN1 R5 A:116: keep, but add the Bedrock premise: `(premise: the RabakBench values match Table 3 only if the second column is Chinese, including the unsupported-language dash for AWS Bedrock)`; label stays `[Inferred]`.
  - INV(a) LionGuard 2 row, Operating threshold cell: replace "Which header order is right [To be verified]" with "Table 3's Chinese and Malay labels are probably swapped, because the RabakBench paper Table 4 values for other systems match Table 3 only in that reading [Inferred] (P2 Tables 1 and 3; arXiv 2507.05980 Table 4)".
  - LN1 R8 A:185: unchanged except add "(a rerun on the public RabakBench set could settle it)" (T23).
  - Summary change: none.

### T24 — Smaller numeric inconsistencies in the paper (class a, M)
- Verdict: RESOLVED. Each digit re-read in html v2; the brief's "66.6 versus 66.5 in Table 8" is true; the BeaverTails and SORRY-Bench repeat is real, not a slip.
- Evidence (arXiv 2507.15339 html v2): Table 4 row "LionGuard 2 | 73.7 | 73.7 | 70.5 | 100.0" under "BT | SRY-B | OAI | SST". Table 5 row "LionGuard 2 | 87.1 | 85.6" (RabakBench Singlish, without and with noise) against 88.1 in Tables 1 and 3. Table 8 "Binary F1 on Tamil splits when adding machine-translated data", row "LionGuard 2 | 66.5 | 64.5 | 71.5" under "RB_TA | SGHC_TA | SGTG_TA" against 66.6 in Tables 1 and 3, and 64.5 and 71.5 equal to Table 3.
- Label to use: `[Documented]`.
- Draft impact:
  - LN1 R5 A:117, replace by: `• RabakBench Singlish is 88.1 in Tables 1 and 3 and 87.1 in Table 5, and RabakBench Tamil is 66.6 in Tables 1 and 3 and 66.5 in Table 8; no source explains the differences (arXiv 2507.15339 Tables 1, 3, 5 and 8) **[Documented]**`
  - LN1 R5 A:118: no change (73.7 and 73.7 is as printed in Table 4); optionally add "as printed".
  - LN1 Reviewer note 6 (moves to the change log): the "Table 8" claim is now verified.
  - Summary change: none.

### T25 — "about 4%" binary-head disagreement (class a, M)
- Verdict: RESOLVED. The paper's "about 4%" corresponds to the over-prediction rate; under-prediction is a further 0.70%.
- Evidence (arXiv 2507.15339 html v2): section 7.2 "About 4% of examples aggregated across two localised and three general datasets show disagreement between the binary head and category heads (Appendix E.1)." Table 11 row "Overall average | 4.19 | 0.70 | 43 075" with "Over-predict means the binary head flags unsafe while all categories remain below threshold; under-predict is the opposite." Caption: "The binary head over-flags in only 4 % of cases and under-flags in <1 %". Section 7.2: "Although deriving the binary decision as max(category-scores) removes the mismatch, we keep the dedicated binary head as it boosts performance".
- Label to use: `[Documented]`.
- Draft impact:
  - LN1 R5 A:123, replace by: `• The paper says "About 4% of examples … show disagreement between the binary head and category heads" (section 7.2); Table 11 gives an overall average of 4.19% over-predicted and 0.70% under-predicted over 43,075 samples, with RabakBench Singlish highest at 9.99% over-predict (arXiv 2507.15339 section 7.2, Appendix E.1, Table 11) **[Documented]**`
  - LN1 R5, add: `• The paper says deriving the binary decision as the maximum of the category scores "removes the mismatch", and keeps the dedicated binary head because it boosts performance (arXiv 2507.15339 section 7.2) **[Documented]**`
  - LN1 R7 A:172: change "since the paper reports about 4%" to "since the paper reports the binary head over-predicting in about 4% of examples".
  - LN1 R8 A:181: replace by `• Whether the dedicated binary key or the maximum of the category keys is the better verdict (the paper keeps the binary head because it boosts performance and says the maximum removes the mismatch; which works better per variant needs testing)`.
  - INV(a) LionGuard 2 row: replace "About 4% of examples show disagreement between the binary head and the category heads [Documented] (P2 section 7.2)" with "About 4% of examples show disagreement between the binary head and the category heads; the overall average is 4.19% over-predicted and 0.70% under-predicted [Documented] (P2 section 7.2, Table 11)".
  - Summary change: none.

### T29 — Throughput 300 tokens/s and the embedding call (class a, M)
- Verdict: PARTLY RESOLVED. The text is confirmed; whether the "embedding call" is the hosted OpenAI request is not stated.
- Evidence (arXiv 2507.15339 section 3): "Running synchronously on a single CPU, the embedding call handles ≈250 tokens/s, while the classifier head itself processes ≈1.5×10^4 tokens/s, giving an end-to-end throughput of ≈300 tokens/s." and "As most latency comes from the embedding call, batching or caching embeddings can raise throughput well beyond these figures." Absence: the paper (sections 3, 7.1, Appendix hardware paragraph, which covers only decoder fine-tuning) does not say whether the embedding call is the hosted OpenAI API or a local model, and gives no hardware model.
- Label to use: `[Documented]` for the quotes; `[Not disclosed]` for the hosted-versus-local question.
- Draft impact:
  - LN1 R6 A:150: unchanged; add after it: `• Whether the paper's "embedding call" is the hosted OpenAI request, and the CPU model used (checked the paper sections 3 and 7.1 and its hardware paragraph; not stated) **[Not disclosed]**`
  - LN1 R8 A:184: keep as the open question (needs testing for the measured half).
  - INV(a) LionGuard 2 row: replace "including the embedding call" with "where the embedding call handles about 250 tokens per second and most latency comes from it" and add "whether that call is the hosted OpenAI request [Not disclosed] (P2 sections 3 and 7.1 checked)".
  - Summary change: none.

### T31 — Residual document check for a threshold (class a, M)
- Verdict: RESOLVED (confirmed `[Not disclosed]`).
- Evidence (absence, searched case-insensitively for threshold, calibrat, cut-off, operating point): the three model cards, both dataset cards, the notebook (T19), the playbook page, blogs 1 and 2 (no hit), blog 3 (only "using the same 0.5 threshold" and calibration plots for LionGuard 2.1 against the comparator), the paper (only the 0.5 evaluation point, section 5.1, and Appendix E.1), the Sentinel Guardrails LionGuard section (only the severity-level table, no cut-off). Hosted Sentinel behaviour stays under Sentinel.
- Label to use: `[Not disclosed]`.
- Draft impact:
  - LN1 R5 A:107: extend the list of what was checked to "the three cards, the two dataset cards, the label-mapping notebook, the playbook, the paper, the three blog posts and the demo Space README".
  - INV(a) rows 12 to 14 operating threshold cells: add "the label-mapping notebook and dataset cards" to LionGuard 2's checked list only where the file exists.
  - Summary change: none.

### T34 — Maximum input length per variant, documentation half (class a, M)
- Verdict: RESOLVED. GovTech states none (confirmed); owners' pages give the embedder limits, which match the Sentinel table.
- Evidence (not GovTech docs): OpenAI embeddings page table "text-embedding-3-large | 9,615 | 64.6% | 8192" under "Max input" (https://developers.openai.com/api/docs/guides/embeddings). Google model page (https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001): "Input token limit 2,048", "Output dimension size Flexible, supports: 128 - 3072". Hugging Face page of EmbeddingGemma: "Maximum input context length of 2048 tokens". GovTech: Sentinel Guardrails page "lionguard-2 … 8192", "lionguard-2-1 … 2048", "lionguard-2-lite … 2048" (hosted service). Note: the Google embeddings guide page states "The overall maximum input tokens limit is 8192 tokens" in its multimodal section for gemini-embedding-2 only; the 2,048 figure is the one for gemini-embedding-001.
- Label to use: `[Documented]` for each owner limit, attributed "not GovTech docs"; GovTech's own silence stays `[Not disclosed]`.
- Draft impact:
  - LN1 R6, after A:149 add three bullets:
    - `• LionGuard 2 embedder limit: OpenAI lists a max input of 8192 for text-embedding-3-large (OpenAI docs, not GovTech docs) **[Documented]**`
    - `• LionGuard 2.1 embedder limit: Google lists an input token limit of 2,048 for gemini-embedding-001 (Google model page, not GovTech docs) **[Documented]**`
    - `• LionGuard 2 Lite embedder limit: the Hugging Face page of EmbeddingGemma lists a maximum input context length of 2048 tokens (Google page, not GovTech docs) **[Documented]**`
  - LN1 R6 A:154: unchanged (Sentinel's 8192, 2048, 2048 now agree with the owners' limits; keep as cross-reference).
  - LN1 R8 A:183: replace by `• What happens on text longer than each embedder's limit, and whether Singlish, Chinese and Tamil token counts change the effective limit (the owners state the limits; GovTech states none; needs testing)`.
  - INV(c) Gemini row: add the 2,048 limit (see T14). INV(e) row 75: add "Google and EmbeddingGemma pages give 2,048 [Documented] (Google pages, not GovTech docs)".
  - Summary change: none.

### T45 — Does the stale `text-embedding-3-small` docstring recur in 2.1 and Lite? (class a, M)
- Verdict: RESOLVED. No: only the LionGuard 2 file carries it.
- Evidence (code read at the pins): `lionguard2.py@be4e38c9:97` "…after it has been encoded with OpenAI's `text-embedding-3-small` model." and `:104` "…the embeddings from OpenAI's `text-embedding-3-small` model". `lionguard2.py@1c3a9ea7:97` "The model takes in an input text that has been encoded with Gemini's `gemini-embedding-001` model." `lionguard2lite.py@d56c17a0:97` "…encoded with Google's `embeddinggemma-300m` model." Line 9: `INPUT_DIMENSION = 3072  # length of OpenAI embeddings` (LionGuard 2), `3072 … Gemini` (2.1), `768 … EmbeddingGemma-300m` (Lite). Otherwise the three files differ only in class names and the model name in docstrings (diff run locally). OpenAI's embeddings page gives 1536 as the default dimension for text-embedding-3-small, so the docstring's "defaults to 3072" fits the large model (OpenAI page, not GovTech docs).
- Label to use: `[Documented: repo govtech/lionguard-2@be4e38c9]` for the conflict; 2.1 and Lite `[Documented: repo ...]` for their correct docstrings.
- Draft impact:
  - LN1 R4 A:69, replace by: `• Conflict: the docstring of lionguard2.py in LionGuard 2 says the input is encoded with OpenAI's text-embedding-3-small, while the card, inference.py and config.json use text-embedding-3-large at 3072 dimensions (lionguard2.py@be4e38c9:97) **[Documented: repo govtech/lionguard-2@be4e38c9]**` and add `• The docstrings of the LionGuard 2.1 and 2 Lite model files name their own embedders, gemini-embedding-001 and embeddinggemma-300m, so the stale name occurs only in the LionGuard 2 file (lionguard2.py@1c3a9ea7:97) **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**` and the same with `lionguard2lite.py@d56c17a0:97` under `[Documented: repo govtech/lionguard-2-lite@d56c17a0]` (one label per repo).
  - INV(a) rows 13 and 14: no change.
  - Summary change: none.

### T48 — Playbook says paper and blog "describe how each version works" (class a, M)
- Verdict: RESOLVED (kept as written; wider check done).
- Evidence (absence): searched html v1 and v2 of 2507.15339 and the three blog posts for "gemini-embedding", "embeddinggemma", "Gemma", "2.1", "lite": hits only "Gemini 2.0 Flash" and "AWS Nova Lite" as annotators, ShieldGemma as a related model, and blog 3's mentions of LionGuard 2.1 results. Blog 3 (28 Sep 2026) says: "LionGuard requires both embedding generation, which can be run locally or through an API depending on the variant, and classifier inference on the selected hardware." Playbook: "so the LionGuard 2 [paper] and [blog post] describe how each version works".
- Label to use: playbook sentence `[Documented: repo govtech-responsibleai/playbook@45908b48]`; absence `[Not disclosed]`.
- Draft impact:
  - LN1 R4 A:74: extend the checked list to name "html v1 and v2 of the paper and the blog of 28 Sep 2026, which only says embedding generation 'can be run locally or through an API depending on the variant'".
  - Summary change: none.

### T57 — Inference inside Documented or Not-disclosed bullets (class a, M)
- Verdict: RESOLVED (drafting fixes).
- Evidence: README section 3 rule 5; support for the replacement facts: Hub API sha equals the pin on 2026-10-09 for all three model repos, `lastModified` 2025-11-18T07:20:21Z (lionguard-2), 2025-11-18T09:01:38Z (2.1), 2025-11-18T08:59:25Z (Lite); blog 21 Aug 2026 "Reporting and access to retrained models are currently only available to Sentinel users within the Singapore Government."
- Label to use: facts `[Documented]`, conclusions `[Inferred]`.
- Draft impact:
  - LN1 R4 A:61, replace by two bullets: `• A GovTech blog (21 Aug 2026) says "LionGuard 2 uses a shared representation feeding into 11 classification heads" (GovTech AI blog) **[Documented]**` and `• The code has seven head modules and eleven output keys, so the blog's 11 probably counts output keys (premise: lionguard2.py@be4e38c9:172-177 gives eleven keys from seven heads) **[Inferred]**`.
  - LN1 R4 A:90: see T6 (rewritten as an absence only).
  - LN1 R4 A:92, replace by two bullets: `• The three model repositories were last modified 2025-11-18, and their head revisions on 2026-10-09 are the pinned ones (Hugging Face API, read 2026-10-09) **[Documented]**` and `• No retrained model has therefore been published in those repositories (premise: no commit since 2025-11-18 and the blog says retrained models are for Sentinel users) **[Inferred]**`.
  - Summary change: none.

### T7 — Licence sub-items (class a, M)
- Verdict: RESOLVED.
- Evidence: (i) the paper's "clear usage guidelines that prohibit deployment for harmful applications" are not located: the LICENSE has no such text, the cards end after the Usage section, the playbook and the three blogs contain no "guideline" or "prohibit" text for LionGuard (case-insensitive search of cards, LICENSE, playbook, blogs, Hugging Face collection page). (ii) The LICENSE exclusion is quoted under T6. (iii) The card metadata of 2.1 and Lite is identical (`license: other`, `license_name: govtech-singapore`, `license_link: LICENSE`, README.md lines 3 to 5 at each pin).
- Label to use: `[Not disclosed]` for (i); `[Documented: repo ...]` per repo for (ii) and (iii).
- Draft impact:
  - LN1 R4: add (after the T6 ND bullet) `• The "clear usage guidelines that prohibit deployment for harmful applications" named in the paper's ethics section (checked the LICENSE, the three cards, the playbook page and the three blog posts; no such guidelines found) **[Not disclosed]**`
  - LN1 R4 A:88: replace by three bullets, one per repo (see T58).
  - INV(a) rows 13 and 14 Licence cells: already carry the metadata; no change.
  - Summary change: none.

### T8 — Licences of the other GovTech artefacts (class c, M)
- Verdict: PARTLY RESOLVED. Terms of the public sets are read; RabakBench-full has none.
- Evidence: RabakBench card (https://huggingface.co/datasets/govtech/RabakBench/blob/3c02a5b8574b0d0374d532704be6971e67532e22/README.md): `license: other`, `license_name: govtech-singapore`; "Intended Uses: Benchmark moderation APIs / guardrails. Research on code-mixing toxicity detection." "Out-of-Scope Uses: Fine-tuning models to generate **unsafe content**." The LICENSE of RabakBench and of lionguard-2-synthetic-instruct has md5 01aeb061dcdbf0bd0612ad2b76ac5b6c (same as the model repos). `RabakBench-full` (https://huggingface.co/datasets/govtech/RabakBench-full): "This repository is publicly accessible, but you have to accept the conditions to access its files and content." "No dataset card yet"; Hub `gated: manual`, `cardData: None`; files `rabakbench_en.csv`, `_ms`, `_ta`, `_zh`; `LICENSE` returns HTTP 404. Demo Space: README front matter holds no licence key; no LICENSE file in the file list.
- Label to use: `[Documented: repo govtech/RabakBench@3c02a5b8]`; for RabakBench-full and the Space `[Not disclosed]` (card, metadata and file list checked); access terms of the gated set are shown only to a signed-in user and were not requested.
- Draft impact:
  - INV(d) RabakBench row, Licence or access cell: append `Intended uses on the card: "Benchmark moderation APIs / guardrails" and "Research on code-mixing toxicity detection"; out-of-scope use: "Fine-tuning models to generate unsafe content" [Documented: repo govtech/RabakBench@3c02a5b8] (card)`.
  - INV(d) RabakBench-full row: the existing cell is correct (gated manual, no LICENSE or licence metadata `[Not disclosed]`); add "(HTTP 404 for LICENSE, Hub cardData empty; observed 2026-10-09)".
  - LN1 R7 and R8: no claim about permitted use of RabakBench; the possible-source bullet (see "R032 rewording") quotes the card's intended use only.
  - Summary change: none.

### T10 — Gemma terms: Model Derivative and the Prohibited Use Policy (class c, M)
- Verdict: PARTLY RESOLVED. The text is quoted (below); GovTech does not discuss either point; how the terms apply is a judgement for the user and is not decided here.
- Evidence (Google pages, not GovTech docs, read 2026-10-09):
  - Section 3.2 (https://ai.google.dev/gemma/terms): "You must not use any of the Gemma Services: for the restricted uses set forth in the Gemma Prohibited Use Policy … or in violation of applicable laws and regulations."
  - Section 1.1(e): "Model Derivatives" means "(iii) any other machine learning model which is created by transfer of patterns of the weights, parameters, operations, or Output of Gemma, to that model in order to cause that model to perform similarly to Gemma"; and "For clarity, Outputs are not deemed Model Derivatives."
  - Section 3.1: "You must include the use restrictions referenced in Section 3.2 as an enforceable provision in any agreement … governing the use and/or distribution of Gemma or Model Derivatives".
  - Prohibited Use Policy, Last modified February 21, 2024 (https://ai.google.dev/gemma/prohibited_use_policy): "You may not use nor allow others to use Gemma or Model Derivatives to:" … "Generating content that promotes or encourages hatred;" … "Generate sexually explicit content, including content created for the purposes of pornography or sexual gratification (e.g. sexual chatbots). Note that this does not include content created for scientific, educational, documentary, or artistic purposes."
  - GovTech silence: the Lite README, LICENSE and playbook do not mention the Gemma terms, derivatives or the policy (searched).
- Label to use: `[Documented]` for each quoted term (Google page, not GovTech docs); `[Not disclosed]` for GovTech's position.
- Draft impact:
  - LN1 R7, after the T9 bullet add (one fact each):
    - `• Gemma Terms of Use section 3.2 says "You must not use any of the Gemma Services: for the restricted uses set forth in the Gemma Prohibited Use Policy" or "in violation of applicable laws and regulations" (Google page, not GovTech docs) **[Documented]**`
    - `• The Gemma Prohibited Use Policy (last modified February 21, 2024) lists "Generating content that promotes or encourages hatred" and "Generate sexually explicit content", with a note that this "does not include content created for scientific, educational, documentary, or artistic purposes" (Google page, not GovTech docs) **[Documented]**`
    - `• The Gemma terms define Model Derivatives to include a model "created by transfer of patterns of the weights, parameters, operations, or Output of Gemma" and say "Outputs are not deemed Model Derivatives" (Google page, not GovTech docs) **[Documented]**`
  - LN1 R8 A:187: see T13 (whole bullet below).
  - INV(c) Gemma row: replace the last two sentences by "Section 3.1 sets conditions for Distribution of Gemma or Model Derivatives, and section 1.1(e) defines Model Derivatives [Documented] (same page, not GovTech docs). The Prohibited Use Policy page is at ai.google.dev/gemma/prohibited_use_policy [Documented] (Google page, not GovTech docs). Whether the LionGuard 2 Lite classifier counts as a Model Derivative, and whether embedding harmful test text is a restricted use [Not disclosed] (Lite README, LICENSE and PB checked; not discussed)". Add the policy URL to the Source URL cell.
  - Summary change: none.

### T11 — OpenAI side of the terms question (class c, M)
- Verdict: PARTLY RESOLVED. The data-controls page now answers the embeddings-endpoint question; the OpenAI terms and usage-policy pages are unreadable (HTTP 403).
- Evidence (https://developers.openai.com/api/docs/guides/your-data, not GovTech docs, read 2026-10-09): "Your data is your data. As of March 1, 2023, data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)." "By default, abuse monitoring logs are generated for all API feature usage and retained for up to 30 days, unless longer retention is required by law …". Endpoint table, columns "Endpoint | Data used for training | Abuse monitoring retention | Application state retention | Zero Data Retention eligible", row "/v1/embeddings | No | 30 days | None | Yes". HTTP 403 for https://openai.com/policies/terms-of-use, /service-terms, /usage-policies, /business-terms, /row-terms-of-use (observed 2026-10-09).
- Label to use: `[Documented]` for the page facts; the content of OpenAI's usage policies and terms about harmful or explicit input `[To be verified]` (not readable).
- Draft impact:
  - LN1 R7, replace A:166 with these bullets (one HTTP fact per bullet, one fact each):
    - `• OpenAI's data-controls page says data sent to the OpenAI API "is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)" (OpenAI docs, not GovTech docs) **[Documented]**`
    - `• The same page lists /v1/embeddings with no training use, abuse-monitoring retention of 30 days, no application-state retention, and Zero Data Retention eligibility "Yes" (OpenAI docs, not GovTech docs; read 2026-10-09) **[Documented]**`
    - `• https://openai.com/policies/terms-of-use, /service-terms and /usage-policies returned HTTP 403 to the fetch tool (observed 2026-10-09) **[Documented]**`
    - `• platform.openai.com/docs/guides/your-data ends at developers.openai.com/api/docs/guides/your-data (final URL, HTTP 200, observed 2026-10-09) **[Documented]**`
  - LN1 R7 A:167 `[To be verified]`: replace by the R8-style unlabelled open question (see T13 below). INV(c) OpenAI row: replace "Whether those logs apply to embeddings calls [To be verified]" with "The same page lists /v1/embeddings with abuse-monitoring retention of 30 days and Zero Data Retention eligibility Yes [Documented] (OAI data controls page, not GovTech docs). Whether OpenAI's usage policies or service terms restrict harmful or explicit input to the embeddings endpoint [To be verified] (the pages returned HTTP 403)". Add `https://openai.com/policies/usage-policies` to the Source URL cell only if the 403 fact is kept.
  - Summary change: none.

### T12 — Gemini side of the terms question (class c, M)
- Verdict: PARTLY RESOLVED. Terms read; the tier is set by the billing account, not by the endpoint; the terms do not mention embeddings; whether gemini-embedding-001 has a free tier is not stated on the pricing page.
- Evidence (https://ai.google.dev/gemini-api/terms, "Effective March 23, 2026", page last updated 2026-04-28, not GovTech docs): "Any Services that are offered free of charge like direct interactions with Google AI Studio or unpaid quota in Gemini API are unpaid Services". Unpaid: "Do not submit sensitive, confidential, or personal information to the Unpaid Services." and "human reviewers may read, annotate, and process your API input and output". Tier: "Your access to Gemini API is a "Paid Service" only when accessing the API through a Cloud Project associated with an active billing account." Paid: "Google doesn't use your prompts … or responses to improve our products" and "Google logs prompts and responses for a limited period of time, solely for detecting and preventing violations of the Prohibited Use Policy". Use restriction: "you must comply with our Prohibited Use Policy". Generative AI Prohibited Use Policy (Last Modified December 17, 2024, https://policies.google.com/terms/generative-ai/use-policy): "Do not engage in sexually explicit, violent, hateful, or harmful activities. This includes generating or distributing content that facilitates: …" and "We may make exceptions to these policies based on educational, documentary, scientific, or artistic considerations". Pricing page (https://ai.google.dev/gemini-api/docs/pricing) lists "Gemini Embedding 2" with a free tier and "Used to improve our products | Yes | No" but no entry for gemini-embedding-001. Search of the terms page for "embed": only a navigation label.
- Label to use: `[Documented]` for the quoted terms (Google pages, not GovTech docs); embeddings treatment and the free-tier status of gemini-embedding-001 `[Not disclosed]` (terms page and pricing page checked).
- Draft impact:
  - LN1 R7, replace A:167's Gemini half and add (one fact each):
    - `• Gemini API Additional Terms (effective March 23, 2026) say of unpaid quota: "Do not submit sensitive, confidential, or personal information to the Unpaid Services" (Google page, not GovTech docs) **[Documented]**`
    - `• The same terms say "Your access to Gemini API is a "Paid Service" only when accessing the API through a Cloud Project associated with an active billing account", and that for Paid Services Google "doesn't use your prompts … or responses to improve our products" (Google page, not GovTech docs) **[Documented]**`
    - `• Google's Generative AI Prohibited Use Policy (last modified December 17, 2024) says "Do not engage in sexually explicit, violent, hateful, or harmful activities" and allows exceptions "based on educational, documentary, scientific, or artistic considerations" (Google page, not GovTech docs) **[Documented]**`
    - `• Whether the Gemini terms treat an embedding call differently from other calls, and whether gemini-embedding-001 has a free tier (checked the terms and pricing pages; the terms do not mention embeddings and the pricing page lists only gemini-embedding-2) **[Not disclosed]**`
  - INV(c) Gemini row: replace "Which tier applies to an embedding call and to the bench key [To be verified]" with "The tier depends on whether the API is reached through a Cloud Project with an active billing account [Documented] (same page, not GovTech docs). Whether gemini-embedding-001 has a free tier [Not disclosed] (terms and pricing pages checked)". Add `https://policies.google.com/terms/generative-ai/use-policy` to the Source URL cell.
  - Summary change: none.

### T13 (R8 part) — Terms bullet in R8
- Draft impact (R8 A:187), replace by: `• Whether OpenAI's usage policies and service terms (the pages returned HTTP 403) and Google's Gemini and Gemma terms allow sending harmful or explicit test text to the embedding services, and which account tier would apply (the owners' data-handling pages are quoted in R7; which test text may be sent is left to be decided before any testing; owners' pages only, not GovTech docs)`
- R8 Summary: replace by `Summary: **Key open questions.** Operating threshold per variant, any Lite or wider 2.1 evaluation, input length and latency, how the licence texts relate, embedder terms for test text, whether a retrained model is released, and jailbreak coverage.` (36 words; label-free.)

### T17 — Sentinel docs cross-reference facts (class a, L)
- Verdict: RESOLVED.
- Evidence (https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails, HTTP 200 read 2026-10-09, no pin): section "LionGuard Versions" table "lionguard-2 | OpenAI's text-embedding-large-3 | 8192", "lionguard-2-1 | Google's gemini-embedding-001 | 2048", "lionguard-2-lite | Google's embeddinggemma-300m | 2048"; rows "lionguard-2-binary | Input/Output | Detects if the text contains harmful content of any kind". The Onboarding Guide link `/docs/wiki/Sentinel-Onboarding-Guide` returns HTTP 403 to a plain GET (2026-10-09).
- Label to use: `[Documented]`, no pin, read date in plain text.
- Draft impact: add "(read 2026-10-09)" to the Sentinel source hints in A:53, A:94, A:95, A:154 and INV(e); mention the 403 only in the URL check (P9). Summary change: none.

### T18 — Provenance of blog, Sentinel and playbook quotes (class a, L)
- Verdict: RESOLVED. Quotes re-read live today and match.
- Evidence (verbatim in today's raw text): blog 29 Jul 2025 "Performance remains robust for Chinese (88%) and Malay (78%), though slightly behind popular solutions like LlamaGuard 4 for Tamil." and heading "LionGuard 2 as an input and output guardrail"; blog 21 Aug 2026 "Architecturally, LionGuard 2 uses a shared representation feeding into 11 classification heads", "more than 200 false positives and false negatives", "we'll be rolling out the first retrained LionGuard 2 model, incorporating your feedback, very soon.", "Reporting and access to retrained models are currently only available to Sentinel users within the Singapore Government."; blog 28 Sep 2026 "A fair latency comparison would therefore require a more controlled setup.", "the same 0.5 threshold", "lower average calibration error on the original test set and the English/Singlish and Chinese RabakBench sets"; playbook (raw at 45908b48 and main) and live page; Sentinel table (T17). Differences found: none. Blog 3 numbers (0.7318 and the six others) match the table.
- Label to use: unchanged.
- Draft impact: none (move Reviewer notes 9 of A and 8 of INV to the change log as "re-read live at P5"). Summary change: none.

### T20 — Completeness of the Hugging Face model list (class a, L)
- Verdict: RESOLVED.
- Evidence (public Hub listing, https://huggingface.co/api/models?author=govtech, /datasets?author=govtech, /spaces?author=govtech, read 2026-10-09): 7 models: lionguard-v1, lionguard-2, lionguard-2.1, lionguard-2-lite, jina-embeddings-v2-small-en-off-topic, stsb-roberta-base-off-topic, llama3-8b-sea-lionv2.1-instruct-secure. 10 datasets: MinorBench, PolicyBench, PolicyBenchFull, CIRCLE, lionguard-2-synthetic-instruct, RabakBench, RabakBench-full (manual), RubricBench (manual), SynthSite, veiled-sh (manual). 5 Spaces: off-topic-demo, system-prompt-leakage, Biome, lionguard-demo, rai-bench. No further LionGuard model repo (no ONNX or retrained variant).
- Label to use: `[Documented]` (Hub listing, read 2026-10-09).
- Draft impact:
  - INV(d) intro, replace "the org's Hugging Face listing holds 7 models, 10 datasets and 5 Spaces [Not disclosed] (those checks; training code not published where found)" with "No training or inference repository exists on GitHub [Not disclosed] (those checks). The org's Hugging Face listing holds 7 models (the four LionGuard repos here plus two off-topic classifiers and a SEA-LION chat model), 10 datasets (three LionGuard-related datasets here; the others are unrelated) and 5 Spaces (one LionGuard demo here) [Documented] (Hub listing, read 2026-10-09)".
  - Summary change: none.

### T26 — 16 versus 17 benchmarks (class a, L)
- Verdict: RESOLVED (reconciliation kept as `[Inferred]`, now with a count).
- Evidence (arXiv 2507.15339 html v2): abstract "outperforms several commercial and open-source systems across 17 benchmarks"; section 5.1 "on 1 internal test set and 16 public benchmarks, including 13 localised datasets from Chua et al. (2025); Ng et al. (2024) and 4 general English datasets". Table 3 has 13 columns (Test, RabakBench x4, SGHateCheck x4, SGToxicGuard x4) and Table 4 has 4, which sum to 17 with the internal Test column counted among the 13.
- Label to use: `[Inferred]` (arithmetic on the tables).
- Draft impact: LN1 R5 A:122, replace by `• The counts fit together if the 13 localised datasets include the internal test set (premise: Table 3 has 13 columns including Test, and Table 4 adds 4 English sets, giving 17 in all, or 1 internal and 16 public) **[Inferred]**`. Summary change: none.

### T28 — Different test sets side by side (class a, L)
- Verdict: RESOLVED (drafting).
- Evidence: A:31 already names the native-speaker test set (Table 13: Chinese 85.0, Malay 81.4, Tamil 41.1, overall 72.7 F1); A:112 names RabakBench (Tamil 66.6, Chinese 87.8, Malay 78.4).
- Label to use: `[Documented]`.
- Draft impact: LN1 R2 A:31 stays as is (it names the native-speaker test set). Add after it a separate bullet: `• This is a different test set from RabakBench, so the Tamil F1 of 41.1 here and 66.6 in Table 1 are not comparable (premise: Table 13 is the native-speaker set and Table 1 is RabakBench) **[Inferred]**`. Summary change: none.

### T43 — Remote code and revision pinning (class a, L)
- Verdict: RESOLVED (alignment, R032 wording).
- Evidence: README usage in all three cards: `AutoModel.from_pretrained("govtech/lionguard-2", trust_remote_code=True)`, `("govtech/lionguard-2.1", trust_remote_code=True)`, `("govtech/lionguard-2-lite", trust_remote_code=True)` with no `revision` argument (README.md lines 61 to 64, 59, 60).
- Label to use: `[Documented: repo ...]` per repo for the README facts (A:75 to A:77 already); `[Inferred]` for the suggestion.
- Draft impact:
  - LN1 R7 A:158 stays the minimum-setup bullet; add after it: `• A bench could pin each model repository to a revision, because the README loads the repository code with trust_remote_code=True and no revision argument, so the repository's Python runs on load (premise: the README usage and the repos can change) **[Inferred]**`
  - INV(c) trust_remote_code row: replace "Pinning a revision for the bench is advisable [Inferred]" with "A bench could pin a revision [Inferred]". Summary change: none.

### T46 — Sentinel docs spell "text-embedding-large-3" (class a, L)
- Verdict: RESOLVED (kept as written).
- Evidence: Sentinel page "lionguard-2 | OpenAI's text-embedding-large-3 | 8192"; card and playbook "text-embedding-3-large"; OpenAI embeddings page lists "text-embedding-3-large".
- Label to use: `[Documented]` for the Sentinel spelling (no pin, read 2026-10-09).
- Draft impact: none. Summary change: none.

### T47 — "11 heads" explained as "counting output keys" (class a, L)
- Verdict: RESOLVED. Handled with T57 (split into a Documented bullet and an Inferred bullet).
- Draft impact: see T57, LN1 R4 A:61. Summary change: none.

### T52 — LionGuard 1 embedding dimension (class a, L)
- Verdict: RESOLVED. The embedder owner's page gives the dimension and sequence length.
- Evidence (https://huggingface.co/BAAI/bge-large-en-v1.5, not GovTech docs, read 2026-10-09): MTEB table "BAAI/bge-large-en-v1.5 | 1024 | 512" under "Dimension | Sequence Length"; `1_Pooling/config.json` "word_embedding_dimension": 1024; "License: mit". GovTech's `config.json` sets `"max_length": 512` for the same model.
- Label to use: `[Documented]` (BAAI page, not GovTech docs).
- Draft impact:
  - INV(a) LionGuard 1 row, Embedding model cell: replace "Embedding dimension [Not disclosed] (README, config.json and inference.py checked)" with "The embedder's owner lists a dimension of 1024 and a sequence length of 512 [Documented] (BAAI model page, not GovTech docs); GovTech files state no dimension [Not disclosed] (README, config.json and inference.py checked)".
  - INV(c) BAAI row: append "The page lists dimension 1024 and sequence length 512 [Documented] (BAAI page, not GovTech docs)". Summary change: none.

### T55 — Covered-by convention for block (d) and (e) rows (class a, L)
- Verdict: RESOLVED by convention (no source).
- Evidence: R011 and the marker set; INV self-check (21 header cells, 2 legacy, 14 inventory-only).
- Label to use: n/a.
- Draft impact: no change: block (d) rows (including the new arXiv 2507.05980 row from T15) keep `— (inventory only, not in Table 3)`; block (c) third-party rows keep the LN1 header; block (e) keeps the inventory-only marker with no Sentinel header. Main may log this as a precedent. Summary change: none.

### T56 — Frozen Sentinel final cites section 7.2 for the binary head (class a, L)
- Verdict: RESOLVED (FYI for the change log; no edit to frozen sheets).
- Evidence (arXiv 2507.15339 html v2): the binary head ("we attached a single binary head (safe/unsafe)") is under 4.2.2 "Training a Lightweight Classifier"; section 7.2 is "Misalignment between binary and category labels". "Tamil 66.6 versus 66.5": Table 8 row "LionGuard 2 | 66.5 | 64.5 | 71.5" and Tables 1 and 3 "66.6" (T24), so that Sentinel claim is correct.
- Label to use: n/a.
- Draft impact: change-log note only. Summary change: none.

### T58 — One label for two sources or for a computation (class a, L)
- Verdict: RESOLVED (drafting).
- Evidence: README section 3 rule 5; the per-repo card metadata and the md5 hint are shown under T6 and T7.
- Label to use: see below.
- Draft impact:
  - LN1 R4 A:62, replace by two bullets: `• LionGuard 2 classifier size: 848,942 float32 parameters and a model.safetensors of 3,398,496 bytes (Hugging Face API, read 2026-10-09) **[Documented: repo govtech/lionguard-2@be4e38c9]**` and `• The paper says "The resulting classifier contains 0.85M parameters and occupies only 3.2 MB on disk" (arXiv 2507.15339 section 4.2.2) **[Documented]**`
  - LN1 R4 A:86 and A:87: md5 comparison becomes a plain-text hint (T6 text).
  - LN1 R4 A:88, replace by three bullets (T7 text), one per repo: `• The LionGuard 2.1 card metadata reads license: other, license_name: govtech-singapore, license_link: LICENSE **[Documented: repo govtech/lionguard-2.1@1c3a9ea7]**`, and the same for `govtech/lionguard-2-lite@d56c17a0` and `govtech/lionguard-2@be4e38c9`.
  - INV(a) Licence cells and INV(c) licence row: "(md5 ..., compared 2026-10-09)" stays as a plain-text hint after the repo label (already so). Summary change: none.

### T59 — Process language and ruling ids in deliverable text (class a, L)
- Verdict: RESOLVED (rewordings listed; the merger applies them once the TBV bullets are replaced by T9, T11, T12).
- Evidence: README section 7 and the Presidio T9 precedent (finals carry no process language).
- Label to use: unchanged per bullet.
- Draft impact:
  - LN1 R3 A:53: delete "; covered under the Sentinel column" (keep "(Sentinel docs, hosted API, read 2026-10-09)").
  - LN1 R4 A:90 and R6 A:143: delete "(see R7)" (T6, T51 texts).
  - LN1 R7 A:163, A:166, A:167: replaced by T9, T11, T12 text (no "was not read", "was not worked around", or "returned HTTP 403 to the fetch tool" beyond the one HTTP-fact bullet).
  - LN1 R7 A:176: delete the bullet ("Nothing is run during research; this is the plan for the bench (R019)").
  - LN1 R8 A:186: delete ", routed as a licensing item"; A:192: replace "(a bench-design choice for the user)" with "(left open)".
  - INV scope paragraph: delete "(R019)" after "marked "not GovTech docs""; INV(c) intro: replace by "What a team running the models itself must obtain. Third-party rows cite the owner's own page and are not GovTech docs. No embedding service was called and no weights were downloaded." (delete "(R019)" and "Nothing was signed in to, requested or called; the OpenAI and Google service terms were read only where quoted."); INV(c) licence row: see T6.
  - Summary change: none.

## R032 rewording (bench content as proposals)

Text in R7, R8 and the inventory that reads as a decided bench plan, with proposed replacements (no research behind them; the merger applies them). Labels stay `[Inferred]`.

- LN1 R7 A:164: `... and each text to be classified is sent to OpenAI to be embedded (premise: inference.py embeds the texts through the OpenAI client) **[Inferred]**` (drops "that is a data-handling decision for the bench"). A:165: same change for Google and `genai`.
- LN1 R7 A:168 to A:175, replace with:
  - `• A bench could use labelled safe and unsafe examples for each of the six categories and both levels, including Level 2 cases to check that Level 1 is also high **[Inferred]**`
  - `• A bench could add benign near-misses (for example matter-of-fact talk about sexuality, or news about violence) to measure false positives **[Inferred]**`
  - `• A bench could cover English, Singlish, Chinese, Malay and Tamil, with translated pairs, and expect weaker Tamil results (premise: the paper's Tamil figures) **[Inferred]**`
  - `• A bench could add noisy variants (casing, punctuation, misspellings) of a subset to repeat the paper's robustness check **[Inferred]**`
  - `• A bench could log the binary score and the category scores to count disagreements, since the paper reports the binary head over-predicting in about 4% of examples **[Inferred]**`
  - `• A bench could sweep thresholds per key and score the same texts as prompts and as model responses, plus any retrieved text or tool output it uses **[Inferred]**`
  - `• A bench could run the same set through LionGuard 2, 2.1 and 2 Lite and time each embedding call separately from the classifier call **[Inferred]**`
  - `• The dataset embeddings would allow a head-only smoke test with no external calls, but the set is Singlish and English only and about 2% unsafe, so it is unlikely to suit as an evaluation set (premise: dataset card statistics of 2,055 safe and 43 unsafe) **[Inferred]**`
- LN1 R7, add possible sources of evaluation data (suggestion wording):
  - `• Possible source of evaluation data: the RabakBench public set (132 samples per language), whose card lists "Benchmark moderation APIs / guardrails" as an intended use **[Documented: repo govtech/RabakBench@3c02a5b8]**`
  - `• The notebook map_benchmark_labels.ipynb maps seven public datasets (OpenAI moderation evaluation, BeaverTails, SimpleSafetyTests, RTP-LX, SORRY-Bench, SGHateCheck, SGToxicGuard) to the six-category taxonomy (code read, not run) **[Documented: repo govtech/lionguard-2@be4e38c9]**`
  - `• Those seven datasets could serve as further possible sources of evaluation data, with their own terms to be checked (premise: GovTech's notebook maps their labels to this taxonomy) **[Inferred]**`
- LN1 R7 A:176: delete (T59). LN1 R8 A:192: `• Which variant could serve as a first-pass default: the playbook recommends 2.1 for performance and Lite for local use, while 2 and 2.1 need an external key (left open)` (T41).
- INV(a) rows: no bench wording found. INV(c) trust_remote_code row: "Pinning a revision for the bench is advisable" becomes "A bench could pin a revision" (T43). INV(d) demo Space row: see T5 below.

## Class (b) and CP1 items (not resolved here; closing notes)

| ID | Status | Note and proposed text |
|---|---|---|
| T1 | closed by R031 | One column LN1. No draft change; the per-variant bullets stay. |
| T2 | closed by R031 | Prefix `LionGuard:`. No change; frozen after CP2. |
| T3 | closed by R031 | All three variants kept; dependencies stated in R7 and INV(c) (T49, T51, T9 to T12 give the wording). |
| T4 | closed by R031 for P5 | Terms facts are now in the file (T9 to T13). Which test text may be sent is left to be decided before bench testing; R7 and R8 wording above is a proposal. The OpenAI usage policies and service terms stay unreadable (HTTP 403). |
| T5 | main ruling applies | Demo Space is a reference only (submitting text is a form submission under CLAUDE.md rule 5). Add the data-flow fact, below. |
| T23 | stays open | Needs authors or a rerun on the public RabakBench set. No change. |
| T30 | stays open | Paper's hardware paragraph covers only decoder fine-tuning (g4dn.xlarge or A100); no latency, memory or GPU figure for 2.1 or Lite in the cards, playbook, paper or blogs (re-checked). |
| T32, T35, T42 | stay open (testing) | No change; R019 bars installs and API calls in research. |
| T33, T37 | stay open (honest gap) | Re-checked: Lite has no evaluation in cards, playbook, paper, blogs or the demo; 2.1 has only the blog 3 table. |
| T36 | documentation half closed | Paper Appendix E.2 says annotators were encouraged to write "prompt-injection or role-playing scenarios"; Tables 13 to 16 give results by language, overall and by category only, so no per-subset result exists. A:37 `[Not disclosed]` stands; testing half stays open. |
| T38 | stays open (honest gap) | Hub head revisions equal the pins on 2026-10-09 (T57). |
| T39 | stays open (honest gap) | Sentinel page and playbook checked again; no statement that hosted and open weights are the same. |
| T40 | stays open (honest gap) | Wording change per T14 (drop the Google lifecycle clause). |
| T41 | CP1 item, suggestion wording | R8 text under "R032 rewording". |
| T44 | stays open (honest gap) | `git ls-remote` for govtech-responsibleai/lionguard, /lionguard-demo, /lionguard2 and /LionGuard answered "Repository not found" again on 2026-10-09; the Hub listing (T20) shows no training repo. |
| T53 | stays open (honest gap) | Access not requested (R019). Hub `cardData: None` and no LICENSE (HTTP 404), see T8. |
| T54 | partly closed | Hub API for the Space (read 2026-10-09): runtime stage RUNNING, sha 4ade46d1. Whether the Google Sheet is configured is not visible from the repo (secrets are read from environment variables). |

### T5 — Demo Space data flow (proposed text)
- Evidence (code read at 4ade46d1, `app/backend/services.py`): line 158 `if GOOGLE_SHEET_URL and GOOGLE_CREDENTIALS:` followed by a results row holding `"text": text`, `"binary_score": binary_score`, and `save_results_data(results_row)` which calls `ws.append_row(list(row.values()))` (line 62); line 338 `if GOOGLE_SHEET_URL and GOOGLE_CREDENTIALS:` followed by `_log_chatbot_sync` (the chat message and category scores are appended to a sheet); lines 33 and 199 to 214: `openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))` and `get_openai_response_async`, and lines 217 to 223 call OpenAI moderation. The Space README says only "Demo for LionGuard 2.".
- Draft impact:
  - LN1 R5, after A:110 add: `• The demo's analysis route appends each submitted text, its binary score and per-category maxima to a Google Sheet, and its chat route logs the message and scores to a Google Sheet, in both cases only when a sheet URL and service-account credentials are configured (services.py@4ade46d1:158-165, :338-341) **[Documented: repo govtech/lionguard-demo@4ade46d1]**`
  - LN1 R5, add: `• The demo's chat route also sends each message to OpenAI for a chat reply and for OpenAI moderation (services.py@4ade46d1:199-223) **[Documented: repo govtech/lionguard-demo@4ade46d1]**`
  - LN1 R7, add: `• A bench could avoid the hosted demo for test text, because its code may write submissions to a Google Sheet and sends chat messages to OpenAI (premise: services.py@4ade46d1 behaviour above; whether the live Space has the sheet configured is not visible) **[Inferred]**`
  - INV(d) demo Space row, "Revision or date" cell: replace "Live status [To be verified]" in the access cell with "Live status: the Hub API reports runtime stage RUNNING [Documented] (HFAPI, read 2026-10-09)". Keep the existing data-flow sentence and add "The hosted Space is a reference only" if main wants it recorded in the sheet.
  - R9: add the `services.py` blob URL (T13 list).
  - Summary change: none.

## Summary table

| T | Verdict | Label | Changes a Summary? |
|---|---|---|---|
| T6 | STILL OPEN (conflict carried; evidence complete) | `[Documented: repo ...]` / `[Documented]` per text; relation `[Not disclosed]` | R1 (via T49) |
| T9 | RESOLVED | `[Documented]` | no |
| T21 | RESOLVED | `[Documented]` | no |
| T27 | RESOLVED | `[Documented]` | R2 |
| T49 | RESOLVED | `[Documented]` | R1 |
| T50 | RESOLVED | `[Documented]` | R4 |
| T51 | RESOLVED | `[Documented]`, `[Inferred]` | R7 |
| T13 | RESOLVED | per T9, T11, T12 | R8 Summary text (optional) |
| T14 | RESOLVED (main ruling) | unchanged | no |
| T15 | RESOLVED | `[Documented]` | no |
| T16 | RESOLVED | `[Documented: repo govtech-responsibleai/playbook@45908b48]` | no |
| T19 | RESOLVED | `[Documented: repo govtech/lionguard-2@be4e38c9]` | no |
| T22 | RESOLVED (conflict carried) | `[Documented]`, `[Inferred]` | no |
| T24 | RESOLVED | `[Documented]` | no |
| T25 | RESOLVED | `[Documented]` | no |
| T29 | PARTLY RESOLVED | `[Documented]`, `[Not disclosed]` | no |
| T31 | RESOLVED (ND confirmed) | `[Not disclosed]` | no |
| T34 | RESOLVED | `[Documented]` (owners), `[Not disclosed]` (GovTech) | no |
| T45 | RESOLVED | `[Documented: repo ...]` | no |
| T48 | RESOLVED | `[Documented: repo ...]`, `[Not disclosed]` | no |
| T57 | RESOLVED | `[Documented]`, `[Inferred]` | no |
| T7 | RESOLVED | `[Not disclosed]`, `[Documented: repo ...]` | no |
| T8 | PARTLY RESOLVED | `[Documented: repo govtech/RabakBench@3c02a5b8]`, `[Not disclosed]` | no |
| T10 | PARTLY RESOLVED | `[Documented]`, `[Not disclosed]` | no |
| T11 | PARTLY RESOLVED | `[Documented]`, `[To be verified]` | no |
| T12 | PARTLY RESOLVED | `[Documented]`, `[Not disclosed]` | no |
| T17 | RESOLVED | `[Documented]` | no |
| T18 | RESOLVED | unchanged | no |
| T20 | RESOLVED | `[Documented]` | no |
| T26 | RESOLVED | `[Inferred]` | no |
| T28 | RESOLVED | `[Documented]`, `[Inferred]` | no |
| T43 | RESOLVED | `[Documented: repo ...]`, `[Inferred]` | no |
| T46 | RESOLVED | `[Documented]` | no |
| T47 | RESOLVED | `[Documented]`, `[Inferred]` | no |
| T52 | RESOLVED | `[Documented]` | no |
| T55 | RESOLVED (convention) | n/a | no |
| T56 | RESOLVED (FYI) | n/a | no |
| T58 | RESOLVED | per bullet | no |
| T59 | RESOLVED | per bullet | no |

## Report

1. Counts per verdict over the 39 assigned items (34 class a, 5 class c): RESOLVED 33, PARTLY RESOLVED 5 (T8, T10, T11, T12, T29), STILL OPEN 1 (T6, a source conflict that no official page reconciles), CORRECTION 0 as a verdict (corrections are listed in item 2). T55 and T56 are RESOLVED by convention or as FYI. The 20 class (b) items were not resolved; T1 to T3 are closed by R031, T5 by main's ruling, T36 and T54 had their documentation halves checked.
2. CORRECTIONs to the drafts (facts in the draft that the sources contradict or that were mis-stated), listed although filed under RESOLVED:
   - A:123, R7 A:172, R8 A:181 and INV(a): "about 4% disagreement" actually matches the over-predict rate; the paper's own Table 11 gives 4.19% over and 0.70% under (T25).
   - A:126: the premise "the paper's test set is not published" is not stated in the paper; replaced by the blog's own wording (T21).
   - A:115 and INV(a): Table 3 values for LlamaGuard 4 12B are close to, not equal to, RabakBench Table 4 (60.6 / 54.6 / 65.2 / 73.0 versus 60.53 / 54.20 / 65.92 / 73.77) (T22).
   - A:163 and A:187: "Gemma Appendix not read" is moot; the Appendix lists EmbeddingGemma (T9).
   - INV(c) Gemini row: the "remains available" and "gemini-embedding-2" sentence falls under main's drop rule (T14).
   - The brief's "66.5 in Table 8" is true; reviewer note 6 can be dropped (T24).
3. Summary lines that must change: R1 (T49), R2 (T27), R4 (T50), R7 (T51); optionally R8 (T13) and the code-identifier fixes R3 ("The classifier call takes only an array of embeddings of the text.") and R6 ("then pass the vectors to the classifier"). New texts are in the entries above. R5 Summary (77.0) is confirmed unchanged.
4. Items still open after P5: licence relation (T6), OpenAI usage policies and service terms (T11, HTTP 403, `[To be verified]`), Gemini embeddings free-tier status (T12), whether the paper's embedding call is the hosted OpenAI request (T29), Model Derivative and Prohibited Use Policy applicability (T10, user judgement), and all class (b) testing items.
5. Count changes for the merger: INV block (d) goes from 10 to 11 rows (T15); the R9 additions are listed under T13; no change to the Covered-by markers.

QUESTIONS
- Q-A (main, for the brief): T15 adds an 11th row to inventory block (d), so the config module `build_lionguard_inventory.py` needs BLOCKS 4/11/8/11/4. Confirm before the merge.
- Q-B (main): the RabakBench card cites a second paper (arXiv 2507.11966, on the translation approach). Not read here; say if it should be checked for authorship and added as a source.
- Q-C (user, only if the licence reading matters to the bench): T6 stays two or more labelled texts with the relation `[Not disclosed]`; no official page reconciles them.
