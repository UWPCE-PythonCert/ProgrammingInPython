
.. _unit_testing:

#######################
Test Driven Development
#######################

"Testing" is any strategy for making sure your code behaves as expected. "Unit Testing" is a particular strategy, that:

* is easy to run in an automated fashion.
* utilized isolated tests for each individual

"Test Driven Development" (TDD) is a development strategy that integrates the development of unit tests with the code itself. In particular, you write the tests *before* you write the code, which seems pretty backward, but it has some real strengths.

We'll demonstrate this technique with an example.

Unit testing - Dive Into Python 3
 
The Following is adapted from Mark Pilgram's excellent "Dive into Python"

https://diveintopython3.problemsolving.io/

The primary difference is that this version uses the simpler pytest testing framework, rather than `unittest`, which is discussed in: :ref:`unit_testing`_

Unit Testing
============

   | ❝ Certitude is not the test of certainty. We have been cocksure of
     many things that were not so. ❞
   | — `Oliver Wendell Holmes,
     Jr. <http://en.wikiquote.org/wiki/Oliver_Wendell_Holmes,_Jr.>`__


(Not) Diving In
---------------

Kids today. So spoiled by these fast computers and fancy “dynamic”
languages. Write first, ship second, debug third (if ever). In my day,
we had discipline. Discipline, I say! We had to write programs by
*hand*, on *paper*, and feed them to the computer on *punchcards*. And
we *liked it!*

In this module, you’re going to write and debug a set of utility
functions to convert to and from Roman numerals.

You’ve most likely seen Roman numerals, even if you didn’t recognize them. You may have seen them in copyrights of old movies and television shows (“Copyright MCMXLVI” instead of “Copyright 1946”), or on the dedication walls of libraries or universities (“established MDCCCLXXXVIII” instead of “established 1888”). You may also have seen them in outlines and bibliographical references. It’s a system of representing numbers that really does date back to the ancient Roman empire (hence the name).


The Rules for Roman Numerals
----------------------------

In Roman numerals, there are seven characters that are repeated and combined in various ways to represent numbers.

|    I = 1
|    V = 5
|    X = 10
|    L = 50
|    C = 100
|    D = 500
|    M = 1000

The following are some general rules for constructing Roman numerals:

* Sometimes characters are additive. I is 1, II is 2, and III is 3. VI is 6 (literally, “5 and 1”), VII is 7, and VIII is 8.


* The tens characters (I, X, C, and M) can be repeated up to three times. At 4, you need to subtract from the next highest fives character. You can't represent 4 as IIII; instead, it is represented as IV (“1 less than 5”). 40 is written as XL (“10 less than 50”), 41 as XLI, 42 as XLII, 43 as XLIII, and then 44 as XLIV (“10 less than 50, then 1 less than 5”).


* Sometimes characters are ... the opposite of additive. By putting certain characters before others, you subtract from the final value. For example, at 9, you need to subtract from the next highest tens character: 8 is VIII, but 9 is IX (“1 less than 10”), not VIIII (since the I character can not be repeated four times). 90 is XC, 900 is CM.

* The fives characters can not be repeated. 10 is always represented as X, never as VV. 100 is always C, never LL.

* Roman numerals are read left to right, so the order of characters matters very much. DC is 600; CD is a completely different number (400, “100 less than 500”). CI is 101; IC is not even a valid Roman numeral (because you can't subtract 1 directly from 100; you would need to write it as XCIX, “10 less than 100, then 1 less than 10”).


The rules for Roman numerals lead to a number of interesting observations:

#. There is only one correct way to represent a particular number as a
   Roman numeral.
#. The converse is also true: if a string of characters is a valid Roman
   numeral, it represents only one number (that is, it can only be
   interpreted one way).
#. There is a limited range of numbers that can be expressed as Roman
   numerals, specifically ``1`` through ``3999``. The Romans did have
   several ways of expressing larger numbers, for instance by having a
   bar over a numeral to represent that its normal value should be
   multiplied by ``1000``. For the purposes of this exercise, let’s
   stipulate that Roman numerals go from ``1`` to ``3999``.
#. There is no way to represent 0 in Roman numerals.
#. There is no way to represent negative numbers in Roman numerals.
#. There is no way to represent fractions or non-integer numbers in
   Roman numerals.

Let’s start mapping out what a ``roman.py`` module should do. It will
have two main functions, ``to_roman()`` and ``from_roman()``. The
``to_roman()`` function should take an integer from ``1`` to ``3999``
and return the Roman numeral representation as a string ...

Stop right there. Now let’s do something a little unexpected: write a
test case that checks whether the ``to_roman()`` function does what you
want it to. You read that right: you’re going to write code that tests
code that you haven’t written yet.

This is called *test-driven development*, or TDD. The set of two
conversion functions — ``to_roman()``, and later ``from_roman()`` — can
be written and tested as a unit, separate from any larger program that
uses them. Technically, you can write unit tests with plain Python -- recall the ``assert`` statement that you have already used to write simple tests. But it is very helpful to use a framework to make it easier to write and run your tests. In this program, we use the `pytest` package: it is both very easy to get started with, and provides a lot of powerful features to aide in testing complex systems.

.. note:: `pytest` does not come with Python out of the box. But it is easily installable via `pip` (or conda, if you are using conda)
  ``python -m pip install pytest`` Once installed, you have the pytest command available in your terminal.

FIXME: Add a page maybe on installing and using pytest?

Unit testing is an important part of an overall testing-centric
development strategy. If you write unit tests, it is important to write
them early and to keep them updated as code and requirements change.
Many people advocate writing tests before they write the code they’re
testing, and that’s the style I’m going to demonstrate here.

But unit tests are beneficial, even critical, no matter when you write them.

-  Before writing code, writing unit tests forces you to detail your
   requirements in a useful fashion.
-  While writing code, unit tests keep you from over-coding. When all
   the test cases pass, the function is complete.
-  When refactoring code, they can help prove that the new version
   behaves the same way as the old version.
-  When maintaining code, having tests will help you cover your ass when
   someone comes screaming that your latest change broke their old code.
   (“But *sir*, all the unit tests passed when I checked it in...”)
-  When writing code in a team, having a comprehensive test suite
   dramatically decreases the chances that your code will break someone
   else’s code, because you can run their unit tests first. (I’ve seen
   this sort of thing in code sprints. A team breaks up the assignment,
   everybody takes the specs for their task, writes unit tests for it,
   then shares their unit tests with the rest of the team. That way,
   nobody goes off too far into developing code that doesn’t play well
   with others.)

A Single Question
-----------------

.. note:: Every Test is an Island.

A test case answers a single question about the code it is testing. A
test case should be able to...

- run completely by itself, without any human input. Unit testing is
  about automation.
- determine by itself whether the function it is testing has passed
  or failed, without a human interpreting the results.
- run in isolation, separate from any other test cases (even if they
  test the same functions). Each test case is an island.

Given that, let’s build a test case for the first requirement:

1. The ``to_roman()`` function should return the Roman numeral
   representation for all integers ``1`` to ``3999``.

Let's take a look at
:download:`roman.py <source/examples/test_driven_development/roman.py>`.

.. code-block:: python

"""
    KNOWN_VALUES = ((1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                         (9, 'IX'),
                         (10, 'X'),
                         (50, 'L'),
                         (100, 'C'),
                         (500, 'D'),
                         (1000, 'M'),
                    ...
                         (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values():
            """
            to_roman should give known result with known input
            """
            for integer, numeral in KNOWN_VALUES
                result = roman1.to_roman(integer)
                assert numeral == result

It is not immediately obvious how this code does ... well, *anything*.
It defines a big data structure full of examples (download the
:download:`roman.py <source/examples/test_driven_development/roman.py>`
file to see the full set), and a single function.

The entire script has no ``__main__`` block, so even that one function won't run. But it does do something, I promise.

`KNOWN_VALUES` is a tuple of integer/numeral pairs that were verified manually. It includes the lowest ten numbers, the highest number, every number
that translates to a single-character Roman numeral, and a random sampling of other valid numbers.
You don’t need to test every possible input, but you should try to test all the obvious edge cases.

..note:: This is a major challenge of unit testing -- how to catch all the edge cases, without over testing every little thing.

`pytest` makes it really simple to write a test case: simply define a function named ``test_anything``. pytest will identify any function with: "``test_``"" at the start of the name as a test function.

* Every individual test is its own function. A test function takes no
   parameters, returns no value, and must have a name beginning with the
   five letters ``test_``. If a test function exits normally without
   a failing assertion or other exception, the test is considered passed; if the function raises a failed assertion, failed.

In the ``test_to_roman_known_values`` function, you call the actual ``to_roman()`` function. (Well, the function hasn’t been written yet, but once it is, this is the line that will call it).
Notice that you have now defined the API for the ``to_roman()`` function: it must take an integer (the number to convert) and return a string (the Roman numeral representation). If the API is different than that, this test is considered failed.

.. Also notice that you are not trapping any exceptions when you call ``to_roman()``. This is intentional. ``to_roman()`` shouldn’t raise
..    an exception when you call it with valid input, and these input
..    values are all valid. If ``to_roman()`` raises an exception, this
..    test is considered failed.

Assuming the ``to_roman()`` function was defined correctly, called
correctly, completed successfully, and returned a value, the last
step is to check whether it returned the *right* value. This is
accomplished with a simple assertion that the returned value is
equal to the known correct value:

.. code-block:: python

    assert numeral == result

If the assertion fails, the test fails.

Note that in this case, we are looping through all the known values, testing each on in the loop. If any of the known values fails, the test will fail, and end the test function -- the rest of the values will not be tested.

If every value returned from``to_roman()`` matches the known value you expect, the assert will never fail, and ``test_to_roman_known_values``
eventually exits normally, which means ``to_roman()`` has passed this
test.


Write a test that fails, then code until it passes.
...................................................

Once you have a test case, you can start coding the ``to_roman()``
function. First, you should stub it out as an empty function and make
sure the tests fail. If the tests succeed before you’ve written any
code, your tests aren’t testing your code at all! Unit testing is a
dance: tests lead, code follows. Write a test that fails, then code
until it passes.

For a small system like this, we can put the code and the tests in the same file. But as you build larger systems, it is customary to put the tests in a separate file -- more on that later.

You can actually try your tests out before even writing any code!

To run tests with pytest, you pass in the test file on the command line:

.. code-block:: bash

    $ pytest roman.py
    =========================== test session starts ===========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 1 item

    roman.py F                                                          [100%]

    ================================ FAILURES =================================
    _______________________ test_to_roman_known_values ________________________

        def test_to_roman_known_values():
            """
            to_roman should give known result with known input
            """
            for integer, numeral in KNOWN_VALUES:
    >           result = roman1.to_roman(integer)
    E           NameError: name 'roman1' is not defined

    roman.py:75: NameError
    ========================= short test summary info =========================
    FAILED roman.py::test_to_roman_known_values - NameError: name 'roman1' i...
    ============================ 1 failed in 0.14s ============================

There's a lot going on here! pytest has found your test function, sets itself up and run the tests it finds (in this case only the one). Then it runs the test (which in this case fails), and reports the failure(s). Along with the fact that it fails, tells you why it failed (a NameError) where it failed (line 75 of the file), and shows you the code before the test failure. This may seem like a lot of information for such a simple case, but it can be invaluable in a more complex system.



.. code-block:: python

   # roman1.py

   def to_roman(n):
       '''convert integer to Roman numeral'''
       pass                                   ①

#. At this stage, you want to define the API of the ``to_roman()``
   function, but you don’t want to code it yet. (Your test needs to fail
   first.) To stub it out, use the Python reserved word ``pass``, which
   does precisely nothing.

Execute ``romantest1.py`` on the command line to run the test. If you
call it with the ``-v`` command-line option, it will give more verbose
output so you can see exactly what’s going on as each test case runs.
With any luck, your output should look like this:

.. code:: screen

   you@localhost:~/diveintopython3/examples$ python3 romantest1.py -v
   test_to_roman_known_values (__main__.KnownValues)                      ①
   to_roman should give known result with known input ... FAIL            ②

   ======================================================================
   FAIL: to_roman should give known result with known input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest1.py", line 73, in test_to_roman_known_values
       self.assertEqual(numeral, result)
   AssertionError: 'I' != None                                            ③

   ----------------------------------------------------------------------
   Ran 1 test in 0.016s                                                   ④

   FAILED (failures=1)                                                    ⑤

#. Running the script runs ``unittest.main()``, which runs each test
   case. Each test case is a method within a class in ``romantest.py``.
   There is no required organization of these test classes; they can
   each contain a single test method, or you can have one class that
   contains multiple test methods. The only requirement is that each
   test class must inherit from ``unittest.TestCase``.
#. For each test case, the ``unittest`` module will print out the
   ``docstring`` of the method and whether that test passed or failed.
   As expected, this test case fails.
#. For each failed test case, ``unittest`` displays the trace
   information showing exactly what happened. In this case, the call to
   ``assertEqual()`` raised an ``AssertionError`` because it was
   expecting ``to_roman(1)`` to return ``'I'``, but it didn’t. (Since
   there was no explicit return statement, the function returned
   ``None``, the Python null value.)
#. After the detail of each test, ``unittest`` displays a summary of how
   many tests were performed and how long it took.
#. Overall, the test run failed because at least one test case did not
   pass. When a test case doesn’t pass, ``unittest`` distinguishes
   between failures and errors. A failure is a call to an ``assertXYZ``
   method, like ``assertEqual`` or ``assertRaises``, that fails because
   the asserted condition is not true or the expected exception was not
   raised. An error is any other sort of exception raised in the code
   you’re testing or the unit test case itself.

*Now*, finally, you can write the ``to_roman()`` function.

[`download ``roman1.py`` <examples/roman1.py>`__]

.. code:: pp

   roman_numeral_map = (('M',  1000),
                        ('CM', 900),
                        ('D',  500),
                        ('CD', 400),
                        ('C',  100),
                        ('XC', 90),
                        ('L',  50),
                        ('XL', 40),
                        ('X',  10),
                        ('IX', 9),
                        ('V',  5),
                        ('IV', 4),
                        ('I',  1))                 ①

   def to_roman(n):
       '''convert integer to Roman numeral'''
       result = ''
       for numeral, integer in roman_numeral_map:
           while n >= integer:                     ②
               result += numeral
               n -= integer
       return result

#. ``roman_numeral_map`` is a tuple of tuples which defines three
   things: the character representations of the most basic Roman
   numerals; the order of the Roman numerals (in descending value order,
   from ``M`` all the way down to ``I``); the value of each Roman
   numeral. Each inner tuple is a pair of ``(numeral, value)``. It’s not
   just single-character Roman numerals; it also defines two-character
   pairs like ``CM`` (“one hundred less than one thousand”). This makes
   the ``to_roman()`` function code simpler.
#. Here’s where the rich data structure of ``roman_numeral_map`` pays
   off, because you don’t need any special logic to handle the
   subtraction rule. To convert to Roman numerals, simply iterate
   through ``roman_numeral_map`` looking for the largest integer value
   less than or equal to the input. Once found, add the Roman numeral
   representation to the end of the output, subtract the corresponding
   integer value from the input, lather, rinse, repeat.

If you’re still not clear how the ``to_roman()`` function works, add a
``print()`` call to the end of the ``while`` loop:

.. code:: nd

   while n >= integer:
       result += numeral
       n -= integer
       print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))

With the debug ``print()`` statements, the output looks like this:

.. code:: nd

   >>> import roman1
   >>> roman1.to_roman(1424)
   subtracting 1000 from input, adding M to output
   subtracting 400 from input, adding CD to output
   subtracting 10 from input, adding X to output
   subtracting 10 from input, adding X to output
   subtracting 4 from input, adding IV to output
   'MCDXXIV'

So the ``to_roman()`` function appears to work, at least in this manual
spot check. But will it pass the test case you wrote?

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest1.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok               ①

   ----------------------------------------------------------------------
   Ran 1 test in 0.016s

   OK

#. Hooray! The ``to_roman()`` function passes the “known values” test
   case. It’s not comprehensive, but it does put the function through
   its paces with a variety of inputs, including inputs that produce
   every single-character Roman numeral, the largest possible input
   (``3999``), and the input that produces the longest possible Roman
   numeral (``3888``). At this point, you can be reasonably confident
   that the function works for any good input value you could throw at
   it.

“Good” input? Hmm. What about bad input?

⁂

.. _romantest2:

“Halt And Catch Fire”
---------------------

The Pythonic way to halt and catch fire is to raise an exception.

It is not enough to test that functions succeed when given good input;
you must also test that they fail when given bad input. And not just any
sort of failure; they must fail in the way you expect.

.. code:: screen

   >>> import roman1
   >>> roman1.to_roman(4000)
   'MMMM'
   >>> roman1.to_roman(5000)
   'MMMMM'
   >>> roman1.to_roman(9000)  ①
   'MMMMMMMMM'

#. That’s definitely not what you wanted — that’s not even a valid Roman
   numeral! In fact, each of these numbers is outside the range of
   acceptable input, but the function returns a bogus value anyway.
   Silently returning bad values is *baaaaaaad*; if a program is going
   to fail, it is far better if it fails quickly and noisily. “Halt and
   catch fire,” as the saying goes. The Pythonic way to halt and catch
   fire is to raise an exception.

The question to ask yourself is, “How can I express this as a testable
requirement?” How’s this for starters:

   The ``to_roman()`` function should raise an ``OutOfRangeError`` when
   given an integer greater than ``3999``.

What would that test look like?

[`download ``romantest2.py`` <examples/romantest2.py>`__]

.. code:: pp

   import unittest, roman2
   class ToRomanBadInput(unittest.TestCase):                                 ①
       def test_too_large(self):                                             ②
           '''to_roman should fail with large input'''
           self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 4000)  ③

#. Like the previous test case, you create a class that inherits from
   ``unittest.TestCase``. You can have more than one test per class (as
   you’ll see later in this chapter), but I chose to create a new class
   here because this test is something different than the last one.
   We’ll keep all the good input tests together in one class, and all
   the bad input tests together in another.
#. Like the previous test case, the test itself is a method of the
   class, with a name starting with ``test``.
#. The ``unittest.TestCase`` class provides the ``assertRaises`` method,
   which takes the following arguments: the exception you’re expecting,
   the function you’re testing, and the arguments you’re passing to that
   function. (If the function you’re testing takes more than one
   argument, pass them all to ``assertRaises``, in order, and it will
   pass them right along to the function you’re testing.)

Pay close attention to this last line of code. Instead of calling
``to_roman()`` directly and manually checking that it raises a
particular exception (by wrapping it in `a ``try...except``
block <your-first-python-program.html#exceptions>`__), the
``assertRaises`` method has encapsulated all of that for us. All you do
is tell it what exception you’re expecting (``roman2.OutOfRangeError``),
the function (``to_roman()``), and the function’s arguments (``4000``).
The ``assertRaises`` method takes care of calling ``to_roman()`` and
checking that it raises ``roman2.OutOfRangeError``.

Also note that you’re passing the ``to_roman()`` function itself as an
argument; you’re not calling it, and you’re not passing the name of it
as a string. Have I mentioned recently how handy it is that `everything
in Python is an
object <your-first-python-program.html#everythingisanobject>`__?

So what happens when you run the test suite with this new test?

.. code:: screen

   you@localhost:~/diveintopython3/examples$ python3 romantest2.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok
   test_too_large (__main__.ToRomanBadInput)
   to_roman should fail with large input ... ERROR                         ①

   ======================================================================
   ERROR: to_roman should fail with large input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest2.py", line 78, in test_too_large
       self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 4000)
   AttributeError: 'module' object has no attribute 'OutOfRangeError'      ②

   ----------------------------------------------------------------------
   Ran 2 tests in 0.000s

   FAILED (errors=1)

#. You should have expected this to fail (since you haven’t written any
   code to pass it yet), but... it didn’t actually “fail,” it had an
   “error” instead. This is a subtle but important distinction. A unit
   test actually has *three* return values: pass, fail, and error. Pass,
   of course, means that the test passed — the code did what you
   expected. “Fail” is what the previous test case did (until you wrote
   code to make it pass) — it executed the code but the result was not
   what you expected. “Error” means that the code didn’t even execute
   properly.
#. Why didn’t the code execute properly? The traceback tells all. The
   module you’re testing doesn’t have an exception called
   ``OutOfRangeError``. Remember, you passed this exception to the
   ``assertRaises()`` method, because it’s the exception you want the
   function to raise given an out-of-range input. But the exception
   doesn’t exist, so the call to the ``assertRaises()`` method failed.
   It never got a chance to test the ``to_roman()`` function; it didn’t
   get that far.

To solve this problem, you need to define the ``OutOfRangeError``
exception in ``roman2.py``.

.. code:: pp

   class OutOfRangeError(ValueError):  ①
       pass                            ②

#. Exceptions are classes. An “out of range” error is a kind of value
   error — the argument value is out of its acceptable range. So this
   exception inherits from the built-in ``ValueError`` exception. This
   is not strictly necessary (it could just inherit from the base
   ``Exception`` class), but it feels right.
#. Exceptions don’t actually do anything, but you need at least one line
   of code to make a class. Calling ``pass`` does precisely nothing, but
   it’s a line of Python code, so that makes it a class.

Now run the test suite again.

.. code:: screen

   you@localhost:~/diveintopython3/examples$ python3 romantest2.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok
   test_too_large (__main__.ToRomanBadInput)
   to_roman should fail with large input ... FAIL                          ①

   ======================================================================
   FAIL: to_roman should fail with large input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest2.py", line 78, in test_too_large
       self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 4000)
   AssertionError: OutOfRangeError not raised by to_roman                 ②

   ----------------------------------------------------------------------
   Ran 2 tests in 0.016s

   FAILED (failures=1)

#. The new test is still not passing, but it’s not returning an error
   either. Instead, the test is failing. That’s progress! It means the
   call to the ``assertRaises()`` method succeeded this time, and the
   unit test framework actually tested the ``to_roman()`` function.
#. Of course, the ``to_roman()`` function isn’t raising the
   ``OutOfRangeError`` exception you just defined, because you haven’t
   told it to do that yet. That’s excellent news! It means this is a
   valid test case — it fails before you write the code to make it pass.

Now you can write the code to make this test pass.

[`download ``roman2.py`` <examples/roman2.py>`__]

.. code:: pp

   def to_roman(n):
       '''convert integer to Roman numeral'''
       if n > 3999:
           raise OutOfRangeError('number out of range (must be less than 4000)')  ①

       result = ''
       for numeral, integer in roman_numeral_map:
           while n >= integer:
               result += numeral
               n -= integer
       return result

#. This is straightforward: if the given input (``n``) is greater than
   ``3999``, raise an ``OutOfRangeError`` exception. The unit test does
   not check the human-readable string that accompanies the exception,
   although you could write another test that did check it (but watch
   out for internationalization issues for strings that vary by the
   user’s language or environment).

Does this make the test pass? Let’s find out.

.. code:: screen

   you@localhost:~/diveintopython3/examples$ python3 romantest2.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok
   test_too_large (__main__.ToRomanBadInput)
   to_roman should fail with large input ... ok                            ①

   ----------------------------------------------------------------------
   Ran 2 tests in 0.000s

   OK

#. Hooray! Both tests pass. Because you worked iteratively, bouncing
   back and forth between testing and coding, you can be sure that the
   two lines of code you just wrote were the cause of that one test
   going from “fail” to “pass.” That kind of confidence doesn’t come
   cheap, but it will pay for itself over the lifetime of your code.

⁂

.. _romantest3:

More Halting, More Fire
-----------------------

Along with testing numbers that are too large, you need to test numbers
that are too small. As `we noted in our functional
requirements <#divingin>`__, Roman numerals cannot express 0 or negative
numbers.

.. code:: nd

   >>> import roman2
   >>> roman2.to_roman(0)
   ''
   >>> roman2.to_roman(-1)
   ''

Well *that’s* not good. Let’s add tests for each of these conditions.

[`download ``romantest3.py`` <examples/romantest3.py>`__]

.. code:: pp

   class ToRomanBadInput(unittest.TestCase):
       def test_too_large(self):
           '''to_roman should fail with large input'''
           self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, 4000)  ①

       def test_zero(self):
           '''to_roman should fail with 0 input'''
           self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, 0)     ②

       def test_negative(self):
           '''to_roman should fail with negative input'''
           self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, -1)    ③

#. The ``test_too_large()`` method has not changed since the previous
   step. I’m including it here to show where the new code fits.
#. Here’s a new test: the ``test_zero()`` method. Like the
   ``test_too_large()`` method, it tells the ``assertRaises()`` method
   defined in ``unittest.TestCase`` to call our ``to_roman()`` function
   with a parameter of 0, and check that it raises the appropriate
   exception, ``OutOfRangeError``.
#. The ``test_negative()`` method is almost identical, except it passes
   ``-1`` to the ``to_roman()`` function. If either of these new tests
   does *not* raise an ``OutOfRangeError`` (either because the function
   returns an actual value, or because it raises some other exception),
   the test is considered failed.

Now check that the tests fail:

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest3.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok
   test_negative (__main__.ToRomanBadInput)
   to_roman should fail with negative input ... FAIL
   test_too_large (__main__.ToRomanBadInput)
   to_roman should fail with large input ... ok
   test_zero (__main__.ToRomanBadInput)
   to_roman should fail with 0 input ... FAIL

   ======================================================================
   FAIL: to_roman should fail with negative input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest3.py", line 86, in test_negative
       self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, -1)
   AssertionError: OutOfRangeError not raised by to_roman

   ======================================================================
   FAIL: to_roman should fail with 0 input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest3.py", line 82, in test_zero
       self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, 0)
   AssertionError: OutOfRangeError not raised by to_roman

   ----------------------------------------------------------------------
   Ran 4 tests in 0.000s

   FAILED (failures=2)

Excellent. Both tests failed, as expected. Now let’s switch over to the
code and see what we can do to make them pass.

[`download ``roman3.py`` <examples/roman3.py>`__]

.. code:: pp

   def to_roman(n):
       '''convert integer to Roman numeral'''
       if not (0 < n < 4000):                                              ①
           raise OutOfRangeError('number out of range (must be 1..3999)')  ②

       result = ''
       for numeral, integer in roman_numeral_map:
           while n >= integer:
               result += numeral
               n -= integer
       return result

#. This is a nice Pythonic shortcut: multiple comparisons at once. This
   is equivalent to ``if not ((0 < n) and (n < 4000))``, but it’s much
   easier to read. This one line of code should catch inputs that are
   too large, negative, or zero.
#. If you change your conditions, make sure to update your
   human-readable error strings to match. The ``unittest`` framework
   won’t care, but it’ll make it difficult to do manual debugging if
   your code is throwing incorrectly-described exceptions.

I could show you a whole series of unrelated examples to show that the
multiple-comparisons-at-once shortcut works, but instead I’ll just run
the unit tests and prove it.

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest3.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok
   test_negative (__main__.ToRomanBadInput)
   to_roman should fail with negative input ... ok
   test_too_large (__main__.ToRomanBadInput)
   to_roman should fail with large input ... ok
   test_zero (__main__.ToRomanBadInput)
   to_roman should fail with 0 input ... ok

   ----------------------------------------------------------------------
   Ran 4 tests in 0.016s

   OK

⁂

.. _romantest4:

And One More Thing…
-------------------

There was one more `functional requirement <#divingin>`__ for converting
numbers to Roman numerals: dealing with non-integers.

.. code:: screen

   >>> import roman3
   >>> roman3.to_roman(0.5)  ①
   ''
   >>> roman3.to_roman(1.0)  ②
   'I'

#. Oh, that’s bad.
#. Oh, that’s even worse. Both of these cases should raise an exception.
   Instead, they give bogus results.

Testing for non-integers is not difficult. First, define a
``NotIntegerError`` exception.

.. code:: nd

   # roman4.py
   class OutOfRangeError(ValueError): pass
   class NotIntegerError(ValueError): pass

Next, write a test case that checks for the ``NotIntegerError``
exception.

.. code:: nd

   class ToRomanBadInput(unittest.TestCase):
       .
       .
       .
       def test_non_integer(self):
           '''to_roman should fail with non-integer input'''
           self.assertRaises(roman4.NotIntegerError, roman4.to_roman, 0.5)

Now check that the test fails properly.

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest4.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok
   test_negative (__main__.ToRomanBadInput)
   to_roman should fail with negative input ... ok
   test_non_integer (__main__.ToRomanBadInput)
   to_roman should fail with non-integer input ... FAIL
   test_too_large (__main__.ToRomanBadInput)
   to_roman should fail with large input ... ok
   test_zero (__main__.ToRomanBadInput)
   to_roman should fail with 0 input ... ok

   ======================================================================
   FAIL: to_roman should fail with non-integer input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest4.py", line 90, in test_non_integer
       self.assertRaises(roman4.NotIntegerError, roman4.to_roman, 0.5)
   AssertionError: NotIntegerError not raised by to_roman

   ----------------------------------------------------------------------
   Ran 5 tests in 0.000s

   FAILED (failures=1)

Write the code that makes the test pass.

.. code:: pp

   def to_roman(n):
       '''convert integer to Roman numeral'''
       if not (0 < n < 4000):
           raise OutOfRangeError('number out of range (must be 1..3999)')
       if not isinstance(n, int):                                          ①
           raise NotIntegerError('non-integers can not be converted')      ②

       result = ''
       for numeral, integer in roman_numeral_map:
           while n >= integer:
               result += numeral
               n -= integer
       return result

#. The built-in ``isinstance()`` function tests whether a variable is a
   particular type (or, technically, any descendant type).
#. If the argument ``n`` is not an ``int``, raise our newly minted
   ``NotIntegerError`` exception.

Finally, check that the code does indeed make the test pass.

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest4.py -v
   test_to_roman_known_values (__main__.KnownValues)
   to_roman should give known result with known input ... ok
   test_negative (__main__.ToRomanBadInput)
   to_roman should fail with negative input ... ok
   test_non_integer (__main__.ToRomanBadInput)
   to_roman should fail with non-integer input ... ok
   test_too_large (__main__.ToRomanBadInput)
   to_roman should fail with large input ... ok
   test_zero (__main__.ToRomanBadInput)
   to_roman should fail with 0 input ... ok

   ----------------------------------------------------------------------
   Ran 5 tests in 0.000s

   OK

The ``to_roman()`` function passes all of its tests, and I can’t think
of any more tests, so it’s time to move on to ``from_roman()``.

⁂

.. _romantest5:

A Pleasing Symmetry
-------------------

Converting a string from a Roman numeral to an integer sounds more
difficult than converting an integer to a Roman numeral. Certainly there
is the issue of validation. It’s easy to check if an integer is greater
than 0, but a bit harder to check whether a string is a valid Roman
numeral. But we already constructed `a regular expression to check for
Roman numerals <regular-expressions.html#romannumerals>`__, so that part
is done.

That leaves the problem of converting the string itself. As we’ll see in
a minute, thanks to the rich data structure we defined to map individual
Roman numerals to integer values, the nitty-gritty of the
``from_roman()`` function is as straightforward as the ``to_roman()``
function.

But first, the tests. We’ll need a “known values” test to spot-check for
accuracy. Our test suite already contains `a mapping of known
values <#romantest1>`__; let’s reuse that.

.. code:: nd

       def test_from_roman_known_values(self):
           '''from_roman should give known result with known input'''
           for integer, numeral in self.known_values:
               result = roman5.from_roman(numeral)
               self.assertEqual(integer, result)

There’s a pleasing symmetry here. The ``to_roman()`` and
``from_roman()`` functions are inverses of each other. The first
converts integers to specially-formatted strings, the second converts
specially-formated strings to integers. In theory, we should be able to
“round-trip” a number by passing to the ``to_roman()`` function to get a
string, then passing that string to the ``from_roman()`` function to get
an integer, and end up with the same number.

.. code:: nd

   n = from_roman(to_roman(n)) for all values of n

In this case, “all values” means any number between ``1..3999``, since
that is the valid range of inputs to the ``to_roman()`` function. We can
express this symmetry in a test case that runs through all the values
``1..3999``, calls ``to_roman()``, calls ``from_roman()``, and checks
that the output is the same as the original input.

.. code:: nd

   class RoundtripCheck(unittest.TestCase):
       def test_roundtrip(self):
           '''from_roman(to_roman(n))==n for all n'''
           for integer in range(1, 4000):
               numeral = roman5.to_roman(integer)
               result = roman5.from_roman(numeral)
               self.assertEqual(integer, result)

These new tests won’t even fail yet. We haven’t defined a
``from_roman()`` function at all, so they’ll just raise errors.

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest5.py
   E.E....
   ======================================================================
   ERROR: test_from_roman_known_values (__main__.KnownValues)
   from_roman should give known result with known input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest5.py", line 78, in test_from_roman_known_values
       result = roman5.from_roman(numeral)
   AttributeError: 'module' object has no attribute 'from_roman'

   ======================================================================
   ERROR: test_roundtrip (__main__.RoundtripCheck)
   from_roman(to_roman(n))==n for all n
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest5.py", line 103, in test_roundtrip
       result = roman5.from_roman(numeral)
   AttributeError: 'module' object has no attribute 'from_roman'

   ----------------------------------------------------------------------
   Ran 7 tests in 0.019s

   FAILED (errors=2)

A quick stub function will solve that problem.

.. code:: nd

   # roman5.py
   def from_roman(s):
       '''convert Roman numeral to integer'''

(Hey, did you notice that? I defined a function with nothing but a
`docstring <your-first-python-program.html#docstrings>`__. That’s legal
Python. In fact, some programmers swear by it. “Don’t stub; document!”)

Now the test cases will actually fail.

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest5.py
   F.F....
   ======================================================================
   FAIL: test_from_roman_known_values (__main__.KnownValues)
   from_roman should give known result with known input
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest5.py", line 79, in test_from_roman_known_values
       self.assertEqual(integer, result)
   AssertionError: 1 != None

   ======================================================================
   FAIL: test_roundtrip (__main__.RoundtripCheck)
   from_roman(to_roman(n))==n for all n
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest5.py", line 104, in test_roundtrip
       self.assertEqual(integer, result)
   AssertionError: 1 != None

   ----------------------------------------------------------------------
   Ran 7 tests in 0.002s

   FAILED (failures=2)

Now it’s time to write the ``from_roman()`` function.

.. code:: pp

   def from_roman(s):
       """convert Roman numeral to integer"""
       result = 0
       index = 0
       for numeral, integer in roman_numeral_map:
           while s[index:index+len(numeral)] == numeral:  ①
               result += integer
               index += len(numeral)
       return result

#. The pattern here is the same as the ```to_roman()`` <#romantest1>`__
   function. You iterate through your Roman numeral data structure (a
   tuple of tuples), but instead of matching the highest integer values
   as often as possible, you match the “highest” Roman numeral character
   strings as often as possible.

If you're not clear how ``from_roman()`` works, add a ``print``
statement to the end of the ``while`` loop:

::

   def from_roman(s):
       """convert Roman numeral to integer"""
       result = 0
       index = 0
       for numeral, integer in roman_numeral_map:
           while s[index:index+len(numeral)] == numeral:
               result += integer
               index += len(numeral)
               print('found', numeral, 'of length', len(numeral), ', adding', integer)

.. code:: nd

   >>> import roman5
   >>> roman5.from_roman('MCMLXXII')
   found M of length 1, adding 1000
   found CM of length 2, adding 900
   found L of length 1, adding 50
   found X of length 1, adding 10
   found X of length 1, adding 10
   found I of length 1, adding 1
   found I of length 1, adding 1
   1972

Time to re-run the tests.

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest5.py
   .......
   ----------------------------------------------------------------------
   Ran 7 tests in 0.060s

   OK

Two pieces of exciting news here. The first is that the ``from_roman()``
function works for good input, at least for all the `known
values <#romantest1>`__. The second is that the “round trip” test also
passed. Combined with the known values tests, you can be reasonably sure
that both the ``to_roman()`` and ``from_roman()`` functions work
properly for all possible good values. (This is not guaranteed; it is
theoretically possible that ``to_roman()`` has a bug that produces the
wrong Roman numeral for some particular set of inputs, *and* that
``from_roman()`` has a reciprocal bug that produces the same wrong
integer values for exactly that set of Roman numerals that
``to_roman()`` generated incorrectly. Depending on your application and
your requirements, this possibility may bother you; if so, write more
comprehensive test cases until it doesn't bother you.)

⁂

.. _romantest6:

More Bad Input
--------------

Now that the ``from_roman()`` function works properly with good input,
it's time to fit in the last piece of the puzzle: making it work
properly with bad input. That means finding a way to look at a string
and determine if it's a valid Roman numeral. This is inherently more
difficult than `validating numeric input <#romantest3>`__ in the
``to_roman()`` function, but you have a powerful tool at your disposal:
regular expressions. (If you’re not familiar with regular expressions,
now would be a good time to read `the regular expressions
chapter <regular-expressions.html>`__.)

As you saw in `Case Study: Roman
Numerals <regular-expressions.html#romannumerals>`__, there are several
simple rules for constructing a Roman numeral, using the letters ``M``,
``D``, ``C``, ``L``, ``X``, ``V``, and ``I``. Let's review the rules:

-  Sometimes characters are additive. ``I`` is ``1``, ``II`` is ``2``,
   and ``III`` is ``3``. ``VI`` is ``6`` (literally, “\ ``5`` and
   ``1``\ ”), ``VII`` is ``7``, and ``VIII`` is ``8``.
-  The tens characters (``I``, ``X``, ``C``, and ``M``) can be repeated
   up to three times. At ``4``, you need to subtract from the next
   highest fives character. You can't represent ``4`` as ``IIII``;
   instead, it is represented as ``IV`` (“\ ``1`` less than ``5``\ ”).
   ``40`` is written as ``XL`` (“\ ``10`` less than ``50``\ ”), ``41``
   as ``XLI``, ``42`` as ``XLII``, ``43`` as ``XLIII``, and then ``44``
   as ``XLIV`` (“\ ``10`` less than ``50``, then ``1`` less than
   ``5``\ ”).
-  Sometimes characters are… the opposite of additive. By putting
   certain characters before others, you subtract from the final value.
   For example, at ``9``, you need to subtract from the next highest
   tens character: ``8`` is ``VIII``, but ``9`` is ``IX`` (“\ ``1`` less
   than ``10``\ ”), not ``VIIII`` (since the ``I`` character can not be
   repeated four times). ``90`` is ``XC``, ``900`` is ``CM``.
-  The fives characters can not be repeated. ``10`` is always
   represented as ``X``, never as ``VV``. ``100`` is always ``C``, never
   ``LL``.
-  Roman numerals are read left to right, so the order of characters
   matters very much. ``DC`` is ``600``; ``CD`` is a completely
   different number (``400``, “\ ``100`` less than ``500``\ ”). ``CI``
   is ``101``; ``IC`` is not even a valid Roman numeral (because you
   can't subtract ``1`` directly from ``100``; you would need to write
   it as ``XCIX``, “\ ``10`` less than ``100``, then ``1`` less than
   ``10``\ ”).

Thus, one useful test would be to ensure that the ``from_roman()``
function should fail when you pass it a string with too many repeated
numerals. How many is “too many” depends on the numeral.

.. code:: nd

   class FromRomanBadInput(unittest.TestCase):
       def test_too_many_repeated_numerals(self):
           '''from_roman should fail with too many repeated numerals'''
           for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
               self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)

Another useful test would be to check that certain patterns aren’t
repeated. For example, ``IX`` is ``9``, but ``IXIX`` is never valid.

.. code:: nd

       def test_repeated_pairs(self):
           '''from_roman should fail with repeated pairs of numerals'''
           for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
               self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)

A third test could check that numerals appear in the correct order, from
highest to lowest value. For example, ``CL`` is ``150``, but ``LC`` is
never valid, because the numeral for ``50`` can never come before the
numeral for ``100``. This test includes a randomly chosen set of invalid
antecedents: ``I`` before ``M``, ``V`` before ``X``, and so on.

.. code:: nd

       def test_malformed_antecedents(self):
           '''from_roman should fail with malformed antecedents'''
           for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                     'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
               self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)

Each of these tests relies the ``from_roman()`` function raising a new
exception, ``InvalidRomanNumeralError``, which we haven’t defined yet.

.. code:: nd

   # roman6.py
   class InvalidRomanNumeralError(ValueError): pass

All three of these tests should fail, since the ``from_roman()``
function doesn’t currently have any validity checking. (If they don’t
fail now, then what the heck are they testing?)

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest6.py
   FFF.......
   ======================================================================
   FAIL: test_malformed_antecedents (__main__.FromRomanBadInput)
   from_roman should fail with malformed antecedents
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest6.py", line 113, in test_malformed_antecedents
       self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)
   AssertionError: InvalidRomanNumeralError not raised by from_roman

   ======================================================================
   FAIL: test_repeated_pairs (__main__.FromRomanBadInput)
   from_roman should fail with repeated pairs of numerals
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest6.py", line 107, in test_repeated_pairs
       self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)
   AssertionError: InvalidRomanNumeralError not raised by from_roman

   ======================================================================
   FAIL: test_too_many_repeated_numerals (__main__.FromRomanBadInput)
   from_roman should fail with too many repeated numerals
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "romantest6.py", line 102, in test_too_many_repeated_numerals
       self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)
   AssertionError: InvalidRomanNumeralError not raised by from_roman

   ----------------------------------------------------------------------
   Ran 10 tests in 0.058s

   FAILED (failures=3)

Good deal. Now, all we need to do is add the `regular expression to test
for valid Roman numerals <regular-expressions.html#romannumerals>`__
into the ``from_roman()`` function.

.. code:: nd

   roman_numeral_pattern = re.compile('''
       ^                   # beginning of string
       M{0,3}              # thousands - 0 to 3 Ms
       (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                           #            or 500-800 (D, followed by 0 to 3 Cs)
       (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                           #        or 50-80 (L, followed by 0 to 3 Xs)
       (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                           #        or 5-8 (V, followed by 0 to 3 Is)
       $                   # end of string
       ''', re.VERBOSE)

   def from_roman(s):
       '''convert Roman numeral to integer'''
       if not roman_numeral_pattern.search(s):
           raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))

       result = 0
       index = 0
       for numeral, integer in roman_numeral_map:
           while s[index : index + len(numeral)] == numeral:
               result += integer
               index += len(numeral)
       return result

And re-run the tests…

.. code:: nd

   you@localhost:~/diveintopython3/examples$ python3 romantest7.py
   ..........
   ----------------------------------------------------------------------
   Ran 10 tests in 0.066s

   OK

And the anticlimax award of the year goes to… the word “\ ``OK``\ ”,
which is printed by the ``unittest`` module when all the tests pass.

`☜ <advanced-iterators.html>`__ `☞ <refactoring.html>`__

© 2001–11 `Mark Pilgrim <about.html>`__
