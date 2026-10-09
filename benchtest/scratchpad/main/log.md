# Log (append-only, newest last)

- 2026-10-09 baseline pushed: tag baseline-2026-10-09, release created (NeMo, Llama Guard, Sentinel, sheet 4 v2)
- 2026-10-09 build made portable (paths.py, products.py registry); rebuild = baseline workbook, 0 semantic diffs; verify_groups 53/53, verify_sentinel 40/40
- 2026-10-09 handover docs written: CLAUDE.md, handover_plan.md, READMEs, .claude/agents (10), settings.json, rulings R001–R008
- 2026-10-09 dry run (cold-read + presidio P0): 20 instruction gaps (7 H). Fixed: tool bootstrap, allowlist, fetch_text.py, check_drafts.py, explorer P0 template/outputs/checklist, header+ID rules (R009), R002 direction definition, quoting/pinning/redirect rules, seeds.md, Windows path in drafts README. presidio P0 kept as real P0; Q03→R010, Q04→R009; Q01/Q02 to user at CP1
- 2026-10-09 cloud first run: xlsx skill listed (anthropic-skills:xlsx); soffice present; openpyxl/docx/playwright import OK; build_two_level.py rebuild vs HEAD → TOTAL DIFFS 0 (workbook restored to HEAD); fetch_text.py smoke OK (status 200, 2 hits); check_drafts.py sentinel_two_level --final → 0 errors
- 2026-10-09 connector tool names: Context7 = mcp__Context7__resolve-library-id, mcp__Context7__query-docs; Hugging Face = mcp__Hugging_Face__hub_repo_details, hf_fs, hub_repo_search, dynamic_space, hf_whoami. Added mcp__Context7 and mcp__Hugging_Face to settings allow-list. GitHub MCP is scoped to ziqiangg/guardrail_research only → vendor repos via `git clone --depth 1 --branch <tag> <url> /tmp/<name>` (tested OK on presidio@2.2.364) or github.com blob pages via fetch_text.py
- 2026-10-09 B1 started: presidio P1, modelarmor P0, sdp P0
