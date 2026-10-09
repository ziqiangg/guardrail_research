# R015 — Label for "not built for X" statements; release-note access
- Date: 2026-10-09   Product: global (first use: presidio P4, T57; Q5)   Asked by: gr-triager (presidio P4, Q5/Q6)
- Question 1: Which label does a statement such as "LLM prompt/response screening is out of the product's stated purpose" carry when it is derived from the vendor's module list rather than quoted?
- Ruling 1: `[Inferred]`, with the premise named in the bullet (e.g. "home page module list"), applied consistently in every column. Upgrade to `[Documented]` only with a URL and a verbatim vendor sentence stating the scope (CLAUDE.md hard rule 2).
- Question 2: The GitHub MCP cannot read data-privacy-stack/*. How are tags and release notes read?
- Ruling 2: `add_repo` confirms public vendor repos are served for anonymous git reads (clone/fetch/ls-remote) by the session proxy; GitHub API (release bodies) is not available. Use `git ls-remote --tags` for the latest tag and a shallow clone at the tag (R013) for code, CHANGELOG.md and docs. Release-page text that cannot be read stays `[To be verified]`; CHANGELOG.md at the tag is an acceptable official substitute, labelled `[Documented: repo <repo>@<tag>]`.
- decided_by: main (CLAUDE.md hard rules 1–2; R013)
