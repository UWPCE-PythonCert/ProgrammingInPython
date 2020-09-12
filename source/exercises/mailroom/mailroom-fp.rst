:orphan:

.. _exercise_mailroom_fp:

#####################
Mailroom - Functional
#####################

Making Mailroom Functional

or: Adding a few functional features :-)

A new approach
==============

It was reasonable to build the simple MailRoom program using a single module, a simple data structure, and functions that manipulate that data structure. It was reasonable to refactor Mailroom around classes when it started to become unwieldy with all of the features we wanted to add to it.

Due to the success of Mailroom and the good PR it has generated with all its thank you letters, the donations are pouring in.  This has raised the attention of wealthy philanthropists who are willing to contribute matching funds.  Our problem now is to expand Mailroom so that it can run projections and account for matching funds offered by philanthropists.  Management is tremendously happy with us and has offered to support our expansion of Mailroom toward a distributed architecture capable of running calculations on matching funds across the donor database in parallel.

This is a good candidate for a functional programming approach.

Updating the code
=================

Preparation
-----------

Mailroom is our longest running exercise.  At this point you may have several versions of the program in separate files or indeed many versions of the program within the same python source file with some sections commented in and others commented out.

In terms of Mailroom's developmental chronology the original exercise added features over the course of several weeks.  A major branch likely occurred when refactoring around object orientation.  Another major branch may be occurring here as we investigate functional programming concepts.  Is it starting to feel disorganized and a little out of control?  Welcome to the world of real software development.

If you are familiar with git as we have been using it so far, it may be a good time to "branch out" (pun intended), and start using git's branching features.

On the other hand, if git is still painful for you, feel free to simply make a copy of your currently working mailroom code (and tests) in a new directory.

IF you want to try branching, there are some notes here: :ref:`git_branching`

Making new files
----------------

If you don't want to mess around with branching:

You will need to come up with a good naming convention for your source files.  You could consider separate source file names all within the same directory like this:


.. code-block:: bash

  mailroom/mailroom.py
  mailroom/mailroom_oo.py
  mailroom/mailroom_fp.py

Or separate directories for each of your versions like this:

.. code-block:: bash

  mailroom/mailroom.py
  mailroom_oo/mailroom.py
  mailroom_fp/mailroom.py

Regardless of how you decide to manage names and track versions you may also need to decide where to start on this exercise.  Should you start from your most recent version which likely involves classes or do you back out to an earlier version before we studied object orientation?  Another option is to start again from scratch.  The choice is yours.


Map, Filter, Reduce
-------------------

1. Add a new feature to Mailroom using ``map`` so that each donation on record can be doubled, tripled or indeed multiplied by any arbitrary factor based on the whims of philanthropists who would like to support our cause.

  This will require a new function (or method in your donor database class) called ``challenge(factor)`` that takes a multiplier ``(factor)``, and multiplies all the donations of all the donors by the factor.  The function returns a NEW donor database, with the new data.

2. Add a new feature to Mailroom using filter so that donations either above or below a specified dollar amount are included in the map operations of #1 above.

  You can do this by adding ``min_donation`` ``and max_donation`` optional keyword parameters to your ``challenge`` function. You'll want to filter the donations before passing them to map.

3. Refactor the new features outlined in #1 and #2 above such that they can be used to run projections.  Imagine the following scenario.  You are an account manager out in the field meeting with philanthropists and talking with them about the many ways they might structure their matching contributions.  You would like a feature that could show them, based on past contributions, what their total contribution would become under different scenarios.  For instance, based on donations in the current database, show them (a) what their total contribution would come to in dollars if they were to double contributions under $100.  And then (b) show them what their total contribution would come to if they were to triple contributions over $50.

  This may require another option in your menu-driven interface.

Use ``map``, ``filter`` and either ``sum`` or ``reduce`` to accomplish the goals above.


Distributed Processing
----------------------

Map, filter and reduce lend themselves to parallel, distributed programming.  Indeed algorithms that lend themselves gracefully to map/filter solutions tend to lend themselves equally well to parallel processing.  We have a name for it: `embarrassingly parallel`_.

Our next expansion of Mailroom stands on the shoulders of the work you did with map, filter and reduce.  We are going to take advantage of the embarrassingly parallel property of map/filter algorithms to run map operations in parallel.

We have many avenues open to us in terms of setting up the back-end infrastructure for this exercise.  In lieu of a supercomputer cluster, which we could "easily" spin up on any of several cloud computing services, we are going to use `IPython Parallel`_.  Note that we could spin up IPython Parallel across a cluster of machines, but for the purposes of this exercise running it locally will suffice.

To get started follow the instructions in this :ref:`ipyparallel_quickstart`.

Look now at the code you created for the map, filter, reduce exercise above.  Focus on the map operations.  Your task is to replace the map operations using one of IPython Parallel's `apply`_ functions.  For this exercise ``apply_sync()`` may be your most straightforward option.  For our purposes Python's built-in ``map`` and IPyParallel's ``apply`` are conceptually identical: they both apply a function to all the elements of a data structure.

.. _embarrassingly parallel: https://en.wikipedia.org/wiki/Map_(parallel_pattern)
.. _IPython Parallel: https://ipyparallel.readthedocs.io/en/latest/
.. _apply: http://ipyparallel.readthedocs.io/en/6.0.2/multiengine.html?highlight=apply_sync#calling-python-functions


Closures
--------

**Do this only after you learn about closures next class!**

Closures are another functional programming strategy.  They allow you to create functions according to parameters that are known only at runtime and not beforehand.

Your task now is to replace the functions that you have been passing to ``map()`` or ``apply()`` with a closure.

