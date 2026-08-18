# 2.4 First login & setup (AWS · Azure · GCP)

You finished the three provider trees for accounts / subscriptions / projects. This page is the **shared overview** for first login. Each cloud then has its own walkthrough.

This follows **[Accounts, subscriptions & projects](./1010_accounts_subscriptions_projects.md)**.

## On this page

- [Before you start](#before-you-start)
- [Provider pages](#provider-pages)
- [Quick compare](#quick-compare)
- [Where this sits in the syllabus](#where-this-sits-in-the-syllabus)

## Before you start

| Need | Why |
|------|-----|
| **Email you control** | Every cloud ties signup and recovery to email |
| **Phone** (often) | MFA / verification |
| **Payment method** | Free tiers still usually need a card; watch free-trial limits |
| **One cloud at a time** | Finish first login on one provider before jumping to the next |

**Safety habits (all three)**

- Turn on **MFA** on day one.  
- Avoid daily work as the all-powerful root / global admin.  
- Prefer a **lab / personal** box first — do not invent a full company org tree on day one.

## Provider pages

2.5 AWS — [First login & setup](../aws/docs/1015_first_login_setup.md)  
2.6 Azure — [First login & setup](../azure/docs/1015_first_login_setup.md)  
2.7 GCP — [First login & setup](../gcp/docs/1015_first_login_setup.md)

| Cloud | First hard box | Console |
|-------|----------------|---------|
| **AWS** | Account | Management Console |
| **Azure** | Subscription | Azure portal |
| **GCP** | Project | Cloud console |

## Quick compare

| Step | AWS | Azure | GCP |
|------|-----|-------|-----|
| Sign up / sign in | AWS account (root email) | Microsoft account → Entra tenant | Google account (or Cloud Identity) |
| First hard box | **Account** | **Subscription** | **Project** |
| Open UI | Management Console | Azure portal | Cloud console |
| Pay | Account billing | Billing account → subscription | Billing account → project |
| Day-one security | MFA on root; IAM user next | MFA; avoid living as Global Admin | 2SV; later least-privilege IAM |
| Grow later | Organization + OUs | Root MG + MGs | Organization + folders |

```text
Day one:   create the box  →  open the console  →  turn on MFA
Later:     hang many boxes under the company tree (org / MG / folders)
```

## Where this sits in the syllabus

Next: the three provider first-login pages, then **[Regions & availability zones](./1020_regions_availability_zones.md)**.

Related trees:

- [2.1 AWS · Accounts & Organizations](../aws/docs/1010_accounts_organizations.md)  
- [2.2 Azure · Subscriptions & management groups](../azure/docs/1010_subscriptions_management_groups.md)  
- [2.3 GCP · Organizations & folders](../gcp/docs/1010_orgs_folders.md)

<br/>
<p>
    <span style="float: left;">
        <a href="../gcp/docs/1010_orgs_folders.md">Previous: GCP Organizations</a>
        &nbsp;
        <a href="../aws/docs/1015_first_login_setup.md">Next: AWS Registration</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="../README.md">Cloud</a>
        &nbsp;|&nbsp;
        <a href="./1010_accounts_subscriptions_projects.md">Topic: Accounts, subscriptions & projects</a>
    </span>
</p>
