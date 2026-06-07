# 🔁 Git Server vs Git Client

> [!NOTE]
> - A **Git client** is any machine or software environment where Git is installed and used to **interact with repositories**.
> - A **Git server** is a machine or service that **hosts Git** repositories and allows **other machines (Git clients) to interact with them**.

<p align="center">
  <img src="./../static/server_clients/server_clients.svg" alt="Alt Text" width="35%"/>
</p>

**Fig:** Git Server - Git Glient interaction

As shown in the figure above, the **Git Server** is configured to **host a Git repository**.
The repository, referred to as `REPO`, contains all essential project data, including: `Full commit history, Branch-related information and Configuration files and metadata`
This repository is shared across all connected servers and clients.
All users can work with the **local repository** on their local client **independently**, to the server.

### 🧩 How Does a Git Client Work Independently from the Server?

- When you **clone** a repository, the Git server gives you the **entire copy**, including all version history.
  - This means you **don’t need to contact the server** to view or go back to earlier versions.

- When you run `git commit`, it **does not send changes to the server**. Instead:
  - It creates a **new version** (called a *snapshot*) of your project.
  - These snapshots are saved in your **local repository**.
  - So, you can **commit changes without being connected** to the server.

- Git supports **multiple branches** in a repository, and all of them are copied when you clone.
  - This lets you **switch between branches locally**, without needing the server.

> [!NOTE]
> Even though a **Git client** works independently from the server, keep these points in mind:
>
> 1. After cloning a repository, if new changes are added to the server, the client **won’t be notified automatically**.  
>    You must run `git fetch` or `git pull` to get those updates.
>
> 2. When you commit changes on the client, they are saved locally.  
>    The server **won’t know about them** until you run `git push` to send your changes.
>
> 3. If both the client and server modify the same file, you may face a **merge conflict**.  
>    The longer you wait to push your changes, the higher the chance someone else has edited the same file—leading to more conflicts during merging.

> [!TIP]
> A **Git server typically doesn't make changes by itself** (i.e., no one usually works directly on the server).  
> Most updates come from **changes made by clients**, which are later pushed and merged into the server repository.

## 🗄️Common **Git Servers** available in market

Below are the main Git server products available in the market:

**GitHub** - A cloud-based Git hosting service owned by Microsoft, offering free public repositories, collaboration tools, CI/CD pipelines, and a large open-source community.  **I personally prefer to use this.**

**GitLab** - A complete DevOps platform with built-in CI/CD, issue tracking, and container registry. Available as both cloud-hosted and self-hosted options.

**Bitbucket** - A Git repository management solution by Atlassian, integrating seamlessly with Jira and other Atlassian tools. Offers both cloud and self-hosted deployments.

**Azure DevOps** - Microsoft's comprehensive DevOps platform with Git repositories, pipelines, boards, and artifacts. Strong integration with Azure cloud services.

**Gitea** - A lightweight, open-source, self-hosted Git service written in Go. Easy to install and resource-efficient for small teams.

**GitBucket** - A Git platform powered by Scala, easily deployable on JVM. Provides GitHub-like features for self-hosted environments.


# 🖥️ Git Clients List

Below are the main Git Client products available in the market:

### 🖊️ Command Line
- **Git CLI using git-scm** (Windows, macOS, Linux) – The official command-line client, most powerful and flexible. **I personally prefer to use this.**

### 🌱 Beginner-Friendly
- **GitHub Desktop** (Windows, macOS) – Free, simple UI, integrates with GitHub.
- **SourceTree** (Windows, macOS) – Free, Atlassian’s GUI, good for Bitbucket/GitHub.
- **TortoiseGit** (Windows) – Free, integrates into Windows Explorer.

### ⚙️ Cross-Platform GUIs
- **GitKraken** (Windows, macOS, Linux) – Modern UI, visualization of branches, free & paid versions.
- **SmartGit** (Windows, macOS, Linux) – Professional-grade, supports Git, SVN, Mercurial.
- **Tower** (Windows, macOS) – Paid, polished interface, popular among teams.

### 🧑‍💻 Developer-Oriented
- **Git Extensions** (Windows) – Free, integrates with Visual Studio and VS Code.
- **Magit** (Emacs plugin, cross-platform) – Text-based, extremely powerful for advanced users.
- **MeGit (EGit)** (Windows, macOS, Linux) – Based on Eclipse Git integration.