.. _dict_as_switch:

################################
Using a Dictionary to ``switch``
################################

Python does not have a ``switch/case statement``.  Why not?

https://www.python.org/dev/peps/pep-3103/

So what to use instead of "switch-case"?

``switch`` / ``case``
=====================

What is ``switch``?
-------------------

Many languages have a "switch-case" construct::

    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };

How do you say this in Python?

``if-elif`` chains
------------------

The obvious way to say it is a chain of ``elif`` statements:

.. code-block:: python

    if argument ==  0:
        return "zero"
    elif argument == 1:
        return "one"
    elif argument == 2:
        return "two"
    else:
        return "nothing"

And there is nothing wrong with that, but....

dict as switch
--------------

The ``elif`` chain is neither elegant nor efficient. There are a number of ways to say it in python -- but one elegant one is to use a dict:

.. code-block:: python

    arg_dict = {0:"zero", 1:"one", 2: "two"}
    arg_dict.get(argument, "nothing")

Simple, elegant and fast.

You can do a dispatch table by putting functions as the value.

Example: The mailroom2 solution.

Switch with functions
---------------------

What would this be like if you used functions instead? Think of the possibilities.

.. code-block:: ipython

    In [11]: def my_zero_func():
        return "I'm zero"

    In [12]: def my_one_func():
        return "I'm one"

    In [13]: switch_func_dict = {
        0: my_zero_func,
        1: my_one_func,
    }

    In [14]: switch_func_dict.get(0)()
    Out[14]: "I'm zero"

Again, fast and efficient.

This is possible because functions are "first class objects" in Python.

OO switch/case
--------------

Another way to do the equivalent of switch / case is subclassing.

If you haven't learned about classes in Python this will be pretty confusing. But here's a high level overview:

In C, before C++, a common idiom was something like::

    switch(object_type) {
        case circle:
            draw_a_circle();
        case square:
            draw_a_square();
        case polygon:
            draw_a_polygon();
        default:
            draw_nothing();
    };

That is, a different function is called depending on what type of "thing" you are dealing with.

This is actually a really common idiom in C. And even in modern OO code written by old C developers -- I had a developer on my team do exactly this in a program we were working on. It was a map drawing program (written in Python), and there was code all over it like::

    if layer.type == "tiles":
        do_something_with_tiles
    elif layer.type == "grid":
        do_somethign_with_grid

This was a maintainability nightmare -- if you added a new layer type, you had to find every one of these constructs and add another ``elif`` block to it.

The OO way
----------

With object oriented programming, you can "subclass" objects, and use "polymorphism" to achieve this kind of selection. Say you have a bunch of objects you want to be able to draw. Give each of them a ``draw()`` method, and then the above switch statement becomes:

the_object.draw()

That's IT!

You don't have to test to see which type of object it is, you only have to know that it knows how to draw itself.

Now when you add a new object type -- all you need to do is make sure it has a draw() method (and other needed methods) and then all the other code will know how to use it without your changing anything.
