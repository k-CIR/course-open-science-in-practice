# Git branching

- Format: Workshop
- Teacher: Andreas

In this hands-on session you will practice branching in git. Still working locally.

So far you have worked on a **single straight line** of commits — what Git calls a branch. Branches are what make Git powerful for experimentation and collaboration: they let you work on a new idea in isolation, without risking the stable version of your project. In this workshop everything stays on your own machine; remotes (GitHub, pushing, pull requests) come in a later session.

By the end of the workshop you should be able to:

- Explain what a branch is (a movable pointer to a commit)
- Create, list, switch between, and delete branches
- Merge a branch back into another and understand a fast-forward merge
- Recognise and resolve a **merge conflict**
- Visualise your history with `git log --graph`

Start by opening your project in Positron

## Check where you are

```sh
git status
```

??? tip "Useful branch commands:"

      | Command | What it does |
      | --- | --- |
      | `git branch` | List branches (current marked with `*`) |
      | `git branch <name>` | Create a branch (without switching to it) |
      | `git switch <name>` | **Preferred:** move onto an existing branch |
      | `git switch -c <name>` | **Preferred:** create and switch to a new branch |
      | `git checkout <name>` | Older equivalent of `git switch <name>` |
      | `git checkout -b <name>` | Older equivalent of `git switch -c <name>` |
      | `git branch -d <name>` | Delete a branch you no longer need |
      | `git branch -D <name>` | Force-delete a branch (even if unmerged) |

!!! tip "Name branches by intent"
    Use descriptive names like `add-logging`, `fix-mean-bug`, or `try-new-model`. Avoid vague names like `test` or `branch1`.

## Exercise 1 — Branch and commit in isolation

Start from the project you built in the previous session (the one with `analysis.R` / `analysis.py` and its tests).

??? tip "Create and switch to a branch"

      ```sh
      git switch -c improve-summary
      ```

2. On this branch, edit your script to also report the **median** value.
3. Run your script to confirm everything works.
??? tip "Commit the change"

      ```sh
      git add analysis.R          # or analysis.py
      git commit -m "Report median in summary"
      ```

??? tip "Switch back to `main` and open the script"

      ```sh
      git switch main
      ```

      your median change is **not there**. That is the point: the work is isolated on `improve-summary`.

## Merge a branch back

Visualise your history
```sh
git log --oneline --graph --all
```

??? tip "Once a branch's work is finished and tested, bring it into `main` with a merge."

      ```sh
      # Make sure you are on the branch that should receive the changes
      git switch main

      # Merge the other branch in
      git merge improve-summary
      ```

### Fast-forward merges

??? task "Explain what happend to `HEAD`"

      If `main` has not moved since you branched, Git simply moves the `main` pointer forward to the same commit as `improve-summary`. This is a **fast-forward** merge — no new commit is created, because the histories are already a straight line.

      To always record a merge commit even when a fast-forward is possible, use:

      ```sh
      git merge --no-ff improve-summary
      ```

      The `--no-ff` (no fast-forward) flag creates an explicit merge commit, which keeps a clear record that the work came from a separate branch. Many teams prefer this for readability.

??? task "Visualise your history: git`git log --oneline --graph --all`. What do you see?"
      ```sh
      * 232528e (HEAD -> main, improve-summary) added median
      * d3d4264 added values
      * f701e59 added min values
      * e15b308 first commit
      ```

## Exercise 2 — A second branch and a real merge

1. From `main`, create another branch: `git switch -c add-range`.
2. On `add-range`, edit the script to also report the **range** (max − min).
3. Check that script works and commit it.
4. Switch back to `main` and add **standard deviation**
5. Check that script works and commit it.

??? task "Inspect the result: `git log --oneline --graph --all`. What do you see?"

      ```sh
      * d6c6e69 (HEAD -> main) sd added
      | * 7e5c133 (add-range) range added
      |/  
      * 232528e (improve-summary) added median
      * d3d4264 added values
      * f701e59 added min values
      * e15b308 first commit
      ```

## Merge conflicts

A conflict happens when two branches change the **same lines** of the same file and Git cannot decide which version to keep. This is normal and not dangerous — Git just pauses the merge and asks you to choose.

### Trigger a conflict on purpose

1. From `main`, create `git switch -c change-label`.
2. On `change-label`, edit the printed label text (for example change `"Mean:"` to `"Average:"`). Commit it.
3. Switch to `main`, then create `git switch -c change-value` from `main`.
4. On `change-value`, edit the **same line** to a different label (e.g. `"Mean value:"`). Commit it.
5. Merge the first branch into `main`, then try to merge the second:

   ```sh
   git switch main
   git merge change-label
   git merge change-value
   ```

   The second merge stops with `CONFLICT (content): Merge conflict in analysis.R`.

### Resolve the conflict

Open the conflicted file. Git marks the conflicting region like this:

```text
<<<<<<< HEAD
cat(sprintf("Mean value: %.2f\n", mean_value))
=======
cat(sprintf("Average: %.2f\n", mean_value))
>>>>>>> change-value
```

- The part between `<<<<<<< HEAD` and `=======` is your current branch's version.
- The part between `=======` and `>>>>>>> change-value` is the incoming branch's version.

Edit the file so it contains **only the version you want** (delete the marker lines), or try the `Resolve in Merge Editor` if that is available. This tool can be helpful especially when there are larger conflicts.

then stage and commit:

```sh
git add analysis.R          # or analysis.py
git commit -m "Resolve label conflict, keep 'Mean value'"
```

!!! tip "Abort a messy merge"
    If a conflict gets out of hand, back out completely with `git merge --abort`. This returns you to the state before the merge started.

## Clean up finished branches

After a branch is merged and you no longer need it, delete it to keep the list tidy:

```sh
git branch -d improve-summary
git branch -d add-range
```

Git refuses `git branch -d` on a branch whose work is not yet merged, which protects you from losing work. Use `-D` only when you are certain you want to discard an unmerged branch.

## Recap of the commands you learned

| Command | Purpose |
| --- | --- |
| `git branch` | List, create, or delete branches |
| `git switch <name>` / `-c` | Move to / create-and-move to a branch |
| `git checkout -b <name>` | Older equivalent of `git switch -c` |
| `git merge <branch>` | Merge another branch into the current one |
| `git merge --no-ff <branch>` | Merge but always create a merge commit |
| `git merge --abort` | Cancel an in-progress merge |
| `git log --oneline --graph --all` | Visualise branch and merge history |
| `git branch -d` / `-D` | Delete a branch (safe) / force-delete |

!!! success "What you can now do"
    You can isolate experimental work on branches, merge finished work back into `main`, resolve the inevitable conflicts, and keep your history readable with a graph view — all locally.

## What comes next

Remotes (`git remote`, `git clone`, `git push`, `git pull`) and pull requests build directly on branching. The next workshop takes your local branches and connects them to a shared repository on GitHub.
