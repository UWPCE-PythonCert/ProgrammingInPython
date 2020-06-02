.. _exercise_fibonacci:

*************************
Fibonacci Series Exercise
*************************

Computing the Fibonacci and Lucas Series
========================================

Goal:
-----

The `Fibonacci Series`_ is a numeric series starting with the integers 0 and 1.

In this series, the next integer is determined by summing the previous two


This gives us::

    0, 1, 1, 2, 3, 5, 8, 13, ...

.. note: 0+1 is 1; 1+1 is 2; 1+2 is 3; 2+3 is 5; 3+5 is 8; and so on forever...

We will write a function that computes this series -- then generalize it.

.. _Fibonacci Series: http://en.wikipedia.org/wiki/Fibbonaci_Series

Step 1
------

* Create a new module ``series.py`` in the ``lesson02`` folder in your student folder.

  - In it, add a function called ``fibonacci``.

  - The function should have one parameter ``n``.

  - The function should return the ``nth`` value in the fibonacci series (starting with zero index).

* Ensure that your function has a well-formed ``docstring``

Note that the fibonacci series is naturally recursive -- the value is
defined by previous values:

fib(n) = fib(n-2) + fib(n-1)


Lucas Numbers
--------------

The `Lucas Numbers`_ are a related series of integers that start with the
values 2 and 1 rather than 0 and 1. The resulting series looks like this::

    2, 1, 3, 4, 7, 11, 18, 29, ...

.. _Lucas Numbers: http://en.wikipedia.org/wiki/Lucas_number


In your ``series.py`` module, add a new function ``lucas`` that returns the
``nth`` value in the *lucas numbers* series (starting with zero index).

Ensure that your function has a well-formed ``docstring``

YOu should find it's *very* similar to the ``fibonacci()`` function.

Generalizing
------------

Both the *fibonacci series* and the *lucas numbers* are based on an identical formula:

fib(n) = fib(n-2) + fib(n-1)

That's why the code is so similar.

This formula creates a class of series that are all related -- each with a different two starting numbers.

Add a third function called ``sum_series`` that can compute all of these related series.

It should have one required parameter and two optional parameters.
The required parameter will determine which element in the
series to print.
The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the *fibonacci series* (because 0 and 1 are the defaults).

Calling it with the optional arguments 2 and 1 will
produce values from the *lucas numbers*.

Other values for the optional parameters will produce other series.

**Note:** While you *could* check the input arguments, and then call one
of the functions you wrote, the idea of this exercise is to make a general
function, rather than one specialized. So you should re-implement the code
in this function.

In fact, you could go back and re-implement your fibonacci and lucas
functions to call ``sum-series`` with particular arguments.

Ensure that your function has a well-formed ``docstring``

Tests...
--------

Add a block of code to the end of your ``series.py`` module.
Use the block to write a series of ``assert`` statements that
demonstrate that your three functions work properly.

Use comments in this block to inform the observer what your tests do.

We have created a template for you to use to clarify what we mean by these asserts:

:download:`series_template.py <../exercises/series_template.py>`

Add your new module to your personal git repo and commit frequently while working on your implementation.
Include good commit messages that explain concisely both *what* you are doing and *why*.

When you are finished, push your changes to your fork of the class repository in GitHub and make a pull request.

