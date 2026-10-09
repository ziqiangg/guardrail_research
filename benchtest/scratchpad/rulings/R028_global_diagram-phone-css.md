# R028 — Shared diagram CSS: fix phone-width overflow on all pages
- Date: 2026-10-09   Product: all diagrams   Asked by: gr-diagrammer / gr-verifier (sdp, presidio, modelarmor P10)
- Question: every page is 628 px wide on a 375 px screen (grid children with `min-width: auto` next to SVGs with a min-width). Add `.wrap > *, .stage > *, .grid2 > * { min-width: 0; }` to the shared base CSS of all pages?
- Ruling: Yes, fix all pages. Add the line to the shared base CSS block in all six pages (nemo-rails, llama-guard, sentinel, presidio, sdp, modelarmor) and to the CSS spec in diagrams/README.md §3; remove presidio's local copy from its Additions block. Style only, no content change to done products. Gate: scrollWidth == innerWidth at 375 on every page, and no element box change at 1280.
- decided_by: user (AskUserQuestion, 2026-10-09)
- Applies to: all diagrams
- Supersedes: none
