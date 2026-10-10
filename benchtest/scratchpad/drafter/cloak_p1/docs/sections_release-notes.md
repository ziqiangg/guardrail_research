# Release Notes

All release notes for Cloak.

---

## Legend

| Acronym    | Description                   |
|------------|-------------------------------|
| Tabular    | Tabular Data Anonymisation    |
| FTA        | Free Text Anonymisation       |
| MDG        | Mock Data Generation          |
| SDG        | Synthetic Data Generation     |
| Decryption | Decryption and Secret Sharing |

---

## `v2.2.2` (Released on 4 August 2024)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- Miscellaneous bug fixes and improvements

---

## `v2.2.1` (Released on 28 August 2024)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- Miscellaneous bug fixes and improvements

---

## `v2.2.0` (Released on 07 August 2024)

**Features**

- Intranet API

**Improvements**

- New API Request flow

**Bug Fixes**

- Miscellaneous bug fixes and improvements

---

## `v2.1.9` (Released on 07 August 2024)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- Miscellaneous bug fixes and improvements

---

## `v2.1.8` (Released on 31 July 2024)

**Features**

N/A

**Improvements**

- Added the Salt ID in the Salt display table

**Bug Fixes**

- Miscellaneous bug fixes and improvements

---

## `v2.1.7` (Released on 24 July 2024)

**Features**

N/A

**Improvements**

- Added fields for whitelisted account creation

**Bug Fixes**

- Miscellaneous bug fixes and improvements

---

## `v2.1.6` (Released on 10 July 2024)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- Miscellaneous bug fixes and improvements

---

## `v2.1.5` (Released on 3 July 2024)

**Features**

- Secure Internet API (L4)

**Improvements**

- [FTA] Regex custom entities

**Bug Fixes**

N/A

---

## `v2.1.4` (Released on 4 June 2024)

**Features**

N/A

**Improvements**

- [FTA] Allow bulk upload of inclusion/ exclusion list (e.g. txt or csv file)
- [FTA] Support for custom salts and user managed salts
- [FTA] Allow for user managed secret keys
- [Tabular] Inform user if file is password protected on upload

**Bug Fixes**

- [Tabular] Error when parsing headers of excel file when newline exists.
- [General] Bug fixes for notifications and miscellaneous items.

---

## `v2.1.3` (Released on 27 May 2024)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- [General] Bug fixes and updates

---

## `v2.1.2` (Released on 1 Apr 2024)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- [Tabular] Fixed issue when WOG B fails transformation, it does not get re-routed back to Step 2.
- [Tabular] Fixed issue when a column contains a long free-text data, the upload fails.

---

## `v2.1.1` (Released on 19 Mar 2024)

**Features**

- [Packages] Added approval flow before downloading package file.

**Improvements**

- [Packages] Guide for specific packages moved to internal pages instead of homepage.

**Bug Fixes**

N/A

---

## `v2.1.0` (Released on 19 Mar 2024)

**Features**

- [Decryption] Decrypt encrypted free-text or tabular data using secret keys.
- [Secrets & Salts] View the usage and sharing history of secrets that you own.
- [Secrets & Salts] Manage and share secret keys and salt values with others.
- [Notifications] In-app notifications to receive real-time alerts and updates
- [Packages] Leverage Cloak's transformation techniques using downloadable Python Packages.
- [FTA] Create and reuse project settings as templates

**Improvements**

- [Tabular] The option to select a sample dataset for experimenting with Tabular Anonymisation
- [FTA] Added the ORGANIZATION entity type
- [FTA] Added salt parameter for Pseudonymisation transformation
- [General] UI updates and fixes

**Bug Fixes**

- [FTA] Fixed uploads for PDF and Word doc

---

## `v2.0.7` (Released on 11 Mar 2024)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- [FTA] Fixed double quotes escaping during transformation

---

## `v2.0.6` (Released on 4 Mar 2024)

**Features**

- [Tabular] Auto tag identifiers on Step 1 to assist with manual tagging of columns.
- [Tabular] Add a new button to allow user to execute NLP auto tagging on Step 1.

**Improvements**

N/A

**Bug Fixes**

- [FTA] Fixed "Exceptions" toggle not functioning as expected.
- [FTA] Fixed issue preventing downloads from completing successfully.

---

## `v2.0.5` (Released on 20 Feb 2024)

**Features**

N/A

**Improvements**

- [FTA] Updated FTA API guide with "allow_list" parameters which allows a list of **text** to be excluded from detection.

**Bug Fixes**

- [FTA] Fixed an issue when the settings under preview is not taking effect on csv files.

---

## `v2.0.4` (Released on 29 Jan 2024)

**Features**

- Implemented further security checks on login when using username + password combination.

**Improvements**

- Added notifications banner on login page.
- [MDG] Allows REGEX feature.

**Bug Fixes**

- [MDG] Fixed injecting custom values.
- [FTA] Fixed inconsistent output rows due to unclean data.
- [FTA] Fixed uploading PDF files.

---

## `v2.0.3` (Released on 15 Jan 2024)

**Features**

- [FTA] Support select columns from CSV files (Maximum 10 columns)

**Improvements**

- [FTA] Improved the performance, now can support up to 100k rows * 10 columns per CSV file.

**Bug Fixes**

- [FTA] Fixed a bug when special characters found from CSV header e.g. "/".
- [FTA] Fixed a bug when "Pipe character" is selected as CSV delimiter.
- [FTA] Fixed a bug when CSV file contains more than 1.3k rows.

---

## `v2.0.2` (Released on 18 December 2023)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- [Tabular] previously excel files failed during upload due to duplicate header names.
- [Tabular] report generation failed due to removal transformation.

---

## `v2.0.1` (Released on 4 December 2023)

**Features**

- [FTA] Added Word document support
- [API] Reconstruct endpoint for FTA API

**Improvements**

- [Tabular] Allow users to restart a job even on anonymisation failure.
- [FTA] Dedicated modal for Downloads
- [MDG] Generate Real NRIC

**Bug Fixes**

- [FTA] Miscellaneous issues related to highlighting of PII entities

---

## `v2.0.0` (Released on 20 November 2023)

**Features**

- Rebranding of enCRYPT to Cloak.
- [Tabular] Support for selecting columns on upload (max at 100).
- [FTA] Added CSV upload flow to support multi-line anonymisation.
- [MDG] Generate UEN (Selection: UEN Types)
- [MDG] Generate Agency Name / Agency Acronyms (Selection: Camel case/Uppercase)
- [API] General Availability of Tabular and Free Text Anonymisation API.

**Improvements**

- [MDG] Allow multiple custom string values
- [MDG] Generate Decimal based on no. of decimal places

**Bug Fixes**

N/A

---

## `v1.3.0` (Released on 08 August 2023)

**Features**

- [API] Availability of Free Text Anonymisation API for selected users.

**Improvements**

- [Tabular] Allow downloads to occur even if report does not generate successfully.

**Bug Fixes**

N/A

---

## `v1.2.2` (Released on 06 July 2023)

**Features**

- [Tabular] Availability of export data feature from enCRYPT to Analytics.Gov through API integration.

**Improvements**

- New tab "API Keys" to facilitate the new export data feature.

**Bug Fixes**

N/A

---

## `v1.2.1` (Released on 27 June 2023)

**Features**

N/A

**Improvements**

- [Tabular] Accepting higher column support of up to 50 columns from 20.
- [Tabular] Supporting of Excel files.

**Bug Fixes**

N/A

---

## `v1.2.0` (Released on 23 June 2023)

**Features**

- [MDG] Mock Data Generation feature availability
- [FTA] Free Text Anonymisation feature availability
- [Tabular] New Transformation type Generalisation Categorical added
- [Tabular] Field Level Encryption.

**Improvements**

- Overhaul to the homepage to include navigations to new features such as Mock Data Generation and Free Text Anonymisation.
- Secrets tab added in home page to supplement Field Level Encryption function.

**Bug Fixes**

N/A

---

## `v1.1.0` (Released on 24 April 2023)

**Features**

- [Tabular] Perturbation transformation added

**Improvements**

- [Tabular] Added tooltips with full attribute names on Step 2
- [Tabular] Auto refresh of main page if jobs were in preparing, uploading or transforming status.
- Users who has access to WOG AD logins have their password based login disabled; to login using WOG AD only.

**Bug Fixes**

N/A

---

## `v1.0.3` (Released on 4 April 2023)

**Features**

N/A

**Improvements**

N/A

**Bug Fixes**

- K-anonymity - previously was erroneously dropping the first column during transformation.

---

## `v1.0.2` (Released on 31 March 2023)

**Features**

- [Tabular] Allow users to delete jobs

**Improvements**

- [Tabular] Changed email template for user download link
- [Tabular] Immediately removing raw data after user downloads transformed data.

**Bug Fixes**

- [Tabular] Report generation - previously fails when null values are found on the pie chart segment.

---

## `v1.0.1` (Released on 20 March 2023)

**Features**

N/A

**Improvements**

- [Tabular] Accept ISO format from frontend on generalisation techniques for periodic dates.
- Performance improvements in compute for backend.

**Bug Fixes**

- [Tabular] Generalisation transformation - previously large numbers becomes scientific notations and grouped wrongly.

---

## `v1.0.0` (Released on 13 March 2023)

**Features**

- [Tabular] Anonymisation Flow according to Whole-of-Government data sharing policy for CSV files up to 20 columns and 100MB in size.

**Improvements**

N/A

**Bug Fixes**

N/A
