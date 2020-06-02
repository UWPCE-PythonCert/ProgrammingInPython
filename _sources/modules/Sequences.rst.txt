:orphan:

.. _sequences:

################
Python Sequences
################


Ordered collections of objects


What is a Sequence?
===================

A sequence is an ordered collection of objects.

They are analogous to what are often called "arrays" or "lists" in other programming languages.

But in Python, there are number of types that all fit this description, each with special customization. But any object that has the behavior expected of a sequence can be treated the same way in Python:

Remember Duck Typing?

If it looks like a duck and quacks like a duck...

OR: If it looks and acts like a sequence -- it **is** a sequence.

Technically, if it satisfies the "Sequence Protocol", it is a sequence.

Python is all about these protocols -- we will see more of them.

The Sequence Protocol
---------------------

A *sequence* can be considered as anything that supports *at least* these operations:

* Indexing
* Slicing
* Membership
* Concatenation
* Length
* Iteration

I'll get into all of those as we go along.

Sequence Types
--------------

There are eight built in types in Python that are *sequences*:

* string
* list
* tuple
* bytes
* bytearray
* buffer
* array.array
* range object (almost)

For this lesson, you won't see much beyond strings, lists, and tuples --
the rest are pretty special purpose.

But what we learn in this lesson applies to all sequences (with minor caveats).

I'll use lists, strings and tuples in the examples.

So let's take a look at the key parts of the sequence protocol:

Indexing
========

Items in a sequence may be looked up by *index* using the indexing
operator: ``[]``

Indexing in Python always starts at zero.

Here is an example with a string -- a string is a sequence of characters.

.. code-block:: ipython

    In [98]: s = "this is a string"
    In [99]: s[0]
    Out[99]: 't'
    In [100]: s[5]
    Out[100]: 'i'

Note that the first character is indexed with zero -- I sometimes call that the "zeroth" item in the sequence.

Zero indexing may seem odd at first (if you are not already a programming geek), but it turns out to make a lot of things easier. More on that later.

You can use negative indexes to count from the end:

.. code-block:: ipython

    In [2]: a_list = [34, 56, 19, 23, 55]

    In [3]: a_list[-1]
    Out[3]: 55

    In [4]: a_list[-2]
    Out[4]: 23

    In [5]: a_list[-4]
    Out[5]: 56


Indexing beyond the end of a sequence causes an IndexError:

.. code-block:: ipython

    In [6]: a_list
    Out[6]: [34, 56, 19, 23, 55]

    In [7]: a_list[5]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-7-c1f9ac3b6fee> in <module>()
    ----> 1 a_list[5]

    IndexError: list index out of range

Pretty straight forward so far...

Slicing
-------

Slicing is a real "power tool" of Python -- it can allow very short code.

Slicing a sequence creates a new sequence with a range of objects from the
original sequence.

It also uses the indexing operator (``[]``), but with a twist.

``sequence[start:finish]`` returns all `sequence[i]` for which `start <= i < finish`

That's a fancy way to say that it's all the items from start to finish -- including start, but NOT including finish.

This also may be a bit unintuitive -- but it's very practical.

.. code-block:: ipython

    In [121]: s = "a bunch of words"
    In [122]: s[2]
    Out[122]: 'b'
    In [123]: s[6]
    Out[123]: 'h'
    In [124]: s[2:6]
    Out[124]: 'bunc'
    In [125]: s[2:7]
    Out[125]: 'bunch'

Helpful Hint
------------

It can really help if you think about slicing this way:

(write this out!)

Think of the indexes as pointing to the spaces between the items::

       a       b   u   n   c   h       o   f       w   o   r   d   s
     |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15

Slicing
-------

Python has some other slicing shortcuts...

You do not have to provide both ``start`` and ``finish``:

.. code-block:: ipython

    In [6]: s = "a bunch of words"
    In [7]: s[:5]
    Out[7]: 'a bun'
    In [8]: s[5:]
    Out[8]: 'ch of words'

Either ``0`` or ``len(s)`` will be assumed, respectively.

You can combine this with the negative index to get the end of a sequence:

.. code-block:: ipython

    In [4]: s = 'this_could_be_a_filename.txt'
    In [5]: s[:-4]
    Out[5]: 'this_could_be_a_filename'
    In [6]: s[-4:]
    Out[6]: '.txt'

**That** is a real-world example I use all the time.

Why start from zero?
--------------------

Python indexing feels 'weird' to some folks -- particularly those that don't come with a background in the C family of languages.

Why is the "first" item indexed with **zero**?

Why is the last item in the slice **not** included?

*Because* these lead to some nifty properties::

    len(seq[a:b]) == b-a

    seq[:b] + seq[b:] == seq

    len(seq[:b]) == b

    len(seq[-b:]) == b

There are very many fewer "off by one" errors as a result.

More on Slicing
---------------

Slicing takes a third argument: ``step`` which controls which items are
returned:

.. code-block:: ipython

    In [18]: a_tuple
    Out[18]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

    In [19]: a_tuple[0:15]
    Out[19]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    In [20]: a_tuple[0:15:2]
    Out[20]: (0, 2, 4, 6, 8, 10, 12, 14)

    In [21]: a_tuple[0:15:3]
    Out[21]: (0, 3, 6, 9, 12)

    In [22]: a_tuple[::-1]
    Out[22]: (19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

Very cool -- a negative step reverses the results!

Slicing vs. Indexing
--------------------

Though they share an operator, slicing and indexing have a few important
differences:

* Indexing will always return one single object (a scalar), whereas slicing will return a sequence of objects.

So if you start with, say, a list of numbers, indexing will return a single number.  Slicing, on the other hand, will return list of numbers -- even if that list only has one number in it -- or zero!

Note that strings are a bit of an exception -- there is no character type in Python -- so a single character is a string -- a sequence of length-1.

* Indexing past the end of a sequence will raise an error, slicing will not:

.. code-block:: ipython

    In [129]: s = "a bunch of words"
    In [130]: s[17]
    ----> 1 s[17]
    IndexError: string index out of range
    In [131]: s[10:20]
    Out[131]: ' words'
    In [132]: s[20:30]
    Out[132]: ''

(try it yourself....)

Membership
==========

All sequences support the ``in`` and ``not in`` membership operators:

.. code-block:: ipython

    In [15]: s = [1, 2, 3, 4, 5, 6]
    In [16]: 5 in s
    Out[16]: True
    In [17]: 42 in s
    Out[17]: False
    In [18]: 42 not in s
    Out[18]: True


For strings, the membership operations are like ``substring`` operations in
other languages:

.. code-block:: ipython

    In [20]: s = "This is a long string"
    In [21]: "long" in s
    Out[21]: True

This does not work for sub-sequences of other types (can you think of why?):

.. code-block:: ipython

    In [22]: s = [1, 2, 3, 4]
    In [23]: [2, 3] in s
    Out[23]: False


Concatenation
=============

Using ``+`` or ``*`` on sequences will *concatenate* them:

.. code-block:: ipython

    In [18]: l1 = [1,2,3,4]
    In [19]: l2 = [5,6,7,8]
    In [20]: l1 + l2
    Out[20]: [1, 2, 3, 4, 5, 6, 7, 8]
    In [21]: (l1+l2) * 2
    Out[21]: [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]

Multiplying and Slicing
-----------------------

You can apply this concatenation to slices as well, leading to some nicely
concise code:

from CodingBat: Warmup-1 -- front3

.. code-block:: python

    def front3(str):
      if len(str) < 3:
        return str+str+str
      else:
        return str[:3]+str[:3]+str[:3]

This non-pythonic solution can also be expressed like so:

.. code-block:: python

    def front3(str):
        return str[:3] * 3

Length
======

All sequences have a length.  You can get it with the ``len`` builtin:

.. code-block:: ipython

    In [36]: s = "how long is this, anyway?"
    In [37]: len(s)
    Out[37]: 25

Remember: Sequences are 0-indexed, so the last index is ``len(s)-1``:

.. code-block:: ipython

    In [38]: count = len(s)
    In [39]: s[count]
    ------------------------------------------------------------
    IndexError                Traceback (most recent call last)
    <ipython-input-39-5a33b9d3e525> in <module>()
    ----> 1 s[count]
    IndexError: string index out of range

Better to use ``s[-1]``


Miscellaneous
=============

There are a bunch more operations supported by most sequences.
Min and Max
-----------

All sequences also support the ``min`` and ``max`` builtins:

.. code-block:: ipython

    In [42]: all_letters = "thequickbrownfoxjumpedoverthelazydog"

    In [43]: min(all_letters)
    Out[43]: 'a'

    In [44]: max(all_letters)
    Out[44]: 'z'

Why are those the answers you get? (hint: ``ord('a')``)

Of course this works with numbers, too!

.. code-block:: ipython

    In [1]: seq = [4,2,8,3,5,8,5,7]

    In [2]: min(seq)
    Out[2]: 2

    In [3]: max(seq)
    Out[3]: 8


Index
-----

All sequences also support the ``index`` method, which returns the index of the first occurrence of an item in the sequence:

.. code-block:: ipython

    In [46]: all_letters.index('d')
    Out[46]: 21

This causes a ``ValueError`` if the item is not in the sequence:

.. code-block:: ipython

    In [47]: all_letters.index('A')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-47-2db728a46f78> in <module>()
    ----> 1 all_letters.index('A')

    ValueError: substring not found

Count
-----

A sequence can also be queried for the number of times a particular item
appears:

.. code-block:: ipython

    In [52]: all_letters.count('o')
    Out[52]: 4
    In [53]: all_letters.count('the')
    Out[53]: 2

This does not raise an error if the item you seek is not present:

.. code-block:: ipython

    In [54]: all_letters.count('A')
    Out[54]: 0


Iteration
=========

All sequences are "iterables".

You can iterate over a sequence with ``for``:

.. code-block:: python

    for element in sequence:
        do_something(element)

Which is what we mean when we say a sequence is an "iterable".

There are some complexities about that -- but more on that in another lesson.


Lists, Tuples...
================


The *primary* sequence types.

Lists
-----

Lists can be constructed using list literals (``[]``):

.. code-block:: ipython

    In [1]: []
    Out[1]: []
    In [2]: [1,2,3]
    Out[2]: [1, 2, 3]
    In [3]: [1, 'a', 7.34]
    Out[3]: [1, 'a', 7.34]

Or by using the ``list`` type object as a constructor:

.. code-block:: ipython

    In [6]: list()
    Out[6]: []
    In [7]: list(range(4))
    Out[7]: [0, 1, 2, 3]
    In [8]: list('abc')
    Out[8]: ['a', 'b', 'c']

It will take any "iterable" (which means any sequence automatically -- remember that all sequences are iterable?)

List Elements
-------------

The elements contained in a list need not be of a single type.

Lists are *heterogenous*, *ordered* collections.

Each element in a list is a value, and can be in multiple lists and have
multiple names (or no name):

.. code-block:: ipython

    In [9]: name = 'Brian'
    In [10]: a = [1, 2, name]
    In [11]: b = [3, 4, name]
    In [12]: a[2]
    Out[12]: 'Brian'
    In [13]: b[2]
    Out[13]: 'Brian'
    In [14]: a[2] is b[2]
    Out[14]: True

Notice that even with a "literal" -- the elements don't need to be literals as well -- they can be names.

They can even be function calls:

.. code-block:: ipython

    In [4]: def fun(n):
       ...:     return n * 2
       ...:

    In [5]: l = [3, 'four', fun(3), fun(9)]

    In [6]: l
    Out[6]: [3, 'four', 6, 18]


Tuples
------

Tuples can be constructed using tuple literals (``()``):

.. code-block:: ipython

    In [15]: ()
    Out[15]: ()
    In [16]: (1, 2)
    Out[16]: (1, 2)
    In [17]: (1, 'a', 7.65)
    Out[17]: (1, 'a', 7.65)
    In [18]: (1,)
    Out[18]: (1,)

Tuples and Commas...
--------------------

Tuples don't NEED parentheses...

.. code-block:: ipython

    In [161]: t = (1,2,3)
    In [162]: t
    Out[162]: (1, 2, 3)
    In [163]: t = 1,2,3
    In [164]: t
    Out[164]: (1, 2, 3)
    In [165]: type(t)
    Out[165]: tuple


But they *do* need commas...!

.. code-block:: ipython

    In [156]: t = ( 3 )
    In [157]: type(t)
    Out[157]: int
    In [158]: t = ( 3, )
    In [160]: type(t)
    Out[160]: tuple

This is a Python "gotcha" -- some folks on my team recently had a weird bug that two of them could not figure out. They were getting a type error -- something like:

TypeError: unsupported operand type(s) for /: 'tuple' and 'float'

which made no sense -- there were no tuples involved -- in this case, the value was being pulled from a list -- and it WAS a float. They even put type checking code in there, and it was, indeed, a float.

After poking at the code a bit, I suddenly spotted an extra comma -- BINGO! that was it.

The code was more involved, and thus harder to see, but it was pretty much like this:

.. code-block:: python

    In [16]: l = [3, 4, 5, 6]

    In [17]: x = l[3],

then a bit further down, x was used:

.. code-block:: python

    In [18]: y = x / 2.0
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-18-5289811a13ac> in <module>()
    ----> 1 y = x / 2.0

    TypeError: unsupported operand type(s) for /: 'tuple' and 'float'

Would you have seen that?

Converting something to a Tuple
-------------------------------

You can also use the ``tuple`` type object to convert any iterable (sequence) into a tuple:

.. code-block:: ipython

    In [20]: tuple()
    Out[20]: ()
    In [21]: tuple(range(4))
    Out[21]: (0, 1, 2, 3)
    In [22]: tuple('garbanzo')
    Out[22]: ('g', 'a', 'r', 'b', 'a', 'n', 'z', 'o')


Tuple Elements
--------------

The elements contained in a tuple need not be of a single type.

Tuples are *heterogenous*, *ordered* collections.

Each element in a tuple is a value, and can be in multiple tuples and have
multiple names (or no name):

.. code-block:: ipython

    In [23]: name = 'Brian'
    In [24]: other = name
    In [25]: a = (1, 2, name)
    In [26]: b = (3, 4, other)
    In [27]: for i in range(3):
       ....:     print(a[i] is b[i], end=' ')
       ....:
    False False True

Look familiar from lists??

Lists vs. Tuples
----------------


    So why have both?

Mutability
==========

.. image:: /_static/transmogrifier.jpg
   :align: center
   :width: 35%
   :alt: Presto change-o


image from flickr by `illuminaut`_, (CC by-nc-sa)

.. _illuminaut: https://www.flickr.com/photos/illuminaut/3595530403


Mutability in Python
====================

All objects in Python fall into one of two camps:

* Mutable
* Immutable

Objects which are mutable may be *changed in place*.

Objects which are immutable may not be changed.

Ever.

The Types We Know
-----------------

========= ===========
Immutable Mutable
========= ===========
String    List
Integer   Dictionary
Float
Tuple
========= ===========

This may make it look like the Mutables are rare -- but in fact, most "container types", and most custom objects are mutable.

Immutable types are the exception

Lists Are Mutable
-----------------

Try this out:

.. code-block:: ipython

    In [28]: food = ['spam', 'eggs', 'ham']
    In [29]: food
    Out[29]: ['spam', 'eggs', 'ham']
    In [30]: food[1] = 'raspberries'
    In [31]: food
    Out[31]: ['spam', 'raspberries', 'ham']



We repeat the exercise with a Tuple:

.. code-block:: ipython

    In [32]: food = ('spam', 'eggs', 'ham')
    In [33]: food
    Out[33]: ('spam', 'eggs', 'ham')
    In [34]: food[1] = 'raspberries'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-34-0c3401794933> in <module>()
    ----> 1 food[1] = 'raspberries'

    TypeError: 'tuple' object does not support item assignment


Watch Out when name binding
---------------------------

This property means you need to be aware of what you are doing with your lists:

.. code-block:: ipython

    In [36]: original = [1, 2, 3]
    In [37]: altered = original
    In [38]: for i in range(len(original)):
       ....:     if True:
       ....:         altered[i] += 1
       ....:

Perhaps we want to check to see if altered has been updated, as a flag for
whatever condition caused it to be updated.

What is the result of this code?

Perhaps Not What You Expect
---------------------------

Our ``altered`` list has been updated as we'd expect:

.. code-block:: ipython

    In [39]: altered
    Out[39]: [2, 3, 4]

But so has the ``original`` list:

.. code-block:: ipython

    In [40]: original
    Out[40]: [2, 3, 4]

Why?

Let's look at that code again.

What does the line: ``altered = original`` do?

It binds the name: "altered" to the same object that "original" is bound to.

That is, there is only one list, even though it is referred to by two names. So when you mutate (or change) that list from *either* name, the changes show up when you refer to it by the other name.

Other Gotchas
-------------

Easy container setup, or deadly trap?

(note: you can nest lists to make a 2D-ish array)

.. code-block:: ipython

    In [13]: bins = [ [] ] * 5

    In [14]: bins
    Out[14]: [[], [], [], [], []]

    In [15]: words = ['one', 'three', 'rough', 'sad', 'goof']

    In [16]: for word in words:
       ....:     bins[len(word)-1].append(word)
       ....:

So, what is going to be in ``bins`` now?

There is only **One** bin
-------------------------

.. code-block:: ipython

    In [65]: bins
    Out[65]:
    [['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof']]

We multiplied a sequence containing a single *mutable* object.

We got a list containing five references to a single *mutable* object.


Mutable Default Argument
------------------------

Watch out especially for passing mutable objects as default values for function parameters:

.. code-block:: ipython

    In [71]: def accumulator(count, ac_list=[]):
       ....:     for i in range(count):
       ....:         ac_list.append(i)
       ....:     return ac_list
       ....:
    In [72]: accumulator(5)
    Out[72]: [0, 1, 2, 3, 4]
    In [73]: accumulator(7)
    Out[73]: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6]

What is going on here???

It turns out that that code: ``ac_list=[]`` is evaluated *when the function is defined* -- **not** when the function is called.

So the name "ac_list" in the local scope of that function always refers to the same list. So every time the function is called, more is added to that same list.

The moral of the story here is:

**Do not use mutable objects for default arguments!**

It turns out that this early evaluation can be useful -- but for now, just remember not to use mutables as default arguments.

By the way --this is how you *should* write that code:

.. code-block:: ipython

    In [21]: def accumulator(count, ac_list=None):
        ...:     if ac_list is None:
        ...:         ac_list = []
        ...:     for i in range(count):
        ...:         ac_list.append(i)
        ...:     return ac_list

    In [22]: accumulator(5)
    Out[22]: [0, 1, 2, 3, 4]

    In [23]: accumulator(7)
    Out[23]: [0, 1, 2, 3, 4, 5, 6]

This will ensure that a new list will be created if one is not passed-in.


Mutable Sequence Methods
========================

In addition to all the methods supported by sequences we've seen above, mutable sequences (the List), have a number of other methods that are used to change it in place.

You can find all these in the Standard Library Documentation:

https://docs.python.org/3/library/stdtypes.html#typesseq-mutable

Assignment
-----------

You've already seen changing a single element of a list by assignment.

Pretty much the same as "arrays" in most languages:

.. code-block:: ipython

    In [100]: my_list = [1, 2, 3]
    In [101]: my_list[2] = 10
    In [102]: my_list
    Out[102]: [1, 2, 10]


Growing the List
----------------

``.append()``, ``.insert()``, ``.extend()``

.. code-block:: ipython

    In [74]: food = ['spam', 'eggs', 'ham']
    In [75]: food.append('sushi')
    In [76]: food
    Out[76]: ['spam', 'eggs', 'ham', 'sushi']
    In [77]: food.insert(0, 'beans')
    In [78]: food
    Out[78]: ['beans', 'spam', 'eggs', 'ham', 'sushi']
    In [79]: food.extend(['bread', 'water'])
    In [80]: food
    Out[80]: ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']


More on Extend
--------------

You can pass any sequence to ``.extend()``:

.. code-block:: ipython

    In [85]: food
    Out[85]: ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']
    In [86]: food.extend('spaghetti')
    In [87]: food
    Out[87]:
    ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water',
     's', 'p', 'a', 'g', 'h', 'e', 't', 't', 'i']

So be careful -- a string is a single object --but also a sequence of characters.


Shrinking the List
------------------

``.pop()``, ``.remove()``

.. code-block:: ipython

    In [203]: food = ['spam', 'eggs', 'ham', 'toast']
    In [204]: food.pop()
    Out[204]: 'toast'
    In [205]: food.pop(0)
    Out[205]: 'spam'
    In [206]: food
    Out[206]: ['eggs', 'ham']
    In [207]: food.remove('ham')
    In [208]: food
    Out[208]: ['eggs']


You can also delete *slices* of a list with the ``del`` keyword:

.. code-block:: ipython

    In [92]: nums = range(10)
    In [93]: nums
    Out[93]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [94]: del nums[1:6:2]
    In [95]: nums
    Out[95]: [0, 2, 4, 6, 7, 8, 9]
    In [96]: del nums[-3:]
    In [97]: nums
    Out[97]: [0, 2, 4, 6]


Copying Lists
-------------

You can make copies of part of a list using *slicing*:

.. code-block:: ipython

    In [227]: food = ['spam', 'eggs', 'ham', 'sushi']
    In [228]: some_food = food[1:3]
    In [229]: some_food[1] = 'bacon'
    In [230]: food
    Out[230]: ['spam', 'eggs', 'ham', 'sushi']
    In [231]: some_food
    Out[231]: ['eggs', 'bacon']

If you provide *no* arguments to the slice, it makes a copy of the entire list:

.. code-block:: ipython

    In [232]: food
    Out[232]: ['spam', 'eggs', 'ham', 'sushi']
    In [233]: food2 = food[:]
    In [234]: food is food2
    Out[234]: False


Shallow Copies
--------------

The copy of a list made this way is a *shallow copy*.

The list is itself a new object, but the objects it contains are not.

*Mutable* objects in the list can be mutated in both copies:

.. code-block:: ipython

    In [249]: food = ['spam', ['eggs', 'ham']]
    In [251]: food_copy = food[:]
    In [252]: food[1].pop()
    Out[252]: 'ham'
    In [253]: food
    Out[253]: ['spam', ['eggs']]
    In [256]: food.pop(0)
    Out[256]: 'spam'
    In [257]: food
    Out[257]: [['eggs']]
    In [258]: food_copy
    Out[258]: ['spam', ['eggs']]


Copies can solve problems
-------------------------

Consider this common pattern:

.. code-block:: python

    for x in somelist:
        if should_be_removed(x):
            somelist.remove(x)

This looks benign enough, but changing a list while you are iterating over it can be the cause of some pernicious bugs.

The Problem
-----------

For example:

.. code-block:: ipython

    In [27]: l = list(range(10))
    In [28]: l
    Out[28]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [29]: for item in l:
       ....:     l.remove(item)
       ....:
    In [30]: l
    Out[30]: [1, 3, 5, 7, 9]

Was that what you expected?

The Solution
------------

Iterate over a copy, and mutate the original:

.. code-block:: ipython

    In [33]: l = list(range(10))

    In [34]: for item in l[:]:
       ....:     l.remove(item)
       ....:
    In [35]: l
    Out[35]: []


Miscellaneous List Methods
==========================

These methods change a list in place and are not available on immutable sequence types.

``.reverse()``

.. code-block:: ipython

    In [129]: food = ['spam', 'eggs', 'ham']
    In [130]: food.reverse()
    In [131]: food
    Out[131]: ['ham', 'eggs', 'spam']

``.sort()``

.. code-block:: ipython

    In [132]: food.sort()
    In [133]: food
    Out[133]: ['eggs', 'ham', 'spam']

Because these methods mutate the list in place, they have a return value of ``None``


Custom Sorting
--------------

``.sort()`` can take an optional ``key`` parameter.

It should be a function that takes one parameter (list items one at a time) and returns something that can be used for sorting:

.. code-block:: ipython

    In [137]: def third_letter(string):
       .....:     return string[2]
       .....:
    In [138]: food.sort(key=third_letter)
    In [139]: food
    Out[139]: ['spam', 'eggs', 'ham']

You end up with the list sorted by the third letter in each element.

List Performance
----------------

* indexing is fast and constant time: O(1)
* ``x in l`` is proportional to n: O(n)
* visiting all is proportional to n: O(n)
* operating on the end of list is fast and constant time: O(1)

  * append(), pop()

* operating on the front (or middle) of the list depends on n: O(n)

  * ``pop(0)``, ``insert(0, v)``
  * But, reversing is fast. ``Also, collections.deque``

What the heck does this O() thing mean?  That is known as "big O" notation for time complexity.  What it does is provide an indication of how much more time an operation will take depending on how many items the operation is acting on.

Check out the Python wiki entry on Time Complexity for more info:

http://wiki.python.org/moin/TimeComplexity


Choosing Lists or Tuples
========================

Here are a few guidelines on when to choose a list or a tuple:

* If it needs to be mutable: list

* If it needs to be immutable: tuple

  * provides safety when passing to a function (and as a key in a dict)

Otherwise ... taste and convention.


Convention
----------

Lists are homogeneous collections:
-- they alway contain values of the same type
-- they simplify iterating, sorting, etc

Tuples are mixed types:
-- they group multiple values into one logical thing
-- they are similar to simple C structs.


Other Considerations
--------------------

* Do you need to do the same operation to each element?

  * list

* Is there a small collection of values which make a single logical item?

  * tuple

* Do you want to document that these values won't change?

  * tuple

* Do you want to build it iteratively?

  * list

* Do you need to transform, filter, etc?

  * list


More Documentation
------------------

For more information, read the list docs:

https://docs.python.org/3.6/library/stdtypes.html#mutable-sequence-types

(actually any mutable sequence....)

