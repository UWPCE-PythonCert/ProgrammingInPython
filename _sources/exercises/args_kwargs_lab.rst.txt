.. _exercise_args_kwargs_lab:

``args`` and ``kwargs`` Lab
===========================

Goal:
-----

Develop an understanding of using advanced argument passing and parameter definitons.

If this is all confusing -- you may want to review this:

http://stupidpythonideas.blogspot.com/2013/08/arguments-and-parameters.html

.. note::

  This is not all that clearly specified -- the goal is for you to
  experiment with various ways to define and call functions, so you
  can understand what's possible, and what happens with each call.
  It is also entirely silly, since the function does not do anything
  at all, but it will teach you about using parameters effectively.


Test Driven Development?
------------------------

Since this code isn't really going to do anything, it doesn't make a lot of sense to test it.  However, you need to run the code somehow. So this is a good chance to practice test-driven development -- even if only as a way to run your code as you write it.

For each step of the exercise, write a test that calls your function in a particular way, and test that it returns what you expect. In this case, what you will be testing is not really the code -- but rather your own expectations of what the results should be.

You will also be testing Python's argument handling, which you can be pretty sure DOES work correctly.

So while these won't be useful tests in the usual sense, this is a chance to get used to test driven development.


Procedure
---------

We are going to do this as test driven development: Your first task for each step below is to write a test that will ensure your code does what you think it should do.

Keyword Arguments
-----------------

* Write a function that has four optional parameters (with defaults):

  - `fore_color`
  - `back_color`
  - `link_color`
  - `visited_color`

* Have it return the colors (use strings for the colors, e.g. "blue", "red", etc.)

* Call it with a couple different parameters set. That is, write tests that verify that all of the following work as advertised:

  - Using just positional arguments:

    - ``func('red', 'blue', 'yellow', 'chartreuse')``

  - Using just keyword arguments:

    -  ``func(link_color='red', back_color='blue')``

  - using a combination of positional and keyword

    -  ``func('purple', link_color='red', back_color='blue')``

  - using ``*some_tuple`` and/or ``**some_dict``

    - ``regular = ('red', 'blue')``

    - ``links = {'link_color': 'chartreuse'}``

    - ``func(*regular, **links)``


Generic parameters
------------------

* Write a new function with the parameters as:

``*args`` and ``**kwargs``

* Have it return the colors (use strings for the colors again)

* Call it with the same various combinations of arguments used above.

* Also have it print ``args`` and ``kwargs`` directly, so you can be sure you understand what's going on.

* Note that in general, you can't know what will get passed into ``**kwargs`` So maybe adapt your function to be able to do something reasonable with any keywords.

