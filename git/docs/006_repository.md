# 📦 Git Repository

A Git repository is your project directory with additional metadata that Git uses to manage version control.

The repository contains all information about your project, including version history, branches, remote server details, and configurations. Everything you need is stored within the repository itself.

> [!NOTE]
> Some global configurations and authentication tokens may be stored outside the repository in your system's Git configuration files.

```mermaid
graph TD
    A[my-project/] --> B[.git/]
    A --> C[src/]
    A --> D[README.md]
    A --> E[.gitignore]
    
    B --> F[objects/]
    B --> G[refs/]
    B --> H[HEAD]
    B --> I[config]
    B --> J[index]
    
    C --> K[main.js]
    C --> L[utils.js]
    
    G --> M[heads/]
    G --> N[remotes/]
    
    M --> O[main]
    M --> P[feature-branch]
    
    N --> Q[origin/]
    Q --> R[main]
    
    style B fill:#ffe1e1
    style F fill:#e1f5ff
    style G fill:#e1ffe1
```

**Fig:** Sample Git repository folder structure

## Repository Structure

- **`.git/`** - The core Git directory containing all version control metadata. This hidden folder stores everything Git needs to track your project's history.

    - **`.git/objects/`** - The object _database_ where Git stores all file contents of project commit history.

    - **`.git/refs/`** - Contains pointers to branches and tags. Organized into subdirectories for **local branches and remote tracking branches**.

        - **`.git/refs/heads/`** - Stores references to local branch heads. Each file represents a branch and contains the SHA-1 hash of the commit at the branch tip.

        - **`.git/refs/remotes/`** - Contains references to remote branches. Typically organized by remote name (e.g., `origin/`), tracking the state of branches on remote repositories.

    - **`.git/HEAD`** - A special pointer indicating the current branch or commit you're working on. Usually points to a reference in `refs/heads/`.

    - **`.git/config`** - Repository-specific configuration file containing settings like remote URLs, branch tracking information, and user preferences for this repository.

    - **`.git/index`** - The staging area (also called the index) that holds information about files staged for the next commit. Acts as a snapshot of what will be committed.

- **`.gitignore`** - Specifies files and directories that Git should ignore and not track in version control.

- **`README.md`** - Project documentation file (part of your working directory).

- **`src/`** - Your project's source code directory. **This is not Git-specific;** the folder name src is just an example and can be any name you choose for organizing your project related directories and files.


# 🔰 Repository Creation

To create a Git repository, you need to:
- Select a Git server and set up your account
- Choose and install a Git client tool

If needed, refer back to the [Server | Client Page](./004_server_clients.md) for more details.

To collaboratively use Git from different remote locations, you need a Git repository that is accessible remotely. **GitHub** is one such server that provides Git repository hosting services. You can easily create a free GitHub account and host your remote Git repositories at no cost.

```mermaid
graph LR
    subgraph "Development Team"
        C1[👤 Developer 1<br/>Local Repo]
        C2[👤 Developer 2<br/>Local Repo]
        C3[👤 Developer 3<br/>Local Repo]
    end
    
    subgraph "Remote Git Servers"
        subgraph "GitHub"
            GH1[📦 Repo A<br/>Shared Code]
        end
        
        subgraph "GitLab"
            GL1[📦 Repo A<br/>Shared Code]
        end
        
        subgraph "Bitbucket"
            BB1[📦 Repo A<br/>Shared Code]
        end
    end
    
    C1 <-->|push/pull| GH1
    C2 <-->|push/pull| GL1
    C3 <-->|push/pull| BB1
    
    GH1 <-.->|sync| GL1
    GL1 <-.->|sync| BB1
    BB1 <-.->|sync| GH1
    
    style C1 fill:#e1f5ff,stroke:#0366d6,stroke-width:2px
    style C2 fill:#e1f5ff,stroke:#0366d6,stroke-width:2px
    style C3 fill:#e1f5ff,stroke:#0366d6,stroke-width:2px
    style GH1 fill:#fff5e1,stroke:#f9826c,stroke-width:2px
    style GL1 fill:#fff5e1,stroke:#fc6d26,stroke-width:2px
    style BB1 fill:#fff5e1,stroke:#fc6d26,stroke-width:2px
```

**Fig:** Git multiple clients configured to access multiple remote servers.

> [!TIP]
> Normally only one Git remote server is required. In the diagram above I intentionally included three remote servers from different providers to demonstrate that this is possible.

## Configure Git Server account and repository (using GitHub)

Below are the steps:
1. go to https://github.com/

2. Signup as given below
<div style="text-align: center;">
 <img src="../static/repository/signup.png" width="30%">
</div>
3. Finish the verifications.

It will redirect to below dashboard https://github.com/dashboard:

<div style="text-align: center;">
 <img src="../static/repository/launch.png" width="100%">
</div>

4. In Top-left corner there have 2 options:
    - **Create Repository:** Allows you to create new repository.
    - **Import Repository:** Allows you to import other github repository and create new one using imported repository.

5. Choose create Repository
    - Add a test repository for understanding the flow
    <div style="text-align: center;">
        <img src="../static/repository/testrepo.png" width="100%">
    </div>

6. Click on **Create Repository** button and it will create repository in remote server of github. You can interact using the webpages as given below:

<div style="text-align: center;">
 <img src="../static/repository/testrepo_landing.png" width="100%">
</div>

**Now you have to connect with this remote server repository using a Git client**

# Configure Git Client and Connect to Your Repository

### Step 1: Install Git Client

Download and install Git from [git-scm.com/install/](https://git-scm.com/install/).

**Prefer a graphical interface?** Check out [Git GUI tools](https://git-scm.com/tools/guis) for alternatives.

### Step 2: Open a Terminal

**On Linux:** Use your system bash directly to run Git commands.

**On Windows:** Use **Git Bash**, which is installed automatically with git-scm.

### Step 3: Navigate to Your Desired Directory

Move to the directory where you want to clone the repository:

```bash
cd /path/to/your/directory
```

### Step 4: Clone the Repository

Clone your remote repository using the `git clone` command:

```bash
git clone REPOSITORY_URL
```

**Where do I find `REPOSITORY_URL`?** Copy it from your remote repository page:

<div style="text-align: center;">
 <img src="../static/repository/repo_url.png" width="70%">
</div>

### Step 5: Explore Your Repository Structure

Navigate to the newly created folder and view its structure:

```bash
cd repository-name
```

You should see the `.git/` directory and other project files. To view hidden files (including `.git/`), enable the "show hidden files" option in your file explorer.

> [!NOTE]
> **You have successfully completed the following:**
> 
> 1. Created a remote repository on GitHub
> 2. Cloned the remote repository to your local machine, creating a local copy
> 3. Established a connection between your local and remote repositories for future synchronization

### How to see your git Client-Server connection config ?
Open your `./.git/config` file

You can see the configuration as given below:
```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/USER_NAME/REPO_NAME.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

Note the `[remote "origin"]` section.
