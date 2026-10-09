# Handover plan — semi-automated guardrail research in Claude Code cloud

You are the **main (manager) session**. Read `CLAUDE.md` first, then this file, then `benchtest/scratchpad/main/status.md` and the `benchtest/scratchpad/rulings/` index.

**Resuming?** If `benchtest/scratchpad/main/handover_20261010.md` (or a later `handover_*.md`) exists, read it right after this file; it states the exact next step.

Your job is to run the remaining products through the pipeline below, 2–3 at a time, using the `gr-*` subagents. You do not research, draft or write the workbook yourself.

## 1. State at handover (2026-10-09)
- **Done:** NeMo (16 columns, 3b, 3c, diagram), Llama Guard (5 columns, 3d, diagram), Sentinel (7 columns, 3e, diagram), and sheet 4 (24 groups).
- **Baseline:** the tag `baseline-2026-10-09`. After it, the build was made portable and registry-driven; the workbook is semantically identical.
- **To do**, in batches:

| Batch | Products | Notes |
|---|---|---|
| B1 | presidio, modelarmor, sdp | Well documented. Establishes the rhythm. **presidio P0 is already done** (dry run, `explorer/20261009_presidio_p0.md`), so start presidio at P1. Its open questions Q01 and Q02 go to the user at presidio CP1 (`main/queue.md`). |
| B2 | purplellama, lionguard | See the scope rulings R004 and R005. |
| B3 | cloak, litmus | GovTech; public docs are probably sparse, so expect honest gaps. Litmus gets an eval sheet only. |
| Final | sheet 4 regroup (`gr-grouper`) | After all products are in the workbook. Needs user approval. |

## 2. One-time setup (user, before the first cloud session)
1. **Claude GitHub App:** install it on `ziqiangg/guardrail_research`. It gives cloud access and lets PRs be created from claude.ai/code.
2. **claude.ai/code → Environments → new environment** for this repo:
   - Network access: **Full**.
   - Setup script, pasted verbatim. It runs as root and is cached for about 7 days if it finishes within about 5 minutes:
     ```bash
     #!/bin/bash
     set -e
     apt-get update -qq
     DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends libreoffice-calc fonts-liberation
     pip install -q -r requirements.txt || pip install -q openpyxl==3.1.5 python-docx lxml pandas markitdown
     pip install -q playwright && python -m playwright install --with-deps chromium
     ```
   - Environment variables: none required. Don't put secrets in them.
3. **claude.ai → Customize:**
   - enable the **xlsx** skill (Anthropic document skills; it is licensed, so it is not vendored in the repo);
   - add the **Context7** and **Hugging Face** connectors.
4. **Start a cloud session** on `main` with the prompt: *"Read CLAUDE.md and handover_plan.md, then run batch B1."* The session works on its own branch. Open a PR from claude.ai/code when you want to merge.

**First-run checks (main session):**
- Confirm `xlsx` is listed under skills.
- Confirm the Context7, Hugging Face and GitHub tools respond.
- Run `which soffice` and `python -c "import openpyxl, docx, playwright"`.
- Run the build once: `PYTHONIOENCODING=utf-8 python benchtest/build_two_level.py`. Then compare against HEAD with `benchtest/compare_workbooks.py`; it must show 0 diffs.
- Load the tools as in `CLAUDE.md` "Tool bootstrap". Record the exact Context7 and Hugging Face tool names in `log.md`. If they differ from the `mcp__…` entries in `.claude/settings.json`, add them and commit (`chore: allow connector tools`). Otherwise an unattended run stalls on permission prompts.
- Smoke-test the helpers: `python benchtest/tools/fetch_text.py https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails --grep "the default" --max 2`, and `python benchtest/tools/check_drafts.py columns benchtest/drafts/sentinel_two_level.md --final`, which must give 0 errors.
- Record the results in `scratchpad/main/log.md`. If any check fails, report it to the user before starting B1.

## 3. Pipeline per product (P0–P10)
`<slug>` is the product slug. Every phase ends with a commit `<slug> P<n>: …`, a push, an update to `status.md`, and a line in `log.md`.

| Phase | Agent(s) | Input | Output | Exit check (main) |
|---|---|---|---|---|
| P0 Explore | gr-explorer ×1–2 (split by docs vs code/models: `_p0-docs`, `_p0-code`) | slug, today's date, `main/seeds.md` entry, rulings | `scratchpad/explorer/<date>_<slug>_p0.md` (template in gr-explorer.md) + q-files | proposed columns + inventory blocks, sources, gaps, conflicts; main updates `seeds.md` (drop UNVERIFIED) and routes questions |
| P1 Brief | gr-drafter | explorer notes + rulings | `drafts/<slug>_brief.md`: scope, **exact column headers** `<Product>: <function>`, inventory blocks, sources, facts to re-verify, labels, format (copy the structure of `sentinel_brief.md`) | main reads the headers and scope section only. A new column split or scope question is batched to the user with CP1. |
| P2 Drafts | gr-drafter ×2–3 in parallel: cols A, cols B (split columns ~evenly), inventory (+ eval tooling) | brief | `<slug>_cols_a.md`, `_cols_b.md`, `_inventory.md` (+ `_eval_tooling.md`) | each agent's self-check output |
| P3 Mechanical | main runs `python benchtest/tools/check_drafts.py` (no agent) | drafts | — | `columns` on each cols file → 0 errors; `inventory` on the inventory draft → 0 errors (Covered-by checked once finals exist) |
| P4 Triage | gr-triager | brief + drafts | `<slug>_triage.md` | counts per class; H items |
| **CP1** | **user** | counts, top H items, conflicts, any column-split/scope question | ruling `R<NNN>_<slug>_cp1.md` (`decided_by: user`) | approval recorded |
| P5 Resolve | gr-resolver ×1–2 (split by topic) | triage (a)+(c) items | `<slug>_resolutions_<N>.md` | counts per verdict; CORRECTIONs listed |
| P6 Merge | gr-merger | drafts + triage + resolutions + rulings | `<slug>_two_level.md`, `_inventory_final.md` (+`_eval_tooling.md`), `_changes.md`, `_summaries_preview.md` | `check_drafts.py columns <two_level> --final --expect N` and `inventory <final> --headers <two_level>` → 0 errors |
| P7 Verify | gr-verifier (fresh, Opus) → fixes via SendMessage to the **same** gr-merger | finals + originals + evidence | `<slug>_review.md`; merger appends "Verifier fixes" | verdict PASS or all required fixes applied; main re-runs P3 |
| **CP2** | **user** | `_summaries_preview.md` link, inventory preview (block names + row counts), open-item counts, judgement calls | ruling `R<NNN>_<slug>_cp2-approval.md` | approval recorded → product appended to `main/queue.md` |
| P8 Apply | gr-xlsx-writer (**one at a time**, in queue order) | CP2 ruling + finals | workbook, registry, `build_<slug>_inventory.py`, `verify_<slug>_apply.py` | agent's verify passes; main runs `compare_workbooks.py` on HEAD vs new: diffs only in new columns/sheet |
| P9 URLs | gr-url-checker | `drafts/<slug>_urls.txt` | `<slug>_url_check.txt` | 0 `broken`/`network` (else route to gr-resolver to fix the source, then re-merge → re-apply) |
| P10 Diagram | gr-diagrammer → gr-verifier (diagram review) | finals + diagrams README | `diagrams/<slug>-explained.html` | checklist all ticked; then **user review** (non-blocking: other products continue) |

**Parallelism:**
- Up to 3 products run P0–P7 concurrently, each in its own agents.
- P8 is serialised through `main/queue.md`, because the workbook is binary and can't be merged.
- P10 can run in parallel with other products' work.
- Never run two `gr-xlsx-writer` agents at once, and never let any other agent touch the workbook.

**Product-specific notes** (these are rulings; see `rulings/`):
- **purplellama:**
  - Table 3 columns for Prompt Guard 2 (Prompt Guard 1 is legacy, inventory only), each LlamaFirewall scanner (PromptGuard, AlignmentCheck, CodeShield, regex/custom), and Code Shield.
  - CyberSecEval goes in an eval-tooling sheet.
  - The existing Llama Guard columns stay untouched and are cross-referenced.
  - One HTML page covers the whole umbrella and links `llama-guard-explained.html`.
- **lionguard:**
  - A standalone, self-hosted product: the HF models 2, 2.1 and Lite, plus 1 as legacy.
  - Input and output columns, per R002.
  - Cross-reference Sentinel column AA and sheet 3e, and don't duplicate facts beyond what the columns need.
- **litmus:** an evaluation tool. Eval-tooling sheet plus HTML; no Table 3 columns.
- **cloak:** GovTech's PII service. The playbook says its Sentinel integration is "coming soon"; cross-reference Sentinel AF.
- **sdp:** Google Cloud Sensitive Data Protection, formerly Cloud DLP. Cover the inspection and de-identification functions as separate columns, as the evidence supports.

## 4. Manager protocol
**Context discipline**
- Keep only the following in your context: `status.md`, `queue.md`, ruling titles, agent final reports and script outputs.
- Don't open full drafts. When you need to know something from a file, run a script (grep, parse, count) or ask an agent.
- Delegate every research, drafting, triage, merge, verify, write and diagram task.
- Give each subagent prompt:
  - today's date (`YYYYMMDD`);
  - the slug and phase;
  - exact input and output paths;
  - the relevant ruling IDs;
  - "read CLAUDE.md and <README>";
  - the required report format.
- Prefer resuming an agent with SendMessage over spawning a new one when continuing its own work: fix loops, rate-limit resumes, follow-ups. Use a **fresh** agent for verification.

**Question routing.** Agents end with a `QUESTIONS` block; you are the proxy. For each question, in order:
1. **Precedent:** search `scratchpad/rulings/`. If a ruling covers it, answer by citing that ruling.
2. **Rules:** if `CLAUDE.md` or a README settles it, rule `decided_by: main` and cite the rule.
3. **Facts:** if it is a factual or source question, route it to a gr-explorer (or the product's gr-resolver), get the answer with URL and quote, rule `decided_by: main`, and resume the asker with the answer.
4. **Conflicts:** for a conflict between agents or drafts, prefer the more primary source with a verbatim quote (code at a pinned ref over docs; official docs over a blog). Log both sides.
5. **Otherwise escalate.** Escalate to the user only for decision-bearing questions:
   - scope or column-split changes;
   - new sheets outside the pre-approved series;
   - reversing a user ruling;
   - licensing or terms judgements;
   - anything irreversible or published;
   - CP1 and CP2.

   Batch escalations into one `AskUserQuestion` call: up to 4 questions, each with options and your recommendation first. Combine them with the next CP when one is due.
6. **Record:** write each ruling file, add it to `queue.md` under resolved questions, and resume the blocked agent.

**Auto-answer defaults** (rule without the user):
- formatting, naming and label hygiene, per the READMEs;
- word limits;
- how to cite a source;
- whether a vendor blog counts as official: yes, if it is on the vendor's domain;
- archived official pages (Wayback) count as `[Documented]` with "(archived official page, <date>)", while current availability stays `[To be verified]`;
- dropping an optional suggestion;
- choosing between two equivalent wordings;
- retrying a failed fetch through another official mirror.

**Failure handling**
- **Rate limit or session limit:** the agent stops. Resume it with SendMessage ("continue where you left off; the file X doesn't exist yet"). Check whether it wrote partial files first.
- **VM reclaimed or new session:** read `status.md`, `queue.md` and `log.md`, plus `git log --oneline -20`, then resume each product at its recorded phase. Treat uncommitted work as lost and redo that phase.
- **A source returns 403/404, or is gated or regional:** try the official alternates (raw docs repo, archived official page, vendor PDF). Otherwise record "checked X, not reachable" and give the item `[To be verified]`. Never use unofficial copies.
- **A check fails after P8:** stop the queue, resume the xlsx writer with the failure output, and don't apply the next product until it passes.
- **A vendor product is renamed or deprecated mid-run:** that's a scope question, so batch it to the user.

## 5. Definitions of done
**Product:** every item in the `CLAUDE.md` checklist is ticked, and:
- `status.md` says `done`;
- the CP1 and CP2 rulings exist;
- the workbook verify passes;
- the URL check has 0 broken links;
- the diagram is reviewed;
- everything is pushed.

**Run:**
- all 7 new products are done;
- sheet 4 is regrouped and approved;
- a final full-workbook rebuild shows 0 unexpected diffs;
- the URL check across all products is clean;
- there is a summary for the user listing deliverables, open items per product, and suggested next steps (which comparison group to test first, as the source docx asks);
- a PR is opened on claude.ai/code.

## 6. Model and effort map (from `.claude/agents/`)
| Agent | Model / effort |
|---|---|
| Main session | Opus 5.5, high |
| gr-explorer | Sonnet, medium |
| gr-drafter, gr-triager, gr-resolver, gr-merger, gr-diagrammer, gr-grouper | Sonnet, high |
| gr-verifier | Opus, high |
| gr-xlsx-writer | Sonnet, medium (xlsx skill) |
| gr-url-checker | Haiku, low |

If quality slips, raise the drafter to Opus for that product and log it in `lessons.md`.
