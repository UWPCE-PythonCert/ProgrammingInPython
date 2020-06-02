.. _a_bit_on_mutability:


=====================================
A bit more on mutability (and copies)
=====================================

mutable objects
----------------

We've talked about this: mutable objects can have their contents changed in place.

Immutable objects can not.

This has implications when you have a container with mutable objects in it:

.. code-block:: ipython

    In [28]: list1 = [ [1,2,3], ['a','b'] ]

one way to make a copy of a list:

.. code-block:: ipython

    In [29]: list2 = list1[:]

    In [30]: list2 is list1
    Out[30]: False

they are different lists.


What if we set an element to a new value?

.. code-block:: ipython

    In [31]: list1[0] = [5,6,7]

    In [32]: list1
    Out[32]: [[5, 6, 7], ['a', 'b']]

    In [33]: list2
    Out[33]: [[1, 2, 3], ['a', 'b']]

So they are independent.


But what if we mutate an element?

.. code-block:: ipython

    In [34]: list1[1].append('c')

    In [35]: list1
    Out[35]: [[5, 6, 7], ['a', 'b', 'c']]

    In [36]: list2
    Out[36]: [[1, 2, 3], ['a', 'b', 'c']]

uuh oh! mutating an element in one list mutated the one in the other list.


Why is that?

.. code-block:: ipython

    In [38]: list1[1] is list2[1]
    Out[38]: True

The elements are the same object!

This is known as a "shallow" copy -- Python doesn't want to copy more than it needs to, so in this case, it makes a new list, but does not make copies of the contents.

Same for dicts (and any container type -- even tuples!)

If the elements are immutable, it doesn't really make a differnce -- but be very careful with mutable elements.


The copy module
----------------

most objects have a way to make copies (``dict.copy()`` for instance).

but if not, you can use the ``copy`` module to make a copy:

.. code-block:: ipython

    In [39]: import copy

    In [40]: list3 = copy.copy(list2)

    In [41]: list3
    Out[41]: [[1, 2, 3], ['a', 'b', 'c']]

This is also a shallow copy.


But there is another option:

.. code-block:: ipython

    In [3]: list1
    Out[3]: [[1, 2, 3], ['a', 'b', 'c']]

    In [4]: list2 = copy.deepcopy(list1)

    In [5]: list1[0].append(4)

    In [6]: list1
    Out[6]: [[1, 2, 3, 4], ['a', 'b', 'c']]

    In [7]: list2
    Out[7]: [[1, 2, 3], ['a', 'b', 'c']]

``deepcopy`` recurses through the object, making copies of everything as it goes.



I happened on this thread on stack overflow:

http://stackoverflow.com/questions/3975376/understanding-dict-copy-shallow-or-deep

The OP is pretty confused -- can you sort it out?

Make sure you understand the difference between a reference, a shallow copy, and a deep copy.

Mutables as default arguments:
------------------------------

Another "gotcha" is using mutables as default arguments:

.. code-block:: ipython

    In [11]: def fun(x, a=[]):
       ....:     a.append(x)
       ....:     print(a)
       ....:

This makes sense: maybe you'd pass in a specific list, but if not, the default is an empty list.

But:

.. code-block:: ipython

    In [12]: fun(3)
    [3]

    In [13]: fun(4)
    [3, 4]

Huh?!


Remember that that default argument is defined when the function is created: there will be only one list, and every time the function is called, that same list is used.


**The solution:**

The standard practice for such a mutable default argument:

.. code-block:: ipython

    In [15]: def fun(x, a=None):
       ....:     if a is None:
       ....:         a = []
       ....:     a.append(x)
       ....:     print(a)
    In [16]: fun(3)
    [3]
    In [17]: fun(4)
    [4]

You get a new list every time the function is called

For more reading.

This: http://python.net/crew/mwh/hacks/objectthink.html#question

Is a link to a discussion on comp.lang.python from over 15 years ago -- but the issues are still the same. In particular, Alex Martelli's answer is brilliant.

Go read it....

