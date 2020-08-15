.. _dicts_and_sets:

#####################
Dictionaries and Sets
#####################

Dictionary
==========

Python calls it a ``dict``

Other languages call it:

  * dictionary
  * associative array
  * map
  * hash table
  * hash
  * key-value pair

It is also known in Python as a "mapping", as it "maps" keys to values.

It is like an array, in that it holds a number of items, and you can index into it to get at particular items. But it can use arbitrary indexes, rather than a sequence of numbers.

These indexes are called "keys", and the items stored are called "values".

So for any Python sequence, you might do::

  item = stuff[3]

for a dict, you do::

  item = stuff["third"]

.. note:: It is *very* common to use strings as keys in a dictionary. So common that virtually all examples you'll see both here and on the Internet use strings as keys. And many other languages have similar objects that only allow strings (like JavaScript objects, for instance). Python dicts, on the other hand, can use many types as keys, and this can be a very powerful feature to keep in mind.


Dictionary Constructors
-----------------------

So how does one make a dict? There are a few ways...

The dict "literal":

.. code-block:: python

    # This dict "lies"
    >>> {'key1': 3, 'key2': 5}
    {'key1': 3, 'key2': 5}

Calling the dict type object constructor:

.. code-block:: python

    # passing in a sequence of (key,value) pairs:
    >>> dict([('key1', 3), ('key2', 5)])
    {'key1': 3, 'key2': 5}

    # passing keys and values as keyword arguments:
    >>> dict(key1=3, key2= 5)
    {'key1': 3, 'key2': 5}

    # creating an empty dict, and then populating it:
    >>> d = {}
    >>> d['key1'] = 3
    >>> d['key2'] = 5
    >>> d
    {'key1': 3, 'key2': 5}


Dictionary Indexing
-------------------

And how do you get stuff out (index it)?

The same way you index a sequence, except the index (now called a key) can be various types, rather than just an integer:

.. code-block:: python

    >>> d = {'name': 'Brian', 'score': 42}

    >>> d['score']
    42

    >>> d = {1: 'one', 0: 'zero'}

    >>> d[0]
    'zero'

What if the key doesn't exist in the dict? You get a ``KeyError`` exception:

.. code-block:: python

    >>> d['non-existing key']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'non-existing key'



What can keys be?
-----------------

Surely not ANYTHING?

Not quite: keys can be any "immutable":

  * number
  * string
  * tuple

.. code-block:: ipython

    In [325]: d[3] = 'string'
    In [326]: d[3.14] = 'pi'
    In [327]: d['pi'] = 3.14
    In [328]: d[ (1,2,3) ] = 'a tuple key'

What if you try to use a mutable type?

.. code-block:: ipython

    In [329]: d[ [1,2,3] ] = 'a list key'
       TypeError: unhashable type: 'list'

Actually -- any "hashable" type.

So, technically, it's not mutability, but hashability that matters.

Although for most intents and purposes, you want to use immutable types as keys in dicts.

Hashing
-------

What does "hashable" mean? (https://computersciencewiki.org/index.php/Hashing)

Hash functions convert arbitrarily large data to a small proxy (usually an integer).

They always return the same proxy for the same input.

MD5, SHA, etc, are some well known hash algorithms.

Dictionaries hash the key to an integer proxy and use it to find the key and value.

Key lookup is efficient because the hash function leads directly to a bucket with very few keys (often just one).

What would happen if the proxy (hash) changed after storing a key?

(Answer: you wouldn't be able to find it again!)

Hashability requires immutability.

Key lookup is very efficient:

The access time is constant regardless of the size of the dict.

Dictionary indexing
-------------------

Note: cPython name look-ups are implemented with dicts -- it's highly optimized.

Key to value:

 * lookup is one way.

Value to key:

 * requires visiting the whole dict.

If you need to check dict values often, create another dict or set.

(But note that it's then up to you to keep them in sync).


Dictionary Ordering (not)
-------------------------

Traditionally, dictionaries have had no defined order. See this example from Python 3.5:

.. code-block:: ipython

    In [352]: d = {'one':1, 'two':2, 'three':3}
    In [353]: str(d)
    Out[353]: {'one': 1, 'three': 3, 'two': 2}
    In [354]: d.keys()
    Out[354]: dict_keys(['three', 'two', 'one'])

Note how I defined the dict in a natural order, but when it gets printed, or you display the keys, they are in a different order.

However, In cPython 3.6, the internal implementation was changed, and it *does* happen to preserve order. In cPython 3.6, that is considered an implementation detail -- and you should not count on it! However, as of cPython 3.7, dictionaries preserving order are part of the language specification. This was declared by Guido on the python-dev mailing list on
Dec 15, 2017 <https://mail.python.org/pipermail/python-dev/2017-December/151283.html>.

.. code-block:: ipython

    In Python 3.6, the above code results in:

    In [9]: d = {'one':1, 'two':2, 'three':3}

    In [10]: str(d)
    Out[10]: "{'one': 1, 'two': 2, 'three': 3}"

    In [11]: d.keys()
    Out[11]: dict_keys(['one', 'two', 'three'])


When new items are added to a dict, they go on the "end":

.. code-block:: ipython

    In [12]: d = {}

    In [13]: d['one'] = 1

    In [14]: d['two'] = 2

    In [15]: d['three'] = 3

    In [16]: str(d)
    Out[16]: "{'one': 1, 'two': 2, 'three': 3}"

and ``dict.popitem()`` will remove the "last" item in the dict.

**CAUTION** This is new behavior in cPython 3.6 -- older versions of Python (notably including Python 2) do not preserve order.  In older versions, there is a special version of a dict in the collections module: ``collections.OrderedDict`` which preserves order in all versions of Python, and has a couple extra features.

Also: while Python dicts now *preserve* order, they are not really a fully ordered object: there is no direct way to get, say, the "third" item in a dict, or to inset an item at a particular location.



Dictionary Iterating
--------------------

``for``  iterates over the keys

.. code-block:: ipython

    In [23]: d = {'name': 'Brian', 'score': 42}

    In [24]: for x in d:
        ...:     print(x)
        ...:
    name
    score

dict keys and values
--------------------

.. code-block:: ipython

    In [25]: d = {'name': 'Brian', 'score': 42}

    In [26]: d.keys()
    Out[26]: dict_keys(['name', 'score'])

    In [27]: d.values()
    Out[27]: dict_values(['Brian', 42])

    In [28]: d.items()
    Out[28]: dict_items([('name', 'Brian'), ('score', 42)])

Notice that these are of type ``dict_keys`` and ``dict_values``. These are special types that provide iteration, printing and other features, but are tied to the underlying dict, rather than copies. They are actually Sets (see below), so can be compared to sets, and the ``in`` operator is efficient.

(Python2 would simply create lists of keys and values -- but then you were making a copy when you probably didn't need one). If you do need a copy, or a proper Sequence, simmply wrap them in a ``list()``:

.. code-block:: python

    the_values_as_a_list = list(a_dict.values())


dict keys and values
--------------------

Iterating on everything

.. code-block:: ipython

    In [26]: d = {'name': 'Brian', 'score': 42}

    In [27]: for k, v in d.items():
        print("%s: %s" % (k,v))
       ....:
    name: Brian
    score: 42


Dictionary Performance
-----------------------

  * Indexing is fast and constant time: O(1).

  * ``x in s`` is fast and constant time: O(1).

  * Visiting all items is proportional to n: O(n).

  * Inserting is constant time: O(1).

  * Deleting is constant time: O(1).


 http://wiki.python.org/moin/TimeComplexity


Other dict operations:
----------------------

See them all here:

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

Is it in there?

.. code-block:: ipython

  In [5]: d
  Out[5]: {'that': 7, 'this': 5}

  In [6]: 'that' in d
  Out[6]: True

  In [7]: 'this' not in d
  Out[7]: False

Containment is on the keys.

Think of it like a "real" dictionary, where the keys are the words, and the values are the definitions.

Is the word "gullible" in the dictionary? is asking if the key is in the dict.


Getting something: (like indexing)
----------------------------------

.. code-block:: ipython

  In [9]: d.get('this')
  Out[9]: 5

But you can specify a default:

.. code-block:: ipython

  In [11]: d.get('something', 'a default')
  Out[11]: 'a default'

`get()` never raises an Exception (default is None).


iterating
---------

.. code-block:: ipython

  In [13]: for item in d:
     ....:     print(item)
     ....:
  this
  that

Which is equivalent to, but a bit faster than:

.. code-block:: ipython

  In [15]: for key in d.keys():
      print(key)
     ....:
  this
  that

In fact, there are very few things you can do with the ``dict_keys`` that you can't do directly with the dict.

But to get values, you must specify you want the values:

.. code-block:: ipython

  In [16]: for val in d.values():
      print(val)
     ....:
  5
  7

and to get both, you use ``.items``:

.. code-block:: ipython

  In [4]: for item in d.items():
     ...:     print(item)
     ...:
  ('this', 5)
  ('that', 7)


``pop()``
---------

"Popping": getting the value while removing it.

Pop out a particular key:

.. code-block:: ipython

  In [19]: d.pop('this')
  Out[19]: 5

  In [20]: d
  Out[20]: {'that': 7}

pop out an arbitrary key, value pair

.. code-block:: ipython

  In [23]: d.popitem()
  Out[23]: ('that', 7)

  In [24]: d
  Out[24]: {}

note that it's the last item, so not completely arbitrary.

``setdefault``
--------------

This one is handy:

``setdefault(key[, default])``

gets the value if it's there, sets it to the specified default if it's not. Returns the value in either case.

.. code-block:: ipython

  In [4]: d = {}

  In [5]: d.setdefault('something', 'a value')
  Out[5]: 'a value'

  In [6]: d
  Out[6]: {'something': 'a value'}

The next time you call it, it gets the already set value:

.. code-block:: ipython

  In [7]: d.setdefault('something', 'a different value')
  Out[7]: 'a value'


Assignment
----------

Assignment (with ``=``) is a link to the original dict, just like lists or anything else. Remember that assignment is simply binding a new name to something.

And dicts are mutable -- so be careful!

.. code-block:: ipython

  In [47]: d
  Out[47]: {'something': 'a value'}

  In [48]: item_view = d

  In [49]: d['something else'] = 'another value'

  In [50]: item_view
  Out[50]: {'something': 'a value', 'something else': 'another value'}


If you want a copy, use the explicit copy method to get a copy:

.. code-block:: ipython

  In [51] item_copy = d.copy()

  In [52]: d['another thing'] = 'different value'

  In [53]: d
  Out[53]:
  {'another thing': 'different value',
   'something': 'a value',
   'something else': 'another value'}

  In [54]: item_copy
  Out[54]: {'something': 'a value', 'something else': 'another value'}

or pass any mapping into the dict constructor::

.. code-block:: python

  new_dict = dict(old_dict)



Sets
====

a ``set``  is an unordered collection of distinct values.

Essentially, a ``set`` is a dict with only keys.

https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset

Set Constructors:
-----------------

.. code-block:: ipython

    >>> set()
    set()

    >>> set([1, 2, 3])
    {1, 2, 3}

    >>> {1, 2, 3}
    {1, 2, 3}

    >>> s = set()

    >>> s.update([1, 2, 3])
    >>> s
    {1, 2, 3}


Set Properties
---------------

``Set``  members must be hashable, like dictionary keys -- and for same reason (efficient lookup).

No indexing (unordered).

.. code-block:: ipython

    >>> s[1]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing


Set Methods
-----------

.. code-block:: ipython

    >> s = set([1])
    >>> s.pop() # an arbitrary member
    1
    >>> s.pop()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'pop from an empty set'
    >>> s = set([1, 2, 3])
    >>> s.remove(2)
    >>> s.remove(2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 2


All the "set" operations from math class...

.. code-block:: python

    s.isdisjoint(other)

    s.issubset(other)

    s.union(other, ...)

    s.intersection(other, ...)

    s.difference(other, ...)

    s.symmetric_difference( other, ...)

Set Operators
-------------

All the basic set operations are support with math-class like operators:

Test whether every element in the set is in other::

  set <= other


Test whether the set is a proper subset of other, that is, set <= other and set != other::

  set < other

Test whether every element in other is in the set::

  set >= other

Test whether the set is a proper superset of other, that is, ``set >= other and set != other``::

  set > other

Union: Return a new set with elements from the set and all others::

  set | other | ...

Intersection: Return a new set with elements common to the set and all others::

  set & other & ...

Difference: Return a new set with elements in the set that are not in the others::

  set - other - ...

Symmetric difference: return a new set with elements in either the set or other but not both::

  set ^ other

In fact, it is the operator versions that make the ``set`` object "officially" a Set: (`Set ABC <https://docs.python.org/3.8/library/collections.abc.html?highlight=set%20abc#collections.abc.Set>`_)


Frozen Set
----------

Another kind of set: ``frozenset``

immutable -- for use as a key in a dict (or another set...):

.. code-block:: python

    >>> fs = frozenset((3,8,5))
    >>> fs.add(9)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'frozenset' object has no attribute 'add'

A few added notes:
==================

The count() method
------------------

All Python sequences (including strings) have a ``count()`` method:

.. code-block:: ipython

    In [1]: s = "This is an arbitrary string"

    In [2]: s.count('t')
    Out[2]: 2

What if you want a case-insensitive count?

.. code-block:: ipython

    In [3]: s.lower().count('t')
    Out[3]: 3

set.update()
------------

If you want to add a bunch of stuff to a set, you can use update:

.. code-block:: ipython

    In [1]: s = set()

    In [2]: s.update
    Out[2]: <function set.update>

    In [3]: s.update(['this', 'that'])

    In [4]: s
    Out[4]: {'that', 'this'}

    In [5]: s.update(['this', 'thatthing'])

    In [6]: s
    Out[6]: {'that', 'thatthing', 'this'}

**NOTE:** It's VERY often the case that when you find yourself writing a trivial loop -- there is a way to do it with a built in method!



Sorting stuff in dictionaries:
-------------------------------

dicts aren't sorted, so what if you want to do something in a sorted way?

The "standard" way:

.. code-block:: python

  for key in sorted(d.keys()):
      ...

As dicts DO preserve order, you can make a sorted version of a dict:

.. code-block:: python

  sorted_dict = dict(sorted(dict.items(), key=sort_key))

where sort_key is a function that takes the (key, value) tuple and returns a value to sort on.


Another option:

.. code-block:: python

    collections.OrderedDict

Also other nifty stuff in the ``collections`` module:

https://docs.python.org/3.6/library/collections.html

**NOTE:** As of Python 3.6, dicts do preserve order. But they are not full featured ordered objects. If you want a "properly" ordered object, use ``OrderedDict``.

