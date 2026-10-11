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
| `build_<slug>_inventory.py`, `build_purplellama_eval.py`, `build_litmus_eval.py` | Per-product inventory configs (3d–3m) and the extra eval-tooling sheets (3k, 3n). `build_cloak_inventory.py` / `build_lionguard_inventory.py` are the newest templates. |
| `build_groups_sheet.py` | Sheet 4 (comparison groups, bands, coverage panel) from `drafts/groups_v3.md`. |
| `verify_<slug>_apply.py`, `verify_groups_v3_apply.py` | One-shot independent checks of each product's apply and of the sheet-4 regroup, against the commit before it (they fail afterwards on the "only X is new" check; see scratchpad lessons 14 and 16). `verify_sentinel_apply.py` and `verify_groups_apply.py` are pinned to frozen baselines and now fail on sheet/column counts only. |
| `compare_workbooks.py` | Semantic diff of two workbooks across all sheets; exit 0 means identical. |
| `tools/fetch_text.py` | Prints a page's verbatim text, its final URL and HTTP status, with an optional `--grep`. Used for quoting official sources. |
| `tools/check_drafts.py` | Mechanical checks of column and inventory drafts for any product prefix (P2/P3/P6/P7). Exit 0 means no errors. |
| `fill_nemo_columns.py`, `extract_tables.py` | Legacy first-pass steps. Other scripts import constants from them. `extract_tables.py` refuses to overwrite a filled sheet 4. |
| `scripts_legacy/` | Retired scripts; not runnable against the current workbook. |
| `baselines/` | Frozen workbook versions v2–v7 that the verifies compare against. **Never edit.** |
| `drafts/`, `diagrams/`, `scratchpad/` | See each folder's README. |

## Workbook sheet map (2026-10-11, all ten products)
| Sheet | Content | Built from |
|---|---|---|
| 3. Guardrail Research Table | Rows R1–R9 (Summary row + grey Detail row, outlined). Columns: A–D fixed; E Bedrock (template example); F–U NeMo (16); V–Z Llama Guard (5); AA–AG GovTech Sentinel (7); AH–AM Presidio (6); AN–AS Sensitive Data Protection (6); AT–BC Model Armor (10); BD LionGuard (1); BE–BK Purple Llama (7: Prompt Guard 2 / LlamaFirewall / Code Shield prefixes); BL–BN Cloak (3). Litmus has no columns. New products append in registry order. | docx + each product's `*_two_level.md` |
| 3b. NeMo Rail Inventory | Surface table, rail types, formula panel | `drafts/inventory.md` |
| 3c. NeMo Evaluation Tooling | Tools, datasets, results, reuse | `drafts/eval_tooling.md` |
| 3d. Llama Guard Inventory | Variants, category crosswalk, integration paths, coverage panel | `drafts/lg_inventory_final.md` |
| 3e. GovTech Sentinel Inventory | Model variants, guardrail catalogue, LionGuard crosswalk, access paths, panel | `drafts/sentinel_inventory_final.md` |
| 3f–3n | 3f Presidio, 3g SDP, 3h Model Armor, 3i LionGuard, 3j Purple Llama, 3k CyberSecEval Eval Tooling, 3l Cloak, 3m Litmus, 3n Litmus Eval Tooling (inventory sheets lettered in the order products reached the workbook; eval sheets follow their product's inventory) | `drafts/<slug>_inventory_final.md` / `<slug>_eval_tooling_final.md` |
| 4. Candidate Comparison Groups | 34 groups (14 multi-product, 20 single-product) + coverage panel; regrouped once after all products (R006, R042) | `drafts/groups_v3.md` |

## Running the build
```bash
pip install -r requirements.txt
PYTHONIOENCODING=utf-8 python benchtest/build_two_level.py
# after a change: compare the rebuilt workbook with the last commit (diffs only where intended)
git show HEAD:"benchtest/AI Guardrails Research and Comparison.xlsx" > /tmp/prev.xlsx
PYTHONIOENCODING=utf-8 python benchtest/compare_workbooks.py /tmp/prev.xlsx "benchtest/AI Guardrails Research and Comparison.xlsx"
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
