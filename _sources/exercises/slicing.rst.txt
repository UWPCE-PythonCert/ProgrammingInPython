.. _exercise_slicing:

###########
Slicing Lab
###########

Goal
====

Get the basics of sequence slicing down.

Tasks
-----

Write some functions that take a sequence as an argument, and return a copy of that sequence:

* with the first and last items exchanged.
* with every other item removed.
* with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
* with the elements reversed (just with slicing).
* with the last third, then first third, then the middle third in the new order.

  - Example:   ``(1,2,3,4,5,6)`` should return: ``(5,6,1,2,3,4)`` (start with a length that's a multiple of three, but make sure it doesn't crash for other lengths)

**NOTE:** These should work with ANY sequence -- but you can use strings to test, if you like.

Your functions should look like:

.. code-block:: python

  def exchange_first_last(seq):
      return a_new_sequence

Tests:
------

.. code-block:: python

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

Write a test or two like that for each of the above functions.


