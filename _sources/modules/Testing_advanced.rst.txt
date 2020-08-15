:orphan:

.. _advanced_testing:

################
Advanced Testing
################

Testing in Python


What is testing?
================


Code which runs your application in as close to a real environment as
feasible and validates its behavior


Terminology of testing
----------------------

-  Unit tests
-  Integration tests
-  High level system tests
-  Acceptance tests
-  Black box / White box testing


"V" model and tests levels
--------------------------
.. image:: /_static/test_v_model.png


Unit testing
------------

-  Test smallest discrete units of source code
-  Tests should be independent of each other
-  Can separate tests from required resources through fixtures and
   mocking
-  Automatable
-  Integrates with the development process


What should be tested?
----------------------

The percentage of code which gets run in a test is known as the
"coverage".

100% coverage is an ideal to strive for. But the decision on when and
what to test should take into account the volatility of the project.

**NOTE** Even if every line of code is run during tests (100% coverage),
they may not be comprehensive! It is very hard to anticipate every weird
input some code may get.


Unit Testing tools
------------------

-  unittest, the test framework that ships with Python. Port of Java jUnit

   http://docs.python.org/3/library/unittest.html

-  pytest, a test runner, and also an alternative to unittest, which you should be pretty familiar with now

   http://pytest.org/latest/

-  mock, an object mocking library. Ships with Python 3.3+

   https://docs.python.org/dev/library/unittest.mock.html

Note that while mock is in the ``unittest`` package, you do not need to be using ``unittest`` tests to use it.


About Unit Testing
------------------

1. Tests should be independent.
2. Tests do not run in order, which shouldn't matter, see point 1.
3. Test fixtures are available to do any setup / teardown needed for tests.
4. Test behavior not implementation dependent.
5. Mocking is available to fake stuff you may not want to run in your tests.

This all applies regardless of your test framework

unittest
--------

The unittest framework comes with the standard library

Unittest is ported from Java's jUnit -- it is therefore OO-heavy, and
requires a lot of boilerplate code.

Many projects built custom testing Frameworks on top of it -- e.g. Django

Therefore you will encounter it

So it's good to be familiar with it.

Key missing features:

 * A test runner

   - many people use nose or pytest to run unittest tests.

 * Parameterized tests

   - there are kludges and some third-party tools for this.


unittest.TestCase anatomy
-------------------------

* create a new subclass of ``unittest.TestCase``
* name test methods ``test_foo`` so the test runner finds them
* make calls to the ``self.assert*`` family of methods to validate results

.. code-block:: python

    import unittest
    class TestMyStuff(unittest.TestCase):

        def setUp(self):
            self.x = 2

        def test_add(self):
            self.assertEqual(self.x+2, 4)

        def test_len(self):
            self.assertEqual(len('foo'), 3)

    if __name__ == '__main__':
        unittest.main()


Assert Methods
---------------

TestCase contains a number of methods named ``assert*`` which can be used
for validation, here are a few common ones:

.. code-block:: python

    assertEqual(first, second, msg=None)
    assertNotEqual(first, second, msg=None)
    assertTrue(expr, msg=None)
    assertFalse(expr, msg=None)
    assertIn(first, second)
    assertRaises(exc, fun, msg=None, *args, **kwargs)

See a full list at:

http://docs.python.org/3/library/unittest.html#assert-methods or

``dir(unittest.TestCase)`` or to get really fancy

.. code-block:: python

    [print(i) for i in dir(unittest.TestCase) if i.startswith('assert')]


Running your tests
==================

How do you actually run your tests?


running tests in a single module
--------------------------------

Call unittest.main() right in your module

.. code-block:: python

        if __name__ == "__main__":
            unittest.main()

or from the command line:

.. code-block:: bash

  python -m unittest test_my_module  # with or without .py on end

  python -m unittest test_my_module.TestClass  # particular class in a module

  python -m unittest test_my_module.TestClass.test_method  # particular test

If it gets cumbersome with many TestCases, organize the tests into a
test suite (or use a test runner, which we get to soon).

Test Suites
-----------

Test suites group test cases into a single testable unit

.. code-block:: python

    import unittest

    from calculator_test import TestCalculatorFunctions

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)

    unittest.TextTestRunner(verbosity=2).run(suite)

Tests can also be organized into suites in the

``if __name__ == "__main__":``

block


TestRunners: pytest and Nose2
-----------------------------

Nose2 is the new nose. Nose is no longer maintained, and directs users to nose2.

Both pytest and Nose2 are test runners: they auto-discover test cases.

They will find tests for you so you can focus on writing tests, not
maintaining test suites.

To find tests, pytest and nose look for modules (such as python files)
whose names start with ‘test’. In those modules, they will load tests
from all unittest.TestCase subclasses, as well as functions whose names
start with ‘test’.

So running your tests is as easy as

.. code-block:: bash

    $ pytest

or

.. code-block:: bash

    $ nose2

http://nose2.readthedocs.org/en/latest/getting_started.html#running-tests

https://docs.pytest.org/en/latest/index.html

A number of projects use nose -- so you may encounter it, but we'll focus
on pytest for now.


Fixtures: Setting up your tests for success
-------------------------------------------

(or failure!)

Test fixtures are a fixed baseline for tests to run from consistently,
also known as test context.

Fixtures can (and should) be set up fresh before each test, once before each test
case, or before an entire test suite.


Fixtures in unittest
--------------------

unittest provides fixture support via these methods:

-  setUp / tearDown - these are run before and after each test method
-  setUpClass / tearDownClass - these are run before/after each TestCase
-  setUpModule / tearDownModule - run before/after each TestSuite
-  addCleanup / doCleanups - called after tearDown,
   in case a test throws an exception

Fixtures in pytest
------------------

pytest provides a fixture system that is powerful and flexible:

https://docs.pytest.org/en/latest/fixture.html#fixture

You use a decorator to create a fixture:

.. code-block:: python

    import pytest

    @pytest.fixture
    def smtp():
        import smtplib
        return smtplib.SMTP("smtp.gmail.com")

A fixture is simply a function that will get run when it is used, and
returns *something* that your tests need:

To use a fixture, you add it as a parameter to your test function:

.. code-block:: python

    def test_ehlo(smtp):
        response, msg = smtp.ehlo()
        assert response == 250
        assert 0 # for demo purposes

The parameter gets set to the value returned by the fixture function.
The fixture function is automatically run before each test.

Let's see this in action:

:download:`pytest_fixtures.py <../examples/testing/pytest_fixtures.py>`

.. code-block:: bash

    $ pytest -s -v pytest_fixtures.py

The ``-s`` tells pytest not to capture stdout -- so we can see print statements.

The ``-v`` is verbose mode -- so we can see a bit more what is going on.

"Teardown"
-----------

If your fixture needs to clean itself up after its done, this is known as
"teardown"

To accomplish this in pytest, you use "yield", rather than "return".

The teardown code will run after the yield

.. code-block:: python

  @pytest.fixture
  def smtp(request):
      smtp = smtplib.SMTP("smtp.gmail.com")
      yield smtp  # provide the fixture value
      print("teardown smtp")
      smtp.close()

Remember that putting a yield in a function makes it a generator function -- which provides a way to halt execution of the function, return a value, and then pick up where it left off. So in this case, you use whatever code you want to generate your object -- then after the yield, all those variables will be there, so you can do whatever clean up you need to do.

See the example again for this...

Testing floating point values
=============================

Why can't we just test if .5 == 1/2 ?

.. code-block:: ipython

    In [1]: 3 * .15 == .45
    Out[1]: False

    In [2]: 3 * .15
    Out[2]: 0.44999999999999996

    In [3]: 3 * .15 * 10 / 10  == .45
    Out[3]: True

There are an infinite number of real numbers, so they are
stored as an approximation in computing hardware.

https://docs.python.org/3/tutorial/floatingpoint.html


Levels of precision of floating point
-------------------------------------

Python floating point numbers are stored in `IEEE 754 <http://en.wikipedia.org/wiki/IEEE_floating_point>`_ 64-bit double precision format, so 1 bit for the sign, 11 bits for the exponent, and the remaining 52 for the fraction.

So we can count on up to about 16 digits of precision in decimal:

.. code-block:: ipython

    In [39]: len(str(2**52))
    Out[39]: 16

    In [40]: .1+.2
    Out[40]: 0.30000000000000004

    In [41]: len('3000000000000000')
    Out[41]: 16

    # with repeated operations, the errors eventually build up:
    # here's multiplying by "1" 10 million times:
    In [64]: x=1
    In [69]: for i in range(10000000): x *= (.1 + .2)/.3
    Out [69]: 1.000000002220446


assertAlmostEqual
-----------------

assertAlmostEqual is a custom assert in ``unittest`` that verifies that two floating point values are close enough to each other.

Add a places keyword argument to specify the number of decimal places.

.. code-block:: python

    import unittest

    class TestAlmostEqual(unittest.TestCase):

        def setUp(self):
            pass

        def test_floating_point(self):
            self.assertEqual(3*.15, .45)

        def test_almost_equal(self):
            self.assertAlmostEqual(3*.15, .45, places=7)


What is close enough?
---------------------

**Warning**

``assertAlmostEqual`` lets you specify *decimal places*, i.e. the number of digits after the decimal point.

This works great for numbers that are about magnitude 1.0 (as above)

But what if you have numbers that are very large? (or small):

  - ``1.0e22``
  - ``1.0000000000001e22``

are they almost equal?

Remember that python floating point numbers store the exponent and up
to 16 decimal digits.

So those two are almost as close as you can get. But:

.. code-block:: ipython

    In [30]: x = 1e22

    In [31]: y = 1.0000000000001e22

    In [32]: '%g'%(y - x)
    Out[32]: '1.00034e+09'

They are different by about a billion!

In general, we don't want to compare floating point numbers to within a
certain number of decimal places.

Anyone remember "significant figures" from science classes?

``isclose()``
-------------

Python 3.5 introduced the ``isclose()`` function in the ``math`` module:

https://www.python.org/dev/peps/pep-0485/

.. code-block:: ipython

    In [39]: import math

    In [40]: x
    Out[40]: 1e+22

    In [41]: y
    Out[41]: 1.0000000000001e+22

    In [42]: math.isclose(x, y)
    Out[42]: True

So this works for any magnitude number.

.. code-block:: python

    is_close(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool

    Determine whether two floating point numbers are close in value.

       rel_tol
           maximum difference for being considered "close", relative to the
           magnitude of the input values
        abs_tol
           maximum difference for being considered "close", regardless of the
           magnitude of the input values

    Return True if a is close in value to b, and False otherwise.

``rel_tol`` essentially specifies how many significant figures you want:
``1e-09`` is 9 significant figures: about half of what floats can store.

``abs_tol`` is required for comparisons to zero -- nothing is
"relatively close" to zero


Using ``isclose()`` with ``unittest``
-------------------------------------

Ideally, ``TestCase`` would have an ``assertIsClose`` method.
But you can use:

.. code-block:: python

    import unittest
    from math import isclose

    class TestAlmostEqual(unittest.TestCase):

        def test_floating_point(self):
            self.assertEqual(3*.15, .45)

        def test_almost_equal(self):
            self.assertTrue( isclose( 3*.15, .45, rel_tol=7) )

**NOTE** This is one of the key flaws with the unittest module: while
it can test anything with ``assertTrue`` and the like -- if there is no
nifty ``assert*`` method for your use-case, you lose the advantages of
the ``assert*`` methods.

What are those advantages? -- mostly a prettier printing of information
in the error::

  FAIL: test_floating_point (__main__.TestAlmostEqual)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/Users/Chris/PythonStuff/UWPCE/Py300-Spring2017/Examples/testing/test_floats.py", line 17, in test_floating_point
      self.assertEqual(3 * .15, .45)
  AssertionError: 0.44999999999999996 != 0.45

But when you use assertTrue::

  FAIL: test_isclose_tiny (__main__.TestAlmostEqual)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/Users/Chris/PythonStuff/UWPCE/Py300-Spring2017/Examples/testing/test_floats.py", line 32, in test_isclose_tiny
      self.assertTrue(math.isclose(4 * .15e-30, .45e-30))
  AssertionError: False is not true

Not that helpful -- is it? I thikn we all already know that False is not true ;-)

``pytest`` give you nice informative messages when tests fail -- without special asserts.


Parameterized Tests
===================

Often you want to run exactly the same tests, but with different outputs and inputs.

You can do this a really naive way, by putting multiple asserts into one test:

.. code-block:: python

  def test_multiply():
      assert multiply(2, 2) == 4
      assert multiply(2, -1) == -4
      assert multiply(-2, -3) == 6
      assert multiply(3, 0) == 0
      assert multiply(0, 3) == 0

If they all pass, fine, but if not, it will fail on the first one,
and you'll have no idea if the others pass.

Plus, it gets a bit tedious to write, particularly if the code is more
complex than a single function call.

You can write a separate test for each case:

.. code-block:: python

  def test_multiply_both_positive():
      assert multiply(2, 2) == 4

  def test_multiply_one_negative):
      assert multiply(2, -1) == -4

  def test_multiply_both_negative():
      assert multiply(-2, -3) == 6

  def test_multiply_second_zero():
      assert multiply(3, 0) == 0

  def test_multiply_first_zero():
      assert multiply(0, 3) == 0

But talk about tedious!!!

Unfortunately, ``unittest`` does not have a built-in way to solve this problem.
There is a nifty library called parameterized, which does solve it (and they spell parameterize correctly).
It works with nose, unittest, and pytest.

https://pypi.python.org/pypi/parameterized

.. code-block:: python

    @parameterized([
        (2, 2, 4),
        (2, 3, 8),
        (1, 9, 1),
        (0, 9, 0),])
    def test_pow(base, exponent, expected):
        assert_equal(math.pow(base, exponent), expected)


You will find many more examples on their website.


``pytest.mark.parametrize``
---------------------------

With pytest, you don't need a third party library: as it provides a nifty built-in way to do it:

https://docs.pytest.org/en/latest/parametrize.html#parametrize-basics

.. code-block:: python

  param_names = "arg1, arg2, result"
  params = [(2, 2, 4),
            (2, -1, -2),
            (-2, -2, 4),
            ]
  @pytest.mark.parametrize(param_names, params)
  def test_multiply(arg1, arg2, result):
      assert multiply(arg1, arg2) == result

I find this very, very, useful.

See :download:`test_calculator_pytest.py </examples/testing/calculator/test_calculator_pytest.py>`


Code Coverage
-------------

"Coverage" is the fraction of your code that is run by your tests.
That is, how much code is "covered" by the tests.

It's usually reported as a percentage of lines of code that were run.

If a line of code is *not* run in your tests -- you can be pretty
sure it hasn't been tested -- so how do you know it works?

So 100% coverage is a good goal (though harder to achieve than you might think!)

Keep in mind that 100% coverage does **NOT** mean that your code is *fully* tested -- you have no idea how many corner cases may not have been checked.

But it's a good start.


The coverage tool
-----------------

``coverage.py`` is a tool (written by Ned Batchelder) for checking code testing
coverage in python:

https://coverage.readthedocs.io

It can be installed with ``pip``:

.. code-block:: bash

  $ python -m pip install coverage

To run coverage on your test suite:

.. code-block:: bash

  $ coverage run my_program.py arg1 arg2

This generates a .coverage file. To analyze it on the console:

.. code-block:: bash

  $ coverage report

Or you can generate an HTML report in the current directory:

.. code-block:: bash

  $ coverage html

To find out coverage across the standard library, add -L:

::

      -L, --pylib   Measure coverage even inside the Python installed
                    library, which isn't done by default.


Branch Coverage
---------------

consider the following code:

.. code-block:: python

    x = False  # 1
    if x:      # 2
        print("in branch")  # 3
    print("out of branch")  # 4

We want to make sure the branch is being bypassed correctly in the False
case

Track which branch destinations were not visited with the --branch
option to run:

.. code-block:: bash

    coverage run --branch myprog.py

http://nedbatchelder.com/code/coverage/branch.html


Using coverage with pytest
--------------------------

There is a plug-in for pytest that will run coverage for you when you run your tests:

.. code-block:: bash

    $ pip install pytest-cov

    # now it can be used
    $ pytest --cov code_module test_module.py

https://pypi.python.org/pypi/pytest-cov

There are a number of ways to invoke it and get different reports:

To get a nifty html report:

.. code-block:: bash

    $ pytest --cov code_module --cov-report html test_module.py


Doctests
========

Tests placed in docstrings to demonstrate usage of a component to a
human in a machine testable way

.. code-block:: python

    def square(x):
        """
        Squares x.

        >>> square(2)
        4
        >>> square(-2)
        4
        """
        return x * x

.. code-block:: bash

        python -m doctest -v example.py

Now generate documentation, using epydoc for example:

.. code-block:: bash

  $ epydoc example.py


http://docs.python.org/3/library/doctest.html

http://www.python.org/dev/peps/pep-0257/

http://epydoc.sourceforge.net/

These days, most Python projects use Sphinx to do their documentation:

http://sphinx-doc.org/

Well worth checking out -- and you can have Sphinx run your doctests for you.

My Take:
--------

doctests are really cool -- but they are more a way to test your documentation, than a way to test your code. Which is great -- you can have examples in your docs, and know that they are still correct.


Test Driven Development (TDD)
=============================

In TDD, the tests are written to meet the requirements before the code
exists.

Once the collection of tests passes, the requirement is considered met.

We've been trying to get you to do this from the beginning of this class :-)

We don't always want to run the entire test suite. In order to run a
single test with pytest:

.. code-block:: bash

    $ pytest -k "test_divide"

The -k means:

  only run tests which match the given substring expression. An expression is a python evaluatable expression where all names are substring-matched against test names and their parent classes.

So you can pretty easily select a subset of your tests if they have consistent naming scheme.

Exercises
=========

-  Add unit tests for each method in calculator_functions.py
-  Add fixtures via setUp/tearDown methods and setUpClass/tearDownClass
   class methods. Are they behaving how you expect?

or

-  Use pytest fixtures instead.
-  Add additional unit tests for floating point calculations
-  Fix any failures in the code
-  Add doctests to calculator_functions.py

Here are the files you'll need:

:download:`calculator.py <../examples/testing/calculator/calculator.py>`

:download:`calculator_functions.py <../examples/testing/calculator/calculator_functions.py>`

:download:`calculator_test.sh <../examples/testing/calculator/calculator_test.sh>`

:download:`test_calculator_pytest.py <../examples/testing/calculator/test_calculator_pytest.py>`

:download:`calculator_test_suite.py <../examples/testing/calculator/calculator_test_suite.py>`

:download:`test_calculator.py <../examples/testing/calculator/test_calculator.py>`


Mocking
=======

Now we've got the tools to really test
--------------------------------------

Consider the application in:

:download:`wikidef.zip <../examples/wikidef.zip>`

Give the command line utility a subject, and it will return a definition.

.. code-block:: bash

    ./define.py Robot

How can we test our application code without abusing (and waiting for)
Wikipedia?


Using Mock objects
------------------

Using Mock objects to test an application with service dependencies

Mock objects replace real objects in your code at runtime during test

This allows you to test code which calls these objects without having
their actual code run

Useful for testing objects which depend on unimplemented code, resources
which are expensive, or resources which are unavailable during test
execution

https://docs.python.org/3/library/unittest.mock-examples.html


Mocks
-----

The MagicMock class will keep track of calls to it so we can verify
that the class is being called correctly, without having to execute the
code underneath

.. code-block:: python

        from unittest import mock

        mock_object = mock.MagicMock()
        mock_object.foo.return_value = "foo return"
        print(mock_object.foo.call_count)
        print(mock_object.foo())
        print(mock_object.foo.call_count)
        # raise an exception by assigning to the side_effect attribute
        mock_object.foo.side_effect = Exception
        mock_object.foo()


Easy mocking with mock.patch
----------------------------

patch acts as a function decorator, class decorator, or a context
manager

Inside the body of the function or with statement, the target is patched
with a new object. When the function/with statement exits the patch is
undone


Using patch
-----------

::

    # patch with a decorator
    @patch.object(Wikipedia, 'article')
    def test_article_success_decorator_mocked(self, mock_method):
        article = Definitions.article("Robot")
        mock_method.assert_called_once_with("Robot")

    # patch with a context manager
    def test_article_success_context_manager_mocked(self):
        with patch.object(Wikipedia, 'article') as mock_method:
            article = Definitions.article("Robot")
            mock_method.assert_called_once_with("Robot")

There are a number of ways to use ``mock.patch`` -- this is a nice discussion of that: `The Many Flavors of mock.patch <http://treyhunner.com/2014/10/the-many-flavors-of-mock-dot-patch/>`_


mocking with pytest
-------------------

pytest uses the same mock library, but has a little different syntax.

Here is an example of mocking ``input()`` with pytest:

:download:`test_mock_input.py </examples/testing/test_mock_input.py>`

``pytest-mock`` is a utility that makes it easier to mock
with pytest.

.. code-block:: bash

   $ pip install pytest-mock

Here is a nice blog post about using it:

https://medium.com/@bfortuner/python-unit-testing-with-pytest-and-mock-197499c4623c

Exercise
........

When ``define.py`` is given the name of a non-existent article, an exception
is thrown. This exception causes another exception to occur, and the whole thing is not very readable. Why does this happen?

Use what you know about exceptions to throw a better exception, and
then add a new test that confirms this behavior. Use mock for your test, so you are not hammering Wikipedia.


Mocking a builtin
-----------------

Say you would like to mock input in this function in a file called mock_input.py:

.. code-block:: python

    def get_input():
        color = input("What is your favorite color? ")
        return color


In your test file, you would do this:

.. code-block:: python

    @mock.patch('builtins.input')
    def test_get_input(self, new_mocked_input):
        new_mocked_input.return_value = 'blue'
        self.assertEqual(mock_input.get_input(), 'blue')

Exercise
........

See if you can use mocking of the ``input()`` function to write a full set of tests for the interactive portion of your mailroom program.


