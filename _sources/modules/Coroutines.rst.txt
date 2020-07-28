.. _coroutines:

###################
Notes on Coroutines
###################

.. note:: These notes are incomplete, but maybe the first section is still useful?

Coroutines are a key feature required to do "proper" async programming in Python.

In practical use, coroutines are used in the context of an async framework that
provides handy utilities, and most importantly, an event loop to actually run the code.

But it's helpful to play around a bit with coroutines on their own, to get a better understanding of what they really are, and how they work.

What is a coroutine?
====================

Coroutines are functions that can hold state, and vary between invocations;
there can be multiple instances of a given coroutine at once.

This may sound a bit familiar from generators -- a generator function can hold
state when it yields, and there can be multiple instances of the same generator
function at once.

The difference is that coroutines, in addition to holding state, can also return
control flow back to the system while they are holding that state.

Hopefully this will make a bit more sense after we've experimented a bit.


Coroutines By Themselves
========================

Coroutines are really only useful when controlled by an event loop.  And for the most part, you are going to use an event loop provided by an async framework, like the built in``asyncio`` package.

But it can be instructive to know about what is going on directly with coroutines, so we'll experiment a bit here:

We can make a coroutine with the ``async`` keyword:

.. code-block:: python

  async def corout():
    print("running corout")

This, of course is a coroutine that does nothing but print a message. But let's run it and see what happens:

.. code-block:: ipython

    In [28]: corout()
    Out[28]: <coroutine object corout at 0x1063ef6d0>

Hmm -- nothing. The print statement didn't happen. But what we got back is a "coroutine object". So calling a coroutine function doesn't run the code in the function, but rather creates a coroutine object and returns that. In fact, you can make any number of coroutine objects with the same "async def" function.

Why is that?

Recall from the definition of coroutines: "... that can hold state". So you want to be able to create multiple instances of a coroutine, so each one can hold different state (again, very similar to generators).

So how do we actually run the code in the coroutine instance? First, we need to save it in a variable so we can refer to it, and then we can call its ``send`` method.

.. code-block:: ipython

    In [33]: cr = corout()

    In [34]: type(cr)
    Out[34]: coroutine

    In [35]: cr.send(None)
    running corout
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    <ipython-input-35-72be8e65d115> in <module>()
    ----> 1 cr.send(None)

    StopIteration:

So calling ``send`` ran the print statement, and then raised a ``StopIteration`` exception.  This is looking even more like a generator, isn't it?

.. code-block:: ipython

    In [36]: def genfunction():
        ...:     print("in the generator")
        ...:     yield None
        ...:

    In [37]: g = genfunction()

    In [38]: next(g)
    in the generator

    In [39]: next(g)
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    <ipython-input-39-5f315c5de15b> in <module>()
    ----> 1 next(g)

    StopIteration:

And indeed, they have a lot on common -- in fact, before Python 3.5, when the ``async`` keyword was added, you used generator functions to make coroutines.

But if a coroutine raises ``StopIteration`` right away, what's the point? Well, recall that the point of a coroutine (and asnyc in general), is to be able to return control to the system, while you wait for something else to happen. And thus the "await" keyword. So a coroutine isn't useful unless it uses ``await``

``await an_awaitable`` suspends the coroutine until something is done, then returns the "awaitable"'s result.

hmm -- we have a trick here -- we need an "awaitable" object -- how do we get one of those? Well, a coroutine is awaitable, so let's make the simplest one of those:




