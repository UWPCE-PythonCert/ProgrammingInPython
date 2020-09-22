.. _oo_intro:

#######################
OO Intro - Report Class
#######################

This assignment uses Object Oriented Programming to design a class that can be used to manage data reporting.

We have done some reporting in our mailroom program, but that report was pretty simple and used simple functions to accomplish the work.

We will explore here how one can utilize OO to improve and enhance reporting capabilities.


Procedure
=========

Use the :download:`report.py` and :download:`test_report.py` files as a starting point for your code.

Notice that the ``Report`` class has attributes and methods defined for you, including input parameters as well as expected output.

You will need to fill out the code and docstrings for each defined method containing additional information on what is expected.

There is also some example code in the ``__main__`` block, to see how it's used.

Use TDD: write a test for each method before you add that functionality. There is a test file started for you -- it has one (failing) test for one of the methods.

The Row class
-------------

The ``Report`` class uses another class, ``Row``, that is fully defined (and tested) for you. This class represents a single row in your report, and the report class will hold a list of the row instances.

There are big advantages to using a class like ``Row`` rather than a simple dictionary. This design creates a clear contract about what is part of a row, whereas with a dictionary you can put anything in it, so it is harder to catch when a key is misspelled or missing.

A class like ``Row`` is often called a "data class" (since it only holds "data" and doesn't actually have any logic to it).

This is such a popular pattern that Python introduced ``dataclasses`` in
`version 3.7 <https://www.python.org/dev/peps/pep-0557>`_ to make this even simpler.
You do not use them in this assignment but you should know that they exist and why.

You can read more about ``dataclasses`` in the Python docs here:

https://docs.python.org/3/library/dataclasses.html

Or a more descriptive tutorial here:

https://realpython.com/python-data-classes/.

Reminder: use Test Driven Development and make sure you have complete unit tests for all of your class methods.

