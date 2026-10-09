# Queues

## xlsx-writer queue (products with a CP2 approval ruling, apply in this order, one at a time)
| # | Slug | CP2 ruling | Queued | Applied (commit) |
|---|---|---|---|---|

## Open questions (from agents)
| Q file | Product | Routed to | State | Ruling |
|---|---|---|---|---|
| explorer/20261009_presidio_q01.md: official org after the transfer (data-privacy-stack vs Microsoft) and the header prefix | presidio | **user at presidio CP1** | open (blocking for P1: brief must state the prefix as provisional `Presidio:`) | — |
| explorer/20261009_presidio_q02.md: six single columns vs a merged set; recognizer-family granularity; + (i) PD5 column vs inventory-only, (ii) ~30 family rows vs ~120 per-entity rows (P1) | presidio | **user at presidio CP1** | open (non-blocking) | — |

| explorer/20261009_modelarmor_q01.md: 10 columns (R002 split) vs 6 vs folding MA9/MA10; antivirus + MCP screening as inventory or MA11; prefix `Model Armor:` (Q03); P1 adds alt (e) 14 cols if response-side file/image evidence appears, MA11 = tool-call screening (MCP and Agent Gateway) | modelarmor | **user at modelarmor CP1** | open (non-blocking) | — |
| explorer/20261009_sdp_q01–q03.md: prefix `Sensitive Data Protection:` vs `Google Cloud …`; content policy (SD7) column vs inventory; fold SD2→SD1, SD4→SD3 | sdp | **user at sdp CP1** | open (non-blocking; P1 drafts defaults) | — |

## Resolved questions
| Q file | Ruling | Decided by |
|---|---|---|
| explorer/20261009_presidio_q03.md (presidio-research placement) | R010 | main |
| explorer/20261009_presidio_q04.md (column ID prefix) | R009 | main |
| presidio P1 report: Covered-by marker for current non-column rows | R011 | main |
| modelarmor P0 Q02 (MA5/MA6 vs SDP) | R012 | main |
| modelarmor P0 Q04 / presidio P1 (vendor GitHub access) | R013 | main |
| modelarmor P1 Q-D (inventory sheet letter) | rule: R003 — letter assigned at P8 in workbook order; brief's `3f` is provisional | main |
| sdp P1 Q04 (sheet letter) / Q05 (seeds host) | R003 (letter at P8); seeds already on docs.cloud.google.com | main |
