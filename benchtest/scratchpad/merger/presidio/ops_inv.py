"""Inventory edits for presidio (sheet 3f). Imported by merge_presidio.py."""
import re

RP = "[Documented: repo data-privacy-stack/presidio@2.2.364]"
RR = "[Documented: repo data-privacy-stack/presidio-research@0.3.2]"
BLOB = "https://github.com/data-privacy-stack/presidio/blob/2.2.364/"
MS = "https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/"
PD5 = "Presidio: PII detection and anonymisation in structured data (tables and JSON)"
PD6 = "Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers)"
CLASSIFIERS = "the pyproject classifiers (no Development Status classifier in any package at the tag)"


def cov_add(V, blk, key, header, reason):
    old = V.cell_get(blk, key, "Covered by")
    assert header not in old
    V.sub(blk, key, "Covered by", old, old + " ; " + header, reason, kind="covered")


def apply(V):
    # ------------------------------------------------------------------ scope paragraph
    V.para_sub("both owners are recorded and the choice of official source is open for CP1.",
               "both owners are recorded; the sources used are the Data Privacy Stack docs host, GitHub organisation and container registry, plus the Microsoft-authored transition page and docs stub.",
               "T1 (R016): ownership ruled, process wording removed")
    V.para_sub("because the deployed site does not match docs/ at the tag (Python versions differ, see block (d)).",
               "because the deployed site was last published on 2026-07-04 (gh-pages branch, 18 days before the 2.2.364 tag) and differs from docs/ at the tag in places (Python versions, score_thresholds, one entity row; see blocks (a), (b), (d)).",
               "T14")
    V.para_sub("Evaluation-toolkit facts are pinned to data-privacy-stack/presidio-research at the short SHA 0cb36502 (commit 0cb365021884d849c5bc21957de67c91943c1662, 2026-09-30; no release tag was visible in the shallow clone).",
               "Evaluation-toolkit facts are pinned to data-privacy-stack/presidio-research at release tag 0.3.2 (commit 06d2030688ece62f58047e567aecd70e4bb5f104, 2026-08-04).",
               "T11, R014: pin moved from HEAD to the release tag")
    V.para_sub("(commit 06d2030688ece62f58047e567aecd70e4bb5f104, 2026-08-04).",
               "(commit 06d2030688ece62f58047e567aecd70e4bb5f104, 2026-08-04). Licences of third-party components are given in the cells that name them and cite the owner's page, marked \"not Presidio docs\"; those pages were read on 2026-10-09, and Hugging Face model cards also give their last-modified dates.",
               "T6 (R016 item 5, R019, main Q4): third-party licence sources, read date stated")

    V.para_sub("Code facts are read from a shallow clone at tag 2.2.364", "Code facts are read from the repository at tag 2.2.364",
               "style 4: process wording 'shallow clone' removed")
    # ------------------------------------------------------------------ (a) components
    V.para_sub("Versions are the values in each package's pyproject.toml at 2.2.364. The release title \"Release 2.2.364 / 0.0.60\" is not read here, so which package the second number names is checked only against pyproject.toml: 0.0.60 is the presidio-image-redactor version, and presidio-structured is 0.0.8 [Documented: repo data-privacy-stack/presidio@2.2.364] (pyproject.toml of each package).",
               "Versions in the table are the values in each package's pyproject.toml at 2.2.364: presidio-image-redactor 0.0.60, presidio-structured 0.0.8, presidio-cli 0.0.9, and presidio-analyzer, presidio-anonymizer and the presidio meta-package 2.2.364 [Documented: repo data-privacy-stack/presidio@2.2.364] (pyproject.toml of each package).",
               "T10 CORRECTION: the release-title wording (unread, and wrong in the brief) is replaced by the pyproject values")
    # status checked lists (T60)
    V.sub("a", "presidio-analyzer", "Status", "or the pyproject classifiers, while IMG and GSS carry such marks)",
          "or the pyproject classifiers (no Development Status classifier in any package at the tag), while IMG and GSS carry such marks)", "T60: premise confirmed")
    V.sub("a", "presidio-cli", "Status", "(checked README and pyproject; no stable or beta mark)",
          "(checked the README, " + CLASSIFIERS + " and the docs pages; no stable or beta mark)", "T60")
    V.sub("a", "presidio (meta-package)", "Status", "(checked README and pyproject)",
          "(checked the README, " + CLASSIFIERS + " and the docs pages)", "T60")
    V.sub("a", "NLP engine: slim", "Status", "for a slim engine page; none found)",
          "for a slim engine page and " + CLASSIFIERS + "; none found)", "T60")
    V.sub("a", "NLP engine: no-op", "Status", "no page mentions no_op)",
          "no page mentions no_op; " + CLASSIFIERS + ")", "T60")
    # T6 licences
    V.append("a", "presidio-image-redactor", "Default engine", "Tesseract licence Apache-2.0 [Documented] (tesseract-ocr/tesseract LICENSE, not Presidio docs). pytesseract licence Apache-2.0 [Documented] (madmaze/pytesseract LICENSE, not Presidio docs)", "T6 (R016 item 5)")
    V.url_add("a", "presidio-image-redactor", ["https://github.com/tesseract-ocr/tesseract/blob/main/LICENSE", "https://github.com/madmaze/pytesseract/blob/master/LICENSE"], "T6")
    V.append("a", "DICOM image redactor", "Default engine", "pydicom licence MIT-style, with portions outlined in its LICENSE file [Documented] (pydicom/pydicom LICENSE, not Presidio docs)", "T6")
    V.url_add("a", "DICOM image redactor", ["https://github.com/pydicom/pydicom/blob/main/LICENSE"], "T6")
    V.append("a", "NLP engine: spaCy", "Default engine", "spaCy library licence MIT [Documented] (explosion/spaCy LICENSE, not Presidio docs). Model en_core_web_lg 3.8.0 licence MIT; its listed OntoNotes 5 source is \"commercial (licensed by Explosion)\" [Documented] (explosion/spacy-models meta file, not Presidio docs)", "T6")
    V.url_add("a", "NLP engine: spaCy", ["https://github.com/explosion/spaCy/blob/master/LICENSE", "https://github.com/explosion/spacy-models/blob/master/meta/en_core_web_lg-3.8.0.json"], "T6")
    V.sub("a", "NLP engine: Stanza", "Default engine", "Extra install: pip install \"presidio_analyzer[stanza]\" [Documented] (INST)",
          "Extra install: presidio_analyzer with the stanza extra [Documented] (INST)", "hygiene: pip-extra brackets removed from the cell", kind="hygiene")
    V.append("a", "NLP engine: Stanza", "Default engine", "Stanza library licence Apache-2.0 [Documented] (stanfordnlp/stanza LICENSE, not Presidio docs). Stanza model licences [To be verified] (not read)", "T6")
    V.url_add("a", "NLP engine: Stanza", ["https://github.com/stanfordnlp/stanza/blob/main/LICENSE"], "T6")
    V.sub("a", "NLP engine: transformers", "Default engine", "Extra install: pip install \"presidio_analyzer[transformers]\" [Documented] (INST)",
          "Extra install: presidio_analyzer with the transformers extra [Documented] (INST)", "hygiene: pip-extra brackets removed from the cell", kind="hygiene")
    V.append("a", "NLP engine: transformers", "Default engine", "transformers library licence Apache-2.0 [Documented] (huggingface/transformers LICENSE, not Presidio docs). Sample model StanfordAIMI/stanford-deidentifier-base licence MIT [Documented] (Hugging Face model card, last modified 2024-10-09, not Presidio docs)", "T6")
    V.url_add("a", "NLP engine: transformers", ["https://github.com/huggingface/transformers/blob/main/LICENSE", "https://huggingface.co/StanfordAIMI/stanford-deidentifier-base"], "T6")
    # no-op row (T9, T13)
    V.sub("a", "NLP engine: no-op", "Version read", "CHANGELOG.md lists it under [unreleased] ", "CHANGELOG.md lists it under its unreleased heading ",
          "T13, hygiene: no bracketed non-label", kind="hygiene")
    V.sub("a", "NLP engine: no-op", "Version read", "whether the GitHub 2.2.364 release notes name it was not readable here [To be verified]",
          "the GitHub 2.2.364 release notes were not read [To be verified]", "T9 (main Q1), style 4: process wording removed")
    # presidio-research (T11, T6, T60)
    old_ver = V.cell_get("a", "presidio-research", "Version read")
    assert old_ver == "0.3.2 [Documented: repo data-privacy-stack/presidio-research@0cb36502] (pyproject.toml:3) at commit 0cb36502. Latest release tag not determined [To be verified] (the shallow clone showed no tags; github.com release pages returned 403)", old_ver
    V.sub("a", "presidio-research", "Version read", old_ver,
          "0.3.2 " + RR + " (pyproject.toml:3), tag 0.3.2 is the highest tag " + RR, "T11: pinned to the release tag; the [To be verified] latest-tag item is answered")
    V.sub("a", "presidio-research", "Status",
          "Not stated [Not disclosed] (checked README, pyproject, CHANGELOG; no stable or beta mark; CHANGELOG has an Unreleased section)",
          "Not stated [Not disclosed] (checked the README, " + CLASSIFIERS + ", the CHANGELOG and the docs pages; no stable or beta mark; the CHANGELOG at the tag has an empty Unreleased heading)",
          "T11, T60")
    V.sub("a", "presidio-research", "Default engine", ">=3.11,<3.15 [Documented: repo data-privacy-stack/presidio-research@0cb36502] (pyproject.toml:7)",
          ">=3.11,<3.14 " + RR + " (pyproject.toml:7)", "T11: requires-python at the tag")
    n = V.cell_get("a", "presidio-research", "Default engine").count("presidio-research@0cb36502")
    V.sub("a", "presidio-research", "Default engine", "presidio-research@0cb36502", "presidio-research@0.3.2",
          "T11: remaining repo labels re-pinned to tag 0.3.2", kind="pin", count=n)
    V.sub("a", "presidio-research", "Package or repo", "presidio-research@0cb36502", "presidio-research@0.3.2", "T11", kind="pin")
    V.sub("a", "presidio-research", "Purpose", "presidio-research@0cb36502", "presidio-research@0.3.2", "T11", kind="pin",
          count=V.cell_get("a", "presidio-research", "Purpose").count("presidio-research@0cb36502"))
    V.sub("a", "presidio-research", "Source URL", "/blob/0cb365021884d849c5bc21957de67c91943c1662/README.md", "/blob/0.3.2/README.md", "T11, T70: URL re-pinned", kind="pin")
    V.sub("a", "presidio-research", "Source URL", "/blob/0cb365021884d849c5bc21957de67c91943c1662/pyproject.toml", "/blob/0.3.2/pyproject.toml", "T11, T70: URL re-pinned", kind="pin")
    V.append("a", "presidio-research", "Default engine", "Notebook 5 uses the model OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1, licence Apache-2.0 [Documented] (Hugging Face model card, last modified 2026-01-13, not Presidio docs)", "T6")
    V.url_add("a", "presidio-research", ["https://huggingface.co/OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1"], "T6")
    # legacy V1 (T65)
    V.sub("a", "Legacy V1", "Version read", "Branch V1 contents not read [To be verified]",
          "Branch V1 head 037d239f (2021-02-28) has VERSION 0.95 and a README marked \"DEPRECATED\" that names PyPI presidio-analyzer==0.95 and Docker tag v1 [Documented: repo data-privacy-stack/presidio@037d239f] (VERSION; README.MD)",
          "T65: branch read")
    V.url_add("a", "Legacy V1", [BLOB.replace("2.2.364", "037d239f819271da57b9ff0e1eb4f84b2f1da6f5") + "README.MD"], "T65")

    # ------------------------------------------------------------------ (b) recognizers
    V.para_sub("(SUP page text searched for \"disabled\" and \"enabled\"; none found).",
               "(SUP page text searched for \"disabled\" and \"enabled\"; none found). docs/supported_entities.md at the tag marks only PH_UMID as \"Disabled by default\" [Documented: repo data-privacy-stack/presidio@2.2.364] (docs/supported_entities.md:161).",
               "T19")
    # T61 extras
    V.sub("b", "Global financial identifiers", "Extra install", "None beyond presidio-analyzer [Inferred] (premise: regex recognizers with validation code; no extra in pyproject.toml optional-dependencies names them)",
          "regex is a core dependency used by IbanRecognizer " + RP + " (pyproject.toml:31; generic/iban_recognizer.py)", "T61: premise checked by an import scan")
    V.append("b", "Global contact and network identifiers", "Extra install", "tldextract is a core dependency used by EmailRecognizer " + RP + " (pyproject.toml:32)", "T61")
    V.sub("b", "Spain:", "Extra install", "None [Inferred] (premise: regex recognizers in the core package)",
          "regex is a core dependency used by EsPassportRecognizer " + RP + " (pyproject.toml:31; country_specific/spain/es_passport_recognizer.py)", "T61")
    none_new = "None; imports are standard library and presidio_analyzer only " + RP + " (import scan of the recognizer folder)"
    for key in ["Global date pattern", "Medical licence", "USA:", "UK:", "Italy:", "Poland:", "Singapore:", "Australia:", "India:", "Finland:",
                "Korea:", "Nigeria:", "Philippines:", "Canada:", "Sweden:", "South Africa:", "Thailand:", "Turkey:", "Germany:"]:
        cur = V.cell_get("b", key, "Extra install")
        assert re.fullmatch(r"None \[Inferred\] \(premise: regex recognizers? in the core package\)", cur), (key, cur)
        V.sub("b", key, "Extra install", cur, none_new, "T61: premise checked by an import scan")
    # T21
    V.sub("b", "Medical licence", "Enabled by default", "recognizer_registry/recognizer_registry.py:128-139", "recognizer_registry/recognizer_registry.py:137-138",
          "T21: line cite of the documented premise corrected")
    # T19 / T13 Philippines
    V.sub("b", "Philippines:", "Entities", "PH_UMID, which SUP does not list [Documented: repo data-privacy-stack/presidio@2.2.364] (country_specific/philippines/ph_umid_recognizer.py:42)",
          "PH_UMID, which the live SUP page does not list but docs/supported_entities.md lists with \"Disabled by default\" " + RP + " (docs/supported_entities.md:161; country_specific/philippines/ph_umid_recognizer.py:42)", "T19")
    V.sub("b", "Philippines:", "Enabled by default", "CHANGELOG.md says PhUmidRecognizer", "CHANGELOG.md under its unreleased heading says PhUmidRecognizer", "T13")
    V.url_add("b", "Philippines:", [BLOB + "docs/supported_entities.md"], "T19")
    # T70: directory links /blob/ -> /tree/
    pat = re.compile(r"https://github\.com/data-privacy-stack/presidio/blob/(2\.2\.364/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific/[a-z_]+/)(?= ;|$)")
    done = 0
    for key in ["USA:", "UK:", "Spain:", "Italy:", "Singapore:", "Australia:", "India:", "Korea:", "Nigeria:", "Philippines:", "Sweden:", "Turkey:", "Germany:"]:
        cur = V.cell_get("b", key, "Source URL")
        m = pat.search(cur)
        assert m, key
        V.sub("b", key, "Source URL", m.group(0), m.group(0).replace("/blob/", "/tree/"), "T70 (main Q5): directory link /blob/ to /tree/", kind="url")
        done += 1
    assert done == 13
    # T6 licences, T7, T8, hygiene
    V.append("b", "MedicalNERRecognizer", "Extra install", "Model licence MIT [Documented] (blaze999/Medical-NER model card, last modified 2024-04-08, not Presidio docs)", "T6")
    V.url_add("b", "MedicalNERRecognizer", ["https://huggingface.co/blaze999/Medical-NER"], "T6")
    V.sub("b", "GLiNERRecognizer", "Detection method", "The GLN page names the model's licence as Apache 2.0 (Presidio docs, not GLiNER docs) [Documented] (GLN)",
          "The GLN page names the model's licence as Apache 2.0 [Documented] (GLN, Presidio docs, not GLiNER docs). Model licence Apache-2.0 [Documented] (urchade/gliner_multi_pii-v1 model card, last modified 2024-04-20, not Presidio docs). GLiNER library licence Apache-2.0 [Documented] (urchade/GLiNER LICENSE, not Presidio docs)",
          "T6, hygiene: hint moved after the label; owner licence pages added")
    V.sub("b", "GLiNERRecognizer", "Languages", "The model is described as multi PII (Presidio docs, not GLiNER docs) [Documented] (GLN)",
          "The model is described as multi PII [Documented] (GLN, Presidio docs, not GLiNER docs)", "hygiene: hint moved after the label", kind="hygiene")
    V.url_add("b", "GLiNERRecognizer", ["https://huggingface.co/urchade/gliner_multi_pii-v1", "https://github.com/urchade/GLiNER/blob/main/LICENSE"], "T6")
    V.append("b", "BasicLangExtractRecognizer", "Extra install", "LangExtract licence Apache-2.0 [Documented] (google/langextract LICENSE, not Presidio docs). Ollama licence MIT [Documented] (ollama/ollama LICENSE, not Presidio docs). The Ollama library page for Qwen2.5 says \"all models except the 3B and 72B are released under the Apache 2.0 license\" [Documented] (ollama.com/library/qwen2.5:1.5b, not Presidio docs). The shipped 1.5B model is therefore under Apache 2.0 [Inferred] (premise: the quoted sentence and the model id qwen2.5:1.5b)",
             "T6; label split: the page's rule is [Documented], its application to the shipped 1.5B model is a deduction")
    V.url_add("b", "BasicLangExtractRecognizer", ["https://github.com/google/langextract/blob/main/LICENSE", "https://github.com/ollama/ollama/blob/main/LICENSE", "https://ollama.com/library/qwen2.5:1.5b"], "T6")
    V.append("b", "AzureOpenAILangExtractRecognizer", "Extra install",
             "The code passes the text to LangExtract: \"text_or_documents\": kwargs.pop(\"text\") and a call to lx.extract " + RP + " (predefined_recognizers/third_party/langextract_recognizer.py:161,172). The text therefore leaves the local process for the configured Azure endpoint [Inferred] (premise: the Azure OpenAI client class AzureOpenAILanguageModel is built from an endpoint, azure_openai_provider.py:33,99)",
             "T8")
    V.append("b", "AzureOpenAILangExtractRecognizer", "Extra install",
             "Azure OpenAI processes prompts and responses within the customer-specified geography unless a Global or DataZone deployment type is used, and the models are stateless [Documented] (Microsoft docs, not Presidio docs)", "T7")
    V.url_add("b", "AzureOpenAILangExtractRecognizer", [BLOB + "presidio-analyzer/presidio_analyzer/predefined_recognizers/third_party/langextract_recognizer.py", MS + "openai/data-privacy"], "T7, T8")
    V.sub("b", "AzureAILanguageRecognizer", "Extra install", "azure-ai-language extra [Documented] (AAL: pip install \"presidio-analyzer[azure-ai-language]\")",
          "azure-ai-language extra [Documented] (AAL)", "hygiene: pip-extra brackets removed from the cell", kind="hygiene")
    V.sub("b", "AzureAILanguageRecognizer", "Extra install", "The text leaves the local process for the Azure endpoint [Inferred] (premise: RemoteRecognizer with a TextAnalyticsClient to a configured endpoint)",
          "The code passes the text to TextAnalyticsClient.recognize_pii_entities " + RP + " (azure_ai_language.py:121-123). The text therefore leaves the local process for the configured endpoint [Inferred] (premise: the client is built from the endpoint)",
          "T8: code call documented, conclusion kept as [Inferred]")
    V.append("b", "AzureAILanguageRecognizer", "Extra install", "Azure Language may temporarily store data sent in calls for up to 48 hours and does not store or process customer data outside the deployment region [Documented] (Microsoft docs, not Presidio docs)", "T7")
    V.url_add("b", "AzureAILanguageRecognizer", [MS + "language-service/data-privacy"], "T7")
    V.sub("b", "AzureHealthDeidRecognizer", "Extra install", "ahds extra (pip install presidio-analyzer[ahds]) and the AHDS_ENDPOINT environment variable",
          "ahds extra of presidio-analyzer and the AHDS_ENDPOINT environment variable", "hygiene: pip-extra brackets removed from the cell", kind="hygiene")
    V.append("b", "AzureHealthDeidRecognizer", "Extra install",
             "The code passes the text to deid_client.deidentify_text " + RP + " (predefined_recognizers/third_party/ahds_recognizer.py:113-117). The text therefore leaves the local process for the configured endpoint [Inferred] (premise: the client is built from the endpoint)", "T8")
    V.append("b", "AzureHealthDeidRecognizer", "Extra install",
             "Retention and region of data sent to the AHDS de-identification service [Not disclosed] (checked the Presidio AHDS page and the Microsoft AHDS overview page)", "T7")
    V.url_add("b", "AzureHealthDeidRecognizer", ["https://learn.microsoft.com/en-us/azure/healthcare-apis/deidentification/overview"], "T7")

    # ------------------------------------------------------------------ (c) operators
    for name in ["replace", "redact", "hash", "mask", "custom", "keep", "encrypt"]:
        hdr, rows = V.table("c")
        hit = [i for i in rows if V.split(V.lines[i])[0] == name]
        assert len(hit) == 1, name
        old = V.split(V.lines[hit[0]])[hdr.index("Covered by Table 3 column")]
        V.sub("c", name, "Covered by", old, old + " ; " + PD5,
              "T66 (main Q2): PD5 R4 cites the factory operator list and R7 tests this operator; decrypt, deanonymize_keep and surrogate_ahds not added (PD5 hardcodes the Anonymize type; the surrogate needs an extra)", kind="covered")
    V.sub("c", "mask", "Default behaviour", "No default values are stated for the three parameters [Not disclosed] (checked ANON and operators/mask.py)",
          "All three parameters are required and have no default; a missing one raises InvalidParamError \"Expected parameter ...\" " + RP + " (operators/mask.py:47,53-54; services/validators.py:53-54). The ANON page states no defaults for them [Not disclosed] (checked ANON)",
          "T38: code fact documented; the docs absence kept separately")
    V.url_add("c", "mask", [BLOB + "presidio-anonymizer/presidio_anonymizer/services/validators.py"], "T38")
    V.sub("c", "encrypt", "Default behaviour", "Key-size values [To be verified] (the allowed sizes come from the cryptography library, not read)",
          "Key size must be 128, 192 or 256 bits (error text \"must be of length 128, 192 or 256 bits\") " + RP + " (operators/encrypt.py:41-49; operators/aes_cipher.py:50-57)",
          "T38: [To be verified] closed from code")
    V.sub("c", "surrogate_ahds", "Install or dependency", "Extra: pip install presidio-anonymizer[ahds] [Documented] (ANON)",
          "Extra: the ahds extra of presidio-anonymizer [Documented] (ANON)", "hygiene: pip-extra brackets removed from the cell", kind="hygiene")
    V.append("c", "surrogate_ahds", "Install or dependency",
             "The code passes the text to client.deidentify_text " + RP + " (operators/ahds_surrogate.py:270-277). The text therefore leaves the local process for the configured endpoint [Inferred] (premise: the client is built from the endpoint)", "T8")
    V.append("c", "surrogate_ahds", "Install or dependency",
             "Retention and region of data sent to the AHDS de-identification service [Not disclosed] (checked the Presidio AHDS page and the Microsoft AHDS overview page)", "T7")
    V.url_add("c", "surrogate_ahds", ["https://learn.microsoft.com/en-us/azure/healthcare-apis/deidentification/overview"], "T7")

    # ------------------------------------------------------------------ (d) integration paths
    V.para_sub("[Inferred] (premise: the pages sit under Samples in the mkdocs nav).",
               "[Inferred] (premise: the pages sit under Samples > Deployment in mkdocs.yml:85,120-128 [Documented: repo data-privacy-stack/presidio@2.2.364]).", "T63")
    V.append("d", "Docker images", "Caveats", "The INST page also shows a local build tag presidio/presidio-anonymizer mapped to 5001:5001 [Documented] (INST)", "T16")
    cov_add(V, "d", "Docker images", PD6, "T66 (main Q2): PD6 R7 cites running the Analyzer image with ad_hoc_recognizers")
    V.sub("d", "Kubernetes", "Status", "Sample [Inferred] (premise: lives under Samples in the nav)",
          "Sample [Inferred] (premise: the page sits under Samples > Deployment in mkdocs.yml:85,120-128 [Documented: repo data-privacy-stack/presidio@2.2.364])", "T63")
    V.append("d", "Kubernetes", "Caveats", "Ingress by default; TLS not mentioned [Not disclosed] (checked K8S)", "T52")
    V.url_add("d", "Kubernetes", [BLOB + "mkdocs.yml"], "T63")
    V.sub("d", "Azure App Service", "Status", "Sample [Inferred] (premise: under Samples in the nav)",
          "Sample [Inferred] (premise: the page sits under Samples > Deployment in mkdocs.yml:85,120-128 [Documented: repo data-privacy-stack/presidio@2.2.364])", "T63")
    V.append("d", "Azure App Service", "Caveats", "IP-range access restriction script [Documented] (APPSVC)", "T52")
    V.url_add("d", "Azure App Service", [BLOB + "mkdocs.yml"], "T63")
    V.sub("d", "Spark and Microsoft Fabric", "Status", "Sample [Inferred] (premise: under Samples in the nav)",
          "Sample [Inferred] (premise: the pages sit under Samples > Deployment in mkdocs.yml:85,120-128 [Documented: repo data-privacy-stack/presidio@2.2.364])", "T63")
    V.url_add("d", "Spark and Microsoft Fabric", [BLOB + "mkdocs.yml"], "T63")
    V.sub("d", "Azure Data Factory", "Status", "Sample [Inferred] (premise: under Samples in the nav)",
          "Sample [Inferred] (premise: the pages sit under Samples > Deployment in mkdocs.yml:85,120-128 [Documented: repo data-privacy-stack/presidio@2.2.364])", "T63")
    V.url_add("d", "Azure Data Factory", [BLOB + "mkdocs.yml"], "T63")
    V.sub("d", "Batch engines", "Status",
          "the 2.2.364 release notes and CHANGELOG [unreleased] mention it, but the release page was not readable here [To be verified]",
          "the CHANGELOG lists it under its unreleased heading " + RP + " (CHANGELOG.md:38); the GitHub release notes were not read [To be verified]",
          "T9 (main Q1), T13, style 4: CHANGELOG at the tag is the substitute; no bracketed non-label; no process wording")
