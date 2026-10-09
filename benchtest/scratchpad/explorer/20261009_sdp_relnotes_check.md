# sdp release-notes check (2026-10-09)
URL: https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes (HTTP 200, final URL unchanged; fetched with fetch_text.py)

## Item 1: MEDICAL_ID legacy window (~2026-10-11)
Finals wording: sdp_inventory_final.md line 38 (Health block): "Since 2026-07-13, MEDICAL_ID with InfoType.version unset or stable also reports MEDICAL_RECORD_NUMBER findings as MEDICAL_ID; and the note offered the old behaviour with version legacy for the next 90 days [Documented] (DOCS release-notes). That window ends about 2026-10-11 [Inferred] (premise: 90 days counted from the note date)". Cited URL: .../sensitive-data-protection/docs/release-notes (sdp_two_level.md line 221).
Status: MATCH. Entry July 13, 2026 (Change): "If you leave InfoType.version unset or set it to stable when setting the MEDICAL_ID infoType in your InspectConfig, Sensitive Data Protection includes MEDICAL_RECORD_NUMBER findings as type MEDICAL_ID in the scan results. You can still use the old functionality by setting InfoType.version to legacy for the next 90 days."
Arithmetic: 2026-07-13 + 90 days = 2026-10-11. OK. No later entry changes this.

## Item 2: PERSON_NAME promotion to stable (~2026-11-02)
Finals wording: sdp_two_level.md line 86: "For the new PERSON_NAME version the note says "In 30 days, the new version will be promoted to stable." (release note dated 2026-10-03 ...) [Documented]"; line 178: "...about 30 days after 2026-10-03, so results may shift after about 2026-11-02 [Inferred]".
Status: MATCH. Entry October 03, 2026 (Change): "A new version with an updated name dictionary is available for the PERSON_NAME infoType detector. You can try it out by setting InfoType.version to latest when including the PERSON_NAME infoType in your InspectConfig. You can still use the previous functionality by setting InfoType.version to stable or leaving it unset when using the PERSON_NAME infoType. In 30 days, the new version will be promoted to stable."
Arithmetic: 2026-10-03 + 30 = 2026-11-02. OK.

## New entries dated after 2026-09-01
Page's newest entry is October 03, 2026 (the PERSON_NAME one above, already in the finals). The previous entry is August 31, 2026 (content policies GA), before the cut-off. No other new entries; nothing new on image redaction or content safety classification after 2026-09-01.

## Recommended action
None.
