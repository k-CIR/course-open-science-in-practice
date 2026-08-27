# Git and testing in practice

- Format: Workshop
- Teacher: Andreas

In this hands-on session you will learn how to combine **automated tests** with your Git workflow. A script that only *prints* results is hard to verify; tests assert that your code behaves as expected, give you a repeatable check after every change, and — crucially — become part of the version history you commit.

You can follow the **R** track (`testthat`) or the **Python** track (`pytest`). Both teach the same Git lessons. Everything stays on your own machine.

By the end of the workshop you should be able to:

- Write a small unit test for an R or Python function
- Run the tests and interpret pass/fail output
- Commit the tests so they live alongside your code in Git
- Use a "red → green → commit" loop when changing code
- Build a tiny, runnable test suite for a small analysis project

## Why tests belong in version control

Tests are code. Like the rest of your analysis, they benefit from being versioned:

- A test you wrote last month proves *when* a behaviour was correct and *when* it broke.
- Committing tests together with the code they cover keeps them in sync.
- When a teammate (or future you) checks out an old commit, the matching tests come with it.

The everyday loop is: **edit code → run tests → if green, commit**. Tests are the gate that decides whether a change is worth recording.

## The project we will test

Start from a small analysis project (the one from earlier sessions, or a new folder). We will factor the calculations into a **function** so they can be tested in isolation.

=== "R (analysis.R)"

    ```r
    # analysis.R
    # A tiny descriptive-stats script used to practise testing.

    summarize <- function(values) {
      list(
        mean = mean(values),
        min  = min(values),
        max  = max(values)
      )
    }

    values <- c(4, 8, 15, 16, 23, 42)
    result <- summarize(values)

    cat(sprintf("Mean: %.2f\n", result$mean))
    cat(sprintf("Min:  %d\n",   result$min))
    cat(sprintf("Max:  %d\n",   result$max))
    ```

=== "Python (analysis.py)"

    ```python
    # analysis.py
    # A tiny descriptive-stats script used to practise testing.

    def summarize(values):
        return {
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
        }

    values = [4, 8, 15, 16, 23, 42]
    result = summarize(values)

    print(f"Mean: {result['mean']:.2f}")
    print(f"Min:  {result['min']}")
    print(f"Max:  {result['max']}")
    ```

If you are starting fresh, initialise the repository and make your first commit:

```sh
git init
git add analysis.R            # or analysis.py
git commit -m "Add summarize function and script"
```

## Write your first test

A unit test checks one behaviour with `expect_equal` (R) or `assert` (Python). Create a test file next to your script.

=== "R (test_analysis.R with testthat)"

    ```r
    # test_analysis.R
    library(testthat)

    source("analysis.R")   # makes summarize() available

    test_that("summarize returns correct statistics", {
      out <- summarize(c(4, 8, 15, 16, 23, 42))

      expect_equal(out$mean, 18)
      expect_equal(out$min,  4)
      expect_equal(out$max,  42)
    })

    test_that("summarize handles a single value", {
      out <- summarize(c(7))
      expect_equal(out$mean, 7)
      expect_equal(out$min,  7)
      expect_equal(out$max,  7)
    })
    ```

    Run the tests:

    ```sh
    Rscript -e 'testthat::test_file("test_analysis.R")'
    ```

    A passing run prints `Test passed 🌈`. A failure prints the expected vs. actual values.

=== "Python (test_analysis.py with pytest)"

    ```python
    # test_analysis.py
    from analysis import summarize

    def test_summarize_basic():
        out = summarize([4, 8, 15, 16, 23, 42])
        assert out["mean"] == 18
        assert out["min"] == 4
        assert out["max"] == 42

    def test_summarize_single_value():
        out = summarize([7])
        assert out["mean"] == 7
        assert out["min"] == 7
        assert out["max"] == 7
    ```

    Run the tests:

    ```sh
    python -m pytest test_analysis.py
    ```

    A green dot and `2 passed` means success; a red `F` shows which assertion failed.

!!! note "Install the test framework once"
    R: install `testthat` with `install.packages("testthat")`.
    Python: install `pytest` with `pip install pytest` (or `python -m pip install pytest`).

## Commit the tests

Run the tests and confirm they pass, then record the test file in Git:

```sh
git add test_analysis.R      # or test_analysis.py
git commit -m "Add tests for summarize function"
```

From now on, every change to `analysis.R` / `analysis.py` should be followed by a test run, and a green suite is your signal that it is safe to commit.

## Exercise 1 — Extend the suite (red → green)

1. Add a new requirement: `summarize` should also report the **median**.
2. First, write a failing test for the median (the function does not return it yet, so the test is **red**).
3. Update `summarize` to return the median, and update the script to print it.
4. Run the tests — they should now be **green**.
5. Commit both the code and the new test together:

   ```sh
   git add analysis.R test_analysis.R     # or the .py versions
   git commit -m "Add median to summarize and test it"
   ```

This red → green → commit rhythm is the core of test-driven, version-controlled work.

## Exercise 2 — Break it on purpose, then fix it

1. In `analysis.R` / `analysis.py`, deliberately introduce a bug — for example, divide the mean by `length(values) - 1` in R, or forget to divide in Python.
2. Run the tests. They should **fail**, proving the tests actually guard your logic.
3. Fix the code so the tests pass again.
4. Commit the fix:

   ```sh
   git add analysis.R            # or analysis.py
   git commit -m "Fix mean calculation, restore green tests"
   ```

## Exercise 3 — Test edge cases

Good tests cover the awkward inputs, not just the happy path.

1. Add a test for an **empty** input. In R, `mean(numeric(0))` returns `NaN`; in Python, `sum([])/len([])` raises `ZeroDivisionError`. Assert the behaviour you expect (or that it raises an error).
2. In Python you can assert an error is raised:

   ```python
   import pytest

   def test_empty_raises():
       with pytest.raises(ZeroDivisionError):
           summarize([])
   ```

3. In R you can assert a warning/error with `expect_error` or check for `NaN` with `expect_true(is.nan(...))`.
4. Run the suite and commit the new edge-case tests:

   ```sh
   git add test_analysis.R      # or test_analysis.py
   git commit -m "Add edge-case tests for empty input"
   ```

## Running the whole suite

As your project grows, you will have several test files. Run them all at once:

=== "R"

    ```sh
    Rscript -e 'testthat::test_dir(".")'
    ```

    This runs every `test_*.R` file in the folder.

=== "Python"

    ```sh
    python -m pytest
    ```

    With no file argument, `pytest` discovers every `test_*.py` file.

Make it a habit to run the full suite before committing, so you never record a state where the tests are red.

## Recap

| Step | Command (R / Python) |
| --- | --- |
| Write a test | `test_analysis.R` / `test_analysis.py` |
| Run tests | `Rscript -e 'testthat::test_file(...)'` / `python -m pytest ...` |
| Run all tests | `testthat::test_dir(".")` / `python -m pytest` |
| Commit green tests | `git add <testfile> && git commit -m "..."` |

!!! success "What you can now do"
    You can write unit tests for your analysis functions, run them as a suite, use a red→green loop to develop safely, and commit tests alongside the code they protect — making your repository both runnable and verifiable at any point in history.

## What comes next

With local commits, branches, and tests in place, the final piece is sharing: connecting your repository to a remote (GitHub) and opening pull requests, where tests often run automatically before a branch is merged.
