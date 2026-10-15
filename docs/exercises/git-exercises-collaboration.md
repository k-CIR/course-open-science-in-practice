# Git collaboration

In this hands-on session you will close the circle and practice the collaboration process, by cloning, forking, merging and making pull requests.

You will pair up with a **code buddy** and contribute to *each other's* mini-project repository: forking, branching, pushing, and opening a pull request against a real, live repository instead of your own. By the end you should be able to:

- [ ] Clone a repository and confirm the remote it inherited
- [ ] Fork a repository and add the original as a second (`upstream`) remote
- [ ] Explain the difference between `fetch`, `pull`, and `clone`
- [ ] Push a branch and open a pull request
- [ ] Recover from a rejected push when the remote has moved on
- [ ] Merge a pull request and sync the result back to your own machine

## Prerequisites

- A GitHub account with SSH configured (Workshop #2).
- Your own mini-project repository already pushed to GitHub, with at least one commit.
- A **code buddy** — pair up with someone else in the room. You will fork their repository and they will fork yours.

??? task "Exercise 4.1 — Clone and inspect the inherited remote"

    Before forking anything, confirm what cloning actually sets up for you.

    Clone any public repository you do not own, for example the course example repo:

    ```sh
    git clone https://github.com/NiklasEdvall/an-approved-repo.git
    cd an-approved-repo
    ```

    **1.** Inspect the remote that was created for you automatically. What is the remote?

    **2.** How many branches does the repository have?

    **3.** Inspect the commit history, what do you see?

    **4.** When was the first commit?

    ??? help "Help"

        Check remote(s): `git remote -v`

        A single remote named `origin`, pointing at the URL you cloned — both for fetch and for push, even if you do not actually have push access to it. `git clone` always wires up `origin`; whether you can push there is a separate question, decided by the remote's permissions, not by Git.

        Check branches: `git branch`

        Check commit log: `git log --oneline --graph`

        Check from beginning: `git log --reverse`

    Compare this to starting from scratch: `git init` followed by `git remote add origin <url>` — the same end state, reached in two explicit steps instead of one.



??? task "Exercise 4.2 — Fork your buddy's repository"

    **1.** On GitHub, open your code buddy's mini-project repository and click **Fork**. This creates a copy under *your* account (`you/their-repo`).

    **2.** Clone **your fork** — not their original — to your machine:

    ```sh
    git clone git@github.com:you/their-repo.git
    cd their-repo
    git remote -v
    ```

    **3.** Confirm `origin` points at your fork, then add their original repository as a second remote:

    ```sh
    git remote add upstream git@github.com:buddy/their-repo.git
    git remote -v
    ```

    You should now see two remotes: `origin` (your fork, read/write) and `upstream` (their original, read-only for you).

??? task "Exercise 4.3 — `fetch` vs. `pull`"

    **1.** Ask your buddy to make a small commit directly to their repository (e.g. add a line to their README) and push it.

    **2.** On your machine, download it *without* touching your files:

    ```sh
    git fetch upstream
    git log main..upstream/main --oneline
    ```
    What do you see?

    Try also `git log --oneline`

    Your working directory and `main` are unchanged — only `upstream/main` moved.

    **3.** Now actually bring it in:

    ```sh
    git merge upstream/main
    ```

    or, equivalently in one step next time: `git pull upstream main`.

    ??? question "So what did `git pull` actually do?"
        `git pull upstream main` is shorthand for `git fetch upstream` followed by `git merge upstream/main`. Using `fetch` first (as in step 2) lets you inspect incoming changes before merging; `pull` does both at once, which is faster but skips the inspection step.

??? task "Exercise 4.4 — Create a local branch from a remote branch"

    **1.** Run the following commands and explain what you think they are doing

    ```sh
    git branch -r
    git switch --track -c inspect-upstream upstream/main
    git status
    git branch -vv
    ```

    ??? help "Help"
        ```sh
        git branch -r                                  # List remote-tracking branches available locally
        git switch --track -c inspect-upstream upstream/main  # Create and switch to a local branch tracking upstream/main
        git status                                     # Show the current branch and working-tree status
        git branch -vv                                 # List local branches, their latest commits, and tracking status
        ```

    **2.** Which branch is checked out now?

    **3.** Make a change to .gitignore eg. add `.DS_Store`, stage and commit your changes and `git push upstream HEAD:main`. What happens?

    ??? help "Help"
        Your don't have write access to upstream branch.
        `upstream/main` is updated by `git fetch upstream`; `inspect-upstream` is a local branch you can switch to and work on. It is set to track `upstream/main`. In this exercise, switch back to `main` before making or pushing contribution commits, because `upstream` is the buddy's repository and is read-only for you.

    **4.** Switch back to your own `main` branch and merge the changes in inspect-upstream:

    ```sh
    git switch main
    git merge inspect-upstream
    ```

??? task "Exercise 4.5 — Contribute a change via pull request"

    **1.** Create a branch for your contribution:

    ```sh
    git switch -c add-my-name
    ```

    **2.** Make a small, safe change — for example add your name to a `CONTRIBUTORS.md` file, or fix an obvious typo in their README. Commit it.

    **3.** Push the branch to **your fork** (`origin`, not `upstream` — you have no write access there):

    ```sh
    git push -u origin add-my-name  # Push the local add-my-name branch to origin and set it as its upstream
    ```

    **4.** On GitHub, open your fork. You should see a prompt to open a pull request. Open one **targeting your buddy's repository**, with a short, clear title and description of what the change does and why.

    !!! info "Where does a fork's pull request go?"
        Even though your branch lives on `origin` (your fork), the pull request targets `upstream` (their repository) — GitHub remembers the fork relationship and offers this automatically.

??? task "Exercise 4.6 — Handle a rejected push"

    Simulate the most common collaboration hiccup (or if you have worked on two different machines): pushing when the remote has moved on without you.

    **1.** Make a new commit locally on `main`, but do **not** push it yet.

    **2.** Edit a the file directly on GitHub's web interface, which creates a commit on `origin/main` you do not have locally.

    **3.** Try to push. What happens?

    ??? help "Help"
        ```sh
        git push origin main
        ```

        Git refuses:

        ```text
        ! [rejected]        main -> main (fetch first)
        error: failed to push some refs
        ```

    4. Recover exactly as the error suggests:

       ```sh
       git pull origin main
       # resolve any conflicts, same as in the branching workshop
       git push origin main
       ```

    ??? tip "Why does Git refuse instead of overwriting?"
        A plain push can only **fast-forward** the remote. If the remote has commits you do not have, pushing anyway would silently erase them from the branch. Git refuses and asks you to integrate those commits first — the same protective instinct behind merge conflicts.

??? task "Exercise 4.7 — Review and merge the pull request"

    Swap roles: review the pull request your buddy opened against **your** repository.

    **1.** On GitHub, open the pull request in your repository. Read the diff, leave at least one review comment.

    **2.** If it looks good, click **Merge pull request**.

    **3.** Delete the now-merged branch (GitHub offers a button; or from the command line: `git push origin --delete <branch-name>`).

    **4.** Both of you should now pull the merged result down locally:

    ```sh
    git switch main
    git pull origin main
    ```

    !!! info "Merging on GitHub only changes the remote"
        Clicking **Merge** updates `main` on GitHub — it does **not** touch anyone's local `main` automatically. Everyone, including whoever opened the PR, still needs to `git pull` to see the merged result on their own machine.

## Recap of the commands you learned

| Command | Purpose |
| --- | --- |
| `git clone <url>` | Copy a repository and automatically create `origin` |
| `git remote add upstream <url>` | Register a second remote, e.g. the project you forked from |
| `git fetch <remote>` | Download new commits without touching your branches or files |
| `git branch -r` | List remote-tracking branches |
| `git switch --track -c <local> <remote>/<branch>` | Create a local branch that tracks a remote branch |
| `git pull <remote> <branch>` | `fetch` + `merge` in one step |
| `git push -u origin <branch>` | Push a new branch and set it to track the remote |
| `git push origin --delete <branch>` | Delete a branch on the remote after it is merged |

!!! success "What you can now do"
    You can clone and fork a repository, keep a fork in sync with `upstream`, push a branch and open a pull request against a repository you do not own, recover from a rejected push, and merge — and correctly sync — a reviewed contribution.

## What comes next

Your mini-project should end up with at least one branch and merge of its own — this is exactly the collaboration opportunity described in [your project requirements](../project/project-description.md). Use the independent work time this afternoon to keep building your pipeline, and feel free to open a small pull request against your buddy's project again if you want more practice before the examination seminar.
