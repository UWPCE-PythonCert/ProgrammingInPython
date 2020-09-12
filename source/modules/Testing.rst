
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

.. centered:: **It gets better**

Test Frameworks
---------------

So far our tests have been limited to code in an ``if __name__ == "__main__":``
block.


* They are run *only* when the file is executed
* They are *always* run when the file is executed
* You can't do anything else when the file is executed without running tests.


This is not optimal.

You really want ways to structure your tests, and run your tests, that can be controlled and provide nifty features. You do want tests to be run often while you are developing, but they should be a specific test that is done *during* development, not when the code is running operationally.


Standard Library: ``unittest``
------------------------------

Python comes with the ``unittest`` package that provides a number of nifty features. It was introduced in version 2.1 -- so it's been around a long time.

It is more or less a port of `JUnit <https://junit.org>`_ from Java, which shows. It has a style and structure that fits Java better than Python:

It is a bit verbose: you have to write classes & methods (And we haven't covered that yet!)

But you will see it used in others' code, so it's good to be familiar with it.
And seeing how verbose it can be will help you appreciate other options.

So here's a bit of an introduction -- if the class stuff confuses you, don't worry about it -- you don't need to actually DO this yourself at this point.


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

``unittest.main()`` is called in the module where the tests are. Which means that they can be, but do not have to be, in the same file as your code.

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
            test_val1, test_val2 = 2, 3
            expected = 6
            actual = my_func(test_val1, test_val2)
            self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()

So this is pretty straightforward, but it's kind of a lot of code for just one test, yes?


Advantages of ``unittest``
--------------------------

The ``unittest`` module is pretty full featured

It comes with the standard Python distribution, no installation required.

It provides a wide variety of assertions for testing many types of results.

It allows for a "set up" and "tear down" work flow both before and after all tests and before and after each test.

It's well known and well understood.


Disadvantages of ``unittest``
-----------------------------

It's Object Oriented, and quite "heavyweight".

  - modeled after Java's ``JUnit``.

It uses the Framework design pattern, so knowing how to use the features means learning what to override.

Needing to override means you have to be cautious.

Test discovery is both inflexible and brittle.

It doesn't really take advantage of Python's introspection capabilities:
    - There are explicit "assert" methods for each type of test
    - The available assertions are not the least bit complete
    - All the assertions really do is provide pretty printing of errors

Testing for Exceptions is awkward

Test discovery is limited

And there is no built-in parameterized testing.


Other Options
-------------

Due to these limitations, folks in the Python community have developed other options for testing in Python:

* **Nose2**: https://github.com/nose-devs/nose2

* **pytest**: http://pytest.org/latest/

* ... (many frameworks supply their own test runners: e.g. Django)

Nose was the most common test runner when I first started learning testing, but it has been in maintenance mode for a while. Even the nose2 site recommends that you consider pytest.

pytest has become the defacto standard testing system for those that want a more "pythonic" and robust test framework.

pytest is very capable and widely used.

For a great description of the strengths of pytest, see:

`The Cleaning Hand of Pytest <https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684>`_

If you look above, pytest provided every feature of ``unittest`` except being in the standard library. And none of the disadvantages. It also can run ``unittest`` tests, so if you already have ``unittest`` tests, or like some of its features, you can still use pytest.

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

    **Do you have any tests?**


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
    ====================== test session starts =======================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/testing
    collected 3 items

    test_random_unitest.py ...                                 [100%]

    ======================= 3 passed in 0.03s ========================


You should have gotten similar results when you ran ``pytest`` yourself.

Take a few minutes to look this file over.

``test_random_unitest.py`` contains the tests for some of the functions in the built in``random`` module. You really don't need to test Python's built in modules -- they are already tested! This is just to demonstrate the process.


What is Happening Here?
-----------------------

Let's look again at the results of running pytest on this file:

.. code-block:: bash

    $ pytest
    ====================== test session starts =======================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/testing
    collected 3 items

    test_random_unitest.py ...                                 [100%]

    ======================= 3 passed in 0.03s ========================


When you run the ``pytest`` command, ``pytest`` starts in your current
working directory and searches the file system for things that might be tests.

It follows some simple rules:

* Any python file that starts with ``test_`` or ``_test`` is imported.

* Any functions in them that start with ``test_`` are run as tests.

* Any classes that start with ``Test`` are treated similarly, with methods that begin with ``test_`` treated as tests.

( don't worry about "classes" part just yet ;-) )

* Any ``unittest`` test cases are run.

So in this case, pytest found the ``test_random_unitest.py`` file and in that file, found the ``TestSequenceFunctions`` TestCase class, and ran the tests defined in that class. In this case, there were three of them, and they all passed.

pytest
------

The pytest test framework is simple, flexible and configurable.

Read the documentation for more information:

https://docs.pytest.org

Those docs are a bit intimidating, but with pytest, as they say:

.. centered::  "The easy stuff is easy, and the hard stuff is possible"

-- and you can get very far with the easy stuff.

In addition to finding and running tests, it makes writing tests simple, and provides a bunch of nifty utilities to support more complex testing.

To give this a try, download this file:

:download:`test_random_pytest.py <../examples/testing/test_random_pytest.py>`

And run pytest again on this file:

.. code-block:: bash

    $ pytest test_random_pytest.py
    ====================== test session starts =======================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/testing
    collected 5 items

    test_random_pytest.py .....                                [100%]

    ======================= 5 passed in 0.02s ========================

Note that if you had not passed in the filename, it would have run the tests in both the test files.


pytest tests
------------

Now take a look at ``test_random_pytest.py`` -- It is essentially the same tests -- but written in native pytest style -- simple test functions, rather than classes and special assertions.

The beauty of pytest is that it takes advantage of Python's dynamic nature -- you don't need to use any particular structure to write tests, and you don't need to use special assertions to get good reporting.

* Any function named appropriately is a test.

* If the function doesn't raise an Exception or fail an assertion, the test passes.

It's that simple.

Look at ``test_random_pytest.py`` to see how this works.

.. code-block:: python

    import random
    import pytest

The ``random`` module is imported because that's what we are testing.
``pytest`` only needs to be imported if you are using its utilities -- more on this in a moment.

.. code-block:: python

    example_seq = list(range(10))

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

And this is pretty much the same thing, except that it loops to make sure that every item returned by ``.sample()`` is in the original sequence.

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

Then the "real work": calling ``random.shuffle`` on the sequence. This should re-arrange the elements without adding or losing any.

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

Note that pytest didn't print out the results of the print statement when the test passed, but when it failed, it printed it (under "Captured stdout call"). This means you can put diagnostic print calls in your tests, and they will not clutter up the output when they are not needed. This is *very* helpful!


Testing for Exceptions
......................

One of the things you might want to test about your code is that it raises an Exception when it should -- and that the Exception it raises is the correct one.

In this example, if you try to call ``random.shuffle`` with an immutable sequence, such as a tuple, it should raise a ``TypeError``. Since raising an Exception will generally stop the code (and cause a test to fail), we can't use an assertion to test for this.

pytest provides a "context manager", ``pytest.raises()``, that can be used to test for Exceptions.  The test will pass if and only if the specified Exception is raised by the enclosed code. You use it like so:

.. code-block:: python

    def test_shuffle_immutable():
        """
        Trying to shuffle an immutable sequence raises an Exception
        """
        with pytest.raises(TypeError):
            random.shuffle((1, 2, 3))

The ``with`` block is how you use a context manager -- it will run the code in the following block,
and perform various actions at the end of the code, or when an Exception is raised.
This is the same ``with`` as used to open files. In that case, it is used to assure that the file is properly closed when you are done with it.
In this case, the ``pytest.raises()`` context manager captures any Exceptions, and raises an ``AssertionError`` if no Exception is raised, or if the wrong Exception is raised.

In this case, the test will only pass if a ``TypeError`` is raised by the call to ``random.shuffle()`` with a tuple as an argument.

Try changing that to a different Exception and see what happens:

.. code-block:: python

    def test_shuffle_immutable():
        """
        Trying to shuffle an immutable sequence raises an Exception
        """
        with pytest.raises(ValueError):
            random.shuffle((1, 2, 3))

I get a lot of context information, concluding with::

    ==================== short test summary info =====================
    FAILED test_random_pytest.py::test_shuffle_immutable - TypeErro...
    ================== 1 failed, 4 passed in 0.18s ===================

So you got an Exception -- but not the one expected -- so the test failed.


The next test:

.. code-block:: python

    def test_sample_too_large():
        """
        Trying to sample more than exist should raise an error
        """
        with pytest.raises(ValueError):
            random.sample(example_seq, 20)

is very similar, except that this time, a ``ValueError`` has to be raised for the test to pass.

pytest provides a number of other features for fixtures, parameterized tests, test classes, configuration, shared resources, etc. If you want to learn more about that, read the pytest documentation, and this introduction to more advanced concepts: :ref:`advanced_testing`


But simple test functions like this will get you very far.


Test Driven Development
-----------------------

Test Driven Development or "TDD", is a development process where you write tests to assure that your code works, *before* you write the actual code.

This is a very powerful approach, as it forces you to think carefully about exactly what your code should do before you start to write it. It also means that you know when you code is working, and you can refactor it in the future with assurance that you haven't broken it.

Give this exercise a try to get the idea:

:ref:`exercise_unit_testing`
