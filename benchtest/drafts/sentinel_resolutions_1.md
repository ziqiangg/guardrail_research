# Sentinel resolutions, agent 1 (LionGuard models, papers, HF repos, model licences)

Items: T22, T23, T24, T25, T26, T27, T28, T29, T30, T31, T32, T45, T46, T48, T49, T70, T71, T72, T74, T75 (20 items). Nothing else was edited.

## Method and access notes (read first)

- Short names. A = `sentinel_cols_a.md` (SN1 = LionGuard column, SN3 = off-topic column). B = `sentinel_cols_b.md` (SN4 = leakage column). INV(a)/(c)/(d) = `sentinel_inventory.md` sections (a) model variant table, (c) crosswalk, (d) access paths; INV-RN = its Reviewer notes. G = aiguardian.gov.sg Sentinel-Guardrails page. PBL = playbook LionGuard page. LG2P = arXiv 2507.15339 (html v2, read 2026-10-08). LG1P = arXiv 2407.10995. OTP = arXiv 2411.12946. RBP = RabakBench paper arXiv 2507.05980 (GovTech-affiliated authors; dataset `govtech/RabakBench`; used only as a cross-check for T22).
- Nothing came from a summarising fetch. WebFetch was not used. arXiv `/html/` pages, `/abs/` pages, blog.ai.gov.sg pages and playbook pages were downloaded with curl; tables were parsed from the raw HTML cell by cell. HF files were read raw from `huggingface.co/<repo>/resolve/<sha>/<file>`; shas, dates and commit lists come from the HF Hub API. Safetensors headers were read by byte-range request (tensor shapes only; no weights loaded). The leakage pickle was never loaded or executed; its opcode stream was listed with `pickletools.genops` (static parse, run with `python -I`).
- Pins used (full shas): `govtech/lionguard-v1@92cc0491764602c97031693a7f1a2bcc82c6aaf9`, `govtech/lionguard-2@be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591`, `govtech/lionguard-2.1@1c3a9ea7718f81ea32e6688c0ff18ac8866525e8`, `govtech/lionguard-2-lite@d56c17a08a937f2591a906fb5c8ec699a844c422`, `govtech/jina-embeddings-v2-small-en-off-topic@806cf24c6786533036354a18b485a90620be210f`, `govtech/stsb-roberta-base-off-topic@505c86b18bc66ce68492376e47a748a7ac10e422`; Spaces `govtech/system-prompt-leakage@0161b10c0549a471392821cb89f09dea6fcd1e45`, `govtech/lionguard-demo@4ade46d19acee9c9088c711533a7c47fe24a8e3b`, `govtech/off-topic-demo@025255e92b26c8902dec96ec5f72f730e1bf429e`. Same shas as the drafts. Safetensors headers were read from `main`, which equals these shas on 2026-10-08.
- Playbook pin: `govtech-responsibleai/playbook@97338569d8711ae4c7a6615a34deb92a720beba8` (2026-08-04) is the head I saw. `website/docs/tools/lionguard.md` has exactly one commit in the history, `8cd4c0616464c1ff548373e4972f410ec11e295b` (2026-07-29, "release: v2.0.0"). The rendered page says "Last updated on Jul 28, 2026".
- Quote rule: quotes are verbatim and under 40 words.
- NEW source found (affects T28, T29, T23, T31): GovTech blog "Decision Models for Guardrails: Exploring Jev and Kev for Moderation", `https://blog.ai.gov.sg/decision-models-for-guardrails-exploring-jev-and-kev-for-moderation/`, dated 28 Sep 2026. It contains a table of binary F1 for LionGuard 2.1. Also relevant: blog "Guardrails in the Wild: Closing the Retraining Loop for LionGuard 2", `https://blog.ai.gov.sg/guardrails-in-the-wild-closing-the-retraining-loop-for-lionguard-2/`, dated 21 Aug 2026. Both are Sentinel-relevant; the other agent may want them for the retraining and default-model questions (that blog says the first retrained LionGuard 2 model is rolling out to Sentinel users "very soon").

---

### T22 — RabakBench per-language columns (Table 1 versus Table 3)
- Verdict: RESOLVED (with CORRECTION to the "unresolved" wording). The paper's Table 3 column headers are very probably mislabelled; Chinese is 87.8 and Malay is 78.4. The paper alone does not say so, but a second GovTech paper settles it.
- Evidence:
  - LG2P Table 1 (`https://arxiv.org/html/2507.15339`), verbatim header rows: "Embeddings | Test | RabakBench" then "SS | ZH | MS | TA". Row: "text-embedding-3-large 3,072d OpenAI (2025) | 77.0 | 88.1 | 87.8 | 78.4 | 66.6".
  - LG2P Table 3, verbatim header rows: "Moderator | Test | RabakBench | SGHateCheck | SGToxic Guard" then "SS | MS | ZH | TA | SS | MS | ZH | TA | SS | MS | ZH | TA". Row: "LionGuard 2 | 77.0 | 88.1 | 87.8 | 78.4 | 66.6 | 98.8 | 92.1 | 97.4 | 64.5 | 99.7 | 98.2 | 99.2 | 71.5".
  - Table 3 caption: "(–) indicates that the model does not support that language." AWS row: "AWS Bedrock Guardrails | 57.1 | 69.6 | – | 21.1 | – | 82.2 | – | 40.6 | – | 91.5 | – | 74.2 | –".
  - html v1, html v2 and the PDF (`https://arxiv.org/pdf/2507.15339v2`, text extracted with pdftotext) agree: Table 1 reads "SS ZH MS TA", Table 3 reads "SS MS ZH TA". The two tables are the same in v1 and v2 for these cells. No text in the paper states which order is right.
  - Blog (`https://blog.ai.gov.sg/introducing-lionguard-2-multilingual-llm-guardrail-for-singapore/`, 29 Jul 2025): "Performance remains robust for Chinese (88%) and Malay (78%)". This matches the Table 1 order.
  - Cross-check, RBP Table 4 (`https://arxiv.org/html/2507.05980`), header "Type | Guardrail | Singlish | Chinese | Malay | Tamil | Average". Rows: Google Cloud Model Armor "62.37 | 67.95 | 74.30 | 73.56"; LlamaGuard 4 12B "60.53 | 54.20 | 65.92 | 73.77"; LlamaGuard 3 8B "54.76 | 53.05 | 52.81 | 46.84"; AWS Bedrock Guardrail "66.50 | 0.59 | 18.49 | 0.57".
  - The same systems in LG2P Table 3 (SS, "MS", "ZH", TA): Model Armor 62.5, 68.3, 74.0, 73.4; LlamaGuard 4 60.6, 54.6, 65.2, 73.0; LlamaGuard 3 55.2, 53.6, 53.1, 47.3; AWS 69.6, –, 21.1, –. The numbers line up with RBP's Chinese then Malay, not with Table 3's printed MS then ZH. AWS fits too: RBP has AWS near zero on Chinese and about 18 on Malay, and Table 3 has the dash in the column printed "MS" and 21.1 in the column printed "ZH".
  - New blog evidence for 2.1 (T28) also lists Chinese above Malay: "RabakBench Malay | 0.8420", "RabakBench Chinese | 0.8688".
- Label to use: Chinese 87.8 and Malay 78.4 for LionGuard 2 on RabakBench: [Documented] (LG2P Table 1 and the blog agree). "Table 3 header order MS then ZH is a labelling error": [Inferred] (my comparison of Table 3 numbers with RBP Table 4). The same swap very probably applies to the SGHateCheck and SGToxicGuard column groups of Table 3, so Malay and Chinese for those would be 97.4 and 92.1 (SGHateCheck) and 99.2 and 98.2 (SGToxicGuard) [Inferred]; RBP has no SGHateCheck or SGToxicGuard figures, so this part is not independently checked. If you want a single hedge, use [To be verified] only for those two groups.
- Draft impact:
  - A SN1 R5 bullet "Table 3 (localised), LionGuard 2 as printed: RabakBench columns 88.1, 87.8, 78.4, 66.6; SGHateCheck ...; SGToxicGuard ..." Replace with: "RabakBench binary F1 at 0.5, LionGuard 2: Singlish 88.1, Chinese 87.8, Malay 78.4, Tamil 66.6 (Table 1 order; the blog says Chinese 88% and Malay 78%) **[Documented]**".
  - A SN1 R5 bullet "Table 3 ... as printed" for SGHateCheck and SGToxicGuard: replace with "Table 3 also gives SGHateCheck 98.8, 92.1, 97.4, 64.5 and SGToxicGuard 99.7, 98.2, 99.2, 71.5 under the printed header SS, MS, ZH, TA; the printed Malay and Chinese labels are probably swapped (see next bullet), so the values for Chinese and Malay on these two sets are **[To be verified]**".
  - A SN1 R5 bullet "Language-column conflict: Table 1 labels ... Table 3 labels ...": replace with "Table 1 labels the RabakBench columns SS, ZH, MS, TA and Table 3 labels them SS, MS, ZH, TA with identical LionGuard 2 values; the Table 3 row for LlamaGuard 4, LlamaGuard 3 and Model Armor matches the GovTech RabakBench paper only if Chinese comes before Malay, so Table 3's header is probably mislabelled **[Inferred]**".
  - A SN1 R5 bullet "The GovTech blog says 'Chinese (88%) and Malay (78%)', which matches Table 1; the paper itself does not resolve it" Keep, and change "the paper itself does not resolve it" to "the paper text does not say which table is right **[Documented]**".
  - A SN1 R5 bullet "Margins: ... 8-25% ..." see T23 (arithmetic note).
  - A SN1 R8 bullet "Correct Chinese and Malay values for RabakBench in the paper ..." Replace with: "Table 3 header order for Chinese and Malay (Table 1 and the blog give Chinese 87.8, Malay 78.4; the GovTech RabakBench paper supports Table 1's order; the SGHateCheck and SGToxicGuard Chinese and Malay values still rest on the Table 3 header)".
  - A SN1 R8 Summary: replace the clause "what the ZH and MS columns really are in the paper" (see the new Summary under T28).
  - A RN-A bullet "SN1 conflict, paper Table 1 versus Table 3 ... Treat the labelling as unresolved": replace with "Resolved by cross-check: GovTech RabakBench paper Table 4 (Chinese then Malay) matches LG2P Table 3's third-party rows only if Table 3's MS and ZH labels are swapped; AWS's dash therefore sits on Chinese, not Malay, in LG2P's Table 3 [Inferred]. Note: AWS language support itself was not checked in AWS docs".
  - INV(a) LG2 Headline eval: add "RabakBench binary F1: Singlish 88.1, Chinese 87.8, Malay 78.4, Tamil 66.6 [Documented] (arXiv 2507.15339 Table 1; Table 3 prints Chinese and Malay headers in the opposite order [Inferred] mislabel)". INV-RN paper-note bullet "The per-language RabakBench column order in Table 3 text reads SS, MS, ZH, TA ... I did not quote per-language numbers" Replace with the cross-check conclusion above.
  - Brief: "Table 1 and Table 3 order the ZH and MS columns differently, so verify against the html": record as resolved with the above.
- Changes Summary? Y (A SN1 R8 Summary only).

### T23 — Paper numeric inconsistencies
- Verdict: PARTLY RESOLVED. Every inconsistency is real and now pinned to a cell; one more was found (the "8-25%" margin claim). The 16-versus-17 point is not a contradiction.
- Evidence:
  - Singlish: Table 3 and Table 1 give "88.1"; Table 5 (`Moderator | RBSS | RBSS_noise`) gives "LionGuard 2 | 87.1 | 85.6", caption "LionGuard 2 remains robust, dropping only 1.5%". 87.1 minus 85.6 is 1.5. Blog: "an F1 score of 87% on RabakBench". RBP does not report LionGuard 2. No source says why the numbers differ.
  - Tamil: Table 3 and Table 1 "66.6"; Table 8 (`Training variant | RBTA | SGHCTA | SGTGTA`) "LionGuard 2 | 66.5 | 64.5 | 71.5". SGHateCheck Tamil 64.5 and SGToxicGuard Tamil 71.5 agree with Table 3.
  - Throughput (section 3): "the embedding call handles ≈250 tokens s−1, while the classifier head itself processes ≈1.5×10^4 tokens s−1, giving an end-to-end throughput of ≈300 tokens s−1". These are not contradictory in the sense of sequential stages are not additive here (250 tokens/s embedding alone would cap the end-to-end figure at or below 250); the text is internally odd. The Sep 2026 blog repeats "roughly 300 tokens/s on a single CPU" without the 250.
  - Benchmark count: LG2P section 5.1 "on 1 internal test set and 16 public benchmarks, including 13 localised datasets ... and 4 general English datasets"; heading "Performance on 17 Benchmarks". Blog: "across 16 benchmarks" and lists three localised plus four English sets. So 16 public plus 1 internal is 17; the blog counts only the public ones (counting languages: 12 + 4 = 16). Not a contradiction. But "13 localised + 4 general" is also 17, which double counts the internal test set as one of the 13.
  - Qwen row, Table 1 verbatim: "Qwen3-Embedding-0.6B 1,024d Zhang et al. (2025) | 87.2 | 61.4 | 67.9 | 60.9 | 56.4". The row above: "cohere-embed-multilingual-v3.0 1,024d Cohere (2025a) | 72.9 | 64.2 | 67.9 | 60.9 | 56.4". Last three cells repeat. Qwen Test 87.2 exceeds the chosen model's 77.0 although the text says text-embedding-3-large "achieved the highest binary F1". The PDF text extraction interleaves the rows of this table, so it could not be compared cell by cell; the same numbers appear.
  - New: section 5.1 "LionGuard 2 obtains the highest scores on Singlish, Chinese, and Malay, with margins of 8-25% over the next-best model". Computed from Table 3 (my arithmetic, absolute F1 points, LionGuard 2 minus the best other row): test 19.9; RabakBench SS 18.5, Chinese/Malay 18.1 and 4.4; SGHateCheck SS 9.2, 13.0, 8.1; SGToxicGuard SS 5.0, 7.4, 7.2. Swapping the Chinese and Malay labels does not change the set. So the margins are 4.4 to 19.9, not 8 to 25, in absolute points.
- Label to use: the cell values: [Documented]. The 8-25% non-reproduction: [Inferred]. 16 versus 17: [Documented].
- Draft impact:
  - A SN1 R4 speed bullet: replace with "Speed in the paper, single CPU, synchronous: the embedding call about 250 tokens/s, the head about 1.5 x 10^4 tokens/s, end to end about 300 tokens/s; the numbers are stated together without a method, and 300 is above the embedding-only 250 (paper section 3) **[Documented]**" (keeps the caveat). INV(a) LG2 Headline eval: "about 300 tokens per second end to end on one CPU" add "(paper also gives 250 for the embedding call alone)".
  - A SN1 R5 Singlish bullet ("RabakBench Singlish as 88.1 in Table 3 and 87.1 in Table 5, and the blog says 87%"): keep, add "no source explains the difference **[Documented]**".
  - A SN1 R5 margins bullet: replace "margins of 8-25%" with "the paper text says margins of 8-25% over the next-best model on Singlish, Chinese and Malay; absolute differences computed from Table 3 are 4.4 to 19.9 points **[Inferred]**".
  - A SN1 R2 noisy-variant bullet (87.1 to 85.6): fine, keep.
  - A RN-A SN1 inconsistencies bullet: replace "The blog says 16 benchmarks and the paper 17 (1 internal plus 16 public)" with "Blog 16 and paper 17 are consistent: the paper counts 1 internal test set plus 16 public benchmarks; the paper's own '13 localised' also seems to count the internal set". Qwen bullet: keep.
- Changes Summary? N.

### T24 — "LionGuard 1.1" (Table 3) versus "LionGuard 1" (Table 4)
- Verdict: PARTLY RESOLVED, with a CORRECTION to the inventory's handling.
- Evidence:
  - "LionGuard 1.1" occurs once in LG2P: the Table 3 row "LionGuard 1.1 | 53.7 | 58.4 | 57.1 | 70.7 | 69.1 | 45.5 | 37.4 | 22.9 | 17.4 | 24.2 | 10.7 | 9.6 | 7.4". Table 4 row "LionGuard 1 | 35.0 | 31.6 | 55.8 | 34.7"; Table 5 row "LionGuard 1 | 58.4 | 64.2". The Singlish value 58.4 is the same in Table 3 ("LionGuard 1.1", SS) and Table 5 ("LionGuard 1", RBSS), so they are the same system under two labels (my inference). Same in html v1.
  - Text, section 2: "Our earlier system, LionGuard 1 Foo and Khoo (2025)". Section 4: "70% smaller than what was used for LionGuard 1".
  - Blog caption under its comparison figure: "(Note: LionGuard is an improved internal version of the original LionGuard 1)".
  - HF `govtech/lionguard-v1` commit list (HF API): "2024-09-01 update model artefacts", "2024-09-02 update thresholds", "2024-09-18 revert lionguard binary model", last README change 2024-11-16. LG1P was submitted 2024-06-24 (v1) and the HF repo was created 2024-07-16.
- Label to use: that Table 3 "1.1" is the same system as "LionGuard 1": [Inferred]. That the comparator is "an improved internal version": [Documented] (blog). That it equals the published HF `lionguard-v1` weights: [Not disclosed].
- Draft impact:
  - INV(a) LG1 Headline eval cell: after "In the LionGuard 2 paper LionGuard 1 scores 35.0 / 31.6 / 55.8 / 34.7 ... [Documented]" append "The paper's own table 3 calls its comparator 'LionGuard 1.1', and the GovTech blog calls it 'an improved internal version of the original LionGuard 1', so these figures may not be the published lionguard-v1 weights [Inferred]". Keep the PR-AUC 0.819 (LG1P Table 4) as the headline for the HF model.
  - INV-RN paper-note bullet: replace "I quoted only the Table 4 numbers" with the above sentence.
  - No SN1 bullet quotes LG1 numbers.
- Changes Summary? N.

### T25 — "About 4%" binary versus category disagreement
- Verdict: RESOLVED. The sources differ in wording only; the table gives the exact figures. Use A's wording, and fix INV(a).
- Evidence:
  - LG2P section 7.2: "About 4% of examples aggregated across two localised and three general datasets show disagreement between the binary head and category heads (Appendix E.1)."
  - Table 11 caption: "The binary head over-flags in only 4 % of cases and under-flags in <1 %". Table 11 rows: "Overall average | 4.19 | 0.70 | 43 075" (columns Over-predict (%), Under-predict (%), # samples). Per benchmark over-predict: RabakBench (SS) 9.99, SGHateCheck (SS) 4.60, BeaverTails 4.08, SORRY-Bench 3.19, OAI Moderation Eval 4.52.
  - Sum 4.19 + 0.70 is 4.89, so total disagreement is about 4.9%, and "about 4%" matches the over-flag part only. Binary over-predict means binary says unsafe while no category does (my reading of the caption, [Inferred]).
- Label to use: [Documented].
- Draft impact:
  - A SN1 R2 limitation bullet: replace with "Limitation: the paper says about 4% of examples show the binary head and category heads disagreeing (section 7.2); Table 11 splits this into over-predict 4.19% and under-predict 0.70% on average over 43,075 samples, with RabakBench Singlish highest at 9.99% over-predict **[Documented]**".
  - A SN1 R7 bullet "to quantify the roughly 4% head mismatch": change "roughly 4%" to "roughly 4 to 5%". Label stays [Inferred].
  - INV(a) LG2 Headline eval: "binary head over-flags in 4 percent of cases" is correct for the over-flag direction; add "and under-flags in under 1 percent [Documented]". INV(c) Overall unsafe row: "disagrees with category heads in about 4 percent of cases" is the paper's wording (section 7.2) and is acceptable; optionally "about 4 to 5 percent (over 4.19, under 0.70)".
- Changes Summary? N.

### T26 — Does any source map LionGuard 1 to LionGuard 2?
- Verdict: CORRECTION. INV(c) cites "arXiv 2507.15339 Table 17 maps taxonomies" under [Documented] for the LG1-to-LG2 misconduct mapping, but Table 17 does not contain LionGuard 1. The intro sentence "no source states a LionGuard 1 to LionGuard 2 mapping" is right.
- Evidence:
  - LG2P Table 17 caption: "Mappings of the Taxonomy used by 7 selected Guardrails to our chosen Taxonomy". Guardrail column values in the table: Azure AI Content Safety, AWS Bedrock Guardrail, Google Cloud Model Armor, OpenAI Moderation, LlamaGuard 3 8B, LlamaGuard 4 12B (six named). Table 18 caption: "Mappings of the Taxonomy used by selected Guardrails to our chosen Taxonomy" (benchmark taxonomies). A search of the parsed tables for "LionGuard" returns only Tables 3, 4, 5, 8, 13 to 16, never 17 or 18. LG2P section 1: "(i) a richer risk taxonomy with severity levels", no category mapping.
  - LG1P section 3, the seven categories verbatim: "Encouraging public harm: Content that promotes, facilitates, or encourages harmful public acts, vice or organized crime." "Encouraging self-harm: Content that promotes or depicts acts of self-harm, such as suicide, cutting, and eating disorders." "Toxic: Content that is rude, disrespectful, or profane, including the use of slurs." "Violent: Content that depicts death, violence, or physical injury." Hateful, Harassment and Sexual definitions also match the INV wording.
  - HF `lionguard-v1` config key names (binary, hateful, harassment, public_harm, self_harm, sexual, toxic, violent) were already read by the draft.
- Label to use: LG1 category definitions: [Documented] (LG1P section 3). Every LG1-to-LG2 mapping cell: [Inferred]. Table 17 as a source: only for the third-party guardrail mappings, not for LG1.
- Draft impact:
  - INV(c) All Other Misconduct Level 1 row, Notes cell: replace "(arXiv 2407.10995; arXiv 2507.15339 Table 17 maps taxonomies). Mapping [Inferred]" with "(arXiv 2407.10995 section 3). Mapping [Inferred]; LionGuard 2 paper Table 17 maps other guardrails (Azure, AWS, Google, OpenAI, LlamaGuard 3 and 4), not LionGuard 1".
  - INV(c) intro sentence: keep, add "(checked arXiv 2507.15339 Tables 17 and 18, arXiv 2407.10995 section 3, the HF cards and G)".
  - The 12 [Inferred] crosswalk cells stay [Inferred].
- Changes Summary? N.

### T27 — LionGuard 1 language and data claims
- Verdict: RESOLVED. The claims hold; only the language wording needs care.
- Evidence:
  - LG1P section 1: "resulting in a novel dataset of 138k Singlish texts"; section 4: "The final dataset consisted of 138,000 labelled texts." Split 70/15/15.
  - LG1P section 4: "We defined seven categories of safety risks for LionGuard."
  - LG1P discussion: "LionGuard may not generalize well to other domains and languages, as it was trained specifically to detect harmful content in the Singapore context."
  - HF card (`govtech/lionguard-v1@92cc0491`): "LionGuard is a classifier for detecting unsafe content in the Singapore context. It uses pre-trained BAAI English embeddings". It states no language list; HF metadata has no language tag.
  - No evaluation in other languages appears in LG1P (Singlish test split only; the paper's own limitation says so).
- Label to use: 138k Singlish texts and seven categories plus binary: [Documented]. "Other languages not evaluated": [Inferred] (absence in LG1P and the caveat above). "English/Singlish only": [Inferred].
- Draft impact:
  - INV(a) LG1 Languages cell: replace with "Singlish texts (138,000 labelled) with English BGE embeddings [Documented] (arXiv 2407.10995 section 4; card says 'BAAI English embeddings'); the paper warns it 'may not generalize well to other domains and languages' [Documented]; evaluation in other languages not found [Inferred]".
  - INV(a) LG1 Categories cell: already correct ("seven categories plus binary [Documented]").
- Changes Summary? N.

### T28 — Any evaluation of LionGuard 2.1 or Lite
- Verdict: CORRECTION for 2.1 (an official evaluation exists); STILL OPEN for Lite (checked HF README, playbook, G-level claims, both blogs, playbook repo; not stated). The drafts say "no paper, evaluation or model-card benchmark exists for 2.1 or Lite"; for 2.1 there is a small one in a GovTech blog.
- Evidence:
  - Blog, 28 Sep 2026, "Decision Models for Guardrails: Exploring Jev and Kev for Moderation" (`https://blog.ai.gov.sg/decision-models-for-guardrails-exploring-jev-and-kev-for-moderation/`): "We wanted to compare Jev directly against LionGuard 2.1". Caption: "Binary safe/unsafe F1 for Jev, Kev, fine-tuned Kev, and LionGuard 2.1 across selected moderation benchmarks." Method: "using the same 0.5 threshold".
  - Table verbatim, column "LionGuard 2.1" (dataset: value): Original test 0.7318; RabakBench English/Singlish 0.8618; RabakBench Malay 0.8420; RabakBench Tamil 0.7267; RabakBench Chinese 0.8688; SimpleSafetyTests 1.0000; OpenAI Moderation 0.7397. The same table gives Jev 0.8385, 0.8745, 0.8766, 0.7805, 0.8809, 1.0000, 0.7639 (Jev is a third-party model; not Sentinel scope).
  - "Original test" is described as "a held-out private LionGuard test split", so it is not the paper's test set (the paper's own LionGuard 2 figure on its test set is 77.0, 2.1 is 73.18 here; whether they are the same split is not stated).
  - Playbook (`.../tools/lionguard/`): "All share the same methodology and differ only in the embedding model they use"; 2.1 is "Strong performance across all benchmarks, particularly in multilingual settings." No numbers. Playbook repo code search for "LionGuard 2.1" returns only `website/docs/tools/lionguard.md` at `97338569`.
  - Checked, not stated: HF README of `govtech/lionguard-2.1` and `govtech/lionguard-2-lite` (no benchmark table; the two READMEs hold only the taxonomy and usage), HF commit lists of both repos (no results files), LG2P (does not mention 2.1 or Lite), blog "Introducing LionGuard 2" (does not mention them), blog "Guardrails in the Wild" (21 Aug 2026; no 2.1 or Lite numbers), blog.ai.gov.sg home page and page 2 and RSS (no LionGuard Lite item).
- Label to use: the 2.1 figures: [Documented] (blog.ai.gov.sg, 28 Sep 2026). Lite evaluation: [Not disclosed].
- Draft impact:
  - A SN1 R4 bullet "Variant differences: no paper, evaluation or model-card benchmark exists for 2.1 or Lite; the playbook says ..." Replace with two bullets: "Variant differences: the playbook says the three versions share one methodology and differ 'only in the embedding model' **[Documented]**" and "No paper or model-card benchmark exists for 2.1 or Lite; the only GovTech evaluation found is one table for 2.1 in the 28 Sep 2026 blog (binary F1 at 0.5: own private test split 0.7318, RabakBench Singlish 0.8618, Malay 0.8420, Tamil 0.7267, Chinese 0.8688, SimpleSafetyTests 1.0000, OpenAI Moderation 0.7397) **[Documented]**" and "No evaluation of LionGuard 2 Lite was found in the Hugging Face card, playbook, LionGuard 2 paper or the three GovTech blog posts checked **[Not disclosed]**".
  - A SN1 R8 bullet "Any benchmark of LionGuard 2.1 or Lite (no paper or card results found on Hugging Face, the playbook or the blog)": replace with "Any evaluation of LionGuard 2 Lite, and any 2.1 evaluation beyond one blog table (no paper or card results; checked HF cards, playbook, three GovTech blog posts)".
  - A SN1 R8 Summary (new, use this one, 30 words): "**Key open questions.** Which variant runs per suite key, how embeddings are hosted, what threshold to use, and any evaluation of Lite or of 2.1 beyond one blog table."
  - INV(a) LG2.1 Headline eval cell: replace "No evaluation numbers published for 2.1 [Not disclosed] (README, PBL, G, API checked)" with "Binary F1 at 0.5 (private test split 0.7318; RabakBench Singlish 0.8618, Malay 0.8420, Tamil 0.7267, Chinese 0.8688; SimpleSafetyTests 1.0000; OpenAI Moderation 0.7397) [Documented] (blog.ai.gov.sg, 28 Sep 2026); no paper or card benchmark [Not disclosed] (README, PBL, G, API checked)". INV(a) Lite Headline eval cell stays [Not disclosed]; extend "(README, PBL, G, API, blog posts checked)".
  - INV(a) LG2.1 Paper cell: keep. INV(a) LG2.1 row Source URL: add the blog URL. A SN1 R9: add the blog URL.
- Changes Summary? Y (A SN1 R8 Summary).

### T29 — Release or announcement date of LionGuard 2.1 and Lite
- Verdict: STILL OPEN (checked HF commit history, playbook repo and page, blog.ai.gov.sg index, page 2, RSS and three posts; no announcement or release date stated).
- Evidence:
  - HF commit lists (HF API): `lionguard-2.1` "2025-11-17 initial commit" through "2025-11-18 Update README.md" (last commit `1c3a9ea7`); `lionguard-2-lite` "2025-11-18 initial commit" through "2025-11-18 Update README.md" (`d56c17a0`). Repo creation dates: 2.1 2025-11-17, Lite 2025-11-18 (HF API createdAt 2025-11-17T06:51:48Z and 2025-11-18T04:12:25Z). The history shows no visibility change; HF does not expose whether a repo was private first.
  - Playbook: only mention is the LionGuard page, added in the single commit `8cd4c061` (2026-07-29), whose message says "Document the three LionGuard 2 versions (2, 2.1, Lite) and their embedding models". The page says "Last updated on Jul 28, 2026". That is a documentation date, not a release date.
  - Blog 28 Sep 2026 uses LionGuard 2.1 as the comparator without announcing it. No post on blog.ai.gov.sg is titled for 2.1 or Lite.
- Label to use: [Not disclosed] for announcement and release dates. HF repo creation dates stay [Documented: repo ...@sha] as repo dates (see T74).
- Draft impact:
  - INV(a) LG2.1 Release cell: replace "Announcement or blog for 2.1 [Not disclosed] (blog.ai.gov.sg LionGuard 2 post and PBL checked)" with "Announcement or release date [Not disclosed] (checked blog.ai.gov.sg index, page 2 and RSS, three LionGuard blog posts, PBL, playbook repo history, HF commit lists). First public mention found in GovTech docs: playbook page, commit 2026-07-29 [Documented: repo govtech-responsibleai/playbook@8cd4c061]".
  - INV(a) Lite Release cell: append "Announcement or release date [Not disclosed] (same sources checked)".
  - A SN1: no change needed (no date claimed).
- Changes Summary? N.

### T30 — Head architecture wording
- Verdict: RESOLVED. Both wordings are compatible and the shapes are now confirmed from the safetensors headers. One new wording difference: a GovTech blog says "11 classification heads".
- Evidence:
  - `lionguard2.py@be4e38c9`: shared layers `nn.Linear(self.input_dim, 256)`, ReLU, Dropout(0.2), `nn.Linear(256, 128)`, ReLU, Dropout(0.2). Each head: `nn.Linear(128, 32)`, ReLU, `nn.Linear(32, 2)`, Sigmoid, with the comment "2 thresholds for ordinal classification". `self.n_outputs = len(self.category_order)` which is 7 per config.json.
  - Safetensors header tensor shapes (via range request): `shared_layers.0.weight` [256, 3072] for `lionguard-2` and `lionguard-2.1`, [256, 768] for `lionguard-2-lite`; `shared_layers.3.weight` [128, 256]; each of `output_heads.0` to `output_heads.6`: `.0.weight` [32, 128], `.2.weight` [2, 32].
  - Parameter check: (3072x256+256) + (256x128+128) + 7x(128x32+32+32x2+2) = 786,688 + 32,896 + 29,358 = 848,942, equal to the HF total 848,942 for 2 and 2.1. Lite: 768 replaces 3072, giving 196,864 + 32,896 + 29,358 = 259,118, equal to the HF total. So the 2.1 `input_dim` 3072 is confirmed by shapes.
  - Output keys: config.json `categories` lists 11 keys over the 7 heads (binary 1, hateful 2, insults 1, sexual 2, physical_violence 1, self_harm 2, all_other_misconduct 2). `predict` takes column j of head i, so single-level heads use only the first output.
  - Blog, 21 Aug 2026 ("Guardrails in the Wild"): "LionGuard 2 uses a shared representation feeding into 11 classification heads." That counts outputs, not head modules in the released code.
  - Playbook/LG2P: paper says about 0.85M parameters (consistent).
- Label to use: [Documented: repo govtech/lionguard-2@be4e38c9] (code and shapes); the parameter arithmetic is mine, [Inferred], but it equals the HF totals. The "11 heads" wording: [Documented] (blog) and conflicts in wording only.
- Draft impact:
  - A SN1 R4 Head bullet: replace "then seven heads of 32 hidden units with two sigmoid outputs, P(level above 0) and P(level above 1)" with "then seven head modules, each 128 to 32 to 2 with sigmoid outputs, P(level above 0) and P(level above 1), giving the 11 output keys; 848.9K parameters for 2 and 2.1, 259.1K for Lite, which equals the sum of the layer shapes **[Documented: repo govtech/lionguard-2@be4e38c9]**". Add bullet: "A GovTech blog (21 Aug 2026) describes the model as 'a shared representation feeding into 11 classification heads', counting output keys rather than the seven head modules in the code **[Documented]**".
  - A SN1 R4 Input dimension bullet: keep, change label cite to "(config `input_dim`; first layer weight shape 256 x 3072 for 2 and 2.1 and 256 x 768 for Lite in the safetensors header)". Remove the caveat in INV-RN "I took this as documented config, not verified against the safetensors shape" and say it was verified.
  - INV(a) LG2 Base model cell "7 heads of 128-32-2": correct, keep. INV(a) LG2.1 Base model cell: append "first layer shape 256 x 3072 confirmed in safetensors header".
- Changes Summary? N.

### T31 — Tamil coverage wording
- Verdict: RESOLVED (wording alignment). Sources agree on substance: coverage is partial and weak.
- Evidence:
  - LG2P abstract: "supporting English, Chinese, Malay, and partial Tamil". Blog: "Support for English, Singlish, Chinese, Malay, and partial Tamil" and "partial Tamil moderation"; playbook LionGuard page: "Support for English, Singlish, Chinese, Malay, and partial Tamil."
  - LG2P section 5.3: "However, its Tamil performance remains moderate, highlighting an area for future improvement." Appendix E.2 text: "On Tamil, LionGuard 2 achieves moderate performance, ranking in the middle of the evaluated models". So "moderate" is the paper's own word on the native-speaker set.
  - Numbers (binary F1 on RabakBench, SGHateCheck, SGToxicGuard): Tamil 66.6, 64.5, 71.5 (Table 3), the lowest language for LionGuard 2 in each group; on the native-speaker set (Table 13, header "Chinese | Malay | Tamil | Overall", "Acc. | F1"): "LionGuard 2 | 85.5 | 85.0 | 79.5 | 81.4 | 40.7 | 41.1 | 70.6 | 72.7". In Table 3, LlamaGuard 4 12B beats it on Tamil (73.0 RabakBench, 77.9 SGToxicGuard); the blog says LionGuard 2 is "slightly behind" it.
  - Section 7.3 is titled "Lower performance for Tamil". Table 8: adding machine-translated Tamil or Malay data made Tamil worse (RBTA 66.5 baseline versus 23.1 and 21.2).
  - HF cards for 2.1 and Lite: "tuned for English/Singlish, Chinese, Malay, and Tamil" (no "partial"); HF tags en, ms, ta, zh. Blog 28 Sep 2026 for 2.1: RabakBench Tamil 0.7267 against Chinese 0.8688 and Malay 0.8420 (the lowest of the four).
- Label to use: [Documented].
- Draft impact:
  - A SN1 R2 languages bullet: fine ("partial Tamil"). Add to the Tamil limitation bullet: "the paper calls Tamil performance 'moderate' on the native-speaker set; LlamaGuard 4 12B scores higher on Tamil in Table 3 **[Documented]**".
  - INV(a) LG2 Languages cell "(PBL; arXiv 2507.15339 says Tamil is moderate)" is acceptable; make it "partial Tamil (PBL, paper abstract); Tamil F1 41.1 against 85.0 Chinese and 81.4 Malay on the native-speaker set [Documented]".
  - INV(a) LG2.1 and Lite Languages cells: append "The HF cards say 'Tamil' without 'partial'; for 2.1 the blog gives Tamil F1 0.7267 on RabakBench, lowest of four languages [Documented]; for Lite no Tamil figure [Not disclosed]".
- Changes Summary? N.

### T32 — Embedder naming and the 8192 limit
- Verdict: PARTLY RESOLVED. The correct name is `text-embedding-3-large` at 3072 dimensions; the 8192 limit is not checked here (OpenAI's page is off the allowed list).
- Evidence:
  - HF card `lionguard-2@be4e38c9`: "It leverages OpenAI’s `text-embedding-3-large` with a multi-head classifier". Usage: `model="text-embedding-3-large", dimensions=3072 # dimensions of the embedding`.
  - `lionguard2.py`: line 9 "INPUT_DIMENSION = 3072  # length of OpenAI embeddings" and the docstring "after it has been encoded with OpenAI's `text-embedding-3-small` model". The 2.1 file's docstring (diff against the 2 file) was rewritten to "Gemini's `gemini-embedding-001` model"; the 2 file was not corrected. text-embedding-3-small defaults to 1536 dimensions, so the docstring is inconsistent with `input_dim` 3072 (the 1536 default is general knowledge, not read from a GovTech source).
  - LG2P Table 1: "text-embedding-3-large 3,072d OpenAI (2025)". Section 7.1: "LionGuard 2 inherits its representations from OpenAI’s text-embedding-3-large."
  - The Sentinel docs typo "text-embedding-large-3" (draft A and INV(b) already attribute it to G).
  - Not found in any GovTech source: the 8192 token limit other than in G's version table (as the draft says).
- Label to use: `text-embedding-3-large`, 3072: [Documented: repo govtech/lionguard-2@be4e38c9] and [Documented] (paper). G's spelling: [Documented] as a typo. 8192 limit: [Documented] (G only, not independently checked).
- Draft impact:
  - A SN1 R4 bullets on the typo, the docstring and the version table: correct as written. INV(b) lionguard-2-binary row quoting "text-embedding-3-large" as Documented (G): change source to "(HF card, arXiv 2507.15339; G spells it text-embedding-large-3)".
  - A RN-A bullet "SN1 token limit of 8192 ... I did not check OpenAI's documented limit": keep.
- Changes Summary? N.

### T45 — Parameter counts of the two off-topic models
- Verdict: RESOLVED (computed from tensor shapes). INV(a) [Not disclosed] can be replaced; A's 33M is the base-model count, not the released model.
- Evidence:
  - Safetensors header read by byte-range from the pinned repos; sum of all tensor shapes (all F32): bi-encoder `models/off-topic-jinaai-jina-embeddings-v2-small-en-TwinEncoder.safetensors` 97 tensors, 36,016,258 parameters; cross-encoder `models/off-topic-cross-encoder-stsb-roberta-base-CrossEncoder.safetensors` 205 tensors, 125,015,234 parameters. HF API `safetensors` field is null for both repos, which is why INV and card say nothing.
  - Bi-encoder tensor groups: `shared_encoder`, `adapter1`, `adapter2` (down 256x512, up 512x256), `attn_pooling_1_to_2`, `attn_pooling_2_to_1`, `cross_attention_1_to_2`, `cross_attention_2_to_1`, `projection_layer`, `classifier` (so it matches the paper's adapters, attention pooling and cross-attention).
  - OTP section 3.3: "jina-embeddings-v2-small-en (Günther et al., 2024), which has 33M parameters and an 8k token limit. For our experiments, we trim sequences to 1k tokens." No count is given for the cross-encoder.
- Label to use: counts: [Inferred] (my sum of the tensor shapes in the pinned files; method reproducible). 33M base model: [Documented] (OTP).
- Draft impact:
  - INV(a) off-topic bi-encoder Params cell: replace "[Not disclosed] (README and HFAPI give no count)" with "About 36.0 million (36,016,258, sum of safetensors tensor shapes) [Inferred]; the card gives none; the paper gives 33M for the base jina model only [Documented]". Cross-encoder cell: "About 125.0 million (125,015,234, sum of safetensors tensor shapes) [Inferred]; the card gives none [Documented]".
  - A SN3 R4 bi-encoder bullet: after "(33M parameters, 8k token limit)" add "the released twin-encoder checkpoint sums to about 36.0M parameters including adapters and heads **[Inferred]**" (keep the bullet single-fact by adding a new bullet).
- Changes Summary? N.

### T46 — Off-topic context lengths
- Verdict: RESOLVED. The values are consistent once the roles are separated.
- Evidence:
  - Bi-encoder `config.json`: `"max_length": 1024`; README: "Maximum Context Length: 1024 tokens"; OTP: "we trim sequences to 1k tokens" and base model "8k token limit". Inference scripts: `tokenizer(..., truncation=True, padding="max_length", max_length=max_length)` with `max_length = config['classifier']['embedding']['max_length']`, so every pair is truncated and padded to 1024.
  - Cross-encoder `config.json`: `"max_length": 512`; README: "Maximum Context Length: 514 tokens". The scripts use the config value with `truncation=True, padding="max_length"`. Safetensors header: `base_model.embeddings.position_embeddings.weight` shape [514, 768], which is the RoBERTa 514 positions (two reserved), i.e. 512 usable tokens (the 512 usable reading is general RoBERTa knowledge).
  - So 514 is the model's position-table size, 512 is what the shipped scripts actually use.
- Label to use: bi-encoder 1024: [Documented: repo ...@806cf24c] (config and card agree). Cross-encoder script limit 512 and card 514: [Documented: repo ...@505c86b1]; "514 includes two reserved positions": [Inferred].
- Draft impact:
  - A SN3 R4 cross-encoder bullet "config `max_length` 512; the model card says '514 tokens'": keep, add "; the safetensors position table has 514 rows and the inference scripts truncate to the config value of 512 **[Documented: repo govtech/stsb-roberta-base-off-topic@505c86b1]**".
  - A SN3 R6 length bullet: keep. INV(a) bi-encoder Base model cell: "card max context 1024" correct; add "config.json max_length 1024". INV(a) cross-encoder Base model cell: change "card max context 514 tokens" to "card max context 514 tokens; config.json and scripts use 512".
- Changes Summary? N.

### T48 — Leakage evaluation in the off-topic paper
- Verdict: RESOLVED. The paper mentions leakage in one sentence only; it has no leakage method detail or figures. B's "no paper or evaluation" needs a small nuance; INV(a) is right that the sentence exists.
- Evidence:
  - OTP section 6 "Deployment Considerations" (`https://arxiv.org/html/2411.12946`) verbatim: "Moreover, the methodology has also been utilized to detect system prompt leakage or other categories of undesired model outputs."
  - Full text search of the HTML for "leak": one hit, that sentence. No table, figure or number for leakage. Section 5.1 limitations and section 7 conclusion do not mention it. The conclusion says the methodology "generalize[s] to other misuse categories (e.g., jailbreak or harmful prompts)" for off-topic classifiers, not leakage.
  - Not stated: whether the Space classifier (logistic regression on embeddings) is the model the sentence refers to; the paper's methodology is synthetic data generation plus fine-tuned bi- and cross-encoders, a different architecture from the Space. Blog.ai.gov.sg posts checked (LionGuard 2 launch, Jev and Kev, Guardrails in the Wild) have no leakage evaluation.
- Label to use: the sentence: [Documented] (arXiv 2411.12946 section 6). "No leakage evaluation figures": [Not disclosed] naming OTP section 6, the Space, G, playbook and three blog posts as checked.
- Draft impact:
  - B SN4 R2 bullet "No precision, recall, ... is published ... [Not disclosed]" and the next bullet "Sources checked for evaluation figures ... (no model card, no paper)": replace the second with "Sources checked for evaluation figures: aiguardian.gov.sg Sentinel pages, playbook Sentinel and privacy pages, the Hugging Face Space and org listing, the off-topic paper and three GovTech blog posts; the off-topic paper (section 6) says in one sentence that its methodology 'has also been utilized to detect system prompt leakage' and gives no figures **[Not disclosed]**". Add a bullet: "The off-topic paper (section 6) states the guardrail methodology was also used to detect system prompt leakage, with no method detail or numbers **[Documented]**".
  - B SN4 R4 bullet "No model card, paper, training data or evaluation is published for it": change "paper" to "dedicated paper", keep label. B SN4 R8 bullet "Training data, labels and evaluation ... (none published ...)": append "(the off-topic paper mentions leakage in one sentence only)".
  - B SN4 R2 Summary: "No category list or evaluation figure is published" remains true.
  - INV(a) leakage Paper cell is already right; the Headline eval cell "None published [Not disclosed] (README, app.py, G, PBS checked)": add "off-topic paper section 6 checked: one sentence, no figures".
  - A SN3: no change (A did not read the sentence as an evaluation).
- Changes Summary? N.

### T49 — Space classifier internals
- Verdict: RESOLVED (static pickle inspection). The model is a scikit-learn LogisticRegression; features are 1536 plus 1536; the pickle was never unpickled.
- Evidence:
  - Space file list (HF API): `.gitattributes`, `Dockerfile`, `README.md`, `app.py`, `logistic_regression_text_embedding_3_small.pkl` (112,275 bytes, LFS), `requirements.txt`. `requirements.txt` (verbatim): "httpx==0.27.2 numpy==2.1.3 openai==1.54.0 scikit-learn==1.6.1". `Dockerfile`: "FROM python:3.13-slim ... gradio==5.50.0". The app does `clf = pickle.load(f)` on that file and `clf.predict_proba(combined_embedding)[0][1]`; the call is `client.embeddings.create(input=[system_prompt, output], model="text-embedding-3-small")` through `AzureOpenAI(api_version="2024-02-01", ...)`.
  - Static opcode listing (`pickletools.genops`, no execution) of the file at the pinned sha: module "sklearn.linear_model._logistic", class "LogisticRegression"; params penalty 'l2', tol 0.0001, C 1.0, solver 'lbfgs', max_iter 100, multi_class 'auto'; `n_features_in_` array shape (3072,); `feature_names_in_` strings "system_prompt_embeddings_1" to "system_prompt_embeddings_1536" (1536 names) and "content_embeddings_1" to "content_embeddings_1536" (1536 names); `classes_` int64; `coef_` float64; `_sklearn_version` '1.3.2'.
  - Training data, labels, class balance and fit metrics are not in the pickle's opcode stream beyond the above.
- Label to use: all pickle facts: [Documented: repo govtech/system-prompt-leakage@0161b10c] (read from the pinned file by static parsing, my method); training data and evaluation: [Not disclosed].
- Draft impact:
  - B SN4 R4 bullet "The classifier is described as logistic regression only by its file name; the pickle was not opened ...": replace with "The pickle's static opcode listing (not loaded) names the class `sklearn.linear_model._logistic.LogisticRegression` with L2 penalty, C 1.0, lbfgs solver and 100 maximum iterations, fitted on 3072 features named system_prompt_embeddings_1 to _1536 and content_embeddings_1 to _1536 **[Documented: repo govtech/system-prompt-leakage@0161b10c]**" and "Training data, labels, class balance and any evaluation of the classifier **[Not disclosed]**".
  - B SN4 R4 bullet on requirements: add "; the pickle records scikit-learn 1.3.2 as its writer version while requirements pin 1.6.1 **[Documented: repo govtech/system-prompt-leakage@0161b10c]**".
  - B SN4 R4 Summary: "a logistic regression over embeddings of the system prompt and the output" is now supported by the class name; keep text, and the label already pins the repo. B SN4 R8 bullet "Training data ... (none published; the pickle was not opened)": replace "the pickle was not opened" with "the pickle's structure was read statically, not loaded". B RN-B: remove "pickle was not opened" statements and add the method.
  - INV(a) leakage Params cell: see T75. INV(a) leakage Base model cell "Logistic regression (file ...)": add "class LogisticRegression, scikit-learn 1.3.2 writer version [Documented: repo ...@0161b10c]".
  - Triage provenance note ("the pickle in the leakage Space (T49, never opened)"): now statically parsed.
- Changes Summary? N.

### T70 — Licence text of each HF model
- Verdict: RESOLVED. All six model LICENSE files are byte-identical; the draft's assumption was right. Facts only.
- Evidence:
  - MD5 of `LICENSE` at the pinned sha is `01aeb061dcdbf0bd0612ad2b76ac5b6c` for all six: `lionguard-v1@92cc0491`, `lionguard-2@be4e38c9`, `lionguard-2.1@1c3a9ea7`, `lionguard-2-lite@d56c17a0`, `jina-embeddings-v2-small-en-off-topic@806cf24c`, `stsb-roberta-base-off-topic@505c86b1`. READMEs of all six carry `license: other`, `license_name: govtech-singapore`, `license_link: LICENSE` (the `lionguard-v1` card too).
  - Opening sentence: "Except for any logos, trade marks, service marks, names, insignias, emblems, the Singapore state crest and Singapore national coat of arms ... the contents of this repository are provided under the MIT License SUBJECT FURTHER TO THE FOLLOWING:"
  - Clause (1): "The MIT License and the terms herein (collectively, the “Terms”) shall be governed by the laws of Singapore." Also: "shall be referred to and finally resolved by arbitration administered by the Singapore International Arbitration Centre (“SIAC”)". Seat "Singapore", "one (1) arbitrator", language "English".
  - Then "MIT License / Copyright 2020 Government Technology Agency." with the standard MIT grant ("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies") and the standard warranty disclaimer ("AS IS").
  - Also excluded: "any asset or code identified by the Government Technology Agency (“GovTech”) as not licensed to you (such identification may come in the form of a filename labelled with “restricted” or similar phrasing)". No such labelled file appears in the six repo file lists.
  - The LICENSE text says nothing about embedding-model terms, research-only use or data. (No legal advice intended.)
- Label to use: [Documented: repo govtech/<repo>@<sha>] for each repo; one bullet for "identical across six" [Documented] (checksum comparison).
- Draft impact:
  - A SN1 R4 licence bullet: replace with "Licence of the Hugging Face weights: README `license_name: govtech-singapore`; the LICENSE file grants the MIT licence 'SUBJECT FURTHER TO' Singapore governing law and SIAC arbitration, and excludes GovTech and Singapore public-sector marks and any asset GovTech marks as not licensed **[Documented: repo govtech/lionguard-2@be4e38c9]**". Add: "The LICENSE file is byte-identical in lionguard-v1, lionguard-2, lionguard-2.1, lionguard-2-lite and both off-topic repos **[Documented]**".
  - A SN3 R4 licence bullet (pinned to the stsb repo): keep, now supported; extend pin to both "govtech/stsb-roberta-base-off-topic@505c86b1, govtech/jina-embeddings-v2-small-en-off-topic@806cf24c".
  - INV(a) all Licence cells: for LG2.1, Lite, both off-topic and LG1, change "Same licence text" to "LICENSE read directly; identical to LionGuard 2 (same checksum) [Documented: repo ...@sha]". INV(d) self-hosted rows: keep. INV-RN last provenance line "LICENSE text was read only in lionguard-2 and assumed identical ... [Inferred]": replace with "LICENSE files of all six models were read and compared by checksum; identical".
- Changes Summary? N.

### T71 — Licence of the Spaces
- Verdict: RESOLVED. No Space has a LICENSE file or licence metadata.
- Evidence:
  - File lists (HF API, pinned shas): `system-prompt-leakage`: `.gitattributes`, `Dockerfile`, `README.md`, `app.py`, `logistic_regression_text_embedding_3_small.pkl`, `requirements.txt`. `lionguard-demo`: `.gitattributes`, `Dockerfile`, `README.md`, `app/backend/__init__.py`, `main.py`, `models.py`, `services.py`, `app/frontend/` files, `requirements.txt`, `utils.py`. `off-topic-demo`: `.gitattributes`, `.gitignore`, `Dockerfile`, `README.md`, `app.py`, `requirements.txt`, `utils.py`. No LICENSE in any.
  - README front matter: leakage "title: System Prompt Leakage Demo ... sdk: docker app_file: app.py pinned: false"; lionguard-demo "title: LionGuard ... short_description: Localised Multilingual Moderation Classifier for Singapore" and body "Demo for [LionGuard 2](https://arxiv.org/abs/2507.15339)."; off-topic-demo front matter only plus "Check out the configuration reference". No `license` key in any; HF API cardData has no licence for the leakage Space and `license: null`.
  - Dependencies: leakage app needs `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` (from `os.getenv` in app.py); lionguard-demo requirements include `openai`, `google-genai`, `gspread`, `google-auth` (the demo calls embedding APIs and a Google Sheets client; use is the demo's, not stated as a licence term). Terms of the Azure, OpenAI or Google services: not in GovTech files.
- Label to use: [Not disclosed] for Space licence terms, naming files and metadata checked.
- Draft impact:
  - B SN4 R4 README bullet "No model card, paper, training data or evaluation is published for it; the Space README holds only front matter": add a bullet "No LICENSE file and no licence key in the Space metadata (checked file list, README front matter and Hub metadata) **[Not disclosed]**".
  - INV(a) leakage Licence cell "No licence in the Space README [Not disclosed] (README front matter checked)": append "; no LICENSE file in the Space; same for lionguard-demo and off-topic-demo (file lists checked) [Not disclosed]". INV(d) HF demo Spaces row, Caveats: add "None of the three Spaces carries a LICENSE file or licence metadata [Not disclosed]".
- Changes Summary? N.

### T72 — "Research and public-interest" wording versus the MIT-style licence; embedder terms
- Verdict: PARTLY RESOLVED. The paper sentence exists; no licence or card text carries a research-only restriction or "usage guidelines". Embedder service terms are not in any GovTech source.
- Evidence:
  - LG2P Ethical Considerations, "Responsible Deployment and Access Controls", verbatim: "Our model weights are published on Hugging Face exclusively for research and public interest purposes only, with clear usage guidelines that prohibit deployment for harmful applications." (The draft INV paraphrase "for research and public-interest use with usage guidelines" drops "exclusively ... only" and "prohibit deployment for harmful applications".) Same section: "we restrict API access to internal government applications".
  - HF `lionguard-2` LICENSE and README@be4e38c9: search for research, guideline, acceptable use, prohibit returns nothing; the licence grants MIT rights subject to Singapore law and SIAC arbitration (see T70). The same holds for the 2.1 and Lite and the off-topic READMEs (searched).
  - Embedder terms: README usage requires an OpenAI key (`lionguard-2`) or Gemini key (`lionguard-2.1`); Lite uses `google/embeddinggemma-300m` through sentence-transformers. OpenAI, Google and Azure terms are outside the allowed source list and were not read; the leakage Space needs Azure OpenAI.
  - Paper statements on closed embedders: section 7.1, "LionGuard 2 inherits its representations from OpenAI’s text-embedding-3-large."
- Label to use: paper sentence: [Documented] (arXiv 2507.15339 ethical considerations). That the licence file does not repeat it: [Documented: repo govtech/lionguard-2@be4e38c9] (absence). Embedder service terms: [Not disclosed] (checked HF cards, LICENSE files, paper; vendor terms not read).
- Draft impact:
  - INV(a) LG2 Licence cell: replace "Paper says weights are published for research and public-interest use with usage guidelines [Documented]" with "Paper says weights are published 'exclusively for research and public interest purposes only, with clear usage guidelines that prohibit deployment for harmful applications' [Documented] (arXiv 2507.15339 ethical considerations); the LICENSE and card carry no such restriction or guideline text [Documented: repo govtech/lionguard-2@be4e38c9]; how the two relate is [Not disclosed]".
  - INV(d) self-hosted LionGuard row: add Caveats "Embedding vendor terms (OpenAI, Google) are not covered in GovTech files [Not disclosed]". A SN1 R4 self-hosting bullet: unchanged.
  - A SN1 R4: add bullet "The paper says the weights are published 'exclusively for research and public interest purposes only'; the repository LICENSE is MIT-based with no such limit **[Documented]**" (two sources, both quoted; mention in Reviewer notes as a conflict of wording).
- Changes Summary? N.

### T74 — HF "created" dates versus release dates
- Verdict: RESOLVED as a wording fix; actual public-release dates STILL OPEN (HF API gives creation and commit dates, not visibility changes).
- Evidence (HF API `createdAt`, commit lists; arXiv abs pages; blog):
  - `lionguard-v1`: created 2024-07-16 (initial commit 87d3d4d4); arXiv 2407.10995 "Submitted on 24 Jun 2024" (so the paper predates the repo).
  - `lionguard-2`: created 2025-06-30; README edited 2025-07-04 (two commits); paper arXiv 2507.15339 "Submitted on 21 Jul 2025" (v1) and v2 dated 28 Sep 2025 (page footer "arXiv:2507.15339v2 [cs.CL] 28 Sep 2025"); blog "29 Jul 2025". Last commit 2025-11-18 "Update README.md".
  - `lionguard-2.1`: created 2025-11-17; `lionguard-2-lite`: created 2025-11-18.
  - Off-topic: both repos created 2024-11-16; arXiv 2411.12946 "Submitted on 20 Nov 2024". The Hub API dates "Updated 22 Nov, 2024" and "25 Nov, 2024" are last-commit dates. `off-topic-demo` Space created 2024-09-24, which matches the paper's "deployed internally since September 2024" only as a coincidence of dates (no source links them).
  - `system-prompt-leakage` Space created 2024-12-05, last commit 2026-03-20; `lionguard-demo` created 2025-06-23, last 2025-11-19.
  - Whether any repo was private before it was made public: not exposed by the Hub API or commit history.
- Label to use: creation and last-commit dates: [Documented: repo ...@sha]. Public release date: [Not disclosed].
- Draft impact:
  - INV(a) Release cells (all rows): relabel the column text from "Release" to "Repo created / last commit; public release date [Not disclosed]" (the column header cannot change the label form). For LG2: "HF repo created 2025-06-30 (public date not exposed), paper 2025-07-21 (v2 2025-09-28), blog 2025-07-29". For LG1: add "paper 2024-06-24 predates the HF repo". Also add the leakage and demo Spaces dates above.
  - A SN1: no dates claimed.
- Changes Summary? N.

### T75 — Leakage feature size "3072 if embeddings are 1536 each"
- Verdict: RESOLVED. Confirmed by code and by the pickle's feature names.
- Evidence:
  - `app.py@0161b10c`: `embedding = client.embeddings.create(input=[system_prompt, output], model="text-embedding-3-small")`, then `combined_embedding = np.array(system_prompt_embedding + output_embedding).reshape(1, -1)`. The `+` on Python lists concatenates, so the row has the two vectors end to end. No `dimensions` argument is passed. The default text-embedding-3-small size is 1536 (general knowledge, not read from a GovTech file).
  - Pickle (static parse, T49): `n_features_in_` array shape (3072,), `feature_names_in_` with 1536 names "system_prompt_embeddings_1..1536" followed by 1536 names "content_embeddings_1..1536".
- Label to use: [Documented: repo govtech/system-prompt-leakage@0161b10c].
- Draft impact:
  - INV(a) leakage Params cell: replace with "Logistic regression with 3072 input features: 1536 system-prompt embedding values then 1536 output ('content') embedding values [Documented: repo govtech/system-prompt-leakage@0161b10c] (app.py and pickle feature names, static parse); file size 112,275 bytes; training data and metrics [Not disclosed]".
  - B SN4 R4 bullet "concatenates the two vectors into one row": add "(3072 features, 1536 each) **[Documented: repo govtech/system-prompt-leakage@0161b10c]**".
- Changes Summary? N.

---

## Summary table

| Item | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T22 | RESOLVED (Table 3 header mislabelled; Chinese 87.8, Malay 78.4) | [Documented] (Table 1, blog); [Inferred] (mislabel cross-check, other two groups) | Y (A SN1 R8) |
| T23 | PARTLY RESOLVED (all inconsistencies confirmed; new margin discrepancy) | [Documented]; [Inferred] for margins | N |
| T24 | PARTLY RESOLVED (1.1 same as 1; comparator is an internal version) | [Inferred]; [Not disclosed] for equality with HF weights | N |
| T25 | RESOLVED (4.19 over, 0.70 under) | [Documented] | N |
| T26 | CORRECTION (Table 17 does not cover LionGuard 1) | [Inferred] mappings; [Documented] definitions | N |
| T27 | RESOLVED | [Documented]; [Inferred] for "only English/Singlish" | N |
| T28 | CORRECTION for 2.1 (blog table exists); STILL OPEN for Lite | [Documented] (2.1); [Not disclosed] (Lite) | Y (A SN1 R8) |
| T29 | STILL OPEN | [Not disclosed] | N |
| T30 | RESOLVED (shapes and parameter sums confirm) | [Documented: repo ...@sha] | N |
| T31 | RESOLVED (wording) | [Documented] | N |
| T32 | PARTLY RESOLVED (8192 unchecked) | [Documented] | N |
| T45 | RESOLVED (computed 36.0M and 125.0M) | [Inferred] | N |
| T46 | RESOLVED (514 positions, 512 used) | [Documented: repo ...@sha] | N |
| T48 | RESOLVED (one sentence, no figures) | [Documented]; [Not disclosed] for figures | N |
| T49 | RESOLVED (LogisticRegression, 3072 features, sklearn 1.3.2) | [Documented: repo ...@0161b10c] | N |
| T70 | RESOLVED (six identical LICENSE files) | [Documented: repo ...@sha] | N |
| T71 | RESOLVED (no licence in any Space) | [Not disclosed] | N |
| T72 | PARTLY RESOLVED (vendor terms not read) | [Documented]; [Not disclosed] | N |
| T74 | RESOLVED (wording); release dates open | [Documented: repo ...@sha]; [Not disclosed] | N |
| T75 | RESOLVED (1536 + 1536) | [Documented: repo ...@0161b10c] | N |

## Reviewer notes (for the merge)

- Conflict, resolved by a second GovTech paper: LG2P Table 1 versus Table 3 column order for Chinese and Malay. Resolution rests on my comparison with RBP Table 4, so it is [Inferred]; RBP was not in the brief's paper list as a named item ("RabakBench: check its arXiv id if you cite it"); arXiv 2507.05980 has GovTech affiliations in its author block (read from the HTML).
- Conflict in wording: LG2P says weights are for "research and public interest purposes only" and the HF LICENSE is MIT-based with no such limit (T72).
- Conflict in wording: "11 classification heads" (blog, 21 Aug 2026) versus 7 head modules and 11 output keys (HF code) (T30).
- New official sources discovered that other agents may need: both 2026 blog posts named in the Method section. The 21 Aug 2026 post says the first retrained LionGuard 2 model will be rolled out to Sentinel users "very soon" and that "millions of chat messages pass through our guardrails" in a week; those are Sentinel facts for the other agent.
- Items that remain open after this pass: T29 (release and announcement dates), Lite evaluation (T28), vendor embedding terms (T72), 8192 token limit check (T32), public release date versus repo creation (T74), SGHateCheck and SGToxicGuard Chinese and Malay values (T22, depends on the same header).
- Method caveats: parameter sums and the margin arithmetic are my calculations from published shapes and tables. The pickle was parsed statically with `pickletools.genops` and never loaded. PDF text extraction of Tables 1 and 3 interleaves rows; the header strings were still readable.
