# UEN

---

### Unique Entity Number (UEN)

[UEN](https://www.uen.gov.sg/ueninternet/faces/pages/admin/aboutUEN.jspx) is the standard identification number for Singapore registered entities.

---

### Default setting:

- Detects UEN for businesses and local companies registered with ACRA. See details [here](https://www.uen.gov.sg/ueninternet/faces/pages/admin/aboutUEN.jspx).
- REPLACE UENs with the `<SG_UEN>` tag.

**Validation disabled:**  
Both real and fake UEN numbers following the formats below are detected.
- `xxxxxxxx#` — 8 digits (`x`) followed by 1 letter (`#`, A-Z, case-insensitive)
- `xxxxxxxxx#` — 9 digits (`x`) followed by 1 letter (`#`, A-Z, case-insensitive)
- `@xx##xxxx#` - starts with `T`, `S`, or `R` (`@`, case-insensitive), followed by digits (`x`) and letters (`#`, A-Z, case-insensitive)


---

### Example:

| Original Value                                          | Anonymised Value                  |
|---------------------------------------------------------|---------------------------------|
| My business UEN is 201807324Z.                          | My business UEN is `<SG_UEN>`.  |
| Let's utilise this distribution service, and search 201933199G under SG UEN. | Let's utilise this distribution service, and search `<SG_UEN>` under SG UEN. |
| She runs a few farming companies including Eggcellent, UEN: T12AB3456C, in Singapore. | She runs a few farming companies including Eggcellent, UEN: `<SG_UEN>`, in Singapore. |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
