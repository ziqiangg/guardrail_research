"""Inventory edits for lionguard (sheet 3x). Imported by merge_lionguard.py."""

R2L = "[Documented: repo govtech/lionguard-2@be4e38c9]"
HDR = "LionGuard: Localised harmful-content classification"


def apply(V):
    # ------------------------------------------------------------------ scope paragraph
    V.para_sub("(staging branch; page footer reads Last updated on Jul 28, 2026)",
               "(the branch the playbook site is built from; the same page text is on main at 97338569; page footer reads Last updated on Jul 28, 2026)",
               "T16: the site is built from staging and the page file is identical on main (workflow and md5 read), so no unreleased label is needed")
    V.para_sub('are cited only for gating, licence, terms and embedder identity and are marked "not GovTech docs" (R019).',
               'are cited only for embedder identity (model name, input limit, output dimension), gating, licence and terms, and are marked "not GovTech docs".',
               "T14 (main P4 Q2), T59: scope of third-party facts stated; ruling id removed")
    V.para_sub("nothing was installed, run or downloaded, and no API was called.",
               "nothing was installed, run or downloaded, and no model or embedding service was called; the public Hugging Face Hub metadata was read with plain GET requests.",
               "hygiene: 'no API was called' contradicted the HFAPI reads (public metadata JSON); reworded")
    V.para_sub("P1 = arXiv 2407.10995 (LionGuard 1);",
               "P1 = arXiv 2407.10995 (LionGuard 1); RB = arXiv 2507.05980 (GovTech RabakBench paper, html v2 of 2 Feb 2026);",
               "T15: short name for the RabakBench paper, now an official source")

    # ------------------------------------------------------------------ (a)
    V.sub("a", "=LionGuard 1 (legacy)", "Embedding model",
          "Embedding dimension [Not disclosed] (README, config.json and inference.py checked)",
          "The embedder's owner lists a dimension of 1024 and a sequence length of 512 [Documented] (BAAI model page, not GovTech docs); GovTech files state no dimension [Not disclosed] (README, config.json and inference.py checked)",
          "T52: dimension from the embedder owner's page")
    V.sub("a", "=LionGuard 2", "HF repo", "(notebook not read)",
          "(the notebook maps the labels of seven public benchmark datasets to the six-category taxonomy and holds no threshold or model call; code read, not run)",
          "T19: notebook read")
    V.sub("a", "=LionGuard 2", "Operating threshold",
          "(README, config.json, inference.py, lionguard2.py, PB, P2 and B1 to B3 checked; only the 0.5 evaluation point and the demo bands in block (d) exist)",
          "(README, config.json, inference.py, lionguard2.py, the label-mapping notebook, the two dataset cards, PB, P2 and B1 to B3 checked; only the 0.5 evaluation point and the demo bands in block (d) exist)",
          "T31, T19: checked list extended")
    V.sub("a", "=LionGuard 2", "Operating threshold", "Which header order is right [To be verified].",
          "Table 3's Chinese and Malay labels are probably swapped, because the RabakBench paper Table 4 values for other systems match Table 3 only in that reading [Inferred] (P2 Tables 1 and 3; RB Table 4).",
          "T22: one label convention with the column (Inferred, premise named)")
    V.sub("a", "=LionGuard 2", "Operating threshold",
          "About 4% of examples show disagreement between the binary head and the category heads [Documented] (P2 section 7.2)",
          "About 4% of examples show disagreement between the binary head and the category heads; the overall average is 4.19% over-predicted and 0.70% under-predicted [Documented] (P2 section 7.2, Table 11)",
          "T25, CORRECTION: 'about 4%' is the over-prediction rate")
    V.sub("a", "=LionGuard 2", "Operating threshold",
          "End-to-end throughput about 300 tokens per second on one CPU, including the embedding call [Documented] (P2 section 3)",
          "End-to-end throughput about 300 tokens per second on one CPU, where the embedding call handles about 250 tokens per second and most latency comes from it [Documented] (P2 section 3). Whether that call is the hosted OpenAI request [Not disclosed] (P2 sections 3 and 7.1 checked)",
          "T29: 'including the embedding call' restated as the paper words it; hosted-versus-local recorded as an absence")
    V.sub("a", "=LionGuard 2", "Licence",
          "The LICENSE text has no research-only wording [Documented: repo govtech/lionguard-2@be4e38c9]. How the two relate [Not disclosed] (LICENSE, card, PB and B1 Open-Sourced section checked)",
          "The LICENSE text has no research-only wording [Not disclosed] (LICENSE read in full). How the LICENSE, the card metadata and the paper's research-only statement relate [Not disclosed] (LICENSE, card, PB, B1 Open-Sourced section, the paper's contributions, ethics and conclusion, and the Hugging Face collection page checked; not stated)",
          "T6; hygiene (README section 3 rule 2): an absence in the LICENSE is Not disclosed, not Documented")

    # ------------------------------------------------------------------ (c)
    V.para_sub("What a team running the models itself must obtain. Third-party rows are cited to the owner's own page and are not GovTech docs (R019). Nothing was signed in to, requested or called; the OpenAI and Google service terms were read only where quoted.",
               "What a team running the models itself must obtain. Third-party rows cite the owner's own page and are not GovTech docs. No embedding service was called and no weights were downloaded.",
               "T59: ruling id and process sentence removed (text given by the resolver)")
    V.sub("c", "OpenAI embeddings API", "Access terms",
          "openai.com/policies/terms-of-use and /service-terms returned HTTP 403 and were not read [Documented] (observed 2026-10-09). Whether those logs apply to embeddings calls [To be verified]",
          "The same page lists /v1/embeddings with abuse-monitoring retention of 30 days and Zero Data Retention eligibility Yes [Documented] (OAI data controls page, not GovTech docs). openai.com/policies/terms-of-use, /service-terms and /usage-policies returned HTTP 403 [Documented] (observed 2026-10-09). Whether OpenAI's usage policies or service terms restrict harmful or explicit input to the embeddings endpoint [To be verified] (the pages returned HTTP 403)",
          "T11, T59: the embeddings-endpoint question answered by the data-controls page; the remaining open part is the unreadable usage policies and terms")
    V.url_add("c", "OpenAI embeddings API", ["https://openai.com/policies/usage-policies"], "T11: the 403 fact names the usage-policies page")
    V.sub("c", "Google Gemini API", "Access terms",
          'Google docs say "For text-only use cases, gemini-embedding-001 remains available" and name a newer model gemini-embedding-2 [Documented] (GEM, not GovTech docs)',
          "Google's model page gives an input token limit of 2,048 and an output dimension of 128 to 3072 for gemini-embedding-001 [Documented] (Google model page, not GovTech docs)",
          "T14 (main P4 Q2): lifecycle sentence dropped; T34: input limit and dimension added")
    V.sub("c", "Google Gemini API", "Access terms",
          "Which tier applies to an embedding call and to the bench key [To be verified]",
          "The tier depends on whether the API is reached through a Cloud Project with an active billing account [Documented] (same page, not GovTech docs). Google's Generative AI Prohibited Use Policy says \"Do not engage in sexually explicit, violent, hateful, or harmful activities\" [Documented] (Google policy page, not GovTech docs). Whether gemini-embedding-001 has a free tier [Not disclosed] (terms and pricing pages checked)",
          "T12: tier rule and use policy added; free-tier status recorded as an absence")
    V.url_add("c", "Google Gemini API", ["https://policies.google.com/terms/generative-ai/use-policy", "https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001"],
              "T12, T34: policy and model pages")
    V.sub("c", "Gemma Terms of Use", "Access terms",
          "Section 3.1 sets conditions for Distribution of Gemma or Model Derivatives [Documented] (same page, not GovTech docs). Whether the LionGuard 2 Lite classifier counts as a Model Derivative [Not disclosed] (Lite README, LICENSE and PB checked; not discussed)",
          "Section 3.1 sets conditions for Distribution of Gemma or Model Derivatives, and section 1.1(e) defines Model Derivatives [Documented] (same page, not GovTech docs). The Prohibited Use Policy page is at ai.google.dev/gemma/prohibited_use_policy [Documented] (Google page, not GovTech docs). Whether the LionGuard 2 Lite classifier counts as a Model Derivative, and whether embedding harmful test text is a restricted use [Not disclosed] (Lite README, LICENSE and PB checked; not discussed)",
          "T10: Model Derivative definition and Prohibited Use Policy page added")
    V.url_add("c", "Gemma Terms of Use", ["https://ai.google.dev/gemma/prohibited_use_policy"], "T10")
    V.append("c", "BAAI/bge-large-en-v1.5", "Access terms",
             "The page lists dimension 1024 and sequence length 512 [Documented] (BAAI page, not GovTech docs)", "T52")
    V.sub("c", "trust_remote_code=True", "Access terms",
          "Pinning a revision for the bench is advisable [Inferred]", "A bench could pin a revision [Inferred]",
          "T43, R032 rewording: proposal, not advice")
    V.sub("c", "GovTech repo licence", "Access terms",
          "The two sources are not reconciled in any GovTech page read [Not disclosed] (LICENSE, cards, PB, B1 to B3 checked). This is a licensing item for the user and no conclusion on permitted use is drawn here",
          "The LICENSE excludes any asset or code identified by GovTech as not licensed to you [Documented: repo govtech/lionguard-2@be4e38c9] (LICENSE). How the LICENSE, the card metadata and the paper's research-only statement relate [Not disclosed] (LICENSE, cards, PB, B1 to B3, the paper's contributions, ethics and conclusion, and the Hugging Face collection page checked; not stated)",
          "T6, T59: process sentence removed; exclusion added")

    # ------------------------------------------------------------------ (d)
    V.para_sub(", and the org's Hugging Face listing holds 7 models, 10 datasets and 5 Spaces [Not disclosed] (those checks; training code not published where found).",
               " [Not disclosed] (those checks). The org's Hugging Face listing holds 7 models (the four LionGuard repos here plus two off-topic classifiers and a SEA-LION chat model), 10 datasets (three LionGuard-related datasets here; the others are unrelated) and 5 Spaces (one LionGuard demo here) [Documented] (Hub listing, read 2026-10-09).",
               "T20: the Hub listing is a Documented fact, not a Not disclosed one; the absence claim keeps its own label")
    V.append("d", "govtech/RabakBench:", "Licence or access",
             'Intended uses on the card: "Benchmark moderation APIs / guardrails" and "Research on code-mixing toxicity detection"; out-of-scope use: "Fine-tuning models to generate unsafe content" [Documented: repo govtech/RabakBench@3c02a5b8] (card)',
             "T8")
    V.sub("d", "govtech/RabakBench-full:", "Licence or access",
          "(file list and Hub metadata checked)", "(file list and Hub metadata checked; HTTP 404 for LICENSE, Hub cardData empty; observed 2026-10-09)",
          "T8")
    V.sub("d", "govtech/lionguard-demo:", "Licence or access", "Live status [To be verified]",
          "Live status: the Hub API reports runtime stage RUNNING [Documented] (HFAPI, read 2026-10-09). Reference only; no text was submitted to the hosted Space",
          "T54, T5 (main P4 ruling: demo Space is reference only)")
    V.sub("d", "Playbook page tools/lionguard", "Revision or date",
          "Staging branch commit 45908b48 (main is at 97338569, git ls-remote 2026-10-09) [Documented: repo govtech-responsibleai/playbook@45908b48]",
          "Commit 45908b48 on staging, the branch the site is built from (workflow pages-staging.yml); the page file is identical at main 97338569 (md5 compared 2026-10-09) [Documented: repo govtech-responsibleai/playbook@45908b48]",
          "T16")
    V.row_insert("d", "arXiv 2507.15339 LionGuard 2:",
        "| arXiv 2507.05980 Lost in Localization: Building RabakBench with Human-in-the-Loop Validation to Measure Multilingual Safety Gaps [Documented] (arXiv abstract page). Authors Gabriel Chua, Leanne Tan, Ziyu Ge, Roy Ka-Wei Lee [Documented] (arXiv abstract page) | Paper (vendor-authored; RabakBench) | GovTech authors, with two co-authors also listing SUTD | Submitted 8 Jul 2025 (v1), last revised 2 Feb 2026 (v2) [Documented] (arXiv abs) | Open on arXiv [Documented] (HTTP 200 observed 2026-10-09) | — (inventory only, not in Table 3) | https://arxiv.org/abs/2507.05980 ; https://arxiv.org/html/2507.05980 |",
        "T15 (main P4 Q1, P5 Q-A): GovTech-authored paper added as the 11th row of block (d); block count 10 to 11")

    # ------------------------------------------------------------------ (e)
    V.sub("e", "Hosted API behaviour", "What stays", "(GS; Sentinel docs, hosted API)", "(GS; Sentinel docs, hosted API, read 2026-10-09)", "T17")
    V.sub("e", "Variant table", "What stays", "(G; Sentinel docs, hosted API)", "(G; Sentinel docs, hosted API, read 2026-10-09)", "T17")
    V.sub("e", "Access and integration paths", "What stays", "(G LionGuard Versions; Sentinel docs, hosted API)",
          "(G LionGuard Versions; Sentinel docs, hosted API, read 2026-10-09)", "T17")
    V.append("e", "Access and integration paths", "What this sheet adds",
             "Google and EmbeddingGemma pages give 2,048 [Documented] (Google pages, not GovTech docs)", "T34")
