# 2.7 GCP — First login & setup

This page is the GCP walkthrough for **[First login & setup](../../docs/1015_first_login_and_setup.md)**.

**Goal:** sign in with a Google identity, create one **project** (your first hard box), and link a **Cloud Billing account**.

## On this page

- [Create / sign in](#create--sign-in)
- [First console login](#first-console-login)
- [Day-one security](#day-one-security)
- [What to do next](#what-to-do-next)
- [Where this sits in the syllabus](#where-this-sits-in-the-syllabus)

## Create / sign in

1. Open [cloud.google.com](https://cloud.google.com/) → **Get started for free** or **Console**.  
2. Sign in with a Google account (personal is fine for labs).  
3. Companies later use **Cloud Identity** or Google Workspace with a domain — not required on day one.  
4. Accept the free-trial / billing prompts Google shows for your region.

Official: [Get started with Google Cloud](https://cloud.google.com/docs/get-started)

| First piece | GCP name |
|-------------|----------|
| Hard box | **Project** |
| Who signs in | Google account / **Cloud Identity** |
| Who pays | **Cloud Billing account** |
| Console | [Google Cloud console](https://console.cloud.google.com/) |

## First console login

1. Open the **[Google Cloud console](https://console.cloud.google.com/)**.  
2. Create a **project** (or select the one the trial created). Note the **project ID** — APIs and CLI use it.  
3. Open **Billing** and **link** a Cloud Billing account to that project (needed for most real usage).  
4. Confirm the project picker in the top bar shows your lab project.

Stay in **one project** for learning. A full **Organization** + **folders** tree is optional until you need many projects.

## Day-one security

1. Turn on **2-Step Verification** on the Google account.  
2. Prefer least privilege later (IAM roles on the project) instead of always using the owner account for every click.  
3. Know the split: **Cloud Identity** = who signs in; **Billing account** = who pays; **project** = where resources live.  
4. Optional: set a budget alert on the billing account.

Company tree (Organization, folders) is in [2.3 Organizations & folders](./1010_orgs_folders.md). Deeper IAM is in M2.

## What to do next

- Practice finding Compute Engine, Cloud Storage, and IAM in the console.  
- Keep one lab project; add Organization/folders when you need many boxes.  
- Then continue to **regions & zones**.

## Where this sits in the syllabus

<br/>
<p>
    <span style="float: left;">
        <a href="../../azure/docs/1015_first_login_setup.md">Previous: Azure Registration</a>
        &nbsp;
        <a href="../../docs/1020_regions_availability_zones.md">Next: Topic 3 · Regions</a>
    </span>
    <span style="float: right;">
        <a href="../../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="../../README.md">Cloud</a>
        &nbsp;|&nbsp;
        <a href="../../docs/1015_first_login_and_setup.md">Topic: First login & setup</a>
    </span>
</p>
