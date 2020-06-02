.. _more_on_functions:

More on Functions
=================

From the materials you have covered up to this point you should have mastered the basics of writing functions.

In particular, you know that functions can contain a chunk of code that can be written once, and used multiple times from other parts of the code.

You know that you can pass values into the function, and that it can return values to the "calling" code.

Now we will dig a bit deeper down into the specifics of functions in Python:

Variable scope
--------------

Defining a function:

.. code-block:: python

    def fun(x, y):
        z = x + y
        return z

``x``, ``y``, ``z`` are *local* names.

``x`` and ``y`` because they are function *parameters*

``z`` because it was "bound" inside the function.


Local vs. Global
----------------

Names bound in Python have a *scope*

That *scope* determines where a symbol is visible, and what value it has in a
given block.

.. code-block:: ipython

    In [14]: x = 32
    In [15]: y = 33
    In [16]: z = 34
    In [17]: def fun(y, z):
       ....:     print(x, y, z)
       ....:
    In [18]: fun(3, 4)
    32 3 4

``x`` is global, while ``y`` and ``z`` are local to the function.

But, did the value of ``y`` and ``z`` change in the *global* scope?

.. code-block:: ipython

    In [19]: y
    Out[19]: 33

    In [20]: z
    Out[20]: 34

No -- they did not. The "y" and "z" names *inside* the function are completely separate from the "y" and "z" outside the function.

The ones outside the function are "global" names.

**NOTE:** "global" in Python means global to the module (generally a single file), not global to an entire program. Which is really good, as you have little way of knowing what names are being used in packages you are using, but are not writing yourself!

In general, you should use global names mostly for constants.

The Python convention is to designate global constants by typing the
names we bind to them in ALL_CAPS:

.. code-block:: python

    INSTALLED_APPS = ['foo', 'bar', 'baz']
    CONFIGURATION_KEY = 'some secret value'
    ...

This is just a convention, but it's a good one to follow.


Global Gotcha
-------------

Take a look at this function definition:

.. code-block:: ipython

    In [21]: x = 3

    In [22]: def f():
       ....:     y = x
       ....:     x = 5
       ....:     print(x)
       ....:     print(y)
       ....:

What is going to happen when we call ``f``?


Try it and see:

.. code-block:: ipython

    In [34]: f()
    ---------------------------------------------------------------------------
    UnboundLocalError                         Traceback (most recent call last)
    <ipython-input-34-0ec059b9bfe1> in <module>()
    ----> 1 f()

    <ipython-input-33-4363b2b69f73> in f()
          1 def f():
    ----> 2     y = x
          3     x = 5
          4     print(x)
          5     print(y)

    UnboundLocalError: local variable 'x' referenced before assignment

Because you are binding the symbol ``x`` locally, it becomes a local and masks
the global value already bound. So in the line that caused the error:

.. code-block:: python

    y = x

Python knows that x is a local name, as it is assigned on the next line.  But on this line,  x has not yet been given a value -- hence the error.


Parameters
----------

So far we've seen simple parameter lists:

.. code-block:: python

    def fun(x, y, z):
        print(x, y, z)

These types of parameters are called *positional*

When you call a function, you **must** provide arguments for all *positional*
parameters *in the order they are listed*.

You can provide *default values* for parameters in a function definition:

.. code-block:: ipython

    In [24]: def fun(x=1, y=2, z=3):
       ....:     print(x, y, z)
       ....:

When parameters are given with default values, they become *optional*.

.. code-block:: ipython

    In [25]: fun()
    1 2 3

You can provide arguments to a function call for *optional* parameters
positionally:

.. code-block:: ipython

    In [26]: fun(6)
    6 2 3
    In [27]: fun(6, 7)
    6 7 3
    In [28]: fun(6, 7, 8)
    6 7 8

Or, you can use the parameter name as a *keyword* to indicate which you mean:

.. code-block:: ipython

    In [29]: fun(y=4, x=1)
    1 4 3

Once you've provided a *keyword* argument in this way, you can no longer
provide any *positional* arguments:

.. code-block:: ipython

    In [30]: fun(x=5, 6)
      File "<ipython-input-30-4529e5befb95>", line 1
        fun(x=5, 6)
    SyntaxError: non-keyword arg after keyword arg

Recursion
---------

You've seen functions that call other functions.

If a function calls *itself*, we call that **recursion**.

Like with other functions, a call within a call establishes a *call stack*.

With recursion, if you are not careful, this stack can get *very* deep.

Python has a maximum limit to how much it can recurse. This is intended to
save your machine from running out of RAM.

Recursion can be Useful
-----------------------

Recursion is especially useful for a particular set of problems.

For example, take the case of the *factorial* function.

In mathematics, the *factorial* of an integer is the result of multiplying that integer by every integer smaller than itself down to 1.

::

    5! == 5 * 4 * 3 * 2 * 1

We can use a recursive function nicely to model this mathematical function:

.. code-block:: python

  def fact(n):
      """compute the factorial of the input value, n"""
      if n == 0:
          return 1
      else:
          return n * fact(n-1)

This is a typical structure for a recursive function:

A) It starts with a check to see if the recursive process is "done" -- can it simply return a simple value.

B) If not, then it does a computation using the same function with another value.

It is critical that the first check is there, or the function will never terminate.

Further Reading
---------------

Here's a nice blog post about writting better functions:

https://jeffknupp.com/blog/2018/10/11/write-better-python-functions/




