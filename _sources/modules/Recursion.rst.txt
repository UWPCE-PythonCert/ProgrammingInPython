#########
Recursion
#########

You've seen functions that call other functions.

If a function calls *itself*, we call that **recursion**

Like with other functions, a call within a call establishes a *call stack*

With recursion, if you are not careful, this stack can get *very* deep.

Python has a maximum limit to how much it can recurse. This is intended to
save your machine from running out of RAM.

Recursion is especially useful for a particular set of problems.

For example, take the case of the *factorial* function.

In mathematics, the *factorial* of an integer is the result of multiplying that
integer by every integer smaller than it down to 1.

::

    5! == 5 * 4 * 3 * 2 * 1

We can use a recursive function nicely to model this mathematical function:

::

  1! = 1
  2! = 2 * 1  =  2 * 1!
  3! = 3 * 2 * 1 = 3 * 2!

So we have a pattern here -- each value can be defined in terms of the previous value.

So generically::

  1! = 1
  n! = n * (n-1)!

How would we put that in code? Pretty straightforward translation:

.. code-block:: python

    def factorial(n):
        return n * factorial(n-1)

That was pretty easy -- what happens when we run it?

.. code-block:: ipython

    In [2]: factorial(3)
    ---------------------------------------------------------------------------
    RecursionError                            Traceback (most recent call last)
    <ipython-input-2-3fd9b1939623> in <module>()
    ----> 1 factorial(3)

    <ipython-input-1-5ff805d50ea6> in factorial(n)
          1 def factorial(n):
    ----> 2     return n * factorial(n-1)

    ... last 1 frames repeated, from the frame below ...

    <ipython-input-1-5ff805d50ea6> in factorial(n)
          1 def factorial(n):
    ----> 2     return n * factorial(n-1)

    RecursionError: maximum recursion depth exceeded

OOPS! that didn't work -- why not? Let's add a print...

.. code-block:: python

    def factorial(n):
        print("factorial called with", n)
        return n * factorial(n-1)

And call it:

.. code-block:: ipython

    In [5]: factorial(3)
    factorial called with 3
    factorial called with 2
    factorial called with 1
    factorial called with 0
    factorial called with -1
    factorial called with -2
    factorial called with -3
    factorial called with -4
    factorial called with -5
    ...
    <ipython-input-3-54c2cb2bf478> in factorial(n)
          1 def factorial(n):
          2     print("factorial called with", n)
    ----> 3     return n * factorial(n-1)

    RecursionError: maximum recursion depth exceeded while calling a Python object

Now it's clear what's going on -- each time you call the function, it calls itself with a value one less -- but then it just keeps going into the deep negative numbers, and only stops because Python reaches its recursion limit.

This makes clear a core requirement of recursive functions:

 **Recursive functions must have a termination criteria!**

That is, there must be a case (or more than one) for which they return a direct value. What should that be for factorial? Well, it's part of the definition that 1! == 1 -- so let's put that in our function:

.. code-block:: python

    def factorial(n):
        print("factorial called with", n)
        if n == 1:
            return 1
        return n * factorial(n-1)

and try that:

.. code-block:: ipython

    In [7]: factorial(3)
    factorial called with 3
    factorial called with 2
    factorial called with 1
    Out[7]: 6

Much better!  Try it out now with various values, and maybe without the print:

.. code-block:: ipython

    In [14]: factorial(1)
    Out[14]: 1

    In [15]: factorial(2)
    Out[15]: 2

    In [16]: factorial(3)
    Out[16]: 6

    In [17]: factorial(4)
    Out[17]: 24

Looking good!

Exercise for the reader: What happens if you pass in a negative number?
Think about it first, before you try it. Hint -- it won't work!
How would you change your code to make it more robust?

Summary
-------

* Whenever you have a function that can be defined in terms of itself, you have a use case for recursion.  It can make for nice compact, clear code.

* Python will create a new "stack frame" for each call to the function -- so each call is kept separate, with separate local variables.

But:

* Python has a limited recursion depth -- so it can't be used for "big" problems.

* You do need to make sure the calls will terminate.
