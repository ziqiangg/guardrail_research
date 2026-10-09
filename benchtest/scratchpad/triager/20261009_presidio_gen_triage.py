#!/usr/bin/env python
"""Generates benchtest/drafts/presidio_triage.md from the item list below.
Triager scratch script (no research; reads nothing but its own data). Run from repo root:
  python benchtest/scratchpad/triager/20261009_presidio_gen_triage.py
"""
import collections
import re
import sys

OUT = "benchtest/drafts/presidio_triage.md"

# (key, group, item, locations, class, source/why, priority, files)
# files: subset of A (cols_a), B (cols_b), I (inventory), R (brief/rulings/other)
ITEMS = []


def add(key, grp, item, loc, cls, src, pri, files):
    ITEMS.append(dict(key=key, grp=grp, item=item, loc=loc, cls=cls, src=src, pri=pri, files=files))


G1 = "Decisions, scope, licensing"
G2 = "Pins, releases, provenance"
G3 = "Default configuration and entity coverage"
G4 = "Published numbers (thresholds, accuracy, latency)"
G5 = "Anonymizer and Deanonymizer"
G6 = "Image Redactor"
G7 = "presidio-structured"
G8 = "Custom recognizers"
G9 = "REST service, security, limits"
G10 = "Summary labels and entailment"
G11 = "Inventory only"
G12 = "Other"

# ---------------------------------------------------------------- G1
add("q01", G1,
    "[CP1] Q01 ownership. Treat data-privacy-stack (docs host, repo, GHCR) as the official source and fix the prefix "
    "Presidio:. The transition page says the project is moving from Microsoft ownership; the microsoft.github.io root is a "
    "redirect stub; github.com/microsoft/presidio answers 301 (P0). CLAUDE.md rule 1 asks for a ruling when the old official "
    "site states the transfer, and on its face it does. The FAQ says Presidio 'has since transitioned' while the transition "
    "page says 'in the process of transitioning'.",
    "BR Scope and Official sources; PD1 R4 (A:88-89), R8 (A:171); PD2 R4 (A:308), R8 (A:360); PD3 R4 (A:452), R8 (A:504); "
    "PD4 R4 (B:74-75); PD5 R4 (B:250-251); PD6 R4 (B:400); INV scope note, INV-RN 1(v); R4 Summaries of PD1 to PD6 "
    "(ownership move); the prefix in every header",
    "c",
    "User ruling at CP1 (ownership and licensing judgement). Evidence already read: transition page, stub text, 301 header, "
    "LICENSE (MIT, Copyright Presidio Contributors). After the ruling: record it in the CLAUDE.md Products row (it already says 'decided at CP1') and seeds, and drop "
    "the Q01 bullets from PD1 to PD3 R8 (they are process items, absent from PD4 to PD6 R8)",
    "H", "ABIR")

add("q02a", G1,
    "[CP1] Q02a column split: keep six columns, or merge to four (PD3 into PD2, PD6 into PD1). Facts for the decision: PD3 "
    "has its own mechanics (AES-CBC, token offsets, key handling, LiteLLM restore); PD6 shares request fields and result "
    "fields with PD1 (R5, R6).",
    "BR Scope and Open user questions; all rows of PD1, PD2, PD3, PD6; A RN-10(1), A RN-11",
    "b (CP1 decision)",
    "User decision at CP1 (closes when chosen, as NeMo b22). If merged, the merger combines Detail bullets and the PD1 and "
    "PD2 Summaries are rewritten",
    "H", "ABR")

add("q02b", G1,
    "[CP1] Q02b PD5 presidio-structured: Table 3 column or inventory only. For: it reuses the Analyzer and Anonymizer on "
    "JSON and tables that can sit on the data path, and adds per-column majority-vote mapping and JSON key context. "
    "Against: Python package only (no REST route, Docker image or CLI at the tag), no docs page ties it to LLM traffic, "
    "whole-cell replacement, alpha maturity (see {maturity}).",
    "BR Scope; PD5 R3 Summary and (B:218, 222, 225), R8 (B:295, 305); B RN-10; INV(a) row 15",
    "b (CP1 decision)",
    "User decision at CP1. PD5 R3 Summary is [Inferred] and says the package 'fits retrieved records and tool outputs'; that "
    "sentence goes if PD5 becomes inventory only",
    "H", "BIR")

add("q02c", G1,
    "[CP1] Q02c inventory granularity: recognizer-family rows (31 now, main accepted 14/31/10/14) or a per-entity catalogue "
    "(about 80 rows by the live page count, not about 120 as the brief estimated; see {entcount}).",
    "BR Open user questions; INV scope, INV-RN 9; A RN-5(5)",
    "b (CP1 decision)",
    "User decision at CP1; P8 needs an inventory config with fixed row counts, so this must close before the merge",
    "M", "AIR")

add("r010", G1,
    "R010 check: presidio-research stays an inventory row, not an evaluation-tooling sheet. It carries the only published "
    "figures (notebooks 4 and 5) and the R7 route of PD1 to PD3 and PD6.",
    "PD1 R5 (A:104-114), R7 (A:152-155); PD2 R7 (A:346); PD6 R7 (B:442-444); INV(a) row 23",
    "b (CP1 decision)",
    "FYI only. R010 turns this into a user question only if evidence needs sheet-level treatment; the drafts show none (no "
    "table, JSON, image or Anonymizer evaluator found; PD4 to PD6 did not read the repo, see {rsread})",
    "L", "ABIR")

add("complic", G1,
    "(suggested, not open in the drafts) Licences of third-party components a bench must download: spaCy en_core_web_lg, "
    "Tesseract and pytesseract, blaze999/Medical-NER, urchade/gliner_multi_pii-v1 (Apache 2.0 stated only on the GLiNER "
    "sample page), StanfordAIMI/stanford-deidentifier-base, the OpenMed model in notebook 5, the Ollama model in the shipped "
    "LangExtract config. The drafts state the MIT licence of Presidio itself only.",
    "PD1 R4 (A:64-72, 86-87), R5 (A:109); PD4 R4 (B:55-57, 76-77); INV(a) rows 18-20; INV(b) rows 55-59",
    "c",
    "Model cards and tool licences are third-party (not Presidio official sources). CP1 question: does the sheet carry "
    "component licences at all? If yes, cite each owner's page in plain text 'not Presidio docs'",
    "M", "ABI")

add("azureterms", G1,
    "Azure-hosted pieces (AHDS recognizer and surrogate operator, Azure AI Language recognizer, Azure OpenAI LangExtract "
    "recognizer, Document Intelligence OCR): retention, regions and data-handling terms. Presidio pages say only that an "
    "endpoint is needed.",
    "PD1 R6 (A:132-137), R8 (A:167); PD2 R6 (A:331), R8 (A:356); PD4 R4 (B:59), R8 (B:141); INV(b) rows 59-61; INV(c) row 76",
    "c",
    "Terms of Microsoft services: honest gap on the Presidio side. If wanted, cite Microsoft's own service pages as 'not "
    "Presidio docs' (R007 item 1 precedent: AWS docs for AWS semantics). The code-side half (what is sent) is {azureflow}",
    "M", "ABI")

add("azureflow", G1,
    "What leaves the process for the Azure recognizers and operators: the code sends text (or image bytes for Document Intelligence) to "
    "the configured endpoint. PD1 R6 states it as [Inferred] from endpoint and key parameters; PD4 R4 shows the call for OCR.",
    "PD1 R6 (A:132-137); PD2 R8 (A:356); PD4 R4 (B:59); INV(b) rows 59-61; INV(c) row 76",
    "a", "Read azure_ai_language.py, ahds_recognizer.py, azure_openai_provider.py, ahds_surrogate.py at the tag and quote the call that takes the text; "
    "upgrade the Inferred bullet. Terms side is {azureterms}",
    "M", "AB")

# ---------------------------------------------------------------- G2
add("relnotes", G2,
    "Release 2.2.364 on GitHub: is it the latest release, what is its exact title ('Release 2.2.364 / 0.0.60'), and what do "
    "its notes say (batch deanonymisation, no-op NLP engine, Python 3.14 compatibility, CLI threshold flag)? The release page "
    "could not be read in P1 or P2 (github.com 403, MCP scoped to this repo).",
    "PD1 R4 (A:81 TBV), R8 (A:170); PD2 R8 (A:359); PD3 R4 (A:443 TBV), R8 (A:501); PD4 R8 (B:143); PD5 R8 (B:306); PD6 R8 "
    "(B:452); A RN-4; B RN-3; INV(a) row 22 (TBV); INV(d) row 98 (TBV); INV-RN 2, 3; queue (routed to P5 via triage)",
    "a",
    "Latest tag: git ls-remote --tags on data-privacy-stack/presidio (queue hint). Release body: ask main to attach the repo "
    "(add_repo) and use get_latest_release or get_release_by_tag; the P0 note S19 already holds the verbatim JSON text "
    "(hint only). If still unreadable the TBV labels stay and no release-note fact may be used. 2.2.364 is the pin of "
    "every repo label",
    "H", "ABIR")

add("sixty", G2,
    "Which package the number 0.0.60 belongs to. Brief, P0 note and queue read the title as 'presidio-structured 0.0.60'; "
    "pyproject files at the tag say image-redactor 0.0.60, structured 0.0.8, cli 0.0.9. Only the title wording itself is "
    "unread.",
    "BR; B RN-4(1); PD4 R4 (B:65); PD5 R4 Summary and (B:229); INV(a) rows 13-17 and block note; INV-RN 2",
    "a",
    "CORRECTION already supported by pyproject.toml at the tag; confirm the title text with {relnotes}. Main to correct "
    "the P0 note and seeds line. PD5 R4 Summary ('version 0.0.8') is consistent with the code",
    "M", "BIR")

add("rpin", G2,
    "presidio-research pin: PD1 to PD3 cite tag 0.3.2 (06d20306, 2026-08-04); the inventory cites short SHA 0cb36502 (HEAD, "
    "2026-09-30) for 7 labels, says 'no tags visible' and 'latest release not determined'. A RN-3 says tags up to 0.3.2 "
    "exist and that notebook 5 and pyproject differ between 0.3.2 and HEAD (requires-python >=3.11,<3.14 at 0.3.2 vs "
    "<3.15 at HEAD). R014 requires the release-tag pin.",
    "PD1 R2 (A:26), R5 Summary and (A:104, 108-114), R7 (A:153-155); PD2 R5 (A:320); A RN-3; INV scope note, INV(a) row 23, "
    "INV-RN 5; queue",
    "a",
    "git ls-remote --tags on data-privacy-stack/presidio-research (queue hint); re-pin the inventory row to the tag, then "
    "re-read version, requires-python and README at that tag. Also settles whether a later tag than 0.3.2 exists. The "
    "figures in the PD1 R5 Summary are pinned to the headline source",
    "H", "AIR")

add("rsread", G2,
    "presidio-research read status is inconsistent: PD4 R7, PD5 R7 and PD6 R7 say its README, tag and data format were not "
    "read (403) and carry TBV, while PD1 to PD3 read it by shallow clone. PD2 R5 and PD3 R7 make scope claims about it "
    "('no Anonymizer evaluator', 'no reversibility test') pinned to 0.3.2.",
    "PD4 R7 (B:126); PD5 R7 (B:290); PD6 R7 (B:444); B RN-3; PD2 R5 (A:320); PD3 R7 (A:491); A RN-3",
    "a",
    "Read presidio-research at the tag from {rpin}: README, docs/evaluation.md, data generator, evaluator modules; look for "
    "table, JSON, image or OCR modes and for any Anonymizer test. Replace the three TBV bullets, re-check the two scope "
    "absences",
    "M", "ABR")

add("unrel", G2,
    "Features present in the 2.2.364 code but listed under CHANGELOG.md [unreleased]: NoOpNlpEngine, per-recognizer "
    "score_thresholds, BatchDeanonymizeEngine, PhUmidRecognizer, the GB phone-region fix. The live registry and Python API "
    "pages do not mention score_thresholds; the tagged docs do.",
    "PD1 R4 (A:82); PD3 R4 (A:441-442); PD6 R4 (B:395-398), R8 (B:452, 457); INV(a) row 22; INV(b) row 48; INV(d) row 98; "
    "INV-RN 3",
    "a",
    "Release notes ({relnotes}); docs deploy lag ({docspin}); git log of CHANGELOG.md between 2.2.363 and 2.2.364. Both "
    "sides are already written as two bullets; the question is only whether the CHANGELOG heading is stale",
    "M", "ABI")

add("docspin", G2,
    "The deployed docs site cannot be tied to a commit: it differs from docs/ at the tag (Python 3.10 to 3.13 live, 3.14 at "
    "the tag), so every site fact is an unpinned [Documented] read on 2026-10-09.",
    "BR Official sources; INV scope note; every '(Presidio docs, ... read 2026-10-09)' bullet",
    "a",
    "Docs deploy workflow under .github/workflows and mkdocs.yml (which branch builds the site); compare docs/installation.md "
    "and 2 or 3 distinctive passages on that branch (README section 3 rule 8; R007 item 7). Pin only if they match",
    "M", "ABIR")

add("pyver", G2,
    "Python versions are stated four ways: live installation page 3.10 to 3.13; docs/installation.md at the tag 3.10 to "
    "3.14; pyproject requires-python >=3.10,<3.15; presidio-cli README 3.10 to 3.13 vs its classifiers 3.10 to 3.14; "
    "release note says 3.14 compatibility was added.",
    "PD1 R4 (A:83-85); PD2 R4 (A:305-306); PD3 R4 (A:449-450); PD4 R4 (B:66-67); PD5 R4 (B:248-249); INV(a) rows 11-13, 15, 16; "
    "INV(d) row 87; INV-RN 1(ii)",
    "a",
    "Likely explained by docs lag ({docspin}) and the release notes ({relnotes}); keep one bullet per source, do not pick "
    "(README rule 4)",
    "M", "ABI")

add("dockername", G2,
    "Docker image names: analyzer and anonymizer pages show local build names (presidio-analyzer), the installation page shows "
    "ghcr.io names; stale mcr.microsoft.com references may remain on other pages.",
    "PD1 R4 (A:74-76); PD2 R4 (A:296-297); INV(d) row 88; INV-RN 1(iii)",
    "a",
    "grep docs/ at the tag and the live pages for mcr.microsoft.com and docker run; transition and installation pages",
    "L", "AI")

add("ghcr", G2,
    "Do the GHCR images exist with a tag matching 2.2.364 (INV says 'current for 2.2.364 [Inferred]', no image pulled), and which "
    "Tesseract version does the image-redactor image contain (docs: tested v5.2.0; Dockerfile has no pin)?",
    "PD4 R4 (B:57-58 ND), R8 (B:137); INV(d) row 88; PD1 R4 (A:74)",
    "b",
    "Registry manifest or image pull plus tesseract -v inside the container. Pulling images is outside the read-only rule "
    "(queue note), so it needs CP1 consent ({localrun})",
    "M", "ABI")

# ---------------------------------------------------------------- G3
add("active", G3,
    "Which recognizers and entities are actually active in a default English install. PD1 R2 Summary says '16 pattern "
    "recognizers plus a spaCy model'; the YAML has 24 enabled entries but the English-only registry drops ES, IT and PL "
    "ones (Inferred from loader code); a notebook output of unknown Presidio version shows 19 entities and 17 recognizers; "
    "SG_UEN, FI_PERSONAL_IDENTITY_CODE, KR_PASSPORT and ABA_ROUTING_NUMBER have no YAML entry.",
    "PD1 R2 Summary and (A:23-29), R7 (A:150), R8 (A:165); INV(b) intro (line 28), rows 37, 39-42, 45, 46; INV-RN 1(i), 4; "
    "A RN-5(3)(4), A RN-7(a); queue (Docker test of /supportedentities)",
    "b",
    "Run the 2.2.364 Analyzer: get_supported_entities() and the loaded recognizer list (pip works, no image needed), or GET "
    "/supportedentities?language=en and GET /recognizers on the GHCR image. Code reading (recognizers_loader_utils.py:171-183, "
    "407-413) already gives the Inferred answer. Needs CP1 consent ({localrun})",
    "H", "ABIR")

add("sup_vs_yaml", G3,
    "Source conflict: the supported-entities page lists entities that default_recognizers.yaml disables (SG_NRIC_FIN, UK_*, AU_*, "
    "IN_*, KR_*, DE_*) with no default-off note, lists three entities with no YAML entry, and omits entities that the YAML or "
    "code has (PH_UMID, ABA_ROUTING_NUMBER, DE_LANR, DE_BSNR, DE_VAT_ID, DE_FUEHRERSCHEIN). No entity type for secrets "
    "(API keys, passwords) is recorded as [Not disclosed].",
    "PD1 R2 (A:28-29, 39); INV(b) intro and rows 37, 38, 42, 44-46, 48, 54; INV-RN 1(i)",
    "a",
    "Re-read the supported-entities page, /analyzer/recognizer_registry_provider/ and /analyzer/filtering_by_country/ for any "
    "default-enabled statement; docs/supported_entities.md at the tag. Both sides are already written (README rule 4); the "
    "runtime answer is {active}",
    "M", "AI")

add("entcount", G3,
    "Entity-row count: the live supported-entities page has 80 rows, docs/supported_entities.md at the tag has 81 "
    "(unreconciled), the brief estimated about 120. The PD1 R2 Summary says 'about 80 types' and a Detail bullet gives the "
    "count as [Documented] although it is our own count.",
    "PD1 R2 Summary and (A:18); A RN-5(5); BR Inventory and Open questions; INV(b) intro",
    "a",
    "Diff the live page text against docs/supported_entities.md at the tag and count distinct entity ids (include the 8 "
    "MEDICAL_* ids); decide whether the Summary keeps 'about 80'",
    "H", "AIR")

add("medlic", G3,
    "MEDICAL_LICENSE sits under country_specific/us with country_code us (YAML too) although the entity page lists it as Global; a "
    "country filter without us would drop it [Inferred].",
    "INV(b) row 35",
    "a",
    "docs/analyzer/filtering_by_country page and recognizer_registry.py:128-139 at the tag; upgrade or keep the Inferred label",
    "L", "I")

# ---------------------------------------------------------------- G4
add("thresh_doc", G4,
    "No recommended score threshold is published for the default recognizers (also images, structured data, custom "
    "recognizers). Only examples: 0.4 (no-code tutorial), 0.7 (provider page), 0.4 to 0.5 (German recipe), 0.4 (research "
    "wrapper). The PD4, PD5 and PD6 R5 Summaries state 'no threshold advice ... is published'.",
    "PD1 R5 (A:99-105), R8 (A:161); PD4 R5 Summary and (B:90), R8 (B:135); PD5 R5 Summary and (B:264); PD6 R5 Summary and "
    "(B:414), R8 (B:454); P0 gap G3",
    "a",
    "Residual docs check: grep docs/ at the tag and at HEAD plus presidio-research docs for 'threshold'. If nothing, the ND "
    "stands (checked pages are named in each bullet). Bench value comes from {thresh_bench}",
    "H", "ABR")

add("thresh_bench", G4,
    "Best score threshold per entity type and per component, found by a sweep on a labelled set (weight recall with F2 as the "
    "docs advise).",
    "PD1 R7 (A:156); PD4 R8 (B:135); PD5 R5 (B:264); PD6 R8 (B:453-454)",
    "b", "Threshold sweep with presidio-research on a labelled prompt and response set; stays open", "M", "AB")

add("nbprov", G4,
    "Provenance of the notebook figures in the PD1 R5 Summary (F2 0.661 for default recognizers on 1500 synthetic samples; "
    "tuned engine F2 0.91): the Presidio version is not printed, hardware is not stated, the only date hint is the experiment "
    "file name 20260723. Whether 'default settings' equals the 2.2.364 defaults is therefore unproven.",
    "PD1 R5 Summary and (A:104, 108-114), R8 (A:164); A RN-3, A RN-8; INV-RN 5; R014",
    "a",
    "Notebook JSON metadata and outputs at the tag, git dates of notebooks 4 and 5 against the 2.2.364 release (2026-07-22), "
    "presidio-research CHANGELOG and README results section; pyproject needs presidio-analyzer>=2.2.364. Gives a bound, not "
    "an exact version; exact check is {nbrepro}",
    "H", "AIR")

add("nbrepro", G4,
    "Reproduce notebook 4 (F2 0.661, precision 0.733, recall 0.646; 1500 synthetic samples, IoU 0.75, threshold 0.4) and "
    "notebook 5 (F2 0.91) on Presidio 2.2.364 with presidio-research 0.3.2.",
    "PD1 R5 (A:108-109, 112-114); A RN-8",
    "b", "Re-run the notebooks; stays open (needs CP1 consent for local runs, {localrun})", "M", "AR")

add("uplift", G4,
    "The evaluation page says notebook 5 'boosts the f score in ~30%'; the printed outputs give +0.249 absolute (about +38% "
    "relative, [Inferred]). Part of the gap is label coverage (STREET_ADDRESS 3071 tokens, TITLE, AGE, ZIP_CODE have no "
    "default entity type) and the mapping step was not checked.",
    "PD1 R5 (A:110-113); A RN-6 (last item), A RN-8",
    "a",
    "Evaluation page wording, notebook 5 markdown cells and the CanonicalMapper mapping cell in notebook 4 at presidio-research "
    "0.3.2. Vendor docs and vendor notebooks disagree; keep both bullets (R007 item 4)",
    "M", "AR")

add("latency", G4,
    "Latency, throughput, memory and sizing are not published (single gunicorn worker by default; one unlabelled 5.84 s "
    "timing for 1500 samples; an author guideline of 100 ms per 100 tokens; Kubernetes and App Service pages give no "
    "figures). Bullets that bundle accuracy, latency and throughput also appear under {accuracy_other}.",
    "PD1 R5 (A:114-116), R8 (A:162); PD2 R5 (A:319), R8 (A:351); PD3 R5 (A:464); PD4 R6 (B:113), R8 (B:138); PD5 R5 (B:265), R8 "
    "(B:303); PD6 R5 (B:415-416), R8 (B:456); INV(d) rows 89, 92, 93",
    "b",
    "Benchmark on bench hardware. Documentation side is a closed question: vendor publishes none (checked Home, analyzer, "
    "FAQ, evaluation, GPU and recipe pages). Honest gap",
    "M", "ABI")

add("accuracy_an", G4,
    "Per-entity accuracy of the default Analyzer recognizers, of the GLiNER and LangExtract recognizers, and of any non-English "
    "recognizer or model (the German recipe tabulates Precision, Recall, F2 and Latency as TBD).",
    "PD1 R2 (A:30-33), R5 (A:117-118), R8 (A:163, 166)",
    "b", "Labelled-set evaluation per entity and language with presidio-research. Vendor publishes aggregates only. Honest gap",
    "M", "A")

add("accuracy_other", G4,
    "No accuracy figure is published for the Anonymizer (end-to-end leakage), encrypt and decrypt, image redaction on real screenshots "
    "and scans (DICOM demo covers 4 sample files only), the structured column map, or custom recognizers. The PD4, PD5 and PD6 "
    "R5 Summaries state 'no ... accuracy figure is published'.",
    "PD2 R5 (A:319), R8 (A:351); PD3 R5 (A:464); PD4 R5 Summary and (B:95), R8 (B:132); PD5 R5 Summary and (B:265), R8 (B:300); "
    "PD6 R5 Summary and (B:416, 456)",
    "b",
    "Bench tests with labelled data. The absence claims are [Not disclosed] with pages named; the three R5 Summaries carry a "
    "[Documented] label (see {sumlabel}). Honest gap",
    "H", "AB")

# ---------------------------------------------------------------- G5
add("none_strategy", G5,
    "ConflictResolutionStrategy: the enum docstring describes NONE (no resolution) but the enum has two members. Does any mode "
    "skip conflict resolution?",
    "PD2 R2 (A:267), R8 Summary and (A:352)",
    "a",
    "Read anonymizer_engine.py and conflict_resolution_strategy.py at the tag for None handling; anonymizer docs. A code read "
    "should settle it; running a call confirms",
    "M", "A")

add("rest_ops", G5,
    "Operators over REST: `keep`, `surrogate_ahds` and the deanonymizer `deanonymize_keep`. The API spec lists five operator "
    "schemas and says `decrypt` is the only deanonymizer; the code accepts every registered operator except `custom`.",
    "PD2 R4 (A:300), R8 (A:353); PD3 R4 (A:439), R8 (A:500); A RN-6",
    "b", "Send each operator to POST /anonymize and POST /deanonymize on the 2.2.364 service; docs-vs-code conflict is already recorded", "M", "A")

add("anon_misc", G5,
    "Anonymizer behaviours needing a run: merge_entities_with_spaces=True on two names separated by a space; offsets with non-BMP "
    "or mixed-script text; whether hash output length or format leaks anything to a model; which operator works best per entity "
    "type for LLM prompts (answer quality).",
    "PD2 R8 (A:354-355, 357-358)",
    "b", "Bench tests; stays open", "M", "A")

add("wrongkey", G5,
    "Decrypt with a wrong key, a damaged or truncated token, or non-UTF-8 plaintext: exception types and REST status (code reading "
    "suggests an exception and a generic HTTP 500).",
    "PD3 R5 (A:461), R7 (A:487), R8 Summary and (A:496)",
    "b", "Run the cases listed in PD3 R7; stays open", "M", "A")

add("llmtokens", G5,
    "Does an LLM keep 44-character base64 tokens intact, what do they cost in model tokens, and do repeated entities (different "
    "token each time) still give coherent answers?",
    "PD3 R2 (A:416), R7 (A:488-489), R8 (A:497)",
    "b", "Needs a model in the bench loop; stays open", "M", "A")

add("keymgmt", G5,
    "Key generation, storage and rotation guidance for encrypt, and any plan for authenticated encryption (cipher is CBC with no MAC "
    "[Inferred]). Drafts checked the anonymizer page, tutorials, samples and FAQ; only hash-salt advice exists.",
    "PD3 R4 (A:436), R6 (A:476), R8 (A:498-499)",
    "a",
    "Guidance half: re-read the OpenAI best-practices sample, encrypt_decrypt sample and docs/ for 'key'. Roadmap half is an honest "
    "gap (issues and roadmap not reachable here)",
    "M", "A")

add("litellm", G5,
    "What LiteLLM does beyond the Presidio page (restoring masked tokens, per-key switches).",
    "PD3 R2 (A:409-410), R8 (A:503); INV(d) row 96",
    "b", "Third-party product: LiteLLM behaviour is not Presidio evidence and its docs are not an official source here. Honest gap", "L", "AI")

add("nemo_restore", G5,
    "Whether NeMo Guardrails PII flows can restore masked values in a reply (not described in sheet 3 columns E and F).",
    "PD3 R4 (A:453), R8 (A:502); INV(d) row 97",
    "a", "Local check of two_level_v2.md columns E and F and the NVIDIA page already cited in INV(d) row 97", "L", "AI")

add("inv_vs_pd3", G5,
    "Cross-draft: INV(c) encrypt says key-size values [To be verified]; PD3 R4 documents 128, 192 or 256 bits from encrypt.py:43. INV(c) mask "
    "says no parameter defaults are stated [Not disclosed] after reading mask.py; PD2 R2 and R6 give the validations.",
    "INV(c) rows 73, 77; PD3 R4 (A:435), R6 (A:472); PD2 R2 (A:254), R6 (A:327)",
    "a", "Read encrypt.py, aes_cipher.py and mask.py at the tag; align the inventory cells with the column bullets", "M", "AI")

# ---------------------------------------------------------------- G6
add("imgthr", G6,
    "Image Redactor REST: the multipart form hard-codes score_threshold=0.4, the JSON form passes none (Analyzer default 0); the "
    "fill colour is read only from the form field `data`, so a JSON request is probably always filled black [Inferred].",
    "PD4 R5 (B:87-89), R6 (B:108), R7 (B:128), R8 Summary and (B:135-136)",
    "b", "Send the same image through both forms and compare boxes and fill; stays open", "M", "B")

add("imgscope", G6,
    "Scope and limits of image redaction: faces, signatures, handwriting, barcodes and QR codes (docs name only 'PII text "
    "entities'); accuracy on screenshots, scans and rotated text; non-English OCR (Tesseract language plus Analyzer language); "
    "image formats, multi-frame files, size limits; whether EXIF or PNG text chunks survive.",
    "PD4 R2 (B:29), R3 (B:41), R7 (B:119-120), R8 Summary and (B:132-134, 138-139)",
    "b", "Negative-control and degraded-image tests. Docs ND is an absence claim with pages named", "M", "B")

add("imgenv", G6,
    "Image-redactor container sets ANALYZER_CONF_FILE, NLP_CONF_FILE and RECOGNIZER_REGISTRY_CONF_FILE that no package code reads "
    "([Inferred] from a search).",
    "PD4 R4 (B:71)", "a", "grep presidio-image-redactor at the tag for the three names; upgrade or drop the Inferred bullet", "L", "B")

add("apispec", G6,
    "API spec problems: docs/api-docs/api-docs.yml has no /redact path although the image-redactor page points to an API spec for "
    "it; the spec omits allow_list, allow_list_match and regex_flags; the live api-docs page is rendered by script and was not "
    "read.",
    "PD4 R4 (B:72-73), R8 (B:140); PD1 R6 (A:124); PD6 R6 (B:423); PD2 R4 (A:300); B RN-3",
    "a",
    "Find the spec file the live api-docs page loads (yaml or json) and read it; check api-docs.yml at HEAD; docs/api/ pages",
    "M", "AB")

add("roadmap", G6,
    "Roadmaps: image redactor from beta to stable; a REST or Docker route for presidio-structured; PySpark and k-anonymity "
    "(listed as future work).",
    "PD4 R8 (B:142); PD5 R3 (B:218), R8 (B:304-305)",
    "b", "Roadmap is not documented (CHANGELOG, home, structured and image pages checked). Honest gap", "L", "B")

# ---------------------------------------------------------------- G7
add("maturity", G7,
    "Maturity label of presidio-structured. INV(a) says 'alpha [Documented]' from the getting-started-structured page; PD5 R4 says the "
    "label is [Not disclosed] after checking the structured page, README, home and FAQ (that page is not in PD5 R9); PD5 R8 says "
    "'alpha in 2024'.",
    "PD5 R4 (B:246-247), R8 (B:304); INV(a) row 15; B RN-10",
    "a", "Read /getting_started/getting_started_structured/ and presidio-structured/README at the tag; fix PD5 R4 and add the URL to PD5 R9. Feeds {q02b}", "M", "BI")

add("struct_behaviour", G7,
    "presidio-structured behaviours inferred from code: replace without new_value probably yields '<None>'; hash, mask, encrypt "
    "on int, float or empty cells; column names with spaces (getattr); in-place mutation of the input; _remove_low_scores and "
    "score_threshold unused; one-entity-per-column mislabelling of sparse or free-text columns; referential integrity across tables.",
    "PD5 R4 (B:241, 262), R5 (B:262), R8 Summary and (B:296-302)",
    "b", "Small Python harness on the 2.2.364 package; some points are code-readable first", "M", "B")

add("concepts", G7,
    "Concepts page says StructuredEngine 'is responsible for detecting PII entities'; code puts detection in the analysis builders and "
    "StructuredEngine only anonymises.",
    "PD5 R4 (B:244-245)", "a", "Check the concepts page at HEAD and docs/ at the tag; docs defect, report only", "L", "B")

# ---------------------------------------------------------------- G8
add("pd6_stale", G8,
    "PD6 R8 asks whether non-pattern recognizers can be sent per request over REST; PD6 R4 already shows the code builds only "
    "PatternRecognizer.from_dict.",
    "PD6 R8 (B:448) vs R4 (B:393)", "a", "Close the R8 bullet or restate it as [Documented: repo] in R4", "L", "B")

add("httperr", G8,
    "HTTP status for an invalid regex, a score outside 0 to 1, or a language with no matching recognizer (code suggests HTTP 500).",
    "PD6 R8 (B:449)", "b", "Send the bad requests to POST /analyze; stays open", "M", "B")

add("regex_timeout", G8,
    "REGEX_TIMEOUT_SECONDS with batch and multi-process runs; whether ad-hoc regex can block other requests; who may send ad-hoc "
    "recognizers given no built-in authentication.",
    "PD6 R7 (B:440), R8 (B:450-451)", "b", "Send a backtracking pattern with concurrent requests; deployment question for the bench", "M", "B")

add("overlap_weak", G8,
    "Recommended pattern scores for weak patterns; how a custom entity that overlaps a built-in one is resolved; context words with "
    "NoOpNlpEngine (code warns the Lemma enhancer cannot use words from the text).",
    "PD6 R5 (B:414), R8 (B:454-455)", "b", "Bench tests with overlapping digit patterns and the no_op config", "M", "B")

add("batchthr", G8,
    "Request-level score_threshold with recognizer-level score_thresholds in batch REST calls (precedence documented only at the tag).",
    "PD6 R8 (B:453); PD1 R5 (A:100)", "b", "Run batch /analyze with both settings; depends on {unrel}", "L", "AB")

# ---------------------------------------------------------------- G9
add("authtls", G9,
    "Authentication, TLS and rate-limit guidance beyond the FAQ paragraph. TLS is [Not disclosed] in five columns after checking "
    "FAQ, installation and analyzer pages; Kubernetes, App Service and Data Factory sample pages were not named.",
    "PD1 R6 (A:140-142), R8 (A:168); PD2 R6 (A:334); PD3 R6 (A:477-478); PD4 R6 (B:112, 114); PD6 R6 (B:432); INV(d) rows 89, 90, 92, 93",
    "a", "Read the Kubernetes, App Service and Data Factory sample pages and grep docs/ for TLS, HTTPS, ingress, auth; if nothing, ND stands", "M", "ABI")

add("limits", G9,
    "Maximum text length, request size and behaviour on very long inputs; dataset size and row limits (structured). app.py enforces "
    "none and no page states any.",
    "PD1 R6 (A:141), R8 (A:169); PD2 R6 (A:333); PD4 R6 (B:113), R8 (B:138); PD5 R6 (B:278); PD6 R6 (B:431)",
    "b", "Send long inputs and large tables; stays open. Docs side is ND with pages named", "M", "ABR")

add("corrhdr", G9,
    "Decision-process page says the correlation id is returned in an x-correlation-id response header; app.py sets none "
    "([Inferred] from a search of one file).",
    "PD1 R6 (A:139)", "a", "grep the whole presidio-analyzer package and Flask hooks; upgrade to [Documented: repo] or [Not disclosed]", "L", "A")

add("declog", G9,
    "Decision-process logging writes the token list of the analysed text to standard output, so PII can reach logs ([Inferred]).",
    "PD1 R6 (A:138)", "a", "Decision-process page example and analyzer logging code at the tag", "L", "A")

add("langdetect", G9,
    "Automatic language detection is not described (caller supplies language).",
    "PD1 R3 (A:52)", "a", "Residual grep of docs/ for 'detect' with language; ND stands if none", "L", "A")

# ---------------------------------------------------------------- G10
add("oop_label", G10,
    "The 'out of purpose' statement (prompt injection, harmful content, topics) is labelled inconsistently: [Inferred] in PD1 R2 and "
    "PD2 R2, [Documented] in PD4 R2 Summary and bullet, PD5 R2 Summary and bullet, PD6 R2 bullet (Summary is Inferred). The brief asked "
    "for [Documented]; README rule 2 treats an absence as [Not disclosed] or [Inferred]; B RN-7 offers the switch.",
    "PD1 R2 (A:38); PD2 R2 (A:272); PD4 R2 Summary and (B:19); PD5 R2 Summary and (B:198); PD6 R2 (B:362); B RN-7; BR Scope",
    "a",
    "Main ruling (no source needed): one convention for all six columns. Triager proposal: [Inferred] with the premise 'home page module list' "
    "everywhere, which changes the PD4 R2 and PD5 R2 Summary labels",
    "H", "ABR")

add("sumlabel", G10,
    "Summary label stronger than its Detail (README section 4 rule 5): PD1 R2 Summary [Documented] rests on the Inferred '16 pattern "
    "recognizers' bullet; PD4 R5, PD5 R5 and PD6 R5 Summaries [Documented] contain 'no threshold advice or accuracy figure is "
    "published', whose bullets are [Not disclosed].",
    "PD1 R2 Summary vs (A:26-27); PD4 R5 Summary vs (B:90, 95); PD5 R5 Summary vs (B:264-265); PD6 R5 Summary vs (B:414, 416)",
    "a", "Relabel the four Summaries or reword to documented parts only; re-count words (several sit at 44 or 45)", "H", "AB")

add("sument", G10,
    "Summary claims not entailed by the row's own Detail: PD3 R1 'Presidio stores nothing between calls' (the statement is in PD2 R2, A:258); PD2 R1 "
    "'a list of the changes with positions in the new text' (lives in R3 and R5); PD1 R6 'other languages need extra configuration' "
    "(lives in R2).",
    "PD3 R1 Summary (A:397); PD2 R1 Summary (A:235); PD1 R6 Summary (A:120)",
    "a", "Add the supporting bullet to the same row (anonymizer page 'does not store or maintain stateful sessions', R5 fields, languages page) or trim the sentence", "H", "A")

# ---------------------------------------------------------------- G11
add("invstatus", G11,
    "Status cells: 'stable [Inferred]' for Analyzer, Anonymizer and three NLP engines (premise: no beta mark found); 'Not stated "
    "[Not disclosed]' for cli, meta-package, slim, no-op, presidio-research; 'alpha' sits outside the header's stable/beta/legacy "
    "vocabulary (main ruled vendor wording stands).",
    "INV(a) rows 11, 12, 16-23; INV(d) status cells rows 87-98",
    "a", "pyproject Development Status classifiers and package READMEs at the tag; docs nav", "L", "I")

add("invextras", G11,
    "'None beyond presidio-analyzer [Inferred]' in the extras column of about 18 recognizer rows (premise: regex recognizer, no extra in pyproject).",
    "INV(b) rows 32-34, 35, 37-54", "a", "Grep pyproject optional-dependencies and imports in each recognizer file", "L", "I")

add("invlang", G11,
    "Languages not stated for MedicalNER (beyond en), GLiNER, Azure OpenAI LangExtract, Azure AI Language and AHDS recognizers.",
    "INV(b) rows 55, 57, 59-61", "b", "Language coverage belongs to third-party models and Azure services. Honest gap", "L", "I")

add("invsample", G11,
    "Status 'Sample [Inferred] (premise: under Samples in the nav)' for Kubernetes, App Service, Spark and Fabric, Data Factory; Spark page "
    "mentions Databricks runtime 8.1.",
    "INV(d) rows 92-95", "a", "mkdocs.yml navigation at the tag; sample page headers", "L", "I")

add("community", G11,
    "Behaviour of community-listed integrations (LangChain, LlamaIndex, Guardrails AI, LLM Guard, Rasa, Dataiku, LiteLLM) is 'Varies "
    "[Not disclosed]'.",
    "INV(d) row 100", "b", "Third-party projects, not Presidio evidence. Honest gap", "L", "I")

add("v1", G11,
    "Legacy V1: contents of branch V1 not read [To be verified]; Docker tag v1 and PyPI 0.95 come from the V2 page only.",
    "INV(a) row 24", "a", "git ls-remote --heads for branch V1; V2 page", "L", "I")

add("coveredby", G11,
    "Covered-by convention: operator rows (c) list PD2 and PD3 only although PD5 applies the anonymise operators; recognizer rows (b) list "
    "PD1 only although PD4, PD5 and PD6 reuse the Analyzer; the Docker row omits PD6.",
    "INV(b) rows 32-61; INV(c) rows 70-79; INV(d) row 88; BR inventory (c) 'PD5 may be added'",
    "a", "Main/merger convention; no source needed. The marker check passes either way", "L", "IR")

add("nemo_fyi", G11,
    "FYI: the Presidio default replacement string `<ENTITY_TYPE>` is now documented (replace.py@2.2.364:18), while NeMo columns E and F R8 "
    "still say it is 'not verified in the Presidio docs'.",
    "PD2 R2 (A:250); A:79, 303; two_level_v2.md lines 586, 680; INV(d) row 97",
    "a", "No change to frozen NeMo sheets; note in the change log. Also PD2 R2 (A:250) mixes a code fact with a claim about NeMo columns (split it)", "L", "AI")

# ---------------------------------------------------------------- G12
add("german", G12,
    "German recipe is in docs/ at the tag but not in the mkdocs nav; unknown whether the live site serves it. It supplies the 0.4 to 0.5 "
    "tip and the 'TBD' accuracy table.",
    "PD1 R5 (A:103, 117); A RN-9", "a", "mkdocs.yml nav and a live-site search for the recipe", "L", "A")

add("openai_sample", G12,
    "The 'Data Protection toolkit for OpenAI' sample is cited as a Presidio-authored deployment sample but is not in the left nav; its "
    "maintenance status is unknown and its path carries the vendor's spelling 'anonymaztion'.",
    "PD1 R3 (A:49), R9 (A:190); PD2 R3 (A:281); PD3 R2 (A:411-412), R4 (A:445); A RN-10(3)",
    "a", "Samples index page and the file history at the tag; keep the URL as spelled", "L", "A")

add("urlcheck", G12,
    "URL check at P9: all github.com blob URLs were cited from a clone (403 on fetch); PD1 R9 lists the 301 host "
    "data-privacy-stack.github.io/presidio/ and the microsoft.github.io stub (both are HTTP facts, not 200 pages); the inventory cites "
    "presidio-research blobs at the full SHA 0cb36502.",
    "PD1 R9 (A:190, 192, 193); all R9 lists; INV Source URL column; INV-RN 7; INV(a) row 23",
    "a", "gr-url-checker at P9 with the exceptions recorded; blob URLs follow {rpin}", "M", "ABI")

# a cross-reference note used inside texts

# ---------------------------------------------------------------- numbering
def clsletter(c):
    return c.strip()[0]


ids = {it["key"]: "T%d" % n for n, it in enumerate(ITEMS, 1)}
ids["localrun"] = "the CP1 local-run consent item (section 'Items for CP1', point 4)"


def fmt(s):
    def rep(m):
        k = m.group(1)
        if k not in ids:
            sys.exit("unknown ref " + k)
        return ids[k]
    return re.sub(r"\{(\w+)\}", rep, s)


for it in ITEMS:
    for f in ("item", "loc", "src"):
        it[f] = fmt(it[f])
        assert "|" not in it[f], (it["key"], f)

# ---------------------------------------------------------------- counts
cls_ct = collections.Counter(clsletter(i["cls"]) for i in ITEMS)
pri_ct = collections.Counter(i["pri"] for i in ITEMS)
cp = collections.Counter()
for i in ITEMS:
    cp[(clsletter(i["cls"]), i["pri"])] += 1
files = {"A": "presidio_cols_a.md", "B": "presidio_cols_b.md", "I": "presidio_inventory.md", "R": "brief / rulings / queue / other notes"}
file_ct = {k: sum(1 for i in ITEMS if k in i["files"]) for k in files}
decision_ids = [ids[i["key"]] for i in ITEMS if "CP1" in i["cls"] or i["key"] == "q01"]
honest = [ids[i["key"]] for i in ITEMS if "honest gap" in (i["src"] + i["cls"]).lower()]
H_ids = [ids[i["key"]] for i in ITEMS if i["pri"] == "H"]

N = len(ITEMS)
lines = []
w = lines.append
w("# Presidio triage of open evidence items (DRAFT)")
w("")
w("Sources triaged: `presidio_cols_a.md` (PD1 to PD3), `presidio_cols_b.md` (PD4 to PD6), `presidio_inventory.md` (sheet 3f: (a) components 14 rows, (b) recognizers 31, (c) operators 10, (d) integration paths 14), the brief `presidio_brief.md`, the three Reviewer notes sections, explorer notes `20261009_presidio_p0.md` and q01 to q04, rulings R001 to R014, and `scratchpad/main/queue.md` (items routed to triage). No research done; source suggestions only. Nothing here is verified. Written 2026-10-09 by gr-triager. Mechanical checks re-run at the start: `check_drafts.py columns` on both column files gives 0 errors and 0 warnings; `check_drafts.py inventory --headers` against the concatenated column headers gives 0 errors and 0 warnings (14, 31, 10, 14 rows, 8 cells each).")
w("")
w("## Legend")
w("")
w("- File short names: A = presidio_cols_a.md, B = presidio_cols_b.md, INV = presidio_inventory.md, BR = presidio_brief.md. Draft line numbers are as at 2026-10-09 and move when the merger edits (`A:81` = line 81 of cols_a).")
w("- Location notation: `PDn Rk` = column PDn, row Rk (Summary or Detail bullet named; `(A:81)` gives the line); `INV(a) row 22` = inventory block (a), file line 22 (blocks: (a) lines 11-24, (b) 32-62, (c) 70-79, (d) 87-100); `A RN-n`, `B RN-n`, `INV-RN n` = numbered Reviewer notes (A RN-1 to 12 and B RN-1 to 11 count the bullets in order; INV-RN uses its own numbers 1 to 9).")
w("- Labels: ND = [Not disclosed]; TBV = [To be verified]; INF = [Inferred] that rests on an unchecked premise; R8 = unlabelled R8 bullet; SUM = a fact that depends on a summarising fetch (none found, see provenance note).")
w("- Class: a = answerable from an official page, repo file at the pin, or a local file; b = needs testing (stays open) or is a CP1 decision item (closes when chosen, NeMo b22 precedent); `honest gap` = the vendor does not publish it, or it concerns a third-party product or service, and no public document is expected to answer; c = licensing, ownership or terms.")
w("- Priority: H = changes an R1 to R7 Summary line, a Summary label, or a headline number (version pin, F2 figure, entity count). M = Detail level, or only an R8 Summary line (R8 Summaries list questions and are not counted as H, as in the Sentinel triage). L = cosmetic or low impact.")
w("- Short source names: SUP = supported-entities page, TRANS = project_transition page, INST = installation page, GSS = getting_started_structured page, ANON = anonymizer page, LLM = LiteLLM sample page, EVAL = evaluation page (all under https://presidio.dataprivacystack.org/), tag = data-privacy-stack/presidio at 2.2.364 (779dbd28), research = data-privacy-stack/presidio-research.")
w("")
w("## Counts")
w("")
w("Total %d deduplicated items (T1 to T%d), drawn from the 64 R8 bullets (PD1 11, PD2 10, PD3 9, PD4 12, PD5 12, PD6 10), the explicit open labels (columns: ND 32 bullets, TBV 5 bullets and 2 Reviewer-note passages; inventory: ND 26 cells, TBV 5 cells), the [Inferred] items that rest on an unchecked premise (columns 88 Detail bullets in total, inventory 68 label occurrences), the three Reviewer notes sections, the queue items routed to triage, and a cross-draft comparison of the three files." % (N, N))
w("")
w("| Class | Count | of which H |")
w("|---|---|---|")
for c, name in (("a", "a doc-answerable"), ("b", "b needs testing or CP1 decision"), ("c", "c licensing / ownership / terms")):
    w("| %s | %d | %d |" % (name, cls_ct[c], cp[(c, "H")]))
w("| Total | %d | %d |" % (N, pri_ct["H"]))
w("")
w("Priority totals: H %d, M %d, L %d." % (pri_ct["H"], pri_ct["M"], pri_ct["L"]))
w("")
w("Class by priority: " + "; ".join("%s: H %d, M %d, L %d" % (c, cp[(c, "H")], cp[(c, "M")], cp[(c, "L")]) for c in "abc") + ".")
w("")
w("Items touching each source file (an item can touch several): " + "; ".join("%s %d" % (files[k], file_ct[k]) for k in "ABIR") + ".")
w("")
w("CP1 decision items counted in class b: " + ", ".join(i for i in decision_ids if i != ids["q01"]) + " (T1 is class c). Honest-gap items: " + ", ".join(honest) + ".")
w("")
w("Dedup note: the same open question appears in several columns (threshold, latency, accuracy, TLS and authentication, size limits, release notes, Python versions, ownership) and is merged into one id with every location listed. Where a question has both a documentation half and a run-it half it is split into two ids (a + b): %s / %s (thresholds), %s / %s (notebook figures), %s / %s (Azure data flow and terms), %s / %s (release notes and per-recognizer thresholds). The R8 bullet 'Owner question Q01' repeated in PD1 to PD3 is one item (%s)." % (ids["thresh_doc"], ids["thresh_bench"], ids["nbprov"], ids["nbrepro"], ids["azureflow"], ids["azureterms"], ids["relnotes"], ids["unrel"], ids["q01"]))
w("")
w("Provenance note: all three files state that Presidio docs pages were read raw with `fetch_text.py` and code from a shallow clone at the tag, and that WebFetch was not used for any quote or number, so no item is classed as depending on a summarising fetch. Facts that depend on something not read: the GitHub release page and notes for 2.2.364 (%s); presidio-research README and tags in PD4 to PD6 (%s); the live API reference page, which is rendered by script (%s); the getting-started-structured page for PD5 (%s); the deployed-site commit (%s)." % (ids["relnotes"], ids["rsread"], ids["apispec"], ids["maturity"], ids["docspin"]))
w("")
w("Raw label census (whole-file occurrences of the exact bracket text, including Reviewer notes): A: [Documented] 139, [Documented: repo data-privacy-stack/presidio@2.2.364] 102, [Documented: repo data-privacy-stack/presidio-research@0.3.2] 9, [Inferred] 63, [To be verified] 3, [Not disclosed] 16. B: [Documented] 114, repo@2.2.364 125, [Inferred] 44, [To be verified] 4, [Not disclosed] 18. INV: [Documented] 186, repo@2.2.364 206, repo presidio-research@0cb36502 7, [Inferred] 68, [To be verified] 6, [Not disclosed] 27.")
w("")
w("Groups (id ranges): " + "; ".join("%s %s" % (g, "T%d to T%d" % (min(n for n, it in enumerate(ITEMS, 1) if it["grp"] == g), max(n for n, it in enumerate(ITEMS, 1) if it["grp"] == g))) for g in dict.fromkeys(i["grp"] for i in ITEMS)) + ".")
w("")
w("## Items for CP1 (decision-bearing for the user)")
w("")
w("1. %s ownership, official-source status and the frozen prefix `Presidio:` (class c). Evidence is in hand; the ruling is the user's." % ids["q01"])
w("2. %s, %s, %s column split: six vs four columns; PD5 column vs inventory only; family rows vs per-entity catalogue." % (ids["q02a"], ids["q02b"], ids["q02c"]))
w("3. %s whether the sheet should carry licences of third-party components (suggested item, not open in the drafts)." % ids["complic"])
w("4. Local-run consent: b-class items such as %s, %s, %s, %s, %s and %s need the 2.2.364 packages installed and run locally, a spaCy model download, or a GHCR image pull. The queue records that pulling images is outside the read-only rule; running the vendor's open-source packages locally calls no vendor API and signs in nowhere. The user decides whether these run in P5 or stay open for the bench phase." % (ids["active"], ids["ghcr"], ids["rest_ops"], ids["wrongkey"], ids["imgthr"], ids["nbrepro"]))
w("5. %s (FYI) presidio-research stays an inventory row (R010); no evidence in the drafts that it needs a sheet." % ids["r010"])
w("")
w("## Triage table")
w("")
w("| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |")
w("|---|---|---|---|---|---|")
for n, it in enumerate(ITEMS, 1):
    w("| T%d | %s | %s | %s | %s | %s |" % (n, it["item"], it["loc"], it["cls"], it["src"], it["pri"]))
w("")

# ---------------------------------------------------------------- label hygiene
w("## Label hygiene")
w("")
w("Scope: the three files against `drafts/README.md` section 3. Allowed forms: [Documented], [Documented: repo <repo>@<ref>], [Documented: develop/unreleased], [Inferred], [To be verified], [Not disclosed]. Mechanical scan result: every label bracket in A, B and INV is one of the allowed forms; no [Not found], no [To be verified: ...], no [Documented: develop/unreleased] (none was needed: items sitting under CHANGELOG [unreleased] but present in the tagged code carry the repo label, as the brief instructs). Repo labels use the full `data-privacy-stack/presidio@2.2.364` form (A 102, B 125, INV 206), `presidio-research@0.3.2` (A 9) and `presidio-research@0cb36502` (INV 7). No verbatim quote exceeds 37 words (scan of every double-quoted passage of 20 or more characters; two hits at 38 or more words, A:543 and INV row 96, are prose between quote marks, not quotes). Column bullets: one label per bullet in all 6 columns (0 multi-label bullets).")
w("")
w("| Issue | Where | Proposed fix | T-id |")
w("|---|---|---|---|")
hy = [
    ("Presidio-research pin differs between files: repo label `@0.3.2` in A (9 labels) vs `@0cb36502` in INV (7 labels); R014 requires the release tag", "A:26, 104, 108-109, 112, 114, 153-155; INV scope note, INV(a) row 23 and its URLs", "Re-pin INV to the tag after reading it; one repo label per bullet; both full-SHA URLs become tag URLs", ids["rpin"]),
    ("Non-label bracket phrase `[unreleased]` written plainly in table cells and notes (a label parser or COUNTIF could mistake it)", "INV(a) row 22, INV(d) row 98, INV-RN 3 (B has it only inside backticks)", "Write 'under the unreleased heading of CHANGELOG.md' without brackets", ids["unrel"]),
    ("Pip-extra brackets inside cells: `presidio_analyzer[stanza]`, `[transformers]`, `presidio-analyzer[azure-ai-language]`, `[ahds]` (INV rows 61 and 76)", "INV(a) rows 19, 20; INV(b) rows 60, 61; INV(c) row 76 (A has `[ahds]` in backtick code at A:262, 331)", "Low risk because they are attached to a package name; the Sentinel precedent rewrote `[_{level}]`. Keep inside backticks in columns; in INV cells write 'extra ahds' instead", ids["invextras"]),
    ("Own counts labelled [Documented]: 80 entity rows (PD1 R2, A:18), YAML counts 74 / 73 / 50 / 24 (A:23-24, INV(b) intro), DICOM sample set '4 files and 19 labelled items' (B:93, 'count made from the file')", "A:18, 23-25; B:93; B RN-8; INV(b) intro", "Keep [Documented: repo ...] only when the number is stated by the vendor; otherwise [Inferred] with 'counted by parsing' or plain text '(count made from the file)'. The YAML counts agree between A and INV", ids["entcount"]),
    ("Same fact, different labels: 'returns detections, not a verdict' is [Inferred] in PD1 R1, PD2 R1, PD3 R1 and [Documented] in PD1 R5 (field list in code)", "A:12, 94, 244, 405; A RN-7(b)", "Acceptable (classification vs field list); add the premise to R1 or leave as is. No change needed unless the verifier objects", ids["sumlabel"]),
    ("Out-of-purpose statement: [Documented] vs [Inferred] across columns", "A:38, 272; B:19, 198, 362", "One convention; proposal [Inferred] with premise (home page module list)", ids["oop_label"]),
    ("Summary label stronger than the weakest fact it draws on", "PD1 R2, PD4 R5, PD5 R5, PD6 R5 Summaries", "Relabel or reword (README section 4 rule 5)", ids["sumlabel"]),
    ("Summary sentence with no supporting bullet in the same row", "PD3 R1, PD2 R1, PD1 R6 Summaries", "Add the bullet or trim", ids["sument"]),
    ("Fact and cross-reference in one bullet: PD2 R2 (A:250) states the Replace default [Documented: repo] and also says the NeMo columns list it as unverified", "A:250", "Split: code fact stays [Documented: repo], NeMo remark becomes an [Inferred] bullet or moves to R8 (README rule 5)", ids["nemo_fyi"]),
    ("Conflict narrative inside one bullet: 'Python versions conflict (three sources, none picked): package metadata lists 3.10 to 3.14' names one source and says three; PD4 and PD5 have two Python bullets, PD1 to PD3 have three", "B:66 (PD4 R4), B:248 (PD5 R4)", "Drop the narrative lead-in; one fact per bullet, add the docs/installation.md bullet to PD4 and PD5 for parity", ids["pyver"]),
    ("Absence claims correctly labelled [Not disclosed] with pages named (spot check of all 32 column ND bullets and 26 INV ND cells): fine. Exceptions to review: INV(c) mask 'no default values stated' after reading mask.py (a code fact, not a docs absence); INV(a) 'Not stated' status cells (an absence of a label)", "INV(c) row 73; INV(a) rows 16, 17, 21-23", "Re-check against mask.py; keep ND for status cells", ids["inv_vs_pd3"]),
    ("TBV that are really process facts ('github.com returned 403 here')", "A:81, 443; B:126, 290, 444", "Resolve (releases, research repo) or reword as a product-neutral open question; the final files must not mention the proxy or this session", ids["relnotes"]),
    ("Inferred bullets whose premise a quick read would settle: x-correlation-id header (one-file search), image-redactor env vars (package search), Medical licence country filter, 'extras None' (18 rows), Python 3.14 'also lists', cipher has no MAC", "A:139, 436; B:71; INV(b) row 35 and rows 32-54", "Upgrade to [Documented: repo] or [Not disclosed] after the check, or leave as [Inferred] with the premise", ids["corrhdr"]),
    ("Third-party facts without [Documented] attribution rule: GLiNER licence 'Apache 2.0' (INV row 57) is stated as [Documented] from the Presidio GLN page with plain text '(Presidio docs, not GLiNER docs)'; LiteLLM rows follow the same pattern", "INV(b) row 57; INV(d) row 96; A:48, 78; A:409-410", "Compliant with the brief; keep the plain-text attribution", ids["complic"]),
]
for issue, where, fix, t in hy:
    w("| %s | %s | %s | %s |" % (issue, where, fix, t))
w("")
w("Covered-by check: every 'Covered by Table 3 column' cell is either a ;-separated list of exact headers from the six PD headings or the marker `— (inventory only, not in Table 3)` (cli, meta-package, presidio-research, CLI path) or `— (legacy, not in Table 3)` (V1); no `planned` marker is used; no stray values, no bold, no backticks, no pipe inside cells (the checker confirms the headers). Reviewer-notes sections (A 12 bullets, B 11, INV 9 items) must be gone from the merged finals.")
w("")

# ---------------------------------------------------------------- style
w("## Style issues in columns")
w("")
w("1. Summaries are within limits (largest: 45 words at PD4 R2, PD6 R2 and PD6 R4; 44 at PD3 R3, PD4 R4, PD4 R5, PD5 R1, PD6 R5; R7 largest 51 of 60 at PD3). Eight Summaries are within one word of the cap, so relabelling or rewording in %s, %s, %s must not add words. All R8 Summaries start `**Key open questions.**` with no label; all R9 Summaries are plain; no underscores, backticks or `$` in any Summary; Summaries are ASCII." % (ids["sumlabel"], ids["oop_label"], ids["sument"]))
w("2. Code-like identifiers in Summaries (brief forbids them): PD2 R6 'a DEFAULT entry'; PD2 R8 'a NONE conflict strategy'; PD3 R4 'a random IV'; 'DataFrame' (a class name) in PD5 R3, R5, R6, R7 Summaries; 'F2' in PD1 R5 (a metric name, acceptable). Suggested: 'a default entry', 'a no-resolution mode', 'random initialisation vector', 'table'.")
w("3. Internal conflict tags in deliverable bullets: 'Source conflict C2' (A:28, 29), 'C3' (A:84, 450), 'C4' (A:75, 297). C-numbers come from the P0 note and mean nothing in the sheet. Write 'The entity page lists ...' and 'The live page lists ...' as plain pairs.")
w("4. Session and process language in Detail: 'github.com returned HTTP 403 through the proxy on 2026-10-09' (A:81, 443), '... returned 403 here' (A:170, 359; B:126, 143, 290, 306, 444, 452), 'was not readable here' (B:290), 'not readable as text' (A:163, B:140). Finals must not carry process language; resolve through %s and %s or reword as product-neutral open items." % (ids["relnotes"], ids["rsread"]))
w("5. Decision items inside R8: 'Owner question Q01: ... (user ruling)' in PD1 R8 (A:171), PD2 R8 (A:360), PD3 R8 (A:504) but not in PD4 to PD6 R8; 'the decision belongs to CP1' in PD5 R8 (B:295). Remove after CP1 (%s, %s)." % (ids["q01"], ids["q02b"]))
w("6. R8 bullets that restate something the same column already documents: PD6 R8 non-pattern recognizers over REST (B:448 vs B:393); PD2 R8 `keep` and `surrogate_ahds` over REST (A:353 vs A:300, partly); PD1 R8 'Whether 2.2.364 is the latest release' duplicates a TBV bullet at A:81. PD1 R8 Summary says 'a thin default entity set', an evaluation that no R8 bullet states.")
w("7. Repeated boilerplate in R4 of all six columns (ownership, MIT licence, Python lists, 301 host observation, version). PD1 to PD3 carry three Python bullets, PD4 and PD5 carry two (A RN-10(4) says the repetition is deliberate so each column stands alone after a merge). The 301 observation is repeated verbatim in PD4 R4 and PD5 R4 (B:75, B:251). Low priority; keep only if the sheet rows are read separately.")
w("8. Hyphenated product term 'Custom-recognizer detection' in the PD6 header and 'Image Redactor' without '(beta)' in the PD4 header: both follow the brief exactly; CP1 may add 'beta' (the P0 proposal had it). Headers are identical in brief, column files and INV Covered-by cells.")
w("9. Quotes: the ellipsis character (U+2026) appears in PD4 to PD6 quotes (10 lines in B), a beta sign in a PD1 R5 quote and an en dash inside the German-recipe quote (A:103). README allows `…` for omissions; the other characters are inside verbatim quotes. All Summaries are ASCII.")
w("10. One bullet over 420 characters: PD1 R2 (A:25, the long list of disabled entries). Consider splitting; no wrapped bullets found.")
w("11. R9 lists: one URL per bullet in all six columns; PD1 R9 includes two HTTP-fact URLs (the 301 host and the stub) and the vendor-spelled sample path (see %s). PD4 R9 does not list the getting-started-structured page that INV(a) cites for PD5's maturity (see %s)." % (ids["urlcheck"], ids["maturity"]))
w("12. R7 first Detail bullet and Summary start with `**Minimum setup:**` and are [Inferred] in all six columns: compliant. PD1 R7 and PD4 R7 to PD6 R7 cite presidio-research (R010); only PD1 to PD3 cite a pinned repo label for it.")
w("")

# ---------------------------------------------------------------- contradictions
w("## Contradictions")
w("")
w("Source conflicts and cross-file inconsistencies, each with the ids that resolve them. 'Both written' means the drafts already carry two labelled bullets (README rule 4).")
w("")
conts = [
    ("Ownership and name: the original task wording and the P0 handover say 'Microsoft Presidio' (microsoft.github.io, github.com/microsoft); the live site, a 301 and the transition page say the project is moving to Data Privacy Stack (CLAUDE.md and seeds now record the move and defer the decision to CP1). The FAQ says 'has since transitioned', the transition page 'in the process of transitioning'.", ids["q01"]),
    ("Release title: brief, P0 note and queue read 'Release 2.2.364 / 0.0.60' as presidio-structured 0.0.60; pyproject files at the tag give presidio-image-redactor 0.0.60, presidio-structured 0.0.8, presidio-cli 0.0.9. Drafts follow the code; the title itself is unread.", "%s, %s" % (ids["sixty"], ids["relnotes"])),
    ("presidio-research pin: columns cite tag 0.3.2; INV cites HEAD 0cb36502 and says no tags were visible; A RN-3 says tags exist up to 0.3.2. requires-python differs between them (>=3.11,<3.14 at 0.3.2, <3.15 at HEAD).", ids["rpin"]),
    ("presidio-research readable or not: PD1 to PD3 read it; PD4 to PD6 (and B RN-3) say it was not readable and carry TBV.", ids["rsread"]),
    ("presidio-structured maturity: INV(a) '[Documented] alpha' (getting-started-structured page) vs PD5 R4 '[Not disclosed]' after checking other pages; PD5 R8 says 'alpha in 2024'.", ids["maturity"]),
    ("Encrypt key sizes and mask defaults: INV(c) 'key-size values [To be verified]' and 'no defaults stated' vs PD3 R4 'must be of length 128, 192 or 256 bits' and PD2 validations from the same code files.", ids["inv_vs_pd3"]),
    ("Entity page vs default YAML (C2): the page lists entities the YAML disables or omits, with no default-off note; the YAML or code has entities the page omits. Both written.", "%s, %s" % (ids["sup_vs_yaml"], ids["active"])),
    ("Entity row count: live page 80, docs/supported_entities.md at the tag 81, brief about 120.", ids["entcount"]),
    ("Python versions (C3): live 3.10 to 3.13; docs/installation.md at the tag 3.10 to 3.14; pyproject <3.15; CLI README 3.10 to 3.13 vs classifiers to 3.14; release note 3.14. Both written.", ids["pyver"]),
    ("Docker names (C4): local build names on the analyzer and anonymizer pages vs ghcr.io names on the installation page; MCR stale. Both written.", ids["dockername"]),
    ("Docs vs notebooks: the evaluation page says notebook 5 boosts the f score 'in ~30%'; outputs give +0.249 absolute (about 38% relative). Brief expected no published numbers; R014 allows the notebook figures with qualifiers.", "%s, %s" % (ids["uplift"], ids["nbprov"])),
    ("CHANGELOG [unreleased] vs tagged code vs live docs: NoOpNlpEngine, per-recognizer score_thresholds, BatchDeanonymizeEngine, PhUmidRecognizer are in the tag; the CHANGELOG lists them as unreleased; the live registry and API pages omit score_thresholds. PD1 R5 states the threshold precedence as [Documented: repo] while PD6 R4 and R8 present it as an open release question. Both written.", "%s, %s" % (ids["unrel"], ids["relnotes"])),
    ("API spec vs code: spec omits allow_list, allow_list_match, regex_flags; lists five operator schemas; says decrypt is the only deanonymizer while code has deanonymize_keep; has no /redact path although the image-redactor page points to it; decision-process page promises an x-correlation-id header that app.py does not set. Both written (header item is [Inferred]).", "%s, %s, %s" % (ids["rest_ops"], ids["apispec"], ids["corrhdr"])),
    ("Operator naming: AHDS page example uses `surrogate`, the operator table and code use `surrogate_ahds`; operator table omits `deanonymize_keep`. Both written; code preferred (R007 item 4).", ids["rest_ops"]),
    ("ConflictResolutionStrategy: docstring names NONE, enum has two members.", ids["none_strategy"]),
    ("Concepts page says StructuredEngine detects PII; code puts detection in the analysis builders.", ids["concepts"]),
    ("Image Redactor REST thresholds: multipart form 0.4, JSON form none; Python default 0.", ids["imgthr"]),
    ("Out-of-purpose statement: brief says [Documented]; PD1 and PD2 use [Inferred]; PD4, PD5 and PD6 bullets use [Documented].", ids["oop_label"]),
    ("Brief estimates vs findings: ~120 entities (found 80); 'no published numbers' (notebooks print F2 0.661 and 0.91); `SgUenRecognizer` only (found four recognizers absent from the YAML); structured 0.0.60 (found 0.0.8). The drafts record these as corrections (A RN-5, B RN-4).", "%s, %s, %s" % (ids["entcount"], ids["nbprov"], ids["sixty"])),
    ("NeMo columns E and F say the Presidio default replacement string is 'not verified in the Presidio docs'; PD2 R2 documents `<ENTITY_TYPE>` from replace.py and the anonymizer page. NeMo sheets are frozen.", ids["nemo_fyi"]),
    ("FAQ 'Presidio is a library or SDK rather than a service' vs analyzer page 'a Python based service' and the shipped REST services: PD1 R1 already carries both quotes as separate bullets. Both written; no open item.", "none"),
    ("DICOM docs say metadata is not scrubbed while the code uses metadata values to build a PERSON deny list for pixel text: not a conflict (B RN-11), easy to misread; no item.", "none"),
    ("Seeds said 'NeMo K/L wrap Presidio'; corrected at P1 to columns E and F (two_level_v2.md lines 509 and 611, confirmed). No open item.", "none"),
]
for n, (txt, t) in enumerate(conts, 1):
    w("%d. %s See %s." % (n, txt, t) if t != "none" else "%d. %s" % (n, txt))
w("")
w("Cross-draft values compared and found consistent: YAML counts (74 entries, 73 distinct names, 50 disabled, 24 enabled; UkPostcodeRecognizer twice); per-country disabled counts (Germany 13, Korea 4, India 6, Australia 4, Sweden 2, Nigeria 2, Philippines 2, Turkey 2); default NLP engine and model (spacy, en_core_web_lg); default score threshold 0; default operator replace and `<ENTITY_TYPE>`; hash random salt and 16-byte minimum; operator lists ANONYMIZERS and DEANONYMIZERS; REST routes and port 3000; GHCR image names and host ports 5001, 5002, 5003; ownership and licence wording; column headers (brief, columns, INV Covered-by). Compared by reading, not by execution.")
w("")

text = "\n".join(lines)
open(OUT, "w", encoding="utf-8").write(text + "\n")
print("wrote", OUT, "items", N, dict(cls_ct), dict(pri_ct), "H ids", H_ids)
print("file touch", file_ct)
print("decision", decision_ids)
print("honest", honest)
