# Templates

If you regularly anonymise datasets with the same structure or settings, you can save your configuration as a **template** and re-apply it in future jobs. Templates are available for both **tabular** and **free-text** anonymisation.

**What a template saves:**

| | Tabular | Free Text |
|---|---|---|
| **Settings stored** | Column info types, sensitivity types, data types, and transformation techniques | Entity types, anonymisation techniques, parameters, and score threshold |
| **Constraint** | Dataset must have the same column names and access mode | None |
| **Sharing** | Can be shared with other Cloak users | Not shareable |
| **Versioning** | Supports updates (new versions) | Save new only |

---

## Save a Template

### Tabular

1. Complete your anonymisation job as usual (Steps 0-3).
2. At **Step 4 (Download your data)**, under **Template settings**, select **"Save as new template"** and enter a template name.

![Template-Tab-1](_resources/Template-Tab-1.png)

*At Step 4, choose "Save as new template" and enter a name for your template.*

3. Click **Review Template** to verify the saved settings (info type, sensitivity type, data type, and transformation for each column).

![Template-Tab-2](_resources/Template-Tab-2.png ':size=650x')

*The Review Template dialog showing each column's configured settings.*

4. Click **"Start the download process"** to save the template and download your anonymised data.

### Free Text

1. Configure your anonymisation settings (entity types, techniques, score threshold) and preview the results.
2. Click **"Save as template"** in the toolbar.

![Template-FTA-1](_resources/Template-FTA-1.png)

*The "Save as template" button appears in the toolbar alongside Anonymisation Settings and Review findings.*

3. In the dialog, enter a **template name** and review the entity/transformation/parameter summary. Click **"Save template"**.

![Template-FTA-2](_resources/Template-FTA-2.png ':size=650x')

*The Save dialog showing template name, score threshold, and the entity configuration that will be saved.*

---

## Use a Template

### Tabular

When creating a new tabular job, select a saved template from the **"Select a tabular job template"** dropdown at Step 0. The template will pre-fill your tagging and transformation settings in Steps 1 and 2.

![Template-Tab-5](_resources/Template-Tab-5.png)

*Select a saved tabular template at Step 0 to auto-apply your previous settings.*

> The uploaded dataset must share the same column names and access mode as the dataset used when the template was saved.

### Free Text

When creating a new free-text job, select a saved template from the **"Select a free text job template"** dropdown at Step 0. The template will pre-fill your entity and anonymisation technique settings.

![Template-FTA-4](_resources/Template-FTA-4.png)

*Select a saved free-text template at Step 0 to auto-apply your previous entity and technique configuration.*

---

## View and Manage Templates

Navigate to **Templates** in the sidebar to view all your saved templates. The page is divided into two tabs: **Tabular Jobs** and **Free Text Jobs**.

### Tabular Jobs tab

Each tabular template card shows its name, creation date, status, and owner. You can:
- **View template** to inspect the saved column settings
- **Share template** to send it to other Cloak users (see below)
- **Delete template** to remove it permanently

![Template-Tab-3](_resources/Template-Tab-3.png)

*The Tabular Jobs tab showing a template card with status, owner, and action buttons.*

### Free Text Jobs tab

Each free-text template card shows its name, creation date, and score threshold. You can:
- **View template** to inspect the saved entity settings
- **Delete template** to remove it permanently

![Template-FTA-3](_resources/Template-FTA-3.png)

*The Free Text Jobs tab showing a template card with score threshold and action buttons.*

---

## Update a Template (Tabular Only)

If you need to modify a saved tabular template:

1. Create a new job using the template (as described above).
2. Make your changes in Steps 1 and 2.
3. At Step 4, select **"Update existing template"** to overwrite the original, or **"Save as new template"** to keep the original untouched and create a new copy.

---

## Share a Template (Tabular Only)

Tabular templates can be shared with other Cloak users. Free-text templates cannot be shared.

1. Navigate to **Templates** in the sidebar and find the template under the **Tabular Jobs** tab.
2. Click **"Share template"**.
3. Enter one or multiple email addresses (separated by commas) and click **"Share"**.

![Template-Tab-4](_resources/Template-Tab-4.png)

*Enter the recipient's email address to share a tabular template with another Cloak user.*

---

## Delete a Template

To delete a template (tabular or free text):

1. Navigate to **Templates** in the sidebar.
2. Click **"Delete template"** on the template card.

Once deleted, the template cannot be recovered.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
