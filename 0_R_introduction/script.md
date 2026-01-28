In this video, you will learn how to go from a raw data table like this \[on screen\] to a result report like this \[on screen\] using the R programming language for statistical computing.

Firstly, R is the programming language and there are plenty of ways to interact with it. The most basic is in a console or terminal like this.

> *Open command window*

Essentially R is a calculator and in this command window you can perform different calculations. For example addition, subtraction, multiplication, and division.

```r
2+3
[1] 5

7-5
[1] 2

4*3
[1] 12

15/3
[1] 5
```

The 1 in brackets that we see before the returned value just tells us that we had 1 value returned. For longer or more complex output, it is numbered like this to make it easier to gauge the size of the output.

The nice thing is that you can combine data into variables and then use operations on those variables. If we for example give the variable `small` the value 3 and then give the variable `bigger` the value 11 - we can add these two up.

```r
small <- 3
bigger <- 11

small + bigger

[1] 14
```

.. and get the result 14 back.

Variables are a representation of something - in this case just two numbers. One of the more difficult things in R, and programming in general, is to come up with short but descriptive variable names.

Many programming languages use the equals sign to assign variables, but the convention in R is to use an arrow to assign variables, this is not a special character - simply type the smaller-than symbol followed by a dash on your keyboard.

#### \[Chime\] - Use an arrow to assign a variable with information/data.

That little chime will highlight important concepts throughout this video, if you're taking notes - those are the things you should write down and make sure to commit to memory.

Now, when R gets really powerful is when combining numbers into larger variables or lists. We can then use built in functions to perform calculations on many data points at once. Probably the most common built in function in R is `c()`. C stands for combine and is used to combine single data points into a list.

A function in R is always followed by a parenthesis. Inside this parenthesis is where the function receives its inputs. Different functions will take different inputs.

#### \[Chime\] - A function in R is followed by a parenthesis, in which the function takes its inputs.

The inputs to the function `c()` is whatever we want to combine into a variable.

We can for example write:

```r
a <- c(3,4,5,6)
```

to create the variable `a` with four data points, the values 3, 4, 5 and 6.

We can access data points in a variable by referring to their index, their position in the variable, with a square bracket. If we write `a[1]`, we refer to the first value in the variable `a`

```r
a[1]

[1] 3
```

In our case here, the number three. And - we can also use this to perform any operation we want, say for example we want to add the first and second value of the variable a, we then type:

```r
a[1] + a[2]

[1] 7
```

.. and get back 7.

Importantly, indexing in R starts at 1 - the first value in a variable has the index 1. In some other programming languages, like Python, index start at 0. These are just different conventions, but can be a source of confusion when you first get in to writing code.

---

Now, if we have some data - say we measured how many centimeters tall some of or colleagues are, we can put this data in a variable that we name `tall` we can type this in as:

```r
tall <- c(167, 153, 187, 202, 173, 172)
```

We can now use different built in functions to get some descriptives of our data. Commonly we are interested in how much data we have, the mean value of our data, and its standard deviation. We can start finding this out by using the function `length()` for getting information on the length of our variable, meaning how many values it's containing.

```r
length(tall)

[1] 6
```

We see that it holds `6` values so we have six observations in our variable.

If we type:

```r
mean(tall)

[1] 175.6667
```

returns `175.6667`, which is the average height of the people in our data.

Typing:

```r
sd(tall)

[1] 16.91942
```

We see our standard deviation is `16.91942`, which is a measure of how spread out our observations are from the mean, a measurement of or datas distribution.

---

Now, the point with R is that you can write an analysis script for your data. This makes your analysis 100% transparent and reproducible. Basically, this means writing down all the functions and processing steps in a text file that can be executed with R.

To simplify this, there are different programs called _Integrated Development Environment,_ or IDEs, available to facilitate writing code. Popular examples of these are Rstudio for writing R scripts, or VScode for a general-purpose code editor. For data science using the Python language, Spyder is a popular IDE.

Using an IDE lets you browse through variables, view plots, figures and tables and test-run code to build up your analysis piece by piece.

In this video, we'll be using the IDE _Positron_ developed by Posit, which is freely available to download from https://positron.posit.co/

> Video of download + installation process

Importantly, you must first have R installed before you can use it with Positron. Remember, R is the programming language, Positron is an editor you can use to write, edit and execute R code in.

You download and install R from _https://cloud.r-project.org/_

> Open Positron

Having installed R and Positron, the first action I recommend is to go to File -> Preferences -> Themes -> Color theme and selected a dark mode color theme. It's a bit nicer on your retinas.

From this "welcome tab" you can create a new project folder or open a folder for an existing projects. Specify the name of your project folder and where on your computer you want to keep your project folder, which version of R should be used, and open the project in the positron window you have open.

In the standard setup, Positrons workspace is divided in five different sections, but this is highly customizable depending on what you want to see and where.

1. On the bottom middle of the screen you have the exact same R console that we were manually typing code in previously.
2. To the left is the explorer that shows you what files are available in your project folder. Currently it is empty.
3. In the upper middle of the screen is an empty script file.
4. To the upper right, when the session tab is selected we see what variables we have in the current session (right now none) and below that is an area that will display any plots that we create.

Most of our work will be done in the script in the middle. If we type in our same data from before, 6 measurements of how tall our colleagues are

```r
a <- c(3,4,5,6)
```

We execute this line of code, the line where our cursor is located, by pressing `Ctrl + Enter` on Windows or `Cmd + Enter` on Mac. This will run the line of code and we can see in the console below that R has executed the line.

Because we have created a variable `a`, we can now see it in the "Variables" tab to the right.

Obviously, we can't be typing our data in manually. Instead, we typcically load our data from a file. Commonly a .csv file, a text file where data is organized in rows and columns, with each column separated by a comma.

I create a subfolder in the project folder and call it "data" and then copy a sample dataset stored as questionnaire_data.csv into a sub the project folder.

Positron comes with a built in data viewer that makes it easy to inspect data files by just double clicking them in the file explorer. Doing that we see that this file has 120 rows, or observations and 17 columns, or variables.

The data was collected as an online survey of staff and students at a university and contain information on

- Age
- Sex
- How they found survey (survey)
- Their position at the university (position)
- How long they have worked/studied at the university (TimeHere)
- How many hours they sleep an average night (sleep)
- How many hours of screen time they have per day (screen_time)
- 5 separate items from the WHO-5 well-being questionnaire (WHO-5)
- 4 separate items from the Perceived Stress questionnaire (PSQ-4)

To import this data into R, we use the built in function `read.csv()`, which reads a .csv file as its input and creates a data frame from it. A data fram is the standard data format in R, which is basically a table where each column is a variable and each row is an observation.

Similar to before, we assign the output of this function to a variable, which we can call `data`.

Note that because the file is in a subfolder called "data", we need to specify the path to the file relative to where we are running the script from, relative to our working directory. In this case, we need to specify the folder "data/" before the file name.

You can check what your working directory is by typing `getwd()` in the console. If we wanted to make sure we can read the file wherever we run the script from, we could use an absolute path, something like "C:/Users/YourName/Path/To/Project/data/questionnaire_data.csv". But that would make the script less portable, that is - it would only work on the specific computer where that path exists.

Now that we have read in our data, the data frame shows up as a variable and we can click it to inspect it in the data viewer.



Getting started with R, all the different functions available may seem overwhelming. The goal is not to memorize functions, the most common ones will become familiar with practical experience. Rather, you should start by laying out the different steps required to go from raw data to result - the endpoint can be either a statistical result or a visualization. Personally I like to ask

"what plot or figure would best answer this research question?"

WIP notes:

\*\* functions in functions - round() - and: function options + ?

round() ?
