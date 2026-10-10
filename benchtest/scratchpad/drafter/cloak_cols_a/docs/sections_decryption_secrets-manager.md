# Secrets Manager Usage Guide

The Secrets Manager is where you create, store, share, and audit the encryption keys and salts used in your anonymisation jobs. Instead of managing keys in spreadsheets or passing them around via email, Cloak gives you a secure, centralised location where:

- Keys and salts are stored securely and never exposed to shared users
- You control exactly who has access to each secret
- Usage is auditable, so you can see who used which secret and when
- Secrets persist across role changes, so colleagues can continue work without losing access

To view your list of secrets, click **Secrets** in the sidebar.

![Sidebar button](_resources/secrets-manager-9.png ':size=300x')

*Click Secrets in the sidebar to view your secrets.*

![Secrets List](_resources/secrets-manager-1.png)

*Secrets table*

## Step 1: Create your secret

Get started by creating your first secret to encrypt data with, you are also able to simultaneously share the created secret with other valid (active and verified) Cloak users.

![New secret](_resources/secrets-manager-2.png ':size=650x')

*Create new secret*

![Share secret](_resources/secrets-manager-3.png ':size=650x')

*Share secret with other Cloak users*

## Step 2: Manage your secret

In this step, after creating and/or sharing your secret, you can click the **Edit/manage sharing** button to manage the secret. You can share with **up to 10 other users per operation**, and with a **maximum of 50 users per secret**. You can also simultaneously un-share the secret with any number of users by clicking the "cross" icon in the badge  to remove the user from your member list. 

?> Members of shared secrets **will not be able to view or access the secret key and IV value**, but will be able to use it to decrypt data.

![Manage secret](_resources/secrets-manager-4.png ':size=650x')

*Managing a secret*

Secrets that you **currently share with others** are suffixed by an icon in the "Created by me" tab, while secrets that **others share with you** can be found in the "Shared with me" tab.

![Member's view of shared secret](_resources/secrets-manager-5.png)

*Member's view of shared secret*

## Step 3: Audit Secret

In this step, after sharing your secret, you will be able to click the **View audit** button to audit the shared secret. You can then view essential details of the activities performed with the shared secret, such as the member's email, time of usage and activity type. Additionally, you can review the sharing history of the secret to gain a holistic overview of your shared secret, and monitor any suspicious activities.

### Activities

- ***Decrypt Free Text***: Users decrypts a singular encrypted value
- ***Decrypt Preview***: User selects a secret to preview first 5 rows of decrypted tabular data
- ***Decrypt***: User completes their job to decrypt their tabular data
- ***Download***: User downloads their decrypted tabular data

![Activity history of audited secret](_resources/secrets-manager-7.png)

*Activity history of audited secret*

![Sharing history of audited secret](_resources/secrets-manager-8.png)

*Sharing history of audited secret*

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
