.. _subclassing_inheritance:

###########################
Subclassing and Inheritance
###########################

How to put the pieces together to build a complex system without repeating code.

Inheritance
===========

In object-oriented programming (OOP), inheritance is a way to reuse the code
of existing objects, or to establish a subtype from an existing object.

Objects are defined by classes. Classes can inherit attributes and behavior
from pre-existing classes called base classes or super classes.

The resulting classes are known as derived classes or subclasses.

(http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29)

Subclassing
-----------

A subclass "inherits" all the attributes (methods, etc) of the parent class. This means that a subclass will have everything that its "parents" have.

You can then change ("override") some or all of the attributes to change the behavior.  You can also add new attributes to extend the behavior.

You create a subclass by passing the superclass to the ``class`` statement.

The simplest subclass in Python:

.. code-block:: python

    class A_subclass(The_superclass):
        pass

``A_subclass``  now has exactly the same behavior as ``The_superclass`` -- all the same attributes and methods.

Overriding attributes
---------------------

Overriding is as simple as creating a new attribute with the same name:

.. code-block:: ipython

  In [1]:     class Circle:
     ...:         color = "red"
     ...:

We now have a class with a class attribute, ``color``, with the value: "red". All instances of ``Circle`` will be red:

.. code-block:: ipython

  In [2]: c = Circle()

  In [3]: c.color
  Out[3]: 'red'

If we create a subclass of Circle, and set that same class attribute:

.. code-block:: ipython

  In [4]:     class NewCircle(Circle):
     ...:         color = "blue"
     ...:

  In [5]: nc = NewCircle()

  In [6]: nc.color
  Out[6]: 'blue'

We now have a class that is all the same, except that its instances have the color blue.

Note that any methods that refer to that attribute, will get the new value, even if the methods themselves have not changed:

.. code-block:: ipython

    In [10]: class Circle:
        ...:     color = "red"
        ...:
        ...:     def describe(self):
        ...:         return f"I am a {self.color} circle"
        ...:

    In [11]: class NewCircle(Circle):
        ...:     color = "blue"
        ...:

    In [12]: c = Circle()

    In [13]: c.describe()
    Out[13]: 'I am a red circle'

    In [14]: nc = NewCircle()

    In [15]: nc.describe()
    Out[15]: 'I am a blue circle'

Note that this is *why* self is passed in to every method -- when you write the method, you don't know exactly what class ``self`` will be -- it is an instance of the class at the time the method is called.

Overriding methods
------------------

Overriding methods is exactly the same thing, but with methods (remember, a method *is* an attribute in Python -- one that happens to be a function)

.. code-block:: python

    class Circle:
    ...
        def grow(self, factor=2):
            """grows the circle's diameter by factor"""
            self.diameter = self.diameter * factor
    ...

    class NewCircle(Circle):
    ...
        def grow(self, factor=2):
            """grows the area by factor..."""
            self.diameter = self.diameter * math.sqrt(2)


all the instances of the new class will have the new method -- similar, but different, behavior.  Note that both these methods are requiring that the class instance has a ``diameter`` attribute.


**Here's a program design suggestion:**

  Whenever you override a method, the interface of the new method should be the same as the old.  It should take the same parameters, return the same type, and obey the same preconditions and postconditions.

  If you obey this rule, you will find that any function designed to work with an instance of a superclass, like a Deck, will also work with instances of subclasses like a Hand or PokerHand.  If you violate this rule, your code will collapse like (sorry) a house of cards.

-- from *Think Python*


Overriding ``__init__``
-----------------------

``__init__`` is a common method to override.

You often need to call the super class ``__init__``  as well, so that any initialization required is performed:

.. code-block:: python

    class Circle:
        color = "red"
        def __init__(self, diameter):
            self.diameter = diameter
    ...
    class CircleR(Circle):
        def __init__(self, radius):
            diameter = radius*2
            Circle.__init__(self, diameter)


Exception to: "don't change the method signature" rule.

Often when you override ``__init__``, the new class may take an extra parameter or two.  In this case, you will want to keep the signature as similar as possible, and cleanly define what is part of the subclass. A common idiom in this case is this:

.. code-block:: python

    class A_Subclass(A_Superclass):

        def __init__(self, param1, param2, *args, **kwargs):
            self.param1 = param1
            self.init_something(param2)
            super().__init__(*args, **kwargs)

That is:

 * Put the extra parameters in the beginning of the list -- usually as required positional parameters.

 * Accept ``*args`` and ``**kwargs``

 * Pass everything else on to the superclass' __init__

Using ``*args`` and ``**kwargs`` is a way to make it clear that the rest is simply the signature of the superclass.  It is also flexible if the superclass (or others up in the hierarchy) changes -- it could completely change its signature, and this subclass would still work.


Using the superclass' methods
-------------------------------

In a subclass, you can access everything in the superclass: all attributes and other methods:

.. code-block:: python

    class Circle:
    ...
        def get_area(self, diameter):
            return math.pi * (diameter/2.0)**2


    class CircleR2(Circle):
    ...
        def get_area(self):
            return Circle.get_area(self, self.radius*2)


Note that there is nothing special about ``__init__``  except that it gets called automatically when you instantiate an instance. Otherwise, it is the same as any other method -- it gets ``self`` as the first argument, it can or can not call the superclass' methods, etc.


"Favor Object Composition Over Class Inheritance"
-------------------------------------------------

That is a quotation from the "Design Patterns" book -- one of the gospels of OO programming.

But what does it mean?

There are essentially two ways to add multiple functionalities to a class:

Subclassing

and

Composition

As we have just learned about subclassing, you might be tempted to do it a lot. But you need to be careful of over-using subclassing:

https://en.wikipedia.org/wiki/Composition_over_inheritance

Composition is when your classes have attributes of various types that they use to gain functionality -- "delegate" functionality to -- "Delegation" is a related concept in OO.


"Is a" vs "Has a"
.................

Thinking about "is a" vs "has a" can help you sort this out.

For example, you may have a class that needs to accumulate an arbitrary number of objects.

A list can do that -- so maybe you should subclass list?

To help decide -- Ask yourself:

-- **Is** your class a list (with some extra functionality)?

or

-- Does you class **have** a list?

You only want to subclass list if your class could be used anywhere a list can be used. In fact this is a really good way to think about subclassing in general -- subclasses should be specialized versions of the superclass. "Kind of" the same, but with a little different functionality.


Attribute Resolution Order
--------------------------

Once there is a potentially large hierarchy of subclasses, how do you know which one will be used?

When you access an attribute:

``an_instance.something``

Python looks for it in this order:

  * Is it an instance attribute ?
  * Is it a class attribute ?
  * Is it a superclass attribute ?
  * Is it a super-superclass attribute ?
  * ...

It can get more complicated, particularly when there are multiple superclasses (multiple inheritance), but when there is a simple inheritance structure (the usual case) -- it's fairly straightforward.

This is often referred to as "method resolution order" (MRO), because it's more complicated with methods, and in some languages, methods and attributes are more distinct than in Python. In Python, it can be thought of as "name resolution" -- everything in Python is about names and namespaces.

If you want to know more of the gory details -- here's some reading:

https://www.python.org/download/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html


What are Python classes, really?
--------------------------------

Putting aside the OO theory...

Python classes feature:

  * Namespaces

    * One for the class object
    * One for each instance

  * Attribute resolution order -- how do you find an attribute.
  * Auto tacking-on of ``self`` when methods are called
  * automatically calling ``__init__`` when the class object is called.

That's about it -- really!

(Well, not really, there is more fancy stuff going on under the hood -- but this basic structure will get you far).

Type-Based Dispatch
-------------------

Occasionally you'll see code that looks like this:

.. code-block:: python

      if isinstance(other, A_Class):
          Do_something_with_other
      else:
          Do_something_else

When it's called for, Python provides these utilities:

    * ``isinstance()``
    * ``issubclass()``

But it is *very* rarely called for! Between Duck Typing, polymorphism, and EAFP, you rarely need to check for type directly.

Wrap Up
-------

Thinking OO in Python:

Think about what makes sense for your code:

* Code re-use
* Clean APIs
* Separation of Concerns
* ...

OO can be a very powerful approach, but don't be a slave to what OO is *supposed* to look like.

Let OO work for you, not *create* work for you.

And the biggest way to do that is to support code re-use.

