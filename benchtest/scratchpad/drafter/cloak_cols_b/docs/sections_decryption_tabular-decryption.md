# Tabular Decryption Usage Guide

## Step 0: Upload your data

Get started by clicking **Decryption** in the sidebar.

![Sidebar button](_resources/tabular-decryption-9.png ':size=300x')

*Click Decryption in the sidebar to access the decryption options.*

Click **Decrypt Tabular Data**.

![Decryption options](_resources/tabular-decryption-10.png)

*Choose between Decrypt Free Text Data or Decrypt Tabular Data.*

Press the **Decrypt a tabular file** button near the top right corner of the page.

![Decrypt file button](_resources/tabular-decryption-11.png)

*The tabular decryption page showing existing jobs and the "Decrypt a tabular file" button.*

Uploading your **encrypted tabular dataset** that requires decryption. A preview of your dataset will be provided before you choose to upload your dataset.

?> Cloak supports datasets classified up to **Confidential (Cloud-Eligible)** and/or **Sensitive (High)**. Please make sure that data is processed in the proper environment (e.g. GSIB laptop) with proper security controls in place.

![Preview encrypted](_resources/tabular-decryption-1.png ':size=650x')

*Preview of encrypted dataset*

## Step 1: Select the secret you used to encrypt your dataset

This step allows you to choose which secret to use when decrypting your dataset, additionally for secrets that you own and have shared with others. You can also view who has access to that secret by clicking the icon  under the "Actions" column.

![Select secret](_resources/tabular-decryption-2.png ':size=500x')

*Selected secret to decrypt with*

![Member list](_resources/tabular-decryption-3.png ':size=500x')

*Member list of shared secret*

## Step 2: Select columns to decrypt

In this step, after selecting your secret, the columns that can be decrypted successfully will be auto-selected for you.

![Decrypted data](_resources/tabular-decryption-5.png)

*Decrypted Data Field (NRIC)*

After selecting the columns to be decrypted, click the **Start decryption** button near the top right corner of the page.

## Step 3: Download your decrypted dataset

You may decrypt and then download your password-protected dataset in the final step. You will receive a **real-time notification** on the page when the download is ready, and an **email notification** containing the password for your download will also be sent to your registered email. Your download will be **available for up to 24 hours** from the job creation time.

!> Cloak does not store your data. Data is routinely purged from the system after completion of transformation jobs.

![Results notification](_resources/tabular-decryption-6.png ':size=400x')

*Real-time notification for download*

![Email containing password](_resources/tabular-decryption-7.png ':size=650x')

*Email containing password for downloaded zip file*

## Step 4: Review your decrypted dataset

If any of your chosen columns to decrypt contain any values that **failed to decrypt**, a separate csv file named **"failed_cells.csv"** will be provided in the download for you to easily identify the column name and the row number of the value(s) in your decrypted csv file, allowing you to easily rectify any possible errors.

![Outcome](_resources/tabular-decryption-8.png ':size=350x')

*The "failed_cells.csv" file lists the column name and row number of any values that failed to decrypt.*

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
