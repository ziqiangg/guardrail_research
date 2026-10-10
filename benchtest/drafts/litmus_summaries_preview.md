# GovTech Litmus: Summary preview (Checkpoint 2)

Generated from litmus_eval_tooling_final.md on 2026-10-10. Format: section (words excluding the trailing label, top-level Detail bullets): Summary text. Limit 45 words (lessons 18: at most 44 excluding the label). Summaries changed from the draft are marked with an asterisk after the section name. Litmus has no Table 3 columns, so these three Summaries are the only Summary lines.

- **Overview*** (44w, 34 bullets): **Litmus is a hosted testing service for AI applications, not a runtime defence.** It scores an application's responses to curated prompts, from a web app or CI/CD. It is available to public sector teams; a May 2025 portal page labels it proof of concept. **[Documented]**
- **Red-teaming** (36w, 8 bullets): **Litmus runs curated prompts; adaptive attack generation is not described.** The playbook calls them curated adversarial prompts, and one test uses variations of the DAN jailbreak. No page mentions mutation, automated attack generation or red-team automation. **[Not disclosed]**
- **Engine coverage*** (43w, 26 bullets): **Litmus tests an application endpoint over HTTP; its scoring engine is not disclosed.** Setup needs an endpoint, an API key and a parameter specification. No list of supported models or providers, no judge model, and no support statement for guardrailed endpoints is published. **[Not disclosed]**

Counts: 3 Summaries, 2 changed (Overview, Engine coverage), 0 over the limit.
