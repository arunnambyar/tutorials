# ❓What is Git?

Git is a version control system.

## 🛠️ What is a Version Control System?

A **Version Control System (VCS)** is a software tool that helps developers manage changes to their project over time.

## 🔧 Why a Version Control System is Required?

When working on a project—especially as a team—files are constantly being added, modified, or deleted. Without a system to manage these changes, things can quickly become messy and confusing.

A Version Control System (VCS) helps solve common problems like:

### 1. Need of a shared place (like a server) where all your/teams project files and changes are saved.
```mermaid
graph TB
    r[Repository] <-- Push/Pull data --> u1((User1))
    r <-- Push/Pull data --> u2((User2))
    r <-- Push/Pull data --> u3((User2))

    classDef green fill:#9f6,stroke:#333,stroke-width:2px,color:#000;
    classDef orange fill:#f96,stroke:#333,stroke-width:4px,color:#000;

    class r green
    class u1,u2,u3 orange
```

### 2. Multiple people working on the same project without overwriting each other's work
<p align="left">
    <img src="../static/what/multiple-people.png" width=25% height=25%>
</p>

### 3. Merging changes from different team members safely and efficiently
```mermaid
flowchart LR
    u1(("User1")) -.- r1["File: a.py"]
    u2(("User2")) -.- r2["File: a.py"]
    r1 & r2 --> r3["Merged File: a.py"]

    style u1 fill:#FFCDD2,color:#000
    style r1 fill:#FFD600,color:#000
    style u2 fill:#FFCDD2,color:#000
    style r2 fill:#FFF9C4,color:#000
    style r3 fill:#FF6D00,color:#000
```

### 4. Tracking who changed what, when, and why—keeping a full history (or versions) of edits
```mermaid
%%{init:{ "gitGraph":{ "mainBranchName":"LATEST" }}}%%
    gitGraph
        checkout LATEST
        commit id: "v1000, BY: USER1"
        commit id: "v999, BY: USER2" tag: "v1.0.0"
        commit id: "v998, BY: USER2"
        commit id: "v997, BY: USER1" type: REVERSE tag: "RC_1"
        commit id: "v996, BY: USER1"
        commit id: "v995, BY: USER1" type: HIGHLIGHT tag: "8.8.4"
        commit id: "v994, BY: USER2"
```
### 5.  Going back to any of the previous versions of the project
```mermaid
flowchart RL
    v0(("V-0")) -..-> v7(("V-997"))
    v7 ---> v8(("V-998"))
    v8 ---> v9(("V-999"))
    v9 ---> v10(("V-1000<br>LATEST"))
    v10 -- RESETTING VERSION --> v8

    style v0 stroke-width:4px,stroke-dasharray: 5
    style v10 fill:#2962FF,color:#FFFFFF
    linkStyle 4 stroke:#D50000,fill:none
```

### 6.  Recovering deleted files or reverting to earlier versions when needed

```mermaid
flowchart RL
    v0(("V-0")) -..-> v7(("V-997"))
    v7 ---> v8(("V-998"))
    v8 ---> v9(("V-999"))
    v9 ---> v10(("V-1000<br>LATEST"))
    v10 -- Step.1: GOING BACK TO OLD VERSION --> v8
    v8 -- Step.2: GET DELETED/MODIFIED OLD FILE FROM OLD VERSION --> v10

    style v0 stroke-width:4px,stroke-dasharray: 5
    style v10 fill:#2962FF,color:#FFFFFF
    linkStyle 4 stroke:#D50000,fill:none
    linkStyle 5 stroke:#00D500,fill:none

    L_v10_v8_0@{ animation: slow }
    L_v8_v10_0@{ animation: slow }
```


### 7. Creating and working with isolated branches without affecting each other
```mermaid
%%{init: { "gitGraph": { "mainBranchName": "MASTER" } }}%%
gitGraph
    checkout MASTER
    commit
    commit
    commit
    branch FEATURE1
    checkout FEATURE1
    commit
    commit
    checkout MASTER
    commit
    commit
    commit
    commit
    checkout FEATURE1
    commit
    commit
    commit
```

## 🧭 Centralized vs Distributed VCS

A **Centralized VCS** stores all project history in a single central server. Developers connect to this server to get the latest version and to save their changes.

A **Distributed VCS** (like Git) gives every developer a full copy of the entire repository—including its history. This means each user's machine acts like a mini-server, allowing work even without internet access.

Earlier, only centralized systems were common. But today, distributed systems are more popular because they offer better speed, flexibility, and offline access.

> _In short: centralized VCS relies on one hub, while distributed VCS gives everyone a complete copy._

See details [Here](./compare.md)