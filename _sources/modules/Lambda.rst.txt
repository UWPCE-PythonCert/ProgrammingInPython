.. _anonymous_functions:

###########################
Anonymous Functions: Lambda
###########################

The ``lambda`` keyword is a way to create a function on the fly, without giving it a name. Hence the term "anonymous" -- it has no name.

Using ``lambda``
================

Structure
---------

"lambda" is a keyword -- it can not be used as a variable name, etc. A lambda expression looks like:

.. code-block:: python

  lambda <parameters> : <expression>

It is an expression -- which means it evaluates to a value -- which means that it can be assigned to a variable, put in a container (such as a list or dict) etc.

The parameters are just like function parameters -- but without the parentheses. And they exist in the local scope of the lambda, and can thus be used in the expression.

The expression can be any expression using global variables or the parameters -- but not a statement -- anyone remember what the difference is?

An expression is something that evaluates to a value, and can be assigned to a variable etc. but things like ``for`` and ``while`` loops and ``if...else`` structures are NOT expressions, and thus can't be put in a lambda.

In short, lambda is only for very simple functions with no real flow control.

Example
-------

.. code-block:: ipython

    In [1]: f = lambda x, y: x + y

    In [2]: f(3,4)
    Out[2]: 7

This creates a function that takes two positional parameters, ``x`` and ``y``, and returns their sum.

This is ALMOST the same as:

.. code-block:: ipython

    In [3]: def f2(x, y):
       ...:     return x + y

    In [4]: f2(3,4)
    Out[4]: 7

So what is the difference? Well, ``lambda`` creates an "anonymous" function -- it doesn't have a name:

.. code-block:: ipython

    In [10]: f.__name__
    Out[10]: '<lambda>'

All lambda functions are called <lambda>. But:

.. code-block:: ipython

    In [11]: f2.__name__
    Out[11]: 'f2'

Regular "def" defined functions know their name.

So ``lambda`` creates a function, but it doesn't have a name, and it can only have a single expression in it -- no flow control.

What's the point?
-----------------

There is nothing you can do with lambda that you can't do with regular ``def`` functions. But there are times when you just need a simple quick function that you don't need to keep around or refer to again -- so it's a handy syntax for these situations.

A sorting key function is a great example:

.. code-block:: ipython

    In [55]: lst = [("Chris","Barker"), ("Fred", "Jones"), ("Zola", "Adams")]

    In [56]: lst.sort()

    In [57]: lst
    Out[57]: [('Chris', 'Barker'), ('Fred', 'Jones'), ('Zola', 'Adams')]

Tuples are sorted, be default, by their first element. But what if you wanted to sort by the second (index 1) element -- last name in this case:

.. code-block:: ipython

    In [13]: def sort_key(item):
        ...:     return item[1]
        ...:

    In [14]: lst.sort(key=sort_key)

    In [15]: lst
    Out[15]: [('Zola', 'Adams'), ('Chris', 'Barker'), ('Fred', 'Jones')]

straightforward enough. But kind a lot of extra code, eh? and now there is this function: "sort_key" hanging around. You could delete it: ``del sort_key``, but that would be even more code.

But with a lambda, you simply define it inline:

.. code-block:: ipython

    In [16]: lst = [("Chris","Barker"), ("Fred", "Jones"), ("Zola", "Adams")]

    In [17]: lst.sort(key=lambda x: x[1])

    In [18]: lst
    Out[18]: [('Zola', 'Adams'), ('Chris', 'Barker'), ('Fred', 'Jones')]

Nice and compact and clear, with no extra names hanging around.

You'll find them useful with things like ``map``, ``filter``, and ``reduce``. as well.


Functions as first class objects
================================

lambda functions are python objects; they can be stored in a list or other container:

.. code-block:: ipython

    In [7]: l = [lambda x, y: x+y]
    In [8]: type(l[0])
    Out[8]: function


And you can call it by indexing the container:

.. code-block:: ipython

    In [9]: l[0](3,4)
    Out[9]: 7

You can do that with "regular" functions too:

.. code-block:: ipython

    In [12]: def fun(x,y):
       ....:     return x+y
       ....:
    In [13]: l = [fun]
    In [14]: type(l[0])
    Out[14]: function
    In [15]: l[0](3,4)
    Out[15]: 7

If the goal is to have that little function in the list, and you don't need to give it a name and/or reference it anywhere else, then lambda is a cleaner way to do it.

lambda and keyword arguments
----------------------------

lambda functions can take keyword arguments as well:

.. code-block:: ipython

    In [20]: (lambda x=None: x * 2)(x=4)
    Out[20]: 8

Remember that default arguments get evaluated when the function is defined. This is the case with lambda as well.  This can get you in trouble if you use a mutable in a function definition. But it also can be a handy way to "bake in" a value into a function to be used later:

.. code-block:: ipython

    In [186]: l = []
    In [187]: for i in range(3):
        l.append(lambda x, e=i: x**e)

This creates a list, in this case with three items. Each of those items is a function. Note that the lambda is called each time through the loop, so each one has that default parameter defined separately -- and each time the default is set to the current value of ``i`` in the loop. So we get three functions, all the same except for the default value of ``e`` -- that is, each function will raise the input value to a different power.

We can loop through that list, and call each function in turn with the same input value:

.. code-block:: ipython

    In [25]: for f in func_list:
        ...:     print(f(2))
        ...:
    1
    2
    4
    8

and presto! 2 raised to the zeroth, then first, the second, ... power.

This may seem pretty obscure, but it's a handy way to auto-generate custom functions on the fly -- like for GUI callbacks, for instance:

https://wiki.wxpython.org/Passing%20Arguments%20to%20Callbacks





