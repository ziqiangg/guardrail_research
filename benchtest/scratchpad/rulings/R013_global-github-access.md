# R013 — Vendor GitHub access in cloud sessions
- Date: 2026-10-09   Product: global   Asked by: gr-explorer (modelarmor P0, Q04); gr-drafter (presidio P1)
- Question: The GitHub MCP is scoped to this repo and github.com pages return 403 through fetch_text.py. How are vendor repos read?
- Ruling: Read vendor repos from a shallow clone: `git clone --depth 1 [--branch <tag>] <https url> /tmp/<name>` (this form matches the allow-list), and cite github.com blob URLs at the pinned tag/sha. If a clone is denied or fails, record "checked, not reachable" and label `[To be verified]`; never use unofficial mirrors and never work around a permission denial. For products without a vendor repo (Model Armor, SDP), Google sample repos are supporting only; their absence is a recorded gap, not a blocker.
- decided_by: main (CLAUDE.md tool bootstrap fallback; handover §4 failure handling)
