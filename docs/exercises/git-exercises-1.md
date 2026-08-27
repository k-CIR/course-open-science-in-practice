# Git basics

- Format: Workshop
- Teacher: Andreas

In this hands-on session you will learn the **local, single-track workflow** of Git: how to create a project, turn it into a repository, write a small analysis script, and record your work as a series of commits. We deliberately **skip branches and remotes** (GitHub, GitLab, pushing) in this session — those come later. Everything you do in this session stays on your own machine.

By the end of the workshop you should be able to:

- [ ] Initialise a Git repository and check status
- [ ] Use the core edit → stage → commit cycle with confidence
- [ ] Explain the difference between the working directory, the staging area, and the repository
- [ ] Read back your history and inspect what changed between versions
- [ ] Write and run a small test alongside your script, and version it with Git

We will work inside Positron and use the built in terminal but you could run all commands in the terminal of your choosing.

## Create a new project

1. Open the Positron app. If an recent session opens up, click `File` → `Open New Window`
2. Click `New folder` → `Empty Project` and select where you want to store your project. Leave `Initialize Git repository` unchecked for now
3. Select `TERMINAL` in the tab section

??? tip "Check your location"
    You see your username and the current folder name. To see full location run `pwd` and to list all files in the folder run `ls`. There should be no files yet.


Now let's turn the folder into a Git repository:

```sh
git init
```

`git init` creates the hidden `.git` directory — the database that stores your entire history. You never edit inside it by hand. Run `ls -a` to list all content including hidden, you should see a `.git` folder

!!! tip "Check your git location"
    Run `git status` right after `git init`. Git replies with `On branch main` (or `master`) and `No commits yet`. That confirms you are inside a fresh repository.

## Configure Git once per machine

Before your first commit, tell Git who you are. This information is written into every commit so the history can show who did what.

```sh
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

Use the same email you will later use for GitHub so your commits are attributed correctly. The `--global` flag saves this for every repository on your machine; omit it to set it only for the current project.

??? note "Already configured?"
    See your current settings with `git config --list` or just `git config user.name`.

## Create your first script :material-file-plus:

We will build a tiny analysis script. Choose **R** or **Python** — both tracks are equivalent for the Git lessons. The script should do something small but real: read a couple of numbers, compute a summary, and print it.

=== "R (analysis.R)"

    ```r
    # analysis.R
    # A tiny descriptive-stats script used to practise Git.

    values <- c(4, 8, 15, 16, 23, 42)

    mean_value <- mean(values)
    max_value  <- max(values)

    cat(sprintf("Mean: %.2f\n", mean_value))
    cat(sprintf("Max:  %d\n",   max_value))
    ```

=== "Python (analysis.py)"

    ```python
    # analysis.py
    # A tiny descriptive-stats script used to practise Git.

    values = [4, 8, 15, 16, 23, 42]

    mean_value = sum(values) / len(values)
    max_value = max(values)

    print(f"Mean: {mean_value:.2f}")
    print(f"Max:  {max_value}")
    ```

Run it to confirm it works:

=== "R"

    ```sh
    Rscript analysis.R
    ```

=== "Python"

    ```sh
    python analysis.py
    ```

Both should print a mean around `18.00` and a max of `42`.

## The core cycle: status, add, commit

Git does **not** record your files automatically. You decide what becomes part of history in three steps.

### 1. See what changed — `git status`

```sh
git status
```

Right now Git tells you `analysis.R` (or `analysis.py`) is **untracked** — Git sees the new file but is not yet recording it.

### 2. Stage changes — `git add`

Staging is the act of selecting *exactly* what the next commit should contain.

```sh
# Stage a single file
git add analysis.R
```

??? top "Useful `git add` arguments:"

    | Command | What it does |
    | --- | --- |
    | `git add <file>` | Stage one specific file |
    | `git add .` | Stage all changes in the current folder and below |
    | `git add -A` | Stage all changes anywhere in the repo (new, modified, deleted) |
    | `git add -p` | Stage changes **hunk by hunk**, so you can split edits into separate commits |

After staging, run `git status` again — the file now appears under *Changes to be committed*.

### 3. Record a snapshot — `git commit`

```sh
git commit -m "Add first descriptive-stats script"
```

The `-m` flag lets you write the commit message directly. Write messages in the **imperative mood** describing what the commit *does* (e.g. "Add…", "Fix…", "Remove…").

??? tip "Useful `git commit` arguments:"

    | Command | What it does |
    | --- | --- |
    | `git commit -m "msg"` | Commit staged changes with a message |
    | `git commit -a -m "msg"` | Auto-stage modified/deleted tracked files, then commit (skips `git add` for already-tracked files) |

??? warning "What happens if you don't add a commit message?"
    An (annoying) terminal editor (vim) opens and you will be forced to add something.

    You can change the default editor with `git config --global core.editor <editor>`

    If you quit the editor changes are not committed.
    `Aborting commit due to empty commit message.` 

## Exercise 1 — Make a change and commit it

1. Edit your script so it also reports the **minimum** value.
2. Run the script and confirm the new output is correct.
3. Stage and commit the change:

   ```sh
   git add analysis.R
   git commit -m "Report minimum value in summary"
   ```

Confirm there are now two commits (see next section).

## Reading back your history

```sh
git log
```

Shows every commit in reverse chronological order, with its hash, author, date, and message.

??? tip "Helpful `git log` arguments:"

    | Command | What it shows |
    | --- | --- |
    | `git log --oneline` | One compact line per commit (short hash + message) |
    | `git log -n 3` | Only the last 3 commits |
    | `git log --stat` | Which files changed in each commit |
    | `git log -p` | The full diff (line-by-line changes) of each commit |

### `git diff` — what changed but is not yet staged

1. Add some random values to the vector/list
2. run `git diff` to see unstaged changes

Compares your working directory against the staging area. 

??? tip "Useful `git diff` arguments:"
    | Command | What it compares |
    | --- | --- |
    | `git diff` | Working directory ↔ staging area |
    | `git diff --staged` | Staging area ↔ last commit (what you are about to commit) |
    | `git diff HEAD~1` | Working directory ↔ the previous commit |
    | `git diff <hash1> <hash2>` | Two specific commits |

### `git show` — inspect one commit

```sh
git show
```

Shows the most recent commit's metadata and its diff. Add a commit hash to inspect any specific commit:

```sh
git show <commit-hash>
```

## Exercise 2 — Inspect your work

1. Run `git log --oneline` and confirm you see both commits.
2. Run `git diff HEAD~1` to see what the latest commit changed compared with the one before it.
3. Run `git show HEAD~1` to read the full content of your first commit.

## Exercise 3 — Break it on purpose (then fix it)

1. In your script, change the computation of the mean so it is wrong (for example, divide by `length(values) - 1` in R, or forget to divide in Python).
2. Re-run the tests. They should **fail** — this proves the tests actually guard your logic.
3. Fix the script so the tests pass again.
4. Stage and commit:

   ```sh
   git add analysis.R            # or analysis.py
   git commit -m "Fix mean calculation and restore tests"
   ```

This edit → test → commit loop is the everyday rhythm of version-controlled, reproducible analysis.

## Recap of the commands you learned

| Command | Purpose |
| --- | --- |
| `git init` | Create a repository in the current folder |
| `git config --global user.name/email` | Set your identity (once per machine) |
| `git status` | Show untracked, staged, and unstaged changes |
| `git add <file>` / `.` / `-A` / `-p` | Stage changes for the next commit |
| `git commit -m "msg"` | Save a snapshot with a message |
| `git log` / `--oneline` / `-p` | Browse history |
| `git diff` / `--staged` | Inspect changes before/after staging |
| `git show <hash>` | View one commit in detail |

!!! success "What you can now do"
    You can start a project, write an R or Python script, back it up as meaningful commits, check your history, and protect it with automated tests — all locally, with no branches or remotes involved.

## What we deliberately skipped

Branches (`git branch`, `git switch`), remotes (`git remote`, `git push`, `git pull`), and pull requests are **out of scope for this session**. They build directly on what you learned here, so the next workshop will pick up exactly where this one ends.

