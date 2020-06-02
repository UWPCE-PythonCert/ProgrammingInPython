.. _map_filter_reduce:

#####################
Map Filter and Reduce
#####################

``map``, ``filter``, and ``reduce`` are considered key parts of "functional programming"

But there is no real consensus about what "functional" means.

But Python does support these "classic" functional methods.


map
---

``map``  "maps" a function onto a sequence of objects -- It applies the function to each item in the sequence, returning an "iterable" "map object".

The map object delays evaluation until you iterate over it. That way you can pass it to another map, or use it in a for loop, without creating an unnecessary copy of the list.

.. code-block:: ipython

    In [4]: l = [2, 5, 7, 12, 6, 4]

    In [5]: def fun(x):
       ...:     return x*2 + 10
       ...:

    In [6]: map(fun, l)
    Out[6]: <map at 0x1046f2ac8>

    In [7]: list(map(fun, l))
    Out[7]: [14, 20, 24, 34, 22, 18]

And if it's a small function, and you only need it once, this is a great use for ``lambda``

.. code-block:: ipython

    In [26]: list(map(lambda x: x*2 + 10, l))
    Out[26]: [14, 20, 24, 34, 22, 18]

filter
------

``filter``  "filters" a sequence of objects with a boolean function --
It keeps only those for which the function is True -- filtering out the rest.

It similarly returns an iterable object.

To get only the even numbers:

.. code-block:: ipython

    In [27]: l = [2, 5, 7, 12, 6, 4]
    In [28]: list(filter(lambda x: not x%2, l))
    Out[28]: [2, 12, 6, 4]

If you pass ``None`` to ``filter()``, you get only items that evaluate to true:

.. code-block:: ipython

    In [1]: l = [1, 0, 2.3, 0.0, 'text', '', [1,2], [], False, True, None ]

    In [2]: list(filter(None, l))
    Out[2]: [1, 2.3, 'text', [1, 2], True]

reduce
------

``reduce``  "reduces" a sequence of objects to a single object with a function that combines two arguments.

In python3, reduce has been a bit hidden in the "functools" module:

.. code-block:: python

  from functools import reduce

To get the sum:

.. code-block:: ipython

    In [11]: from functools import reduce
    In [12]: l = [2, 5, 7, 12, 6, 4]
    In [13]: reduce(lambda x,y: x+y, l)
    Out[13]: 36


To get the product:

.. code-block:: ipython

    In [32]: reduce(lambda x,y: x*y, l)
    Out[32]: 20160

or

.. code-block:: ipython

    In [13]: import operator
    In [14]: reduce(operator.mul, l)
    Out[14]: 20160

Comprehensions
--------------

Couldn't you do all this with comprehensions?

Yes:

.. code-block:: ipython

    In [33]: [x+2 + 10 for x in l]
    Out[33]: [14, 17, 19, 24, 18, 16]

    In [34]: [x for x in l if not x%2]
    Out[34]: [2, 12, 6, 4]

    In [6]: l
    Out[6]: [1, 0, 2.3, 0.0, 'text', '', [1, 2], [], False, True, None]
    In [7]: [i for i in l if i]
    Out[7]: [1, 2.3, 'text', [1, 2], True]

(Except Reduce)

But Guido thinks almost all uses of reduce are really ``sum()``. In fact, that's why it got moved out of built-ins into the ``functools`` module.


Functional Programming
----------------------

Comprehensions and map, filter, reduce are all "functional programming" approaches.

``map, filter``  and ``reduce``  pre-date comprehensions in Python's history

Some people like that syntax better.

And "map-reduce" is a big concept these days for parallel processing of "Big Data" in NoSQL databases.

(Hadoop, MongoDB, etc.)

