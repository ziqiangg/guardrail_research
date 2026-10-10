# Masking

## Conceal using a character provided

Masking hides characters of a data value, e.g. by using a constant symbol (e.g. `*` or `x`). Masking is typically partial, i.e. applied only to some characters in the attribute.

FTA currently supports general **Masking** and special **NRIC Masking** (for NRIC entity types only).

Find out more about masking [here](/sections/tabular/transformations/masking/intro-to-masking.md).

### Example

| Original value | Transformed value | Description                                                           |
|----------------|-------------------|-----------------------------------------------------------------------|
| 120414         | 120***            | Transforms into a **suffix** masked value                             |
| 120414         | ***414            | Transforms into a **prefix** masked value                             |
| Alabama        | -----ama          | Transforms into a masked value with a **custom character**            |
| Alabama        | A------           | Transforms into a masked value with a **custom number of characters** |

---

## Usage Guide

| Input                 | Description                                            | Default |
|-----------------------|--------------------------------------------------------|---------|
| **Number of Characters** | Used to set the number of characters to mask           | `3`       |
| **Masking Type**          | Used to set the type of masking to apply <br><br> Valid values include: <br> `Suffix`: masks the starting characters <br><br> `Prefix`: masks the ending characters   |  `Suffix`       |
| **Masking Character**     | Used to set a masking character                        | `-`     |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
