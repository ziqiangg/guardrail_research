"""Column edits for presidio (PD1-PD6). Imported by merge_presidio.py. Reason codes: Tn = triage id (resolution in
presidio_resolutions_1.md), 'style n' = triage Style issues in columns, 'hygiene' = triage Label hygiene, 'main Qn' =
main's rulings in queue.md (Resolved questions, rows starting 'presidio')."""

RP = "**[Documented: repo data-privacy-stack/presidio@2.2.364]**"
RR = "**[Documented: repo data-privacy-stack/presidio-research@0.3.2]**"
D = "**[Documented]**"
I = "**[Inferred]**"
ND = "**[Not disclosed]**"
BLOB = "https://github.com/data-privacy-stack/presidio/blob/2.2.364/"
RBLOB = "https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/"
DOCS = "https://presidio.dataprivacystack.org/"


def apply(C):
    # ===================================================================== PD1
    # ---- R2
    C.summary("PD1", 2, "Summary: **PII entity types, English by default.** The supported-entities page groups its types into Global, 18 country sections and a medical section. A default English setup loads pattern recognizers plus a spaCy name and place model. Detection is not guaranteed complete. " + D,
              "T20, T58: drop the own count and the unsupported '16 pattern recognizers' from the Summary (40 words)")
    C.repl("PD1", 2, "The page groups types into Global, 18 country sections", [
        "• The page groups types into Global, 18 country sections (USA, UK, Spain, Italy, Poland, Singapore, Australia, India, Finland, Korea, Nigeria, Philippines, Canada, Sweden, South Africa, Thai, Turkey, Germany) and Medical / Clinical " + D,
        "• 80 distinct entity ids appear in the page tables on 2026-10-09; `docs/supported_entities.md@2.2.364` has 81, the extra id being `PH_UMID` (premise: counted by parsing both pages) " + I],
        "T20: one bullet split; the own count becomes [Inferred] with its premise (was [Documented])")
    C.repl("PD1", 2, "Disabled entries include UK driving licence", [
        "• Disabled entries include UK driving licence, NINO, passport, postcode and vehicle registration; US MBI and NPI; Singapore FIN (`SgFinRecognizer`, line 135); Australia (4); India (6); Korea (4) " + RP,
        "• Further disabled entries: Sweden (2); Germany (13); Turkey (2); Thai, South Africa, Nigeria (2), Philippines (2) and Canada SIN identifiers; Spanish passport; `HuggingFaceNerRecognizer`; `BasicLangExtractRecognizer` " + RP],
        "style 10: bullet over 420 characters split in two")
    C.sub("PD1", 2, "Source conflict C2: the entity page lists", "Source conflict C2: the entity page lists",
          "The entity page lists", "T19, style 3: internal tag 'C2' removed", kind="style")
    C.sub("PD1", 2, "Source conflict C2: `default_recognizers.yaml`", "Source conflict C2: `default_recognizers.yaml`",
          "`default_recognizers.yaml`", "T19, style 3: internal tag 'C2' removed", kind="style")
    C.sub("PD1", 2, "Prompt-injection, harmful-content and topic checks are out of purpose",
          "list no such entity or check " + I, "list no such entity or check (premise: the Home page module list) " + I,
          "T57 (R015): premise named")
    # ---- R3
    C.ins_after("PD1", 3, "Presidio's OpenAI sample says the toolkit", [
        "• The sample is listed in the samples index as a Deployment sample (`docs/samples/index.md@2.2.364:39`) though the sample page is not in the `mkdocs.yml` navigation at the tag " + RP,
        "• Maintenance status of that sample (checked the sample page, the samples index and the navigation; not stated) " + ND],
        "T69")
    C.sub("PD1", 3, "Automatic language detection is not described",
          "(checked the analyzer and languages pages and `app.py`; the caller supplies `language`)",
          "(checked the analyzer and languages pages, `docs/` at the tag, the dependency list and `app.py`; the caller supplies `language`)",
          "T56: checked list extended")
    # ---- R4
    C.repl("PD1", 4, "Source conflict C4: the analyzer page", [
        "• The analyzer page shows `docker run -p 5002:3000 presidio-analyzer`, a locally built image name (Presidio docs, analyzer page) " + D,
        "• The installation page shows the registry name `ghcr.io/data-privacy-stack/presidio-analyzer` and, for a local build, `presidio/presidio-anonymizer` on port 5001:5001 (Presidio docs, installation page) " + D],
        "T16, style 3: 'Source conflict C4' lead-in replaced by two plain bullets")
    C.repl("PD1", 4, "Whether 2.2.364 is the latest GitHub release was not re-confirmed", [
        "• 2.2.364 is the highest version tag of the repository (`git ls-remote --tags`, 2026-10-09) " + RP,
        "• `CHANGELOG.md@2.2.364` has no 2.2.364 section: its top section is the one headed unreleased (line 5), above 2.2.363 dated 2026-06-28 (line 55) " + RP],
        "T9 (main Q1: CHANGELOG at the tag is the substitute for the unread release body); removes the [To be verified] bullet and the proxy wording")
    C.sub("PD1", 4, "The tagged code contains NoOpNlpEngine", "above 2.2.363 " + RP,
          "above 2.2.363 (the file has no 2.2.364 section) " + RP, "T9")
    C.ins_after("PD1", 4, "The tagged code contains NoOpNlpEngine", [
        "• `CHANGELOG.md@2.2.364:74` lists `score_thresholds` for registry YAML entries under 2.2.363 dated 2026-06-28, and line 10 lists the same feature under its unreleased heading " + RP,
        "• The unreleased heading looks stale: the tag and `main` both lack a 2.2.364 section while the tagged code contains these items (premise: `CHANGELOG.md@2.2.364` lines 5 and 55) " + I],
        "T13")
    C.sub("PD1", 4, "also lists `* 3.14` (source conflict C3", "Python: `docs/installation.md@2.2.364:24` also lists `* 3.14` (source conflict C3 with the live page)",
          "Python: `docs/installation.md@2.2.364:24` also lists `* 3.14`, beyond the 3.10 to 3.13 on the live page",
          "T15, style 3: internal tag 'C3' removed", kind="style")
    C.ins_after("PD1", 4, "Ownership: \"The Presidio project is in the process", [
        "• FAQ: \"It was originally created at Microsoft and has since transitioned to an independent, vendor-neutral project maintained by contributors and volunteers from across the community.\" (Presidio docs, FAQ) " + D],
        "T1: second ownership source (tense differs from the transition page; both kept, README section 3 rule 4)")
    C.ins_after("PD1", 4, "Docs host: `https://data-privacy-stack.github.io", [
        "• The docs site is published from the gh-pages branch of the repository by a manually started workflow (`.github/workflows/release-docs.yml@2.2.364`, trigger `workflow_dispatch`); the branch's last commit is dated 2026-07-04 " + RP,
        "• The live docs therefore predate the 2.2.364 tag, which is a likely reason they differ from `docs/` at the tag (premise: gh-pages head 2026-07-04, tag 2026-07-22) " + I],
        "T14")
    # ---- R5
    C.summary("PD1", 5, "Summary: **Spans and scores, no verdict.** Each hit has an entity type, start, end and a 0 to 1 score, plus an optional explanation. The default score threshold is 0. A vendor notebook reports F2 0.661 for default recognizers at threshold 0.4 on synthetic data. " + D,
              "T24, R014: figure keeps its setup qualifier (was 'default settings'; the notebook ran at threshold 0.4) (44 words)")
    C.ins_after("PD1", 5, "Example values only: `default_score_threshold: 0.4`", [
        "• Example value only: `\"score_threshold\": 0.6` in the ad-hoc recognizer request (`docs/tutorial/09_ad_hoc.md@2.2.364:66`) " + RP],
        "T22")
    C.ins_after("PD1", 5, "A German-language recipe advises", [
        "• The recipe also says \"setting `score_threshold=0.5` when no context is present is recommended\" for identifiers without a checksum (`docs/recipes/german-language-support/README.md@2.2.364:118`) " + RP,
        "• The recipe page is served on the live site although the site navigation does not list it (Presidio docs, German language support recipe) " + D],
        "T22, T68")
    C.sub("PD1", 5, "A recommended score threshold for the default English recognizers",
          "tutorial pages; only the examples above)", "tutorial pages and the recipes; only the examples above)",
          "T22: checked list extended")
    C.ins_after("PD1", 5, "Only vendor figures found are in presidio-research notebook 4", [
        "• Notebook 4's printed result is already present in presidio-research commit 2e97411 dated 2026-06-30, which is before the 2.2.364 tag (2026-07-22) (premise: git history of the notebook; the Presidio version is not printed) " + I],
        "T24")
    C.ins_after("PD1", 5, "Notebook 5 (a tuned engine with a Hugging Face NER recognizer", [
        "• Notebook 5's printed result F2 0.91 first appears in commit f2285ca dated 2026-07-28 and names `experiment_20260723-102549.json`; earlier commits print F2 0.903 (premise: git history of the notebook) " + I],
        "T24")
    C.repl("PD1", 5, "Part of the gap is coverage", [
        "• Notebook 5 changes the NER model, the threshold (0.3 against 0.4) and adds recognizers for TITLE, years and AGE, so its gain over notebook 4 mixes several changes (`notebooks/5_Evaluate_Custom_Presidio_Analyzer.ipynb@0.3.2` cells 14 and 18; `docs/mapping_scenarios.md@0.3.2:312`) " + RR,
        "• Part of the gap is coverage: the notebook set labels `STREET_ADDRESS` (3071 tokens), `TITLE`, `AGE` and `ZIP_CODE`, which have no default entity type; the mapping step (`CanonicalMapper`, notebook cell \"Review entity mapping\") was read but its outcome was not checked, so some labels may be folded into others; this is a reading of the printed entity counts against the 19 default entities " + I],
        "T26: confounders added as a [Documented: repo] bullet; coverage reading kept as a separate [Inferred] bullet")
    # ---- R6
    C.ins_after("PD1", 6, "Models: \"When packaging the code into a Docker container", [
        "• \"To extend Presidio to detect PII in an additional language, these modules require modification:\" followed by the NLP engine and the recognizers (Presidio docs, languages page) " + D],
        "T59: supports the Summary clause on other languages")
    C.repl("PD1", 6, "Enabling those recognizers means text leaves", [
        "• Azure AI Language recognizer passes the text to the service: `self.ta_client.recognize_pii_entities([text], language=self.supported_language)` (`azure_ai_language.py@2.2.364:121-123`) " + RP,
        "• AHDS recognizer passes the text to the service: `DeidentificationContent(input_text=text, ...)` then `self.deid_client.deidentify_text(body)` (`ahds_recognizer.py@2.2.364:113-117`) " + RP,
        "• Language-model recognizers pass the text to LangExtract: `\"text_or_documents\": kwargs.pop(\"text\")` and a call to `lx.extract` with those parameters (`langextract_recognizer.py@2.2.364:161,172`), with an Azure OpenAI client class in `azure_openai_provider.py@2.2.364:33` " + RP,
        "• For these recognizers the text leaves the Presidio process for the configured Azure endpoint (premise: the clients are built from the endpoint parameters; the transfer itself happens inside the Azure, langextract and openai packages, which were not read) " + I],
        "T8: the code calls are [Documented: repo]; the conclusion stays [Inferred]")
    C.repl("PD1", 6, "Decision-process logging writes a trace", [
        "• With `log_decision_process` on, the trace includes the NLP artifacts with the token texts and entity texts of the analysed string (`analyzer_engine.py@2.2.364:246-248`; `nlp_artifacts.py@2.2.364:81-84`) " + RP,
        "• The decision-process page says \"The decision process logs will be written to standard output.\" and its example trace line contains the sample text's name and digits (Presidio docs, decision process page) " + D,
        "• So PII from the analysed text reaches standard output when decision-process logging is on (premise: the two bullets above) " + I],
        "T55")
    C.repl("PD1", 6, "Docs versus code: the decision-process page says the correlation id", [
        "• The decision-process page says: \"The id can be retrieved from each API response header: x-correlation-id.\" (Presidio docs, decision process page) " + D,
        "• No code in `presidio-analyzer/app.py` or `presidio_analyzer/` at the tag sets a response header (searched for headers, after_request, add_header and make_response; `app.py@2.2.364:92` only passes the id into `analyze`) " + ND],
        "T54: [Inferred] from a one-file search replaced by a docs bullet plus an absence bullet naming the patterns searched")
    C.repl("PD1", 6, "TLS for the REST service (checked the FAQ", [
        "• TLS for the REST service (checked the FAQ, installation, analyzer, Kubernetes, App Service and Data Factory pages and the Helm chart files; not mentioned) " + ND,
        "• Rate limits for the REST service (checked the same pages; none stated) " + ND,
        "• The Kubernetes sample deploys an NGINX ingress controller by default (Presidio docs, Kubernetes page) " + D,
        "• The App Service sample shows a script that restricts network access to a given IP range (Presidio docs, App Service page) " + D],
        "T52")
    # ---- R8
    C.summary("PD1", 8, "Summary: **Key open questions.** No recommended threshold or latency figure, which listed entities are active in a default install, per-entity accuracy, and retention at the Azure Health Data Services endpoint.",
              "T7: replaces 'a thin default entity set' (no bullet states it) and the three-listed-entities / cloud data-flow clauses now answered (29 words)")
    C.repl("PD1", 8, "Per-entity accuracy of the default recognizers", "• Per-entity accuracy of the default recognizers (the notebooks show aggregate numbers and interactive plots; no per-entity figures were found)",
           "style 4: process wording 'not readable as text' removed", kind="style")
    C.repl("PD1", 8, "Which Presidio version produced the presidio-research notebook outputs",
           "• Which Presidio version produced the notebook outputs (notebook 4 predates the 2.2.364 tag; notebook 5 was run on or after 2026-07-23; neither prints a version; reproduction needs testing)",
           "T24")
    C.repl("PD1", 8, "What exactly leaves the network for Azure AI Language",
           "• Retention and region of data sent to the Azure Health Data Services endpoint (the Presidio AHDS page and the Microsoft overview page do not state them)",
           "T7, T8: what leaves the process is now documented from code (R6); the open part is AHDS retention and region")
    C.repl("PD1", 8, "Whether authentication, TLS or rate limiting is recommended",
           "• Whether TLS termination is expected at an ingress or gateway (the Kubernetes sample deploys an NGINX ingress; no page mentions TLS or rate limits)",
           "T52")
    C.repl("PD1", 8, "Whether 2.2.364 is the latest release and what its release notes say",
           "• What the GitHub release notes for 2.2.364 say (the release page was not read; CHANGELOG.md at the tag lists the changes under its unreleased heading)",
           "T9, style 4: proxy wording removed")
    C.delete("PD1", 8, "Owner question Q01", "T1 (R016): ownership ruled; process item removed")
    # ---- R9
    for u, why in [
        (BLOB + "presidio-analyzer/presidio_analyzer/predefined_recognizers/third_party/ahds_recognizer.py", "T8"),
        (BLOB + "presidio-analyzer/presidio_analyzer/predefined_recognizers/third_party/azure_openai_provider.py", "T8"),
        (BLOB + "presidio-analyzer/presidio_analyzer/predefined_recognizers/third_party/langextract_recognizer.py", "T8"),
        (BLOB + "presidio-analyzer/presidio_analyzer/nlp_engine/nlp_artifacts.py", "T55"),
        (BLOB + ".github/workflows/release-docs.yml", "T14"),
        (BLOB + "docs/supported_entities.md", "T20"),
        (BLOB + "docs/tutorial/09_ad_hoc.md", "T22"),
        (BLOB + "docs/samples/index.md", "T69"),
        (BLOB + "mkdocs.yml", "T69"),
        (DOCS + "recipes/german-language-support/", "T68"),
        (DOCS + "samples/deployments/k8s/", "T52"),
        (DOCS + "samples/deployments/app-service/", "T52"),
        (DOCS + "samples/deployments/data-factory/presidio-data-factory/", "T52"),
        (RBLOB + "docs/mapping_scenarios.md", "T26"),
        ("https://learn.microsoft.com/en-us/azure/healthcare-apis/deidentification/overview", "T7 (Microsoft docs, not Presidio docs)"),
    ]:
        C.add_url("PD1", u, why)

    C.sub("PD1", 4, "Version: `presidio_analyzer` is `version = \"2.2.364\"`", "(local clone log)", "(git log at the tag)",
          "style 4: process wording 'local clone' removed", kind="style")

    # ===================================================================== PD2
    C.ins_after("PD2", 1, "Built-in anonymize operators:", [
        "• The result is an `EngineResult` with `text` and `items`; each item is an `OperatorResult` with `start`, `end`, `entity_type`, `text` and `operator` (Presidio docs, anonymizer page, class diagram) " + D,
        "• The `anonymize` docstring example shows item positions in the new text: input \"My name is Bond, James Bond\" gives \"My name is BIP, BIP.\" with items at 16 to 19 and 11 to 14 (`anonymizer_engine.py@2.2.364:76-81`) " + RP],
        "T59: supports the Summary clause on positions in the new text")
    C.sub("PD2", 2, "Code: `Replace` has", "; the NeMo Guardrails PII columns list this default string as unverified in the Presidio docs", "",
          "T67: a code fact and a cross-reference to other columns were in one bullet; the NeMo note is recorded in this log only (NeMo sheets are frozen, R001)")
    C.ins_after("PD2", 2, "The enum has two members", [
        "• `_remove_conflicts_and_get_text_manipulation_data` runs its merge and containment passes for every strategy value and adds a third pass only when the strategy equals `REMOVE_INTERSECTIONS` (`anonymizer_engine.py@2.2.364:133-196`) " + RP,
        "• A no-resolution mode named NONE therefore does not exist in the tagged code (premise: the enum has two members and the passes above) " + I,
        "• The development branch main (head 2523c7b, dated 2026-10-08) carries a later fix to `REMOVE_INTERSECTIONS` handling (#2331) that is not in tag 2.2.364, so the tagged behaviour described here may differ on main **[Documented: develop/unreleased]**"],
        "T30; main Q3 (commit 2523c7b, label develop/unreleased). The labelled bullet sits in R2 because the checker and README section 4 forbid labels in R8 bullets")
    C.sub("PD2", 2, "Out of purpose: it does not judge harmful content", "and it sees no model or policy context " + I,
          "and it sees no model or policy context (premise: the Home page module list) " + I, "T57 (R015): premise named")
    C.summary_text("PD2", 4, "MIT licence, now under the Data Privacy Stack community.", "MIT licence, moving to the Data Privacy Stack community.",
                   "entailment (T1 contradiction 1: FAQ 'has since transitioned' versus transition page 'in the process of transitioning'): the R4 Detail says the project is moving, so the Summary says moving, as in PD1 and PD4")
    C.repl("PD2", 4, "Source conflict C4: the anonymizer page", [
        "• The anonymizer page shows `docker run -p 5001:3000 presidio-anonymizer`, a locally built name (Presidio docs, anonymizer page) " + D,
        "• The installation page uses the registry name `ghcr.io/data-privacy-stack/presidio-anonymizer` and, for a local build, `presidio/presidio-anonymizer` on port 5001:5001 (Presidio docs, installation page) " + D,
        "• \"The legacy Microsoft Container Registry images at mcr.microsoft.com/presidio-* are no longer updated.\" (Presidio docs, installation page) " + D],
        "T16, style 3: 'Source conflict C4' lead-in replaced by plain bullets; the registry-move quote is its own bullet")
    C.sub("PD2", 4, "also lists `* 3.14`, and `requires-python", "; source conflict C3 with the live page", "",
          "T15, style 3: internal tag 'C3' removed (not listed in the resolution; same defect as PD1/PD3)", kind="style")
    C.summary_text("PD2", 6, "with a DEFAULT entry", "with a default entry", "style 2: code identifier removed from a Summary", )
    C.ins_after("PD2", 6, "AHDS surrogate needs `pip install presidio-anonymizer[ahds]`", [
        "• The AHDS surrogate operator passes the text to the service: `DeidentificationContent(input_text=text, ...)` and `client.deidentify_text(content)` (`ahds_surrogate.py@2.2.364:270-277`) " + RP],
        "T8")
    C.summary("PD2", 8, "Summary: **Key open questions.** No accuracy or latency figures, REST support for the keep and Azure surrogate operators, the effect of space merging on adjacent names, offsets for non-BMP text, and what the Azure surrogate operator retains.",
              "T30: the NONE-strategy question is answered (36 words)")
    C.delete("PD2", 8, "Whether a no-conflict-resolution mode exists", "T30: answered from code")
    C.repl("PD2", 8, "What the AHDS surrogate operator sends to Azure",
           "• What the AHDS surrogate operator retains at Azure (the code passes the text to the AHDS client, see R6; retention is not stated on the Presidio or Microsoft overview pages)",
           "T7, T8")
    C.repl("PD2", 8, "Release notes for 2.2.364 could not be read",
           "• What the GitHub release notes for 2.2.364 say (the release page was not read; CHANGELOG.md at the tag lists the changes under its unreleased heading)",
           "T9, style 4")
    C.repl("PD2", 8, "Owner question Q01",
           "• Whether the post-tag fix to `REMOVE_INTERSECTIONS` handling on the development branch (main commit 2523c7b, #2331; develop/unreleased) changes overlap results compared with tag 2.2.364 (see R2; needs testing against the next release)",
           "main Q3: the Q01 process bullet (T1) is replaced by the open question on commit 2523c7b")
    C.add_url("PD2", "https://learn.microsoft.com/en-us/azure/healthcare-apis/deidentification/overview", "T7 (Microsoft docs, not Presidio docs)")
    C.add_url("PD2", "https://github.com/data-privacy-stack/presidio/commit/2523c7b", "main Q3")

    # ===================================================================== PD3
    C.summary("PD3", 1, "Summary: **Encrypts PII in text so it can be restored later.** The encrypt operator swaps each entity for AES ciphertext, and the Deanonymize engine or the decrypt operator reverses it with the same key. Presidio keeps no session state between calls. " + D,
              "T59: sentence now entailed by a same-row bullet (40 words)")
    C.ins_after("PD3", 1, "The DeanonymizerEngine is a class in Presidio", [
        "• \"Presidio does not store or maintain stateful sessions.\" (Presidio docs, anonymizer page) " + D],
        "T59")
    C.summary_text("PD3", 4, "**AES-CBC with a random IV per entity.** Encrypt returns URL-safe base64 of the IV plus ciphertext;",
                   "**AES-CBC with a random initialisation vector per entity.** Encrypt returns URL-safe base64 of that vector plus ciphertext;",
                   "style 2: abbreviation 'IV' removed from a Summary")
    C.summary_text("PD3", 4, "MIT licence, now under the Data Privacy Stack community.", "MIT licence, moving to the Data Privacy Stack community.",
                   "entailment (as PD2 R4): the R4 Detail says transition, so the Summary says moving")
    C.sub("PD3", 4, "The cipher code uses plain CBC", "(premise: `aes_cipher.py` has no integrity step)",
          "(premise: `aes_cipher.py@2.2.364:8-48` has padding, IV and CBC steps only)", "T35: premise now verified by a full read of the file")
    C.delete("PD3", 4, "Release-note wording for 2.2.364 could not be read", "T9: [To be verified] bullet with proxy wording removed; the CHANGELOG fact is in the bullet above")
    C.sub("PD3", 4, "also lists `* 3.14` (source conflict C3", " (source conflict C3 with the live page)", ", beyond the 3.10 to 3.13 on the live page",
          "T15, style 3: internal tag 'C3' removed", kind="style")
    C.repl("PD3", 4, "NeMo Guardrails columns E and F wrap Presidio",
           "• Restoring masked values is not described in NeMo Guardrails columns E and F or on the NVIDIA Presidio page (checked their text for restore, deanonymise, decrypt and reverse), so this column covers the reverse step " + ND,
           "T37: [Inferred] becomes [Not disclosed] naming what was checked")
    C.sub("PD3", 6, "Key generation, storage, rotation and access control",
          "(checked the anonymizer page, encrypt and decrypt tutorial and sample, and FAQ; the only secret-handling advice is for hash salt)",
          "(checked the anonymizer page, encrypt and decrypt tutorial and sample, the OpenAI sample page and FAQ; examples use a literal key in code; the only secret-handling advice is for hash salt)",
          "T35: checked list extended")
    C.sub("PD3", 8, "Whether authenticated encryption or a deterministic mode is planned",
          "(checked the changelog at the tag and the docs; nothing stated)",
          "(checked the changelog at the tag and the docs; nothing stated; the project issue tracker and roadmap were not read)",
          "T35: roadmap half stays open")
    C.repl("PD3", 8, "Whether the batch deanonymiser is part of the 2.2.364 release notes",
           "• Whether the batch deanonymiser is named in the 2.2.364 release notes (code is in the tag; the CHANGELOG lists it under its unreleased heading; the release page was not read)",
           "T9, style 4")
    C.delete("PD3", 8, "Whether the NeMo Guardrails PII flows", "T37: closed by the [Not disclosed] bullet in R4")
    C.delete("PD3", 8, "Owner question Q01", "T1 (R016): process item removed")
    C.add_url("PD3", "https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/third-party/presidio", "T37: the NVIDIA page named in the R4 bullet")

    # ===================================================================== PD4
    C.summary_text("PD4", 2, "Coverage depends on which recognizers are enabled. **[Documented]**",
                   "Coverage depends on which recognizers are enabled. **[Inferred]**", "T57 (R015): out-of-purpose statement is [Inferred] in every column (text unchanged, 45 words)")
    C.sub("PD4", 2, "Out of purpose: the home page lists the modules", "(Presidio docs, home page, read 2026-10-09) " + D,
          "(premise: Presidio docs, home page, read 2026-10-09) " + I, "T57 (R015)")
    C.ins_after("PD4", 4, "Document Intelligence OCR sends the image bytes", [
        "• Document Intelligence stores submitted input data and analyze results for 24 hours after an analysis completes (Microsoft docs, not Presidio docs) " + D],
        "T7")
    C.repl("PD4", 4, "Python versions conflict (three sources, none picked)", [
        "• Python: `requires-python = \">=3.10,<3.15\"` and classifiers 3.10 to 3.14 (`presidio-image-redactor/pyproject.toml@2.2.364:14-18,23`) " + RP,
        "• Python: `docs/installation.md@2.2.364:24` also lists `* 3.14` " + RP],
        "T15: narrative lead-in dropped, one fact per bullet; installation.md bullet added for parity with PD1 to PD3")
    C.repl("PD4", 4, "The Dockerfile sets `ANALYZER_CONF_FILE`", [
        "• The Dockerfile declares `ANALYZER_CONF_FILE`, `NLP_CONF_FILE` and `RECOGNIZER_REGISTRY_CONF_FILE` as build arguments, environment variables and copied files (`presidio-image-redactor/Dockerfile@2.2.364:3-5,10-12,17-19`) " + RP,
        "• No Python file in `presidio-image-redactor/` references those names (grep of the folder at the tag); in the Analyzer package only the REST app reads them (`presidio-analyzer/app.py@2.2.364:46-49`) " + ND,
        "• `app.py` builds `ImageRedactorEngine()` with defaults (`presidio-image-redactor/app.py@2.2.364:39`), so the analyzer configuration of the image service is probably not changeable by those files (premise: the two bullets above) " + I],
        "T41: premise now verified; three bullets")
    C.ins_after("PD4", 4, "The OpenAPI file at the tag lists `/analyze`", [
        "• The live API page loads `api-docs.yml`, which is identical to the file at the tag, so the live spec also has no `/redact` path (Presidio docs, API reference page) " + D],
        "T42")
    C.summary("PD4", 5, "Summary: **No verdict; an image comes back.** Python returns the redacted image and, optionally, one box per redacted word with entity type, offsets, score and position. REST returns only the image. The score threshold is 0 in Python and 0.4 on the REST upload form. " + D,
              "T58: absence sentence (which rested on [Not disclosed] bullets) replaced by threshold facts entailed by the REST and Python bullets (44 words)")
    C.sub("PD4", 7, "presidio-research (R010):", "presidio-research (R010): ", "presidio-research: ", "style: internal ruling id removed from deliverable text", kind="style")
    C.repl("PD4", 7, "Its README, version and any image or OCR feature were not read",
           "• presidio-research has no image, OCR or DICOM evaluation mode (checked README.md, docs/, presidio_evaluator/ and pyproject.toml at the tag; its models are the Analyzer and single-recognizer wrappers, and its dataset format is text with character spans) " + ND,
           "T12: [To be verified] with proxy wording replaced by an absence claim naming the paths checked")
    C.delete("PD4", 8, "Why the REST API spec at the tag has no /redact path", "T42: answered (live spec identical to the tag; no /redact path in either)")
    C.repl("PD4", 8, "What leaves the network when Document Intelligence is used",
           "• Whether other Azure data terms apply when Document Intelligence is used beyond the 24-hour retention (Microsoft docs, not Presidio docs, were read for retention only)", "T7")
    C.repl("PD4", 8, "Release-note wording for 2.2.364 was not re-read",
           "• What the GitHub release notes for 2.2.364 say (the release page was not read; CHANGELOG.md at the tag lists the changes under its unreleased heading)", "T9, style 4")
    for u, why in [
        (RBLOB + "README.md", "T12"),
        (BLOB + "presidio-analyzer/app.py", "T41"),
        (DOCS + "api-docs/api-docs.yml", "T42"),
        (BLOB + "docs/installation.md", "T15"),
        ("https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/document-intelligence/data-privacy-security", "T7 (Microsoft docs, not Presidio docs)"),
    ]:
        C.add_url("PD4", u, why)

    # ===================================================================== PD5
    C.summary_text("PD5", 2, "topic checks are out of purpose. **[Documented]**", "topic checks are out of purpose. **[Inferred]**",
                   "T57 (R015): out-of-purpose statement is [Inferred] in every column (text unchanged, 41 words)")
    C.sub("PD5", 2, "Out of purpose: the home page lists the modules", "(Presidio docs, home page, read 2026-10-09) " + D,
          "(premise: Presidio docs, home page, read 2026-10-09) " + I, "T57 (R015)")
    C.summary_text("PD5", 3, "Takes a pandas DataFrame or a JSON-like dict or list", "Takes a pandas table or a JSON-like dict or list",
                   "style 2: class name 'DataFrame' removed from a Summary")
    C.repl("PD5", 3, "Scope note for CP1", "• Used on retrieved records or tool output it is on the AI data path; used to de-identify bulk database exports unrelated to an AI conversation it falls outside the scope guide, and the docs describe the second use more than the first " + I,
           "T3 (R016): 'Scope note for CP1' wording removed; PD5 stays a column")
    C.summary("PD5", 4, "Summary: **Two steps over the Analyzer and Anonymizer.** A builder samples and analyses values to map each column or key to one entity type, then the engine applies Anonymizer operators to every value there. Package version 0.0.8, marked alpha, under the MIT licence. " + D,
              "T44 (optional in the resolution, applied): the package is marked alpha on the getting-started page (42 words)")
    C.ins_after("PD5", 4, "Concepts page says \"The StructuredEngine is a class", [
        "• The same sentence is in `docs/learn_presidio/concepts.md@2.2.364:32` " + RP],
        "T46")
    C.repl("PD5", 4, "Current maturity label for presidio-structured is not stated",
           "• The getting-started page says: \"Alpha: This package is currently in alpha, meaning it is in its early stages of development. Features and functionality may change as the project evolves.\" (Presidio docs, getting started with structured data page) " + D,
           "T44 CORRECTION: the draft said the label is not stated; the getting-started page states alpha")
    C.repl("PD5", 4, "Python versions conflict (three sources, none picked)", [
        "• Python: `requires-python = \">=3.10,<3.15\"` and classifiers 3.10 to 3.14 (`presidio-structured/pyproject.toml@2.2.364:14-18,23`) " + RP,
        "• Python: `docs/installation.md@2.2.364:24` also lists `* 3.14` " + RP],
        "T15")
    C.summary("PD5", 5, "Summary: **A transformed table or object plus a column map.** Output is the anonymised table or dict; the analysis step returns a column-to-entity map with no per-cell findings or scores. The detection threshold defaults to 0 and the mixed-strategy cut-off to 0.5. " + D,
              "T58, style 2: absence sentence (resting on [Not disclosed] bullets) replaced by two default values; 'DataFrame' removed (41 words)")
    C.ins_after("PD5", 5, "Score threshold for detection: the builders accept", [
        "• `mixed_strategy_threshold` defaults to 0.5 (`analysis_builder.py@2.2.364:176`) " + RP],
        "T58: supports the new Summary sentence")
    C.summary_text("PD5", 6, "Needs a DataFrame or dict", "Needs a table or dict", "style 2: class name 'DataFrame' removed from a Summary")
    C.summary_text("PD5", 7, "on a small DataFrame and a JSON object", "on a small table and a JSON object", "style 2: class name 'DataFrame' removed from a Summary")
    C.sub("PD5", 7, "presidio-research (R010):", "presidio-research (R010): ", "presidio-research: ", "style: internal ruling id removed from deliverable text", kind="style")
    C.repl("PD5", 7, "Whether presidio-research has any table or JSON mode was not checked",
           "• presidio-research has no table or JSON-document mode (checked README.md, docs/, presidio_evaluator/ and pyproject.toml at the tag; its dataset format is text with character spans) " + ND,
           "T12")
    C.summary("PD5", 8, "Summary: **Key open questions.** The default replace output, behaviour on non-text cells and odd column names, in-place mutation, majority-vote mapping errors, and throughput on large tables.",
              "T3 (R016): drops the CP1 clause; T44: drops 'maturity' (answered) (25 words)")
    C.delete("PD5", 8, "Column or inventory only: no docs page links", "T3 (R016): decision taken, PD5 stays a column")
    C.repl("PD5", 8, "Maturity label and roadmap: alpha in 2024",
           "• Roadmap for presidio-structured: PySpark and k-anonymity are listed as future work (checked the structured page, README and changelog; no dates stated)", "T44")
    C.repl("PD5", 8, "Release-note wording for 2.2.364 was not re-read",
           "• What the GitHub release notes for 2.2.364 say (the release page was not read; CHANGELOG.md at the tag lists the changes under its unreleased heading)", "T9, style 4")
    for u, why in [
        (DOCS + "getting_started/getting_started_structured/", "T44"),
        (BLOB + "docs/learn_presidio/concepts.md", "T46"),
        (BLOB + "docs/installation.md", "T15"),
        (RBLOB + "README.md", "T12"),
    ]:
        C.add_url("PD5", u, why)

    # ===================================================================== PD6
    C.sub("PD6", 2, "Out of purpose: the home page lists Presidio's modules", "(Presidio docs, home page, read 2026-10-09) " + D,
          "(premise: Presidio docs, home page, read 2026-10-09) " + I, "T57 (R015): was [Documented]")
    C.sub("PD6", 4, "The code at the tag implements it", "while `CHANGELOG.md` lists it under `[unreleased]` (CHANGELOG.md@2.2.364:10)",
          "while `CHANGELOG.md` lists it under its unreleased heading (CHANGELOG.md@2.2.364:10)", "T13: no bracketed non-label in deliverable text", kind="hygiene")
    C.ins_after("PD6", 4, "The code at the tag implements it", [
        "• `CHANGELOG.md@2.2.364:74` also lists `score_thresholds` for registry YAML entries under 2.2.363 dated 2026-06-28 " + RP],
        "T13")
    C.summary("PD6", 5, "Summary: **Spans with the score you set.** A custom recognizer returns the usual Analyzer result: entity type, start, end and score. With the decision process on, the explanation names the pattern, regex, original score and context boost. The engine threshold defaults to 0. " + D,
              "T58: absence sentence replaced by the default threshold (entailed by the engine-threshold bullet) (42 words)")
    C.sub("PD6", 7, "presidio-research (R010):", "presidio-research (R010): ", "presidio-research: ", "style: internal ruling id removed from deliverable text", kind="style")
    C.repl("PD6", 7, "Its README, release tag and data format were not read", [
        "• presidio-research can wrap one recognizer: \"Class wrapper for one specific PII recognizer\" (`presidio_evaluator/models/presidio_recognizer_wrapper.py@0.3.2`) " + RR,
        "• Its datasets are text samples with character spans (`InputSample` with `full_text` and `spans`, `data_objects.py@0.3.2:207-211`) " + RR],
        "T12: [To be verified] with proxy wording replaced by two documented bullets")
    C.summary("PD6", 8, "Summary: **Key open questions.** REST error codes for a bad regex or language, server-side regex safety under concurrent requests, how request and recognizer thresholds combine in batch calls, and score choices for weak patterns.",
              "T13, T47: drops non-pattern logic over REST and per-recognizer threshold status (both answered) (33 words)")
    C.delete("PD6", 8, "Whether non-pattern recognizers can be sent per request over REST", "T47: answered by the R4 bullet on PatternRecognizer.from_dict")
    C.delete("PD6", 8, "Whether per-recognizer `score_thresholds` is in the released 2.2.364 package", "T13: answered (tagged code, tagged docs and the 2.2.363 changelog section state it). The generic release-notes bullet T9 asks for here is not repeated: it is already in PD1, PD2, PD4 and PD5 R8")
    for u, why in [
        (RBLOB + "README.md", "T12"),
        (RBLOB + "presidio_evaluator/models/presidio_recognizer_wrapper.py", "T12"),
        (RBLOB + "presidio_evaluator/data_objects.py", "T12"),
    ]:
        C.add_url("PD6", u, why)
