---
title: Introduction to Positron
author: "Niklas Edvall & Andreas Gerhardsson"
---

- Format: Lecture
- Teacher: Andreas

!!! todo "Content TODO"
    This session page is a placeholder. Add learning goals,
    materials, exercises, and links here.

## Why Positron?

For many researchers, R has meant RStudio — a dedicated environment that has served the R community well for over a decade. Positron is a new code editor developed by Posit (the company behind RStudio) that takes a different approach: rather than building a separate application for each language, it extends **Visual Studio Code** — the most widely used code editor in the world — with first-class, deeply integrated support for both R and Python.

The result is an editor that feels immediately familiar to anyone who has used VS Code, while still providing the console, environment pane, and plot viewer that R users expect. Positron is not a replacement for RStudio in the sense that it works differently — it is a deliberate step toward a more general, language-agnostic scientific computing environment.

For this course, Positron matters for two reasons. First, it integrates tightly with Git, making the version control operations you will learn — staging, committing, branching — available directly in the editor without switching to a terminal. Second, it supports Quarto natively, which you will use to write reproducible documents that mix prose, code, and output.

## What is Positron?

Positron is a free, open-source code editor released by Posit in 2024. It is built on the **VS Code engine** (the same foundation used by GitHub Codespaces, Cursor, and many other tools), which means it inherits VS Code's extension ecosystem, keyboard shortcuts, settings format, and terminal integration.

On top of that foundation, Posit has added:

- a dedicated **R language server** that provides auto-complete, inline diagnostics, and go-to-definition for R code
- an integrated **R console** and **Python console** that run inside the editor
- an **environment pane** showing variables, their types, and their values — similar to the RStudio Environment tab
- a **plot viewer** for R graphics output
- a **data viewer** for inspecting data frames interactively
- built-in support for **Quarto** documents and projects

Because it is built on VS Code, Positron also inherits the Source Control panel — a graphical interface for the most common Git operations — and the integrated terminal, which gives you full shell access without leaving the editor.

## The Positron interface

The Positron window is divided into several areas that you will use throughout the course.

**Activity bar** (left edge)
A vertical strip of icons that switch between the main sidebar panels: the file explorer, search, source control (Git), extensions, and others. Clicking an icon opens that panel in the sidebar; clicking it again collapses the sidebar.

**Sidebar**
The panel to the right of the activity bar. In Explorer mode it shows the file and folder tree of your open workspace. In Source Control mode it shows staged, unstaged, and untracked changes and provides buttons for the most common Git operations.

**Editor area** (centre)
Where files open for editing. Multiple files can be open as tabs. You can split the editor into two or more panes side by side, which is useful for reading a data file on one side while writing the script that processes it on the other.

**Console and terminal panel** (bottom)
The lower panel holds several tabs. The R console runs your R code interactively; results, warnings, and errors appear here. The Terminal tab gives you a full shell session. Additional tabs appear for output logs and diagnostics from extensions.

**Secondary sidebar** (right, optional)
Positron adds a second sidebar on the right that hosts the Environment pane (showing your R variables), the Plots pane, and the Connections pane. This layout mirrors the familiar RStudio four-pane design while keeping the editor at the centre.

## Workspaces and projects

In Positron, a **workspace** is a folder you open with **File → Open Folder**. Everything — the terminal working directory, relative file paths in your scripts, Git operations, and extension settings — is anchored to that folder. This is the equivalent of an RStudio project (`.Rproj`).

The recommended workflow for this course is:

1. Create a folder for your project.
2. Open that folder in Positron as a workspace.
3. Initialise a Git repository inside it (`git init` in the terminal, or use the Source Control panel).
4. Write and run your R or Python scripts from within that workspace.

Keeping all project files under one workspace folder, and that folder under Git version control, is the foundation of a reproducible and shareable analysis.

## Extensions

One of Positron's greatest strengths is its extension ecosystem, inherited from VS Code. Extensions add new capabilities to the editor — language support, linters, formatters, AI assistants, database connectors, and more. They are installed from the built-in marketplace (the puzzle-piece icon in the activity bar) and activated automatically when the editor starts.

Extensions relevant to this course:

- **R** (Posit) — the core R language server; installed by default in Positron
- **Quarto** — syntax highlighting, preview, and render support for `.qmd` files
- **GitLens** — enriches the built-in Git support with line-by-line blame, history browsing, and branch comparisons
- **GitHub Copilot** — AI-powered code completion and chat (covered in a later session)
- **Rainbow CSV** — colour-codes CSV columns in the editor, making data files easier to read

You do not need to install all of these immediately. The R and Quarto extensions are the ones to have from the start; the others can be added as the course progresses.

## Git integration in Positron

Because Positron is built on VS Code, the Git integration is built in — no additional extension is required for basic operations. The **Source Control panel** (branch icon in the activity bar) shows:

- **Changes** — files you have edited since the last commit, shown as unstaged
- **Staged changes** — files you have added with `git add`, ready to commit
- A text box for the **commit message** and a **Commit** button

Clicking the `+` icon next to a file stages it. Filling in the message box and clicking Commit is equivalent to `git commit -m "your message"`. The `...` menu at the top of the panel exposes push, pull, branch, and merge operations.

For learning purposes, it is worth doing these operations in the terminal at least a few times first so that you understand what each command does. Once the concepts are clear, the graphical panel is a convenient shortcut for the day-to-day workflow.

## Quarto in Positron

Quarto is a document system that lets you write prose and executable code in the same file. In Positron, `.qmd` files open with full syntax highlighting and a **Preview** button in the top-right corner of the editor that renders the document and displays the result alongside the source.

The typical Quarto document structure looks like this:

```markdown
---
title: "My analysis"
format: html
---

## Data preparation

```{{r}}
library(dplyr)
data <- read.csv("data/input.csv")
```

Some text describing the next step.
```

Running the Preview renders all code chunks and weaves the output — tables, plots, printed values — directly into the document. The rendered file is a single self-contained HTML (or PDF) that can be shared with collaborators or published online without them needing to install R.

Quarto documents committed to a Git repository give you a complete record of both the analysis code and its output at each point in time — which is the closest practical equivalent to a lab notebook for computational research.
