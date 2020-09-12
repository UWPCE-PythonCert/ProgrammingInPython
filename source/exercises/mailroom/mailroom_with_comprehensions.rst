.. _exercise_mailroom_comprehensions:


Mailroom With Comprehensions
============================

**Improve your mailroom by adding (maybe) comprehensions.**


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

So if you have code that looks like:

.. code-block:: python

  new_list = []
  for item in old_list:
      new_list.append(do_something_to(item))

Then you have a candidate for a comprehension.

In your version of mailroom -- there may not be any such constructs -- that's OK, don't use a comprehension unless it cleans up your code.

