# Presidio resolutions 1 (P5): class (a) and (c) items, T1 to T70

Resolver: gr-resolver. Date: 2026-10-09 (20261009). Inputs read: CLAUDE.md, drafts/README.md, presidio_triage.md, presidio_cols_a.md (A), presidio_cols_b.md (B), presidio_inventory.md (INV), rulings R010 to R019, scratchpad/main/{seeds,queue}.md, explorer P0 note.

Items handled (47): T1 to T16, T19 to T22, T24, T26, T30, T35, T37, T38, T41, T42, T44, T46, T47, T52, T54 to T61, T63, T65 to T70. T1 to T5 are settled by R016 (T5 by R010, see its entry). Not handled here (class b, needs testing, or honest gap; they stay open): T17, T18, T23, T25, T27, T28, T29, T31, T32, T33, T34, T36, T39, T40, T43, T45, T48, T49, T50, T51, T53, T62, T64.

## Method and access notes

- Code and repo docs: shallow clones under the session scratchpad (R013 form): `data-privacy-stack/presidio` at tag 2.2.364 (commit 779dbd286d5ef4d1fbe2514275fb1bce358f2417, committed 2026-07-22, `git describe` 2.2.364), `data-privacy-stack/presidio-research` at tag 0.3.2 (06d2030688ece62f58047e567aecd70e4bb5f104, 2026-08-04; then un-shallowed for notebook history), the `main` heads of both repos (presidio main HEAD 2523c7b, 2026-10-08; presidio-research HEAD 0cb36502, 2026-09-30), branch `gh-pages` (HEAD e1987e57, 2026-07-04) and branch `V1`. All line numbers below are from those checkouts.
- Docs site: read as raw text with `python benchtest/tools/fetch_text.py` (final host presidio.dataprivacystack.org, HTTP 200, 2026-10-09); pages are saved in `benchtest/scratchpad/resolver/pages/`. WebFetch was not used for any quote or number.
- Tags: `git ls-remote --tags` on both repos (R015). The highest version tag of data-privacy-stack/presidio is 2.2.364 (56 tags in total); of presidio-research it is 0.3.2.
- Not readable: GitHub release pages (github.com answers HTTP 403 through the session proxy) and the GitHub MCP (`get_release_by_tag` answered: repository "not configured for this session"). The release body of 2.2.364 therefore stays unread; see T9. Not worked around.
- github.com blob pages also answer 403; `raw.githubusercontent.com` answers 200 for the same tagged files (used only to test URL reachability in T70; no content was taken from it that is not also in the clone).
- Out-of-list sources, all read-only GETs and marked "not Presidio docs" in the draft text: Microsoft Learn pages (Azure Language, Azure OpenAI, Document Intelligence, Azure Health Data Services; T7), Hugging Face model cards and the owners' GitHub licence files and the explosion/spacy-models meta file (T6). They are cited under R019 (component licences, vendor terms pages).
- Nothing was installed, run, pulled or called (R019). The un-shallow fetch of presidio-research is a git fetch, not an API call.
- Word counts for every proposed Summary were computed with the checker's rule (trailing bold label excluded; limit 45, R7 60). All proposed Summaries are at or below the limit, contain no backticks, underscores or `$`, and have balanced `**`.

---

### T1 — Ownership, official-source status and the frozen prefix `Presidio:`
- Verdict: RESOLVED
- Evidence: Ruling R016 item 1 (user, 2026-10-09): "Official sources: data-privacy-stack docs, GitHub org and GHCR, plus Microsoft-authored pages (transition page, microsoft.github.io stub). Header prefix `Presidio:` is frozen." Supporting facts re-read: transition page https://presidio.dataprivacystack.org/project_transition/ "The Presidio project is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project under the new GitHub organization Data Privacy Stack."; FAQ https://presidio.dataprivacystack.org/faq/ "It was originally created at Microsoft and has since transitioned to an independent, vendor-neutral project maintained by contributors and volunteers from across the community."; stub https://microsoft.github.io/presidio/ (HTTP 200, body "This page has moved. Redirecting you to https://data-privacy-stack.github.io/presidio/"); `curl -I https://data-privacy-stack.github.io/presidio/` returns HTTP 301 with `location: https://presidio.dataprivacystack.org/` (observed 2026-10-09); `git ls-remote https://github.com/microsoft/presidio` returns the same refs and HEAD (2523c7b) as `data-privacy-stack/presidio` (observed 2026-10-09; the 301 header itself is not visible through the proxy); `CHANGELOG.md@2.2.364:45` "Updated the `LICENSE` file copyright from "Microsoft Corporation" to "Presidio Contributors" (#2134)".
- Label to use: none new. Existing ownership bullets keep `[Documented]` (docs) and `[Documented: repo data-privacy-stack/presidio@2.2.364]` (LICENSE, CHANGELOG).
- Draft impact:
  - A, PD1 R8 (A:171), PD2 R8 (A:360), PD3 R8 (A:504): delete the three "Owner question Q01 ..." bullets (process items; PD4 to PD6 R8 have none). No R8 Summary mentions Q01, so no Summary change.
  - INV, scope paragraph (line 3): replace "both owners are recorded and the choice of official source is open for CP1." with "both owners are recorded; the sources used are the Data Privacy Stack docs host, GitHub organisation and container registry, plus the Microsoft-authored transition page and docs stub."
  - A, PD1 R4: add after A:88 one bullet: `• FAQ: "It was originally created at Microsoft and has since transitioned to an independent, vendor-neutral project maintained by contributors and volunteers from across the community." (Presidio docs, FAQ) **[Documented]**` and keep the transition-page bullet (A:88) as the conflicting-tense pair (README rule 4; note that FAQ says "has since transitioned" and the transition page "in the process of transitioning").
  - Header prefix: no change. Main: CLAUDE.md Products row and seeds.md presidio entry to read "Presidio (data-privacy-stack; formerly Microsoft)" per R016 item 1.
  - R4 Summaries ("MIT licence; ... moving to a community organisation"): no change.

### T2 — Column split (six columns or four)
- Verdict: RESOLVED
- Evidence: R016 item 2 (user): "Six columns PD1–PD6 as drafted (no fold of PD3→PD2 or PD6→PD1; PD5 presidio-structured stays a column)."
- Label to use: not applicable (decision).
- Draft impact: none to PD1 to PD3 or PD6 bullets or Summaries. Drop A RN-10(1) and A RN-11 from the final (Reviewer notes are removed at merge anyway).

### T3 — PD5 presidio-structured: column or inventory only
- Verdict: RESOLVED
- Evidence: R016 item 2 (user): "PD5 presidio-structured stays a column." Facts that matter for the wording after the decision are in T44 (alpha status) and T12 (presidio-research has no table or JSON mode).
- Label to use: not applicable (decision).
- Draft impact:
  - B, PD5 R8 first bullet (B:295) "Column or inventory only: ... the decision belongs to CP1": delete.
  - B, PD5 R8 Summary: replace (new text, 25 words): `Summary: **Key open questions.** The default replace output, behaviour on non-text cells and odd column names, in-place mutation, majority-vote mapping errors, and throughput on large tables.` (also drops "maturity", answered in T44).
  - B, PD5 R3 last bullet (B:225): replace with `• Used on retrieved records or tool output it is on the AI data path; used to de-identify bulk database exports unrelated to an AI conversation it falls outside the scope guide, and the docs describe the second use more than the first **[Inferred]**` (drops "Scope note for CP1").
  - B, PD5 R3 Summary is already `[Inferred]` and states the data-path fit; keep.
  - B RN-10 is not carried into the final.

### T4 — Inventory granularity
- Verdict: RESOLVED
- Evidence: R016 item 3 (user): "Inventory at recognizer-family level (31 rows), not per-entity."
- Label to use: not applicable (decision).
- Draft impact: none. Block row counts stay 14 / 31 / 10 / 14 for the P8 config (T6 below adds licence facts to existing cells, not rows). Count correction for the brief: the entity catalogue has 80 distinct ids on the live page (T20), not about 120.

### T5 — presidio-research stays an inventory row
- Verdict: RESOLVED
- Evidence: R010 (inventory row, not an evaluation-tooling sheet) still applies; R016 does not reopen it. At tag 0.3.2 (https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/README.md) the models folder holds only `presidio_analyzer_wrapper.py` and `presidio_recognizer_wrapper.py` plus `base_model.py`; no image, OCR, table, JSON or Anonymizer evaluator exists (grep for ocr, dicom, image_redactor and presidio_structured in `presidio_evaluator/`, `pyproject.toml`, `README.md` and `docs/`: nothing relevant). See T12.
- Label to use: `[Documented: repo data-privacy-stack/presidio-research@0.3.2]` for the contents; the conclusion "no sheet-level evidence" is a judgement `[Inferred]` (premise: the folder listing above).
- Draft impact: none to Table 3 columns or sheet structure. INV (a) row 23 keeps marker `— (inventory only, not in Table 3)`.

### T6 — Licences of third-party components
- Verdict: RESOLVED
- Evidence (all read 2026-10-09, owner pages, not Presidio docs):
  - spaCy library: https://raw.githubusercontent.com/explosion/spaCy/master/LICENSE "The MIT License (MIT) Copyright (C) 2016-2024 ExplosionAI GmbH".
  - spaCy model en_core_web_lg 3.8.0: https://raw.githubusercontent.com/explosion/spacy-models/master/meta/en_core_web_lg-3.8.0.json `"license": "MIT"`; its listed source OntoNotes 5 carries `"license": "commercial (licensed by Explosion)"`; vectors source `"license": "CC0"`.
  - Tesseract: https://raw.githubusercontent.com/tesseract-ocr/tesseract/main/LICENSE "Apache License Version 2.0, January 2004". pytesseract: https://raw.githubusercontent.com/madmaze/pytesseract/master/LICENSE "Apache License Version 2.0, January 2004". pydicom: https://raw.githubusercontent.com/pydicom/pydicom/main/LICENSE "Except for portions outlined below, pydicom is released under an MIT license".
  - Stanza: https://raw.githubusercontent.com/stanfordnlp/stanza/main/LICENSE "Licensed under the Apache License, Version 2.0". transformers: https://raw.githubusercontent.com/huggingface/transformers/main/LICENSE "Apache License Version 2.0".
  - Model cards (Hugging Face, last-modified dates in brackets; revision shas are not pinned because these are third-party cards): https://huggingface.co/blaze999/Medical-NER "License: mit" [2024-04-08]; https://huggingface.co/urchade/gliner_multi_pii-v1 "License: apache-2.0" [2024-04-20]; https://huggingface.co/StanfordAIMI/stanford-deidentifier-base "License: mit" [2024-10-09]; https://huggingface.co/OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1 "License: apache-2.0" [2026-01-13].
  - GLiNER library: https://raw.githubusercontent.com/urchade/GLiNER/main/LICENSE "Apache License Version 2.0".
  - LangExtract: https://raw.githubusercontent.com/google/langextract/main/LICENSE "Apache License Version 2.0". Ollama: https://raw.githubusercontent.com/ollama/ollama/main/LICENSE "MIT License Copyright (c) Ollama". Model of the shipped LangExtract config (`conf/langextract_config_basic.yaml@2.2.364:34` `model_id: "qwen2.5:1.5b"`): https://ollama.com/library/qwen2.5:1.5b "all models except the 3B and 72B are released under the Apache 2.0 license, while the 3B and 72B models are under the Qwen license."
  - Presidio itself, for contrast: `LICENSE@2.2.364:1-3` "The MIT License (MIT) ... Copyright (c) Presidio Contributors."
- Label to use: `[Documented]` with plain-text source hint "(<owner> page, not Presidio docs)". Stanza model licences and the licence terms of Azure services were not read `[To be verified]` (not added to cells).
- Draft impact (R016 item 5: licences in the inventory; no new rows, so counts stay 14/31/10/14). Append to the named cell, one fact per sentence:
  - INV (a) row 13 (presidio-image-redactor), cell "Default engine or dependency", append: `Tesseract licence Apache-2.0 [Documented] (tesseract-ocr/tesseract LICENSE, not Presidio docs). pytesseract licence Apache-2.0 [Documented] (madmaze/pytesseract LICENSE, not Presidio docs).` Add to the Source URL cell: `https://github.com/tesseract-ocr/tesseract/blob/main/LICENSE ; https://github.com/madmaze/pytesseract/blob/master/LICENSE`.
  - INV (a) row 14 (DICOM): append to "Default engine or dependency": `pydicom licence MIT-style, with portions outlined in its LICENSE file [Documented] (pydicom/pydicom LICENSE, not Presidio docs).` URL: `https://github.com/pydicom/pydicom/blob/main/LICENSE`.
  - INV (a) row 18 (spaCy engine): append: `spaCy library licence MIT [Documented] (explosion/spaCy LICENSE, not Presidio docs). Model en_core_web_lg 3.8.0 licence MIT; its listed OntoNotes 5 source is "commercial (licensed by Explosion)" [Documented] (explosion/spacy-models meta file, not Presidio docs).` URLs: `https://github.com/explosion/spaCy/blob/master/LICENSE ; https://github.com/explosion/spacy-models/blob/master/meta/en_core_web_lg-3.8.0.json`.
  - INV (a) row 19 (Stanza): append: `Stanza library licence Apache-2.0 [Documented] (stanfordnlp/stanza LICENSE, not Presidio docs). Stanza model licences [To be verified] (not read).` URL: `https://github.com/stanfordnlp/stanza/blob/main/LICENSE`.
  - INV (a) row 20 (transformers engine): append: `transformers library licence Apache-2.0 [Documented] (huggingface/transformers LICENSE, not Presidio docs). Sample model StanfordAIMI/stanford-deidentifier-base licence MIT [Documented] (Hugging Face model card, not Presidio docs).` URLs: `https://github.com/huggingface/transformers/blob/main/LICENSE ; https://huggingface.co/StanfordAIMI/stanford-deidentifier-base`.
  - INV (a) row 23 (presidio-research): append to "Default engine or dependency": `Notebook 5 uses the model OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1, licence Apache-2.0 [Documented] (Hugging Face model card, not Presidio docs).` URL: `https://huggingface.co/OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1`.
  - INV (b) row 55 (MedicalNER), cell "Extra install or external service": after "(a third-party Hugging Face model, named here only as the default) [Documented] (SUP)" append `Model licence MIT [Documented] (blaze999/Medical-NER model card, not Presidio docs).` URL: `https://huggingface.co/blaze999/Medical-NER`.
  - INV (b) row 57 (GLiNER), cell "Detection method": keep the existing "Apache 2.0" fact and rename its hint to avoid the label hygiene flag, then add `Model licence Apache-2.0 [Documented] (urchade/gliner_multi_pii-v1 model card, not Presidio docs). GLiNER library licence Apache-2.0 [Documented] (urchade/GLiNER LICENSE, not Presidio docs).` URLs: `https://huggingface.co/urchade/gliner_multi_pii-v1 ; https://github.com/urchade/GLiNER/blob/main/LICENSE`.
  - INV (b) row 58 (BasicLangExtract), cell "Extra install or external service": append `LangExtract licence Apache-2.0 [Documented] (google/langextract LICENSE, not Presidio docs). Ollama licence MIT [Documented] (ollama/ollama LICENSE, not Presidio docs). Shipped model qwen2.5:1.5b is under the Apache 2.0 license [Documented] (Ollama library page, not Presidio docs).` URLs: `https://github.com/google/langextract/blob/main/LICENSE ; https://github.com/ollama/ollama/blob/main/LICENSE ; https://ollama.com/library/qwen2.5:1.5b`.
  - INV scope paragraph: add one sentence `Licences of third-party components are given in the cells that name them and cite the owner's page, marked "not Presidio docs".`
  - Columns: no change needed (R016 puts licences in the inventory). Optional single bullet in PD4 R4 after B:56: `• Tesseract is licensed Apache-2.0 (tesseract-ocr/tesseract LICENSE, not Presidio docs) **[Documented]**` with its URL in PD4 R9.

### T7 — Azure-hosted pieces: retention, regions, data-handling terms
- Verdict: PARTLY RESOLVED (Azure AI Language, Azure OpenAI and Document Intelligence answered from Microsoft pages; Azure Health Data Services retention not stated on the page checked)
- Evidence (Microsoft docs, not Presidio docs; read 2026-10-09 via fetch_text.py):
  - Azure Language, https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/language-service/data-privacy (redirect target of the legacy /legal/cognitive-services/language-service/data-privacy URL): "Language doesn't store or process customer data outside the region where the customer deploys the service instance." and "Data sent in synchronous or asynchronous calls may be temporarily stored by Language for up to 48 hours only and is purged thereafter."
  - Azure OpenAI, https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy: "Models sold by Azure store and process data to provide the service and to monitor for uses that violate the applicable product terms." and "The models are stateless: no prompts or completions are stored in the model." and "Prompts and responses are processed within the customer-specified geography (unless you are using a Global or DataZone deployment type), but may be processed between regions within the geography for operational purposes".
  - Document Intelligence, https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/document-intelligence/data-privacy-security: "The service stores submitted input data and analyze results for 24 hours after an analysis operation completes."
  - Azure Health Data Services de-identification, https://learn.microsoft.com/en-us/azure/healthcare-apis/deidentification/overview: checked for retention, storage and region statements; the overview names Blob Storage options and RBAC only (the page says "Each document processed by a job can't exceed 2 MB."); retention and region not stated there.
- Label to use: `[Documented]` for the three answered services, plain-text hint "(Microsoft docs, not Presidio docs)". AHDS retention: `[Not disclosed]` (checked the AHDS overview page, the Presidio AHDS page and the surrogate operator code).
- Draft impact:
  - INV (b) row 60 (AzureAILanguageRecognizer), cell "Extra install or external service": append `Azure Language may temporarily store data sent in calls for up to 48 hours and does not store or process customer data outside the deployment region [Documented] (Microsoft docs, not Presidio docs).` URL: `https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/language-service/data-privacy`.
  - INV (b) row 59 (AzureOpenAILangExtract), same cell: append `Azure OpenAI processes prompts and responses within the customer-specified geography unless a Global or DataZone deployment type is used, and the models are stateless [Documented] (Microsoft docs, not Presidio docs).` URL: `https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy`.
  - INV (b) row 61 (AzureHealthDeidRecognizer) and INV (c) row 76 (surrogate_ahds): append `Retention and region of data sent to the AHDS de-identification service [Not disclosed] (checked the Presidio AHDS page and the Microsoft AHDS overview page).`
  - B, PD4 R4: after B:59 (Document Intelligence sends image bytes) add `• Document Intelligence stores submitted input data and analyze results for 24 hours after an analysis completes (Microsoft docs, not Presidio docs) **[Documented]**`; add the Microsoft URL to PD4 R9. Replace PD4 R8 bullet B:141 with `• Whether other Azure data terms apply when Document Intelligence is used beyond the 24-hour retention (Microsoft docs, not Presidio docs, were read for retention only)`.
  - A, PD1 R8 (A:167): replace with `• Retention and region of data sent to the Azure Health Data Services endpoint (the Presidio AHDS page and the Microsoft overview page do not state them)`. A, PD2 R8 (A:356): replace with `• What the AHDS surrogate operator sends to Azure and retention there (code passes the text to the AHDS client, see T8; retention not stated on the Presidio or Microsoft overview pages)`.
  - PD1 R8 Summary: see T24 entry list for the new text.

### T8 — What leaves the process for the Azure recognizers and operators
- Verdict: RESOLVED
- Evidence (all `data-privacy-stack/presidio@2.2.364`, https://github.com/data-privacy-stack/presidio/blob/2.2.364/<path>):
  - `presidio-analyzer/presidio_analyzer/predefined_recognizers/third_party/azure_ai_language.py:121-123` `response = self.ta_client.recognize_pii_entities(` `[text], language=self.supported_language`; the client is built at `:103` `TextAnalyticsClient(` with the endpoint read at `:89`.
  - `.../third_party/ahds_recognizer.py:113-117` `body = DeidentificationContent(` `input_text=text,` ... `result = self.deid_client.deidentify_text(body)`.
  - `presidio-anonymizer/presidio_anonymizer/operators/ahds_surrogate.py:270-277` `content = DeidentificationContent(` `input_text=text,` ... `result = client.deidentify_text(content)`.
  - `.../third_party/langextract_recognizer.py:161,172` `"text_or_documents": kwargs.pop("text"),` ... `return lx.extract(**extract_params)`; the Azure client class is `AzureOpenAILanguageModel` (`azure_openai_provider.py:33`) created by `_create_azure_openai_client` (`:99`) from an endpoint.
  - `presidio-image-redactor/presidio_image_redactor/document_intelligence_ocr.py:166` `poller = self.client.begin_analyze_document(self.model_id, imgbytes, **kwargs)`.
- Label to use: `[Documented: repo data-privacy-stack/presidio@2.2.364]` for each "the code passes X to the Azure SDK call Y". The sentence "so the text leaves the process for the configured endpoint" remains `[Inferred]` (premise: the SDK client is constructed with the configured endpoint; the HTTP transfer happens inside the Azure SDK and, for the LangExtract route, inside the langextract and openai packages, which were not read).
- Draft impact:
  - A, PD1 R6, replace A:137 with four bullets, each `[Documented: repo data-privacy-stack/presidio@2.2.364]`: (1) `• Azure AI Language recognizer passes the text to the service: `self.ta_client.recognize_pii_entities([text], language=self.supported_language)` (`azure_ai_language.py@2.2.364:121-123`)`; (2) `• AHDS recognizer passes the text to the service: `DeidentificationContent(input_text=text, ...)` then `self.deid_client.deidentify_text(body)` (`ahds_recognizer.py@2.2.364:113-117`)`; (3) `• Language-model recognizers pass the text to LangExtract: `"text_or_documents": kwargs.pop("text")` and `lx.extract(**extract_params)` (`langextract_recognizer.py@2.2.364:161,172`), with an Azure OpenAI client class in `azure_openai_provider.py@2.2.364:33`; (4) then one bullet `• For these recognizers the text leaves the Presidio process for the configured Azure endpoint (premise: the clients are built from the endpoint parameters; the transfer itself happens inside the Azure, langextract and openai packages, which were not read) **[Inferred]**`. Add `azure_openai_provider.py` and `langextract_recognizer.py` blob URLs (tag 2.2.364) and `ahds_recognizer.py` to PD1 R9.
  - A, PD2 R8 (A:356): see T7. Add to PD2 R6 or R4 one bullet `• The AHDS surrogate operator passes the text to the service: `DeidentificationContent(input_text=text, ...)` and `client.deidentify_text(content)` (`ahds_surrogate.py@2.2.364:270-277`) **[Documented: repo data-privacy-stack/presidio@2.2.364]`.
  - INV (b) row 60 cell "Extra install or external service": change "The text leaves the local process for the Azure endpoint [Inferred] (premise: RemoteRecognizer with a TextAnalyticsClient to a configured endpoint)" to `The code passes the text to TextAnalyticsClient.recognize_pii_entities [Documented: repo data-privacy-stack/presidio@2.2.364] (azure_ai_language.py:121-123). The text therefore leaves the local process for the configured endpoint [Inferred] (premise: the client is built from the endpoint).` Same pattern for rows 59 and 61 and (c) row 76 (AHDS: ahds_recognizer.py:113-117; ahds_surrogate.py:270-277).
  - PD4 R4 (B:59): already `[Documented: repo ...]`; no change.

### T9 — Is 2.2.364 the latest release; what do its notes say
- Verdict: PARTLY RESOLVED (latest tag and CHANGELOG substitute settled; the GitHub release body and title stay unread)
- Evidence:
  - `git ls-remote --tags https://github.com/data-privacy-stack/presidio` (2026-10-09): `779dbd286d5ef4d1fbe2514275fb1bce358f2417 refs/tags/2.2.364`; next lower tags 2.2.363 (5c0ac333), 2.2.362 (2450561b), 2.2.361 (cae43c1a), 2.2.360 (af1c5244); no higher 2.x tag among 56 tags. `git log -1` at the tag: "Bump `presidio-anonymizer` floor in `presidio-structured` (#2184)", committed 2026-07-22.
  - CHANGELOG at the tag (R015 substitute), https://github.com/data-privacy-stack/presidio/blob/2.2.364/CHANGELOG.md: has no `## [2.2.364]` heading; the top section is `## [unreleased]` (line 5), above `## [2.2.363] - 2026-06-28` (line 55). The four features that the P0 note records from the release text appear under `[unreleased]`: line 38 "Added `BatchDeanonymizeEngine` to complement `BatchAnonymizerEngine` for batch deanonymization over lists and nested dictionaries."; line 9 "Added `NoOpNlpEngine` for configurations that do not require NLP engine artifacts"; line 43 "Added Python 3.14 package support for `presidio-anonymizer`, `presidio-image-redactor`, `presidio-cli`, `presidio-structured`, and `presidio`"; line 39 "Added a `--threshold` flag to `presidio-cli` to override the analyzer confidence threshold directly from the command line (#2114)".
  - The same absence of a 2.2.364 heading holds on `main` (HEAD 2523c7b, 2026-10-08): first headings `## [unreleased]` (line 5) then `## [2.2.363]` (line 64).
  - Release page text: not readable (github.com 403; GitHub MCP denied). The P0 note (explorer/20261009_presidio_p0.md S19) records quotes "feat(anonymizer): add batch deanonymization support", "feat: add no-op NLP engine", "feat: add Python 3.14 compatibility to all remaining Presidio packages", "feat(cli): add threshold flag override" from the GitHub release via the MCP at P0; I did not re-read them, so they carry no new label from me.
- Label to use: "2.2.364 is the highest version tag" and "CHANGELOG has no 2.2.364 section" `[Documented: repo data-privacy-stack/presidio@2.2.364]`. "2.2.364 is the latest GitHub release" and the release-note wording stay `[To be verified]`, but are no longer carried as draft bullets (see below). "The changelog's unreleased section is the effective 2.2.364 content" is `[Inferred]` (premise: the tag commit contains these changes and no 2.2.364 section was ever added).
- Draft impact:
  - A, PD1 R4: replace the TBV bullet A:81 with two bullets: `• 2.2.364 is the highest version tag of the repository (`git ls-remote --tags`, 2026-10-09) **[Documented: repo data-privacy-stack/presidio@2.2.364]`; `• `CHANGELOG.md@2.2.364` has no 2.2.364 section: its top section is `[unreleased]` (line 5), above 2.2.363 dated 2026-06-28 (line 55) **[Documented: repo data-privacy-stack/presidio@2.2.364]`. Keep A:82 (unreleased heading versus tagged code) as is, adding "and the CHANGELOG contains no 2.2.364 section".
  - A, PD3 R4: delete the TBV bullet A:443 (A:441 already states that `CHANGELOG.md@2.2.364:38` lists `BatchDeanonymizeEngine` under its unreleased heading).
  - R8 bullets that cite "github.com returned 403": A:170 and A:359 -> `• What the GitHub release notes for 2.2.364 say (the release page was not read; CHANGELOG.md at the tag lists the changes under its unreleased heading)`; A:501 -> `• Whether the batch deanonymiser is named in the 2.2.364 release notes (code is in the tag; the CHANGELOG lists it under its unreleased heading; the release page was not read)`; B:143, B:306, B:452 -> same wording as A:170.
  - INV (a) row 22 (no-op) cell "Version read": replace "whether the GitHub 2.2.364 release notes name it was not readable here [To be verified]" with `the GitHub 2.2.364 release notes were not read [To be verified]`; INV (d) row 98 "Status" cell: replace "the 2.2.364 release notes and CHANGELOG [unreleased] mention it, but the release page was not readable here [To be verified]" with `the CHANGELOG lists it under its unreleased heading [Documented: repo data-privacy-stack/presidio@2.2.364] (CHANGELOG.md:38); the GitHub release notes were not read [To be verified]`.
  - Seeds/brief: the title "Release 2.2.364 / 0.0.60" is unverified; see T10.

### T10 — Which package does 0.0.60 belong to
- Verdict: CORRECTION (brief, P0 note and seeds line are wrong; the drafts are right)
- Evidence: `pyproject.toml` at tag 2.2.364, line 7 of each: presidio-image-redactor `version = "0.0.60"`; presidio-structured `version = "0.0.8"`; presidio-cli `version = "0.0.9"`; presidio-analyzer, presidio-anonymizer and presidio `version = "2.2.364"`. (https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-image-redactor/pyproject.toml, .../presidio-structured/pyproject.toml, .../presidio-cli/pyproject.toml.) The same values are on `main` (HEAD 2523c7b). The release title text itself is unread (T9).
- Label to use: `[Documented: repo data-privacy-stack/presidio@2.2.364]`.
- Draft impact:
  - INV (a), paragraph before the table (line 7): replace the sentence beginning "The release title ..." with `Versions in the table are the values in each package's pyproject.toml at 2.2.364: presidio-image-redactor 0.0.60, presidio-structured 0.0.8, presidio-cli 0.0.9, and presidio-analyzer, presidio-anonymizer and the presidio meta-package 2.2.364 [Documented: repo data-privacy-stack/presidio@2.2.364] (pyproject.toml of each package).`
  - A, B, INV: no value changes (PD4 R4 B:65 and PD5 R4 B:229 are right).
  - Main: correct the P0 note and seeds line (already queued).

### T11 — presidio-research pin
- Verdict: RESOLVED
- Evidence: `git ls-remote --tags https://github.com/data-privacy-stack/presidio-research` (2026-10-09): 0.1.1, 0.2.0, 0.2.1, 0.2.3, 0.3, 0.3.1, `06d2030688ece62f58047e567aecd70e4bb5f104 refs/tags/0.3.2`, 0.22; highest is 0.3.2. At the tag, https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/pyproject.toml line 3 `version = "0.3.2"`, line 6 `license = {text = "MIT"}`, line 7 `requires-python = ">=3.11,<3.14"`, line 18 `"presidio-analyzer>=2.2.364",`. HEAD 0cb36502 (2026-09-30) differs in `requires-python = ">=3.11,<3.15"` and has an Unreleased CHANGELOG section ("Python 3.14 support"). The distribution name is `presidio_evaluator` (pyproject line 2); the README install line is `pip install presidio-evaluator`.
- Label to use: `[Documented: repo data-privacy-stack/presidio-research@0.3.2]` (one repo label, tag form; R014 and README rule 8).
- Draft impact:
  - INV scope paragraph (line 3): replace "Evaluation-toolkit facts are pinned to data-privacy-stack/presidio-research at the short SHA 0cb36502 (commit 0cb365021884d849c5bc21957de67c91943c1662, 2026-09-30; no release tag was visible in the shallow clone)." with `Evaluation-toolkit facts are pinned to data-privacy-stack/presidio-research at release tag 0.3.2 (commit 06d2030688ece62f58047e567aecd70e4bb5f104, 2026-08-04).`
  - INV (a) row 23: change every `[Documented: repo data-privacy-stack/presidio-research@0cb36502]` (7 labels) to `[Documented: repo data-privacy-stack/presidio-research@0.3.2]`; cell "Version read": `0.3.2 [Documented: repo data-privacy-stack/presidio-research@0.3.2] (pyproject.toml:3), tag 0.3.2 is the highest tag [Documented: repo data-privacy-stack/presidio-research@0.3.2]`; requires-python becomes `>=3.11,<3.14 [Documented: repo data-privacy-stack/presidio-research@0.3.2] (pyproject.toml:7), narrower than Presidio`; "Status" cell stays `Not stated [Not disclosed]` but replace "CHANGELOG has an Unreleased section" by "CHANGELOG at the tag has an empty Unreleased heading". Source URLs: replace the two `/blob/0cb365021884d849c5bc21957de67c91943c1662/` URLs by `https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/README.md` and `.../0.3.2/pyproject.toml`.
  - INV-RN 5 not carried. A: PD1 to PD3 already use 0.3.2; A RN-3 not carried.

### T12 — presidio-research read status and scope claims
- Verdict: RESOLVED
- Evidence (https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/...):
  - README.md:3-4 "This package provides evaluation and data-science capabilities for Presidio and PII detection models in general." and "It also includes a fake data generator that creates synthetic sentences based on templates and fake PII."
  - `presidio_evaluator/models/` holds `presidio_analyzer_wrapper.py`, `presidio_recognizer_wrapper.py`, `base_model.py`; `presidio_recognizer_wrapper.py` docstring "Class wrapper for one specific PII recognizer"; `InputSample` takes `full_text` and `spans` (`data_objects.py:207-211`); readers: `read_dataset_json` (`data_objects.py:682`); formatters: `conll_formatter.py`, `i2b2_formatter.py`.
  - No image, OCR, DICOM, table, JSON-document or structured mode and no Anonymizer or Deanonymizer evaluator: grep of `presidio_evaluator/`, `pyproject.toml`, `README.md` and `docs/` for ocr, dicom, image_redactor, presidio_structured found only unrelated CSS comments and a name list; the only `AnonymizerEngine` import is in `presidio_evaluator/data_generator/presidio_pseudonymize.py`. Dependencies at the tag list presidio-analyzer and presidio-anonymizer only (no image-redactor or structured).
  - Dataset format: `data/synth_dataset_v2.json`, read with `InputSample.read_dataset_json("data/synth_dataset_v2.json")` (README.md:96).
- Label to use: `[Documented: repo data-privacy-stack/presidio-research@0.3.2]` for the presence facts; the absences are `[Not disclosed]` naming the paths searched.
- Draft impact:
  - B, PD4 R7: replace B:126 with `• presidio-research has no image, OCR or DICOM evaluation mode (checked README.md, docs/, presidio_evaluator/ and pyproject.toml at the tag; its models are the Analyzer and single-recognizer wrappers, and its dataset format is text with character spans) **[Not disclosed]**`. B, PD4 R7 B:127 stays (premise now verified: use presidio-research for the text step).
  - B, PD5 R7: replace B:290 with `• presidio-research has no table or JSON-document mode (checked README.md, docs/, presidio_evaluator/ and pyproject.toml at the tag; its dataset format is text with character spans) **[Not disclosed]**`.
  - B, PD6 R7: replace B:444 with `• presidio-research can wrap one recognizer: "Class wrapper for one specific PII recognizer" (`presidio_evaluator/models/presidio_recognizer_wrapper.py@0.3.2`) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]` and add `• Its datasets are text samples with character spans (`InputSample` with `full_text` and `spans`, `data_objects.py@0.3.2:207-211`) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]`. Add to PD4 R9, PD5 R9, PD6 R9: `https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/README.md` (and `.../presidio_evaluator/models/presidio_recognizer_wrapper.py` for PD6).
  - A, PD2 R5 (A:320) and PD3 R7 (A:491) absence claims: confirmed; no change (PD2 R5 text "only `presidio_pseudonymize.py` ... imports `AnonymizerEngine`" is correct at the tag).
  - B RN-3 and B's "(R010)" bullets keep working; the PD6 R7 Summary needs no change.

### T13 — Features in the tagged code that CHANGELOG lists under unreleased
- Verdict: RESOLVED
- Evidence: CHANGELOG.md@2.2.364 (https://github.com/data-privacy-stack/presidio/blob/2.2.364/CHANGELOG.md): `## [unreleased]` at line 5 lists `NoOpNlpEngine` (line 9), per-recognizer and per-entity score thresholds (line 10, "Added per-recognizer and per-entity score threshold configuration in the recognizer registry YAML, with the analyzer's global `default_score_threshold` as the fallback (#2116)"), `PhUmidRecognizer` (line 11), the GB phone-region fix (line 14) and `BatchDeanonymizeEngine` (line 38). But the `## [2.2.363] - 2026-06-28` section at line 74 already reads "Recognizer registry YAML entries now accept `score_thresholds` for recognizer-wide and entity-specific score cutoffs, with the analyzer's `default_score_threshold` as the fallback." So score thresholds appear under both sections. Neither the tag nor `main` (2026-10-08) has a 2.2.364 heading (T9). The tagged docs state the feature (`docs/analyzer/recognizer_registry_provider.md@2.2.364:113`, `docs/analyzer/analyzer_engine_provider.md@2.2.364:66,79,82`); the live pages do not (gh-pages branch, T14).
- Label to use: `[Documented: repo data-privacy-stack/presidio@2.2.364]` for each fact; "the unreleased heading is stale rather than the features unreleased" is `[Inferred]` (premise: no 2.2.364 heading exists although the tag and later commits contain these items).
- Draft impact:
  - A, PD1 R4 A:82: append to the bullet: "; the same file lists per-recognizer `score_thresholds` also under 2.2.363 (line 74)" -> split as a second bullet `• `CHANGELOG.md@2.2.364:74` lists `score_thresholds` for registry YAML entries under 2.2.363 dated 2026-06-28, and line 10 lists the same feature under its unreleased heading **[Documented: repo data-privacy-stack/presidio@2.2.364]`.
  - B, PD6 R4 B:396: append `; CHANGELOG.md@2.2.364:74 also lists it under 2.2.363` as a separate bullet as above (one fact per bullet). B, PD6 R8 B:452 ("Whether per-recognizer score_thresholds is in the released 2.2.364 package ...") delete: answered (the tagged code, tagged docs and the 2.2.363 section state it; live docs lag).
  - PD6 R8 Summary: see T24 list (new text without "per-recognizer threshold status").
  - INV (a) row 22 and INV (b) row 48 and INV (d) row 98: replace the plain-text "[unreleased]" with "under the unreleased heading of CHANGELOG.md" (label hygiene: no bracketed non-label).
  - Add one `[Inferred]` bullet to PD1 R4: `• The unreleased heading looks stale: the tag and `main` both lack a 2.2.364 section while the tagged code contains these items (premise: CHANGELOG.md@2.2.364 lines 5 and 55) **[Inferred]`.

### T14 — Which commit does the deployed docs site match
- Verdict: PARTLY RESOLVED (the site cannot be pinned to a commit; its publishing chain and date are established)
- Evidence:
  - Branch `gh-pages` of data-privacy-stack/presidio: HEAD e1987e57d4474f14f9da03884ca1a99ece7dc6a5 (2026-07-04, "Create CNAME"); `CNAME` content `presidio.dataprivacystack.org`; its `installation/index.html` lists python 3.10, 3.11, 3.12, 3.13, as the live page does (live: "Presidio is supported for the following python versions: 3.10 3.11 3.12 3.13"). So the live site is the `gh-pages` branch as of 2026-07-04.
  - `.github/workflows/release-docs.yml@2.2.364`: trigger `on: workflow_dispatch:` (manual); "Builds the docs with Zensical ... and publishes the result to GitHub Pages"; the build ref is whichever ref the dispatcher selects, and a search of the `gh-pages` html and json files for the tag commit and the `main` head ids found no build commit id.
  - Distinctive passages that differ from `docs/` at the tag: `docs/installation.md@2.2.364:24` lists `* 3.14`, the live page does not; `docs/analyzer/recognizer_registry_provider.md@2.2.364:113` documents `score_thresholds`, the `gh-pages` copy of that page does not contain it (0 hits); `docs/supported_entities.md@2.2.364` has the PH_UMID row, the live page does not (T20).
  - The tag 2.2.364 was created on 2026-07-22, 18 days after the last docs publish.
- Label to use: live docs facts stay `[Documented]` without a pin and "read 2026-10-09"; "the site predates the 2.2.364 tag, which explains the differences" is `[Inferred]` (premise: gh-pages HEAD 2026-07-04, tag 2026-07-22).
- Draft impact:
  - INV scope paragraph (line 3): replace "because the deployed site does not match docs/ at the tag (Python versions differ, see block (d))" with `because the deployed site was last published on 2026-07-04 (gh-pages branch, 18 days before the 2.2.364 tag) and differs from docs/ at the tag in places (Python versions, score_thresholds, one entity row; see blocks (a), (b), (d))`.
  - A, PD1 R4: add `• The docs site is published from the gh-pages branch of the repository by a manually started workflow (`.github/workflows/release-docs.yml@2.2.364`, trigger `workflow_dispatch`); the branch's last commit is dated 2026-07-04 **[Documented: repo data-privacy-stack/presidio@2.2.364]` and `• The live docs therefore predate the 2.2.364 tag, which is a likely reason they differ from docs/ at the tag (premise: gh-pages HEAD 2026-07-04, tag 2026-07-22) **[Inferred]`. Add the workflow URL to PD1 R9.
  - No docs bullet gets a pin.

### T15 — Python versions stated four ways
- Verdict: RESOLVED
- Evidence: live page https://presidio.dataprivacystack.org/installation/ "Presidio is supported for the following python versions: 3.10 3.11 3.12 3.13" (same text in gh-pages `installation/index.html`); `docs/installation.md@2.2.364:20-24` lists `* 3.10` ... `* 3.14`; classifiers and `requires-python = ">=3.10,<3.15"` in every package pyproject at the tag (e.g. `presidio-image-redactor/pyproject.toml:14-18,23`; `presidio-structured/pyproject.toml:14-18,23`; `presidio-cli/pyproject.toml:14-18,24`); `presidio-cli/README.md:13` "`Python` version: 3.10, 3.11, 3.12, 3.13"; CHANGELOG.md@2.2.364 line 43 (unreleased: 3.14 for anonymizer, image-redactor, cli, structured, presidio) and line 89 (2.2.363: 3.14 for presidio-analyzer). The docs site predates the tag (T14).
- Label to use: each source its own bullet: docs `[Documented]`, repo files `[Documented: repo data-privacy-stack/presidio@2.2.364]`; the explanation is `[Inferred]`.
- Draft impact:
  - B, PD4 R4: replace B:66 ("Python versions conflict (three sources, none picked): ...") with three bullets: `• Python: `requires-python = ">=3.10,<3.15"` and classifiers 3.10 to 3.14 (`presidio-image-redactor/pyproject.toml@2.2.364:14-18,23`) **[Documented: repo data-privacy-stack/presidio@2.2.364]`; `• Python: `docs/installation.md@2.2.364:24` also lists `* 3.14` **[Documented: repo data-privacy-stack/presidio@2.2.364]`; and keep B:67 (live page 3.10 to 3.13). B, PD5 R4: same replacement for B:248 using `presidio-structured/pyproject.toml@2.2.364:14-18,23`, plus the installation.md bullet; B:249 stays.
  - INV (a) row 16 (cli): the two repo sources already stated; add `CHANGELOG.md@2.2.364:43 lists Python 3.14 support for presidio-cli under its unreleased heading [Documented: repo data-privacy-stack/presidio@2.2.364]` only if wanted; otherwise no change.
  - A, PD1 to PD3: no change (three bullets each, one per source). Drop the internal tag "C3" from A:84 and A:450 (style item 3): write "the live page lists 3.10 to 3.13; `docs/installation.md@2.2.364:24` also lists `* 3.14`".

### T16 — Docker image names
- Verdict: RESOLVED
- Evidence (docs/ at tag 2.2.364 and live pages): ghcr names: `docs/installation.md:111-129` "docker pull ghcr.io/data-privacy-stack/presidio-analyzer" ... `docker run -d -p 5002:3000 ghcr.io/data-privacy-stack/presidio-analyzer:latest`; local build names: `docs/analyzer/index.md:47` `docker run -p 5002:3000 presidio-analyzer`, `docs/anonymizer/index.md:82` `docker run -p 5001:3000 presidio-anonymizer`, `docs/image-redactor/index.md:102` `docker run -p 5003:3000 presidio-image-redactor`; a third name: `docs/installation.md:171-172` `docker build ./presidio-anonymizer -t presidio/presidio-anonymizer` and `docker run -d -p 5001:5001 presidio/presidio-anonymizer` (live installation page lines 264-266); mcr.microsoft.com appears in docs only in statements that the images are no longer updated (`docs/installation.md:102` region, `docs/project_transition.md:35`, `docs/build_release.md:28,40,42`) and in an unrelated devcontainer file. `docs/build_release.md:28`: "The legacy Microsoft Container Registry images at `mcr.microsoft.com/presidio-*` are no longer updated."; `:37` shows `docker pull ghcr.io/data-privacy-stack/presidio-analyzer:<release-version>`. No stale MCR run instruction found.
- Label to use: `[Documented]` for live pages; `[Documented: repo data-privacy-stack/presidio@2.2.364]` for repo docs.
- Draft impact:
  - A, PD1 R4 (A:75) and PD2 R4 (A:297): replace the "Source conflict C4: ..." lead-in by plain pairs: `• The analyzer page shows `docker run -p 5002:3000 presidio-analyzer`, a locally built image name (Presidio docs, analyzer page) **[Documented]`; `• The installation page shows the registry name `ghcr.io/data-privacy-stack/presidio-analyzer` and, for a local build, `presidio/presidio-anonymizer` on port 5001:5001 (Presidio docs, installation page) **[Documented]`. (Drop "C4" from the text.)
  - INV (d) row 88 caveat: add `The INST page also shows a local build tag presidio/presidio-anonymizer mapped to 5001:5001 [Documented] (INST)`.
  - INV-RN 1(iii) not carried.
  - Related to T17 (class b, stays open): `docs/build_release.md:37` says images are pinned by "the release tag shown on the relevant GitHub Packages page"; the existence of a GHCR tag 2.2.364 is still unchecked (no pull, no registry call per R019).

### T19 — Supported-entities page versus default_recognizers.yaml
- Verdict: RESOLVED (no default-on or default-off statement exists on the live entity page; one exists in the tagged repo page)
- Evidence:
  - Live page https://presidio.dataprivacystack.org/supported_entities/ (re-read raw, 80 entity ids): searched for "disabled", "enabled", "default"; the only hit is the MedicalNER sentence "Uses the blaze999/Medical-NER model by default." (no recognizer default-on statement). Registry page https://presidio.dataprivacystack.org/analyzer/recognizer_registry_provider/ line 243 "enabled: enables or disables the recognizer." (no list of defaults). Filtering page https://presidio.dataprivacystack.org/analyzer/filtering_by_country/: no default-on list.
  - Repo page https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/supported_entities.md:161: "| PH_UMID | Philippine Unified Multi-Purpose ID (UMID) / Common Reference Number (CRN). ... Disabled by default. | Pattern match and context |". It is the only "disabled by default" row (grep of that file) and is absent from the live page. `docs/samples/python/langextract/index.md:154` also says "The recognizer is disabled by default in `default_recognizers.yaml`".
  - The ids `DE_LANR`, `DE_BSNR`, `DE_VAT_ID`, `DE_FUEHRERSCHEIN` and `ABA_ROUTING_NUMBER` are on neither the live page nor `docs/supported_entities.md@2.2.364` (id-by-id comparison of both pages, 2026-10-09); `SG_UEN`, `FI_PERSONAL_IDENTITY_CODE`, `KR_PASSPORT` are on both (`docs/supported_entities.md@2.2.364:81,105,112`).
- Label to use: absences on the live page `[Not disclosed]` (checked the three pages above); `PH_UMID` row `[Documented: repo data-privacy-stack/presidio@2.2.364]`.
- Draft impact:
  - INV (b) intro (line 28), sentence "The SUP page gives no note on which entities are disabled by default [Not disclosed] (SUP page text searched for "disabled" and "enabled"; none found)": keep, and add `docs/supported_entities.md at the tag marks only PH_UMID as "Disabled by default" [Documented: repo data-privacy-stack/presidio@2.2.364] (docs/supported_entities.md:161).`
  - INV (b) row 48 (Philippines): in the "Entities" cell replace "PH_UMID, which SUP does not list [Documented: repo ...]" with `PH_UMID, which the live SUP page does not list but docs/supported_entities.md lists with "Disabled by default" [Documented: repo data-privacy-stack/presidio@2.2.364] (docs/supported_entities.md:161; country_specific/philippines/ph_umid_recognizer.py:42)`.
  - A, PD1 R2 A:28 and A:29: drop the internal tag "Source conflict C2:". New A:28: `• The entity page lists `SG_UEN`, `FI_PERSONAL_IDENTITY_CODE` and `KR_PASSPORT` with no default-off note (supported entities page) **[Documented]**`; new A:29: `• `default_recognizers.yaml` has no entry for `SgUenRecognizer`, `FiPersonalIdentityCodeRecognizer`, `KrPassportRecognizer` or `AbaRoutingRecognizer`, although all four are exported in `predefined_recognizers/__init__.py` (the `ABA_ROUTING_NUMBER` type is not on the entity page) **[Documented: repo data-privacy-stack/presidio@2.2.364]**` (text unchanged apart from the lead-in). Both sides stay as two bullets (README rule 4).
  - A, PD1 R2 A:39 (no secrets entity) stays `[Not disclosed]`.
  - The runtime answer is T18 (class b, stays open).

### T20 — Entity-row count: 80, 81 or about 120
- Verdict: RESOLVED
- Evidence: both pages parsed for entity ids on 2026-10-09. Live page (https://presidio.dataprivacystack.org/supported_entities/): 80 distinct ids (71 plus 9 `MEDICAL_*`: `MEDICAL_LICENSE` under Global and eight NER `MEDICAL_*` ids), no duplicates. `docs/supported_entities.md@2.2.364` (https://github.com/data-privacy-stack/presidio/blob/2.2.364/docs/supported_entities.md): 81 ids; the single difference is `PH_UMID` (line 161), present only at the tag. Per-section ids on the live page: Global 13 (incl. `MEDICAL_LICENSE`), USA 7, UK 6, Spain 3, Italy 5, Poland 1, Singapore 2, Australia 4, India 6, Finland 1, Korea 5, Nigeria 2, Philippines 1, Canada 1, Sweden 2, South Africa 1, Thai 1, Turkey 2, Germany 9, Medical 8. The count is mine (counted by parsing); the vendor states no total.
- Label to use: structure of the page `[Documented]`; the counts `[Inferred]` with the premise "counted by parsing the page tables on 2026-10-09" (README label hygiene; the Summary then must not rest on the count).
- Draft impact:
  - A, PD1 R2 A:18, replace the single bullet by two: `• The page groups types into Global, 18 country sections (USA, UK, Spain, Italy, Poland, Singapore, Australia, India, Finland, Korea, Nigeria, Philippines, Canada, Sweden, South Africa, Thai, Turkey, Germany) and Medical / Clinical **[Documented]**` and `• 80 distinct entity ids appear in the page tables on 2026-10-09; `docs/supported_entities.md@2.2.364` has 81, the extra id being `PH_UMID` (counted by parsing both pages) **[Inferred]**`.
  - PD1 R2 Summary: new text (40 words, label stays Documented because it now rests on the structure bullet and on A:24, A:58): `Summary: **PII entity types, English by default.** The supported-entities page groups its types into Global, 18 country sections and a medical section. A default English setup loads pattern recognizers plus a spaCy name and place model. Detection is not guaranteed complete. **[Documented]**` (This also resolves T58 for PD1 R2.)
  - Brief and INV scope: the "about 120" estimate is superseded by 80 (T4).

### T21 — MEDICAL_LICENSE country tag
- Verdict: RESOLVED (premise upgraded to documented; the consequence stays an inference)
- Evidence: `presidio-analyzer/presidio_analyzer/recognizer_registry/recognizer_registry.py:117-140` (docstring of `load_predefined_recognizers`): "recognizers with ``country_code`` set are loaded only when their code is in ``countries``." (lines 137-138) and "Passing an empty list (``countries=[]``) keeps only locale-agnostic recognizers." (lines 140-141). `country_specific/us/medical_license_recognizer.py:21` `COUNTRY_CODE = "us"`; `conf/default_recognizers.yaml:377-379` `name: MedicalLicenseRecognizer`, `type: predefined`, `country_code: us`. Filtering page https://presidio.dataprivacystack.org/analyzer/filtering_by_country/: "Every recognizer under presidio_analyzer.predefined_recognizers.country_specific.<country> ships with its COUNTRY_CODE set to the appropriate ISO code".
- Label to use: premise bullets `[Documented: repo data-privacy-stack/presidio@2.2.364]`; "a country filter without us drops it" `[Inferred]` (premise: the two documented facts).
- Draft impact: INV (b) row 35 cell "Enabled by default": keep the sentence but change its inner label: `... A country filter that omits us would therefore drop it [Inferred] (premise: recognizers with a country_code are loaded only when the code is in the countries list [Documented: repo data-privacy-stack/presidio@2.2.364], recognizer_registry.py:137-138)`. Add `https://presidio.dataprivacystack.org/analyzer/filtering_by_country/` is already in the URL cell. No Summary affected.

### T22 — Recommended score threshold
- Verdict: RESOLVED (absence confirmed; two more example values found)
- Evidence: grep of `docs/` at 2.2.364 and at `main` for "threshold" (excluding ocr_threshold, mixed_strategy and IoU): only examples and one recipe tip: `docs/tutorial/08_no_code.md:41` `default_score_threshold: 0.4`; `docs/tutorial/09_ad_hoc.md:66` `"score_threshold": 0.6,` (request example); `docs/analyzer/analyzer_engine_provider.md:172` `default_score_threshold: 0.7`; `docs/faq.md:120` "Change the acceptance threshold, which defines what is the minimum confidence value for a detected entity to be returned."; German recipe `docs/recipes/german-language-support/README.md:118` "setting `score_threshold=0.5` when no context is present is recommended" and `:125` "Set `score_threshold` to 0.4–0.5 for production use to filter out low-confidence" (live: https://presidio.dataprivacystack.org/recipes/german-language-support/). Presidio-research: `docs/evaluation.md:120` `AnalyzerEngine(default_score_threshold=0.3)` (example); `docs/mapping_scenarios.md:312` "Notebook 4 uses threshold 0.4, Notebook 5 uses 0.3." No threshold advice in `docs/image-redactor/`, `docs/structured/` or `presidio-structured/README.md`.
- Label to use: `[Not disclosed]` for "no general recommended threshold" (checked the pages named); the example values `[Documented: repo ...]`.
- Draft impact:
  - A, PD1 R5 A:102: append to the examples bullet ", `"score_threshold": 0.6` in the ad-hoc tutorial request (`docs/tutorial/09_ad_hoc.md@2.2.364:66`)" as a new bullet `• Example value only: `"score_threshold": 0.6` in the ad-hoc recognizer request (`docs/tutorial/09_ad_hoc.md@2.2.364:66`) **[Documented: repo data-privacy-stack/presidio@2.2.364]`.
  - A, PD1 R5 A:103: add a second German-recipe bullet `• The recipe also says "setting `score_threshold=0.5` when no context is present is recommended" for identifiers without a checksum (`docs/recipes/german-language-support/README.md@2.2.364:118`) **[Documented: repo data-privacy-stack/presidio@2.2.364]`.
  - A, PD1 R5 A:105 ([Not disclosed]) stays; its checked list should add "recipes". PD4/PD5/PD6 R5 threshold-absence bullets (B:90, B:264, B:414) stay `[Not disclosed]`. The Summaries that state the absence are reworded in T58.

### T24 — Provenance of the notebook figures
- Verdict: PARTLY RESOLVED (bounds found; exact Presidio version still unknown, so the headline qualifier changes)
- Evidence (presidio-research git history, un-shallowed clone, 2026-10-09):
  - Notebook 4: the printed line `'F2': 0.661, 'Precision': 0.733, 'Recall': 0.646` is already in commit 2e97411 (2026-06-30, "Hierarchical evaluation improvements - Presidio Evaluator v-next (#172)") and unchanged in ac490f9 (2026-07-21, "trim oversized outputs"); the 2.2.364 tag is dated 2026-07-22 and 2.2.363 was released 2026-06-28 (CHANGELOG.md@2.2.364:55). The notebook metadata shows Python 3.13.9; no Presidio version is printed. Cell 10 source: `analyzer_engine = AnalyzerEngine(default_score_threshold=0.4)` (so the 0.661 is at threshold 0.4, not at the Presidio default 0); markdown cell 9: "Using Presidio with default parameters (not recommended for production)."
  - Notebook 5: F2 0.903 in 2e97411 and ac490f9; `'F2': 0.91, 'Precision': 0.921, 'Recall': 0.907` first appears in f2285ca (2026-07-28, "notebook 5 + DataPrivacyStack updates (#180)"); the output line names `experiment_20260723-102549.json`, one day after the 2.2.364 tag. `pyproject.toml@0.3.2:18` requires `presidio-analyzer>=2.2.364`.
- Label to use: the figures `[Documented: repo data-privacy-stack/presidio-research@0.3.2]` (unchanged); the date bounds `[Inferred]` (premise: git history dates of the committed outputs); "default settings equals the 2.2.364 defaults" is `[Not disclosed]` for notebook 4 (version not printed) and for notebook 5 (run date 2026-07-23 is after the tag, but a main-branch build cannot be excluded).
- Draft impact:
  - A, PD1 R5 Summary: change "for default settings" to "for default recognizers at threshold 0.4". New text (44 words): `Summary: **Spans and scores, no verdict.** Each hit has an entity type, start, end and a 0 to 1 score, plus an optional explanation. The default score threshold is 0. A vendor notebook reports F2 0.661 for default recognizers at threshold 0.4 on synthetic data. **[Documented]**`
  - A, PD1 R5, add after A:108: `• Notebook 4's printed result is already present in presidio-research commit 2e97411 dated 2026-06-30, which is before the 2.2.364 tag (2026-07-22) **[Inferred]** (premise: git history of the notebook; the Presidio version is not printed)` and `• Notebook 5's printed result F2 0.91 first appears in commit f2285ca dated 2026-07-28 and names `experiment_20260723-102549.json`; earlier commits print F2 0.903 **[Inferred]** (premise: git history of the notebook)`. Replace R8 bullet A:164 with `• Which Presidio version produced the notebook outputs (notebook 4 predates the 2.2.364 tag; notebook 5 was run on or after 2026-07-23; neither prints a version; reproduction needs testing)`.
  - A RN-3 and RN-8 not carried. Reproduction (T25) stays open.

### T26 — "~30%" versus the printed outputs
- Verdict: RESOLVED (both vendor statements kept; the notebook differences explain part of the gap)
- Evidence: vendor statements: https://presidio.dataprivacystack.org/evaluation/ "Notebook 5: Shows how one can configure Presidio to detect PII much more accurately, and boost the f score in ~30%." (same in `presidio-research@0.3.2/README.md:22`); README.md:21 "Note that this is using the vanilla Presidio, and the results aren't very accurate." Notebook 5 differs from notebook 4 in more than recognizers (presidio-research@0.3.2): a Hugging Face NER recognizer with `model_name="OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1"` (cell 14), added recognizers for TITLE, years and AGE (cells 14 and following: `get_titles_recognizer`, `get_years_recognizer`, `get_age_recognizer`), a context-aware enhancer, and `default_score_threshold=0.3` (cell 18) against 0.4 in notebook 4; `docs/mapping_scenarios.md:312` "Notebook 4 uses threshold 0.4, Notebook 5 uses 0.3. The lower threshold in NB5 introduces `AGE` predictions". Printed: F2 0.661 to 0.91, +0.249 absolute, 37.7 percent relative (computed).
- Label to use: statements and notebook configuration `[Documented]` / `[Documented: repo data-privacy-stack/presidio-research@0.3.2]`; the relative figure and the attribution of the gap `[Inferred]`.
- Draft impact:
  - A, PD1 R5: keep A:110 (docs "~30%") and A:111 (+0.249, about +38 percent `[Inferred]`). Replace A:113 by `• Notebook 5 changes the NER model, the threshold (0.3 against 0.4) and adds recognizers for TITLE, years and AGE, so its gain over notebook 4 mixes several changes (`notebooks/5_Evaluate_Custom_Presidio_Analyzer.ipynb@0.3.2` cells 14 and 18; `docs/mapping_scenarios.md@0.3.2:312`) **[Documented: repo data-privacy-stack/presidio-research@0.3.2]`, plus the existing coverage reading as a separate `[Inferred]` bullet (STREET_ADDRESS 3071 tokens, TITLE, AGE, ZIP_CODE have no default entity type) with the note that the mapping step was read (`CanonicalMapper`, notebook cell "Review entity mapping") but its outcome was not checked.
  - Add `https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/docs/mapping_scenarios.md` to PD1 R9.

### T30 — ConflictResolutionStrategy NONE
- Verdict: RESOLVED
- Evidence: `presidio-anonymizer/presidio_anonymizer/entities/conflict_resolution_strategy.py:15` "NONE: No conflict resolution will be performed." and members only at `:18-19` (`MERGE_SIMILAR_OR_CONTAINED`, `REMOVE_INTERSECTIONS`). In `anonymizer_engine.py:133-196`, `_remove_conflicts_and_get_text_manipulation_data` runs the same-type merge pass and the containment pass unconditionally and applies a third pass only `if conflict_resolution == ConflictResolutionStrategy.REMOVE_INTERSECTIONS:` (line 196). The docstring still names NONE on `main` (2026-10-08).
- Label to use: `[Documented: repo data-privacy-stack/presidio@2.2.364]` for the code facts; "no mode skips conflict resolution" `[Inferred]` (premise: lines 133-196).
- Draft impact:
  - A, PD2 R2 after A:267: add `• `_remove_conflicts_and_get_text_manipulation_data` runs its merge and containment passes for every strategy value and adds a third pass only when the strategy equals `REMOVE_INTERSECTIONS` (`anonymizer_engine.py@2.2.364:133-196`) **[Documented: repo data-privacy-stack/presidio@2.2.364]` and `• A no-resolution mode named NONE therefore does not exist in the tagged code **[Inferred]** (premise: the enum has two members and the passes above)`.
  - A, PD2 R8: delete A:352. PD2 R8 Summary: new text (36 words): `Summary: **Key open questions.** No accuracy or latency figures, REST support for the keep and Azure surrogate operators, the effect of space merging on adjacent names, offsets for non-BMP text, and what the Azure surrogate operator retains.`

### T35 — Key management and authenticated encryption
- Verdict: PARTLY RESOLVED (guidance half closed as an absence; roadmap half is an honest gap)
- Evidence: key handling in the docs: `docs/tutorial/12_encryption.md:21` `crypto_key = "WmZq4t7w!z%C&F)J"` (a literal in the example); `docs/anonymizer/index.md:245` "key: a cryptographic key used for the encryption."; the only secure-storage advice is for the hash salt, `docs/anonymizer/index.md:304` "If you must store salt, use secure storage (e.g., key vault or secrets manager) with strict access controls". Searched `docs/anonymizer/index.md`, `docs/tutorial/12_encryption.md`, `docs/samples/python/encrypt_decrypt.ipynb`, `docs/faq.md` and the OpenAI sample page for key generation, rotation, storage: nothing. `aes_cipher.py@2.2.364:8-48` read in full: PKCS7 padding, random 16-byte IV, AES-CBC, base64; no tag or MAC step. Roadmap: `CHANGELOG.md@2.2.364` and docs name no plan for authenticated encryption; issue tracker and roadmap pages are not reachable here.
- Label to use: guidance `[Not disclosed]` (pages named above); cipher reading stays `[Inferred]` with its premise now verified; roadmap `[Not disclosed]` (checked the CHANGELOG and docs; issues and roadmap not reachable).
- Draft impact:
  - A, PD3 R6 A:476: extend the checked list to "the anonymizer page, encrypt and decrypt tutorial and sample, the OpenAI sample page and FAQ; examples use a literal key in code". Keep `[Not disclosed]`.
  - A, PD3 R4 A:436: keep `[Inferred]`; change the premise to "`aes_cipher.py@2.2.364:8-48` has padding, IV and CBC steps only".
  - A, PD3 R8 A:498-499: keep (roadmap half) with wording "(checked the changelog at the tag and the docs; nothing stated; the project roadmap was not reachable)".

### T37 — NeMo columns E and F and restoring masked values
- Verdict: RESOLVED
- Evidence: `benchtest/drafts/two_level_v2.md` Column E (line 509) and Column F (line 611): searched lines 509 to 715 for restor, deanonym, de-anonym, decrypt, unmask: no hit. NVIDIA page https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/third-party/presidio (fetched raw): searched restor, deanonym, decrypt, reverse: no hit; it lists input, output and retrieval rails and `pip install presidio-analyzer presidio-anonymizer spacy`.
- Label to use: `[Not disclosed]` (checked NeMo columns E and F and the NVIDIA Presidio page; no restore step described).
- Draft impact: A, PD3 R4 A:453: change the label from `[Inferred]` to `[Not disclosed]` with text `• Restoring masked values is not described in NeMo Guardrails columns E and F or on the NVIDIA Presidio page (checked their text for restore, deanonymise, decrypt and reverse), so this column covers the reverse step **[Not disclosed]**`; R8 bullet A:502 stays closed by this (delete). INV (d) row 97 unchanged. NeMo sheets stay frozen.

### T38 — Inventory cells versus column bullets (key sizes, mask defaults)
- Verdict: RESOLVED
- Evidence: `presidio-anonymizer/presidio_anonymizer/operators/encrypt.py:41-49` both branches call `AESCipher.is_valid_key_size(...)` and raise `Invalid input, key must be of length 128, 192 or 256 bits`; `aes_cipher.py:50-57` `is_valid_key_size` returns `len(key) * 8 in algorithms.AES.key_sizes`. `operators/mask.py:47,53-54` `validate_parameter(masking_char, ...)`, `validate_parameter(params.get(self.CHARS_TO_MASK), ..., int)`, `validate_parameter(params.get(self.FROM_END), ..., bool)`; `services/validators.py:53-54` `if parameter_value is None: raise InvalidParamError(f"Expected parameter {parameter_name}")`. So none of the three mask parameters has a default. Docs: `docs/anonymizer/index.md:244` lists the three parameters without defaults.
- Label to use: `[Documented: repo data-privacy-stack/presidio@2.2.364]`.
- Draft impact:
  - INV (c) row 77 (encrypt), cell "Default behaviour": replace "Key-size values [To be verified] (the allowed sizes come from the cryptography library, not read)" with `Key size must be 128, 192 or 256 bits (error text "must be of length 128, 192 or 256 bits") [Documented: repo data-privacy-stack/presidio@2.2.364] (operators/encrypt.py:41-49; operators/aes_cipher.py:50-57)`.
  - INV (c) row 73 (mask), cell "Default behaviour": replace "No default values are stated for the three parameters [Not disclosed] (checked ANON and operators/mask.py)" with `All three parameters are required and have no default; a missing one raises InvalidParamError "Expected parameter ..." [Documented: repo data-privacy-stack/presidio@2.2.364] (operators/mask.py:47,53-54; services/validators.py:53-54). The ANON page states no defaults for them [Not disclosed] (checked ANON)`.
  - No column change (A:327 and A:435 already right). Add the validators.py blob URL to the row 73 URL cell.

### T41 — Image-redactor container environment variables
- Verdict: RESOLVED
- Evidence: `presidio-image-redactor/Dockerfile@2.2.364:3-5` `ARG NLP_CONF_FILE`, `ARG ANALYZER_CONF_FILE`, `ARG RECOGNIZER_REGISTRY_CONF_FILE`; `:10-12` the three `ENV` lines; `:17-19` the three `COPY` lines. `grep -rn` of those names in `presidio-image-redactor/` finds them only in the Dockerfile. In `presidio-analyzer/` they are read only by the REST app: `presidio-analyzer/app.py:46-49` `os.environ.get("ANALYZER_CONF_FILE")`, `"NLP_CONF_FILE"`, `"RECOGNIZER_REGISTRY_CONF_FILE"`; `AnalyzerEngine` itself reads no such variable. `presidio-image-redactor/app.py:39` `self.engine = ImageRedactorEngine()`.
- Label to use: Dockerfile facts `[Documented: repo data-privacy-stack/presidio@2.2.364]`; "no package code reads them" `[Not disclosed]` (grep of the folder named); "probably not changeable by those files" `[Inferred]` with the premise now verified.
- Draft impact: B, PD4 R4 B:71, replace by three bullets: `• The Dockerfile declares `ANALYZER_CONF_FILE`, `NLP_CONF_FILE` and `RECOGNIZER_REGISTRY_CONF_FILE` as build arguments, environment variables and copied files (`presidio-image-redactor/Dockerfile@2.2.364:3-5,10-12,17-19`) **[Documented: repo data-privacy-stack/presidio@2.2.364]`; `• No Python file in `presidio-image-redactor/` references those names (grep of the folder at the tag); in the Analyzer package only the REST app reads them (`presidio-analyzer/app.py@2.2.364:46-49`) **[Not disclosed]`; `• `app.py` builds `ImageRedactorEngine()` with defaults (`presidio-image-redactor/app.py@2.2.364:39`), so the analyzer configuration of the image service is probably not changeable by those files **[Inferred]** (premise: the two bullets above)`. Add `https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/app.py` to PD4 R9.

### T42 — API spec problems
- Verdict: RESOLVED
- Evidence: the live API page https://presidio.dataprivacystack.org/api-docs/api-docs.html is a Redoc page whose script reads `Redoc.init("./api-docs.yml", ...)`; the file https://presidio.dataprivacystack.org/api-docs/api-docs.yml (HTTP 200, saved) is byte-identical to `docs/api-docs/api-docs.yml@2.2.364` (diff empty). Its paths: `/analyze`, `/recognizers`, `/supportedentities`, `/anonymize`, `/anonymizers`, `/deanonymize`, `/deanonymizers`, `/health`; tags: Analyzer and Anonymizer only (no image-redactor tag); no `/redact`, no `allow_list`, `allow_list_match` or `regex_flags` in `AnalyzeRequest`. The image-redactor page links `https://data-privacy-stack.github.io/presidio/api-docs/api-docs.html#tag/Image-redactor` (`docs/image-redactor/index.md@2.2.364:228`), an anchor with no matching tag. On `main` the spec differs only by an added `deny_list_score` field in the ad-hoc recognizer schema.
- Label to use: `[Documented]` for the live spec file (same as the tag); `[Documented: repo data-privacy-stack/presidio@2.2.364]` for the link line.
- Draft impact:
  - B, PD4 R4 B:72-73: keep both bullets; add `• The live API page loads `api-docs.yml`, which is identical to the file at the tag, so the live spec also has no `/redact` path (Presidio docs, API reference page) **[Documented]**` and add `https://presidio.dataprivacystack.org/api-docs/api-docs.yml` to PD4 R9.
  - B, PD4 R8 B:140: delete (answered). A, PD1 R6 A:124 and B PD6 R6 B:423: add "live and tagged spec identical" only if wanted; no change needed.
  - A, PD2 R4 A:300: unchanged.

### T44 — presidio-structured maturity label
- Verdict: CORRECTION (PD5 R4 B:247 says the label is not stated; the getting-started page states alpha; the inventory is right)
- Evidence: https://presidio.dataprivacystack.org/getting_started/getting_started_structured/ "Alpha: This package is currently in alpha, meaning it is in its early stages of development. Features and functionality may change as the project evolves." Same text in `docs/getting_started/getting_started_structured.md@2.2.364:8`. `presidio-structured/pyproject.toml` has no Development Status classifier; the structured page (https://presidio.dataprivacystack.org/structured/) and `presidio-structured/README.md` carry no maturity word (searched alpha, beta).
- Label to use: `[Documented]` (live page) and `[Documented: repo data-privacy-stack/presidio@2.2.364]` (repo copy).
- Draft impact:
  - B, PD5 R4: replace B:247 with `• The getting-started page says: "Alpha: This package is currently in alpha, meaning it is in its early stages of development. Features and functionality may change as the project evolves." (Presidio docs, getting started with structured data page) **[Documented]**` and keep B:246 (changelog 2.2.352 "Added alpha of presidio-structured"). Add `https://presidio.dataprivacystack.org/getting_started/getting_started_structured/` to PD5 R9.
  - B, PD5 R8 B:304: replace with `• Roadmap for presidio-structured: PySpark and k-anonymity are listed as future work (checked the structured page, README and changelog; no dates stated)`.
  - PD5 R4 Summary, optional (42 words): `Summary: **Two steps over the Analyzer and Anonymizer.** A builder samples and analyses values to map each column or key to one entity type, then the engine applies Anonymizer operators to every value there. Package version 0.0.8, marked alpha, under the MIT licence. **[Documented]**`.
  - INV (a) row 15: no change (already alpha, documented).

### T46 — Concepts page versus code for StructuredEngine
- Verdict: RESOLVED (docs defect confirmed; also present on main)
- Evidence: live https://presidio.dataprivacystack.org/learn_presidio/concepts/ "The StructuredEngine is a class in Presidio that is responsible for detecting PII entities in structured data. It uses the AnalyzerEngine to detect PII entities in the text fields of the structured data."; `docs/learn_presidio/concepts.md@2.2.364:32` and on `main` (2026-10-08) the same sentence; `presidio-structured/presidio_structured/structured_engine.py@2.2.364:32` the class has one public method `anonymize`; detection is in `analysis_builder.py`.
- Label to use: `[Documented]` for the page; `[Documented: repo data-privacy-stack/presidio@2.2.364]` for the code.
- Draft impact: B, PD5 R4: keep B:244 and B:245 as the two sides of the conflict; add the repo pin to B:244 by adding the bullet `• The same sentence is in `docs/learn_presidio/concepts.md@2.2.364:32` **[Documented: repo data-privacy-stack/presidio@2.2.364]**` and the blob URL to PD5 R9 (`.../2.2.364/docs/learn_presidio/concepts.md`).

### T47 — PD6 R8: non-pattern recognizers over REST
- Verdict: RESOLVED
- Evidence: `presidio-analyzer/presidio_analyzer/analyzer_request.py:31-36` `PatternRecognizer.from_dict(rec) for rec in ad_hoc_recognizers`; docs https://presidio.dataprivacystack.org/tutorial/09_ad_hoc/ "it is possible to create ad-hoc recognizers via the Presidio Analyzer API for regex and deny-list based logic."
- Label to use: `[Documented: repo data-privacy-stack/presidio@2.2.364]` (already in PD6 R4 B:393) and `[Documented]` (PD6 R1 B:345).
- Draft impact: B, PD6 R8: delete B:448. PD6 R8 Summary: see T13 / list at the end (new text without non-pattern logic).

### T52 — Authentication, TLS and rate-limit guidance beyond the FAQ
- Verdict: RESOLVED (the absences stand with a longer checked list; two network-control facts added)
- Evidence: FAQ https://presidio.dataprivacystack.org/faq/ "Presidio API endpoints do not include built-in authentication by design." and "It is strongly recommended not to expose Presidio services directly to untrusted networks without an authentication layer in front of them." Kubernetes sample https://presidio.dataprivacystack.org/samples/deployments/k8s/ "Presidio is deployed with an ingress controller by default, and uses nginx as ingress.class." (no TLS, certificate or authentication text: searched tls, ssl, https, authentic; `values.yaml` and chart templates under `docs/samples/deployments/k8s/charts/presidio/` also have no tls or ssl entry). App Service sample https://presidio.dataprivacystack.org/samples/deployments/app-service/ "Use the following script to restrict network access for a specific ip such as your computer, a front-end website or an API management." and "Further network isolation, using virtual networks, is possible using an Isolated tier of Azure App Service." Data Factory sample https://presidio.dataprivacystack.org/samples/deployments/data-factory/presidio-data-factory/ uses a managed identity and Key Vault access policy for the factory (no statement on Presidio endpoint authentication or TLS). No rate-limit text anywhere (searched "rate limit" on the same pages and the FAQ).
- Label to use: the two network-control facts `[Documented]`; TLS and rate limiting `[Not disclosed]` (checked FAQ, installation, analyzer, Kubernetes, App Service and Data Factory pages and the Helm chart files).
- Draft impact:
  - A, PD1 R6: extend A:142 to `• TLS for the REST service (checked the FAQ, installation, analyzer, Kubernetes, App Service and Data Factory pages and the Helm chart files; not mentioned) **[Not disclosed]**`; add `• The Kubernetes sample deploys an NGINX ingress controller by default (Presidio docs, Kubernetes page) **[Documented]**` and `• The App Service sample shows a script that restricts network access to a given IP range (Presidio docs, App Service page) **[Documented]**`. Add "rate limiting" to the A:142 list or a separate `[Not disclosed]` bullet "Rate limits (checked the same pages; none stated)".
  - A, PD1 R8 A:168: replace with `• Whether TLS termination is expected at an ingress or gateway (the Kubernetes sample deploys an NGINX ingress; no page mentions TLS or rate limits)`.
  - A, PD2 R6 A:334 / PD3 R6 A:478 / PD4 R6 B:114 / PD6 R6 B:432: no change needed except extending the checked list as above.
  - INV (d) rows 92 and 93 caveats: add `Ingress by default; TLS not mentioned [Not disclosed] (checked K8S)` for row 92 and `IP-range access restriction script [Documented] (APPSVC)` for row 93 (row 93 already says "network blocking").

### T54 — x-correlation-id response header
- Verdict: RESOLVED
- Evidence: https://presidio.dataprivacystack.org/analyzer/decision_process/ "The id can be retrieved from each API response header: x-correlation-id." (also `docs/analyzer/decision_process.md@2.2.364:79`). In the code: `presidio-analyzer/app.py@2.2.364:92` passes `correlation_id=req_data.correlation_id` into `analyze`; `grep -rn -i "after_request\|headers\|add_header\|response.headers\|make_response"` over `presidio-analyzer/app.py` and `presidio-analyzer/presidio_analyzer/` returns no match; `grep -rn -i correlation` over the Analyzer package (outside tests) finds only the request field, the engine parameter and the tracer calls.
- Label to use: docs side `[Documented]`; code absence `[Not disclosed]` (checked the files and patterns named).
- Draft impact: A, PD1 R6, replace A:139 with two bullets: `• The decision-process page says: "The id can be retrieved from each API response header: x-correlation-id." (Presidio docs, decision process page) **[Documented]**` and `• No code in `presidio-analyzer/app.py` or `presidio_analyzer/` at the tag sets a response header (searched for headers, after_request, add_header and make_response; `app.py@2.2.364:92` only passes the id into `analyze`) **[Not disclosed]**`.

### T55 — Decision-process logging and PII in logs
- Verdict: RESOLVED
- Evidence: `presidio-analyzer/presidio_analyzer/analyzer_engine.py:246-248` `if self.log_decision_process:` `self.app_tracer.trace(` `correlation_id, "nlp artifacts:" + nlp_artifacts.to_json()`; `nlp_engine/nlp_artifacts.py:81-84` `return_dict["tokens"] = [token.text for token in self.tokens]` and `return_dict["entities"] = [entity.text for entity in self.entities]`. Page https://presidio.dataprivacystack.org/analyzer/decision_process/ "The decision process logs will be written to standard output." and the example line "[nlp artifacts:{'entities': (Bart Simpson, 4095, 425), 'tokens': ['My', 'name', 'is', 'Bart', 'Simpson'" (the sample text there is "My name is Bart Simpson, my Credit card is: 4095-2609-9393-4932").
- Label to use: code and docs example `[Documented: repo ...]` and `[Documented]`; "PII from the analysed text reaches standard output" `[Inferred]` (premise: the two documented facts).
- Draft impact: A, PD1 R6, replace A:138 with `• With `log_decision_process` on, the trace includes the NLP artifacts with the token texts and entity texts of the analysed string (`analyzer_engine.py@2.2.364:246-248`; `nlp_artifacts.py@2.2.364:81-84`) **[Documented: repo data-privacy-stack/presidio@2.2.364]`; `• The decision-process page says "The decision process logs will be written to standard output." and its example trace line contains the sample text's name and digits (Presidio docs, decision process page) **[Documented]`; `• So PII from the analysed text reaches standard output when decision-process logging is on **[Inferred]** (premise: the two bullets above)`. Add the `nlp_artifacts.py` blob URL to PD1 R9.

### T56 — Automatic language detection
- Verdict: RESOLVED (absence stands)
- Evidence: grep of `docs/` at 2.2.364 for language detect, langdetect, lingua, fasttext, langid, identify language: no statement of automatic language detection (hits are unrelated: recipes, the languages page "PII detection in different languages", GPU auto-detect of hardware); `presidio-analyzer/pyproject.toml:26-35` dependencies list no language-identification package; `presidio-analyzer/app.py:79-83` requires `language`.
- Label to use: `[Not disclosed]` (checked docs/ at the tag, the languages and analyzer pages, pyproject dependencies and app.py).
- Draft impact: A, PD1 R3 A:52: extend the checked list to "the analyzer and languages pages, `docs/` at the tag, the dependency list and `app.py`"; label unchanged.

### T57 — "Out of purpose" statement label
- Verdict: RESOLVED
- Evidence: R015 ruling 1 (main): "`[Inferred]`, with the premise named in the bullet (e.g. 'home page module list'), applied consistently in every column." Home page module list (https://presidio.dataprivacystack.org/, re-read): "Presidio analyzer: PII identification in text", "Presidio anonymizer: De-identify detected PII entities using different operators", "Presidio image redactor: Redact PII entities from images using OCR and PII identification", "Presidio structured: PII identification in structured/semi-structured data".
- Label to use: `[Inferred]` everywhere, premise "home page module list".
- Draft impact:
  - A, PD1 R2 A:38 (already Inferred): append the premise: `... and list no such entity or check (premise: the Home page module list) **[Inferred]**`. A, PD2 R2 A:272: append `(premise: the Home page module list)`.
  - B, PD4 R2 B:19: change label to `**[Inferred]**` and keep the text ("Out of purpose: the home page lists the modules as ...; none is a prompt-injection, harmful-content or topic check (premise: Presidio docs, home page, read 2026-10-09)"). B, PD5 R2 B:198 and PD6 R2 B:362: same change (PD6 bullet label `[Documented]` -> `[Inferred]`).
  - Summary labels: PD4 R2 Summary label `**[Documented]**` -> `**[Inferred]**` (text unchanged, 45 words). PD5 R2 Summary label `**[Documented]**` -> `**[Inferred]**` (text unchanged, 41 words). PD6 R2 Summary is already `[Inferred]`. PD1 R2 and PD2 R2 Summaries do not carry the statement.
  - Brief, R007-style note: record the convention in the change log.

### T58 — Summary labels stronger than their Detail
- Verdict: RESOLVED (rewording given for all four Summaries; label hygiene note for R1 "no verdict" kept as is)
- Evidence: the cited Detail bullets: PD1 R2 A:26-27 are `[Documented: repo ...@0.3.2]` / `[Inferred]` and A:18 is an own count (T20); PD4 R5 B:90 and B:95, PD5 R5 B:264-265, PD6 R5 B:414 and B:416 are `[Not disclosed]`. README section 4 rule 5: "Each Summary label must match the facts the Summary draws on".
- Label to use: Summaries keep `**[Documented]**` after removing the absence sentences; each new sentence is entailed by a `[Documented: repo ...]` bullet of the same row (named below). Absences remain in the Detail and in the R8 Summaries.
- Draft impact (new Summary lines; word counts computed, limit 45):
  - PD1 R2: see T20 (40 words).
  - PD4 R5 (44 words): `Summary: **No verdict; an image comes back.** Python returns the redacted image and, optionally, one box per redacted word with entity type, offsets, score and position. REST returns only the image. The score threshold is 0 in Python and 0.4 on the REST upload form. **[Documented]**` (entailed by B:81-88).
  - PD5 R5 (41 words): `Summary: **A transformed table or object plus a column map.** Output is the anonymised table or dict; the analysis step returns a column-to-entity map with no per-cell findings or scores. The detection threshold defaults to 0 and the mixed-strategy cut-off to 0.5. **[Documented]**` Add to PD5 R5 Detail: `• `mixed_strategy_threshold` defaults to 0.5 (`analysis_builder.py@2.2.364:176`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**` (B:261 already gives the detection threshold default 0). This also replaces "DataFrame" in the Summary by "table" (style item 2).
  - PD6 R5 (42 words): `Summary: **Spans with the score you set.** A custom recognizer returns the usual Analyzer result: entity type, start, end and score. With the decision process on, the explanation names the pattern, regex, original score and context boost. The engine threshold defaults to 0. **[Documented]**` (entailed by B:405-406, B:412).
  - The "returns detections, not a decision" `[Inferred]` in R1 versus `[Documented]` in R5 (label hygiene row 6): acceptable as is; no change.

### T59 — Summary claims without a supporting bullet in the same row
- Verdict: RESOLVED
- Evidence: PD3 R1: https://presidio.dataprivacystack.org/anonymizer/ "Presidio does not store or maintain stateful sessions." (page line 423). PD2 R1: the anonymizer page class diagram lists `EngineResult` with `text` and `items`, and `OperatorResult` with `start`, `end`, `entity_type`, `text`, `operator`; `presidio-anonymizer/presidio_anonymizer/anonymizer_engine.py@2.2.364:76-81` docstring example: input "My name is Bond, James Bond" gives `text: My name is BIP, BIP.` and items `{'start': 16, 'end': 19, ...}` and `{'start': 11, 'end': 14, ...}` (positions in the new text). PD1 R6: https://presidio.dataprivacystack.org/analyzer/languages/ "In its default configuration, it contains recognizers and models for English." and "To extend Presidio to detect PII in an additional language, these modules require modification:".
- Label to use: `[Documented]` for the page quotes; `[Documented: repo data-privacy-stack/presidio@2.2.364]` for the docstring example.
- Draft impact:
  - A, PD3 R1: add `• "Presidio does not store or maintain stateful sessions." (Presidio docs, anonymizer page) **[Documented]**` and change the Summary's last sentence to "Presidio keeps no session state between calls." New Summary (40 words): `Summary: **Encrypts PII in text so it can be restored later.** The encrypt operator swaps each entity for AES ciphertext, and the Deanonymize engine or the decrypt operator reverses it with the same key. Presidio keeps no session state between calls. **[Documented]**`
  - A, PD2 R1: add `• The result is an `EngineResult` with `text` and `items`; each item is an `OperatorResult` with `start`, `end`, `entity_type`, `text` and `operator` (Presidio docs, anonymizer page, class diagram) **[Documented]**` and `• The `anonymize` docstring example shows item positions in the new text: input "My name is Bond, James Bond" gives "My name is BIP, BIP." with items at 16 to 19 and 11 to 14 (`anonymizer_engine.py@2.2.364:76-81`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**`. Summary unchanged.
  - A, PD1 R6: add `• "To extend Presidio to detect PII in an additional language, these modules require modification:" followed by the NLP engine and the recognizers (Presidio docs, languages page) **[Documented]**`. Summary unchanged.

### T60 — Status cells
- Verdict: RESOLVED
- Evidence: `grep -n "Development Status"` over every `pyproject.toml` at 2.2.364 (analyzer, anonymizer, image-redactor, structured, cli, presidio) and over presidio-research@0.3.2: no match; the READMEs of the six packages and the analyzer and anonymizer docs pages carry no stable, beta, alpha or experimental word (searched); marks that exist: image redactor "Please notice, this package is still in beta and not production ready." (https://presidio.dataprivacystack.org/image-redactor/), structured "Alpha: This package is currently in alpha" (T44), LangExtract sample "(Experimental Feature)".
- Label to use: `stable [Inferred]` rows keep their label and premise (premise confirmed); "Not stated" rows keep `[Not disclosed]`.
- Draft impact: INV (a) rows 11, 12, 16 to 23 and INV (d) status cells: change the checked lists to "checked README, pyproject classifiers (no Development Status classifier in any package at the tag) and the docs pages". The vendor wording "alpha" stays (ruled earlier). No Summary affected.

### T61 — Extras for the regex recognizer rows
- Verdict: RESOLVED
- Evidence: an AST import scan of every file under `presidio-analyzer/presidio_analyzer/predefined_recognizers/` at 2.2.364 lists non-standard-library imports only in these files: `generic/email_recognizer.py` (tldextract), `generic/iban_recognizer.py` and `country_specific/spain/es_passport_recognizer.py` (regex), `generic/phone_recognizer.py` (phonenumbers), `ner/gliner_recognizer.py` (gliner), `ner/huggingface_ner_recognizer.py` (torch, transformers), `third_party/ahds_recognizer.py` (azure), `third_party/azure_ai_language.py` (azure), `third_party/azure_openai_langextract_recognizer.py` and `azure_openai_provider.py` (langextract, openai). `presidio-analyzer/pyproject.toml:26-35` core `dependencies` include `regex` (line 31), `tldextract` (line 32), `phonenumbers` (line 34); extras are listed from line 38.
- Label to use: `[Documented: repo data-privacy-stack/presidio@2.2.364]` (code read; the scan is mine and is stated in the cell).
- Draft impact: INV (b) column "Extra install or external service": replace "None beyond presidio-analyzer [Inferred] (premise: ...)" in rows 32 to 54 as follows. Row 32 (credit card, crypto, IBAN): `regex is a core dependency used by IbanRecognizer [Documented: repo data-privacy-stack/presidio@2.2.364] (pyproject.toml:31; generic/iban_recognizer.py)`. Row 33: keep the phonenumbers fact and add `tldextract is a core dependency used by EmailRecognizer [Documented: repo ...] (pyproject.toml:32)`. Row 39 (Spain): `regex is a core dependency used by EsPassportRecognizer [Documented: repo ...] (pyproject.toml:31)`. Rows 34, 35, 37, 38, 40 to 54 (all other regex recognizers): `None; imports are standard library and presidio_analyzer only [Documented: repo data-privacy-stack/presidio@2.2.364] (import scan of the recognizer folder)`. Rows 36 (NER) and 55 to 61 unchanged.

### T63 — Status "Sample" for deployment pages
- Verdict: RESOLVED (premise verified; the classification stays an inference)
- Evidence: `mkdocs.yml@2.2.364:85` `- Samples:`; `:120-128` under `- Deployment:`: `Presidio with App Service: samples/deployments/app-service/index.md`, `Presidio with Kubernetes: samples/deployments/k8s/index.md`, `Presidio with Spark: samples/deployments/spark/index.md`, `Presidio with Fabric: samples/fabric/index.md`, and the Data Factory pages. `docs/samples/deployments/spark/index.md:7` "**Note** that this code works for Databricks runtime 8.1 (spark 3.1.1) and the libraries described here" (live: https://presidio.dataprivacystack.org/samples/deployments/spark/).
- Label to use: premise `[Documented: repo data-privacy-stack/presidio@2.2.364]`; "Sample" status stays `[Inferred]`.
- Draft impact: INV (d) rows 92 to 95: change "Sample [Inferred] (premise: under Samples in the nav)" to `Sample [Inferred] (premise: the pages sit under Samples > Deployment in mkdocs.yml:85,120-128 [Documented: repo data-privacy-stack/presidio@2.2.364])`. The scope paragraph of block (d) gets the same wording.

### T65 — Legacy V1 contents
- Verdict: RESOLVED
- Evidence: `git ls-remote --heads` lists `refs/heads/V1` at 037d239f819271da57b9ff0e1eb4f84b2f1da6f5; clone of branch V1 (2021-02-28, "Update README.MD"): `VERSION` contains `0.95`; `README.MD` begins "DEPRECATED: - This is the V1 version of Presidio. ... - Note that support for services in this version is ceased." and names `pip install presidio-analyzer==0.95` and Docker `tag=v1`; line 44 "Replacing gRPC with HTTP to allow more customizable APIs and easier debugging."; `docs/development.md:114` `GRPC_PORT`; tag `v0.95` exists (`e13d3f9d`). V2 page https://presidio.dataprivacystack.org/presidio_V2/ "The legacy V1 code base will continue to be available under branch V1 but will no longer be officially supported."
- Label to use: `[Documented: repo data-privacy-stack/presidio@V1]` is not a form the README allows for a branch; use `[Documented: repo data-privacy-stack/presidio@037d239f]` (short sha) for V1 facts and `[Documented]` for the V2 page.
- Draft impact: INV (a) row 24: replace "Branch V1 contents not read [To be verified]" with `Branch V1 head 037d239f (2021-02-28) has VERSION 0.95 and a README marked "DEPRECATED" that names PyPI presidio-analyzer==0.95 and Docker tag v1 [Documented: repo data-privacy-stack/presidio@037d239f] (VERSION; README.MD)`. Add `https://github.com/data-privacy-stack/presidio/blob/037d239f819271da57b9ff0e1eb4f84b2f1da6f5/README.MD` to the row's URL cell. The row's "gRPC services [Documented] (V2)" stays.

### T66 — Covered-by convention
- Verdict: RESOLVED (convention proposal; main or merger decides, see QUESTIONS)
- Evidence: no source needed. Facts: `presidio-structured` applies the Anonymizer operators (`operators_factory.py@2.2.364:24-26` list used by `data_processors.py@2.2.364:78`); PD4 and PD5 reuse the Analyzer; the Analyzer image serves `ad_hoc_recognizers` (`presidio-analyzer/app.py@2.2.364:96`); INV (d) row 89 already lists PD6.
- Label to use: not applicable.
- Draft impact (proposal): (1) INV (c) rows 70 to 75 and 77 (replace, redact, hash, mask, custom, keep, encrypt): append `; Presidio: PII detection and anonymisation in structured data (tables and JSON)` to "Covered by Table 3 column"; decrypt, deanonymize_keep and surrogate_ahds rows unchanged (PD5 hardcodes the Anonymize type; surrogate_ahds is registered only with its extra, and is therefore left out). (2) INV (b): no change (the recognizer rows describe the Analyzer, which PD4 to PD6 reuse but do not redefine). (3) INV (d) row 88 (Docker images): append `; Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers)`. The `check_drafts.py inventory --headers` check passes either way (headers are exact copies of the PD5 and PD6 headings). If main prefers no change, nothing breaks.

### T67 — Presidio default replacement string
- Verdict: RESOLVED
- Evidence: anonymizer page https://presidio.dataprivacystack.org/anonymizer/ "The replacing value will be the entity type e.g.: <PHONE_NUMBER>" (page lines 409-410); `presidio-anonymizer/presidio_anonymizer/operators/replace.py:18` `return f"<{params.get('entity_type')}>"` when `new_value` is empty (`:14-18`). `two_level_v2.md` lines 586 and 680 (NeMo columns E and F R8) still say the string is "not verified in the Presidio docs"; those sheets are frozen (R001).
- Label to use: `[Documented]` and `[Documented: repo data-privacy-stack/presidio@2.2.364]`.
- Draft impact: A, PD2 R2 A:250: split. Keep `• Code: `Replace` has `return f"<{params.get('entity_type')}>"` when `new_value` is empty (`replace.py@2.2.364:18`) **[Documented: repo data-privacy-stack/presidio@2.2.364]**` and delete the clause "; the NeMo Guardrails PII columns list this default string as unverified in the Presidio docs". Record the NeMo note in presidio_changes.md only. No change to NeMo sheets. INV (d) row 97 unchanged.

### T68 — German recipe in the nav and on the live site
- Verdict: RESOLVED
- Evidence: `mkdocs.yml@2.2.364:82-84` the Recipes nav lists only `Home: recipes/index.md`, `Contributing: recipes/CONTRIBUTING.md`, `Template: recipes/template.md`. The live site serves the recipe: https://presidio.dataprivacystack.org/recipes/german-language-support/ HTTP 200, text "Formal evaluation against a labelled German dataset has not yet been performed." and "Set score_threshold to 0.4–0.5 for production use to filter out low-confidence"; the `gh-pages` branch contains `recipes/german-language-support/`; the recipes index page mentions "Multilingual: Examples for Spanish, French, German, and other languages" without a link.
- Label to use: `[Documented]` for the live page; `[Documented: repo data-privacy-stack/presidio@2.2.364]` for the repo copy (already used).
- Draft impact: A, PD1 R5 A:103 and A:117: keep the repo-pinned bullets and add `https://presidio.dataprivacystack.org/recipes/german-language-support/` to PD1 R9; add one bullet `• The recipe page is served on the live site although the site navigation does not list it (Presidio docs, German language support recipe) **[Documented]**`. A RN-9 not carried.

### T69 — "Data Protection toolkit for OpenAI" sample
- Verdict: PARTLY RESOLVED (it is linked from the samples index; maintenance status not stated)
- Evidence: `docs/samples/index.md@2.2.364:39` `| Deployment | | Data Protection toolkit for OpenAI | [Data Protection toolkit for OpenAI](deployments/openai-anonymaztion-and-deanonymaztion-best-practices/index.md)|`; the live samples page https://presidio.dataprivacystack.org/samples/ lists "Data Protection toolkit for OpenAI"; it is not in `mkdocs.yml` navigation (grep for "openai" finds only the Streamlit and synthetic-data samples). The sample page https://presidio.dataprivacystack.org/samples/deployments/openai-anonymaztion-and-deanonymaztion-best-practices/ says "spikes/ - Experimental code, such as a Streamlit chat application" (only the spikes folder is called experimental). No maintenance or support statement found (checked the sample page, the samples index and `mkdocs.yml`); the shallow clone holds one commit, so file history was not read.
- Label to use: index listing `[Documented]` / `[Documented: repo ...]`; maintenance status `[Not disclosed]` (checked the sample page, samples index, nav).
- Draft impact: A, PD1 R3 A:49 (and PD2 R3 A:281, PD3 R2 A:411-412): add after the quote `• The sample is listed in the samples index as a Deployment sample (`docs/samples/index.md@2.2.364:39`) though not in the left navigation **[Documented: repo data-privacy-stack/presidio@2.2.364]**` once (PD1 R3), and `• Maintenance status of that sample (checked the sample page, the samples index and the nav; not stated) **[Not disclosed]**`. Keep the URL with the vendor's spelling "anonymaztion".

### T70 — URL pre-check for P9
- Verdict: PARTLY RESOLVED (pre-check done; P9 still runs the official check)
- Evidence (2026-10-09, GET/HEAD only):
  - 50 docs-site URLs extracted from A, B and INV: 49 return HTTP 200; the one 404 is an extraction artefact (trailing backtick) and not a draft URL. `https://data-privacy-stack.github.io/presidio/` answers HTTP 301 with `location: https://presidio.dataprivacystack.org/`; `https://microsoft.github.io/presidio/` answers 200 with a meta-refresh stub ("This page has moved.").
  - `github.com` answers HTTP 403 through the session proxy for every URL tried (three blob URLs of the two repos, the repository roots of data-privacy-stack/presidio and microsoft/presidio); the 139 distinct `github.com/data-privacy-stack/.../blob/...` URLs in A, B and INV were therefore checked on `raw.githubusercontent.com` (same owner, repo, ref and path): 126 answer 200, so those files exist at the cited refs. The 13 that return 404 on raw are INV (b) Source URL cells that point at a directory with `/blob/` (`.../predefined_recognizers/country_specific/{us,uk,spain,italy,singapore,australia,india,korea,nigeria,philippines,sweden,turkey,germany}/`); raw cannot serve directories.
  - The presidio-research URLs in INV (a) row 23 use the full SHA 0cb365021884d849c5bc21957de67c91943c1662 (reachable on raw) and must follow T11 to `.../blob/0.3.2/...`.
- Label to use: HTTP facts `[Documented]` with plain text "(HTTP 301 to https://presidio.dataprivacystack.org/ observed 2026-10-09)".
- Draft impact:
  - INV (b) rows 37 to 54 (Source URL cells): change the 13 directory links from `/blob/2.2.364/.../country_specific/<country>/` to `/tree/2.2.364/.../country_specific/<country>/`.
  - INV (a) row 23: URLs per T11.
  - Tell gr-url-checker: expect HTTP 403 from github.com for repository URLs in this environment (record as an exception, verified by the raw equivalent returning 200); expect 301 for data-privacy-stack.github.io/presidio/ and the 200 stub for microsoft.github.io/presidio/.
  - Strip the stray backtick artefact only if a `.txt` URL list is built from the drafts by regex.

---

## Summary table

| Tn | Verdict | Label | Changes a Summary? |
|---|---|---|---|
| T1 | RESOLVED (R016) | none new | no |
| T2 | RESOLVED (R016) | n/a | no |
| T3 | RESOLVED (R016) | n/a | yes (PD5 R8 Summary) |
| T4 | RESOLVED (R016) | n/a | no |
| T5 | RESOLVED (R010) | [Documented: repo presidio-research@0.3.2] / [Inferred] | no |
| T6 | RESOLVED | [Documented] (owner pages, not Presidio docs) | no |
| T7 | PARTLY RESOLVED | [Documented] (Microsoft docs); AHDS [Not disclosed] | yes (PD1 R8 Summary) |
| T8 | RESOLVED | [Documented: repo presidio@2.2.364]; conclusion [Inferred] | yes (PD1 R8 Summary, shared with T7) |
| T9 | PARTLY RESOLVED | [Documented: repo presidio@2.2.364]; release notes [To be verified] (dropped from bullets) | no |
| T10 | CORRECTION | [Documented: repo presidio@2.2.364] | no |
| T11 | RESOLVED | [Documented: repo presidio-research@0.3.2] | no |
| T12 | RESOLVED | [Documented: repo presidio-research@0.3.2]; absences [Not disclosed] | no |
| T13 | RESOLVED | [Documented: repo presidio@2.2.364]; staleness [Inferred] | yes (PD6 R8 Summary) |
| T14 | PARTLY RESOLVED | live docs [Documented] unpinned; explanation [Inferred] | no |
| T15 | RESOLVED | [Documented] / [Documented: repo ...] per source | no |
| T16 | RESOLVED | [Documented] | no |
| T19 | RESOLVED | [Not disclosed] (live page); PH_UMID row [Documented: repo ...] | no |
| T20 | RESOLVED | structure [Documented]; counts [Inferred] | yes (PD1 R2 Summary) |
| T21 | RESOLVED | premise [Documented: repo ...]; consequence [Inferred] | no |
| T22 | RESOLVED | [Not disclosed]; examples [Documented: repo ...] | no (Summaries in T58) |
| T24 | PARTLY RESOLVED | figures [Documented: repo presidio-research@0.3.2]; dates [Inferred] | yes (PD1 R5 Summary) |
| T26 | RESOLVED | [Documented: repo presidio-research@0.3.2]; relative gain [Inferred] | no |
| T30 | RESOLVED | [Documented: repo presidio@2.2.364]; conclusion [Inferred] | yes (PD2 R8 Summary) |
| T35 | PARTLY RESOLVED | [Not disclosed]; cipher reading [Inferred] | no |
| T37 | RESOLVED | [Not disclosed] | no |
| T38 | RESOLVED | [Documented: repo presidio@2.2.364] | no |
| T41 | RESOLVED | [Documented: repo ...]; [Not disclosed]; [Inferred] | no |
| T42 | RESOLVED | [Documented] / [Documented: repo ...] | no |
| T44 | CORRECTION | [Documented] | optional (PD5 R4 Summary) |
| T46 | RESOLVED | [Documented] / [Documented: repo ...] | no |
| T47 | RESOLVED | [Documented: repo presidio@2.2.364] | yes (PD6 R8 Summary) |
| T52 | RESOLVED | [Documented]; TLS and rate limits [Not disclosed] | no |
| T54 | RESOLVED | [Documented]; code absence [Not disclosed] | no |
| T55 | RESOLVED | [Documented: repo ...] / [Documented]; conclusion [Inferred] | no |
| T56 | RESOLVED | [Not disclosed] | no |
| T57 | RESOLVED (R015) | [Inferred] | yes (PD4 R2 and PD5 R2 labels) |
| T58 | RESOLVED | [Documented] after rewording | yes (PD1 R2, PD4 R5, PD5 R5, PD6 R5) |
| T59 | RESOLVED | [Documented] | yes (PD3 R1 wording) |
| T60 | RESOLVED | [Inferred] / [Not disclosed] kept | no |
| T61 | RESOLVED | [Documented: repo presidio@2.2.364] | no |
| T63 | RESOLVED | premise [Documented: repo ...]; status [Inferred] | no |
| T65 | RESOLVED | [Documented: repo presidio@037d239f] | no |
| T66 | RESOLVED (proposal) | n/a | no |
| T67 | RESOLVED | [Documented] / [Documented: repo ...] | no |
| T68 | RESOLVED | [Documented] | no |
| T69 | PARTLY RESOLVED | [Documented]; maintenance [Not disclosed] | no |
| T70 | PARTLY RESOLVED | [Documented] (HTTP facts) | no |

## Report

Counts by verdict (47 entries): RESOLVED 38 (including T1 to T5 by rulings, T57 by R015, T66 as a proposal); PARTLY RESOLVED 7 (T7, T9, T14, T24, T35, T69, T70); CORRECTION 2 (T10, T44); STILL OPEN 0 (none of the handled items ended fully open; the residual open parts are named inside the PARTLY entries).

CORRECTION items:
- T10: 0.0.60 is presidio-image-redactor, presidio-structured is 0.0.8, presidio-cli 0.0.9 at 2.2.364; the brief, P0 note and seeds line are wrong, the drafts are right.
- T44: PD5 R4 B:247 says presidio-structured's maturity label is not stated; the getting-started page says "Alpha: This package is currently in alpha ..."; the inventory row is right.
- Also noted as corrections inside other entries: T24 (the headline "default settings" for F2 0.661 was run at threshold 0.4 and its output predates the 2.2.364 tag), T19 (PH_UMID is on the repo copy of the entity page as "Disabled by default" but not on the live page), T13 (score_thresholds is also listed under the 2.2.363 section, not only under unreleased), T38 (INV encrypt key sizes and mask defaults are documented in code).

Summaries that must change (new text in the entries named):
- PD1 R2 (T20/T58), PD1 R5 (T24), PD1 R8 (T7: `Summary: **Key open questions.** No recommended threshold or latency figure, which listed entities are active in a default install, per-entity accuracy, and retention at the Azure Health Data Services endpoint.`, 29 words).
- PD2 R8 (T30).
- PD3 R1 (T59).
- PD4 R2 label only to `[Inferred]` (T57); PD4 R5 (T58).
- PD5 R2 label only to `[Inferred]` (T57); PD5 R5 (T58); PD5 R8 (T3).
- PD6 R5 (T58); PD6 R8 (T13/T47: `Summary: **Key open questions.** REST error codes for a bad regex or language, server-side regex safety under concurrent requests, how request and recognizer thresholds combine in batch calls, and score choices for weak patterns.`, 33 words).
- Optional: PD5 R4 (T44, adds "marked alpha").
- Unchanged: all R1 to R7 Summaries not listed, all PD4 R8 and PD3 R8 Summaries (their questions remain open).

Items still open (not handled here, class b or honest gap): T17, T18, T23, T25, T27, T28, T29, T31, T32, T33, T34, T36, T39, T40, T43, T45, T48, T49, T50, T51, T53, T62, T64. Residual open parts of handled items: GitHub release page and title for 2.2.364 (T9); AHDS retention and region (T7); Stanza model licences (T6); roadmap for authenticated encryption (T35); maintenance status of the OpenAI sample (T69).
