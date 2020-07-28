
.. _unit_testing:

#######
Testing
#######

This page is a quick overview of testing in Python. It provides some background on testing, and the tools available. Later on, we'll get to the details of how to actually do it.

Testing your code is an absolute necessity -- you need to have *some* way to know it's doing what it should.

Having your testing done in an automated way is really a good idea.

You've already seen a very basic testing strategy: putting some ``assert`` statements in the ``__name__ == "__main__"`` block.

You've written some tests using that strategy.

These tests were pretty basic, and a bit awkward in places (testing error
conditions in particular).

    **It gets better**

Test Frameworks
---------------

So far our tests have been limited to code in an ``if __name__ == "__main__":``
block.


* They are run only when the file is executed
* They are always run when the file is executed
* You can't do anything else when the file is executed without running tests.


This is not optimal.

You really want ways to structure your tests, and run your tests, that can be controlled and provide nifty features.


Standard Library: ``unittest``
------------------------------

Python comes with the ``unittest`` package that provides a number of nifty features. It was introduced in version 2.1 -- so it's been around a long time.

It is more or less a port of `JUnit <https://junit.org>`_ from Java, which shows -- it's has a style and structure that fit Java more than Python:

A bit verbose: you have to write classes & methods (And we haven't covered that yet!)

But you will see it used in others' code, so it's good to be familiar with it.
And seeing how verbose it can be will help you appreciate other options.

So here's a bit of an introduction -- if the class stuff confuses you, don't worry about it -- you don't need to actually DO this yourself :-)


Using ``unittest``
------------------

To use ``unittest``, you need to write subclasses of the ``unittest.TestCase`` class (after importing the package, of course):

.. code-block:: python

    # in test.py
    import unittest

    class MyTests(unittest.TestCase):

        def test_tautology(self):
            self.assertEqual(1, 1)

Then you run the tests by using the ``main`` function from the ``unittest``
module:

.. code-block:: python

    # in test.py
    if __name__ == '__main__':
        unittest.main()

``unittest.main()`` is called in the module where there tests are. which means that they can be, but do not have to be, in the same file as your code.

NOTE: tests can also be run by "test runners" for more features.

Testing Your Code
-----------------

You can write your code in one file and test it from another -- and for all but the smallest projects, you want to do that.

in ``my_mod.py``:

.. code-block:: python

    def my_func(val1, val2):
        return val1 * val2

in ``test_my_mod.py``:

.. code-block:: python

    import unittest
    from my_mod import my_func


    class MyFuncTestCase(unittest.TestCase):
        def test_my_func(self):
            test_vals = (2, 3)
            expected = test_vals[0] * test_vals[1]
            actual = my_func(*test_vals)
            self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()

So this is pretty easy, but it's kind of a lot of code for just one test, yes?

Advantages of ``unittest``
--------------------------

The ``unittest`` module is pretty full featured

It comes with the standard Python distribution, no installation required.

It provides a wide variety of assertions for testing all sorts of situations.

It allows for a setup and tear down work flow both before and after all tests and before and after each test.

It's well known and well understood.


Disadvantages of ``unittest``
-----------------------------

It's Object Oriented, and quite "heavyweight".

  - modeled after Java's ``JUnit`` and it shows...

It uses the Framework Design Pattern, so knowing how to use the features means learning what to override.

Needing to override means you have to be cautious.

Test discovery is both inflexible and brittle.

And there is no built-in parameterized testing.


Other Options
-------------

Due to these limitations, folks in the Python community have developed other options for testing in Python:

* **Nose2**: https://github.com/nose-devs/nose2

* **pytest**: http://pytest.org/latest/

* ... (many frameworks supply their own test runners: e.g. django)

Nose was the most common test runner when I first started learning testing, but it has been in maintenance mode for a while. Even the nose2 site recommends that you consider pytest.

pytest has become the defacto standard testing system for those that want a more "pythonic" test framework.

pytest is very capable and widely used.

For a great description of the strengths of pytest, see:

`The Cleaning Hand of Pytest <https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684>`_

If you look above, pytest provided every feature of unittest except being in the standard library. And none of the disadvatages. It also can run unittest tests, so if you already have unittest tests, or like some of its features, you can still use pytest.

So we will use pytest for the rest of this class.


Installing ``pytest``
---------------------

pytest is very easy to install these day:

.. code-block:: bash

    $ python -m pip install pytest

Once this is complete, you should have a ``pytest`` command you can run
at the command line:

.. code-block:: bash

    $ pytest

If you have any tests in your repository, that command will find and run them (If you have followed the proper naming conventions).

    **Do you?**


Pre-existing Tests
------------------

Let's take a look at some examples.

Create a directory to try this out, and download:

:download:`test_random_unitest.py <../examples/testing/test_random_unitest.py>`

In the directory you created for that file, run:

.. code-block:: bash

  $ pytest

It should find that test file and run it.

You can also run pytest on a particular test file:

.. code-block:: bash

  $ pytest test_random_unitest.py

The results you should have seen when you ran ``pytest`` above come
partly from these files.

Take a few minutes to look these files over.

``test_random_unitest.py`` contains the tests for some of the functions in the built in``random`` module. You really don't need to test Python's built in modules -- they are already tested! This is just to demonstrate the process.


What is Happening Here?
-----------------------

You should have gotten results that look something like this:

.. code-block:: bash

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.10.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/temp/test_temp, inifile:
    plugins: cov-2.6.0
    collected 3 items

    test_random_unitest.py ...                                               [100%]

    =========================== 3 passed in 0.06 seconds ===========================


When you run the ``pytest`` command, ``pytest`` starts in your current
working directory and searches the file system for things that might be tests.

It follows some simple rules:

* Any python file that starts with ``test_`` or ``_test`` is imported.

* Any functions in them that start with ``test_`` are run as tests.

* Any classes that start with ``Test`` are treated similarly, with methods that begin with ``test_`` treated as tests.

( don't worry about "classes" part just yet ;-) )

* Any ``unittest`` test cases are run.

pytest
------

This test running framework is simple, flexible and configurable.

Read the documentation for more information:

http://pytest.org/latest/getting-started.html#getstarted

It will run ``unittest`` tests for you, so can be used as a test runner.

But in addition to finding and running tests, it makes writing tests simple, and provides a bunch of nifty utilities to support more complex testing.

Now download this file:

:download:`test_random_pytest.py <../examples/testing/test_random_pytest.py>`

And run pytest again:

.. code-block:: bash

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.10.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/temp/test_temp, inifile:
    plugins: cov-2.6.0
    collected 8 items

    test_random_pytest.py .....                                              [ 62%]
    test_random_unitest.py ...                                               [100%]

    =========================== 8 passed in 0.07 seconds ===========================

Note that it ran the tests in both the test files.

Take a look at ``test_random_pytest.py`` -- It is essentially the same tests -- but written in native pytest style -- simple test functions.

pytest tests
------------

The beauty of pytest is that it takes advantage of Python's dynamic nature -- you don't need to use any particular structure to write tests.

Any function named appropriately is a test.

If the function doesn't raise an error or an assertion, the test passes. It's that simple.

Let's take a look at ``test_random_pytest.py`` to see how this works.

.. code-block:: python

    import random
    import pytest

The ``random`` module is imported becasue that's what we are testing.
``pytest`` only needs to be imported if you are using its utilities -- more on this in a moment.

.. code-block:: python

    seq = list(range(10))

Here we create a simple little sequence to use for testing. We put it in the global namespace so other functions can access it.

Now the first tests -- simply by naming it ``test_something``, pytest will run it as a test:

.. code-block:: python

    def test_choice():
        """
        A choice selected should be in the sequence
        """
        element = random.choice(example_seq)
        assert (element in example_seq)

This is pretty straightforward. We make a random choice from the sequence,
and then assert that the selected element is, indeed, in the original sequence.

.. code-block:: python

    def test_sample():
        """
        All the items in a sample should be in the sequence
        """
        for element in random.sample(example_seq, 5):
            assert element in example_seq

And this is pretty much the same thing, except that it loops to make sure that every item returned by ``.sample`` is in the original sequence.

Note that this will result in 5 separate assertions -- that is fine, you can have as many assertions as you like in one test function. But the test will fail on the first failed assertion -- so you only want to have closely related assertions in each test function.

.. code-block:: python

    def test_shuffle():
        """
        Make sure a shuffled sequence does not lose any elements
        """
        seq = list(range(10))
        random.shuffle(seq)
        seq.sort()  # If you comment this out, it will fail, so you can see output
        print("seq:", seq)  # only see output if it fails
        assert seq == list(range(10))

This test is designed to make sure that ``random.shuffle`` only re-arranges the items, but doesn't add or lose any.

In this case, the global ``example_seq`` isn't used, because ``shuffle()`` will change the sequence -- tests should never rely on or alter global state. So a new sequence is created for the test.  This also allows the test to know exactly what the results should be at the end.

Then the "real work" -- calling ``random.shuffle`` on the sequence -- this should re-arrange the elements without adding or losing any.

Calling ``.sort()`` again should put the elements back in the order they started

So we can then test that after shuffling and re-sorting, we have the same sequence back:

.. code-block:: python

    assert seq == list(range(10))

If that assertion passes, the test will pass.

``print()`` and test failures
.............................

Try commenting out the sort line:

.. code-block:: python

    # seq.sort()  # If you comment this out, it will fail, so you can see output

And run again to see what happens. This is what I got:

.. code-block:: bash

    $ pytest test_random_pytest.py
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.10.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/PythonStuff/UWPCE/PythonCertDevel/source/examples/testing, inifile:
    plugins: cov-2.6.0
    collected 5 items

    test_random_pytest.py F....                                              [100%]

    =================================== FAILURES ===================================
    _________________________________ test_shuffle _________________________________

        def test_shuffle():
            """
            Make sure a shuffled sequence does not lose any elements
            """
            seq = list(range(10))
            random.shuffle(seq)
            # seq.sort()  # If you comment this out, it will fail, so you can see output
            print("seq:", seq)  # only see output if it fails
    >       assert seq == list(range(10))
    E       assert [4, 8, 9, 3, 2, 0, ...] == [0, 1, 2, 3, 4, 5, ...]
    E         At index 0 diff: 4 != 0
    E         Use -v to get the full diff

    test_random_pytest.py:22: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    seq: [4, 8, 9, 3, 2, 0, 7, 5, 6, 1]
    ====================== 1 failed, 4 passed in 0.40 seconds ======================

You get a lot of information when test fails.  It's usually enough to tell you what went wrong.

Note that pytest didn't print out the results of the print statement when the test passed, but when it failed, it printed it (under "Captured stdout call"). This means you can put diagnostic print calls in your tests, and they will not clutter up the output when they are not needed.

Testing for Exceptions
......................

One of the things you might want to test about your code is that it raises an exception when it should -- and that the exception it raises is the correct one.

In this example, if you try to call ``random.shuffle`` with an immutable sequence, such as a tuple, it should raise a ``TypeError``. Since raising an exception will generally stop the code (and cause a test to fail), we can't use an assertion to test for this.

pytest provides a "context manager", ``pytest.raises``, that can be used to test for exceptions.  The test will pass if and only if the specified Exception is raised by the enclosed code. You use it like so:

.. code-block:: python

    def test_shuffle_immutable():
        """
        Trying to shuffle an immutable sequence raises an Exception
        """
        with pytest.raises(TypeError):
            random.shuffle((1, 2, 3))

The ``with`` block is how you use a context manager -- it will run the code enclosed, and perform various actions at the end of the code, or when an exception is raised.
This is the same ``with`` as used to open files. In that case, it is used to assure that the file is properly closed when you are done with it.  In this case, the ``pytest.raises`` context manager captures any exceptions, and raises an ``AssertionError`` if no exception is raised, or if the wrong exception is raised.

In this case, the test will only pass if a ``TypeError`` is raised by the call to ``random.shuffle`` with a tuple as an argument.

The next test:

.. code-block:: python

    def test_sample_too_large():
        """
        Trying to sample more than exist should raise an error
        """
        with pytest.raises(ValueError):
            random.sample(example_seq, 20)

is very similar, except that this time, a ValueError has to be raised for the test to pass.

pytest provides a number of other features for fixtures, parameterized tests, test classes, configuration, shared resources, etc.
But simple test functions like this will get you very far.


Test Driven Development
-----------------------

Test Driven Development or "TDD", is a development process where you write tests to assure that your code works, *before* you write the actual code.

This is a very powerful approach, as it forces you to think carefully about exactly what your code should do before you start to write it. It also means that you know when you code is working, and you can refactor it in the future with assurance that you haven't broken it.

Give this exercise a try to get the idea:

:ref:`exercise_unit_testing`
