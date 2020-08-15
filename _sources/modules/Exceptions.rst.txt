.. _exceptions:

##################
Exception Handling
##################

Exceptions are a really nifty Python feature -- really handy!

From the zen:

.. centered:: "Errors should never pass silently."

.. centered:: "Unless explicitly silenced."


That's what exception handling is all about.

Exceptions
----------

An "Exception" is an indication that something out of the ordinary (exceptional) happened.

Note that they are NOT called "Errors" -- often they are errors, but an Exception is not an indication of an error per se.

This is why exception handling exists -- we often know that exceptions will occur, and know how to handle them -- we don't want the program to crash out.

NOTE: if an Exception is raised in a Python program, and it has not been handled, then the program will stop, and report what happened. I'm sure you have seen this many times while working on your code!


Handling Exceptions
-------------------

So far, Exceptions in your code have indicated a bug that you need to fix. But frequently you can anticipate where an Exception might occur, and your code can do something about it -- give a nice message to the user, or try the operation again in a different way -- the options are endless. Doing something after an Exception has occurred is known as "handling" the Exception.

Exceptions are handled with a "try -- except" block.

This provides another branching structure (kind of like if) -- a way for different code to run depending on what happens in a code block.

Here is an example:

.. code-block:: python

    try:
        with open('missing.txt') as data_file:
            process(data_file)   # never called if file missing
    except FileNotFoundError:
        print("Couldn't find missing.txt")

The ``try:`` block is code that you want to "try" to run. In this case, it's opening and processing a file. But if the file isn't there, then a ``FileNotFoundError`` is "raised". When an Exception is raised, no further code is run -- so the ``process()`` function will not be called. Once an exception is raised, Python looks for an ``except`` line. If the raised Exception matches the one in the ``except`` line, then the code in that block is run.

If there is no ``except``, or the Exception doesn't match, then python will keep moving "up the stack", until the Exception is caught. If it is never caught, then the program will terminate.


Bare ``except``
---------------

*Never* do this:

.. code-block:: python

    try:
        with open('missing.txt') as data_file:
            process(data_file)   # never called if file missing
    except:
        print "couldn't find missing.txt"

If you don't specify a particular exception, ``except`` will catch *All* exceptions.

**Always** capture the *particular* Exception(s) you know how to handle.

Trust me, you can't anticipate everything, and you want the exception to propagate if it is not the one expected when you wrote the code.


Testing for errors "by hand":
-----------------------------

Use Exceptions, rather than your own tests:

Don't do this:

.. code-block:: python

    do_something()
    if os.path.exists('missing.txt'):
        f = open('missing.txt')
        process(f)

It will almost always work -- but the *almost* will drive you crazy.

It is "possible" that the file got deleted by another process in the precise moment between checking for it and opening it. Rare, but possible. Catching the exception will always work -- even in that rare case.


Example from mailroom exercise:
-------------------------------

You want to convert the user's input into an integer. And you want to give a nice message if the user didn't provide a valid input.

So you could do this:

.. code-block:: python

    if num_in.isdigit():
        num_in = int(num_in)

But -- ``int(num_in)`` will only work if the string can be converted to an integer.

So you can also do:

.. code-block:: python

    try:
        num_in = int(num_in)
    except ValueError:
        print("Input must be an integer, try again.")
        continue

This is particularly helpful for things like converting to a float -- much more complicated to check -- and all that logic is already in the ``float()`` constructor.

Or let the Exception be raised if you can't handle it.

EAFP
----

This is all an example of the EAFP principle:

  "It's Easier to Ask Forgiveness than Permission"

    -- Grace Hopper

The idea is that you want to try to do what you want to do -- and then handle it if it doesn't work (forgiveness).

Rather than check to see if you can do it before trying (permission).

Here's a nice PyCon talk by Alex Martelli about that:

http://www.youtube.com/watch?v=AZDWveIdqjY

(Alex Martelli is a Python Luminary -- read / watch anything you find by him).


Do you catch all Exceptions?
----------------------------

For simple scripts, let exceptions happen.

Only handle the exception if the code can and will do something (useful) about it.

This results in much better debugging info when an error does occur.  The user will see the exception, and where in the code it happened, etc.


Exceptions -- ``finally``
-------------------------

There is another component to exception handling control structures:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except FileNotFoundError:
        print("couldn't open missing.txt")
    finally:
        do_some_clean-up

The code in the ``finally:``  clause will always run.

This is really important if your code does anything before the exception occurred that needs to be cleaned up -- open database connection, etc...

**NOTE:** In the above example, you can often avoid all that exception handling code using a with statement:

.. code-block:: python

    with open('missing.txt') as f:
        process(f)

In this case, the file will be properly closed regardless. And many other systems, like database managers, etc. can also be used with ``with``.

This is known as a "context manager", and was added to Python specifically to handle the common cases that required ``finally`` clauses. But if your use case does not already have a context manager that handles the cleanup you may need.

Exceptions -- ``else``
----------------------

Yet another flow control option:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError:
        print("couldn't open missing.txt")
    else:
        process(f) # only called if there was no exception

So the ``else`` block only runs if there was no exception. That was also the case in the previous code, so what's the difference?

**Advantage of** ``else`` **:**

Using the ``else`` block lets you catch the exception as close to where it occurred as possible -- always a good thing.

Why? -- because maybe the ``process(f)`` could raise an exception, too? Then you don't know if the exception came from the ``open()`` call or in some code after that.

This bears repeating:

**Always catch exceptions as close to where they might occur as you can**.

Exceptions -- using the Exception object
----------------------------------------

What can you do in an ``except`` block?

If your code can continue along fine, you can do very little and move along:

.. code-block:: python

    try:
        do_something()
    except ValueError:
        print("That wasn't any good")

And that's that.

But if your code *can't* continue on, you can re-raise the exception:

.. code-block:: python

    try:
        do_something()
    except ValueError:
        print("That wasn't any good")
        raise

The ``raise`` statement will re-raise the same exception object, where it may get caught higher up in the code, or even end the program.

Exception objects are full-fledged Python objects -- they can contain data, and you can add data to them. You can give a name to a raised Exception with ``as``:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError as the_error:
        print(the_error)
        the_error.extra_info = "some more information"
        raise

This prints the exception, then adds some extra information to it, and then re-raises the same exception object -- so it will have that extra data when it gets handled higher up on the stack.

This is particularly useful if you catch more than one exception:

.. code-block:: python

    except (IOError, BufferError, OSError) as the_error:
        do_something_with(the_error)

You may want to do something different depending on which exception it is. And you can inspect the Exception object to find out more about it.  Each Exception has different information attached to it -- you'll need to read its docs to see.

For an example -- try running this code:

.. code-block:: ipython

    In [34]: try:
        ...:     f = open("blah")
        ...: except IOError as err:
        ...:     print(err)
        ...:     print(dir(err))
        ...:     the_err = err

The ``print(dir(err))`` will print all the names (attributes) in the error object. A number of those are ordinary names that all objects have, but a few are specific to this error.

the ``the_err = err`` line is there so that we can keep a name bound to the ``err`` after the code is run. ``err`` as bound by the except line only exists inside the following block.

Now that we have a name to access it, we can look at some of its attributes. The name of the file that was attempted to be opened:

.. code-block:: ipython

    In [35]: the_err.filename
    Out[35]: 'blah'

The message that will be printed is usually in the ``.args`` attribute:

.. code-block:: ipython

    In [37]: the_err.args
    Out[37]: (2, 'No such file or directory')

the ``.__traceback__`` attribute hold the actual traceback object -- all the information about the context the exception was raised in. That can be inspected to get all sorts of info. That is very advanced stuff, but you can investigate the ``inspect`` module if you want to know how.

Multiple Exceptions
-------------------

As seen above, you can catch multiple exceptions with a single ``except`` statement by putting them all in a tuple:

.. code-block:: python

try:
    some_code()
except (Exception1, Exception2, Exception3):
    handle_them_all

You should do this if the action required is same for all those Exceptions.


But if you want to do something different with each exception type, you can have multiple ``except`` blocks:


.. code-block:: python

    try:
       some_code
    except IOError:
        handle_the_error
    except BufferError:
        handle_the_error
    except OSError:
        handle_the_error

So a full-featured ``try`` block has all of this:

.. code-block:: python

    try:
       some_code
    except IOError:
        handle_the_error
    except BufferError:
        handle_the_error
    ...
    else:
        some code to run if none of these exceptions occurred
    finally:
        some code to run always.

The minimal try block is a ``try``, and one ``except``.

Raising Exceptions
-------------------

Many times, Exceptions will be raised by a built in python function, or from some library code that you are using. But there are times when the code you write may not directly handle some particular behavior. In that case, you can raise an exception yourself, and then it can be caught by code higher up the stack. This is done with the ``raise`` statement:

.. code-block:: python

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("b can not be zero")
        else:
            return a / b

(OK, this is a stupid example, as that error will be raised for you anyway. But bear with me).

When you call that function with a zero:

.. code-block:: ipython

    In [515]: divide (12, 0)
    ZeroDivisionError: b can not be zero

Note how you can pass a message to the exception object constructor. It will get printed when the exception is printed. (and it is stored the in the Exception object's ``.args`` attribute)


Built in Exceptions
-------------------

You can create your own custom exceptions.

But for the most part, you can/should use a built in one ...

.. code-block:: python

    exp = \
     [name for name in dir(__builtin__) if "Error" in name]
    len(exp)
    48

There are 48 built-in Exceptions -- odds are good that there's one that matches your use-case.

Also -- custom exceptions require subclassing -- and you haven't learned that yet :-).


Choosing an Exception to raise
------------------------------

Choose the best match you can for the built in Exception you raise.

Example::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise ValueError

Is the *value* of the input the problem here?

Nope: the *type* of the input is the problem::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise TypeError

but should you be checking type anyway? (EAFP)

What I usually do is run some code that's similar that raises a built-in exception, and see what kind it raises, then I use that.


Knowing what Exception to catch
-------------------------------

I usually figure out what exception to catch with an iterative process.

I write the code without a try block, pass in "bad data", or somehow trigger the exception, then see what it is.

Example:

What if the file I want to read doesn't exist?

.. code-block:: ipython

    In [7]: open("some_non_existant_file")
    ---------------------------------------------------------------------------
    FileNotFoundError                         Traceback (most recent call last)
    <ipython-input-7-a18e010ecdd0> in <module>()
    ----> 1 open("some_non_existant_file")

    FileNotFoundError: [Errno 2] No such file or directory: 'some_non_existant_file'

Now I know to use::

    except FileNotFoundError:

In the ``try`` block where I am opening the file.



