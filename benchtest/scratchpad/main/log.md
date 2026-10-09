# Log (append-only, newest last)

- 2026-10-09 baseline pushed: tag baseline-2026-10-09, release created (NeMo, Llama Guard, Sentinel, sheet 4 v2)
- 2026-10-09 build made portable (paths.py, products.py registry); rebuild = baseline workbook, 0 semantic diffs; verify_groups 53/53, verify_sentinel 40/40
- 2026-10-09 handover docs written: CLAUDE.md, handover_plan.md, READMEs, .claude/agents (10), settings.json, rulings R001–R008
- 2026-10-09 dry run (cold-read + presidio P0): 20 instruction gaps (7 H). Fixed: tool bootstrap, allowlist, fetch_text.py, check_drafts.py, explorer P0 template/outputs/checklist, header+ID rules (R009), R002 direction definition, quoting/pinning/redirect rules, seeds.md, Windows path in drafts README. presidio P0 kept as real P0; Q03→R010, Q04→R009; Q01/Q02 to user at CP1
- 2026-10-09 cloud session first-run checks (session claude/focused-fermi-tcot82):
  - PASS: soffice present; openpyxl/docx import; playwright (pip-installed this session; not from setup script); Chromium at /opt/pw-browsers; build_two_level.py rebuild vs HEAD = TOTAL DIFFS 0 (sheet 4 PASS); check_drafts.py columns sentinel_two_level.md --final = 0 errors.
  - Connectors: Context7 tools are `mcp__Context7__resolve-library-id`, `mcp__Context7__query-docs` (added `mcp__Context7` to settings allowlist). Hugging Face connector: NOT present. GitHub MCP: scoped to ziqiangg/guardrail_research only (data-privacy-stack/presidio denied).
  - FAIL: environment network policy is not Full. Proxy rejects CONNECT to data-privacy-stack.github.io, presidio.dataprivacystack.org, microsoft.github.io, docs.cloud.google.com (SDP/Model Armor docs redirect there), huggingface.co, arxiv.org, web.archive.org, www.llama.com, govtech-responsibleai.github.io, www.aiguardian.gov.sg; github.com returns 403. Reachable: cloud.google.com (top level only), pypi.org. WebFetch fails identically (ENOTFOUND). fetch_text.py smoke test failed on aiguardian.gov.sg (403 tunnel).
  - B1 NOT started; reported to user (needs Network access = Full, or the hosts allowlisted).
