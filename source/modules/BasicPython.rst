.. _basic_python_syntax:

Basic Python
============

Values, Types, and Symbols

Expressions and Statements

(Follow along in the iPython interpreter...)

Values
------

All of programming is really about manipulating values.


* Values are pieces of unnamed data: ``42``, ``'Hello, world'``

* In Python, all values are objects.

  - Try ``dir(42)``  - lots going on behind the curtain!

* Every value has a type

  - Try ``type(42)`` - the type of a value determines what it can do.


Literals for the Basic Value types:
------------------------------------

Numbers:
  - floating point: ``3.4``
  - integers: ``456``

Text:
  -  ``"a bit of text"``
  -  ``'a bit of text'``
  - (either single or double quotes work -- why? If you don't know try looking it up in one of the referenced sources!)

Boolean values:
  -  ``True``
  -  ``False``

The nothing object:
  - ``None``

(There are intricacies to all of these that we'll get into later.)


Code structure
--------------

Each line is a piece of code.

Comments:

.. code-block:: ipython

    In [3]: # everything after a '#' is a comment

Expressions:

.. code-block:: ipython

    In [4]: # evaluating an expression results in a value

    In [5]: 3 + 4
    Out[5]: 7


Statements:
statements carry out an action, but do not evaluate to a value, that is you can't assign to them (or put them in a lamda, or...)

.. code-block:: ipython

    In [6]: # statements carry out an action, do not evaluate a value, may contain an expression

    In [7]: line_count = 42

    In [8]: return something



It is somewhat obvious, but handy when playing with code:

.. code-block:: ipython

    In [1]: print("something")
    something

You can print multiple things:

.. code-block:: ipython

    In [2]: print("the value is", 5)
    the value is 5



Any Python object can be printed (though it might not be pretty...)

.. code-block:: ipython

    In [1]: class bar(object):
       ...:     pass
       ...:

    In [2]: print(bar)
    <class '__main__.bar'>



Blocks of code are delimited by a colon and indentation:

.. code-block:: python

    def a_function():
        a_new_code_block
    # end_of_the_block on previous line

.. code-block:: python

    for i in range(100):
        print(i**2)

.. code-block:: python

    try:
        do_something_bad()
    except:
        fix_the_problem()


Python uses indentation to delineate structure. This means that in Python, whitespace is **significant** (but **ONLY** for newlines and indentation).

The standard is to indent with **4 spaces**.

**SPACES ARE NOT TABS**

**TABS ARE NOT SPACES**

Python requires spaces for indents. You can probably set your editor to replace tabs with spaces.
This is a good idea as it is easier to type one tab than 4 spaces.


These two blocks look the same:

.. code-block:: python

    for i in range(100):
        print(i**2)

.. code-block:: python

    for i in range(100):
        print(i**2)



But they are not:

.. code-block:: python

    for i in range(100):
    \s\s\s\sprint i**2

.. code-block:: python

    for i in range(100):
    \tprint i**2

**ALWAYS INDENT WITH 4 SPACES**




Make sure your editor is set to use spaces only --

Even when you hit the <tab> key

[Python itself allows any number of spaces (and tabs), but you are just going to confuse yourself and others if you do anything else]


Expressions
------------

An *expression* is made up of values and operators.


* An expression is evaluated to produce a new value:  ``2 + 2``

  *  The Python interpreter can be used as a calculator to evaluate expressions.

* Integer vs. float arithmetic

  * (Python 3 smooths this out).
  * Always use ``/`` when you want division with float results, ``//`` when you want floored (integer) results (no remainder).

* Type conversions.

  * This is the source of many errors, especially in handling text.

* Type errors - checked at run time only.


Symbols
-------

Symbols are how we give names to values (objects).


* Symbols must begin with an underscore or letter.
* Symbols can contain any number of underscores, letters and numbers.

  * this_is_a_symbol
  * this_is_2
  * _AsIsThis
  * 1butThisIsNot
  * nor-is-this

* Symbols don't have a type; values do.

  * This is why Python is "Dynamic".


Symbols and Type
----------------

Evaluating the type of a *symbol* will return the type of the *value* to which
it is bound.

.. code-block:: ipython

    In [19]: type(42)
    Out[19]: int

    In [20]: type(3.14)
    Out[20]: float

    In [21]: a = 42

    In [22]: b = 3.14

    In [23]: type(a)
    Out[23]: int

    In [25]: a = b

    In [26]: type(a)
    Out[26]: float

*wait!* ``a`` has a different type?!? -- yes, because it's the type of the value: "3.14", names don't actually have a type, the same name can refer to any type.


Assignment
----------

A *symbol* is **bound** to a *value* with the assignment operator: ``=``

* This attaches a name to a value.
* A value can have many names (or none!)
* Assignment is a statement, it returns no value.


Evaluating the name will return the value to which it is bound

.. code-block:: ipython

    In [26]: name = "value"

    In [27]: name
    Out[27]: 'value'

    In [28]: an_integer = 42

    In [29]: an_integer
    Out[29]: 42

    In [30]: a_float = 3.14

    In [31]: a_float
    Out[31]: 3.14

Variables?
----------


* In most languages, what Python calls symbols or names are called "variables".

* In fact, we will probably call them variables in this class.

* That's because they are used, for the most part, for the same purposes.

* But often a "variable" is defined as something like:
  "a place in memory that can store values".

* That is **NOT** the same thing as a symbol or name in Python!

* A name can be bound to a value -- but that has nothing to do with a
  location in memory.

In-Place Assignment
-------------------

You can also do "in-place" assignment with ``+=``.

.. code-block:: ipython

    In [32]: a = 1

    In [33]: a
    Out[33]: 1

    In [34]: a = a + 1

    In [35]: a
    Out[35]: 2

    In [36]: a += 1

    In [37]: a
    Out[37]: 3

also: ``-=, *=, /=, **=, \%=``

**Note:** This is a bit tricky -- if the value is mutable, it is in-place assignment -- that is the object itself is changed. But if the value is immutable (can't be changed), then it is replaced with a new object.

Example with an immutable type:

.. code-block:: ipython

    In [11]: a = 5  # a is an integer -- an immutable type.

    In [12]: b = a  # a and b are names for the SAME integer

    In [13]: a += 5

    In [14]: a
    Out[14]: 10  # a is changed

    In [15]: b
    Out[15]: 5  # b is not.

Example with a mutable type:

.. code-block:: ipython

    In [16]: a = [1, 2, 3] # a is a mutable list

    In [17]: b = a  # b is now another name for the same list

    In [18]: a += [4, 5, 6] # in-place add more to a

    In [19]: b
    Out[19]: [1, 2, 3, 4, 5, 6]

    In [20]: # b is changed --it's the SAME list.


Multiple Assignment
-------------------

You can assign multiple names from multiple expressions in one
statement:

.. code-block:: ipython

    In [48]: x = 2

    In [49]: y = 5

    In [50]: i, j = 2 * x, 3 ** y

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243


Python evaluates all the expressions on the right before doing any assignments.


Nifty Python Trick
------------------

Using this feature, we can swap values between two names in one statement:

.. code-block:: ipython

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243

    In [53]: i, j = j, i

    In [54]: i
    Out[54]: 243

    In [55]: j
    Out[55]: 4

Multiple assignment and symbol swapping can be very useful in certain contexts.

Deleting
--------

You can't actually directly delete values in Python...

``del`` only deletes a name (or "unbinds" the name...)

.. code-block:: ipython

    In [56]: a = 5

    In [57]: b = a

    In [58]: del a

    In [59]: a
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-59-60b725f10c9c> in <module>()
    ----> 1 a

    NameError: name 'a' is not defined


The object is still there...Python will only delete it if there are no
references to it.

.. code-block:: ipython

    In [15]: a = 5

    In [16]: b = a

    In [17]: del a

    In [18]: a
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-18-60b725f10c9c> in <module>()
    ----> 1 a

    NameError: name 'a' is not defined

    In [19]: b
    Out[19]: 5


Identity
--------

Every value in Python is an object.

Every object is unique and has a unique *identity*, which you can inspect with
the ``id`` *builtin*:

.. code-block:: ipython

    In [68]: id(i)
    Out[68]: 140553647890984

    In [69]: id(j)
    Out[69]: 140553647884864

    In [70]: new_i = i

    In [71]: id(new_i)
    Out[71]: 140553647890984


Testing Identity
----------------

You can find out if the values bound to two different symbols are the **same
object** using the ``is`` operator:

.. code-block:: ipython

    In [72]: count = 23

    In [73]: other_count = count

    In [74]: count is other_count
    Out[74]: True

    In [75]: count = 42

    In [76]: other_count is count
    Out[76]: False

**NOTE:** Checking the id of an object, or using "is" to check if two objects are the same is rarely used except for debugging and understanding what's going on under the hood. They are not used regularly in production code.


Equality
--------

You can test for the equality of certain values with the ``==`` operator

.. code-block:: ipython

    In [77]: val1 = 20 + 30

    In [78]: val2 = 5 * 10

    In [79]: val1 == val2
    Out[79]: True

    In [80]: val3 = '50'

    In [81]: val1 == val3
    Out[84]: False

A string is never equal to a number!


Singletons
----------

Python has three "singletons" -- a value for which there is only one instance:

  ``True``, ``False``, and ``None``

To check if a name is bound to one of these, you use ``is``:

.. code-block:: python

    a is True

    b is False

    x is None

Note that in contrast to English -- "is" is asking a question, not making an assertion -- ``a is True`` means "is a set to the value True?"


Operator Precedence
-------------------

Operator Precedence determines what evaluates first:

.. code-block:: python

    4 + 3 * 5 != (4 + 3) * 5

To force statements to be evaluated out of order, use parentheses -- expressions in parentheses are always evaluated first:

   (4 + 3) * 5 != 4 + (3 * 5)

Python follows the "usual" rules of algebra.

Python Operator Precedence
--------------------------

Parentheses and Literals:
  ``(), [], {}``

  ``"", b'', ''``

Function Calls:
  ``f(args)``

Slicing and Subscription:
  ``a[x:y]``

  ``b[0], c['key']``

Attribute Reference:
  ``obj.attribute``

Exponentiation:
  ``**``

Bitwise NOT, Unary Signing:
  ``~x``

  ``+x, -x``

Multiplication, Division, Modulus:
  ``*, /, %``

Addition, Subtraction:
  ``+, -``

Bitwise operations:
  ``<<, >>,``

  ``&, ^, |``

Comparisons:
  ``<, <=, >, >=, !=, ==``

Membership and Identity:
  ``in, not in, is, is not``

Boolean operations:
  ``or, and, not``

Anonymous Functions:
  ``lambda``


String Literals
---------------

A "string" is a chunk of text.

You define a ``string`` value by writing a string *literal*:

.. code-block:: ipython

    In [1]: 'a string'
    Out[1]: 'a string'

    In [2]: "also a string"
    Out[2]: 'also a string'

    In [3]: "a string with an apostrophe: isn't it cool?"
    Out[3]: "a string with an apostrophe: isn't it cool?"

    In [4]: 'a string with an embedded "quote"'
    Out[4]: 'a string with an embedded "quote"'

.. code-block:: ipython

    In [5]: """a multi-line
       ...: string
       ...: all in one
       ...: """
    Out[5]: 'a multi-line\nstring\nall in one\n'

    In [6]: "a string with an \n escaped character"
    Out[6]: 'a string with an \n escaped character'

    In [7]: r'a "raw" string, the \n comes through as a \n'
    Out[7]: 'a "raw" string, the \\n comes through as a \\n'

Python3 strings fully support Unicode, which means they can support literally all the languages in the world (and then some -- Klingon, anyone? -- well `sort of. <http://www.personal.psu.edu/ejp10/blogs/gotunicode/2010/10/conscript-unicode-registry-csu.html>`_)

Because Unicode is native to Python strings, you can get very far without even thinking about it. Anything you can type in your editor will work fine.


Keywords
--------

Python defines a number of **keywords**

These are language constructs.

You *cannot* use these words as symbols.

::

    False     class	  finally      is          return
    None      continue    for          lambda      try
    True      def         from         nonlocal    while
    and       del         global       not         with
    as        elif        if           or          yield
    assert    else        import       pass
    break     except      in           raise



If you try to use any of the keywords as symbols, you will cause a
``SyntaxError``:

.. code-block:: ipython

    In [13]: del = "this will raise an error"
      File "<ipython-input-13-c816927c2fb8>", line 1
        del = "this will raise an error"
            ^
    SyntaxError: invalid syntax

.. code-block:: ipython

    In [14]: def a_function(else='something'):
       ....:     print(else)
       ....:
      File "<ipython-input-14-1dbbea504a9e>", line 1
        def a_function(else='something'):
                          ^
    SyntaxError: invalid syntax


__builtins__
------------

Python also has a number of pre-bound symbols, called **builtins**

Try this:

.. code-block:: ipython

    In [6]: dir(__builtins__)
    Out[6]:
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BaseException',
     'BufferError',
     ...
     'vars',
     'xrange',
     'zip']


You are free to rebind these symbols:

.. code-block:: ipython

    In [15]: type('a new and exciting string')
    Out[15]: str

    In [16]: type = 'a slightly different string'

    In [17]: type('type is no longer what it was')
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-17-907616e55e2a> in <module>()
    ----> 1 type('type is no longer what it was')

    TypeError: 'str' object is not callable

In general, this is a **BAD IDEA** -- hopefully your editor will warn you.


Exceptions
----------

Notice that the first batch of ``__builtins__`` are all *Exceptions*

Exceptions are how Python tells you that something has gone wrong.

There are several exceptions that you are likely to see a lot of:


* ``NameError``: indicates that you have tried to use a symbol that is not bound to a value.

* ``TypeError``: indicates that you have tried to use the wrong kind of object for an operation.

* ``SyntaxError``: indicates that you have mis-typed something.

* ``AttributeError``: indicates that you have tried to access an attribute or
  method that an object does not have (this often means you have a different
  type of object than you expect)


Functions
---------

**What is a function?**

A function is a self-contained chunk of code.

You use them when you need the same code to run multiple times,
or in multiple parts of the program.

Functions allow you to take code that would otherwise be duplicated potentially many times, and put it in one place. Then all you do is call that code to use it.

This is often referred to as "DRY" -- "Don't Repeat Yourself".

It also helps to keep the code clean and maintainable, as there is only one place to make a change. This in turn helps reduce defects.

Functions can take and return information.

The minimal function has at least one statement.

.. code-block:: python

    def a_name():
        a_statement


Pass Statement does nothing (Note the indentation!)

.. code-block:: python

    def minimal():
        pass

This, of course, has limited use -- you will generally have multiple statements in a function -- and they will do something.

However, the pass statement can help you by allowing you to create placeholder functions that you will come back to later to develop and embelish.

Functions: ``def``
------------------

``def``  is a *statement*:

  * it is executed
  * it creates a local name
  * it does *not* return a value


Function defs must be executed before the functions can be called:

.. code-block:: ipython

    In [23]: unbound()
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-23-3132459951e4> in <module>()
    ----> 1 unbound()

    NameError: name 'unbound' is not defined

.. code-block:: ipython

    In [18]: def simple():
       ....:     print("I am a simple function")
       ....:

    In [19]: simple()
    I am a simple function


Calling Functions
-----------------

You **call** a function using the function call operator (parentheses):

.. code-block:: ipython

    In [2]: type(simple)
    Out[2]: function

    In [3]: simple
    Out[3]: <function __main__.simple>

    In [4]: simple()
    I am a simple function

Calling a function is how you run the code in that function.


Functions: Call Stack
---------------------

Functions can call functions -- this makes what is called an execution stack. That is what a "trace back", often referred to in exceptions, is -- the function call stack.

.. code-block:: ipython

    In [5]: def exceptional():
       ...:     print("I am exceptional!")
       ...:     print 1/0
       ...:
    In [6]: def passive():
       ...:     pass
       ...:
    In [7]: def doer():
       ...:     passive()
       ...:     exceptional()
       ...:

You've defined three functions, one of which will *call* the other two.

When an error occurs, you are presented with a "traceback" of the call stack:

Functions: Tracebacks
---------------------

.. code-block:: ipython

    In [8]: doer()
    I am exceptional!
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-8-685a01a77340> in <module>()
    ----> 1 doer()

    <ipython-input-7-aaadfbdd293e> in doer()
          1 def doer():
          2     passive()
    ----> 3     exceptional()
          4

    <ipython-input-5-d8100c70edef> in exceptional()
          1 def exceptional():
          2     print("I am exceptional!")
    ----> 3     print(1/0)
          4

    ZeroDivisionError: integer division or modulo by zero

The error occurred in the ``doer`` function -- but the traceback shows you where that was called from.

Note that this listed in reverse order -- reverse of the order in which the functions are called.

In a more complex system, this can be VERY useful -- learn to read tracebacks!


Functions: ``return``
---------------------

Every function ends by returning a value.

This is actually the simplest possible function:

.. code-block:: python

    def fun():
        return None


If you don't explicitly put ``return``  there, Python will return ``None``:

.. code-block:: ipython

    In [9]: def fun():
       ...:     pass
       ...:
    In [10]: fun()
    In [11]: result = fun()
    In [12]: print(result)
    None

Note that the interpreter eats ``None`` -- you need to call ``print()`` to see it.

More on return
--------------

Only one return statement in a function will ever be executed.

Ever.

Anything after an executed return statement will never get run.

This is useful when debugging!

.. code-block:: ipython

    In [14]: def no_error():
       ....:     return 'done'
       ....:     # no more will happen
       ....:     print(1/0)
       ....:
    In [15]: no_error()
    Out[15]: 'done'


However, functions *can* return multiple results:

.. code-block:: ipython

    In [16]: def fun():
       ....:     return 1, 2, 3
       ....:
    In [17]: fun()
    Out[17]: (1, 2, 3)


Remember multiple assignment?

.. code-block:: ipython

    In [18]: x, y, z = fun()
    In [19]: x
    Out[19]: 1
    In [20]: y
    Out[20]: 2
    In [21]: z
    Out[21]: 3


Functions: parameters
---------------------

In a ``def`` statement, the values written *inside* the parens are
**parameters**

.. code-block:: ipython

    In [22]: def fun(x, y, z):
       ....:     q = x + y + z
       ....:     print(x, y, z, q)
       ....:

x, y, z are *local* names -- so is q


Functions: arguments
--------------------

When you call a function, you pass values to the function parameters as
**arguments**

.. code-block:: ipython

    In [23]: fun(3, 4, 5)
    3 4 5 12

The values you pass in are *bound* to the names inside the function and used.

The name used outside the object is separate from the name used inside the function.

Making a Decision
------------------

**"Conditionals"**

In order to do anything interesting at all, you need to be able to write code to make a decision.

``if`` and ``elif`` (else if) allow you to make decisions:

.. code-block:: ipython

    In [12]: def test(a):
       ....:     if a == 5:
       ....:         print("that's the value I'm looking for!")
       ....:     elif a == 7:
       ....:         print("that's an OK number")
       ....:     else:
       ....:         print("that number won't do!")

    In [13]: test(5)
    that's the value I'm looking for!

    In [14]: test(7)
    that's an OK number

    In [15]: test(14)
    that number won't do!

There is more to it than that, but this will get you started.


What's the difference between these two?

.. code-block:: python

    if a:
        print('a')
    elif b:
        print('b')

    ## versus...
    if a:
        print('a')
    if b:
        print('b')

Lists
-----

A way to store a bunch of stuff in order.

Pretty much like an "array" or "vector" in other languages.

To make a list literal you use square brackets and commas between the items:

.. code-block:: python

    a_list = [2,3,5,9]
    a_list_of_strings = ['this', 'that', 'the', 'other']

You can put any type of object in a list...

Lists are a key Python data type with lots of functionality that we will get into later.

``for`` loops
--------------

Sometimes called a 'determinate' loop.

When you need to do something to all the objects in a sequence:

.. code-block:: ipython

    In [10]: a_list = [2,3,4,5]

    In [11]: for item in a_list:
       ....:     print(item)
       ....:
    2
    3
    4
    5


``range()`` and for
-------------------

``range`` builds sequences of numbers automatically

Use it when you need to do something a set number of times:

.. code-block:: ipython

    num_stars = 4
    In [31]: for i in range(num_stars):
        print('*', end=' ')
       ....:
    * * * *

NOTE: ``range(n)`` creates an "iterable" -- something you can loop over.
We will cover iterables in greater depth in a later lesson.

``assert``
----------

Writing ``tests`` that demonstrate that your program works is an important part of learning to program.

The Python ``assert`` statement is useful in writing simple tests:
for your code.

.. code-block:: ipython

    In [1]: def add(n1, n2):
       ...:     return n1 + n2
       ...:

    In [2]: assert add(3, 4) == 7

    In [3]: assert add(3, 4) == 10

    ---------------------------------------------------------------------
    AssertionError                     Traceback (most recent call last)
    <ipython-input-3-6731d4ac4476> in <module>()
    ----> 1 assert add(3, 4) == 10

    AssertionError:


Intricacies
------------

This is enough to get you started.

Each of the feature we have covered has intricacies special to Python.

We'll get to those over the next couple of lessons -- or really, the rest of the program!


Enough For Now
--------------

That's it for our basic intro to Python.

You now know enough Python to do some basic exercises in Python programming.
