.. _closures:

##############################
Closures and Function Currying
##############################

Defining specialized functions on the fly.

A "Closure" is a fancy CS term that can be very hard to understand. Partly because they are expressed a little differently in every computer language that supports them But this is easiest definition I could find:

    Closure is when a function “remembers” its lexical scope even when the function is executed outside that lexical scope

This definition is provided by Kyle Simpson
(by way of `an article about closures in Javascript <https://medium.com/beginners-guide-to-mobile-web-development/closures-in-functional-programming-and-javascript-3ed730e08fc2>`_).

The basic idea behind the concept of a closure lies in the understanding of the fact that closure is a mechanism by which an inner function will have access to the variables defined in its outer function’s lexical scope even after the outer function has returned.

Which brings us to the key practical part of how this works in Python:


Scope
=====

In order to get a handle on all this, it's important to understand variable scoping rules in Python.

"Scope" is the word for `where` the names in your code are accessible. Another word for a scope is namespace.

Global Scope
------------

The simplest is the global scope. This is where all the names defined right in your code file (module) are. When running in an interactive interpreter,  it is in the global namespace as well.

You can get the global namespace with the ``globals()`` function, but ...

The Python interpreter defines a handful of names when it starts up, and iPython defines a whole bunch more.
Recall that a convention in Python is that names that start with an underscore are "special" in some way -- double underscore names have a special meaning to Python, and single underscore names are considered "private".
Most of the extra names defined by the Python interpreter or iPython that are designed for internal use start with an underscore. These can really "clutter up" the namespace, but they can be filtered out for a more reasonable result:

.. code-block:: python

    def print_globals():
        ipy_names = ['In', 'Out', 'get_ipython', 'exit', 'quit']
        for name in globals().keys():
            if not (name.startswith("_") or name in ipy_names):
                print(name)

Try running that in a newly started interpreter:

.. code-block:: ipython

    In [3]:     def print_globals():
       ...:         ipy_names = ['In', 'Out', 'get_ipython', 'exit', 'quit']
       ...:         for name in globals().keys():
       ...:             if not (name.startswith("_") or name in ipy_names):
       ...:                 print(name)
       ...:

    In [4]: print_globals()
    print_globals

The only name left is "print_globals" itself -- created when we defined the function.

.. note:: Try running ``globals()`` by itself to see all the cruft iPython adds. Also note that ``globals`` returns not just the names, but a dictionary, where the keys are the names, and the items are the values bound to those names.

If we add a name or two, they show up in the global scope:

.. code-block:: ipython

    In [6]: x = 5

    In [7]: this = "that"

    In [8]: print_globals()
    print_globals
    x
    this

names are created by assignment, and by ``def`` and ``class`` statements. We already saw a ``def``, here is a ``class`` definition.

.. code-block:: ipython

    In [11]: class TestClass:
        ...:     pass
        ...:

    In [12]: print_globals()
    print_globals
    x
    this
    test
    TestClass

Always keep in mind that in Python, "global" means "global to the module", *not* global to the entire program. In the case of the interactive interpreter, the module is the "__main__" module (remember ``if __name__ == __main__:``?). But in a particular python file (usually one file is one module), the global scope is global to that one file.


Local Scope
-----------

So that's the global scope -- what creates a new scope?

A new, "local" scope is created by a function or class definition:

There is a built-in function to get the names in the local scope, too, so we can use it to show us the names in a function's local namespace. There isn't a lot of cruft in the local namespace, so we don't need a special function to print it.

Note that ``locals()`` and ``globals()`` returns a dict of the names and the objects they are bound to, so we can print the keys to get the names:

.. code-block:: ipython

    In [15]: def test():
    ...:     x = 5
    ...:     y = 6
    ...:     print(locals().keys())
    ...:

    In [16]: test()
    dict_keys(['y', 'x'])

When a function is called, it creates a clean local namespace.

Similarly a class definition does the same thing:

.. code-block:: ipython

    In [18]: class Test:
        ...:     this = "that"
        ...:     z = 54
        ...:     def __init__(self):
        ...:         pass
        ...:     print(locals().keys())
        ...:
    dict_keys(['__module__', '__qualname__', 'this', 'z', '__init__'])

Interesting -- that print statement ran when the class was defined...

But you see that class attributes are there, as is the ``__init__`` function.

So each function gets a local namespace (or scope), and so does each class. And it follows that each method (function) in the class gets its own namespace as well.

Turns out that this holds true for functions defined within functions also:

.. code-block:: ipython

    In [23]: def outer():
        ...:     x = 5
        ...:     y = 6
        ...:     def inner():
        ...:         w = 7
        ...:         z = 8
        ...:         print("inner scope:", locals().keys())
        ...:     print("outer scope:", locals().keys())
        ...:     inner()

    In [24]: outer()
    outer scope: dict_keys(['inner', 'y', 'x'])
    inner scope: dict_keys(['z', 'w'])

Function Parameters
-------------------

The other way you can define names in a function's local namespace is with function parameters:


.. code-block:: ipython

    In [14]: def fun_with_parameters(a, b=0):
        ...:     print("local names are:", locals().keys())
        ...:
        ...:

    In [15]: fun_with_parameters(4)
    local names are: dict_keys(['a', 'b'])

Notice that no other names have been defined in the function, but both of the parameters (positional and keyword) are local names.


Finding Names
-------------

At any point, there are multiple scopes in play: the local scope, and all the surrounding scopes.
When you use a name, python checks in the local scope first, then moves out one by one until it finds the name.
If you define a new name inside a function, it "overrides" the name in any of the outer scopes.
But any names not defined in an inner scope will be found by looking in the enclosing scopes.

.. code-block:: ipython

    In [33]: name1 = "this is global"

    In [34]: name2 = "this is global"

    In [35]: def outer():
        ...:     name2 = "this is in outer"
        ...:     def inner():
        ...:         name3 = "this is in inner"
        ...:         print(name1)
        ...:         print(name2)
        ...:         print(name3)
        ...:     inner()
        ...:

    In [36]: outer()
    this is global
    this is in outer
    this is in inner

Look carefully to see where each of those names came from. All the print statements are in the inner function, so its local scope is searched first, and then the outer function's scope, and then the global scope. ``name1`` is only defined in the global scope, so that one is found. but ``name2`` is redfined in the scope of the ``outer`` function, so that one is found. And ``name3`` is only defined in the ``inner`` function scope.

The ``global`` keyword
----------------------

Global names can be accessed from within functions, but not if that same name is created in the local scope. So you can't change an immutable object that is outside the local scope:

.. code-block:: ipython

    In [37]: x = 5

    In [38]: def increment_x():
        ...:     x += 5
        ...:

    In [39]: increment_x()
    ---------------------------------------------------------------------------
    UnboundLocalError                         Traceback (most recent call last)
    <ipython-input-39-c9a57e8c0d14> in <module>()
    ----> 1 increment_x()

    <ipython-input-38-dc4f30fe2ac4> in increment_x()
          1 def increment_x():
    ----> 2     x += 5
          3

    UnboundLocalError: local variable 'x' referenced before assignment

The problem here is that ``x += 5`` is the same as ``x = x + 5``, so it is creating a local name, but it can't be incremented, because it hasn't had a value set yet.

How does the interpreter know that ``x`` is a local name? When it compiles the function definition, it marks all the names assigned in the function as local. So when the function runs, it knows that ``x`` is local, and thus it won't go look in the global scope for it.

The ``global`` keyword tells python that you want to use the global name, rather than create a new, local name:

.. code-block:: ipython

    In [40]: def increment_x():
        ...:     global x
        ...:     x += 5
        ...:
        ...:

    In [41]: increment_x()

    In [42]: x
    Out[42]: 10

**NOTE:** The use of ``global`` is frowned upon -- having global variables manipulated in arbitrary other scopes makes for buggy, hard to maintain code! You hardly ever need to use ``global`` -- if a function needs to manipulate a value, you should pass that value into the function, or have it return a value that can then be used to change the global name.


``nonlocal`` keyword
--------------------

The other limitation with ``global`` is that there is only one global namespace. What if you are in a nested scope, and want to get at the value outside the current scope, but not all the way up at the global scope:

.. code-block:: ipython

    In [1]: x = 5

    In [2]: def outer():
       ...:     x = 10
       ...:     def inner():
       ...:         x += 5
       ...:     inner()
       ...:     print("x in outer is:", x)

That's not going to work as the inner x hasn't been initialized:

``UnboundLocalError: local variable 'x' referenced before assignment``

But if we use ``global``, we'll get the global ``x``:

.. code-block:: ipython

    In [4]: def outer():
       ...:     x = 10
       ...:     def inner():
       ...:         global x
       ...:         x += 5
       ...:     inner()
       ...:     print("x in outer is:", x)
       ...:

    In [5]: x
    Out[5]: 5

    In [6]: outer()
    x in outer is: 10

    In [7]: x
    Out[7]: 10

    In [8]: outer()
    x in outer is: 10

    In [9]: x
    Out[9]: 15

This indicates that the global ``x`` is getting changed, but not the one in the ``outer`` scope.

This is enough of a limitation that Python 3 added a new keyword: ``nonlocal``.
What it means is that the name should be looked for outside the local scope, but only as far as you need to go to find it:

.. code-block:: ipython

    In [10]: def outer():
        ...:     x = 10
        ...:     def inner():
        ...:         nonlocal x
        ...:         x += 5
        ...:     inner()
        ...:     print("x in outer is:", x)
        ...:

    In [11]: outer()
    x in outer is: 15

So the ``x`` in the ``outer`` function scope is the one being changed.

While using ``global`` is discouraged, ``nonlocal`` is safer -- as long as it is referring to a name in a scope that is closely defined like the above example. In fact, ``nonlocal`` will not go all the way up to the global scope to find a name:

.. code-block:: ipython

    In [15]: def outer():
        ...:     def inner():
        ...:         nonlocal x
        ...:         x += 5
        ...:     inner()
        ...:     print("x in outer is:", x)
        ...:
      File "<ipython-input-15-fc6f8de72dfc>", line 3
        nonlocal x
        ^
    SyntaxError: no binding for nonlocal 'x' found

But it will go up multiple levels in nested scopes:

.. code-block:: ipython

    In [16]: def outer():
        ...:     x = 10
        ...:     def inner():
        ...:         def inner2():
        ...:             nonlocal x
        ...:             x += 10
        ...:         inner2()
        ...:     inner()
        ...:     print("x in outer is:", x)
        ...:

    In [17]: outer()
    x in outer is: 20


Closures
========

Now that we have a good handle on namespace scope, we can get to see why this is all really useful.

"Closures" is a cool CS term for what is really just defining functions on the fly with some saved state. You can find a "proper" definition here:

`Closures on Wikipedia <https://en.wikipedia.org/wiki/Closure_(computer_programming)>`_

But I have trouble following that, so we'll look at real world examples to get the idea -- it's actually pretty logical, once you have idea about how scope works in Python.


Functions Within Functions
--------------------------

We've been defining functions within functions to explore namespace scope.  But functions are "first class objects" in python, so we can not only define them and call them, but we can assign names to them and pass them around like any other object.

So after we define a function within a function, we can actually return that function as an object:

.. code-block:: python

    def counter(start_at=0):
        count = start_at
        def incr():
            nonlocal count
            count += 1
            return count
        return incr

This looks a lot like the previous examples, but we are returning the function that was defined inside the function. Which means is can be used elsewhere.

What's going on here?
.....................

We have passed the ``start_at`` value into the ``counter`` function.

We have stored it in ``counter``'s scope as a local variable: ``count``

Then we defined a function, ``incr`` that adds one to the value of count, and returns that value.

Note that we declared ``count`` to be nonlocal in ``incr``'s scope, so that it would be the same ``count`` that's in counter's scope.

What type of object do you get when you call ``counter()``?

.. code-block:: ipython

    In [37]: c = counter(start_at=5)

    In [38]: type(c)
    Out[38]: function

So we get a function back -- makes sense. The ``def`` defines a function, and that function is what's getting returned.

Being a function, we can, of course, call it:

.. code-block:: ipython

    In [39]: c()
    Out[39]: 6

    In [40]: c()
    Out[40]: 7

Each time is it called, it increments the value by one -- as you'd expect.

But what happens if we call ``counter()`` multiple times?

.. code-block:: ipython

    In [41]: c1 = counter(5)

    In [42]: c2 = counter(10)

    In [43]: c1()
    Out[43]: 6

    In [44]: c2()
    Out[44]: 11

So each time ``counter()`` is called, a new ``incr`` function is created. Along with the new function, a new namespace is created that holds the ``count`` name. So the new ``incr`` function is holding a reference to that new ``count`` name.

This is what makes it a "closure" -- it carries with it the scope in which it was created (or enclosed - I guess that's where the word closure comes from).

The returned ``incr`` function is a "curried" function -- a function with some parameters pre-specified.

Let's experiment a bit more with these ideas:

:download:`play_with_scope.py <../examples/closures_currying/play_with_scope.py>`

Currying
========

"Currying" is a special case of closures:

`Currying on Wikipedia <https://en.wikipedia.org/wiki/Currying>`_

The idea behind currying is that you may have a function with a number of parameters, and you want to make a specialized version of that function with a couple of parameters pre-set.


Real world Example
------------------

I was writing some code to compute the concentration of a contaminant in a river, as it was reduced by exponential decay, defined by a half-life:

https://en.wikipedia.org/wiki/Half-life

So I wanted a function that would compute how much the concentration would reduce as a function of time -- that is:

.. code-block:: python

    def scale(time):
        return scale_factor

The trick is, how much the concentration would be reduced depends on both time and the half life. And for a given material, and given flow conditions in the river, that half life is pre-determined.  Once you know the half-life, the scale is given by:

.. code-block:: python

  scale = 0.5 ** (time / (half_life))

So to compute the scale, I could pass that half-life in each time I called the function:

.. code-block:: python

    def scale(time, half_life):
        return 0.5 ** (time / (half_life))

But this is a bit klunky -- I need to keep passing that ``half_life`` around, even though it isn't changing. And there are places, like ``map`` that require a function that takes only one argument!

What if I could create a function, on the fly, that had a particular half-life "baked in"?

*Enter Currying* -- Currying is a technique where you reduce the number of parameters that function takes, creating a specialized function with one or more of the original parameters set to a particular value. Here is that technique, applied to the half-life decay problem:

.. code-block:: python

    def get_scale_fun(half_life):
        def half_life_fun(time):
            return 0.5 ** (time / half_life)
        return half_life_fun

**NOTE:** This is simple enough to use a lambda for a bit more compact code:

.. code-block:: python

    def get_scale_fun(half_life):
        return lambda time: 0.5 ** (time / half_life)

Using the Curried Function
..........................

Create a scale function with a half-life of one hour:

.. code-block:: ipython

    In [8]: scale = get_scale_fun(1)

    In [9]: [scale(t) for t in range(7)]
    Out[9]: [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]

The value is reduced by half every hour.

Now create one with a half life of 2 hours:

.. code-block:: ipython

    In [10]: scale = get_scale_fun(2)

    In [11]: [scale(t) for t in range(7)]
    Out[11]:
    [1.0,
     0.7071067811865476,
     0.5,
     0.3535533905932738,
     0.25,
     0.1767766952966369,
     0.125]

And the value is reduced by half every two hours...

And it can be used with ``map``, too:

.. code-block:: ipython

    In [13]: list(map(scale, range(7)))
    Out[13]:
    [1.0,
     0.7071067811865476,
     0.5,
     0.3535533905932738,
     0.25,
     0.1767766952966369,
     0.125]


``functools.partial``
---------------------

The ``functools`` module in the standard library provides utilities for working with functions:

https://docs.python.org/3.5/library/functools.html

Creating a curried function turns out to be common enough that the ``functools.partial`` function provides an optimized way to do it:

What ``functools.partial`` does is:

 * Makes a new version of a function with one or more arguments already filled in.
 * The new version of a function documents itself.

Example:

.. code-block:: python

    def power(base, exponent):
        """returns based raised to the give exponent"""
        return base ** exponent

Simple enough. but what if we wanted a specialized ``square`` and ``cube`` function?

We can use ``functools.partial`` to *partially* evaluate the function, giving us a specialized version:

.. code-block:: python

    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)











