# Landed Property Masking

Landed property masking hides the last 3 digits of a landed property's zipcode. The zipcodes of multi-unit properties (e.g. HDB blocks) are retained in full.

---

## Examples

| Original value | Transformed value | Description                                                        |
|----------------|-------------------|--------------------------------------------------------------------|
| 123456         | 123***            | Transforms into value with masked last 3 digits if the zipcode belongs to a landed property |
| 120414         | 120414            | Retains the value if the zipcode belongs to a multi-unit building  |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
