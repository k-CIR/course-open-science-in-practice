# Glossary

Terms you will encounter in the terminal, in Git, and in your code editor. Entries are aimed at researchers who have some scripting experience (e.g. in R) but are new to version control and the command line.

---

## Terminal & shell basics

**Terminal** (also: console, shell window)
: The text-based application through which you type commands. On macOS it is called *Terminal*; on Windows you may use *Git Bash*, *PowerShell*, or *Command Prompt*; on Linux any terminal emulator works. You interact with it by typing a command and pressing `Enter`.

**Shell**
: The program running *inside* the terminal that interprets your commands. The most common shells are `bash` (default on Linux and older macOS) and `zsh` (default on newer macOS). For most course purposes they behave identically.

**Command**
: A single instruction you type at the prompt, e.g. `git status` or `ls`. Commands can be followed by *flags* and *arguments*.

**Flag** (also: option, switch)
: A modifier that changes how a command behaves. Flags usually start with `-` (short form) or `--` (long form), e.g. `git log --oneline` or `ls -l`.

**Argument**
: A value passed to a command, such as a file name or path: `git add README.md`.

**Prompt**
: The line the shell displays to signal it is ready for input, typically ending with `$` or `%`. You do not type the prompt symbol itself.

**Working directory**
: The folder the shell is currently "inside". Commands that read or write files look here by default. Equivalent to the folder open in your file browser.

**Path**
: The address of a file or folder in the filesystem.

- *Absolute path* – starts from the root of the drive: `/Users/ada/project/script.R`
- *Relative path* – starts from the current working directory: `data/raw/input.csv`

**`~` (tilde)**
: A shorthand for your home directory, e.g. `~/Documents` expands to `/Users/ada/Documents` on macOS.

**`.` and `..`**
: `.` refers to the current directory; `..` refers to the parent directory one level up. Useful in paths: `cd ../other-project`.

---

### Common terminal commands

| Command | What it does |
| --- | --- |
| `pwd` | Print working directory – shows where you are |
| `ls` | List files and folders in the current directory |
| `cd <folder>` | Change directory – move into `<folder>` |
| `mkdir <name>` | Make directory – create a new folder |
| `cp <src> <dst>` | Copy a file from `<src>` to `<dst>` |
| `mv <src> <dst>` | Move (or rename) a file |
| `rm <file>` | Remove a file (no recycle bin – permanent) |
| `cat <file>` | Print the contents of a file to the terminal |
| `clear` | Clear the terminal screen |

---

## Git concepts

**Version control**
: A system that records changes to files over time so you can recall specific versions, compare differences, and collaborate without overwriting each other's work. Git is the most widely used version control system.

**Repository** (repo)
: A project folder tracked by Git. It contains your files plus a hidden `.git/` folder where Git stores the full history of changes.

**Initialise / init**
: The act of turning a plain folder into a Git repository: `git init`. Only done once per project. When you *clone* an existing repo this step is automatic.

**Clone**
: Download a complete copy of a remote repository, including its full history, to your local machine: `git clone <url>`.

**Staging area** (also: index)
: A preparation zone where you collect changes before committing them. You add files to it with `git add`. Think of it as putting items into a box before sealing and labelling it.

**Commit**
: A saved snapshot of the staged changes, permanently stored in the repository history. Each commit has a unique ID (hash), an author, a timestamp, and a message describing what changed. Equivalent to a labelled save point.

**Commit message**
: A short description you write when committing, explaining *why* the change was made. Convention: write in the imperative mood, e.g. `Add data cleaning script` rather than `Added` or `Adding`.

**Hash** (SHA)
: The unique identifier Git assigns to each commit, e.g. `a3f8c12`. You rarely need to type the full hash; the first 6–7 characters usually suffice.

**`HEAD`**
: A pointer to the commit you are currently working from — usually the latest commit on your active branch.

**Branch**
: An independent line of development within a repository. The default branch is typically called `main` (or `master` in older repos). Branches let you experiment or develop features without affecting the stable version.

**Checkout**
: Switch to a different branch or restore a file to a previous state: `git checkout <branch>`.

**Merge**
: Combine the history of one branch into another. Git tries to do this automatically; if two branches edited the same lines, a *merge conflict* occurs and must be resolved manually.

**Merge conflict**
: A situation where Git cannot automatically combine two sets of changes because they affect the same part of a file. Git marks the conflicting lines in the file and you decide which version to keep.

**Pull**
: Download new commits from a remote repository and merge them into your local branch: `git pull`. Combines `git fetch` and `git merge`.

**Push**
: Upload your local commits to a remote repository: `git push`. Others can then see and pull your changes.

**Remote**
: A version of your repository hosted elsewhere, typically on GitHub. The default remote is named `origin`.

**`origin`**
: The conventional name Git gives to the remote repository you cloned from or first pushed to.

**Fetch**
: Download new information from a remote without merging it: `git fetch`. Useful for seeing what has changed before deciding to merge.

**`.gitignore`**
: A plain-text file in the repository root listing file patterns Git should not track. Common entries include temporary files, credentials, large data files, and editor cache folders.

**Staging vs committing — a quick analogy**
: Think of writing a paper. *Staging* (`git add`) is highlighting edits on a printout. *Committing* (`git commit`) is submitting that revised draft with a cover note explaining what you changed.

---

## GitHub concepts

**GitHub**
: A cloud platform for hosting Git repositories. It adds a web interface, issue tracking, pull requests, and collaboration tools on top of Git.

**Fork**
: A personal copy of someone else's GitHub repository, stored under your own GitHub account. You can freely modify a fork without affecting the original.

**Pull request** (PR)
: A proposal to merge changes from one branch (or fork) into another, reviewed on GitHub before the merge happens. The name is slightly misleading — it is a *request for someone to pull your changes*.

**Issue**
: A GitHub discussion thread used to track bugs, feature requests, or tasks. Issues can be linked to pull requests.

**README**
: A file (usually `README.md`) at the root of a repository that describes what the project is, how to set it up, and how to use it. Displayed automatically on the GitHub repository page.

**`main` branch**
: The primary branch of a repository, representing the stable or official version of the project. Previously often called `master`.

---

## File & text concepts

**Plain text**
: A file containing only readable characters with no hidden formatting — e.g. `.R`, `.py`, `.md`, `.csv`. Plain-text files are what Git tracks most effectively. Contrast with binary files such as `.docx` or `.xlsx`.

**Markdown**
: A lightweight markup language where simple symbols add formatting: `**bold**`, `_italic_`, `# Heading`. GitHub renders Markdown automatically in READMEs and issues.

**CSV** (comma-separated values)
: A plain-text format for tabular data where columns are separated by commas and rows by line breaks. Readable by R (`read.csv()`), Python, Excel, and most other tools.

**Script**
: A plain-text file containing a sequence of commands to be run by an interpreter — e.g. an R script (`.R`), a shell script (`.sh`), or a Python script (`.py`).

**Working tree**
: All the files and folders in your repository as they appear on disk right now, as opposed to what is saved in Git history.

---

## Positron and VS Code concepts

**Positron**
: A code editor built by Posit (the company behind RStudio) on top of VS Code. It is designed for data science work with first-class support for R and Python. Because it shares the VS Code engine, most VS Code concepts below apply directly to Positron.

**VS Code** (Visual Studio Code)
: A free, open-source code editor from Microsoft. It is the engine Positron is built on. Many of the same keyboard shortcuts, settings, and extensions work in both.

**Editor** (also: text editor, IDE)
: The main area where you write and edit code. In Positron/VS Code the editor occupies the centre of the window and supports syntax highlighting, auto-complete, and inline error markers.

**Extension** (also: plugin)
: An add-on that gives the editor new capabilities — for example Git integration, a spell checker, a language server for R, or an AI assistant. Extensions are installed from the built-in marketplace (the puzzle-piece icon in the sidebar) and activated automatically on startup.

**Extension marketplace**
: The searchable catalogue of extensions inside Positron/VS Code. Open it with `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac), search by name, and click **Install**.

**Language server** (LSP)
: A background process that analyses your code and provides features like auto-complete, go-to-definition, and inline diagnostics. For R, the `languageserver` R package powers these features; Positron bundles its own R language server.

**Integrated terminal**
: A terminal panel built into the editor (`Ctrl+`` or `Cmd+``), so you can run shell commands and Git operations without switching windows. The working directory is automatically set to the open project folder.

**Command Palette**
: A searchable menu of every editor action, opened with `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac). If you cannot find a button for something, type it here.

**Workspace** (also: project folder)
: The folder you open in Positron/VS Code with **File → Open Folder**. All relative paths, terminal sessions, and extension settings are anchored to this folder. Equivalent to an R project root.

**Workspace settings**
: Configuration values stored in `.vscode/settings.json` inside your project folder. They override the user-level defaults for that project only and can be committed to Git so collaborators share the same editor behaviour.

**User settings**
: Global editor preferences stored in your home directory. They apply to every project unless overridden by workspace settings. Open them via the Command Palette: *Preferences: Open User Settings*.

**Source Control panel**
: The sidebar tab (branch icon) that shows staged, unstaged, and untracked file changes. It provides a graphical interface for the most common Git operations: staging, committing, pulling, and pushing — without needing the terminal.

**Gutter**
: The narrow strip to the left of the line numbers in the editor. Positron/VS Code uses it to display Git change indicators (green for added lines, blue for modified, red for deleted) and breakpoint markers.

**IntelliSense** (also: auto-complete, code completion)
: Suggestions that appear as you type, showing available function names, argument names, and variable names. Powered by the language server. Press `Tab` or `Enter` to accept a suggestion.

**Peek / Go to Definition**
: Right-click a function name and choose **Go to Definition** (or press `F12`) to jump to where it is defined — useful for inspecting package source code or your own helper functions.

**Snippets**
: Short reusable templates for common code patterns. Typing a trigger word (e.g. `fun`) and pressing `Tab` expands it into a full skeleton (e.g. an R function definition). Custom snippets can be added per language.

**Keybinding** (also: keyboard shortcut)
: A key combination assigned to an editor action. Positron/VS Code ships with a large default set; you can customise any of them via **Preferences: Open Keyboard Shortcuts** in the Command Palette.

**Split editor**
: Viewing two files side-by-side in the same window. Drag a tab to the right half of the editor, or use **View → Editor Layout → Split Right**. Useful for comparing a script with its output or a data file.

**Problems panel**
: A panel (usually at the bottom) listing errors and warnings the language server has detected in open files. Click an entry to jump directly to the relevant line.

**Output / Log panel**
: Shows messages from running extensions and background processes. Useful for diagnosing why an extension is not behaving as expected.

**`settings.json`**
: The JSON file that stores editor configuration. You can edit it directly via the Command Palette: *Preferences: Open Settings (JSON)*. Both user-level and workspace-level settings use this format.

**`.vscode/` folder**
: A hidden folder created by VS Code/Positron in your project root that stores workspace settings (`settings.json`), recommended extensions (`extensions.json`), and launch configurations. Committing this folder lets collaborators open the project with the same editor setup.

---

## R-specific connections

**R project (`.Rproj`)**
: An RStudio/Positron file that anchors the working directory to a specific folder, making relative paths in your scripts reliable. Committing the `.Rproj` file helps collaborators open the project with the same settings.

**`here` package**
: An R package (`library(here)`) that constructs file paths relative to the project root, regardless of where the script is run from. Complements Git-tracked R projects and avoids hard-coded absolute paths.

**`renv`**
: An R package that records which packages (and which versions) your project depends on, similar to how Git records file history. Running `renv::restore()` lets a collaborator reproduce your exact package environment.

**Quarto (`.qmd`)**
: A document format that mixes prose (Markdown) with executable R (or Python) code chunks. The rendered output can be HTML, PDF, or slides. Quarto files are plain text and version-controlled cleanly with Git.
