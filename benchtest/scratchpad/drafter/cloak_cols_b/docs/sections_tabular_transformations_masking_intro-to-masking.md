# Masking

Masking hides characters of a data value, e.g., by using a constant symbol (such as `*` or `x`). Masking is typically **partial**, meaning it is applied only to some characters in the attribute.

>Cloak supports special masking cases, including **[NRIC](/sections/tabular/transformations/masking/nric-masking.md)**, **email**, and **[landed property](/sections/tabular/transformations/masking/landed-property-masking.md)** masking.

Depending on the nature of the data fields, you can choose a symbol and a fixed number of characters to mask the appropriate characters (for example, masking the octets in IP addresses).

Alternatively, for **complete masking**, a data field could be [suppressed](/sections/tabular/transformations/suppression.md) unless the length of the data values is relevant.

---

## Examples

| Original value | Transformed value | Description                             |
|----------------|-------------------|---------------------------------------|
| 120414         | 120***            | Transforms into a suffix masked value |
| 120414         | ***414            | Transforms into a prefix masked value |
| Alabama        | -----ama          | Transforms into a masked value with a custom character |
| Alabama        | A------           | Transforms into a masked value with a custom number of characters |

---

## Usage Guide

| Inputs            | Description                                    | Default  |
|-------------------|------------------------------------------------|----------|
| Number of Characters | Used to set the number of characters to mask | `3`      |
| Masking Type      | Used to set the type of masking to apply. Valid values include: <br> - **`Suffix`**— masks the starting characters <br> - **`Prefix`**— masks the ending characters | `Suffix` |
| Masking Character | Used to set a masking character                | `-`      |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
