# Address (SG)

Cloak provides 4 address-related recognisers for Singapore addresses:

| Entity | What it detects | Default | Method |
|--------|----------------|---------|--------|
| SG_ADDRESS | Full Singapore addresses (street + postal code + unit number together) | ON | Pattern matching |
| SG_ADDRESS_POSTAL_CODE | 6-digit Singapore postal codes (e.g. 520123) | ON | Regex |
| SG_ADDRESS_UNIT_NUMBER | Unit/floor numbers (e.g. #05-123, Blk 123) | ON | Regex |
| SG_ADDRESS_STREET | Street names alone (e.g. "Bukit Timah Road") | OFF (advanced) | Pattern matching |

?> The 3 default-on entities cover most use cases. Full addresses, postal codes (which in Singapore often map to a single building), and unit numbers are the highest-risk identifiers.

**SG_ADDRESS_STREET** is not on by default because street names alone are lower-risk and have higher false-positive rates - they overlap with location names and common words like "Victoria" or "Orchard".

!> Turn on **SG_ADDRESS_STREET** if your text contains partial addresses - e.g. "lives on Bukit Timah Road" without a full address - where SG_ADDRESS alone might miss the fragment.

---

## Full Address

*Full Singapore addresses (street + postal code + unit number together)*

### Default setting:

- REPLACE all Full Address values with `<SG_ADDRESS>` tag.

### Examples:

| Original Value | Anonymised Value |
|----------------|-----------------|
| My Singapore address is Block 555 Tampines North Drive 12 #11-11 Singapore 510555. | My Singapore address is `<SG_ADDRESS>`. |
| The nearest mall is at 20 Jurong West Street 26, S648886. | The nearest mall is at `<SG_ADDRESS>`. |

---

## Postal Code

*6-digit Singapore postal codes*

### Default setting:

- REPLACE postal codes with `<SG_ADDRESS_POSTAL_CODE>` tag.
- Overridden if Full Address detection is enabled.

> We are improving our algorithm to improve accuracy for this field. If this field is not accurately detected, you may wish to use the Inclusion or Exceptions feature.

### Examples:

| Original Value | Anonymised Value |
|----------------|-----------------|
| You can mail it to me at 511256. | You can mail it to me at `<SG_ADDRESS_POSTAL_CODE>`. |
| I believe his postal code is S256 310. | I believe his postal code is `<SG_ADDRESS_POSTAL_CODE>`. |

---

## Unit Number

*Unit/floor numbers (e.g. #05-123, Blk 123)*

### Default setting:

- REPLACE unit numbers with `<SG_ADDRESS_UNIT_NUMBER>` tag.
- Overridden if Full Address detection is enabled.

### Examples:

| Original Value | Anonymised Value |
|----------------|-----------------|
| My unit number is #12-23. | My unit number is `<SG_ADDRESS_UNIT_NUMBER>`. |
| The shop you wanted is at #02-154. | The shop you wanted is at `<SG_ADDRESS_UNIT_NUMBER>`. |

---

## Street Name

*Street names alone (e.g. "Bukit Timah Road")*

### Default setting:

- OFF by default. Enable in Anonymisation Settings under advanced entities.
- REPLACE street names with `<SG_ADDRESS_STREET>` tag.

### Examples:

| Original Value | Anonymised Value |
|----------------|-----------------|
| She lives along Bukit Timah Road. | She lives along `<SG_ADDRESS_STREET>`. |
| The office is on Victoria Street. | The office is on `<SG_ADDRESS_STREET>`. |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
