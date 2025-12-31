In this video, you will learn how to go from a raw data table like this \[on screen\] to a result report like this \[on screen\] using the R programming language for statistical computing.

Firstly R is the programming language and there are plenty of ways to interact with it. The most basic is in a command window or terminal like this.

> *Open command window*

Essentially R is a calculator and in this command window you can perform different calculations. For example addition, subtraction, multiplication, and division.

``` r
2+3
[1] 5

7-5
[1] 2

4*3
[1] 12

15/3
[1] 5
```

The 1 in brackets that we see before the returned value just tells us that we had 1 value returned. For longer or more complex output it is numbered like this to make it easier to gauge the size of the output.

The nice thing is that you can combine data into variables and then use operations on those variables. If we for example give the variable `small` the value 3 and then give the variable `bigger` the value 11 - we can add these two up.

``` r
small <- 3
bigger <- 11

small + bigger

[1] 14
```

.. and get the result 14 back.

Variables are a representation of something - in this case just two numbers. One of the more difficult things in R, and programming in general, is to come up with short but descriptive variable names.

Many programming languages use the equals sign to assign variables, but the convention in R is to use an arrow to assign variables, this is not a special character - simply type the smaller-than symbol followed by a dash on your keyboard to assign a variable.

#### \[Chime\] - Use an arrow to assign a variable with information/data.

That little chime will highlight important concepts throughout this video, if you're taking notes - those are the things you should write down and make sure to commit to memory.

Now, when R gets really powerful is when combining numbers into larger variables or lists. We can then use built in functions to perform calculations on many data points at once. Probably the most common built in function in R is `c()`. C stands for combine and is used to combine single data points into a list.

A function in R is always followed by a parenthesis. Inside this parenthesis is where the function receives its inputs. Different functions will take different inputs.

#### \[Chime\] - A function in R is followed by a parenthesis, in which the function takes its inputs.

The inputs to the function `c()` is whatever we want to combine into a variable.

We can for example write:

``` r
a <- c(3,4,5,6)
```

to create the variable `a` with four data points, the values 3, 4, 5 and 6.

We can access data points in a variable by referring to their index, their position in the variable, with a square bracket. If we write `a[1]`, we refer to the first value in the variable `a`

``` r
a[1]

[1] 3
```

In our case here, the number three. And - we can also use this to perform any operation we want, say for example we want to add the first and second value of the variable a, we then type:

``` r
a[1] + a[2]

[1] 7
```

.. and get back 7.

Importantly, indexing in R starts at 1 - the first value in a variable has the index 1. In some other programming languages, like Python, index start at 0. These are just different conventions, but can be a source of confusion when you first get in to writing code.

------------------------------------------------------------------------

Now, if we have some data - say we measured how many centimeters tall some of or colleagues are, we can put this data in a variable that we name `tall` we can type this in as:

``` r
tall <- c(167, 153, 187, 202, 173, 172)
```

We can now use different built in functions to get some descriptives of our data. Commonly we are interested in how much data we have, the mean value of our data, and its standard deviation. We can start finding this out by using the function `length()` for getting information on the length of our variable, meaning how many values it is containing.

``` r
length(tall)

[1] 6
```

We see that it holds `6` values so we have six observations in our variable.

If we type:

``` r
mean(tall)

[1] 175.6667
```

returns `175.6667`, which is the average height of the people in our data.

Typing:

``` r
sd(tall)

[1] 16.91942
```

We see our standard deviation is `16.91942`, which is a measure of how spread out our observations are from the mean, a measurement of or datas distribution.

Getting started with R, all the different functions available may seem overwhelming. The goal is not to memorize functions, the most common ones will become familiar with practical experience. Rather, you should start by laying out the different steps required to go from raw data to result - the endpoint can be either a statistical result or a visualization. Personally I like to ask

"what plot or figure would best answer this research question?"

WIP notes:

\*\* functions in functions - round() - and: function options + ?

round() ?