# Entity Types

Cloak's FTA Tool caters for common data fields that expose individuals or businesses to potential.

Entity types are identified either by the underlying AI Model (e.g. [spaCy](https://spacy.io/models/en#en_core_web_sm)), and a combination of:
- [Regex Patterning](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)  
- [Rule-based Matching](https://spacy.io/usage/rule-based-matching)  
- Validation using checksums (if applicable)

---

## Available Entity Groups

The following entity groups are currently available:

- Personal 
    - Name
    - NRIC (SG)
    - Email Address
    - Phone Number
    - Nationality/Race/Religion
    - Address (SG)
    - Location
    - Passport (SG)
- Financial
    - Currency
    - Credit Card
    - Bank Account Number (SG)
    - Bank Account Number (IBAN)
- Technical Security
    - IP Address
    - URL
- Others
    - Date & Time
    - UEN (SG)
    - Organization
    - Exceptions
    - Custom

> Click [here](https://microsoft.github.io/presidio/supported_entities/) for general information on the PII entities supported by Presidio.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
