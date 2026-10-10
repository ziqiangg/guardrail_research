# Custom Entity (Fixed List)

## Detecting a Fixed List of Words as a Custom Entity

If you have a known, finite list of words or phrases to detect (e.g. hospital names, school names, or organisation acronyms), you can use the **Inclusion Feature** together with a **Custom Entity** to anonymise them.

This approach is ideal when:
- You have a predefined list of terms that Cloak's analyser does not recognise by default
- The terms do not follow a predictable pattern; regular expressions are not suitable
- You want exact-match detection for specific words or phrases

---

## Step-by-Step Guide

### 1. Create a Free Text Anonymisation job and open Anonymisation Settings

Navigate to **Free Text Anonymisation** and open an existing project or create a new one. Click the **Anonymisation Settings** button in the top-left corner.

![FTA page with Anonymisation Settings button](../../_resources/Inclusion-Feature-Custom-1.png)

*The Free Text Anonymisation page with the Anonymisation Settings button highlighted in the toolbar.*

### 2. Navigate to Custom Entities and add a new entity

In the **Update anonymisation settings** panel, click on the **Custom entities** tab. Click **"+ Add a custom entity"** to create a new entity type for your inclusion list.

![Custom entities tab with Add a custom entity button](../../_resources/Inclusion-Feature-Custom-2.png)

*The Custom entities tab in the anonymisation settings panel, showing the "+ Add a custom entity" button.*

### 3. Name your custom entity and select Pattern Matching

In the **Add a custom entity** dialog, enter a name for your entity (e.g. "HOSPITAL") and select **"Pattern-matching based"** as the approach. Click **Add entity**.

![Add a custom entity dialog with HOSPITAL name and Pattern-matching based selected](../../_resources/Inclusion-Feature-Custom-3.png ':size=650x')

*The "Add a custom entity" dialog with "HOSPITAL" entered as the entity name and "Pattern-matching based" selected.*

### 4. Upload your word list via the Inclusion feature

Scroll to the bottom of the transformation settings to find your new custom entity. Under the **Inclusion (optional)** section, upload the list of words to detect by clicking **Upload.csv**.

![Custom entity settings showing HOSPITAL with Inclusion section and Upload.csv button](../../_resources/Inclusion-Feature-Custom-4.png)

*The HOSPITAL custom entity settings showing the Inclusion section with the Upload.csv button.*

The CSV to be uploaded should contain a maximum of 500 words listed in the first column.

![Sample CSV with hospital names in column A](../../_resources/Inclusion-Feature-Custom-5.png ':size=400x')

*A sample CSV file listing hospital names and acronyms in the first column.*

You should now see your listed words as tags in the transformation settings.

![Inclusion list populated with hospital name tags](../../_resources/Inclusion-Feature-Custom-6.png)

*The Inclusion section populated with uploaded hospital names displayed as tags.*

> **Note:**
> - This feature is **word-sensitive**: exact spelling and punctuation must match. For example, if "Changi General Hospital" is listed, "Changi-General-Hospital" will **not** be detected.
> - This feature is **not case-sensitive**. For example, if "CGH" is listed, "cgh" will also be detected.
> - Only the first **500 words** in the CSV will be used.

### 5. Save as Template (optional)

To reuse this custom entity configuration in other projects, save your settings as a Template by clicking **Save as template**.

### 6. Transform

Click **Start anonymisation**. Your text is now transformed with the new custom entity applied.

![Transform result showing hospital names replaced with HOSPITAL tags](../../_resources/Inclusion-Feature-Custom-7.png)

*The anonymisation result with hospital names and acronyms replaced by HOSPITAL tags.*

---

## See Also

The Inclusion Feature can also be used to add words to existing default entities (e.g. LOCATION, PERSON) to improve detection of terms that Cloak does not recognise automatically. See [Inclusion Feature](/sections/fta/advanced-features/inclusion-feature.md) for a step-by-step guide.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
