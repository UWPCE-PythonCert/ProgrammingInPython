.. _modules_and_namespaces:

#######################################
Code Structure, Modules, and Namespaces
#######################################


.. centered:: **How to get what you want when you want it**


Code Structure
==============

In Python, the structure of your code is determined by whitespace. This is nicely clear, and you've probably already figured it out, but we'll formally spell it out here:

How you *indent* your code determines how it is structured

::

    block statement:
        some code body
        some more code body
        another block statement:
            code body in
            that block
        end of "another" block statement
        still in the first block
    outside of the block statement

The colon that terminates a block statement is also important...

One-liners
----------

You can put a one-liner after the colon:

.. code-block:: ipython

    In [167]: x = 12
    In [168]: if x > 4: print(x)
    12

But this should only be done if it makes your code *more* readable. And that is rare.

So you need both the colon and the indentation to start a new a block.  But the end of the indented section is the only indication of the end of the block.

Spaces vs. Tabs
---------------

Whitespace is important in Python.

An indent *could* be:

* Any number of spaces
* A tab
* A mix of tabs and spaces:

If you want anyone to take you seriously as a Python developer:

.. centered:: **Always use four spaces -- really!** (`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_)

.. note::
  If you *do* use tabs (and really, don't do that!) python interprets them as the equivalent of *eight* spaces.  Text editors can display tabs as any number of spaces, and most modern editors default to four -- so this can be *very* confusing! so again:

.. centered::  **Never mix tabs and spaces in Python code**


Spaces Elsewhere
----------------

Other than indenting -- space doesn't matter, technically.

.. code-block:: python

    x = 3*4+12/func(x,y,z)
    x = 3*4 + 12 /   func (x,   y, z)

These will give the exact same results.

But you should strive for proper style. Isn't this easier to read?

.. code-block:: python

    x = (3 * 4) + (12 / func(x, y, z))


.. centered:: **Read** `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ **and install a linter in your editor.**


Modules and Packages
====================

Python is all about *namespaces* -- the "dots"

``name.another_name``

The "dot" indicates that you are looking for a name in the *namespace* of the given object. It could be:

* A name in a module
* A module in a package
* An attribute of an object
* A method of an object

The only way to know is to know what type of object the name refers to.  But in all cases, it is looking up a name in the namespace of the object.

So what *are* all these different types of namespaces?

Modules
-------

A module is simply a namespace. But a module more or less maps to a file with python code in it.

It might be a single file, or it could be a collection of files that define a shared API.

But in the common and simplest case, a single file is a single module.

So you can think of the files you write that end in ``.py`` as modules.

When a module is imported, the code in that file is run, and any names defined in that file are now available in the module namespace.

For a really simple example, if you have the following in the ``trivial.py`` file:

.. code-block:: python
   :linenos:

    x = 1
    y = 2

    def do_nothing(a, b, c):
        print("do_nothing was called with:", a, b, c)

    print("at the end of the trivial module")

What do you think happens when you import that module? What will get printed?

What names will be defined in that module?

How would you access those names?

Before running this code, think about it a bit. Recall what happens when you import a module:

* The code is run in the module, top to bottom.
* The names defined in the module (its global namespace) are made available in the modules namespace.

So: Lines 1-2 assign two names, ``x`` and ``y``. lines 4-5 define a function, named ``do_nothing``. Line 7 prints something.

So: when run, there are three names defined, and one print function run.

Now try it:

.. code-block:: python

    >>> import trivial
    at the end of the trivial module

yes, we got that print function run.

Let's see if the names are there:

.. code-block:: python

    >>> trivial.x
    1
    >>> trivial.y
    2

.. code-block:: python


    >>> trivial.do_nothing(3,4,5)
    do_nothing was called with: 3 4 5

yes, there are, in the ``trivial`` namespace.


Packages
--------

A package is a module with other modules in it.

On a filesystem, this is represented as a directory that contains one or more ``.py`` files, one of which **must** be called ``__init__.py``. The ``__init__.py`` file can be empty (and often is) -- but it must be there.

When there is a package available, you can import only the package, or any of the modules inside it. When a package is imported, the code in the ``__init__.py`` file is run, and any names defined in that file are available in the *package namespace*.

Here we define about the simplest package possible:

Create a directory (folder) for your package:

.. code-block:: bash

    mkdir my_package

Save a file in that package, called ``__init__.py``, and put this in it:

.. code-block:: python

    name1 = "Fred"
    name2 = "Bob"

Save another file in your my_package dir called ``a_module.py``, and put this in it:

.. code-block:: python

    name3 = "Mary"
    name4 = "Jane"

    def a_function():
        print("a_function has been called")

You now have about the simplest package you can have. Make sure your current working dir is the dir that ``my_package`` is in, and start python or iPython. Then try this code:

.. code-block:: ipython

    In [1]: import my_package

    In [2]: my_package.name1
    Out[2]: 'Fred'

    In [3]: my_package.name2
    Out[3]: 'Bob'

The names you've defined are available in the package namespace.

What about the module?

.. code-block:: ipython

    In [4]: my_package.a_module
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-4-8b9269cdf0e5> in <module>()
    ----> 1 my_package.a_module

    AttributeError: module 'my_package' has no attribute 'a_module'

the ``a_module`` name does not exist. It must be imported explicitly:

.. code-block:: ipython

    In [1]: import my_package.a_module

Now the names defined in the ``a_module.py`` file are all there:

.. code-block:: ipython

    In [2]: my_package.a_module.name3
    Out[2]: 'Mary'

    In [3]: my_package.a_module.name4
    Out[3]: 'Jane'

    In [4]: my_package.a_module.a_function()
    a_function has been called

Note that you can also put a package inside a package. So you can create arbitrarily deeply nested hierarchy of packages. This can be helpful for a large, complex collection of related code, such as an entire Web Framework. But from the *Zen of Python*:

   "Flat is better than nested."

So don't overdo it -- only go as deep as you really need to to keep your code organized.


Importing modules
-----------------

You have probably imported a module or two already:

.. code-block:: python

    import sys
    import math

But there a handful of ways to import modules and packages.

.. code-block:: python

    import modulename

Is the simplest way: this adds the name of the module to the global namespace, and lets you access the names defined in that module:

.. code-block:: python

    modulename.a_name_in_the_module

If you want only a few names in a module, and don't want to type the module name each time, you can import only the names you want:

.. code-block:: python

    from modulename import this, that

This brings only the names specified (``this``, ``that``) into the global namespace. All the code in the module is run, but the module's name is not available. But the explicitly imported names are directly available.

Sometimes you want the entire module, but maybe not want to type its entire name eadh time you use. So you can rename a module when you import it. (you may also want to do this if a module has the same name as a variable you want to use...)

.. code-block:: python

    import modulename as a_new_name

This imports the module, and gives it a new name in the global namespace. For example, the numpy package is usually imported as:

.. code-block:: python

    import numpy as np

Because numpy has a LOT of names, some of which may conflict with builtins or other modules, and users want to be able to reference them without too much typing.

You can also import a name within a module and rename it at the same time:

.. code-block:: python

    from modulename import this as that

This imports only one name from a module, while also giving it a new name in the global namespace.


Examples
--------

You can play with some of this with the standard library:

.. code-block:: ipython

    In [1]: import math

    In [2]: math.sin(1.2)
    Out[2]: 0.9320390859672263

    In [3]: from math import cos

    In [4]: cos(1.2)
    Out[4]: 0.3623577544766736

    In [5]: import math as m

    In [6]: m.sin(1)
    Out[6]: 0.8414709848078965

    In [7]: from math import cos as cosine

    In [8]: cosine(1.2)
    Out[8]: 0.3623577544766736


My rules of thumb
-----------------

If you only need a few names from a module, import only those:

.. code-block:: python

    from math import sin, cos, tan

If you need a lot of names from that module, just import the module:

.. code-block:: python

    import math
    math.cos(2 * math.pi)

Or import it with a nice short name:

.. code-block:: python

    import math as m
    m.cos(2 * m.pi)

import \* ?
-----------

.. centered:: **Warning:**

You can also import all the names in a module with:

.. code-block:: python

    from modulename import *

But this leads to name conflicts, and a cluttered namespace. It is NOT recommended practice anymore.


Importing from packages
-----------------------

Packages can contain modules, which can be nested -- ideally not very deeply.

In that case, you can simply add more "dots" and follow the same rules as above.

.. code-block:: python

    from packagename import my_funcs.this_func

.. Here's a nice reference for more detail:

.. http://effbot.org/zone/import-confusion.htm

.. And

:ref:`packaging` goes into more detail about creating (and distributing!) your own package.


What does ``import`` actually do?
---------------------------------

When you import a module, or a symbol from a module, the Python code is *compiled* to *bytecode*.

The result is a ``module.pyc`` file.

Then after compiling, all the code in the module is run **at the module scope** -- that is, in the namespace of the module.

For this reason, it is good to avoid module-scope statements that have global side-effects. This includes things as simple as a ``print()`` -- it will only print the first time the module is imported.


Re-import
----------

The code in a module is *not* re-run when imported again. This makes it efficient to import the same module multiple places in a program. But it means that if you change the code in a module after importing it, that change will not be reflected when it is imported again.

If you DO want a change to be reflected, you can explicitly reload a module:

.. code-block:: python

    import importlib
    importlib.reload(modulename)

This is rarely needed (which is why it's a bit buried in the ``importlib`` module), but is good to keep in mind when you are interactively working on code under development.

Import Interactions
-------------------

Another key point to keep in mind is that all code files in a given python program are sharing the same modules. So if you change a value in a module, that value's change will be reflected in other parts of the code that have imported that same module.

This can create dangerous side effects and hard to find bugs if you change anything in an imported module, but it can also be used as a handy way to store truly global state, like application preferences, for instance.

A rule of thumb for managing global state is to have only *one* part of your code change the values, and everywhere else considers them read-only. You can't enforce this, but you can structure you own code that way.

Let's take a look at an example of this.

Create three modules (python files):

``mod1.py``, ``mod2.py``, ``mod3.py``

``mod1.py`` is very simple -- one name declared:

.. code-block:: python

    x = 5

``mod2.py`` is where a bit actually goes on:

.. code-block:: python

    #!/usr/bin/env python3

    import mod1

    print(f"In mod2: mod1.x = {mod1.x}")

    input("pausing (hit enter to continue >")

    print("importing mod3")

    import mod3

    print(f"Still in mod2: mod1.x = {mod1.x}")

    print("mod3 changed the value in mod1, and that change shows up in mod2")

Here, we import ``mod1``, and we can now see the names defined in it, and print the value of ``x``. Then it pauses, waiting for input. After the user hits the <enter> key, it then imports ``mod3``, and again prints the value of ``x`` that is in ``mod1``. Let's now look at ``mod3.py``:

.. code-block:: python

    import mod1

    print("In mod3 -- changing the value of mod1.x")

    mod1.x = 555

Other than the print -- all ``mod3`` does is re-set the value of ``x`` that is on ``mod1``.
Running ``mod2.py`` results in::

    $ python mod2.py
    In mod2: mod1.x = 5
    pausing (hit enter to continue >
    importing mod3
    In mod3 -- changing the value of mod1.x
    Still in mod2: mod1.x = 555
    mod3 changed the value in mod1, and that change shows up in mod2

You can see that when ``mod2`` changed the value of ``mod1.x``, that changed the value everywhere that ``mod1`` is imported. You want to be very careful about this.

If you are writing ``mod2.py``, and did not write ``mod3`` (or wrote it long enough ago that you don't remember its details), you might be very surprised that a value in ``mod1`` changes simply because you imported ``mod3``.  This is known as a "side effect", and you generally want to avoid them!
