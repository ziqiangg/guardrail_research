# R014 — Evaluation figures from vendor repo notebooks
- Date: 2026-10-09   Product: global (first use: presidio PD1)   Asked by: gr-drafter (presidio P2 cols_a, Q3)
- Question: May printed outputs in a vendor's own repo notebooks (e.g. presidio-research notebook 4: F2 0.661 on synthetic data) count as "published evaluation numbers" in R5, including the Summary?
- Ruling: Yes, label `[Documented: repo <repo>@<tag>]`, pinned to a release tag where one exists (here presidio-research 0.3.2, not HEAD). The Summary may cite a figure only with its setup qualifier in the same sentence (dataset type, e.g. "synthetic", and config, e.g. "default recognizers"); full setup goes in Detail. Derived figures (e.g. relative uplift) are `[Inferred]`. A figure is not a vendor accuracy claim and must not be presented as one.
- decided_by: main (R007 item 1: vendor GitHub is official; CLAUDE.md label rules)
