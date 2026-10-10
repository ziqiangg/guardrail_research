# Usage Guide for Free-Text Anonymisation Tool (FTA)

## Step 1: Create a Project  
- Enter a project name and select a project type

![usage-guide-1](_resources/usage-guide-1.png)

*The project creation page with fields for project name and project type selection.*

### Text Input  
- **Paste** your data into the text box (supports basic formatting and word editing features). Alternatively, select **Use a sample** to use one of our examples. Maximum **20,000 characters** (approx. 3,000 words) per submission.

![usage-guide-2](_resources/usage-guide-2.png)

*The rich text editor with sample text containing personal information ready for anonymisation.*

---

### File Upload  
Upload one or more files by dragging and dropping them into the drop zone. You can upload multiple files in a single project, with the following constraints:

- **CSV files** can only be uploaded together with other CSV files (not combined with PDF or DOCX). Maximum **500 MB** per file.
- **PDF and DOCX files** can be combined in the same upload. Maximum **200 MB** per file.
- Up to **100 files** per project, with a total upload limit of **2 GB**.
- Users on COMET/GSIB devices may be blocked by SIS/Menlo for uploads exceeding **500 MB**.

![usage-guide-15](_resources/usage-guide-15.png)
*The file upload interface showing multiple PDF and DOCX files uploaded in a single project.*

**CSV (.csv) files:**
Ensure that your CSV file has proper headers and no or minimal missing values. If you have an Excel (.xlsx) file, convert it into a .csv before uploading.

**PDF (.pdf) files:**
Different types of PDFs will yield different output types.

| Type       | Description                                     | Output       |
|------------|-------------------------------------------------|--------------|
| Native     | Created from electronic files (e.g., Word, PPT) | .docx        |
| Searchable | Text content recognized as machine-readable text| .csv         |
| Scanned    | Created by scanning physical documents/images   | Failed Upload|

**Word (.docx) files:**
Texts within images will not be detected as text.

?> **Need to process more files or automate your workflow?** Cloak's API supports batch file processing (.csv, .docx, .pdf), custom recognisers, and more. See the [API Guide](/sections/developer-api-guide.md) to get started.

---

## Step 2: Anonymise Your Data  
You will be brought to the Transformation Page. Your **Original Data** is displayed on the left, and your **Anonymised Data** is displayed on the right. 

The preview text is **not editable**. The following previews will be displayed: 
  - CSV preview shows first cell only.  
  - PDF preview shows first page only.  
  - Word preview shows first 200 words only.

![usage-guide-3](_resources/usage-guide-3.png)

*The transformation page showing original text on the left and anonymised preview with entity type labels on the right.*

By default, Cloak scans your text for all available [**Entity Types**](/sections/fta/entity-types/intro.md) and [**Replaces**](/sections/fta/anonymisation-techniques/replace.md) them with their data type as the default anonymisation technique.

>The anonymisation techniques selected will be implemented across all cells in CSV files and on all pages for both PDF and Word files.

Click on the **Anonymisation Setting** button to pull up a drawer to toggle the detection of [**Entity Types**](/sections/fta/entity-types/intro.md) and the corresponding [anonymisation technique](/sections/fta/anonymisation-techniques/intro.md) to be applied for each entity type. You may also toggle to the **Custom entities** tab to "**Add a custom entity**" to enter your own list of keywords to detect and transform. 

![usage-guide-4](_resources/usage-guide-4.png)

*The Anonymisation Settings drawer showing entity type toggles, transformation type, and inclusion options.*

You may toggle the [**Confidence Level (Score)**](/sections/fta/advanced-features/confidence-level.md) and [**Inclusion Feature**](/sections/fta/advanced-features/inclusion-feature.md). 

![usage-guide-5](_resources/usage-guide-5.png ':size=500x')

*The confidence level slider allowing adjustment of the detection threshold from 0 to 1.*

---

### Step 2.1: Review Analyser Results (Optional)  
- Click **Review findings** to see details of detected and transformed entities.  

![usage-guide-6](_resources/usage-guide-6.png)

*The Findings table listing each detected entity with its type, transformation applied, original text, anonymised text, and confidence score.*

---

## Step 3: Download  
- Once you are done with your transformations, click on Download to proceed with the download request. 

![usage-guide-11](_resources/usage-guide-11.png ':size=600x')

*The Start Anonymisation confirmation dialog showing file count, estimated processing time, and output format.*

### An approximate processing time will be displayed. For CSV files Here are some general benchmarks:

| Rows | Columns | Estimated Time |
|-------|---------|----------------|
| 20    | 1       | 1 minute       |
| 100   | 1       | 5 minutes      |
| 100   | 2       | 10 minutes     |
| 5000  | 1       | 4 hours       |


- After clicking proceed, a download request notification will appear, before redirecting you to the home page.

![usage-guide-13](_resources/usage-guide-13.png ':size=400x')

*The notification confirming that the download request has been created.*

- Upon reaching the homepage, your file will be available for download when it's ready. Text and PDF projects typically have a fast processing time, while CSV projects may take longer, depending on the number of rows.

![usage-guide-14](_resources/usage-guide-14.png ':size=650x')

*The homepage job card showing a completed job with "Ready for Download" status and download options.*

An email containing the password required to unzip the folder will be sent to you. You can then utilise 7-ZIP (pre-installed on GSIB devices), to enter the password and extract contents. 

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
