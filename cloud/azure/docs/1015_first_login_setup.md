# 2.6 Azure — First login & setup

This page is the Azure walkthrough for **[First login & setup](../../docs/1015_first_login_and_setup.md)**.

**Goal:** sign in, get a **billing** path, and open one **subscription** (your first hard box) in the portal.

## On this page

- [Create / sign in](#create--sign-in)
- [First portal login](#first-portal-login)
- [Day-one security](#day-one-security)
- [What to do next](#what-to-do-next)
- [Where this sits in the syllabus](#where-this-sits-in-the-syllabus)

## Create / sign in

1. Open [azure.microsoft.com](https://azure.microsoft.com/) → **Start free** or **Sign in**.  
2. Use a Microsoft account (personal) or work/school account. Free-trial paths vary by region and offer.  
3. Complete identity checks and any payment step for trial or pay-as-you-go.  
4. Accept the subscription / agreement screens until a subscription exists.

Official: [Create an Azure account](https://azure.microsoft.com/pricing/purchase-options/azure-account)

| First piece | Azure name |
|-------------|------------|
| Hard box | **Subscription** |
| Who signs in | **Microsoft Entra ID** tenant |
| Who pays | **Billing account** |
| Console | [Azure portal](https://portal.azure.com/) |

## First portal login

1. Open the **[Azure portal](https://portal.azure.com/)**.  
2. Go to **Subscriptions** — confirm at least one subscription (your hard box).  
3. Open **Microsoft Entra ID** — that tenant is who can sign in.  
4. Note your default directory / tenant name.  
5. Optionally create a **resource group** inside the subscription for later labs (packaging inside the box).

Stay in **one subscription** for learning. **Management groups** come later when you need many subscriptions.

## Day-one security

1. Turn on **MFA** for your account.  
2. Avoid living every day as **Global Administrator**. Prefer a named admin for portal work when you can.  
3. Know who owns billing (billing account roles) vs who owns the subscription (RBAC).  
4. Optional: set a budget / cost alert on the subscription.

Company tree (Tenant Root MG, child MGs) is in [2.2 Subscriptions & management groups](./1010_subscriptions_management_groups.md). Deeper identity is in M2.

## What to do next

- Practice finding Virtual machines, Storage accounts, and Resource groups.  
- Keep one lab subscription; grow MGs only when you need isolation.  
- Then continue to GCP first login, or jump to regions.

## Where this sits in the syllabus

<br/>
<p>
    <span style="float: left;">
        <a href="../../aws/docs/1015_first_login_setup.md">Previous: AWS Registration</a>
        &nbsp;
        <a href="../../gcp/docs/1015_first_login_setup.md">Next: GCP Registration</a>
    </span>
    <span style="float: right;">
        <a href="../../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="../../README.md">Cloud</a>
        &nbsp;|&nbsp;
        <a href="../../docs/1015_first_login_and_setup.md">Topic: First login & setup</a>
    </span>
</p>
