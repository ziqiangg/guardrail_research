# benchtest/ — workbook, build pipeline, products registry

## Contents
| Path | What |
|---|---|
| `AI Guardrails Research and Comparison.xlsx` | **The deliverable.** Built entirely by scripts; never edit it by hand or with ad-hoc code. |
| `AI Guardrails Research and Comparison.docx` | Source template: 9 research questions (Table 3) and the grouping rules (Table 4). Read by every build. |
| `products.py` | **Products registry**: ordered list of products → sheet 3 column order, drafts read, inventory builder, sheet order. |
| `paths.py` | All paths (`ROOT`, `DRAFTS`, `DIAGRAMS`, `BASELINES`, `XLSX`, `DOCX`, `bak(n)`). No script hard-codes a path. |
| `build_two_level.py` | **Entry point.** Rebuilds the whole workbook and runs all verifies. |
| `build_inventory.py` | Sheet 3b (NeMo inventory) and its formula panel; LibreOffice recalc if available. |
| `build_eval_sheet.py` | Sheet 3c (NeMo evaluation tooling) from `drafts/eval_tooling.md`. |
| `inventory_sheet.py` | Generic, config-driven inventory-sheet builder and verifier (blocks, Covered-by checks, coverage panels). |
| `build_lg_inventory.py`, `build_sentinel_inventory.py` | Configs for sheets 3d and 3e. **Template for new products.** |
| `build_groups_sheet.py` | Sheet 4 (comparison groups, bands, coverage panel) from `drafts/groups_v2.md`. |
| `verify_sentinel_apply.py`, `verify_groups_apply.py` | Independent checks of the last two changes, against frozen baselines. |
| `compare_workbooks.py` | Semantic diff of two workbooks across all sheets; exit 0 means identical. |
| `tools/fetch_text.py` | Prints a page's verbatim text, its final URL and HTTP status, with an optional `--grep`. Used for quoting official sources. |
| `tools/check_drafts.py` | Mechanical checks of column and inventory drafts for any product prefix (P2/P3/P6/P7). Exit 0 means no errors. |
| `fill_nemo_columns.py`, `extract_tables.py` | Legacy first-pass steps. Other scripts import constants from them. `extract_tables.py` refuses to overwrite a filled sheet 4. |
| `scripts_legacy/` | Retired scripts; not runnable against the current workbook. |
| `baselines/` | Frozen workbook versions v2–v7 that the verifies compare against. **Never edit.** |
| `drafts/`, `diagrams/`, `scratchpad/` | See each folder's README. |

## Workbook sheet map (baseline 2026-10-09)
| Sheet | Content | Built from |
|---|---|---|
| 3. Guardrail Research Table | Rows R1–R9 (Summary row + grey Detail row, outlined). Columns: A–D fixed; E Bedrock (template example); F–U NeMo (16); V–Z Llama Guard (5); AA–AG GovTech Sentinel (7). New products append after AG in registry order. | docx + each product's `*_two_level.md` |
| 3b. NeMo Rail Inventory | Surface table, rail types, formula panel | `drafts/inventory.md` |
| 3c. NeMo Evaluation Tooling | Tools, datasets, results, reuse | `drafts/eval_tooling.md` |
| 3d. Llama Guard Inventory | Variants, category crosswalk, integration paths, coverage panel | `drafts/lg_inventory_final.md` |
| 3e. GovTech Sentinel Inventory | Model variants, guardrail catalogue, LionGuard crosswalk, access paths, panel | `drafts/sentinel_inventory_final.md` |
| 3f… (pre-approved) | One inventory sheet per new product, lettered in the order products reach the workbook; plus eval-tooling sheets for Litmus and CyberSecEval | `drafts/<slug>_inventory_final.md` / `<slug>_eval_tooling.md` |
| 4. Candidate Comparison Groups | 24 groups (6 multi-product, 18 single-product) + coverage panel | `drafts/groups_v2.md` |

## Running the build
```bash
pip install -r requirements.txt
PYTHONIOENCODING=utf-8 python benchtest/build_two_level.py
PYTHONIOENCODING=utf-8 python benchtest/verify_groups_apply.py
PYTHONIOENCODING=utf-8 python benchtest/verify_sentinel_apply.py
```
- Run from any directory; paths resolve from `paths.py`.
- **Known non-failures:**
  - `FAIL F16 ['words=66']`: a NeMo Summary that is over the length limit and has been since v4.
  - `non-Arial cells rows 4-21: 27`: the cells merged away under A–C.
- **Recalculation:** the formulas in the 3b, 3d, 3e and sheet 4 panels are written without cached values. `build_inventory.py` recalculates them only if `soffice` (LibreOffice) is on PATH **and** the xlsx skill's `recalc.py` is found. The skill is found via `XLSX_SKILL_DIR`, or by a search under `~/.claude/skills` or `~/.claude/plugins`. Otherwise Excel computes them when the file is opened.
- **openpyxl saves are not byte-reproducible**, because of zip timestamps. Compare workbooks with `compare_workbooks.py`, never by bytes. If a rebuild shows no semantic diff, discard the byte change with `git checkout -- "benchtest/AI Guardrails Research and Comparison.xlsx"`.

## Adding a product (done only by `gr-xlsx-writer`, after CP2)
1. Final drafts exist and were approved: `drafts/<slug>_two_level.md` and `<slug>_inventory_final.md`, plus `<slug>_eval_tooling.md` if the product has an eval sheet.
2. Add one entry to `PRODUCTS` in `products.py`. The `header_prefix` must exactly match the drafts' `<Product>:` prefix. `HDR_RE`, `MDS` and the sheet `ORDER` derive from the registry automatically.
3. Create `build_<slug>_inventory.py` by copying `build_sentinel_inventory.py`. Set:
   - `md`, `sheet` and `after` (the previous inventory sheet);
   - `BLOCKS` (section markers and row counts from the md);
   - `WIDTHS`;
   - the Covered-by markers;
   - validators;
   - the coverage-panel spec.

   `build_two_level.py` imports every registered builder module automatically.
4. **Eval-tooling sheets** (Litmus, CyberSecEval): `build_eval_sheet.py` is NeMo-specific. Generalise it the way `inventory_sheet.py` generalised the inventories, with config-driven sheet name, md path and section order. Register the new sheet in `EXTRA_SHEETS`, with `after` set to its product's inventory sheet. Prove sheet 3c is unchanged.
5. Rebuild, then write `verify_<slug>_apply.py` modelled on `verify_sentinel_apply.py`. It compares against the previous commit's workbook (`git show HEAD:...`) and checks:
   - every pre-existing sheet and column is semantically unchanged;
   - the new columns equal the md and pass the Summary style checks;
   - the new sheet equals the md;
   - Covered-by values are real sheet 3 headers;
   - XML hygiene is 0/0/0;
   - URLs are harvested to `drafts/<slug>_urls.txt`.
6. Commit "<slug> P8: apply to workbook" with the workbook, scripts and registry together.

**Baselines vs git:** `baselines/` freezes v2–v7 because the existing verifies need them. New work doesn't create v8, v9 and so on. The previous commit is the baseline, so take it from `git show HEAD:<path>`.

## Style rules the build enforces on sheet 3 Summaries
- First run bold for R1–R8.
- A bold label in R1–R7.
- No `**`, backticks, `_` or `$`.
- At most 60 words, and no newline.
- Arial throughout.
- XML hygiene: 0 unpreserved `<t>`, 0 `<r>` without `rPr`, 0 empty `<t>`.
