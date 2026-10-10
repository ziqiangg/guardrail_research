# Replace (Unique)

Replace detected entities with unique, numbered placeholders while maintaining consistent replacements throughout the text.

Unlike standard [Replace](/sections/fta/anonymisation-techniques/replace.md), which uses the same placeholder for all entities of a given type, Replace (Unique) assigns a distinct numbered placeholder to each unique entity value. This allows you to distinguish between different entities after anonymisation while preserving how they relate to one another.

---

## Example

**Input:**

> Case worker Jane Huang conducted a home visit with client Marcus Lee on 12 July 2026.
>
> During the visit, Marcus Lee shared concerns about caring for his mother, Alicia Lee. Jane Huang discussed available caregiver support schemes and arranged a follow-up appointment. Two weeks later, Jane contacted Marcus to check on his progress.

**Standard Replace output:**

> Case worker \<PERSON\> conducted a home visit with client \<PERSON\> on \<DATE_TIME\>.
>
> During the visit, \<PERSON\> shared concerns about caring for his mother, \<PERSON\>. \<PERSON\> discussed available caregiver support schemes and arranged a follow-up appointment. \<DATE_TIME\>, \<PERSON\> contacted \<PERSON\> to check on his progress.

![Standard Replace; all entities share the same placeholder](../../_resources/Replace-Unique-1.png)

*Standard Replace output in Cloak, where all detected person entities share the same generic placeholder.*

**Replace (Unique) output:**

> Case worker \<PERSON_1\> conducted a home visit with client \<PERSON_2\> on \<DATE_TIME\>.
>
> During the visit, \<PERSON_2\> shared concerns about caring for his mother, \<PERSON_3\>. \<PERSON_1\> discussed available caregiver support schemes and arranged a follow-up appointment. \<DATE_TIME\>, \<PERSON_4\> contacted \<PERSON_5\> to check on his progress.

![Replace (Unique); each unique entity gets a distinct numbered placeholder](../../_resources/Replace-Unique-3.png)

*Replace (Unique) output, where each distinct entity receives a unique numbered placeholder.*

This allows you to understand that:

- Multiple distinct individuals are involved;
- The same individual is referenced consistently across the text; and
- The relationships between individuals are preserved,

without revealing their identities.

---

## Configuring Replace (Unique)

1. Open **Anonymisation Settings**.
2. Select **Replace (Unique)** as the transformation type for the desired entity.
3. Enter the placeholder value in the **Replace (Unique) with** field (e.g. `<PERSON>`).
4. Click **Apply anonymisation settings**, then run anonymisation.

Cloak will automatically append a unique number to your placeholder for each distinct entity detected:

```
<PERSON_1>
<PERSON_2>
<PERSON_3>
```

![Replace (Unique) configuration panel](../../_resources/Replace-Unique-2.png)

*The Anonymisation Settings panel with Replace (Unique) selected as the transformation type.*

---

## Important: Entity Matching is Based on Detected Value

Replace (Unique) assigns placeholders based on the **detected entity value**, not on whether references belong to the same real-world individual.

For example:

| Input text | Detected as | Placeholder |
|---|---|---|
| Jane Huang | PERSON | \<PERSON_1\> |
| Jane | PERSON | \<PERSON_2\> |

Because "Jane Huang" and "Jane" are detected as different entity values, they receive different placeholders, even if they refer to the same person.

This behaviour is expected and applies to all supported entity types.

---

## Availability and Limitations

Replace (Unique) is currently available:

- On the Cloak Web App;
- For single CSV uploads; and
- For Cloak's baseline entities (see [Supported Entities](/sections/fta/entity-types/intro.md)).

Replace (Unique) is **not** currently available for:

- PDF files;
- DOCX files;
- Multi-file uploads; or
- Custom entities (including custom regex and dictionary entities).

### Processing Time

Replace (Unique) requires additional processing to maintain consistent entity mappings throughout the file. Anonymisation may take longer than standard Replace.

### Up to Two Entity Types at a Time

Replace (Unique) currently supports up to **two entity types** per anonymisation job.

For example, you may configure:

| Entity | Transformation |
|---|---|
| PERSON | Replace (Unique) |
| ORGANISATION | Replace (Unique) |
| EMAIL | Replace |
| PHONE | Mask |

But you **cannot** apply Replace (Unique) to more than two entity types in the same job:

| Entity | Transformation |
|---|---|
| PERSON | Replace (Unique) |
| ORGANISATION | Replace (Unique) |
| EMAIL | Replace (Unique) |

?> If you would like support for additional file formats, custom entities, or multiple Replace (Unique) entity types in a single job, please let us know via [Cloak Support](https://go.gov.sg/cloak-support).

---

## For Developers: Replace (Unique) via API

Need consistent replacements **across multiple documents**, or require support for more than two entity types, custom entities, or non-CSV formats? You can achieve Replace (Unique) behaviour programmatically using Cloak's `/analyze` endpoint and a mapping table you maintain.

See the full guide: [Replace (Unique) via API](https://docs.developer.tech.gov.sg/docs/cloak-api-guide/sections/api-reference/free-text-anonymisation/replace-unique)

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
