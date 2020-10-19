.. _py2_vs_py3:

########################
Python 2 versus Python 3
########################

now that Python version 2 has officially reached end of life, most recent information is in/about Python 3.

But you will still find a lot of older example code online in Python2, rather than Python3

For the most part, they are the same -- so you can use those examples to learn from.

There are a lot of subtle differences that you don't need to concern yourself with just yet.

But a couple that you'll need to know right off the bat:

print()
-------

In Python2, ``print`` is a "statement", rather than a function. That means it didn't require parentheses around what you want printed:

.. code-block:: python

  print something, something_else

This made it a bit less flexible and powerful.

But -- if you try to use it that way in Python3, you'll get an error:

.. code-block:: python

  In [15]: print "this"
    File "<ipython-input-15-70c8add5d16e>", line 1
      print "this"
                 ^
  SyntaxError: Missing parentheses in call to 'print'

So -- if you get this error, simply add the parentheses:

.. code-block:: ipython

  In [16]: print("this")
  this

Division
--------

In python 3, the division operator is "smart" when you divide integers:

.. code-block:: ipython

  In [17]: 1 / 2
  Out[17]: 0.5

However in Python2, integer division, will give you an integer result:

.. code-block:: ipython

  In [1]: 1/2
  Out[1]: 0

In both versions, you can get "integer division" if you want it with a double slash:

.. code-block:: ipython

  In [1]: 1//2
  Out[1]: 0

And in Python2, you can get the behavior of Python3 with "true division":

.. code-block:: ipython

  In [2]: from __future__ import division

  In [3]: 1/2
  Out[3]: 0.5

For the most part, you just need to be a bit careful with the rare cases where Python2 code counts on integer division.

Iterators vs Lists
------------------

In Python2, a number of functions returned a full list of the contents. But most of the time, you didn't need a list -- you only needed a way to loop through all the items returned. Such an object is called an "iterable" -- more about that later in the class. But for now, if you get an error like::

  TypeError: 'dict_keys' object does not support indexing

Then you likely got an iterator, rather than a "proper" list.  You can fix this by making a list out of it::

  list(an_iterator)

the list constructor will make a list out of any iterable.  So you can now index it, etc.

Other Python2 / Python3 differences
-----------------------------------

The most drastic difference (improvement!) is better Unicode support, and better bytes / Unicode separation.

Most of the other differences are essentially implementation details, like getting iterators instead of sequences -- we'll talk about that more when it comes up in a later lesson.

There are also a few syntax differences with more advanced topics: Exceptions, ``super()``, etc.

