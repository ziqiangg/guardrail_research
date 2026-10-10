# Introduction

## Identifying Unstructured Data Entities Through Language Models (LM)

> ⚠️ **[Beta Feature]**  
> Currently, only **1 LLM-enabled custom entity** is supported per dataset (up to **5,000 documents**). We're working to expand support to larger datasets, multiple entities, and shorter processing times.  
> 💬 Feedback or requests? Email us at [cloak@tech.gov.sg](mailto:cloak@tech.gov.sg).

>Including an LLM-enabled custom entity may increase processing times to **up to 8 hours**.  
>Sit tight! We’ll notify you via email when your job is complete.

---

## What Are Unstructured Entities?

Unstructured entities refer to data **without predictable, fixed patterns** — examples include:

- School names  
- Medical conditions  
- Free-text descriptions  

Cloak allows you to add such custom entities through few-shot prompting, which allows the LLM to detect new entities without fine-tuning. This approach only needs a small set of 3-5 examples (labelled data) instead of labelling a large dataset to train a classifier. 

Cloak privately hosts a language model within our own secure environment on the Government Commercial Cloud (GCC) on AWS. No data is sent to external parties, and this approach is safe for data classified up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH).

---

## When Should You Use This Feature?

As this approach utilises Language Models and requires more processing power and time, we recommend that users only use this feature where:  

- Your entity is not included in Cloak’s pre-defined entities, and is unstructured. For structured entities, try our custom entities (structured) feature.  
- Your entity is not detected accurately due to the unique context of your documents (e.g., formatting).  

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
