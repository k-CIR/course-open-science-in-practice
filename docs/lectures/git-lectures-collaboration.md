---
title: Collaboration
author: "Niklas Edvall & Andreas Gerhardsson"
---

- Format: Lecture
- Teacher: Andreas

## Summary

So far every remote you have touched has been one you created yourself: you pushed, and only you pulled. Real collaboration means several people push to and pull from the *same* shared history, often without ever talking to each other about who does what first. This lecture closes that gap. It covers **cloning** (getting a full, working copy of someone else's repository), **forking** (getting your own remote copy of it on GitHub), and the **pull request** — the mechanism that lets your work travel back into a project you do not have direct write access to.

## Two ways to collaborate

There are two common shapes of collaboration, and the difference is about *who can push where*:

- **Shared repository.** Everyone has write access to the same repository. Each person clones it, works on their own branch, and pushes that branch back to the same remote. This is typical inside a small team or a course group.
- **Fork and pull request.** You do *not* have write access to the original ("upstream") repository — think of an open-source project, or your course buddy's project. Instead you create your own copy on GitHub (a **fork**), push your branch there, and then ask the upstream project to pull your changes in via a **pull request**.

Both shapes end the same way — a maintainer merges a branch into `main` — they just differ in *whose remote* your branch lives on before that happens.

## Cloning: a full copy, remote included

`git clone` does more than copy files. It initialises a new local repository, copies the *entire* history (every commit, every branch you have access to), and — critically — automatically wires up a remote called `origin` pointing back at wherever you cloned from:

```sh
git clone git@github.com:some-user/some-repo.git
cd some-repo
git remote -v
# origin  git@github.com:some-user/some-repo.git (fetch)
# origin  git@github.com:some-user/some-repo.git (push)
```

Compare that to starting a project from scratch with `git init`, where there is no remote at all until you explicitly `git remote add origin <url>` yourself (as you did in the remote session). Cloning *inherits* the remote for you as part of the same command — one less thing to configure, and one less thing to get wrong.

## Fetch, pull, and clone are not the same operation

These three commands all bring history from a remote into your machine, but they do different amounts of work:

| Command | What it downloads | Does it touch your working files / branches? |
| --- | --- | --- |
| `git clone <url>` | Everything, for the first time | Creates a brand-new local repository and checks out the default branch |
| `git fetch <remote>` | New commits and branches from the remote | **No.** Updates remote-tracking branches (e.g. `origin/main`) only; your `main` and working directory are untouched |
| `git pull <remote> <branch>` | New commits from the remote | **Yes.** Runs `git fetch`, then immediately merges (or rebases) the fetched commits into your current branch |

`git fetch` is the "look before you leap" option: it lets you inspect what changed (`git log main..origin/main`) before deciding whether and how to bring it in. `git pull` skips the inspection step and merges right away — convenient, but it is exactly `fetch` + `merge` bundled together, so a pull can produce a merge commit or a conflict just like any other merge.

!!! info "`origin/main` vs `main`"
    `origin/main` is a **remote-tracking branch** — a read-only bookmark recording where `origin`'s `main` was as of your last fetch. Your own `main` only moves when *you* commit or merge into it. This is why `git fetch` is always safe to run: it can update `origin/main`, but it can never change `main` or your files out from under you.

## Forking: your own remote copy

A **fork** is a copy of someone else's repository, created on GitHub itself, that lives under your own account. It has its own independent history and its own remote URL, but GitHub remembers where it was forked from so it can offer you a pull request later.

:octicons-repo-forked-16: The workflow, in order:

1. On GitHub, click **Fork** on the upstream project. GitHub creates `you/some-repo`, a full copy, under your account.
2. Clone *your fork* — not the original — to your machine. Because you cloned your fork, `origin` now points at `you/some-repo`, and you have push access to it.

```sh
git clone git@github.com:you/some-repo.git
cd some-repo
git remote -v
# origin  git@github.com:you/some-repo.git (fetch)
# origin  git@github.com:you/some-repo.git (push)
```

You can push to `origin` freely — it is your copy — but you have no write access to the original project yet.

## Adding a second remote: `upstream`

A single repository is not limited to one remote. To stay in sync with the project you forked from, add it as a second remote — by convention named `upstream`:

```sh
git remote add upstream git@github.com:original-owner/some-repo.git
git remote -v
# origin    git@github.com:you/some-repo.git (fetch)
# origin    git@github.com:you/some-repo.git (push)
# upstream  git@github.com:original-owner/some-repo.git (fetch)
# upstream  git@github.com:original-owner/some-repo.git (push)
```

Now `fetch`, `pull`, and `push` all take an explicit remote name, so you control which direction data moves:

```sh
git fetch upstream          # see what changed in the original project
git merge upstream/main     # bring those changes into your local main
git push origin main        # update your fork with them too
```

`origin` is where *your* work goes; `upstream` is where the *project's* work comes from. Mixing the two up is the most common source of confusion when working with forks — always double-check which remote a command targets.

!!! info "Naming is a convention, not a rule"
    `origin` and `upstream` are just labels — Git does not treat them specially. Everyone uses these two names by convention because it makes every collaboration guide (including this one) predictable to follow.

## Pushing your branch and opening a pull request

Whether you are working in a shared repository or a fork, the shape of contributing a change is the same: branch, commit, push, then ask for a review.

```sh
git switch -c fix-typo
# ... edit and commit ...
git push -u origin fix-typo
```

Pushing a *new* branch does not touch `main` at all — it simply uploads the branch to the remote, ready to be reviewed. On GitHub, this shows up as an option to open a **pull request (PR)**: a formal request that says *"please merge my branch into your `main`"*. A PR is not a Git concept — Git only has branches and commits — it is a GitHub feature layered on top that adds discussion, review comments, and required checks before a merge happens.

:octicons-git-pull-request-16: A pull request against a **fork** targets the upstream repository directly, even though your branch lives on `origin`; GitHub handles finding it because it remembers the fork relationship.

## When your push is rejected

If a teammate (or you, from another machine) already pushed new commits to `main` since you last fetched, your own push is **rejected**, not overwritten:

```text
! [rejected]        main -> main (fetch first)
error: failed to push some refs
```

Git refuses to push because doing so would silently discard commits it does not know about — the same protective instinct as a merge conflict. The fix is the same shape every time: fetch, integrate, then push.

```sh
git pull origin main   # fetch + merge the commits you were missing
# resolve any conflicts, exactly as in the branching session
git push origin main   # now it is a fast-forward from the remote's point of view
```

!!! info "A rejected push is not a conflict — yet"
    Rejection just means the remote moved. Whether resolving it actually produces a merge conflict depends on whether the same lines were touched — most of the time `git pull` merges cleanly and you push again immediately.

## Merging a pull request

Once a reviewer approves a pull request, merging it on GitHub does exactly what `git merge` does locally — fast-forward if possible, or a merge commit if both sides moved — it is just triggered through the web interface instead of your terminal. After the merge:

1. The branch's commits become part of upstream's `main`.
2. You can delete the now-merged branch (locally with `git branch -d`, and on the remote with `git push origin --delete fix-typo`).
3. Everyone — including you — needs to `git pull` to bring that merged `main` down to their own machine.

That last step trips people up: merging a PR only changes the remote. Your local `main` only catches up once you explicitly pull it.

## Summary

- Cloning inherits the remote for you: `origin` is wired up automatically, unlike `git init` where you add it by hand.
- `fetch` downloads without touching your files; `pull` is `fetch` + `merge` in one step.
- Forking makes your own remote copy on GitHub; you clone the fork, so `origin` is *yours*.
- `upstream` is the conventional name for the original project's remote, added with `git remote add`.
- A rejected push means the remote moved on — pull (fetch + merge/resolve), then push again.
- A pull request asks a project to merge your branch; merging it is a normal Git merge triggered from GitHub, and you still need to `pull` afterwards to see it locally.

The workshop puts this into practice: you will clone, fork, add an `upstream` remote, push a branch, and open (and merge) a pull request end to end.
