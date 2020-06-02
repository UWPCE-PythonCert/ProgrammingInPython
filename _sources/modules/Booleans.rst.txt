.. _booleans:

###################
Boolean Expressions
###################

"Boolean" logic is the logic of binary values -- things that can be ony one of two values. Usually, the two values are considered to be true or false.

In programming languages, "booleans" are often a data type -- one that captures this notion of true and false.

Python has a boolean type as well: the singletons ``True`` and ``False``.

Booleans are used in ``if`` statements, as well as the boolean operators, ``and`` and ``or``.

But Python is not limited to using the actual boolean type in logic expressions -- in the spirit of dynamic languages, virtually any type can have values that are considered True or False.

Some like to refer to this concept by the moniker given by Stephan Colbert: "Truthiness"


Truthiness
----------

What is true or false in Python?

* The Booleans: ``True``  and ``False``

* "Something or Nothing"; that is the presence or absence of a value.

*  http://mail.python.org/pipermail/python-dev/2002-April/022107.html


Determining Truthiness: If you want to know if a value is "truthy", you can use the bool constructor to make a boolean out of it:

.. code-block:: python

    bool(something)

This is similar to making an integer out of another value, such a float or a string:

.. code-block:: ipython

    In [1]: int(4.5)
    Out[1]: 4

    In [2]: int("345")
    Out[2]: 345

``bool(something)`` will always evaluate to either ``True`` or ``False``.


What is Falsy?
--------------

* ``None``

* ``False``

* **Nothing:**

    - The zero value of any numeric type: ``0, 0.0, 0j``.

    - Any empty sequence, for example, ``"", (), []``.

    - Any empty mapping, for example, ``dict()``.

    - Instances of user-defined classes:

        *  for which ``__bool__()`` returns False

        *  for which ``__len__()`` returns 0

* http://docs.python.org/library/stdtypes.html

(Don't worry about that last one -- what that means is that user-defined types can control their truthiness behavior).

What is Truthy?
---------------

Everything else.


Pythonic Booleans
-----------------

Any object in Python, when passed to the ``bool()`` type object, will
evaluate to ``True`` or ``False``.

When you use the ``if`` keyword, it automatically does this to the expression provided.

Which means that this is redundant, and not Pythonic:

.. code-block:: python

    if xx == True:
        do_something()
    # or even worse:
    if bool(xx) == True:
        do_something()

Instead, use what Python gives you:

.. code-block:: python

    if xx:
        do_something()


``and``, ``or`` and ``not``
---------------------------

Python has three boolean operators: ``and``, ``or`` and ``not``.

``and`` and ``or`` are binary expressions, and evaluate from left to right.

``and`` will return the first operand that evaluates to False, or the last
operand if none are True:

.. code-block:: ipython

    In [35]: 0 and 456
    Out[35]: 0

``or`` will return the first operand that evaluates to True, or the last
operand if none are True:

.. code-block:: ipython

    In [36]: 0 or 456
    Out[36]: 456


On the other hand, ``not`` is a unary expression (takes one operand) and inverts the boolean value
of this operand:

.. code-block:: ipython

    In [39]: not True
    Out[39]: False

    In [40]: not False
    Out[40]: True

Shortcutting
------------

``and`` and ``or`` returning teh first value that determines the result is known as "shortcutting".  If you think about it, what ``and`` and ``or`` are doing is as little work as possible. They will only evaluate as much as they need to get the answer.

Think about ``and``: it is testing if *both* the operands are True. If the first one is False, there is no need to bother checking the second.

Alternatively, ``or`` is trying to see if only one of the operands is True. So if the first one is True, it can stop, and does not need to evaluate the second.

Also key is that if an operation is "shortcut" -- the second part of the expression will not be evaluated -- so it could be an invalid expression that will never raise an error:

.. code-block:: ipython

    In [3]: 34 or (10/0)
    Out[3]: 34

Since the expression was known to be true after the first value was checked (a number that is nonzero), the second was never evaluated.

.. code-block:: ipython

    In [4]: 34 and (10 / 0)
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-4-cef0e50bb96d> in <module>()
    ----> 1 34 and (10 / 0)

    ZeroDivisionError: division by zero

In this case, the second expression needs to be evaluated -- so it DID raise an error.

This can be exploited to provide compact logic -- but it can also hide bugs!


Because of the return value of the boolean operators, you can write concise
statements, rather than a full ``if -- else`` block like so:

::

                      if bool(x) is False:
    x or y               return y
                      else: return x

                      if bool(x) is False:
    x and y              return x
                      else: return y

                      if bool(x) is False:
    not x                return True
                      else: return False

Chaining
--------

.. code-block:: python

    a or b or c or d
    a and b and c and d


The first value that defines the result is returned


    (take a moment to experiment...)


Conditional Expressions
-----------------------

This is a fairly common idiom:

.. code-block:: python

    if something:
        x = a_value
    else:
        x = another_value

In other languages, this can be compressed with a "ternary operator"::

    result = a > b ? x : y;

(this is the syntax from the C family of languages)

In Python, the same is accomplished with the conditional expression:

.. code-block:: python

    y = 5 if x > 2 else 3

It's pretty self explanatory

PEP 308:
(http://www.python.org/dev/peps/pep-0308/)


Boolean Return Values
---------------------

Remember this puzzle from the CodingBat exercises?

.. code-block:: python

    def sleep_in(weekday, vacation):
        if weekday == True and vacation == False:
            return False
        else:
            return True

Though correct, that's not a particularly Pythonic way of solving the problem.

Here's a better solution:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return not (weekday == True and vacation == False)


And here's an even better one:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return (not weekday) or vacation


bools are integers?
-------------------

In Python, the boolean types are subclasses of integer:

.. code-block:: ipython

    In [1]: True == 1
    Out[1]: True
    In [2]: False == 0
    Out[2]: True


And you can even do math with them (though it's a bit odd to do so):

.. code-block:: ipython

    In [6]: 3 + True
    Out[6]: 4

This is left over from history -- in early versions of Python, there were no boolean types -- folks used integers, with zero as false. And this is true of other languages as well, like classic C. To keep backward compatibility and allow some nifty tricks to still work, bools are subclassed from integers.

It's good to know this if you read others' code, but I do NOT recommend you use this feature!

Try it out:
-----------

Now that you know a bit more about Python boolean operations, it's a good time to visit some coding bat exercises and see if you can make your solutions cleaner and more compact.



