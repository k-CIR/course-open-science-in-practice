---
title: Git safety and remote (GitHub)
author: "Niklas Edvall & Andreas Gerhardsson"
---

- Format: Lecture
- Teacher: Andreas

[:material-file-pdf-box: Download slides (.pdf)](downloads/3-git-remote.pdf){ .md-button download="3-git-remote.pdf" }

## Slides

<div class="slide-gallery" markdown="1">

![Slide 1](../slides/3-git-remote/slide_001.png)
![Slide 2](../slides/3-git-remote/slide_002.png)
![Slide 3](../slides/3-git-remote/slide_003.png)
![Slide 4](../slides/3-git-remote/slide_004.png)
![Slide 5](../slides/3-git-remote/slide_005.png)
![Slide 6](../slides/3-git-remote/slide_006.png)
![Slide 7](../slides/3-git-remote/slide_007.png)
![Slide 8](../slides/3-git-remote/slide_008.png)
![Slide 9](../slides/3-git-remote/slide_009.png)
![Slide 10](../slides/3-git-remote/slide_010.png)
![Slide 11](../slides/3-git-remote/slide_011.png)
![Slide 12](../slides/3-git-remote/slide_012.png)
![Slide 13](../slides/3-git-remote/slide_013.png)
![Slide 14](../slides/3-git-remote/slide_014.png)
![Slide 15](../slides/3-git-remote/slide_015.png)
![Slide 16](../slides/3-git-remote/slide_016.png)
![Slide 17](../slides/3-git-remote/slide_017.png)
![Slide 18](../slides/3-git-remote/slide_018.png)
![Slide 19](../slides/3-git-remote/slide_019.png)
![Slide 20](../slides/3-git-remote/slide_020.png)
</div>

## Summary

![bots](../assets/bot-remote.png){ width=40% align="right"}
You can work on git completely on your own machine. That is great for privacy and for learning how git works without having to be afraid that sensitive data is put somewhere where it should not be. 

However, it also means your work is one spilled coffee away from being lost, and it cannot be shared or collaborated on. A **remote** solves both problems — but it also introduces risk, because whatever you push can be seen by others, and on a public remote it can be seen by *everyone*. This lecture covers the concepts of remotes, and the safety practices — `.gitignore`, secret-handling, and SSH — that keep you from sharing what you did not mean to.

## Remote options
There are a few options for remote handling of your repository. [GitHub](https://github.com) is the most common, but it is owned by Microsoft and not open source. [GitLab](https://about.gitlab.com) is open source and can be set up at a local server. [KI ITA offers a GitLab account](https://staff.ki.se/tools-and-support/it-and-telephony/order-it-and-telephony-services/ki-gitlab-for-managing-source-code) but it can only be accessed by KI associated.

## What is a remote really?

Because Git is distributed, every clone is a full repository with its own complete history. A remote is not a "master" server in the traditional sense — it is simply a convenient, shared meeting point that everyone agrees to push to and pull from. This is why GitHub going down does not destroy your history: your local copy is intact.

A **remote** is just a saved reference — a URL — to another copy of your repository. Git stores it under a short name, by convention `origin`. Adding a remote does not copy anything; it only tells Git *where* `origin` points. The actual copying happens later, explicitly, when you `push` (send your history out) or `pull`/`clone` (bring history in).

To add a remote, use `git remote add <name> <url>`. By convention the primary remote is called `origin`, but that is only a label — Git does not care what you call it.

To change a remote later — for example switching from HTTPS to SSH, or because the repository moved — use `git remote set-url <name> <new-url>`. This only updates the recorded address; it does not touch any commits or history.

You can have multiple remotes registered at once, each under its own name. This is exactly how the forking workflow in the [next lecture](git-lectures-collaboration.md) works: `origin` points at your own copy, while a second remote — conventionally named `upstream` — points at the project you forked from, so you can pull in updates without losing your changes.

```sh
git remote add origin git@github.com:your-user/your-repo.git             # register a remote
git remote set-url origin https://github.com/your-user/your-repo.git     # change its URL
git remote add upstream git@github.com:original-owner/original-repo.git  # add a second remote
git remote -v                                                            # list all remotes, with URLs
```

![remote](../assets/git_flow_remote.svg)

!!! info "git pull/fetch/clone"
    All three bring history from a remote onto your machine, but they differ in *how much* they do and whether they touch your files:

    | Command | What it does |
    | --- | --- |
    | `git clone <url>` | One-time setup: copies the **entire** repository and its history into a new folder, and automatically sets up `origin` for you |
    | `git fetch <remote>` | Downloads new commits and branches from the remote, but does **not** touch your current branch or working files — it only updates remote-tracking references such as `origin/main` |
    | `git pull <remote> <branch>` | Runs `git fetch`, then immediately **merges** (or rebases) the new commits into your current branch — this is the one that can change your files and trigger a merge conflict |

    A useful habit is to `git fetch` first to see *what* changed (`git log main..origin/main`), then `git pull` (or `git merge origin/main`) once you are ready to bring it in. `git clone`, by contrast, you only ever run once per project, right at the start.

    The [collaboration lecture](git-lectures-collaboration.md) goes into more depth on this, including forking a project and keeping your copy in sync with `upstream`.

??? info "The "Sync Changes" button in VS Code / Positron"

    If you use the Source Control panel instead of the terminal, you will not see separate `fetch`, `pull`, and `push` buttons by default — instead there is usually one button, labelled **Sync Changes**, often shown as a circular-arrows icon with a count like `↓2 ↑1`. It is not a new Git operation; it is a convenience wrapper around the commands you already know:

    1. **`git fetch`** — check what is new on the remote
    2. **`git pull`** — merge those changes into your current branch
    3. **`git push`** — send your own commits back up

    The numbers next to the icon tell you *why* a sync is needed before you even click it: `↓2` means two commits exist on the remote that you do not have yet (incoming), `↑1` means you have one local commit the remote does not have yet (outgoing).

    Clicking **Sync Changes** is equivalent to running `git pull` immediately followed by `git push` in the terminal. It has exactly the same behaviour: if the remote has commits that conflict with yours, the merge step pauses in the middle of the sync exactly as a plain `git pull` would, and you resolve it the same way — edit the marked file, stage it, commit — before the push half of the sync can go through.

## The danger: what gets committed, stays committed

The single most important safety rule is this: **once a file is committed and pushed, assume it is permanent and, on a public remote, public.** Even if you delete the file in a later commit, the data still exists in earlier commits in the history. Also if you make a private repository public, its commit history will still be there.

This has two consequences:

1. Be deliberate about what you `git add` in the first place.
2. Never put credentials, tokens, or private data into a commit at all.

The remedy is not "delete it later" — it is "never let it in." That is the job of `.gitignore` and good secret-handling habits.

!!! info "Tool to rewrite commit history"
    If a secret is *accidentally* committed, the correct response is to **treat it as compromised and rotate/revoke it immediately**. Removing it in a later commit does not remove it from history; truly purging it requires rewriting history (with tools like [git-filter-repo](https://github.com/newren/git-filter-repo) or the [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)) and a force-push. Prevention is dramatically simpler than cleanup.
    

## `.gitignore`: deciding what Git never sees

A `.gitignore` file lists patterns for files Git should **not track** — operating-system noise (`.DS_Store`), editor temp files, generated outputs, and, critically, secrets. It lives in the root of your repository and is committed itself, so the rules travel with the project and apply to everyone who clones it.

The mental model: `.gitignore` is a filter at the *entry* to your repository. Files matching its patterns never reach the staging area, never get committed, and therefore never get pushed. You can always verify a rule with `git check-ignore -v <file>`, which reports exactly which line caused a file to be ignored.

For a research project, a good `.gitignore` typically excludes:

- OS and editor junk (`.DS_Store`, `.Rhistory`, `__pycache__/`)
- Regenerable outputs (`/results/`, `*.png`, `*.csv`)
- Secrets (`.env`, `*.key`, `credentials.json`)

The principle: **commit source and documentation; ignore data, outputs, and secrets** (unless a specific data file is itself the curated research output, which is a separate decision).

## Secrets: keep them out of Git entirely

API keys, tokens, and passwords must never enter version control. The safe pattern is to store them in a file *outside* Git — conventionally `.env` — and add that file to `.gitignore`. Your script then reads the value from the environment at runtime rather than from a committed file:

=== "R"

    ```r
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

## SSH keys: proving who you are without a password

To push to GitHub you must prove your identity. HTTPS remotes ask for a username and a personal access token on every push — workable, but tedious. **SSH keys** provide a smoother and more secure alternative.

An SSH key pair has two parts: a **private key** that stays on your machine and must never be shared, and a **public key** that you register with GitHub. When you push, your machine uses the private key to prove it holds the matching pair; GitHub checks it against the public key you registered. No password is transmitted, and the private key is never sent anywhere.

The safety takeaway: add only the **public** key (the file ending in `.pub`) to GitHub. Anyone who obtains your public key learns nothing useful; only the private key grants access, so it stays local and is typically protected by a passphrase.

??? tip "Adding your public key to GitHub"
    :material-key-chain-variant: Already generated a key pair and just need to register the public half with your account? Step-by-step instructions (with copy commands for macOS, Linux, and Windows) are in the setup guide:

    [:material-github: Add the key to GitHub :octicons-arrow-right-16:](../setup/github-setup.md#4-add-the-key-to-github){ .md-button }


## HTTPS vs SSH

Both protocols are valid. SSH is convenient for repeated pushing from a trusted machine and avoids storing tokens locally. HTTPS with a token is common in restricted networks and continuous-integration systems. The safety rules — ignore junk, keep secrets out, push only intended files — apply identically regardless of which you choose. You can switch a remote between them at any time with `git remote set-url`.

## Summary

- A remote is a saved URL (conventionally `origin`); pushing and pulling move history in and out explicitly.
- Committed-and-pushed data is effectively permanent and, on public remotes, public — so be deliberate.
- `.gitignore` filters files at the entry point; commit source, ignore data/outputs/secrets.
- Keep secrets in an ignored `.env` and read them from the environment at runtime.
- SSH keys authenticate passwordlessly: share only the public key, guard the private key.
- Your editor's **Sync Changes** button is just `pull` + `push` in one click — it can conflict and pause exactly like `git pull` does from the terminal.

The [Git remote exercises](../exercises/git-exercises-remote.md) will put these ideas into practice: linking a remote, writing a `.gitignore`, and setting up SSH so you can push safely.
