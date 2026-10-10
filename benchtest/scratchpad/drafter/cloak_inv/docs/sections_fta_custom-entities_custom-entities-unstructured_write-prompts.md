# How to Write Prompts

>Prompt engineering is iterative! As LLM-enabled custom entities require longer processing times, we recommend to: 
>1. Test your definition and examples using Cloak's transformation preview or run a job on a smaller dataset (e.g., <100 documents, which should take <20min).
>2. Examine the output for incorrect detections and improve on the prompt (e.g., include edge cases, clarify ambiguities).
>3. Repeat til desired performance is achieved. You can then run a job on your full dataset.
>4. Still stuck? We'd love to discuss your requirements at cloak@tech.gov.sg. 

---

## Tips and Tricks

### Setting the Entity Name

| **Tip**                          | **Positive Example**         | **Negative Example**      |
|----------------------------------|-------------------------------|----------------------------|
| Reduce ambiguity                 | `PERSON_NAME`, `BUILDING_NAME` | `NAME`                    |
| Use commonly found words         | `LOCATION`                    | `SPATIAL_DESIGNATION`     |

---

### Setting the Definition

| **Tip**                                                              | **Positive Example**                                   | **Negative Example**                   |
|-----------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------|
| Use simple, easy-to-understand language                               | "Find email addresses"                                   | "Detect electronic mail communication identifiers" |
| Avoid jargon and acronyms without wide consensus                      | "Credit card number"                                     | "PAN sequences"                         |
| Provide context and common attributes                                 | "Name of a person residing in Singapore..."              | "Name of a person"                      |
| Provide examples                                                      | "Chinese (e.g., Tan Mei Ling), Malay (Mohammad Bin Ali)" |                                         |

---

## Writing Examples

Variety is key, and quality triumphs quantity! Include 3-5 examples that captures the diversity present in your dataset. 

| **Tip**                                                                                      | **Example**                                                                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Context matters: Provide examples in realistic sentences or paragraphs (including formatting pecularities like xml tags) and represent instances where the entity appears in different parts of the text.  | 1. Patient Tan Mei Ling (S9012345B) was admitted 01-01-25. <br> 2. `ent:PatientRecord<br>Tan Mei Ling<br>S9012345B<br>01-01-25` |
| Provide examples that cover the diverse ways that the entity can be represented (e.g., completeness, spelling, numerical formats, special characters) | 1. Tan Mei Ling <br> 2. Tan Mei Ling (Donna) <br> 3. Ms. Tan <br> 4. Mei Ling                                |
| Where there might be ambiguity, provide examples that clearly demonstrate what should and should not be labelled | *E.g., If you want to identify only specific date/time expressions, not general temporal expressions* <br><br> 1. 6 year old patient admitted **30 Jan 2025, 09:10 AM**, reported chalazion every 3 months in the bilateral eye. <br> 2. Mother takes care of the patient during the weekend. Follow-up scheduled in two weeks on **30-06-2025** <br><br> *E.g., if context determines if something should be identified* <br><br> 1. My mom contacted **MOM** regarding her employment incident <br> 2. The patient presented with **AIDS** and has been receiving government aids for the condition. |

---

## Sample: Disease

| **Field**      | **Details**                                                                                                                                | **Notes** |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Entity Name**| `DISEASE`                                                                                                                                  |           |
| **Definition** | Name of a medical disease or condition. It can be represented in various formats, including acronyms and abbreviations (e.g. MS, IBD, COPD), with mispellings (e.g., Astma, Alzimer's) and variants (e.g., RA, Rh. Arth, Rheum Arthrtis, RhA).  | Specifies ways that the entity can be present in the text, and provides examples
| **Example 1**|`ent:MedicalInfo<br>**UlcerativeColitis**<br>**IBS**<br>mesalamine once daily`| Provides a realistic example of how the entities are present in the text (e.g., template generated section). <br> Includes spelling errors.  |
| **Example 2**| Mr. Wong, 67, seen for **Bronchitc COPD**, reporting persistent cough with sputum. History of **Emphyzma**. | Provides a realistic example of how the entities are present in the text (e.g., main narrative body). <br> Includes spelling errors and acronyms.          |
| **Example 3**|Ms. Roberts follows up for **M-Sclerosis** and reports increased hand tremors, raising concern for a transition to **SPMS**. | Includes acronyms and alternative representations (e.g., "M-Sclerosis" and "SPMS" for multiple sclerosis) |

### Output

![write-prompts-1](_resources/write-prompts-1.png)

*Transformation preview showing a patient record with disease names detected and replaced with DISEASE tags in the anonymised output.*

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
