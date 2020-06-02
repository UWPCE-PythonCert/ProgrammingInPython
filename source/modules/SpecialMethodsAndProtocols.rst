.. _special_methods:

###########################
Special Methods & Protocols
###########################


Special methods (also called *magic* methods) are the secret sauce to Python's duck typing.

Defining the appropriate special methods in your classes is how you make your class act like the standard classes.


What's in a Name?
-----------------

We've seen at least one special method so far::

    __init__

It's all in the double underscores...

Pronounced "dunder"


try: ``dir(2)``  or ``dir(list)``


Generally Useful Special Methods
--------------------------------

Most classes should at least have these special methods:

``object.__str__``:
  Called by the str() built-in function and by the print function to compute
  the *informal* string representation of an object.

``object.__repr__``:
  Called by the repr() built-in function to compute the *official* string representation of an object.

  Ideally: ``eval( repr(something) ) == something``

  This means that the "repr" is what you type to create the object. In practice, this is impractical for complex objects... but it is still a more "formal" form.

  Note that if you don't define a ``__str__`` method, then the ``__repr__`` will be used. And the base class (``object``) has a ``__repr__`` defined, so every class automatically gets one -- but it's ugly :-)


Protocols
----------

The set of special methods needed to emulate a particular type of Python object is called a *protocol*.

Your classes can "become" like Python built-in classes by implementing the methods in a given protocol.

Remember, these are more *guidelines* than laws.  Implement only what you need.


The Numerics Protocol
---------------------

Do you want your class to behave like a number? Implement these methods:

.. code-block:: python

    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__matmul__(self, other)
    object.__truediv__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)

(or the fraction you actually need).


Operator Overloading
--------------------

Most of the previous examples map to "operators": ``+, - , *, //, /, %`` etc. This is often known as "operator overloading", as you are redefining what the operators mean for that specific type.

Note that you can define these operators to do ANYTHING you want -- but it is a really good idea to only define them to mean something that makes sense in the usual way.

One interesting exception to this rule is the ``pathlib.Path`` class, that has defined ``__truediv__`` to mean path concatenation:

.. code-block:: ipython

    In [19]: import pathlib

    In [20]: p1 = pathlib.Path.cwd()

    In [21]: p1
    Out[21]: PosixPath('/Users/Chris/PythonStuff/UWPCE/PythonCertDevel')

    In [22]: p1 / "a_filename"
    Out[22]: PosixPath('/Users/Chris/PythonStuff/UWPCE/PythonCertDevel/a_filename')

While this is not division in any sense, the slash *is* used as a path separator -- so this does make intuitive sense. At least to me -- I think it's pretty cool.


Comparing
---------

If you want your objects to be comparable::

  A > B
  A < B
  A >= B

etc...

There is a full set of magic methods you can use to override the "comparison operators" ::

    __lt__ : <  (less than)
    __le__ : <= (less than or equal)
    __eq__ : == (equal)
    __ge__ : >= (greater than or equal)
    __gt__ :  > (greater than)
    __ne__ : != (not equal)

These are known as the "rich comparison" operators, as they allow fuller featured comparisons. In particular, they are used by numpy to provide "element-wise" comparison -- that is, comparing two arrays yields an array of results, rather than a single result:

.. code-block:: ipython

    In [26]: import numpy as np

    In [27]: arr1 = np.array([3,4,5,6,7,8,9])

    In [28]: arr2 = np.array([9,2,6,2,6,3,9])

    In [29]: arr1 > arr2
    Out[29]: array([False,  True, False,  True,  True,  True, False], dtype=bool)

    In [30]: arr1 == arr2
    Out[30]: array([False, False, False, False, False, False,  True], dtype=bool)

This is just one example -- the point is that for your particular class, you can define these comparisons however you want.

Total Ordering
--------------

You may notice that those operators are kind of redundant -- if ``A > B is True`` then we know that ``A < B is False`` and ``A <= B is False``.

In fact, there is a mathematical / computer science concept known as "Total Order": (https://en.wikipedia.org/wiki/Total_order), which strictly defines "well behaved" objects in this regard.

There may be some special cases, where these rules may not apply for your classes (though I can't think of any :-) ), but for the most part, you want your classes, if they support comparisons at all, to be well behaved, or "total ordered".

Because this is the common case, Python comes with a nifty utility that implements total ordering for you:

https://docs.python.org/3.6/library/functools.html#functools.total_ordering

It can be found in the functools module, and allows you to specify __eq__ and only one of: ``__lt__()``, ``__le__()``, ``__gt__()``, or ``__ge__()``.  It will then fill in the others for you.

Note: if you define only one, it should be ``__lt__``, because this is the one used for sorting (see below for more about that).

Here is the truncated example from the docs:

.. code-block:: python

    @total_ordering
    class Student:
        def __eq__(self, other):
            return ((self.lastname.lower(), self.firstname.lower()) ==
                    (other.lastname.lower(), other.firstname.lower()))
        def __lt__(self, other):
            return ((self.lastname.lower(), self.firstname.lower()) <
                    (other.lastname.lower(), other.firstname.lower()))

Note that this makes it a lot easier than implementing all six comparison operators. However, if you read the doc, it lets you know that ``total_ordering`` has poor performance -- it is doing extra method call re-direction when the operators are used. If performance matters to your use case (and it probably doesn't), you need to write all six comparison dunders.

Sorting
-------

Python has a handful of sorting methods built in:

``list.sort()`` -- for sorting a list in place.
``sorted(iterable)`` -- for creating a sorted copy of an iterable (sequence).

And a couple of more obscure ones.

In order for your custom objects to be sortable, they need the ``__lt__`` (less than) magic method defined -- that's about it.

So if you are using the ``total_ordering`` decorator, it's best to define ``__eq__`` and ``__lt__`` -- that way sorting will be able to use a "native" method for sorting, and maybe get better performance.

Sort key methods
----------------

By default, the sorting methods use ``__lt__`` for comparison, and that algorithm calls ``__lt__`` O(n log(n)) times. But if you pass a "key" function in to the sort call:

``a_list.sort(key=key_fun)``

then the key_fun is only called n times, and if the key returns a simple type, like an integer or float, then the sorting will be faster.

So it often helps to provide a sort_key() method on your class, so it can be passed in to the sort methods:

.. code-block:: python

    class Simple:
        """
        simple class to demonstrate a simple sorting key method
        """

        def __init__(self, val):
            self.val = val

        def sort_key(self):
            return self.val

And to use it:

.. code-block:: python

    list_of_Simple_objects.sort(key=Simple.sort_key)

See: :download:`sort_key.py <../examples/sort_key.py>` for a complete example with timing. Here is an example of running it::

    Timing for 10000 items
    regular sort took: 0.04288s
    key sort took: 0.004779s
    performance improvement factor: 8.9726

So almost 9 times faster for a 10,000 item list. Pretty good, eh?

An Example
----------

Each of these methods supports a common Python operation.

For example, to make '+' work with a sequence type in a vector-like fashion,
implement ``__add__``:

.. code-block:: python

    def __add__(self, v):
        """return the element-wise vector sum of self and v
        """
        assert len(self) == len(v)
        return vector([x1 + x2 for x1, x2 in zip(self, v)])


[a slightly more complete example may be seen here :download:`vector.py <../examples/object_oriented/vector.py>`]

Emulating Standard types
=========================

Making your classes behave like the built-ins.


The Container Protocol
----------------------

Want to make a container type? Here's what you need:

.. code-block:: python

    object.__len__(self)
    object.__getitem__(self, key)
    object.__setitem__(self, key, value)
    object.__delitem__(self, key)
    object.__iter__(self)
    object.__reversed__(self)
    object.__contains__(self, item)

    object.__index__(self)

``__len__`` is called when len(object) is called.

``__reversed__`` is called when reversed(object) is called.

``__contains__`` is called with ``in`` is used: ``something in object``

``__iter__`` is used for iteration -- called when in a for loop.

``__index__`` is used to convert the object into an integer for indexing. So you don't define this in a container type but rather define it for a type so it can be used as an index.  If you have a class that could reasonably be interpreted as an index, you should define this. It should return an integer.  This was added to support multiple integer types for numpy.


Indexing and Slicing
--------------------

``__getitem__`` and ``set__item__`` are used when indexing:

``x = object[i]`` calls ``__getitem__``, and ``object[i] = something`` calls ``__setitem__``.

But indexing is pretty complex in python. There is simple indexing: ``object[i]``, but there is also slicing: ``object[i:j:skip]``

When you implement ``__getitem__(self, index)``, ``index`` will simply be the index if it's a simple index, but if it's slicing, it will be a ``slice`` object. Python also supports multiple slices:

``object[a:b,c:d]``

These are used in numpy to support multi-dimensional arrays, for instance.

In this case, a tuple of slice objects is passed in.

See: :download:`index_slicing.py<../examples/object_oriented/index_slicing.py>`

Callable classes
-----------------

We've been using functions a lot:

.. code-block:: python

    def my_fun(something):
        do_something
        ...
        return something

And then we can call it:

.. code-block:: python

    result = my_fun(some_arguments)


But what if we need to store some data to know how to evaluate that function?

Example: a function that computes a quadratic function:

.. math::

    y = a x^2 + bx + c

You could pass in a, b and c each time:

.. code-block:: python

    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

But what if you are using the same a, b, and c numerous times?

Or what if you need to pass this in to something
(like map) that requires a function that takes a single argument?

"Callables"
-----------

Various places in Python expect a "callable" -- something that you can
call like a function:

.. code-block:: python

    a_result = something(some_arguments)

"Something" in this case is often a function, but can be anything else
that is "callable".

What have we been introduced to recently that is "callable", but not a
function object?

Custom callable objects
------------------------

The trick is one of Python's "magic methods"

.. code-block:: python

    __call__(*args, **kwargs)

If you define a ``__call__`` method in your class, it will be used when
code "calls" an instance of your class:

.. code-block:: python

    class Callable:
        def __init__(self, .....)
            some_initilization
        def __call__(self, some_parameters)

Then you can do:

.. code-block:: python

    callable_instance = Callable(some_arguments)

    result = callable_instance(some_arguments)


Callable example
----------------

An example of writing a callable class:

Write a class for a quadratic equation.

* The initializer for that class should take the parameters: ``a, b, c``

* It should store those parameters as attributes.

* The resulting instance should evaluate the function when called, and return the result:


.. code-block:: python

    my_quad = Quadratic(a=2, b=3, c=1)

    my_quad(0)

Here's one way to do that:
:download:`quadratic.py <../solutions/quadratic/quadratic.py>`

Protocols in Summary
--------------------

Use special methods when you want your class to act like a "standard" type or class in some way.

Look up the special methods you need and define them (and only the ones you need).

There's more to read about the details of implementing these methods:

* https://docs.python.org/3.6/reference/datamodel.html#special-method-names


References
----------

Here is a good reference for magic methods:

http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods

And with a bit more explanation:

https://www.python-course.eu/python3_magic_methods.php

