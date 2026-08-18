# 2.5 AWS — First login & setup

This page is the AWS walkthrough for **[First login & setup](../../docs/1015_first_login_and_setup.md)**.

**Goal:** create one **AWS account** (your first hard box), open the console, and lock down day-one access.

## On this page

- [Create the account](#create-the-account)
- [First console login](#first-console-login)
- [Day-one security](#day-one-security)
- [What to do next](#what-to-do-next)
- [Where this sits in the syllabus](#where-this-sits-in-the-syllabus)

## Create the account

1. Open [aws.amazon.com](https://aws.amazon.com/) → **Create an AWS Account** (or **Sign in** if you already have one).  
2. Use an email you control and a strong root password.  
3. Complete the phone check and payment method AWS asks for (free-tier usage still usually needs a card).  
4. Choose a support plan (Basic is enough for learning).

Official: [Create and activate an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)

| First piece | AWS name |
|-------------|----------|
| Hard box | **AWS account** |
| All-powerful login | **Root user** (account email) |
| Console | [AWS Management Console](https://console.aws.amazon.com/) |

## First console login

1. Sign in at the **[AWS Management Console](https://console.aws.amazon.com/)** as root (email + password) the first time.  
2. Confirm the **account ID** / alias in the top bar — that is your box.  
3. Pick a home region you will use often (for example `ap-south-1`); you can change it later.  
4. Open **Billing** once and confirm the account is active.

Stay in this **one account** for learning. Do not build a full **Organization** tree on day one.

## Day-one security

1. Enable **MFA** on the root user.  
2. Create an **IAM user** (or use **IAM Identity Center** later) with admin rights for daily work.  
3. Stop using the root user for everyday tasks.  
4. Optional: set a billing alarm so surprise usage is visible.

Deeper IAM is covered in M2. Company tree (**Organization**, OUs, member accounts) is in [2.1 Accounts & Organizations](./1010_accounts_organizations.md).

## What to do next

- Practice finding EC2, S3, and IAM in the console.  
- Keep one lab account; add Organizations only when you need many accounts.  
- Then continue to Azure / GCP first login, or jump to regions.

## Where this sits in the syllabus

<br/>
<p>
    <span style="float: left;">
        <a href="../../docs/1015_first_login_and_setup.md">Previous: Registration</a>
        &nbsp;
        <a href="../../azure/docs/1015_first_login_setup.md">Next: Azure Registration</a>
    </span>
    <span style="float: right;">
        <a href="../../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="../../README.md">Cloud</a>
        &nbsp;|&nbsp;
        <a href="../../docs/1015_first_login_and_setup.md">Topic: First login & setup</a>
    </span>
</p>
