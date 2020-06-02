.. _python_classes:

##############
Python Classes
##############

"Classes" are the core of Object Oriented Programming.

They provide the tools for encapsulation (keeping the data with the functions) and subclassing and polymorphism.


How are classes made in Python?
===============================

The ``class`` statement
-----------------------

The ``class``  statement creates a new type object:

.. code-block:: ipython

    In [4]: class C:
        pass
       ...:
    In [5]: type(C)
    Out[5]: type

A class is a type -- interesting!

It is created when the statement is run -- much like ``def``.

So we now have a new type, or class -- it doesn't have any actual functionality, though by default all classes "inherit" from ``object``. In doing so they get some minimal functionality from that:

.. code-block:: ipython

    In [3]: issubclass(C, object)
    Out[3]: True

We can print it:

.. code-block:: ipython

    In [4]: print(C)
    <class '__main__.C'>

And look at all the methods it has!

.. code-block:: ipython

    In [5]: dir(C)
    Out[5]:
    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__']

Most of those don't do anything -- but they are there, so every class is guaranteed to have all the "stuff" Python expects objects to have.

In order for the class to do anything useful, it needs to be given attributes and methods.


A simple ``class``
------------------

About the simplest class you can write that is still useful:

.. code-block:: python

    >>> class Point:
    ...     x = 1
    ...     y = 2
    >>> Point
    <class __main__.Point at 0x2bf928>
    >>> Point.x
    1
    >>> p = Point()
    >>> p
    <__main__.Point instance at 0x2de918>
    >>> p.x
    1

This looks a lot like a "struct" in C -- Python doesn't have structures, so yes, a class with no methods (functions) is essentially a struct.

Basic Structure of a class
--------------------------

.. code-block:: python

    class Point:
    # everything defined in here is in the class namespace

        def __init__(self, x, y):
            self.x = x
            self.y = y

so this class has a method called "__init__" -- which is a Python special method.

see: :download:`simple_classes.py <../examples/classes/simple_classes.py>`

The Initializer
---------------

The ``__init__``  special method is called when a new instance of a class is created.

You can use it to do any set-up you need:

.. code-block:: python

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


It gets the arguments passed when you call the class object:

.. code-block:: python

    Point(x, y)

Once you have defined an __init__, you can create "instances" of the class:

.. code-block:: python

    p = Point(3,4)

And access the attributes:

.. code-block:: python

    print("p.x is:", p.x)
    print("p.y is:", p.y)


Self
----

What is this ``self`` thing?

The instance of the class is passed as the first parameter for every method.

The name "``self``" is only a convention -- but you *DO* want to use it.

.. code-block:: python

    class Point:
        def a_function(self, x, y):
    ...

Does this look familiar from C-style procedural programming?

Anything assigned to a ``self.``  attribute is kept in the instance
name space -- ``self`` *is* the instance.

That's where all the instance-specific data is.


Class Attributes
----------------

.. code-block:: python

    class Point(object):
        size = 4
        color= "red"
        def __init__(self, x, y):
            self.x = x
            self.y = y

Anything assigned in the class scope is a class attribute -- every
instance of the class shares the same one.

Note: the methods defined by ``def`` are class attributes as well.

The class is one namespace, the instance is another.

.. code-block:: python

    class Point:
        size = 4
        color = "red"
    ...
        def get_color(self):
            return self.color
    >>> p3.get_color()
     'red'

So in this case, ``size`` and ``color`` are class attributes.

But note in ``get_color`` -- it accesses color from ``self``:

class attributes are accessed with ``self``  also.

So what is the difference?

 * class attributes are shared by ALL the instances of the class.
 * each instance has its own copy of each instance attribute.

Example:

.. code-block:: ipython

    In [6]: class C:
       ...:     x = [1,2,3] # class attribute
       ...:     def __init__(self):
       ...:         self.y = [4,5,6] # instance attribute
       ...:

    In [7]: c1 = C()

    In [8]: c2 = C()

    In [9]: c1.x is c2.x # does each instance see the same x?
    Out[9]: True

    In [10]: c1.y is c2.y # does each instance see the same y?
    Out[10]: False

But what are the consequences of this? It's a **very** important distinction. watch what happens if we change something in these objects, adding a new item to both the lists in ``c1``:

.. code-block:: ipython

    # add an item to c1's x list
    In [5]: c1.x.append(100)

    In [6]: c1.x
    Out[6]: [1, 2, 3, 100]

    In [7]: c2.x
    Out[7]: [1, 2, 3, 100]

Note that adding something to ``c1.x`` also changed ``c2.x`` that is because they are the *same* list -- ``.x`` is a *class attribute* -- c1 and c2 share the same class, so they share the same class attributes.

But if we change ``y``, an instance attribute:

.. code-block:: ipython

    In [8]: c1.y.append(200)

    In [9]: c1.y
    Out[9]: [4, 5, 6, 200]

    In [10]: c2.y
    Out[10]: [4, 5, 6]

appending to ``c1.y`` did not change ``c2.y`` -- ``y`` in this case is a an *instance* attribute -- each instance has its own version -- changing one will not affect the others.

So when you are deciding where to "put" something, you need to think about whether all instances are the same, or if they each need their own version of the attribute. As a class attribute, you can access it from the class namespace as well, and it will affect all instances of that class:

.. code-block:: python

    In [11]: C.x.append(2222)

    In [12]: c1.x
    Out[12]: [1, 2, 3, 100, 2222]

    In [13]: c2.x
    Out[13]: [1, 2, 3, 100, 2222]

So here we changed ``x`` on the *class* object, ``C``, and the change showed up in all the instances, ``c1`` and ``c2``.


Typical methods
---------------

.. code-block:: python

    import math

    class Circle:
        color = "red"

        def __init__(self, diameter):
            self.diameter = diameter

        def expand(self, factor=2):
            self.diameter = self.diameter * factor
            return None  # note that if you leave that off, it will still return None

        def area(self):
            area = (self.diameter / 2)**2 * math.pi
            return area


Methods take some parameters, and possibly manipulate the attributes in ``self``.

Remember that classes are about encapsulating the data and the functions that act on that data -- the methods are the functions that act on the data.

They may or may not return something useful.

.. note::

  It is convent in Python that methods that change the internal state of an object return None, whereas methods that return a new object, or some calculated result without changing the state return that value.

  You can see examples of this in the python built ins -- methods of lists like ``append`` or ``sort`` return None.


Gotcha !
--------

.. code-block:: python

    ...
        def grow(self, factor=2):
            self.diameter = self.diameter * factor
    ...
    In [205]: C = Circle(5)
    In [206]: C.grow(2,3)

    TypeError: grow() takes at most 2 arguments (3 given)

Huh???? I only gave 2:

``self`` is implicitly passed in for you by Python. so it actually *did* get three!


Functions (methods) are First Class Objects
-------------------------------------------

Note that in Python, functions are first class objects, so a method *is* an attribute.

All the same rules apply about attribute access: note that the methods are defined in the class -- so they are class attributes.
All the instances share the same methods.

But each method gets its own namespace when it is actually called, so there is no confusion -- just like when you call a regular function multiple times.

Manipulating Attributes
-----------------------

Python makes it very easy to manipulate object's attributes -- you can access them with the "dot" notation, and simply set them like any other variable.  With the Circle class above:

.. code-block:: python

    In [15]: c = Circle(2)

    In [16]: c.area()
    Out[16]: 3.141592653589793

    In [17]: c.diameter = 4

    In [18]: c.area()
    Out[18]: 12.566370614359172

Note that after I changed the diameter attribute, when I called the ``area()`` method --it used the new diameter. Simple attribute access changed the state of the object.

So you now know how to:

 * Define a class
 * Give the class shared (class) attributes
 * Add an initializer to set up it's initial state
 * Add methods to manipulate that state.
 * Add methods that return the results of calculations of the current state

You can do a lot with this simple functionality -- but all it's done is put everything together in a neat package -- useful, but the real power of OO comes when you can subclass.  So time to move on:

:ref:`subclassing_inheritance`






