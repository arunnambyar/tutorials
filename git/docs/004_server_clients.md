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

> 3. If both the client and server modify the same file, you may face a **merge conflict**.  
>    The longer you wait to push your changes, the higher the chance someone else has edited the same file—leading to more conflicts during merging.

> [!TIP]
> A **Git server typically doesn't make changes by itself** (i.e., no one usually works directly on the server).  
> Most updates come from **changes made by clients**, which are later pushed and merged into the server repository.