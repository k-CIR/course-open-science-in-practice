---
title: Introduction to R
author: "Niklas Edvall & Andreas Gerhardsson"
---

- Format: Lecture
- Teacher: Andreas

!!! todo "Content TODO"
    This session page is a placeholder. Add learning goals,
    materials, exercises, and links here.

## Why R?

R was designed from the ground up for statistical computing and data analysis. Unlike general-purpose programming languages that require significant setup before you can work with data, R treats data as a first-class citizen: reading a spreadsheet, fitting a regression model, and producing a publication-quality plot are each a matter of a few lines of code and a well-documented function call.

For researchers, this matters in a practical sense. The skills you invest in learning R carry directly across disciplines — the same language used to clean a clinical dataset is used to analyse genomic sequences, model ecological populations, or visualise survey responses. R has a large and active community of researchers who publish their methods as packages, which means that specialised statistical procedures relevant to your field are often already implemented, documented, and peer-reviewed.

R is also free and open source, which removes licensing barriers for yourself, your collaborators, and anyone who later wants to reproduce your work. A published analysis written in R can be run by anyone, anywhere, without a commercial software subscription.

## R compared to point-and-click tools

Many researchers begin their data work in Excel, SPSS, or similar point-and-click tools. These tools are genuinely useful for quick exploration, but they have structural limitations that become significant as analyses grow more complex or need to be shared and reproduced.

In a point-and-click environment, the steps you take — filtering rows, creating a new column, running a test — are not recorded anywhere in a form that can be re-run or inspected. If you return to the same dataset six months later, or hand it to a colleague, the chain of decisions that produced the final result is effectively invisible. Reproducing the analysis means repeating the same sequence of clicks by memory or from hastily written notes.

In R, every step of an analysis is written as code. The code is the record. Running it again on the same data produces exactly the same result. Sharing the analysis means sharing the script. Changing one step — say, applying a different exclusion criterion — means editing one line and re-running, rather than manually redoing every downstream step. This is what reproducibility means in practice, and it is the property that makes a scripted analysis trustworthy and collaborative in a way that a click-based one cannot be.

## The R language — core concepts

R is an interpreted language, meaning you write a statement and R executes it immediately, returning the result. This makes it well suited to interactive data exploration as well as to writing complete analysis scripts.

**Objects and assignment**
Everything in R is an object. You create an object by assigning a value to a name using the `<-` operator:

```r
age <- 42
name <- "Ada"
scores <- c(87, 91, 74, 88)
```

Object names are case-sensitive (`Age` and `age` are different objects) and should be descriptive. The convention in R is to use `snake_case` — words separated by underscores — for readability.

**Vectors**
The fundamental data structure in R is the vector — an ordered collection of values of the same type. Almost every operation in R is vectorised, meaning it applies to all elements automatically:

```r
scores <- c(87, 91, 74, 88)
scores * 2          # multiplies every element
mean(scores)        # returns the average
scores[scores > 85] # selects elements above 85
```

**Functions**
R provides thousands of built-in functions, and packages add many more. A function takes one or more inputs (arguments) and returns an output:

```r
sqrt(16)              # returns 4
round(3.14159, 2)     # returns 3.14
nchar("hello")        # returns 5
```

You can write your own functions to encapsulate repeated logic:

```r
z_score <- function(x) {
  (x - mean(x)) / sd(x)
}
z_score(scores)
```

**Data frames**
The data structure you will work with most is the **data frame** — a rectangular table where each column is a vector and each row is an observation. Data frames map directly onto the kind of datasets researchers work with: one row per subject or sample, one column per variable.

```r
df <- data.frame(
  id    = c(1, 2, 3),
  group = c("A", "B", "A"),
  score = c(87, 91, 74)
)
df$score          # access the score column
df[df$group == "A", ] # filter to group A
```

## Packages

Base R is powerful, but much of what makes R practical for research is the package ecosystem. A package is a collection of functions, datasets, and documentation bundled together and published to CRAN (the Comprehensive R Archive Network) or GitHub.

Packages are installed once and then loaded at the start of each session:

```r
install.packages("dplyr")   # run once to install
library(dplyr)               # run at the top of every script that uses it
```

Three packages you will encounter frequently in this course:

**dplyr** — a grammar of data manipulation. It provides a consistent set of verbs — `filter()`, `select()`, `mutate()`, `summarise()`, `group_by()` — that cover the majority of data wrangling tasks and chain together cleanly using the pipe operator (`|>`):

```r
df |>
  filter(group == "A") |>
  mutate(score_scaled = scale(score)) |>
  summarise(mean_score = mean(score_scaled))
```

**ggplot2** — a system for creating graphics based on the Grammar of Graphics. You build a plot by declaring what data to use, how to map variables to visual properties (axes, colour, size, shape), and which geometric objects to draw:

```r
library(ggplot2)
ggplot(df, aes(x = group, y = score, colour = group)) +
  geom_boxplot() +
  geom_jitter(width = 0.1) +
  theme_minimal()
```

**tidyr** — tools for reshaping data between wide and long formats, which is often a necessary step before plotting or modelling:

```r
library(tidyr)
df_long <- pivot_longer(df, cols = starts_with("score"),
                         names_to = "measure", values_to = "value")
```

These three packages, along with a handful of others, form the **tidyverse** — a collection of packages that share a common design philosophy and work well together. Loading the tidyverse meta-package (`library(tidyverse)`) brings all of them in at once.

## Reading and writing data

Most analyses begin by reading data from a file. R can read from almost any format; the most common in research contexts are CSV files and Excel spreadsheets.

```r
# Read a CSV file
data <- read.csv("data/raw/participants.csv")

# Read an Excel file (requires the readxl package)
library(readxl)
data <- read_excel("data/raw/participants.xlsx", sheet = "Sheet1")

# Write results to a CSV
write.csv(results, "data/processed/results.csv", row.names = FALSE)
```

One important habit is to use **relative paths** rather than absolute paths in your scripts. An absolute path such as `/Users/ada/projects/study/data/participants.csv` works only on your machine. A relative path such as `data/participants.csv` works for anyone who opens the project from its root folder — which is exactly what happens when you share a Git repository and a collaborator clones it.

The `here` package makes relative paths robust and explicit even when scripts are run from different working directories:

```r
library(here)
data <- read.csv(here("data", "raw", "participants.csv"))
```

## Reproducibility in practice

A reproducible R analysis is one where running the script from top to bottom, on a fresh R session, produces the same results every time. A few habits make this achievable:

**Never modify data by hand.** All cleaning, filtering, and transformation should happen in code. If you discover an error in a raw data file, fix it in the script, not in the file itself, and re-run.

**Set a random seed when your analysis uses randomness.** Functions like `sample()`, `rnorm()`, and many modelling procedures draw random numbers. Setting `set.seed(42)` (or any integer) at the top of the script ensures the same sequence of random numbers is drawn each time.

**List all package dependencies explicitly.** Every package your script uses should appear in a `library()` call at the top of the file. Do not rely on packages being loaded by side-effect from another package.

**Use `renv` to record package versions.** Different versions of a package can produce different results. `renv` records the exact version of every package your project uses in a lockfile that can be committed to Git, so a collaborator can restore the identical environment with `renv::restore()`.

```r
# Initialise renv in a new project
renv::init()

# After installing or updating packages, snapshot the state
renv::snapshot()

# A collaborator clones the repo and restores the environment
renv::restore()
```

Combining a version-controlled script with `renv` gives you a complete and portable record of both the analysis logic and the computational environment that produced it — which is the practical meaning of reproducible research.
