# drafts/ : specification for research drafts, triage, resolutions, merge and review

This file is the contract every drafting, triage, resolution, merge and verifier agent follows. The build scripts parse these files with strict rules (section 4 to 6); a file that breaks them fails the build. When this file and a product brief disagree, the brief wins for scope and headers, this file wins for format.

## 1. What lives here

Three kinds of files:

- **Final sources (consumed by the build).** Edit only through the pipeline below. Each is parsed by a script in benchtest/.
- **Intermediate artefacts (not consumed).** Briefs, column drafts, triage, resolutions, change logs, reviews, previews, URL lists. They are the audit trail; keep them, never feed them to the build.
- **Generated files.** The xlsx workbooks and any verification output. Never hand-edit.

Current files by product:

| Product | Final sources (built) | Intermediate artefacts |
|---|---|---|
| NeMo Guardrails (legacy names) | two_level_v2.md (sheet 3 columns), inventory.md (3b rail inventory), eval_tooling.md (3c) | batch1.md to batch3.md, jailbreak.md, dialog_enrich.md, exec_rails.md, two_level.md (v1), triage.md, resolutions_1..3.md, v2_changes.md, v2_review.md, two_level_review.md, eval_tooling_review.md, *_summaries_preview.md, v2_urls.txt |
| Llama Guard | lg_two_level.md (LG1 to LG5), lg_inventory_final.md (3d) | lg_brief.md, lg_cols_a.md, lg_cols_b.md, lg_inventory.md, lg_triage.md, lg_resolutions_1.md, lg_resolutions_2.md, lg_changes.md, lg_review.md, lg_summaries_preview.md, lg_urls.txt, lg_url_check.txt |
| GovTech Sentinel | sentinel_two_level.md (SN1 to SN7), sentinel_inventory_final.md (3e) | sentinel_brief.md, sentinel_cols_a.md, sentinel_cols_b.md, sentinel_inventory.md, sentinel_triage.md, sentinel_resolutions_1.md, sentinel_resolutions_2.md, sentinel_changes.md, sentinel_review.md, sentinel_summaries_preview.md, sentinel_urls.txt, sentinel_url_check.txt |
| Sheet 4 (candidate comparison groups) | groups_v2.md (section A table is parsed by build_groups_sheet.py) | groups.md is historical (v1, sections B to D); do not build from it |

Build entry point: `benchtest/build_two_level.py`. Which drafts it reads is set by the registry `benchtest/products.py`: MDS = two_level_v2, lg_two_level, sentinel_two_level; inventory builders = `build_lg_inventory.py` and `build_sentinel_inventory.py`, which configure `inventory_sheet.py`. It also reads `build_eval_sheet.py` (eval_tooling.md) and `build_groups_sheet.py` (groups_v2.md). Paths come from `benchtest/paths.py`. Verifiers: `verify_sentinel_apply.py` and `verify_groups_apply.py`; `verify_lg_apply.py` is legacy, in `scripts_legacy/`. See `benchtest/README.md`.

## 2. Naming convention for new products

`<slug>_<artefact>.<ext>`. Slugs: `lionguard`, `modelarmor`, `presidio`, `sdp`, `purplellama`, `cloak`, `litmus`. (Existing `lg_` and `sentinel_` keep their names; NeMo keeps its legacy names.)

Artefacts in pipeline order:

| Artefact | File | Built? |
|---|---|---|
| brief | `<slug>_brief.md` | no |
| column drafts | `<slug>_cols_a.md`, `_cols_b.md` (`_cols_c.md` if needed) | no |
| inventory draft | `<slug>_inventory.md` | no |
| evaluation tooling | `<slug>_eval_tooling.md` (only products with an evaluation-tooling sheet, e.g. litmus) | **yes** |
| triage | `<slug>_triage.md` | no |
| resolutions | `<slug>_resolutions_1.md`, `_2.md`, ... (one per resolver agent) | no |
| merged columns | `<slug>_two_level.md` | **yes** |
| merged inventory | `<slug>_inventory_final.md` | **yes** |
| change log | `<slug>_changes.md` | no |
| review | `<slug>_review.md` | no |
| preview | `<slug>_summaries_preview.md` | no |
| URL list | `<slug>_urls.txt` (one URL per line, all R9 and inventory URLs, deduplicated) | no |
| URL check | `<slug>_url_check.txt` (`<HTTP status> <URL>` per line) | no |

Only `two_level`, `inventory_final` and `eval_tooling` are read by the build. Drafts (`cols_*`, `inventory`) use the same grammar as the finals so the merge is a copy plus edits, but they also carry a `## Reviewer notes` section that must be gone from the finals.

## 3. Evidence labels

Allowed labels (bold in columns; plain bracketed text in inventory and eval-tooling cells):

| Label | Use |
|---|---|
| `[Documented]` | stated on an official vendor page (docs, vendor GitHub org, vendor HF org card, vendor-authored paper) that you read |
| `[Documented: repo <repo>@<ref>]` | official code or files; `<ref>` is a release tag or a short SHA (8 chars is enough, e.g. `PurpleLlama@172c1074`); HF repos use the revision sha (e.g. `govtech/lionguard-v1@92cc0491`); one label per repo, split bullets rather than listing repos in one label |
| `[Documented: develop/unreleased]` | only when the text exists only on an unreleased branch; never for tagged or released content |
| `[Inferred]` | a judgement or reasoning step; state the premise in the bullet |
| `[To be verified]` | a checkable fact you could not confirm; needs a source or a test |
| `[Not disclosed]` | the vendor does not say; absence claim |

Rules:

1. **Never upgrade a label** (for example Inferred or To be verified to Documented) without a URL and a verbatim quote from the official source. Record the quote in the resolutions file.
2. **Absence claims are `[Not disclosed]`, never `[Documented]`**, and name what was checked: "(checked the model card, docs page and paper; not stated)".
3. **Source hints are plain text outside the brackets**, after the label: `... [Documented] (arXiv 2507.15339 section 3)`. Do not write `[Documented: arXiv ...]`.
4. **Conflicting official sources get two bullets (or two cell facts), each with its own label**, plus a note naming the conflict; do not pick silently.
5. **A bullet carries one label and one fact.** An inference inside a documented bullet becomes a separate `[Inferred]` bullet. Each Summary label must match the facts the Summary draws on (the label is the weakest label among them).
6. **Official sources only**, defined per product in its brief:
   - Vendor docs and website (e.g. dev.meta.ai, aiguardian.gov.sg, docs.nvidia.com).
   - Vendor GitHub org (e.g. meta-llama, NVIDIA-NeMo, govtech-responsibleai), pinned by tag or SHA.
   - Vendor Hugging Face org (model cards, Spaces, datasets), pinned by revision sha.
   - Vendor-authored papers (arXiv; read the /html/ version for verbatim tables).
   - Third-party docs only where the brief allows it for a stated purpose (e.g. AWS docs for the wrapped Bedrock checks), flagged in plain text as "AWS docs, not Sentinel docs".
   - Blogs, forum posts, reviews and summaries are not evidence. A summarising fetch is not a verbatim read: re-read the raw page for any number or quote you rely on (`python benchtest/tools/fetch_text.py <url> --grep <re>`).
7. **Quoting.** Quotes are verbatim and under 40 words.
   - You may normalise whitespace, join table cells with " | ", and mark omissions with "…".
   - Code or config quotes are single lines, cited as file@ref:line.
   - **HTTP facts** (redirects, 404s, gated pages) are evidence too. Give the URL, the status and the final URL, plus the date checked. Label them `[Documented]` with plain text "(HTTP 301 to … observed 2026-10-09)".
   - **Release-note facts** cite the release page at its tag.
8. **Pinning.**
   - **Code:** pin to the **latest GitHub release tag** unless the product's seed or a ruling says otherwise. Record the canonical `owner/repo`, because the GitHub MCP follows renames silently.
   - **A docs site:** if 2–3 distinctive passages match `docs/` at the pinned tag (or a branch the site is built from), say so and pin to it. Otherwise label the site `[Documented]` without a pin and note the date read.
   - **Hugging Face:** pin to the revision sha.
9. **Moved or renamed projects.** Follow redirects, record both owners, and cite the page that states the transfer. The successor counts as official only per a ruling; see `CLAUDE.md` rule 1.

## 4. Two-level column format (`<slug>_two_level.md`, parsed by build_two_level.parse_md)

Grammar (the parser is line-based; any other line is ignored, including blank lines and prose):

```
## Column <ID>: <Product prefix>: <Header>
### R1
Summary: <one line>
Detail:
• <fact> **[Label]**
  – <sub-bullet>
### R2
...
### R9
```

- Heading regex (fill_nemo_columns.HDR_RE): `^## Column[^:]*:\s*((?:NeMo Guardrails|Llama Guard|GovTech Sentinel):.*)$`. Group 1 (prefix plus header) is the sheet 3 row-3 header and must match the Table 3 header in the brief exactly, including punctuation. **HDR_RE is derived from `benchtest/products.py`. A new product's prefix is accepted once the xlsx writer adds its registry entry (P8); drafters only need to use the exact `<Product>:` prefix fixed in the brief.** A trailing "(expanded)" is stripped by the parser.
- `<ID>` is a short column id. See "Headers and IDs" below.

### Headers and IDs (binding for every new product)
- **Header** = `<Prefix>: <function>`. It becomes the sheet 3 row-3 header and must be identical in every file that uses it: brief, columns, inventory Covered-by, sheet 4.
- **Prefix:** the product's own name as its owner writes it. Include the vendor only when it is part of the brand or needed to disambiguate (precedents: `NeMo Guardrails:`, `Llama Guard:`, `GovTech Sentinel:`). Agree it at P1 and fix it at CP1. Never change it after CP2.
- **Function part:**
  - sentence case, about 4–12 words, no trailing full stop;
  - start with the level when there is one (`Input-level …`, `Output-level …`), following R002;
  - a parenthesis may name the component or backing service, e.g. `(Analyzer)` or `(AWS Bedrock)`;
  - British spelling for ordinary words (anonymisation, organisation), but product and class names stay as the vendor spells them (Anonymizer, recognizer);
  - use "and", not "&", in new headers; existing NeMo headers keep their "&".
- **Column IDs:** a fixed prefix per product plus a number:

| Product | ID prefix | Product | ID prefix |
|---|---|---|---|
| llamaguard | LG | purplellama | PL |
| sentinel | SN | lionguard | LN |
| presidio | PD | cloak | CK |
| modelarmor | MA | litmus | (eval sheet only) |
| sdp | SD | nemo (legacy drafts) | none |
- Exactly rows `### R1` to `### R9`, each once, in a line of its own (`^### R([1-9])\s*$`). A missing, duplicate or extra row fails the assert. Every row needs one `Summary: ` line (note the space) and at least one detail line. `Detail:` is exactly that word on its own line.
- Detail lines start with `• ` (bullet and space) or, for sub-bullets, two spaces then `– ` (en dash, space). Hyphens or `*` are ignored silently, so the content disappears. Do not wrap a bullet over several lines.

Row meanings (the briefs may add product-specific wording):

| Row | Content |
|---|---|
| R1 | function: what the guardrail does |
| R2 | threat or condition it addresses (taxonomy, languages, out-of-scope items) |
| R3 | what it inspects and where it operates (input, output, needs system or user prompt as context) |
| R4 | mechanism: backing model or variant (or `[Not disclosed]`), versions supporting it, serving and integration route |
| R5 | output: verdict, score fields, extra fields, threshold guidance, published evaluation numbers |
| R6 | input and context required, including API parameters and limits |
| R7 | minimum test setup: first Detail bullet and Summary start `**Minimum setup:**`, labelled `[Inferred]` |
| R8 | open items and key open questions (unlabelled) |
| R9 | sources: one URL per Detail bullet |

Summary rules:

- Lead with a **bold phrase** (a short noun phrase or sentence), then 1 to 3 plain sentences.
- At most 45 words, R7 at most 60 (count excluding the trailing bold label).
- R1 to R7 end with one bold label, for example `**[Documented]**`. A repo pin is not put in a Summary; use plain `**[Documented]**` there.
- R8: `Summary: **Key open questions.** <comma-separated list>.` No label.
- R9: plain line, no bold, no label, for example `Meta model cards on GitHub and Hugging Face, Meta docs, papers, and the cookbook source.`
- No backticks, underscores, `$` or code identifiers (write "LionGuard 2", not `lionguard-2-binary`; "Llama Guard 3 8B", not a field name). Use ASCII digits and a plain en dash only as in the examples; no emojis.
- `**` must balance: the build splits on `**` and aborts on an odd count. Backticks are stripped at build time.
- Every claim in a Summary must be entailed by that row's Detail bullets.

Detail rules:

- One fact per `• ` bullet, ending with its bold label. Use sub-bullets only for list items that share the parent's label.
- Config keys, parameter names, model ids and commands go inline in backticks.
- R8 bullets are unlabelled; give the question and name what was checked ("checked the cards and docs, not stated"), or "needs testing".
- R9: one URL per bullet, no label, no commentary. Repo URLs are pinned (blob URL with full SHA or tag; HF tree URL with revision). Every URL cited in R1 to R8 pins must appear in an R9 bullet of that column.
- Final files contain no `## Reviewer notes`, no process language ("this draft", "I checked", "see Reviewer notes"), and no instructions to the reader.

Example (trimmed from lg_two_level.md, LG1 R1 and R8):

```
## Column LG1: Llama Guard: Input-level prompt content-safety classification
### R1
Summary: **Input-level prompt content-safety classification.** Llama Guard reads a user prompt and replies safe or unsafe, listing the violated hazard categories when unsafe. The same model also classifies responses. **[Documented]**
Detail:
• Llama Guard can classify content in LLM inputs (prompt classification) (LG3-1B, LG3-8B and LG4 model cards) **[Documented]**
• Prompt versus response is chosen by the instruction wording (role `User` for the input, `Agent` for the output); it is one model, not two (Meta LG3 and LG4 docs pages) **[Documented]**
### R8
Summary: **Key open questions.** No documented decision threshold, unclear LG4 language coverage, and latency figures only for LG3-1B-INT4 on one phone.
Detail:
• Recommended threshold for the first-token probability in LG3-8B and LG4 (checked the cards, Meta docs pages and papers, not stated)
• Which cut-off works best per version on a labelled prompt set (needs testing)
### R9
Summary: Meta model cards on GitHub and Hugging Face, Meta docs pages, and Meta papers.
Detail:
• https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/Llama-Guard4/12B/MODEL_CARD.md
```

## 5. Inventory format (`<slug>_inventory_final.md`, parsed by inventory_sheet.parse_md)

Structure:

```
# <Product> inventory (final, sheet 3x)
<blank>
Scope: ... Labels ... Short names: PL = ..., HF = ..., DOCS3 = ... (short names for sources, defined once here)
<blank>
## (a) <section name>
<optional one-paragraph intro, becomes a merged note above the table>
| col | col | ... |
|---|---|---|
| cell | cell | ... |
## (b) ...
```

- The first `#` line and the paragraph before `## (a)` are not parsed; they are for readers (title, scope, short-name legend, read date).
- Each block is found by `startswith` of the marker strings in the product config BLOCKS list: `(marker, bold block title or None, expected row count)`. The marker must match the md heading prefix exactly (`## (a) Variant table`), in order. Text under the heading that does not start with `|` is joined into the intro note. Row counts are asserted against the config; when you add or remove a row, tell the owner of the config module (build_lg_inventory.py: 8/14/9 rows; build_sentinel_inventory.py: 9/24/12/9) or the build fails. A new product needs its own config module (md path, sheet name, widths, BLOCKS, `covered` header, `markers`, validators, panel).
- Tables: header row, then a separator row of only `-`, `:` and spaces, then data rows. Every row has the same number of cells as the header. A literal pipe must not appear in a cell (use "or" or a slash); the inventory parser splits on every `|`.
- Cell rules: plain text only, no `**`, no backticks (the build strips both, but they would lose emphasis meaning). A cell may hold several facts; each fact ends with its label, then an optional plain-text source hint: `2023-12-07 [Documented] (Meta announcement post)`. A cell with several URLs separates them with ` ; ` (shown one per line).
- Allowed label forms in cells: `[Documented]`, `[Documented: repo <repo>@<ref>]`, `[Documented: develop/unreleased]`, `[Inferred]`, `[To be verified]`, `[Not disclosed]`. Do not invent forms such as `[Not found]` or `[To be verified: ...]` (earlier drafts used them; the finals normalised them).
- **"Covered by Table 3 column"** (name fixed in config `covered`): a semicolon-separated list of exact Table 3 headers (copy from the brief; the build compares with the sheet's row-3 text, and the panel counts them with COUNTIF substring matching), or exactly one of the markers `— (legacy, not in Table 3)` or `— (planned, not in Table 3)` (em dash). The amber fill and the legacy/planned counters key on these exact strings. Which markers are legal is the config `markers` tuple.
- The last column of each table is the source URL column (plain URLs).

Example (sentinel_inventory_final.md (b), one header and one row, trimmed):

```
| Guardrail ID | Suite | Owner (GovTech/AWS/Meta) | Status (Available/Planned) | Input/Output | Backing model | Covered by Table 3 column | Source URL |
|---|---|---|---|---|---|---|---|
| lionguard-2-binary | lionguard-2 [Documented] (G) | GovTech [Documented] (G) | Available [Documented] (G) | Input/Output [Documented] (G) | LionGuard 2 (OpenAI text-embedding-3-large) [Documented] (HF card, arXiv 2507.15339) | GovTech Sentinel: Localised harmful-content classification (LionGuard 2) | https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails ; https://govtech-responsibleai.github.io/playbook/tools/sentinel/ |
```

(The real table has 11 columns; the full column list is in the file.) Crosswalk blocks (hazard concept by version) have code-set validators in the config (for example S1 to S14, S1 to S11, O1 to O6 in 3d); keep codes in the form the validator regex expects.

## 6. Evaluation-tooling format (`<slug>_eval_tooling.md`, parsed by build_eval_sheet.parse_md)

Used for NeMo (eval_tooling.md, sheet 3c) and by Litmus or CyberSecEval style sheets. Rules from the parser:

- `## <Section>` headings. Only names in the parser's SECTION_ORDER (currently Overview, Tools, Datasets, Published results, Red-teaming, Engine coverage, Reuse for the test bench, Open questions) are kept, in exactly that order; a `## Revision` section is read and dropped (put review fix notes there). Any other `##` heading is ignored, and a wrong order or missing section fails the assert. A new product with different sections needs SECTION_ORDER (and MD, TITLE, NOTE) set in its builder.
- The `## Topic:` / `# ` title and the "Version scope" line above `## Overview` are not parsed.
- Inside a section, in any order:
  - `Summary: <text>` (one line; `**bold**` and a trailing label allowed, backticks stripped),
  - `Detail:` followed by `• ` and `  – ` lines (folded into one cell, subs kept),
  - markdown tables (header, separator, rows; same cell count; literal pipes written `\|`),
  - `• ` lines outside Detail (standalone bullets; `  – ` after one folds into it, otherwise assert),
  - other non-empty lines (for example "Table columns: ...") become notes.
- Table cells may use `**bold**` labels (rendered as rich text) or plain `[Label]`. Typical Tools columns: Tool | Evaluates (Table 3 columns) | Inputs | Outputs/metrics | Judge needed | Engine | Source | Label. "Evaluates" names sheet 3 headers or plain function names.
- Labels follow section 3; code reads are labelled `[Documented: repo <repo>@<tag>]` and noted "(code read, not run)" when not executed. Documented command names that differ from the code are listed as a mismatch under Open questions.
- Open questions: `• ` bullets with `[To be verified]` or `[Not disclosed]`.

## 7. Pipeline artefacts and required content

1. **Brief** (`<slug>_brief.md`, written first, shared by all drafters): scope decisions (what is in, legacy, planned, out of scope); the exact Table 3 headers numbered; official sources list with pins and tool notes (WebFetch summarises, curl or raw files for verbatim; known dead links; gated pages); "facts to RE-VERIFY" (exploration findings, marked not to be copied blindly, with numbers and ids); labels as in section 3 with product definitions of official; the format block (rows R1 to R9 with the product's meanings, Summary and Detail rules); the instruction to add `## Reviewer notes`.
2. **Column drafts** (`_cols_a.md`, `_cols_b.md`): exact section 4 grammar, plus a final `## Reviewer notes` section: contradictions between sources, uncertain items, and facts that came from summarising fetches. Inventory draft (`_inventory.md`): section 5 grammar plus Reviewer notes and a self-check; these are moved into the change log when merged.
3. **Triage** (`_triage.md`): legend (short names, label abbreviations ND, TBV, INF, SUM, class and priority definitions); counts table (by class and priority, dedup note); a table `| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |` with ids T1..Tn. Class: a = answerable from official docs or code, b = needs testing (stays open), c = licensing. Priority: H = affects a Summary or headline number, M = Detail level, L = cosmetic. Location notation names file, column, row (`LG1 R5`) and the Reviewer-note number. Also a label-hygiene section (labels that violate section 3 rules) and a contradictions section (source conflicts, with both sides).
4. **Resolutions** (`_resolutions_N.md`): header listing the items handled; "Method and access notes" (what was read raw, what was unreadable, any out-of-list source); then one `### Tn — <title>` per item with `Verdict:` (RESOLVED, PARTLY RESOLVED, STILL OPEN, CORRECTION), `Evidence:` (verbatim quotes under 40 words each with the URL or pinned path; absences naming what was checked), `Label:` (the label the fact may now carry), `Draft impact:` (exact before/after text per location, or "none"); finishing with a `## Summary table` (item, verdict, label, locations) and a `## Report` (counts, list of CORRECTIONs, Summary lines that must change with new text, items still open).
5. **Merge and change log** (`_changes.md`): inputs and outputs line; Section 1 global changes (scope, before, after, reason); Section 2 per-column and per-row changes as `Location | Before (shortened) | After (shortened) | Reason`; inventory changes per block; conflict decisions (both sources, label each, chosen text); remaining open items (each with what was checked); moved Reviewer notes; self-check (Summary word counts, ref syntax, label presence, row counts). Every substantive change to the draft appears here.
6. **Review** (`_review.md`, fresh verifier who did not merge): date and inputs read; `## Verdict: PASS | PASS WITH FIXES | FAIL`; `## Required fixes` numbered, each naming the location and giving the exact replacement text (with word counts for Summaries); `## Optional suggestions`; check sections (unlogged differences, sourcing and label strength, Summary entailment and style, source spot-checks as a table `| Claim | Location | Source URL | Verbatim quote | Match |`, inventory consistency); an appendix URL table (`| URL | Status | Used in |`).
7. **Summaries preview** (`_summaries_preview.md`): per column, one line per row `- **Rn** (<words>w, <bullets> bullets): <Summary text>`; generated from the final file, used for human checkpointing.
8. **URL files**: `_urls.txt` is every URL in R9 bullets and inventory source cells, deduplicated, one per line; `_url_check.txt` is the result, `<status> <URL>` per line (expected 200; list exceptions such as 403 or 401 gated pages with the reason in the review).

## 8. Mechanical self-checks (run before handing over any final or draft)

Run these yourself; do not rely on reading. **Use the checker.** It is stdlib-only, accepts any product prefix (so it works before registration), and its exit code is 0 when there are no errors. It is calibrated on the approved Llama Guard and Sentinel drafts, which give 0 errors. Run from the repo root:

```bash
python benchtest/tools/check_drafts.py columns   benchtest/drafts/<slug>_cols_a.md            # P2 drafts (Reviewer notes allowed)
python benchtest/tools/check_drafts.py columns   benchtest/drafts/<slug>_two_level.md --final --expect N
python benchtest/tools/check_drafts.py inventory benchtest/drafts/<slug>_inventory_final.md --headers benchtest/drafts/<slug>_two_level.md
```

The legacy snippet below works only for products already registered in `products.py`; it is kept for reference.

```python
import re, sys
sys.path.insert(0, "benchtest")   # run from the repo root; works only for REGISTERED products (prefix in products.py)
import build_two_level as B                       # imports openpyxl, python-docx; fall back to the regexes below if it fails
path = r"...\drafts\<slug>_two_level.md"
cols = B.parse_md(path, expect=N)                 # asserts: N columns, R1..R9 each once, Summary and Detail present
LAB = re.compile(r"\*\*\[(Documented(: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*\s*$")
for c in cols:
    for n, d in c["R"].items():
        s = d["summary"]
        body = LAB.sub("", s).strip()
        limit = 60 if n == 7 else 45
        words = len(re.sub(r"\*\*", "", body).split())
        assert s.count("**") % 2 == 0, (c["header"], n, "unbalanced **")
        assert not re.search(r"[`_$]", s), (c["header"], n, "code char in Summary")
        assert words <= limit, (c["header"], n, words)
        if n <= 7: assert LAB.search(s), (c["header"], n, "Summary label missing")
        if n == 8: assert s.startswith("**Key open questions.**") and not LAB.search(s)
        if n == 9: assert "**" not in s
        bl = [x for x in d["detail"] if x.startswith("• ")]
        if n <= 7: assert all(LAB.search(x) for x in bl), (c["header"], n, [x[:50] for x in bl if not LAB.search(x)])
        if n == 8: assert not any("**[" in x for x in bl)
        if n == 9: assert all(re.fullmatch(r"• https?://\S+", x) for x in d["detail"]), (c["header"], n)
        assert d["detail"][0].startswith("• "), (c["header"], n)      # first detail line is a bullet, not a sub-bullet
        if n == 7: assert "**Minimum setup:**" in s
    assert c["header"] in HEADERS                  # exact Table 3 headers from the brief
```

If `build_two_level` cannot be imported, replicate the parser with these regexes: header `^## Column[^:]*:\s*((?:<prefixes>):.*)$`, row `^### R([1-9])\s*$`, summary `startswith("Summary: ")`, `strip() == "Detail:"`, bullets `startswith("• ")` or `startswith("  – ")`. Also check:

- Every bullet in R1 to R7 ends with a label (sub-bullets `  – ` are exempt); R9 bullets are bare URLs.
- Pinned refs: every `[Documented: repo X@ref]` has a matching R9 URL containing the same ref (short SHA is a prefix of the full SHA in the URL) in the same column.
- No leftover Reviewer notes or process language in finals: `grep -n -i "reviewer notes\|this draft\|I checked\|see above" <file>` returns nothing.
- Inventories: parse with `inventory_sheet.parse_md(CFG)` (the config module's `parse_md(path)` does this) so row counts and cell counts are asserted; then check every "Covered by Table 3 column" cell against the brief headers: split on `;`, each part equals a header or the whole cell equals a marker.
- Eval tooling: `build_eval_sheet.parse_md(path)` asserts section order and table shapes.
- Sheet 4 (`groups_v2.md`, section `## A.`): 8-column table, 24 rows, row names starting `C1 `..`C24 `; columns C to H are `<br>`-joined lines, each starting `• ` except a final `Refs: ` line; no `**` or backticks; column H of single-product groups starts with `• Single-product:` (`build_groups_sheet._parse`).
- URLs: every URL returns 200 (curl -s -o /dev/null -w "%{http_code}"); record exceptions.
- Before declaring done, state the checks you ran and their output (counts of columns, Summaries, over-limit Summaries, missing labels). Do not commit; do not edit files you were not assigned.
