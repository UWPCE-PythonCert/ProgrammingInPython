.. _exercise_unit_testing:

############################
Introduction To Unit Testing
############################

Preparation
-----------

In order to do unit testing, you need a framework in which to write and run your tests.
Earlier in this class, you've been adding "asserts" to your modules -- perhaps in the ``__name__ == "__main__"`` block.  These are, in fact, a kind of unit test.
But as you build larger systems, you'll want a more structured way to write and run your tests.

We will use the pytest testing system for this class.

If you have not already done so -- install pytest like so:

.. code-block:: bash

    $ python3 -m pip install pytest

Once this is complete, you should have a ``pytest`` command you can run
at the command line:

.. code-block:: bash

    $ pytest
    ====================== test session starts ======================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
    rootdir: /Users/chris.barker/Junk/junk
    collected 0 items

    ===================== no tests ran in 0.00s =====================


If you already HAVE some tests -- you may see something different!


Test Driven Development
-----------------------

Download these files, or find them in the exercise repo:

:download:`test_walnut_party.py <unit_testing/test_walnut_party.py>`

and:

:download:`walnut_party.py <unit_testing/walnut_party.py>`

(This is the adapted from the codingbat site: http://codingbat.com/prob/p195669)

In the directory where you put the files, run:

.. code-block:: bash

  $ pytest test_walnut_party.py

You will get a LOT of test failures!

What you've done here is the first step in what is called:

.. centered::  **Test Driven Development (TDD)**

A bunch of tests exist, but the code to make them pass does not yet exist.

The red you see in the terminal when we run our tests is a goad to us to write the code that fixes these tests.

The tests all failed  because currently ``walnut_party()`` looks like:

.. code-block:: python

  def walnut_party(walnuts, is_weekend):
      pass

A totally do nothing function -- of course the tests all fail!


Making tests pass
-----------------

Open:

``test_walnut_party.py``

and:

``walnut_party.py``

In your editor.

Now edit the function in ``walnut_party.py``, and each time you make a change, run the tests again. Continue until all the tests pass.

When the tests pass -- you are done! That's the beauty of test-driven development.

Doing your own:
---------------

Pick another example from codingbat:

``http://codingbat.com``

Do a bit of test-driven development on it:

* Run something on the web site.
* Write a few tests using the examples from the site.
* Then write the function, and fix it 'till it passes the tests.

These tests should be in a file named ``test_something.py`` -- I usually name the test file the same as the module it tests,
with ``test_`` prepended.

.. note::
  Technically, you can name your test files anything you want. But there are two reasons to use standard naming conventions.
  One is that it is clear to anyone looking at the code what is and isn't a test module. The other is that pytest, and other testing systems, use
  `naming conventions <https://docs.pytest.org/en/latest/goodpractices.html#test-discovery>`_ to find your test files.
  If you name your test files: ``test_something.py`` then pytest will find them for you. And if you use the name of the module being tested:
  ``test_name_of_tested_module.py`` then it will be clear which test files belong to which modules.


Do at least two of these to get the hang of the process.

Also -- once you have the tests passing, look at your solution -- is there a way it could be refactored to be cleaner?

Give it a shot -- you'll know if it still works if the tests still pass!

