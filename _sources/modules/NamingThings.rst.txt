:orphan:

.. _style_and_naming:

################
Style and Naming
################

**Style matters!**

PEP 8 reminder
--------------

PEP 8 (Python Enhancement Proposal 8):
https://www.python.org/dev/peps/pep-0008/

Is the "official" style guide for Python code.

Strictly speaking, you only need to follow it for code in the standard library.

But style matters -- consistent style makes your code easier to read and understand.

And everyone in the community has accepted PEP as *the* Python style guide.

So **follow PEP 8**

**Exception:** if you have a company style guide -- follow that instead.

Try the "pycodestyle" module on your code::

  $ python3 -m pip install pycodestyle
  $ pycodestyle my_python_file

Try it now -- really!

Note that ideally you have a linter installed in your editor that yells at you if you violate PEP8 -- no need to run ``pycodestyle`` if it's already in your editor.

See: :ref:`editor_for_python` for suggestions on editors and configuration.

Naming things...
----------------

It matters what names you give your variables.

Python has rules about what it *allows*.

PEP8 has rules for style: capitalization, and underscores and all that.

But you still get to decide within those rules.

So use names that make sense to the reader.

Naming Guidelines
-----------------

Whenever possible, use strong, unambiguous names that relate to a concept in the business area applicable for your program.
For example, ``cargo_weight`` is probably better than ``item_weight``, ``current_fund_price`` is better than ``value``. But all of those are better than ``item``, or ``x``, or ...

Only use single-letter names for things with limited scope: indexes and the like:

.. code-block:: python

    for i, item in enumerate(a_sequence):
        do_something(i, item)

But **don't** use a name like "item", when there is a meaning to what the item is:

.. code-block:: python

    for name in all_the_names:
        do_something_with(name)

Use plurals for collections of things:

.. code-block:: python

    names = ['Fred', 'George', ...]

And then singular for a single item in that collection:

.. code-block:: python

    for name in names:
       ...

**Do** re-use names when the use is essentially the same, and you don't need the old one:

.. code-block:: python

    line = line.strip()
    line = line.replace(",", " ")
    ....

What about Hungarian Notation?
------------------------------

`Hungarian Notation <https://en.wikipedia.org/wiki/Hungarian_notation>`_
is a naming system where the data type is part of the name:

.. code-block:: python

  strFirstName = "Chris"

  listDonations = [400.0, 125.0, 1000.0]

  int_num_days = 30

This method is not recommended nor widely used in the Python community.

One reason is Python's dynamic typing -- it really isn't important what type a value is, but rather, what it means.
And you may end up refactoring the code to use a different type, and then do you want to have to rename everything?
Or worse, the type in the name no longer matches the actual type in the code -- and that's really bad.  I have seen code like this:

.. code-block:: python

  strNumber = input("How many would you like?")
  strNumber = int(strNumber)

  for i in range(strNumber):
      ...

So you have a name used for a string, then it gets converted to an integer, and the data type no longer matches the name.  Wouldn't you be better off if that had never been named with the type in the first place?

While widely used in some circles, it is generally considered bad style in the Python community -- so:

 **Do not use Hungarian Notation**

More About Naming Things
------------------------

Here's a nice talk about naming:

`Jack Diederich: Name things Once <https://www.youtube.com/watch?v=hZ7hgYKKnF0>`_

One note about that talk -- Jack is mostly encouraging people to not use names that are too long and unnecessarily specific.
However, with beginners, it's often tempting to use names that are too *short* and *non-specific*, like "x" and "item" -- so you need to strike a balance.



