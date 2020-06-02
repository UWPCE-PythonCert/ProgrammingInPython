.. _exercise_context_manager:

###############################
A Couple Handy Context Managers
###############################

Context managers can be used in a number of ways -- the classic is to manage resources - that is, close files and the like.  But they are also useful for other handy things when you want to run some code before and after a block of code, or handle exceptions in special way.

Timing Context Manager
======================

This is an example of running some code before and after the enclosed block.

Create a context manager that will print the elapsed time taken to
run all the code inside the context:

.. code-block:: ipython

    In [3]: with Timer() as t:
       ...:     for i in range(100000):
       ...:         i = i ** 20
       ...:
    This code took 0.206805 seconds

NOTE: the ``time`` module has what you need:

.. code-block:: python

    import time

    start = time.clock()
    # some code here
    elapsed = time.clock() - start

``time.clock()`` returns the number of seconds that this process has been running.  You can also use ``time.time()``, which gives the "wall time", rather than the process time. ``time()`` will vary more depending on how busy the system is. But you may want to use it if you want to measure how long it takes to download something, for instance.

Extra Credit
------------

Allow the ``Timer`` context manager to take a file-like
object as an argument (the default should be ``sys.stdout``). The results of the
timing should be printed to the file-like object. You could also pass in a name for this particular context, so the message in the file-like object is labeled -- kind of a poor man's logging system.

Extra Extra Credit
------------------

Implement this as a generator, wrapped by the:

``contextlib.contextmanager``

decorator.

The pytest error handler
========================

pytest come with a nifty context manager for testing for error conditions:

.. code-block:: python

    with pytest.raises(ZeroDivisionError)
        5 / 0

The test should pass

But:

.. code-block:: python

    with pytest.raises(ZeroDivisionError)
        5 / 2

This test should fail -- no Exception occurred.

And so should this one:

.. code-block:: python

    with pytest.raises(ValueError)
        5 / 0

the wrong Exception occurred.

You task is to write a similar context manager (yes, it's already written, but this should help you understand how to handle exceptions in context managers...)


Extra Credit
------------

The pytest version has a few other features:

[https://docs.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions]

See if you can implement a few of them....

Hints:
------

tests fail when an assert fails:

.. code-block:: python

    assert some_expression, "a message"

you get a failure when ``some_expression`` evaluates as false.

This is more-or-less the same as this code:

.. code-block:: python

    if some_expression:
        raise AssertionError("a message")

The reason it exists is not so much to save a bit of typing (though that's nice), but that assertions are designed for tests, and thus can be turned off for an entire python process -- and, indeed are turned off when you turn on optimization.

So in your context manager, you can raise an AssertionError, or force one with an assert:

.. code-block:: python

    assert False, "a message"

either will work fine.

See:
:download:`raising_an_assert.py <../examples/context_managers/raising_an_assert.py>`
