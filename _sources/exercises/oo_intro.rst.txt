.. _oo_intro:

########################
OO Intro - Report Class
########################

This assignment uses Object Oriented Programming to design a class that can be used to manage data reporting.

We have done some reporting in our mailroom program, but that report was pretty simple and used simple functions to accomplish the work.

We will explore here, how one can utilize OO to improve and enhance reporting capabilities.


Procedure
=========

You will use :download:`oo_intro.py` file as a starting point for your code.

You will notice that ``Report`` class will have attributes and methods defined for you, including input parameters (and their types) as well as expected output. You will need to fill out the code for each defined method and docstrings contain additional information on what is expected.

The ``Report`` class uses another class that is fully defined for you, the ``Row`` class. This class represents a single row in your report, and the report class will hold a list of the row instances.
There are big advantages to using a class like ``Row`` in contrast to a simple dictionary, this design creates a clear contract on what's expected to be as part of a row, where with a dictionary it is easy to misspell or miss a key.
A class like ``Row`` is often called a dataclass (since it only holds "data" and doesn't actually have any logic to it).

This is such a popular pattern that python introduced dataclasses to make this even simpler and you can read more about them here:
https://realpython.com/python-data-classes/. You do not use them in this assignment but you should know that they exist and why.



And at last, you will of course want to include unit tests covering all of your class methods.