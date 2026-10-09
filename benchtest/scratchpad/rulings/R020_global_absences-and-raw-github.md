# R020 — Absence labels; raw.githubusercontent.com fallback for vendor code
- Date: 2026-10-09   Product: global   Asked by: gr-resolver (sdp P5 r1, Q2/Q5)
- Ruling 1: A statement that something is not published/offered is `[Not disclosed]` with what was checked (CLAUDE.md hard rule 2). A positive documented definition beside it keeps its own `[Documented]` label. Only scope/purpose conclusions drawn from a vendor's module or feature list are `[Inferred]` (R015).
- Ruling 2: Amends R013. If a shallow clone is denied or fails, read vendor files at a pinned tag via `python benchtest/tools/fetch_text.py https://raw.githubusercontent.com/<org>/<repo>/<tag>/<path>` and cite the github.com blob URL at the same tag. Never work around a permission denial by other means; if both fail, `[To be verified]`.
- decided_by: main (CLAUDE.md hard rules 1–2; R013; lessons.md item 2)
