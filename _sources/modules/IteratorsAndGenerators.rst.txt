.. _iterators_generators:

Iterators and Generators
=========================

  The Tools of Pythonicity

    What goes on in those for loops?


A note about Python History
---------------------------

Python 2
.........

Python used to be all about sequences -- a good chunk of anything you did
was stored in a sequence, or involved manipulating a sequence.

- lists
- tuples
- strings

- ``dict.keys()``
- ``dict.values()``
- ``dict.items()``
- ``zip()``
- ...

In python2 -- those are all sequences. (in the case of zip and dict methods, they return actual lists)

But it turns out that the most common operation for sequences is to iterate through them:

.. code-block:: python

  for item in a_sequence:
      do_something_with_item

So fairly early in Python2, Python introduced the idea of the "iterable".

More or less, an "iterable" is something you can, well, iterate over in
a for loop, but often does not keep the whole sequence in memory at once.

After all -- why make a copy of something just to look at all its items?

Example:

In python2: ``dict.keys()`` returns a list of all the keys in the dict.
But why make a full copy of all the keys, when all you want to do is:

.. code-block:: python

    for k in dict.keys():
        do_something_with(k)

Even worse: ``dict.items()`` created a full list of ``(key, value)`` tuples.
-- a complete copy of all the data in the dict.

Even worse still: ``enumerate(dict.items())`` created a whole list of
``(index, (key, value))`` tuples -- lots of copies of everything.

Enter ``iter*``

Python2 then introduced "iterable" versions of a number of functions and methods:

``itertools.izip``
``dict.iteritems()``
``dict.iterkeys()``
``dict.itervalues()``

So you could now iterate through that stuff without copying anything. Nice performance benefits, but a somewhat ugly interface.

Python3
.......

Python3 embraces iterables -- now everything that could be an iterable without making a copy is done that way -- no unnecessary copies.

If you DO need an actual sequence (becasue you want to do something with it other than iterate over it), you have to make a list out of them explicitly:

``list(dict.keys())``

Then there is an entire module: ``itertools`` that provides nifty ways
to iterate through stuff.

That will be covered elsewhere.

So while I used to say that python was "all about sequences", I know say:

    "Python is all about iterables


Iterators and Iterables
-----------------------

Iteration is one of the main reasons Python code is so readable:

.. code-block:: python

    for x in just_about_anything:
        do_stuff(x)

An "iterable" is anything that can be looped over sequentially, so it does not have to be
a "sequence": list, tuple, etc.  For example, a string is iterable. So is a set.

An iterator is an iterable that remembers state. All sequences are iterable, but
not all sequences are iterators. To make a sequence an iterator, you can call it with iter:

.. code-block:: python

   my_iter = iter(my_sequence)

Iterator Types:

https://docs.python.org/3/library/stdtypes.html#iterator-types

Iterables
---------

To make an object iterable, you simply have to implement the ``__getitem__`` method.

.. code-block:: python

    class T:
        def __getitem__(self, position):
            if position > 5:
                raise IndexError
            return position


``iter()``
----------

How do you get the iterator object from an "iterable"?

The ``iter`` function will make any iterable an iterator. It first looks for the ``__iter__``
method, and if none is found, uses ``__getitem__`` to create the iterator.

The ``iter()`` function:

.. code-block:: ipython

    In [20]: iter([2,3,4])
    Out[20]: <listiterator at 0x101e01350>

    In [21]: iter("a string")
    Out[21]: <iterator at 0x101e01090>

    In [22]: iter( ('a', 'tuple') )
    Out[22]: <tupleiterator at 0x101e01710>


List as an Iterator:
--------------------

.. code-block:: ipython

    In [10]: a_list = [1,2,3]

    In [11]: list_iter = iter(a_list)

    In [12]: next(list_iter)
    Out[12]: 1

    In [13]: next(list_iter)
    Out[13]: 2

    In [14]: next(list_iter)
    Out[14]: 3

    In [15]: next(list_iter)
    --------------------------------------------------
    StopIteration     Traceback (most recent call last)
    <ipython-input-15-1a7db9b70878> in <module>()
    ----> 1 next(list_iter)
    StopIteration:

Using iterators when you can
----------------------------

consider the example from the trigrams problem:

(http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/)

You have a list of words: ``words``

And you want to go through it, three at a time, and match up pairs with
the following word.

The *non-pythonic* way to do that is a loop through the indices:

.. code-block:: python

  for i in range(len(words)-2):
     triple = words[i:i+3]

It works, and is fairly efficient, but what about:

.. code-block:: python

    for triple in zip(words[:-2], words[1:-1], words[2:]):


``zip()`` returns an iterable -- it does not build up the whole list.
So this is quite efficient.

but we are still slicing: ([1:]), which produces a copy -- so we are creating three copies of
the list -- not so good if memory is tight. Note that they are shallow copies, so not **that** bad.

Nevertheless, we can do better:

The ``itertools`` module has a ``islice()`` (iterable slice) function.
It returns an iterator over a slice of a sequence -- so no more copies:

.. code-block:: ipython

    from itertools import islice

    In [68]: triplets = zip(words, islice(words, 1, None), islice(words, 2, None))

    In [69]: for triplet in triplets:
        ...:     print(triplet)
        ...:
    ('this', 'that', 'the')
    ('that', 'the', 'other')
    ('the', 'other', 'and')
    ('other', 'and', 'one')
    ('and', 'one', 'more')


The Iterator Protocol
----------------------

The main thing that differentiates an iterator from an iterable (sequence)
is that an iterator saves state.

An iterable must have the following methods:

.. code-block:: python

    an_iterator.__iter__()

Usually returns the iterator object itself.

.. code-block:: python

    an_iterator.__next__()

Returns the next item from the container. If there are no further items,
raises the ``StopIteration`` exception.


Making an Iterator
-------------------

A simple version of ``range()``

.. code-block:: python

    class IterateMe_1:
        def __init__(self, stop=5):
            self.current = 0
            self.stop = stop
        def __iter__(self):
            return self
        def __next__(self):
            if self.current < self.stop:
                self.current += 1
                return self.current
            else:
                raise StopIteration


What does ``for`` do?
----------------------

Now that we know the iterator protocol, we can write something like a for loop:

:download:`my_for.py <../examples/iterators_generators/my_for.py>`

.. code-block:: python

    def my_for(an_iterable, func):
        """
        Emulation of a for loop.

        func() will be called with each item in an_iterable
        """
        # equiv of "for i in l:"
        iterator = iter(an_iterable)
        while True:
            try:
                i = next(iterator)
            except StopIteration:
                break
            func(i)


Itertools
---------

``itertools``  is a collection of utilities that make it easy to
build an iterator that iterates over sequences in various common ways

http://docs.python.org/3/library/itertools.html

https://pymotw.com/3/itertools/index.html

NOTE:

iteratables are not *only* for ``for``

They can be used with anything that expects an iterable:

``sum``, ``tuple``, ``sorted``, ``list``, ...

Is an iterator a type?
----------------------

Iterators are not a type. An "iterable" is anything that has an ``__iter__``
method that returns an iterator and/or has a ``__getitem__`` method that takes 0-based indexes.

An "iterator" is anything that conforms to the "iterator protocol":

 - Has a ``__next__()`` method that returns objects.
 - Raises ``StopIteration`` when their are no more objects to be returned.
 - Has a ``__iter__()`` method that returns an iterator -- usually itself.
   - sometimes the ``__iter__()`` method re-sets the iteration...

https://docs.python.org/3/glossary.html#term-iterator

Lots of common iterators are different types:

.. code-block:: ipython

  In [23]: type(iter(range(5)))
  Out[23]: range_iterator

  In [24]: iter(list())
  Out[24]: <list_iterator at 0x104437fd0>

  In [27]: type(iter(zip([],[])))
  Out[27]: zip

Here's a nice overview:

http://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/

LAB
----


:download:`iterator_1.py <../examples/iterators_generators/iterator_1.py>`

* Extend (``iterator_1.py`` ) to be more like ``range()`` -- add three input parameters: ``iterator_2(start, stop, step=1)``

* What happens if you break from a loop and try to pick it up again:

.. code-block:: python

    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)

.. code-block:: python

    for i in it:
        print(i)

* Does ``range()``  behave the same?

  - make yours match ``range()``

  - is range an iterator or an iteratable?


Generators
----------

Generators

* give you an iterator object
* no access to the underlying data ... if it even exists


Conceptually:
  Iterators are about various ways to loop over data.

  Generators can generate the data on the fly.

Practically:
  You can use either one either way (and a generator is one type of iterator).

  Generators do some of the book-keeping for you -- simpler syntax.

  Generators also can be used for times you want to pause a function
  and pick it back up later where you left off.


yield
------

``yield``  is a way to make a quickie generator with a function:

.. code-block:: python

    def a_generator_function(params):
        some_stuff
        yield something

Generator functions "yield" a value, rather than returning a value.

It *does* 'return' a value, but rather than ending execution of the
function -- it preserves the state so it can pick up where it left off.

State is preserved in between yields.

A function with ``yield``  in it is a "factory" for a generator

Each time you call it, you get a new generator:

.. code-block:: python

    gen_a = a_generator()
    gen_b = a_generator()

Each instance keeps its own state.

Really just a shorthand for an iterator class that does the book keeping for you.

To master yield, you must understand that when you call the function,
the code you have written in the function body does not run. The function
only returns the generator object. The actual code in the function is run
when ``next()`` is called on the generator itself.

And note that each time you call the "generator function" you get a new
instance of a generator object that saves state separately from other instances.

An example: like ``range()``

.. code-block:: python

    def y_range(start, stop, step=1):
        i = start
        while i < stop:
            yield i
            i += step

Real World Example from FloatCanvas:

https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L100



Note:

.. code-block:: ipython

    In [164]: gen = y_range(2,6)
    In [165]: type(gen)
    Out[165]: generator
    In [166]: dir(gen)
    Out[166]:
    ...
     '__iter__',
    ...
     '__next__',


So the generator **is** an iterator

Note: A generator function can also be a method in a class

In fact, this is a nice way to provide different ways to iterate over
the data in a class in multiple ways.

This is done by the dict protocol with ``dict.keys()`` and ``dict.values()``.

More about iterators and generators:

Chapter 14 in Fluent Python by Luciano Ramalho

http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/

:download:`yield_example.py <../examples/iterators_generators/yield_example.py>`

generator comprehensions
------------------------

yet another way to make a generator:

.. code-block:: python

    >>> [x * 2 for x in [1, 2, 3]]
    [2, 4, 6]
    >>> (x * 2 for x in [1, 2, 3])
    <generator object <genexpr> at 0x10911bf50>
    >>> for n in (x * 2 for x in [1, 2, 3]):
    ...   print n
    ... 2 4 6


More interesting if [1, 2, 3] is also a generator

Note that `map` and `filter` produce iterators.

Keep in mind -- if all you need to do with the results is loop over it
-- use a generator expression rather than a list comprehension.

Other uses for ``yield``
------------------------

The ``yield`` keyword and generator functions were designed with classic "generators" in mind.

That is -- objects that generate values on the fly.

But, as we alluded to earlier, ``yield`` can be used for other things as well.

Anytime you want to return a value, and then hold state until later,
``yield`` can be used.

**Example:** pytest fixtures:

.. code-block:: python

    @pytest.fixture
    def example_fixture(request):
        # setup code here
        value = something()
        yield value  # provide the fixture value
        # do the teardown
        something_with(value)

In this case, the ``yield`` isn't in any sort of loop or anything.
It will only get run once. But the generator will maintain state,
so the value can be used after the yield to do the teardown.

How would this be done without yield? You'd need to store the value in a class:

.. code-block:: python

    class a_fixture():

        def __call__(self):
            # make it callable so it can provide the value
            # setup code here
            value = something()
            self.value = value
            return value

        def teardown(self):
            something_with(self.value)

Not horrible, but not as clean and simple.

LAB
---

Write a few generators:

* Sum of integers
* Doubler
* Fibonacci sequence
* Prime numbers

Test code in:

:download:`test_generator.py <../examples/iterators_generators/test_generator.py>`

Descriptions:

Sum of the integers:
  keep adding the next integer

  0 + 1 + 2 + 3 + 4 + 5 + ...

  so the sequence is:

  0, 1, 3, 6, 10, 15 .....


Doubler:
  Each value is double the previous value:

  1, 2, 4, 8, 16, 32,

Fibonacci sequence:
  The fibonacci sequence as a generator:

  f(n) = f(n-1) + f(n-2)

  1, 1, 2, 3, 5, 8, 13, 21, 34...

Prime numbers:
  Generate the prime numbers (numbers only divisible by them self and 1):

  2, 3, 5, 7, 11, 13, 17, 19, 23...

Others to try:
  Try x^2, x^3, counting by threes, x^e, counting by minus seven, ...

