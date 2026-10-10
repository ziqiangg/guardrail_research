# guardrail_research — shared instructions (all sessions, agents, subagents)

## Purpose
Research AI guardrail products to scope a test bench. For each product, answer 9 research questions (R1–R9) per guardrail function in the workbook. Record its variants and integration paths in an inventory sheet. Explain it in a plain-English HTML page. Finally, group functions that can be tested together (sheet 4).

The source brief is `benchtest/AI Guardrails Research and Comparison.docx`. Its objective: which functions can be evaluated together, which group goes first, and what minimum architecture v1 needs.

## Repo map (read the folder README before working there)
| Path | What | README |
|---|---|---|
| `handover_plan.md` | How the cloud manager session runs the work: phases, agents, protocol | — |
| `.claude/agents/` | Subagent definitions (`gr-*`) | (frontmatter) |
| `.claude/skills/webapp-testing/` | Vendored Playwright skill (Apache-2.0), used by the diagrammer | `SOURCE.md` |
| `benchtest/` | Workbook, docx, build/verify scripts, products registry | `benchtest/README.md` |
| `benchtest/drafts/` | All research drafts; formats, labels, naming | `benchtest/drafts/README.md` |
| `benchtest/diagrams/` | Explainer HTML pages; binding style spec | `benchtest/diagrams/README.md` |
| `benchtest/scratchpad/` | Shared memory: status, queue, rulings, agent notes | `benchtest/scratchpad/README.md` |
| `benchtest/baselines/` | Frozen workbook backups used by the verify scripts. **Never edit.** | — |

## Working directory and date
- Work from the **repo root**, the folder that contains this file. If your shell starts elsewhere, `cd` there first.
- Use `python`, not `python3`. Run scripts as `python benchtest/...`.
- Get today's date with `date +%Y%m%d`, or take it from the main session's prompt. Use it in file names.

## Tool bootstrap (some tools are deferred and must be loaded before use)
- **Web:** `ToolSearch` with query `select:WebFetch,WebSearch`.
- **GitHub:** `ToolSearch` with query `+github get_file_contents`, then `select:` the exact names it lists (`get_file_contents`, `get_latest_release`, `list_tags`, `search_code`).
- **Context7 and Hugging Face (claude.ai connectors):** `ToolSearch` with query `context7` and query `hugging face hub`, then `select:` the listed names.
- **If a tool is missing:** say so in your report and fall back to `python benchtest/tools/fetch_text.py <url>`, which gives verbatim page text, the final URL and the status.
- **Main session, first run:** record the actual connector tool names in `benchtest/scratchpad/main/log.md`. If any prompt for permission, add them to `.claude/settings.json` and commit.

## Hard rules
1. **Official sources only.** Use the vendor's docs, the vendor's GitHub or Hugging Face orgs, vendor-authored papers, and the vendor's own blog/support pages. Third-party blogs, forums and AI summaries are not sources.
   - **Context7 is a locator only:** cite the official page it points to, never Context7 itself.
   - **Ownership changes or redirects:** follow the redirect and record both owners. Treat the successor org as official only if the old official site or repo states the transfer. Then raise a question so main records a ruling.
   - Per-product official domains, repos and pins are listed in `benchtest/scratchpad/main/seeds.md`.
2. **Evidence labels** on every fact: `[Documented]`, `[Documented: repo <repo>@<tag|sha>]`, `[Documented: develop/unreleased]`, `[Inferred]`, `[To be verified]`, `[Not disclosed]`.
   - Never upgrade a label without a URL and a verbatim quote.
   - For an absence, write `[Not disclosed]` and say what you checked.
3. **Be honest about gaps.** Closed or government products (Sentinel, Litmus, Cloak) often aren't fully public. Report what you checked; never fill a gap by inference presented as fact.
4. **WebFetch summarises.** For any number or quote, use `python benchtest/tools/fetch_text.py`, or request VERBATIM text from WebFetch.
5. **Read-only on the web.** Never sign in, submit forms, call vendor APIs or download gated weights.
6. **The workbook is written only by `gr-xlsx-writer`,** one product at a time, and only after a CP2 approval ruling exists in `benchtest/scratchpad/rulings/`.
7. **Never edit `benchtest/baselines/`.** Don't rewrite history. Never force-push or tag; tags fail in cloud sessions anyway.
8. **British spelling. Arial** in all workbook cells.
9. **Python:**
   - Run `pip install -r requirements.txt` if packages are missing.
   - Run scripts as `python benchtest/<script>.py` from the repo root.
   - Set `PYTHONIOENCODING=utf-8`.
10. **Stay in your lane.** Each agent writes only the files its definition lists, plus its own `benchtest/scratchpad/<role>/` folder.

## Products
| Slug | Product | Status (baseline) |
|---|---|---|
| nemo | NVIDIA NeMo Guardrails | done (sheet 3 F–U, 3b, 3c, diagram) |
| llamaguard | Meta Llama Guard 3/4 | done (V–Z, 3d, diagram) |
| sentinel | GovTech Sentinel | done (AA–AG, 3e, diagram) |
| presidio | Presidio (created by Microsoft; moved to the independent `data-privacy-stack` org in 2026; data-privacy-stack sources are official and the prefix is `Presidio:` per R016) | done (AH–AM, 3f, diagram) |
| modelarmor | Google Cloud Model Armor | done (AT–BC, 3h, diagram) |
| sdp | Google Cloud Sensitive Data Protection (Cloud DLP) | done (AN–AS, 3g, diagram) |
| purplellama | Meta Purple Llama: Prompt Guard 2, LlamaFirewall, Code Shield (columns); CyberSecEval (eval sheet); Llama Guard (existing, cross-referenced) | done (BE–BK, 3j, 3k eval, diagram) |
| lionguard | GovTech LionGuard (self-hosted models; cross-ref Sentinel AA) | done (BD, 3i, diagram) |
| cloak | GovTech Cloak | in progress (B3) |
| litmus | GovTech Litmus (evaluation tool → eval sheet only, no Table 3 columns) | in progress (B3) |

The live phase of each product is in `benchtest/scratchpad/main/status.md`.

**Scope guide:**
- **Table 3 columns** cover functions usable on AI prompts or responses, or on their data path: retrieved text, tool calls and outputs, files or images sent to or from the model.
- **Inventory only:** functions that only process data unrelated to the AI conversation, such as bulk database scans. This is unless the user rules otherwise.
- **Uncertain cases** are CP1 questions.
- Column headers and IDs follow `benchtest/drafts/README.md` "Headers and IDs".

**Pre-approved new sheets:**
- one inventory sheet per product, lettered `3f`, `3g`, … in the order products reach the workbook;
- evaluation-tooling sheets for Litmus and CyberSecEval.

Any other new sheet needs a user ruling. Sheet 4 is regrouped once, after all products are done.

## Product checklist (definition of done)
- [ ] P0 exploration notes (`scratchpad/explorer/`)
- [ ] P1 brief `drafts/<slug>_brief.md`, with exact column headers `<Product>: <function>`
- [ ] P2 column drafts (R1–R9, Summary + Detail) + inventory draft (+ eval-tooling draft if any)
- [ ] P3 mechanical checks pass
- [ ] P4 triage → **CP1 (user)**, ruling recorded
- [ ] P5 resolutions → P6 merge (`<slug>_two_level.md`, `_inventory_final.md`, `_changes.md`, `_summaries_preview.md`)
- [ ] P7 fresh verifier PASS (fix loop done) → **CP2 (user)**, ruling recorded
- [ ] P8 xlsx write (registry entry, inventory config, rebuild) → P9 verify script passes; URL check done
- [ ] P10 diagram `diagrams/<slug>-explained.html`; verifier checklist passes; user review
- [ ] `status.md` and `log.md` updated; committed and pushed

## Manager protocol (summary — details in `handover_plan.md`)
- **The main session is a manager.** It delegates research, drafting, triage, merging, verifying, workbook writes and diagrams to `gr-*` agents. It keeps only status, rulings and agent summaries in context. It checks work with scripts, not by reading whole drafts.
- **Agents never talk to the user.** They end with a `QUESTIONS` block, and main routes each question:
  - to another agent, if a fact or source can answer it;
  - decided by main and logged as a ruling `decided_by: main`, if rules or precedent settle it;
  - batched to the user via `AskUserQuestion`, only if it is decision-bearing (scope, column split, new sheet, licensing judgement, CP1/CP2, irreversible or published actions).
- **Persist everything needed to resume** in `benchtest/scratchpad/`. Commit and push at every phase end.

## Git
- Work on the session branch. Commit messages: `<slug> P<n>: <what>`.
- End every commit with the line `Co-Authored-By: Claude <noreply@anthropic.com>`.
- The user merges pull requests on claude.ai/code. `gh pr` doesn't work in cloud sessions.
