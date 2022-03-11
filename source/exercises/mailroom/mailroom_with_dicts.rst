.. _exercise_mailroom_with_dicts:


Mailroom With Dicts
===================

**Incorporate dictionary use.**

Use dicts where appropriate.
----------------------------

The first version of this assignment used these basic data types: numbers, strings, lists and tuples.

However, using dictionaries, an important built in data structure in Python, will let you re-write your program a bit more simply and efficiently.

Update your mailroom program to:

  - Convert your main donor data structure to be a dict. Think about an appropriate key for easy donor look up.

  - Use dicts anywhere else, as appropriate.

  - Use a dict to switch between the users selections.
    see :ref:`dict_as_switch` for what this means.

  - Use a dict and the ``.format()`` method to produce the letter as one big template, rather than building up a big string that produces the letter in parts.


Example:

.. code-block:: ipython

  In [3]: d
  Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


  In [5]: "My name is {first_name} {last_name}".format(**d)
  Out[5]: 'My name is Chris Barker'

Don't worry too much about the ``**``. We'll get into the details later, but for now it means, more or less, "pass this whole dict in as a bunch of keyword arguments."
