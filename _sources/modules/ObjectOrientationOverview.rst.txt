.. _object_orientation_overview:

###########################
Object Orientation Overview
###########################

In the Beginning there was the GOTO.

... and in fact, there wasn't even that.


Programming Paradigms
=====================

https://en.wikipedia.org/wiki/Programming_paradigm

Software Design
---------------

Good software design is about code re-use, clean separation of concerns,
refactorability, testability, etc...

OO can help with all that, but:

  * It doesn't guarantee it.

  * It can get in the way.

What is Object Oriented Programming?

|
    "Objects can be thought of as wrapping their data
    within a set of functions designed to ensure that
    the data are used appropriately, and to assist in
    that use"
|

- http://en.wikipedia.org/wiki/Object-oriented_programming


**Even simpler:**

"Objects are data and the functions that act on them in one place."

This is the core of "encapsulation"


The Dominant Model
------------------

OO is the dominant model for the past couple decades, but it is not the only model, and languages such as Python increasingly mix and blend models (such as  Procedural, Object Oriented, Functional).  In Python, it is best to choose the approach that best solves your problem.


Object Oriented Concepts
------------------------

These are all terms you will hear when talking about Object Oriented Programming:


Class
  A category of objects: particular data and behavior: for example, a "circle" (same as a "type" in Python).

Instance
  A particular object of a class: a specific circle.

Object
  The general case of an instance -- really any value (in Python anyway). This term is a bit overloaded -- it also is the generic term for any class. So a class is a particular kind of object.

Attribute
  Something that belongs to an object (or class): generally thought of
  as a simple value, variable, or single object, as opposed to a ...

Method
  A function that belongs to a class. In Python, functions *are* semantically the same as any other type -- so all methods are "attributes", but not all attributes are methods. Methods are the functions, or more strictly speaking: the 'callable' attributes.

Encapsulation
  The approach where the details of the structure are "hidden" in a class -- the user of the class does not need to know how the data is stored (and may not be able to know...)

Data Protection
  This is the concept that classes can hide data from outside access (sometimes called "private" attributes. Python does not strictly support data protection.

Class vs. Instance Attributes
  Attributes can be attached to a class -- that is, shared by all instances of that class, or they can be attached to only that instance.

Subclassing
  Subclassing is making a special version of a class. It is a class itself, but it gets ("inherits") all the attributes and methods of its "parent" class. This makes it easy to re-use code.

Overriding methods
  When subclassing, the subclass inherits the methods of its parent class. But it can replace them as well, which is called overriding a method.

Operator Overloading
  Python (and most languages) have operators, like `+`, `-`. `*`, etc. Overloading an operator is a way to define what that operator means to a new class that is not originally part of the language.

Polymorphism
  Allowing instances of multiple classes to be used in the same way. Literally means "having many forms". This simply happens with Python's "Duck Typing" -- An object with a given method can have that method called on it. But in statically typed languages, this is a big deal.

Python and OO
-------------

Is Python a "True" Object-Oriented Language?

What are its strengths and weaknesses vis-a-vis OO?

But it does not support *full* encapsulation, i.e., it does not require classes, and classes don't have "private" attributes.

**but ...**

Folks can't even agree on what OO "really" means.

See: `The Quarks of Object-Oriented Development <http://ontheturingtest.blogspot.com/2013/11/the-quarks-of-objected-orientation-la.html>`_
(Deborah J. Armstrong)

Object Oriented Design
----------------------

There are many books (and web sites, and blog posts, and ...) about "Object Oriented Design", which is an approach to designing your program by starting with the "nouns" (objects) the program needs to manipulate.

This may be a good approach for a "pure" OO language, but with Python it tends to lead to verbose, poorly performing code.

So my recommendation is to think in terms of what makes sense for your project:

.. centered:: **There is no single best paradigm for software design**



Python's roots
--------------

|
|  C
|  C with Classes (aka C++)
|  Modula2
|

You can do OO in C
------------------

Which today is not considered an OO Language. See the GTK+ project.

So OO is really a design approach -- putting the data together with the functions that manipulate that data. It isn't defined by language features.

That being said: OO languages give you some handy tools to make it easier
(and safer):

  * Polymorphism (duck typing gives you this)
  * Inheritance

are the big ones.

You will need to understand OO
------------------------------

- It's a good idea for a lot of problems.

- You'll need to work with OO packages.

(Much of the standard library is object oriented).

If not OO Design, then what?
----------------------------

I like to take an incremental design approach:

You start with your specification -- what your program has to **do**

Then you start to create the data structures you need and the functions you need to manipulate that data.

If you find yourself needing more than one function that is manipulating the same data -- you may need a class.

It's almost that simple :-)

You may also find that you need multiple "things" that have slightly different properties or behavior -- that is a case for subclassing.

As you learn what is possible, this will all start to make more sense.

So time to move on to how to actually **do** OO in Python!

Here's how to do it in Python: :ref:`python_classes`
