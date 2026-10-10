# Alias

Replace a name with another

>Alias is only available for the **PERSON** entity type.

The **Alias** technique alters the name of an identified individual, with the aim of maintaining the integrity of its cultural/ethnic context. Useful for use cases (e.g. LLM prompts) which require preserving the **Context** and **Consistency** of names in free text.

---

### Example:

| Original value      | Transformed value      | Description              |
|---------------------|------------------------|--------------------------|
| Faris Bin Ali       | Taufiq Bin Syahri      | Malay (M) name detected  |
| Siti Binte Fahmy    | Syakirah Binte Adam    | Malay (F) name detected  |
| Arun S/O Kautham    | Rohan S/O Arjun        | Indian (M) name detected |
| Lashkmi D/O Saddiq  | Diya D/O Ishann        | Indian (F) name detected |
| Jun Jie Lim         | George Choo            | Chinese context detected |
| George Smith        | John Harrison          | No context detected      |

---

### Customisation Options

| Inputs  | Description                                                                                     | Default |
|---------|-------------------------------------------------------------------------------------------------|---------|
| Context | Used to preserve the cultural and ethnic context of the name. When disabled, the altered name will return a western name. | On      |
| Offset  | Used to adjust the offset. When disabled, the altered name will consistently return a constant value. | On      |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
