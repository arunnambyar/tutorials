# 🗄️ Architecture of Git
![](../static/core/git_architecture.svg)

**Fig:** Architecture diagram of different components of Git

The above diagram shows a high level architectural diagram of git client. There is no much difference between Git Client and Server. Only difference is that, Git server additionally configured to work as a server.

It contains following components:
 1. **Commands:** This component responsible for interpreting the user commands (for eg, git pull, git push, etc).

 2. **Transport:** This component facilitates communication between the `client and the server`.
    - The client is the machine initiating operations like fetching or pushing changes, while the server is the remote repository that receives and processes these requests.
    - Git’s transport module supports multiple protocols, including ssh://, https://, git://, and file://, to handle the requests.
    - A standard Git installation typically includes only the client-side tools, which allow interaction with remote servers such as GitHub, GitLab, Bitbucket, or in-house configured Git servers.
    - That means, other users (from other machines) cannot push changes to your local repository or pull updates from it unless you explicitly configure it to act as a server.
    - However, Git does allow you to configure a repository with server capabilities. Once set up, others can:
        - Clone your repository
        - Fetch updates
        - Push their changes to your repository

 3. **Objects Refs History:** This is a core internal module in Git that manage `file storage, version history, and branch tracking`.
 
 4. **Index:** The `index` is Git’s `staging area`—a middle layer between your `working directory` and the `repository`.
    - You can safely move your current changes in `working directory` to `Index` before moving them into `repository`
    - Also, you can remove contents from `index` if required
    - When you are doing a commit, what ever files/dirs available in `index` are actually moved to `repository`
    - Contents in `index` are managed by an index file
    - All operations relared to Index is managed by `Index module`

> [!TIP]
> In addition to these main components, `working directory`, is where you are working. All projects related ccontents are placed there.<br/>
Also, a `config management` manages all configurations of the Git.

We will cover all those sessions in later portion of the tutorial.