.. _exercise_mailroom_part3_exceptions:


Mailroom Part 3
=================

**Improve your mailroom by adding exceptions and comprehensions.**

Exceptions
----------

Now that you've learned about exception handling, you can update your code to handle errors better, such as when a user inputs bad data.


Comprehensions
--------------

Can you use comprehensions to clean up your code a bit?

Note: you may be tempted to replace loops like this:

.. code-block:: python

    for donor in donors:
        print(donor)

with

.. code-block:: python

    [print(donor) for donor in donors]


That's not the intended use of comprehensions. Because ``print`` function does not return a value, this code will allocate a space for an "empty" result list filled with None values:

    >>> [print(donor) for donor in donors]
    jane
    wendy
    [None, None]
    >>>

List comprehensions are designed for a very specific use case:

*Processing a sequence of items to create another sequence.*

They are not designed to replace all for loops.

