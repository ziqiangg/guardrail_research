# NRIC  
*Singapore National Identification Number*

NRIC refers to Singapore National Identification Number (NRIC Number) and includes:

- Singapore citizens and permanent residents (`"S"`, `"T"`)  
- Foreigners with long-term passes (`"F"`, `"G"`, `"M"`)

---

### Default Setting

- REPLACE NRIC with `<SG_NRIC_FIN>` tag

**Validation disabled:**  
Both real and fake NRIC numbers following the format `@xxxxxxx#` — where `@` is `"S"`, `"T"`, `"F"`, `"G"` or `"M"` (depending on the status of the holder) are detected. 

---

### Example

| **Original Value**                     | **Anonymised Value**                |
|----------------------------------------|-------------------------------------|
| Jason's NRIC is S8372629U.             | Jason's NRIC is `<SG_NRIC_FIN>`.   |
| Amber Heard, T0023857J, is a human.    | Amber Heard, `<SG_NRIC_FIN>`, is a human. |

---

## NRIC Masking

1. As per [SNG (PMO) Circular Minute No. 4/2024](https://intranet.mof.gov.sg/portal/IM/Circulars/ICT/Circular-Minutes/2024/REVISED-ADVISORY-GUIDELINES-ON-NATIONAL-REGISTRATI.aspx) agencies are **no longer allowed** to use **masked / partial NRICs**. This is because the NRIC number’s relatively well-known algorithm makes it easy to derive the full NRIC numbers.
2. You may still wish to anonymise NRICs, for example as a data protection measure, reduce the sensitivity of your datasets or safely fuse datasets using a common identifier.
3. For the above, we recommend [Encryption]((/sections/tabular/transformations/encryption.md)) / [Pseudoanonymisation](/sections/tabular/transformations/pseudonymisation.md) instead, which are more robust forms of anonymization.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
