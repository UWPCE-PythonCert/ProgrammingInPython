
.. _test_driven_development:

FIXME: change the path from my personal to something generic

#######################
Test Driven Development
#######################

"Testing" is any strategy for making sure your code behaves as expected. "Unit Testing" is a particular strategy, that:

* is easy to run in an automated fashion.
* utilized isolated tests for each individual

"Test Driven Development" (TDD) is a development strategy that integrates the development of unit tests with the code itself. In particular, you write the tests *before* you write the code, which seems pretty backward, but it has some real strengths.

We'll demonstrate this technique with an example.
 
The Following is adapted from Mark Pilgrim's excellent "Dive into Python":

https://diveintopython3.problemsolving.io/

The primary difference is that this version uses the simpler pytest testing framework, rather than `unittest`, which is discussed in:
:ref:`unit_testing`

Unit Testing
============

   | "Certitude is not the test of certainty. We have been cocksure of
     many things that were not so."
   | — `Oliver Wendell Holmes,
     Jr. <http://en.wikiquote.org/wiki/Oliver_Wendell_Holmes,_Jr.>`__


(Not) Diving In
---------------

Kids today. So spoiled by these fast computers and fancy “dynamic”
languages. Write first, ship second, debug third (if ever). In my day,
we had discipline. **Discipline, I say!** We had to write programs by
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
uses them.

Technically, you can write unit tests with plain Python -- recall the ``assert`` statement that you have already used to write simple tests. But it is very helpful to use a framework to make it easier to write and run your tests. In this program, we use the `pytest` package: it is both very easy to get started with, and provides a lot of powerful features to aide in testing complex systems.

.. note:: ``pytest`` does not come with Python out of the box. But it is easily installable via `pip` (or conda, if you are using conda)::

              $ python -m pip install pytest

          Once installed, you should have the pytest command available in your terminal.

FIXME: Maybe add a small page on installing and using pytest?

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

.. centered:: **Every Test is an Island**

A test case answers a single question about the code it is testing. A
test case should be able to...

- Run completely by itself, without any human input. Unit testing is
  about automation.
- Determine by itself whether the function it is testing has passed
  or failed, without a human interpreting the results.
- Run in isolation, separate from any other test cases (even if they
  test the same functions). Each test case is an island.

Given that, let’s build a test case for the first requirement:

1. The ``to_roman()`` function should return the Roman numeral
   representation for all integers ``1`` to ``3999``.

Let's take a look at
:download:`roman.py <../examples/test_driven_development/roman.py>`.

.. code-block:: python
    :linenos:

    """
    roman.py

    A Roman numeral to Arabic numeral (and back!) converter

    complete with tests

    tests are expected to be able to be run with the pytest system
    """

        ## Tests for roman numeral conversion

        KNOWN_VALUES = ( (1, 'I'),
                         (2, 'II'),
                         (3, 'III'),
                         (4, 'IV'),
                         (5, 'V'),
                         (6, 'VI'),
                         (7, 'VII'),
                         (8, 'VIII'),
                         (9, 'IX'),
                         (10, 'X'),
                         (50, 'L'),
                         (100, 'C'),
                         (500, 'D'),
                         (1000, 'M'),
                         (31, 'XXXI'),
                         (148, 'CXLVIII'),
                         (294, 'CCXCIV'),
                         (312, 'CCCXII'),
                         (421, 'CDXXI'),
                         (528, 'DXXVIII'),
                         (621, 'DCXXI'),
                         (782, 'DCCLXXXII'),
                         (870, 'DCCCLXX'),
                         (941, 'CMXLI'),
                         (1043, 'MXLIII'),
                         (1110, 'MCX'),
                         (1226, 'MCCXXVI'),
                         (1301, 'MCCCI'),
                         (1485, 'MCDLXXXV'),
                         (1509, 'MDIX'),
                         (1607, 'MDCVII'),
                         (1754, 'MDCCLIV'),
                         (1832, 'MDCCCXXXII'),
                         (1993, 'MCMXCIII'),
                         (2074, 'MMLXXIV'),
                         (2152, 'MMCLII'),
                         (2212, 'MMCCXII'),
                         (2343, 'MMCCCXLIII'),
                         (2499, 'MMCDXCIX'),
                         (2574, 'MMDLXXIV'),
                         (2646, 'MMDCXLVI'),
                         (2723, 'MMDCCXXIII'),
                         (2892, 'MMDCCCXCII'),
                         (2975, 'MMCMLXXV'),
                         (3051, 'MMMLI'),
                         (3185, 'MMMCLXXXV'),
                         (3250, 'MMMCCL'),
                         (3313, 'MMMCCCXIII'),
                         (3408, 'MMMCDVIII'),
                         (3501, 'MMMDI'),
                         (3610, 'MMMDCX'),
                         (3743, 'MMMDCCXLIII'),
                         (3844, 'MMMDCCCXLIV'),
                         (3888, 'MMMDCCCLXXXVIII'),
                         (3940, 'MMMCMXL'),
                         (3999, 'MMMCMXCIX'),
                         )


    def test_to_roman_known_values():
        """
        to_roman should give known result with known input
        """
        for integer, numeral in KNOWN_VALUES:
            result = to_roman(integer)
            assert numeral == result


It is not immediately obvious how this code does ... well, *anything*.
It defines a big data structure full of examples and a single function.

The entire script has no ``__main__`` block, so even that one function won't run. But it does do something, I promise.

`KNOWN_VALUES` is a big tuple of integer/numeral pairs that were verified manually. It includes the lowest ten numbers, the highest number, every number
that translates to a single-character Roman numeral, and a random sampling of other valid numbers.
You don’t need to test every possible input, but you should try to test all the obvious edge cases.

.. note:: This is a major challenge of unit testing -- how to catch all the edge cases, without over testing every little thing.

`pytest` makes it really simple to write a test case: simply define a function named ``test_anything``. pytest will identify any function with: "``test_``"" at the start of the name as a test function.

* Every individual test is its own function. A test function takes no parameters, returns no value, and must have a name beginning with the five letters ``test_``.
  If a test function exits normally without a failing assertion or other exception, the test is considered passed; if the function raises a failed assertion, failed.

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

Note that in this case, we are looping through all the known values, testing each one in the loop. If any of the known values fails, the test will fail, and end the test function -- the rest of the values will not be tested.

If every value returned from ``to_roman()`` matches the known value you expect, the assert will never fail, and ``test_to_roman_known_values``
eventually exits normally, which means ``to_roman()`` has passed this
test.


Write a test that fails, then code until it passes.
...................................................

Once you have a test case, you can start coding the ``to_roman()``
function. First, you should stub it out as an empty function and make
sure the tests fail. If the tests succeed before you’ve written any
code, your tests aren’t testing your code at all! TDD is a
dance: tests lead, code follows. Write a test that fails, then code
until it passes.

For a small system like this, we can put the code and the tests in the same file. But as you build larger systems, it is customary to put the tests in a separate file -- more on that later.

You can actually try your tests out before even writing any code!

To run tests with pytest, you pass in the test file on the command line:

.. code-block::

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
    >           result = to_roman(integer)
    E           NameError: name 'to_roman' is not defined

    roman.py:75: NameError
    ========================= short test summary info =========================
    FAILED roman.py::test_to_roman_known_values - NameError: name 'to_roman'...
    ============================ 1 failed in 0.15s ============================

There's a lot going on here! pytest has found your test function, set itself up, and run the tests it finds (in this case only the one).
Then it runs the test (which in this case fails), and reports the failure(s).
Along with the fact that it fails, it tells you why it failed (a ``NameError``) where it failed (line 75 of the file), and shows you the code before the test failure.
This may seem like a lot of information for such a simple case, but it can be invaluable in a more complex system.

We got a NameError, because there is no ``to_roman`` function defined in the file. So let's add that now:

(:download:`roman1.py <../examples/test_driven_development/roman1.py>`)

.. code-block:: python

   # roman1.py

   def to_roman(n):
       '''convert an integer to Roman numeral'''
       pass

At this stage, you want to define the API of the ``to_roman()`` function, but you don’t want to code it yet (your tests need to fail first).
To stub it out, use the Python reserved word ``pass``, which does precisely nothing.

Now run pytest again, with the function defined:

.. code-block::

    $ pytest roman1.py
    =========================== test session starts ===========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 1 item

    roman1.py F                                                         [100%]

    ================================ FAILURES =================================
    _______________________ test_to_roman_known_values ________________________

        def test_to_roman_known_values():
            """
            to_roman should give known result with known input
            """
            for integer, numeral in KNOWN_VALUES:
                result = to_roman(integer)
    >           assert numeral == result
    E           AssertionError: assert 'I' == None

    roman1.py:84: AssertionError
    ========================= short test summary info =========================
    FAILED roman1.py::test_to_roman_known_values - AssertionError: assert 'I...
    ============================ 1 failed in 0.15s ============================

Again, pytest has found the test, run it, and again it failed.
But this time, it failed with an ``AssertionError`` -- one of the known values did not equal what was expected.
In addition to the line number where the failure occurred, pytest tells you exactly what the values being compared were.
In this case, 'I' does not equal ``None`` -- obviously not. But why did you get a ``None`` there? because Python returns None when a function does not explicitly return another value. In this case, the only content in the function is ``pass``, so ``None`` was returned implicitly.

.. note:: It may seem silly, and a waste of time, to go through this process when you *know* that it will fail: you haven't written the code yet!
          But this is, in fact, a useful process.
          You have learned that your test is running and that it really does fail when the function does nothing.
          This may seem trivial, and, of course, experienced practitioners don't *always* run tests against a do-nothing function.
          But when a system gets large, with many hundreds of tests, it's easy for things to get lost -- it really is useful to know for sure that your tests are working before you start to rely on them.


Overall, the test run failed because at least one test case did not pass.
When a test case doesn’t pass, pytest distinguishes between failures and errors.
A failure is a failed assertion that fails because the asserted condition is not true.
An error is any other sort of exception raised in the code you’re testing or the test code itself.

*Now*, finally, you can write the ``to_roman()`` function.

:download:`roman2.py <../examples/test_driven_development/roman2.py>`

.. code-block:: python
    :linenos:

    """
    roman.py

    A Roman numeral to arabic numeral (and back!) converter

    complete with tests

    tests are expected to be able to be run with the pytest system
    """

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
                         ('I',  1))


    def to_roman(n):
        '''convert integer to Roman numeral'''
        result = ''
        for numeral, integer in roman_numeral_map:
           while n >= integer:
               result += numeral
               n -= integer
        return result


    ## Tests for roman numeral conversion

    KNOWN_VALUES = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'),
                     )


    def test_to_roman_known_values():
        """
        to_roman should give known result with known input
        """
        for integer, numeral in KNOWN_VALUES:
            result = to_roman(integer)
            assert numeral == result

``roman_numeral_map`` is a tuple of tuples which defines three
things: the character representations of the most basic Roman
numerals; the order of the Roman numerals (in descending value order,
from ``M`` all the way down to ``I``); the value of each Roman
numeral. Each inner tuple is a pair of ``(numeral, value)``. It’s not
just single-character Roman numerals; it also defines two-character
pairs like ``CM`` (“one hundred less than one thousand”). This makes
the ``to_roman()`` function code simpler.

Here’s where the rich data structure of ``roman_numeral_map`` pays
off, because you don’t need any special logic to handle the
subtraction rule. To convert to Roman numerals, simply iterate
through ``roman_numeral_map`` looking for the largest integer value
less than or equal to the input. Once found, add the Roman numeral
representation to the end of the output, subtract the corresponding
integer value from the input, lather, rinse, repeat.

If you’re still not clear how the ``to_roman()`` function works, add a
``print()`` call to the end of the ``while`` loop:

.. code-block:: python

    while n >= integer:
        result += numeral
        n -= integer
        print(f'subtracting {integer} from input, adding {numeral} to output')

With the debug ``print()`` statements, the output looks like this:

.. code-block:: ipython

    In [3]: run roman2.py

    In [4]: to_roman(1424)
    subtracting 1000 from input, adding M to output
    subtracting 400 from input, adding CD to output
    subtracting 10 from input, adding X to output
    subtracting 10 from input, adding X to output
    subtracting 4 from input, adding IV to output
    Out[4]: 'MCDXXIV'

So the ``to_roman()`` function appears to work, at least in this manual
spot check. But will it pass the test case you wrote?

.. code-block::

    In [7]: ! pytest roman2.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 1 item

    roman2.py .                                                     [100%]

    ========================== 1 passed in 0.01s ==========================


Hooray! The ``to_roman()`` function passes the “known values” test case. It’s not comprehensive, but it does put the function through
its paces with a variety of inputs, including inputs that produce
every single-character Roman numeral, the largest possible input
(``3999``), and the input that produces the longest possible Roman
numeral (``3888``). At this point, you can be reasonably confident
that the function works for any good input value you could throw at
it.

“Good” input? Hmm. What about bad input?


“Halt And Catch Fire”
---------------------

The Pythonic way to halt and catch fire is to raise an exception.

It is not enough to test that functions succeed when given good input;
you must also test that they fail when given bad input. And not just any
sort of failure; they must fail in the way you expect.

.. code-block:: ipython

  In [10]: to_roman(3000)
  Out[10]: 'MMM'

  In [11]: to_roman(4000)
  Out[11]: 'MMMM'

  In [12]: to_roman(5000)
  Out[12]: 'MMMMM'

  In [13]: to_roman(9000)
  Out[13]: 'MMMMMMMMM'

That’s definitely *not* what you wanted — that’s not even a valid Roman
numeral!
In fact, after 3000, each of these numbers is outside the range of
acceptable input, but the function returns a bogus value anyway.
Silently returning bad values is *baaaaaaad*; if a program is going
to fail, it is far better if it fails quickly and noisily. “Halt and
catch fire,” as the saying goes. In Python, the way to halt and catch
fire is to raise an exception.

The question to ask yourself is, “How can I express this as a testable
requirement?” How’s this for starters:

   The ``to_roman()`` function should raise an ``ValueError`` when
   given an integer greater than ``3999``.

Why a ValueError? I think it's a good idea to use one of the standard built-in exceptions is there is one that fits your use case. In this case, it is the *value* of the argument that is the problem -- it is too large. So a ``ValueError`` is appropriate.

So how do we test for an exception? What would that test look like?

:download:`roman.py <../examples/test_driven_development/roman3.py>`.

.. code-block:: python

    import pytest

    def test_too_large():
        """
        to_roman should raise an ValueError when passed
        values over 3999
        """
        with pytest.raises(ValueError):
            to_roman(4000)


Like the previous test case, the test itself is a function with a name starting with ``test_``. pytest will know that it's a test due to the name.

The test function has a docstring, letting us know what it is testing.

Now look at the body of that function; what the heck is that ``with`` statement? ``with`` is how we invoke a "context manager" -- the code indented after the ``with`` is run in the "context" created, in this case, by the ``pytest.raises`` function. What ``pytest.raises`` does is check to make sure that the Exception specified is raised by the following code. So in this example, if ``to_roman(4000)`` raises an ``ValueError``, the test will pass, and if it does not raise an Exception, or raises a different Exception, the test will fail.

.. note:: Context managers are a powerful and sometimes complex feature
          of Python. They will be covered later in detail, but for now, you only need to know that the code inside the with block runs in a special way controlled by what follows the ``with`` statement, including exception handling.
          You will see ``with`` when working with files (:ref:`files`), and you can read more about it in: :ref:`context_managers`

CAUTION: you are now using a utility from the ``pytest`` package, so you need to make sure to import pytest first:

..code-block:: python

    In [18]: ! pytest roman3.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 2 items

    roman3.py .F                                                    [100%]

    ============================== FAILURES ===============================
    ___________________________ test_too_large ____________________________

        def test_too_large():
            """
            to_roman should raise an ValueError when passed
            values over 3999
            """
            with pytest.raises(ValueError):
    >           to_roman(4000)
    E           Failed: DID NOT RAISE <class 'ValueError'>

    roman3.py:115: Failed
    ======================= short test summary info =======================
    FAILED roman3.py::test_too_large - Failed: DID NOT RAISE <class 'Val...
    ===================== 1 failed, 1 passed in 0.08s =====================


You should have expected this to fail since you haven’t written any
code to pass it yet. Did it fail in the way you expected?

Yes! ``pytest.raises`` did its job -- a ``ValueError`` was not raised, and the test failed.

Of course, the ``to_roman()`` function isn’t raising the
``ValueError`` because you haven’t told it to do that yet.
That’s excellent news! It means this is a valid test case — it fails before you write the code to make it pass.

Now you can write the code to make this test pass.

:download:`roman4.py <../examples/test_driven_development/roman4.py>`.

.. code-block::

    def to_roman(n):
        '''convert integer to Roman numeral'''
        if n > 3999:
            raise ValueError("number out of range (must be less than 4000)")

        result = ''
        for numeral, integer in roman_numeral_map:
            while n >= integer:
                result += numeral
                n -= integer
        return result

#. This is straightforward: if the given input (``n``) is greater than
   ``3999``, raise an ``ValueError`` exception. The unit test does
   not check the human-readable string that accompanies the exception,
   although you could write another test that did check it (but watch
   out for internationalization issues for strings that vary by the
   user’s language or environment).

Does this make the test pass? Let’s find out.

.. code-block:: ipython

    In [19]: ! pytest roman4.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 2 items

    roman4.py ..                                                    [100%]

    ========================== 2 passed in 0.01s ==========================

Hooray! Both tests pass. Because you worked iteratively, bouncing
back and forth between testing and coding, you can be sure that the
two lines of code you just wrote were the cause of that one test
going from “fail” to “pass.” That kind of confidence doesn’t come
cheap, but it will pay for itself over the lifetime of your code.


More Halting, More Fire
-----------------------

Along with testing numbers that are too large, you need to test numbers
that are too small.
As `we noted in our functional requirements, Roman numerals cannot express 0 or negative numbers.

.. code-block:: ipython

    In [20]: run roman4.py

    In [21]: to_roman(-1)
    Out[21]: ''

    In [22]: to_roman(0)
    Out[22]: ''

Well *that’s* not good. Let’s add tests for each of these conditions.

:download:`roman5.py <../examples/test_driven_development/roman5.py>`.

.. code-block:: python

    def test_zero():
        """to_roman should raise an ValueError with 0 input"""
        with pytest.raises(ValueError):
            to_roman(0)


    def test_negative():
        """to_roman should raise an ValueError with negative input"""
        with pytest.raises(ValueError):
            to_roman(-1)

The first new test is the ``test_zero()`` function. Like the
``test_too_large()`` function, it it uses the ``pytest.raises`` context manager to call our ``to_roman()`` function with a parameter of 0, and check that it raises the appropriate exception: ``ValueError``.

The ``test_negative()`` method is almost identical, except it passes
``-1`` to the ``to_roman()`` function. If either of these new tests
does *not* raise an ``ValueError`` (either because the function
returns an actual value, or because it raises some other exception),
the test is considered failed.

Now check that the tests fail:

.. code-block:: python

    In [24]: ! pytest roman5.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 4 items

    roman5.py ..FF                                                  [100%]

    ============================== FAILURES ===============================
    ______________________________ test_zero ______________________________

        def test_zero():
            """to_roman should raise an ValueError with 0 input"""
            with pytest.raises(ValueError):
    >           to_roman(0)
    E           Failed: DID NOT RAISE <class 'ValueError'>

    roman5.py:123: Failed
    ____________________________ test_negative ____________________________

        def test_negative():
            """to_roman should raise an ValueError with negative input"""
            with pytest.raises(ValueError):
    >           to_roman(-1)
    E           Failed: DID NOT RAISE <class 'ValueError'>

    roman5.py:129: Failed
    ======================= short test summary info =======================
    FAILED roman5.py::test_zero - Failed: DID NOT RAISE <class 'ValueErr...
    FAILED roman5.py::test_negative - Failed: DID NOT RAISE <class 'Valu...
    ===================== 2 failed, 2 passed in 0.09s =====================

Excellent. Both tests failed, as expected. Now let’s switch over to the
code and see what we can do to make them pass.

:download:`roman6.py <../examples/test_driven_development/roman6.py>`.

.. code-block::

    def to_roman(n):
        """convert integer to Roman numeral"""
        if not (0 < n < 4000):
            raise ValueError("number out of range (must be 1..3999)")

        result = ''
        for numeral, integer in roman_numeral_map:
            while n >= integer:
                result += numeral
                n -= integer
        return result

Note the ``not (0 < n < 4000)`` This is a nice Pythonic shortcut: multiple comparisons at once.
This is equivalent to ``if not ((0 < n) and (n < 4000))``, but it’s much
easier to read. This one line of code should catch inputs that are
too large, negative, or zero.

If you change your conditions, make sure to update your
human-readable error strings to match.  pytest won’t care,
but it’ll make it difficult to do manual debugging if
your code is throwing incorrectly-described exceptions.

I could show you a whole series of unrelated examples to show that the
multiple-comparisons-at-once shortcut works, but instead I’ll just run
the unit tests and prove it.

.. code-block:: python

    In [26]: ! pytest roman6.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 4 items

    roman6.py ....                                                  [100%]

    ========================== 4 passed in 0.01s ==========================

Excellent! The tests all pass -- your code is working! Remember that you still have the "too large" test -- and all the tests of converting numbers. So you know you haven't inadvertently broken anything else.


And One More Thing ...
----------------------

There was one more functional requirement for converting numbers to Roman numerals: dealing with non-integers.

.. code-block:: ipython

    In [30]: run roman6.py

    In [31]: to_roman(0.5)
    Out[31]: ''

Oh, that’s bad.

.. code-block:: ipython

    In [32]: to_roman(1.0)
    Out[32]: 'I'

What about that? technically, 1.0 is a float type, not an integer. But it does have an integer value, and Python considers them equal:

.. code-block:: ipython

    In [35]: 1 == 1.0
    Out[35]: True

So I'd say that we want 1.0 to be convertable, but not 0.5 (or 1.00000001 for that matter)

Testing for non-integers is not difficult. Simply write a test case that checks that a ``ValueError`` is raised if you pass in a non-integer value.

:download:`roman7.py <../examples/test_driven_development/roman7.py>`.

.. code-block:: python

    def test_non_integer():
        """to_roman should raise an ValueError with non-integer input"""
        with pytest.raises(ValueError):
            to_roman(0.5)

And while we are at it, test a float type that happens to be an integer.

.. code-block:: python

def test_float_with_integer_value():
    """to_roman should work for floats with integer values"""
    assert to_roman(3.0) == "III"

Why a ``ValueError``? because it's the value that matters, not the type. It's OK to pass in a float type, as long as the value is an integer.

Now check that the test fails properly.

.. code-block:: python

    In [36]: ! pytest roman7.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 6 items

    roman7.py ....F.                                                [100%]

    ============================== FAILURES ===============================
    __________________________ test_non_integer ___________________________

        def test_non_integer():
            """to_roman should raise an ValueError with non-integer input"""
            with pytest.raises(ValueError):
    >           to_roman(0.5)
    E           Failed: DID NOT RAISE <class 'ValueError'>

    roman7.py:135: Failed
    ======================= short test summary info =======================
    FAILED roman7.py::test_non_integer - Failed: DID NOT RAISE <class 'V...
    ===================== 1 failed, 5 passed in 0.10s =====================

Yup -- it failed.

**Hint:** when you add a new test, and see that it fails, also check that there are *more* tests than there were. In this case, 1 failed, and 5 passed. In the previous run, 4 passed -- so you know there are, in fact, two additional tests, one of which passed. Why might there not be? because we all like to copy-and-paste, and then edit. If you forget to rename the test function, it will overwrite the previous one -- and we want all our tests to be preserved.

So now write the code that makes the test pass.

:download:`roman8.py <../examples/test_driven_development/roman8.py>`.

.. code-block::

    def to_roman(n):
        """convert integer to Roman numeral"""
        if not (0 < n < 4000):
            raise ValueError("number out of range (must be 1..3999)")

        if int(n) != n:
            raise ValueError("Only integers can be converted to Roman numerals")

        result = ''
        for numeral, integer in roman_numeral_map:
            while n >= integer:
                result += numeral
                n -= integer
        return result

``int(n) != n`` is checking that when you convert the value to an integer, it doesn't change. We need to do that, because simply checking if you can convert to an integer isn't enough -- when a float is converted to an integer, the fractional part is truncated:

.. code-block:: python

    In [37]: int(1.00001)
    Out[37]: 1

if the result of converting to an integer is equal to the original, than it had an integral value. Note that this will work with all the built numerical types:

.. code-block:: ipython

    In [42]: int(Decimal(3)) == 3
    Out[42]: True

    In [43]: int(Decimal(3.5)) == 3.5
    Out[43]: False

Finally, check that the code does indeed make the test pass.

.. code-block:: python

    In [44]: ! pytest roman8.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 6 items

    roman8.py ......                                                [100%]

    ========================== 6 passed in 0.02s ==========================


The ``to_roman()`` function passes all of its tests, and I can’t think
of any more tests, so it’s time to move on to ``from_roman()``.


A Pleasing Symmetry
-------------------

Converting a string from a Roman numeral to an integer sounds more
difficult than converting an integer to a Roman numeral. Certainly there
is the issue of validation. It’s easy to check if an integer is greater
than 0, but a bit harder to check whether a string is a valid Roman
numeral. But we can at least make sure that correct Roman numerals convert correctly.

So we have the problem of converting the string itself. As we’ll see in
a minute, thanks to the rich data structure we defined to map individual
Roman numerals to integer values, the nitty-gritty of the
``from_roman()`` function is as straightforward as the ``to_roman()``
function.

But first, the tests. We’ll need a “known values” test to spot-check for
accuracy. Our test suite already contains a mapping of known
values: let’s reuse that.

.. code-block:: python

    def test_from_roman_known_values():
        """from_roman should give known result with known input"""
        for integer, numeral in KNOWN_VALUES:
            result = from_roman(numeral)
            assert integer == result

There’s a pleasing symmetry here. The ``to_roman()`` and
``from_roman()`` functions are inverses of each other. The first
converts integers to specially-formatted strings, the second converts
specially-formated strings to integers. In theory, we should be able to
“round-trip” a number by passing to the ``to_roman()`` function to get a
string, then passing that string to the ``from_roman()`` function to get
an integer, and end up with the same number.

.. code-block:: python

   n = from_roman(to_roman(n)) for all values of n

In this case, “all values” means any number between ``1..3999``, since
that is the valid range of inputs to the ``to_roman()`` function. We can
express this symmetry in a test case that runs through all the values
``1..3999``, calls ``to_roman()``, calls ``from_roman()``, and checks
that the output is the same as the original input.

.. code-block:: python


    def test_roundtrip():
        '''from_roman(to_roman(n))==n for all n'''
        for integer in range(1, 4000):
            numeral = to_roman(integer)
            result = from_roman(numeral)
            assert integer == result


These new tests won’t even fail properly yet. We haven’t defined a
``from_roman()`` function at all, so they’ll just raise errors.

.. code-block:: python

    In [48]: ! pytest roman9.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 8 items

    roman9.py ......FF                                              [100%]

    ============================== FAILURES ===============================
    ____________________ test_from_roman_known_values _____________________

        def test_from_roman_known_values():
            """from_roman should give known result with known input"""
            for integer, numeral in KNOWN_VALUES:
    >           result = from_roman(numeral)
    E           NameError: name 'from_roman' is not defined

    roman9.py:152: NameError
    ___________________________ test_roundtrip ____________________________

        def test_roundtrip():
            '''from_roman(to_roman(n))==n for all n'''
            for integer in range(1, 4000):
                numeral = to_roman(integer)
    >           result = from_roman(numeral)
    E           NameError: name 'from_roman' is not defined

    roman9.py:160: NameError
    ======================= short test summary info =======================
    FAILED roman9.py::test_from_roman_known_values - NameError: name 'fr...
    FAILED roman9.py::test_roundtrip - NameError: name 'from_roman' is n...
    ===================== 2 failed, 6 passed in 0.10s =====================

A quick stub function will solve that problem.

.. code-block:: python

   # roman10.py
   def from_roman(s):
       '''convert Roman numeral to integer'''

Hey, did you notice that? I defined a function with nothing but a docstring. That’s legal Python. In fact, some programmers swear by it. “Don’t stub; document!”

Now the test cases will properly fail.

.. code-block:: ipython

    In [50]: ! pytest roman10.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 8 items

    roman10.py ......FF                                             [100%]

    ============================== FAILURES ===============================
    ____________________ test_from_roman_known_values _____________________

        def test_from_roman_known_values():
            """from_roman should give known result with known input"""
            for integer, numeral in KNOWN_VALUES:
                result = from_roman(numeral)
    >           assert integer == result
    E           assert 1 == None

    roman10.py:157: AssertionError
    ___________________________ test_roundtrip ____________________________

        def test_roundtrip():
            """from_roman(to_roman(n))==n for all n"""
            for integer in range(1, 4000):
                numeral = to_roman(integer)
                result = from_roman(numeral)
    >           assert integer == result
    E           assert 1 == None

    roman10.py:165: AssertionError
    ======================= short test summary info =======================
    FAILED roman10.py::test_from_roman_known_values - assert 1 == None
    FAILED roman10.py::test_roundtrip - assert 1 == None
    ===================== 2 failed, 6 passed in 0.11s =====================


Now it’s time to write the ``from_roman()`` function.

.. code-block::

    def from_roman(s):
        """convert Roman numeral to integer"""
        result = 0
        index = 0
        for numeral, integer in roman_numeral_map:
            while s[index:index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result

The pattern here is the same as the ```to_roman()`` function.
You iterate through your Roman numeral data structure (a tuple of tuples),
but instead of matching the highest integer values as often as possible,
you match the “highest” Roman numeral character
strings as often as possible.

If you're not clear how ``from_roman()`` works, add a ``print``
statement to the end of the ``while`` loop:

.. code-block:: ipython

    def from_roman(s):
        """convert Roman numeral to integer"""
        result = 0
        index = 0
        for numeral, integer in roman_numeral_map:
            while s[index:index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
                print(f'found, {numeral} of length, {len(numeral)} adding {integer}')
        return result

.. code-block:: ipython

    In [52]: run roman10.py

    In [53]: from_roman('MCMLXXII')
    found, M of length, 1 adding 1000
    found, CM of length, 2 adding 900
    found, L of length, 1 adding 50
    found, X of length, 1 adding 10
    found, X of length, 1 adding 10
    found, I of length, 1 adding 1
    found, I of length, 1 adding 1
    Out[53]: 1972

Time to re-run the tests.

.. code-block:: ipython

    In [54]: ! pytest roman10.py
    ========================= test session starts =========================
    platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/examples/test_driven_development
    collected 8 items

    roman10.py ........                                             [100%]

    ========================== 8 passed in 0.38s ==========================


Two pieces of exciting news here. The first is that the ``from_roman()``
function works for good input, at least for all the `known
values. The second is that the “round trip” test also
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

.. code-block:: python

   class FromRomanBadInput(unittest.TestCase):
       def test_too_many_repeated_numerals(self):
           '''from_roman should fail with too many repeated numerals'''
           for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
               self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)

Another useful test would be to check that certain patterns aren’t
repeated. For example, ``IX`` is ``9``, but ``IXIX`` is never valid.

.. code-block:: python

       def test_repeated_pairs(self):
           '''from_roman should fail with repeated pairs of numerals'''
           for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
               self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)

A third test could check that numerals appear in the correct order, from
highest to lowest value. For example, ``CL`` is ``150``, but ``LC`` is
never valid, because the numeral for ``50`` can never come before the
numeral for ``100``. This test includes a randomly chosen set of invalid
antecedents: ``I`` before ``M``, ``V`` before ``X``, and so on.

.. code-block:: python

       def test_malformed_antecedents(self):
           '''from_roman should fail with malformed antecedents'''
           for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                     'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
               self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, s)

Each of these tests relies the ``from_roman()`` function raising a new
exception, ``InvalidRomanNumeralError``, which we haven’t defined yet.

.. code-block:: python

   # roman6.py
   class InvalidRomanNumeralError(ValueError): pass

All three of these tests should fail, since the ``from_roman()``
function doesn’t currently have any validity checking. (If they don’t
fail now, then what the heck are they testing?)

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

   you@localhost:~/diveintopython3/examples$ python3 romantest7.py
   ..........
   ----------------------------------------------------------------------
   Ran 10 tests in 0.066s

   OK

And the anticlimax award of the year goes to… the word “\ ``OK``\ ”,
which is printed by the ``unittest`` module when all the tests pass.

`☜ <advanced-iterators.html>`__ `☞ <refactoring.html>`__

© 2001–11 `Mark Pilgrim <about.html>`__
