# Lessons (process)

Lessons carried over from the NeMo, Llama Guard and Sentinel runs. When a lesson generalises, fold it into a README or `CLAUDE.md` and note it here.

1. **WebFetch summarises.** Numbers drawn from summarised fetches caused errors that a verifier later caught (e.g. Llama Guard PGD 6% vs 22%). Always request verbatim text, or read the raw HTML or arXiv html.
2. **raw.githubusercontent.com may reset the connection.** Use github.com blob pages (`?plain=1`), the GitHub MCP, or a shallow clone.
3. **Agents can hit session limits mid-task without writing their output.** Check for partial files before resuming, then resume with SendMessage.
4. **Brief facts were wrong several times** (LG1 code order, "English only" for 11B-V). Drafters must re-verify everything in the brief.
5. **A fresh verifier always found 4–9 required fixes** after the merge. Never skip P7.
6. **Leftover old text after a correction** is the most common merge defect. The verifier must grep for the known-wrong strings listed in the resolutions.
7. **Readability:** dense prose in sheet 4 was rejected. Use short bullets of 12 words or fewer, with references on a grey `Refs:` line.
8. **The user's workbook may be open in Excel** (`~$` lock file); check before any write when working locally.
9. **openpyxl saves are not byte-reproducible.** Compare workbooks with `benchtest/compare_workbooks.py`.
10. **Products move.** Presidio left Microsoft for the `data-privacy-stack` org; the GitHub MCP followed the rename silently. Always record the canonical `owner/repo` and the final URLs (dry run, 2026-10-09).
11. **Cold-read dry runs find real gaps.** Re-run one after any major instruction change.
