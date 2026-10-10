# Inclusion Feature

## Improve Detection by Adding Words to an Existing Entity

The **Inclusion Feature** allows you to specify additional words or phrases that should be detected and anonymised under an existing entity type. This is useful when Cloak's analyser does not automatically recognise certain terms; for example, specific location names, organisation acronyms, or domain-specific terminology that should be tagged under an existing entity.

You can add words individually or upload a CSV file containing up to 500 entries.

---

## Example Scenario

In the example below, the text mentions "BMTC School, Pulau Tekong". While "Pulau Tekong" is automatically detected as a `<LOCATION>`, "BMTC School" is not recognised by Cloak's default analyser.

![FTA page showing BMTC School not detected as a location](../../_resources/Inclusion-Feature-Location-1.png)

*The anonymised preview shows that "BMTC School" is not detected as a location entity by default.*

By adding "BMTC School" to the **LOCATION** entity's inclusion list, you can ensure it is detected and anonymised correctly.

---

## Step-by-Step Guide

### 1. Open Anonymisation Settings

Navigate to your Free Text Anonymisation project. Click the **Anonymisation Settings** button in the top-left corner.

### 2. Find the entity you want to improve and add words to its Inclusion list

In the **Update anonymisation settings** panel, stay on the **Default entities** tab. Scroll to the entity you want to add words to (e.g. LOCATION). Under the **Inclusion (optional)** section, type the word or phrase you want Cloak to detect and press Enter. You can also click **Upload.csv** to bulk-upload a list of words.

![LOCATION entity with BMTC School added to the inclusion list](../../_resources/Inclusion-Feature-Location-2.png)

*The LOCATION entity settings panel with "BMTC School" added to the inclusion list.*

### 3. Apply settings and transform

Click **Apply anonymisation settings**, then click **Start anonymisation**. The words you added to the inclusion list are now detected under that entity type.

![Transform result showing BMTC School now detected as LOCATION](../../_resources/Inclusion-Feature-Location-3.png)

*After applying the inclusion list, "BMTC School" is now correctly detected and anonymised as a LOCATION entity.*

---

## Important Notes

| Behaviour | Detail |
|-----------|--------|
| **Word-sensitive** | Exact spelling and punctuation must match. For example, if "BMTC School" is listed, "BMTC-School" will **not** be detected. |
| **Not case-sensitive** | Matching is case-insensitive. For example, if "BMTC School" is listed, "bmtc school" will also be detected. |
| **500-word limit** | Only the first 500 words in a CSV upload will be used. |

---

## See Also

The Inclusion Feature can also be used to create entirely new custom entities with a fixed list of words to detect. See [Custom Entity (Fixed List)](/sections/fta/custom-entities/custom-entities-fixed-list.md) for a step-by-step guide.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
