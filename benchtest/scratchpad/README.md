# scratchpad/ — shared working memory

The scratchpad is the project's persistent memory across sessions, agents and subagents. Anything a later session needs in order to resume, or anything one agent must hand to another, is written here and committed. It holds no deliverables; those live in `drafts/`, `diagrams/` and the workbook.

## Structure (exactly one level deep)

```
scratchpad/
  README.md          this file
  main/              main (manager) session only
  rulings/           decisions on questions, written by main only
  explorer/  drafter/  triager/  resolver/  merger/
  verifier/  xlsx-writer/  diagrammer/  url-checker/  grouper/
```

- Don't create sub-folders. If a new agent role is added to `.claude/agents/`, add a matching folder with a `.gitkeep`.
- Each agent writes only to its own role folder, plus the deliverables its definition allows.
- Only the main session writes to `main/` and `rulings/`.

## File naming

| Kind | Pattern | Example |
|---|---|---|
| Agent working note | `<YYYYMMDD>_<slug>_<topic>.md` | `explorer/20261010_presidio_sources.md` |
| Agent question | `<YYYYMMDD>_<slug>_q<NN>.md` | `drafter/20261010_modelarmor_q01.md` |
| Ruling | `R<NNN>_<slug>_<topic>.md` (`<slug>` = `global` if project-wide) | `rulings/R007_presidio_column-split.md` |
| Main state files | fixed names (below) | `main/status.md` |

- **Product slugs:** `nemo`, `llamaguard`, `sentinel`, `lionguard`, `modelarmor`, `presidio`, `sdp`, `purplellama`, `cloak`, `litmus`, `groups` (sheet 4), `global`.
- **Names:** lower-case. Topics use kebab-case. Dates are the session date. `<NNN>` / `<NN>` are zero-padded and sequential (ruling numbers are global across products).

## main/ (fixed files)

| File | Content |
|---|---|
| `status.md` | Product board: one row per slug with its phase (P0–P10, CP1/CP2 state), branch, last commit, blocker. Updated at every phase end. |
| `queue.md` | (1) xlsx-writer queue: products that passed CP2, in apply order. (2) Open questions: ID, asker file, routed to, state. |
| `log.md` | Append-only dated one-liners: `2026-10-10 14:02 presidio P4 triage done (31 items: a 20, b 9, c 2)`. |
| `lessons.md` | Process lessons learned. When one generalises, main updates the relevant README or `CLAUDE.md`, then notes it here. |

## Question format (agent → main)

An agent ends its final report with a `QUESTIONS` block. It also writes each question to its own folder:

```markdown
# Q<NN> — <one-line question>
- Product: <slug>   Phase: P<n>   Asked by: <agent role> (<file that raised it>)
- Context: <2–4 lines; cite files/rows, e.g. drafts/presidio_cols_a.md PR3 R4>
- Options: (a) … (b) … (c) …
- Asker's recommendation: <option + why>
- Blocking? yes/no (what is paused until answered)
```

## Ruling format (main only)

```markdown
# R<NNN> — <topic>
- Date: YYYY-MM-DD   Product: <slug|global>   Asked by: <role> (<question file>)
- Question: <verbatim or tight paraphrase>
- Options considered: (a) … (b) …
- Ruling: <the decision, stated so an agent can apply it without context>
- Decided by: user | main
- Rationale & sources: <why; cite README/CLAUDE.md rule, precedent R<NNN>, or official URL + quote>
- Applies to: <slug|all products> ; files affected: <…>
- Supersedes: <R<NNN>|none>
```

- `Decided by: user` is used for anything escalated through `AskUserQuestion`, including all CP1/CP2 approvals.
- CP approvals are rulings too, e.g. `R012_presidio_cp2-approval.md`. The xlsx writer must find a CP2 ruling for a product before it writes that product to the workbook.
- Before asking the user anything, main searches `rulings/` for precedent.

## Housekeeping
- Commit scratchpad changes together with the phase they belong to.
- Never store secrets, tokens or personal data here.
- Large raw dumps (fetched HTML, model cards) don't belong here. Keep extracts with URL + quote; put raw files in `/tmp`.
