# Git safety

- Format: Workshop
- Teacher: Andreas

In this hands-on session you will connect your local repository to a **remote** on GitHub, and learn the safety practices that keep you from sharing things you did not mean to: `.gitignore`, handling secrets, and SSH keys.

Everything you did in the previous sessions stayed on your own machine. A remote is another copy of your repository, usually hosted (here: GitHub), that lets you back up your work and collaborate. With that power comes risk: it is easy to accidentally publish data files, credentials, or large outputs. This workshop focuses on doing remotes **safely**.

By the end of the workshop you should be able to:

- Explain what a remote is and add one with `git remote`
- Push your local history to GitHub and clone a repository
- Write a `.gitignore` so unwanted files never get committed
- Keep secrets (API keys, tokens, passwords) out of Git


## Prerequisites

Make sure to have setup your GitHub account and 

## What is a remote?

A **remote** is simply a reference (a URL) to another repository. Git stores it under a short name — by convention the primary remote is called `origin`. Adding a remote does not copy anything yet; it just tells Git *where* `origin` points.

```sh
# After creating an empty repo on GitHub, link it to your local repo
git remote add origin git@github.com:your-user/your-repo.git

# List your remotes and their URLs
git remote -v
```

| Command | What it does |
| --- | --- |
| `git remote -v` | Show remotes and their fetch/push URLs |
| `git remote add <name> <url>` | Register a new remote |
| `git remote set-url <name> <url>` | Change a remote's URL (e.g. switch to SSH) |
| `git remote rename <old> <new>` | Rename a remote |
| `git remote remove <name>` | Delete a remote reference |

## Push and clone

```sh
# Send your local main branch (and its history) to origin
git push -u origin main
```

The `-u` (set-upstream) flag links your local `main` to `origin/main`, so later you can just run `git push` / `git pull`.

To get a copy of an existing repository (for example a course template):

```sh
git clone git@github.com:some-user/some-repo.git
```

`git clone` automatically sets `origin` for you and checks out the default branch.

!!! warning "Push only what you intend to share"
    Once something is pushed to a public remote, assume it is public forever. This is why `.gitignore` and secret-handling (below) matter *before* your first push.

## `.gitignore` — keep junk and secrets out

A `.gitignore` file lists patterns for files Git should **never track**. It belongs in the root of your repository and is committed like any other file, so everyone collaborating on the project shares the same rules.

Create `.gitignore`:

```sh
touch .gitignore
```

A good starter for a data-science project:

```text
# OS noise
.DS_Store
Thumbs.db

# Editor / IDE
.Rproj.user/
.Rhistory
.venv/
__pycache__/
*.swp

# Outputs that can be regenerated
/output/
/results/
*.csv
*.png

# Secrets — NEVER commit these
.env
*.key
credentials.json
```

Lines starting with `#` are comments. A leading `/` anchors the pattern to the repository root; `*` is a wildcard.

Useful ignore commands:

| Command | What it does |
| --- | --- |
| `git status` | Shows ignored files only if you ask (see below) |
| `git check-ignore -v <file>` | Explains *why* a file is ignored (which rule matched) |
| `git add -f <file>` | Force-add a file even if it matches an ignore rule |
| `git status --ignored` | List both tracked and ignored files |

Commit your `.gitignore` so the rules travel with the project:

```sh
git add .gitignore
git commit -m "Add .gitignore for outputs, OS noise, and secrets"
```

## Exercise 1 — Ignore the right things

1. In your project, create a file you do **not** want tracked, e.g. `notes.txt` containing scratch thoughts, or `draft.png` as a throwaway plot.
2. Add a rule to `.gitignore` for it (e.g. `notes.txt` or `*.png`).
3. Confirm Git agrees:

   ```sh
   git check-ignore -v notes.txt
   git status --ignored
   ```

4. Confirm it does **not** appear under "Changes not staged for commit".
5. Commit your updated `.gitignore`.

## Secrets: never commit credentials

API keys, tokens, passwords, and private keys must never enter Git — not even "temporarily", and not even if you later delete them, because the data stays in history.

- Store secrets in a file outside version control, e.g. `.env`, and add `.env` to `.gitignore`.
- Read secrets from the environment at runtime, not from a committed file.

=== "R"

    ```r
    # Read a token from the environment, never hard-code it
    token <- Sys.getenv("GITHUB_TOKEN")
    if (token == "") stop("Set the GITHUB_TOKEN environment variable")
    ```

=== "Python"

    ```python
    import os

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Set the GITHUB_TOKEN environment variable")
    ```

If you **accidentally commit a secret**, treat it as compromised: rotate/revoke it immediately. Removing the file and committing again does *not* erase it from history. (Fully purging history needs `git filter-repo` or the BFG Repo-Cleaner and a force-push — out of scope here, but the rule stands: prevent, don't just delete.)

## Exercise 2 — Prove a secret stays out

1. Create `.env` with a fake line: `GITHUB_TOKEN=fake-not-a-real-token`.
2. Add `.env` to `.gitignore` and confirm it is ignored with `git check-ignore -v .env`.
3. Try `git add .env` — Git should refuse (or at least it must not appear in `git status`).
4. If you ever needed to commit a *template* instead, commit `.env.example` with placeholder values and keep the real `.env` ignored.

## SSH keys — push without a password

HTTPS remotes ask for your username/password (or a token) on every push. SSH keys let your machine prove its identity to GitHub automatically and securely.

### 1. Generate a key pair

```sh
ssh-keygen -t ed25519 -C "you@example.com"
```

Press Enter to accept the default location (`~/.ssh/id_ed25519`). You may add a passphrase for extra safety.

### 2. Start the agent and add the key

```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### 3. Add the **public** key to GitHub

```sh
cat ~/.ssh/id_ed25519.pub
```

Copy that output and paste it into GitHub → Settings → SSH and GPG keys → New SSH key. **Never** share the private key (`id_ed25519` without `.pub`).

### 4. Test the connection

```sh
ssh -T git@github.com
```

You should see a message like `Hi <user>! You've successfully authenticated...`.

### 5. Use the SSH remote

If your remote is still an HTTPS URL, switch it:

```sh
git remote set-url origin git@github.com:your-user/your-repo.git
git push -u origin main
```

Now pushes no longer prompt for credentials.

!!! note "SSH vs HTTPS"
    Both work. SSH is convenient for repeated pushing from one machine; HTTPS with a token is common in CI and restricted networks. The safety rules (`.gitignore`, no secrets) apply either way.

## Exercise 3 — End-to-end safe push

1. Ensure your `.gitignore` covers outputs and secrets.
2. Confirm no unwanted files are staged: `git status`.
3. Generate an SSH key (if you have not), add the public key to GitHub, and verify with `ssh -T git@github.com`.
4. Set your remote to the SSH URL and push:

   ```sh
   git remote set-url origin git@github.com:your-user/your-repo.git
   git push -u origin main
   ```

5. On GitHub, confirm your committed files are present but your ignored files (`.env`, outputs) are **not**.

## Recap

| Topic | Key commands |
| --- | --- |
| Remotes | `git remote add origin <url>`, `git remote -v` |
| Share / fetch | `git push -u origin main`, `git clone <url>` |
| Ignore | `.gitignore`, `git check-ignore -v`, `git status --ignored` |
| Secrets | Keep in `.env` (ignored); read from environment |
| SSH | `ssh-keygen`, `ssh-add`, add `.pub` to GitHub, `ssh -T git@github.com` |

!!! success "What you can now do"
    You can safely connect a local repository to GitHub: ignore junk and secrets with `.gitignore`, keep credentials out of history, and authenticate with SSH so pushing is both passwordless and secure.

## What comes next

With remotes in place, the natural follow-up is collaboration through **forks, branches, and pull requests** — where your tests (from the testing session) can run automatically before a branch is merged.
