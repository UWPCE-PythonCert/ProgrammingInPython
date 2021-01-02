:orphan:

.. _metaprogramming:

################
Metaprogramming
################

**Programs that write programs....**

Metaprogramming
===============

  "Metaprogramming is a programming technique in which computer programs have the ability to treat programs as their data. It means that a program can be designed to read, generate, analyze or transform other programs, and even modify itself while running."

``https://en.wikipedia.org/wiki/Metaprogramming``

In other words: A metaprogram is a program that writes (or modifies) programs.

As a dynamic language, Python is very well suited to metaprogramming, as it allows objects to be modified at run time. It also provides excellent tools for:

**Introspection:**

  "The ability of a program to examine the type or properties of an object at runtime."


Everything  is an object
------------------------

Everything is an object in python: simple types like numbers and strings, as well as functions, classes, etc.

That means that everything:

* Can be created at runtime

* Passed as a parameter

* Returned from a function

* Assigned to a variable

This "everything is an object" is what allows full introspection and metaprogramming.

**Wait!** didn't we use these features with closures and decorators??

Yes, indeed we did. And decorators are one of Python's metaprogramming tools. In this case, it's manipulating functions (and methods, which are just functions in a class) with code. Now we're going to learn how to manipulate other objects as well.


Introspection and manipulation tools
====================================

``getattr()`` and ``setattr()``
-------------------------------

These are the basic tools for, well, getting and setting attributes. They allow you to get and set attributes of an object by name:

.. code-block:: ipython

  In [1]: class Dummy():
     ...:     """A class with nothing in it"""
     ...:     pass
     ...:

  In [2]: obj = Dummy()

  In [3]: vars(obj)
  Out[3]: {}

  In [4]: setattr(obj, 'this', 54)

  In [5]: vars(obj)
  Out[5]: {'this': 54}

  In [6]: getattr(obj, 'this')
  Out[6]: 54

Let's play with this: (demo)

NOTE: Do attributes have to be legal python names?? Try it!

Note: there is also ``delattr`` to remove an attribute.

Namespaces are Dictionaries
---------------------------

Another cool feature of python is that namespaces are (often) dictionaries. That means that you can directly manipulate the names and associated values of many objects directly.

You can get the dict of a namespace with the ``vars()`` builtin:

From a note on python-ideas:

  "... It isn't to be
  a slightly different version of dir(), instead vars() should return the
  object's namespace. Not a copy of the namespace, but the actual
  namespace used by the object."

This is not always true, e.g. for classes vars() returns a mappingproxy.

From the Python Docs:

"Objects such as modules and instances have an updateable ``__dict__`` attribute; however, other objects may have write restrictions on their ``__dict__`` attributes (for example, classes use a types.MappingProxyType to prevent direct dictionary updates)."

https://docs.python.org/3.6/library/functions.html#vars


``__dict__``
------------

An object's ``__dict__`` special attribute is used as the namesapce of an updateable object -- it's what you might expect, an actual dictionary used to hold the names in the namespace.

For the most part, ``vars()`` will return the ``__dict__`` of an object. It's kind of like ``len()`` and the ``__len__`` attribute.  But it's a bit better to use ``vars()`` to access an object's namespace -- it will work in more places.

``dir()``
---------

You may have used ``dir()`` to see the names in an object. It looks a lot like vars().keys() -- but it's not. There are two key differences:

``dir()`` walks the class hierarchy of an object to give you all the attributes available:

Create a class with a class attribute and an instance attribute:

.. code-block:: python

    In [7]: class C:
       ...:     a_class_attribute = 0
       ...:     def __init__(self):
       ...:         self.an_instance_attribute = 0

create an instance of that class.

.. code-block:: python

    In [8]: c = C()

    In [9]: dir(c)
    Out[9]:
    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     ...
     '__subclasshook__',
     '__weakref__',
     'a_class_attribute',
     'an_instance_attribute']

Note that both the class attribute and the instance attribute are there.

Let's see what ``vars()`` gives us:

.. code-block:: python

    In [10]: vars(c)
    Out[10]: {'an_instance_attribute': 0}

Just the instance attribute. Now let's look at the class object:

.. code-block:: python

    In [11]: vars(C)
    Out[11]:
    mappingproxy({'__dict__': <attribute '__dict__' of 'C' objects>,
                  '__doc__': None,
                  '__init__': <function __main__.C.__init__>,
                  '__module__': '__main__',
                  '__weakref__': <attribute '__weakref__' of 'C' objects>,
                  'a_class_attribute': 0})

Now we get the class attribute, and a bunch more, but not all of them by any means. That's because the rest are inherited from ``object``.

``vars()`` is also giving the namespace dict -- both the names and the values. So it's what you want if you are going to manipulate an object.


Manipulating a namespace
------------------------

``vars()`` with no argument returns the local namespace (same as ``locals()``). So you can manipulate even the local module namespace directly:

.. code-block:: ipython

  In [1]: fred
  ---------------------------------------------------------------------------
  NameError                                 Traceback (most recent call last)
  <ipython-input-1-08b622ddf7eb> in <module>()
  ----> 1 fred

  NameError: name 'fred' is not defined

Of course it's not -- we haven't defined it. But if I access the local namespace with vars, and then add a name:

.. code-block:: ipython

  In [2]: local_ns = vars()

  In [3]: local_ns['fred'] = "This is a new name in the local namespace"

  In [4]: fred
  Out[4]: 'This is a new name in the local namespace'

Now the name ``fred`` is there, just as if we had assigned the name in the normal way:

.. code-block:: ipython

  In [5]: fred = "now a different value"

  In [6]: fred
  Out[6]: 'now a different value'

and we can access names that way too:

.. code-block:: ipython

  In [7]: local_ns['fred']
  Out[7]: 'now a different value'

Note that I didn't call vars() again to get the new value -- ``vars()`` returns the actual dict used for the namespace -- so it's mutated, the change shows up everywhere.

Keep in mind that not all namespaces are writable. class objects, for instance, return a ``mappingproxy``, which is the namespace of the class object, but it is not a regular dict -- it's essentially a read-only dict.


Example of Manipulating Instance Attributes
-------------------------------------------

Check out the code here:
:download:`get_set_attr.py </examples/metaprogramming/get_set_attr.py>`

It uses ``vars()`` in the str method to dynamically create a nice printable class.

Then there is a simple function that lets the user manipulate that class, changing and adding attributes.

Can you add code to let the user delete an attribute?


Class Objects
=============

Metaprogramming is all about creating and manipulating programs. Classes are a very important part of programming in Python, so naturally, to do proper metaprogramming, we need to be able to create and manipulate class objects as well.

And classes can have a lot more complexity than simple objects (or instances).


What's in a Class?
------------------

A class (and instance) object stores its attributes in a dictionary, or dictionary-like object. instances use a regular old python dict. You can access that dict with the ``__dict__`` attribute or ``vars()`` function:

.. code-block:: ipython

  In [56]: class Simple():
      ...:       ...:     this = "a class attribute"
      ...:       ...:     def __init__(self):
      ...:       ...:         self.that = "an instance attribute"
      ...:

  In [57]: vars(Simple)
  Out[57]:
  mappingproxy({'__dict__': <attribute '__dict__' of 'Simple' objects>,
                '__doc__': None,
                '__init__': <function __main__.Simple.__init__>,
                '__module__': '__main__',
                '__weakref__': <attribute '__weakref__' of 'Simple' objects>,
                'this': 'a class attribute'})

And an instance of that object:

.. code-block:: ipython

  In [59]: obj = Simple()

  In [60]: obj.__dict__
  Out[60]: {'that': 'an instance attribute'}


What class does this object belong to?
--------------------------------------

Every object has a ``__class__`` attribute specifying what class the object belongs to:

.. code-block:: ipython

    In [16]: obj.__class__
    Out[16]: __main__.Simple

and that is the actual class object:

.. code-block:: ipython

  In [17]: obj.__class__ is Simple
  Out[17]: True

what is the class of a class object itself?

.. code-block:: ipython

  In [61]: Simple.__class__
  Out[61]: type

Interesting -- we've seen ``type`` as a function that tells you what type an object is (which is it's ``__class__``, by the way...). But it turns out ``type()`` is so much more...

"type" or "class"
-----------------

We talk about "classes", and yet we get the class of an object with ``type()``.

In python, "type" and "class" are essentially the same thing.

So why the two names?

History: in the early days of python, a "type" was a built-in object, and a "class" was an object created with code:

type - class unification began in python 2.2:

``https://www.python.org/download/releases/2.2/descrintro/``

In python3, the unification is complete -- types *are* classes and vice-versa -- the terms are interchangeable.

``type()``
----------

So: ``type()`` will tell you what type (or class) and object is if you pass it one parameter. But if you pass it more, it does something pretty cool -- it makes a brand new class object.

From the docstring:

.. code-block:: ipython

  Docstring:
  type(object) -> the object's type
  type(name, bases, dict) -> a new type

So that means if you pass in a single parameter, an object -- it will return the type of that object. But if you pass in three arguments, you get a new class object!


Creating a class from scratch
-----------------------------

.. code-block:: python

    In [14]: atts = {'foo':'nice', 'bar':'sweet'}

    In [15]: type("CoolClass", (), atts)
    Out[15]: __main__.CoolClass

    In [16]: CoolClass = type("CoolClass", (object,), atts)

    In [19]: cc = CoolClass()

    In [20]: cc.foo
    Out[20]: 'nice'

    In [21]: cc.bar
    Out[21]: 'sweet'

    In [22]: vars(CoolClass)
    Out[22]:
    mappingproxy({'__dict__': <attribute '__dict__' of 'CoolClass' objects>,
                  '__doc__': None,
                  '__module__': '__main__',
                  '__weakref__': <attribute '__weakref__' of 'CoolClass' objects>,
                  'bar': 'sweet',
                  'foo': 'nice'})


That is equivalent to:

.. code-block:: python

   class CoolClass:
      foo = 'nice'
      bar = 'sweet'


But it was created at runtime, returned from a function and assigned to a variable.

http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example

And it is a *class object*, not and instance -- it can be used to make instances from there.

The signature is: ::

    type(name, bases, dict)

so you need to pass in three things to make a class object.

``name``:  the name of the class -- this is what comes after the ``class`` keyword in the usual way...

``bases``: a tuple of base classes -- this is the same as passing them when contructing the class.

``dict``: this is a dictionary of the class attributes -- this will become the ``__class__`` of the class object (after some standard stuff is added)




Using type() to build a class
-----------------------------

The ``class`` keyword is syntactic sugar, we can get by without it by
using type

.. code-block:: python

    class MyClass:
        x = 1

or

.. code-block:: python

    MyClass = type('MyClass', (), {'x': 1})

(``object`` is automatically a superclass)


Adding methods to a class built with ``type()``
-----------------------------------------------

remember that functions are objects, so methods are simply attributes of a class that happen to be functions. So to add a method to a class created with ``type()``, just define a function with the correct signature and add it to the attr dictionary:

.. code-block:: python

    def my_method(self):
        print("called my_method, x = %s" % self.x)

    MyClass = type('MyClass',(), {'x': 1, 'my_method': my_method})
    o = MyClass()
    o.my_method()

How would you do an __init__ this way?

Try it yourself.....does it work?


What type is type?
------------------

.. code-block:: ipython

  In [30]: type(type)
  Out[30]: type

Hmm, so type is a a type --this is the special case -- it has to stop somewhere!

Metaclasses
-----------

Objects get created from classes. So what is the class of a class?

The class of a Class is a metaclass

The metaclass can be used to dynamically create a class

The metaclass, being a class, also has a metaclass


What is a metaclass?
--------------------

-  A class is something that makes instances
-  A metaclass is something that makes classes
-  A metaclass is most commonly used as a class factory
-  Metaclasses allow you to do 'extra things' when creating a class,
   like registering the new class with some registry, adding methods
   dynamically, or even replace the class with something else entirely (sound familiar from decorators?)
-  Every object in Python has a metaclass
-  The default metaclass is ``type``


``metaclass``
-------------

So the default metaclass is ``type`` -- that is, type is used to make the class. But now we get to the fun stuff -- we can write our own metaclass -- and use that to create new class objects.

Setting a class' metaclass:
...........................

.. code-block:: python

  class Foo(metaclass=MyMetaClass):
      pass


The class assigned to the ``metaclass`` keyword argument will be used to create the object class ``Foo``. (instead of ``type``)

If the ``metaclass`` kwarg is not defined, it will use type to create the class.

Whatever is assigned to ``metaclass`` should be a callable with the
same signature as type(): (``(name, bases, dict)``)

**Python2 NOTE:**

In Python 2, instead of the keyword argument, a special class attribute: ``__metaclass__`` is used:

.. code-block:: python

    class Foo(object):
      __metaclass__ = MyMetaClass

Otherwise it's the same.

The __metaclass__ attribute is part of determining that function. If __metaclass__ is a key in the body dictionary then the value of that key is used. This value could be anything, although if not callable an exception will be raised.
from http://jfine-python-classes.readthedocs.io/en/latest/decorators-versus-metaclass.html

Why use metaclasses?
--------------------

What a metaclass does is create a way to create custom classes on the fly.  You can do it directly with the ``type``, but if you write a metaclass, new classes can be made with that metaclass in the usual way.

They can be useful when creating an API or framework.

Whenever you need to manage object creation for one or more classes.

Examples may help, so take a look at:
:download:`singleton.py </examples/metaprogramming/singleton.py>`

Or consider the Django ORM:

.. code-block:: python

  class Person(models.Model):
      name = models.CharField(max_length=30)
      age = models.IntegerField()

  person = Person(name='bob', age=35)
  print person.name

When the Person class is created, it is dynamically modified to
integrate with the database configured backend. Thus, different
configurations will lead to different class definitions. This is
abstracted from the user of the Model class. And the user doesn't have to know anything about that ugly database stuff :-)


Here is the Django Model metaclass:

https://github.com/django/django/blob/master/django/db/models/base.py#L61

pretty ugly, eh?


``__new__``
-----------

A bit of a sidetrack ...

What is this ``__new__`` thing? It's another of Python's special dunder methods. ``__new__`` is called when you make a new instance of a class.

Wait? isn't ``__init__`` the constructor of the class?

Not really -- ``__init__`` is the *initializer* -- it initializes the instance -- setting instance attributes, etc. But remember its signature?

.. code-block:: python

  def __init__(self, *args, **kwargs)

What's that self thing? That's the instance that is being initialized -- but it already exists -- it has to already have been created.

Most of the time, that's all you need -- you want the instance created in the usual default way, and then you can initialize it. But if you need to do something before the object is initialized -- you can define a ``__new__`` method.

.. code-block:: python

    class Class():
        def __new__(cls, arg1, arg2):
            some_code_here
            return cls(...)
            ...

* ``__new__`` is called: it returns a new instance

* The code in ``__new__`` is run to pre-initialize the instance

* ``__init__`` is called

* The code in ``__init__`` is run to initialize the instance

``__new__`` is a static method (it can be called on the class object itself) -- but it must be called with a class object as the first argument.

.. code-block:: python

    class Class(superclass):
        def __new__(cls, arg1, arg2):
            some_code_here
            return superclass.__new__(cls)
            .....

``cls`` is the class object.

The arguments (arg1, arg2) are what's passed in when calling the class.

It needs to return a class instance -- usually by directly calling the superclass ``__new__`` (which returns a new instance).

If there are no superclasses, you can call ``object.__new__`` (or ``super().__new__``)


When to use ``__new__``
------------------------

When would  you need to use it:

* Subclassing an immutable type:

  - It's too late to change it once you get to ``__init__``

* When ``__init__`` is not called:

  - unpickling

  - copying

You may need to put some code in ``__new__`` to make sure things
go right.

More detail here:

https://docs.python.org/3/reference/datamodel.html#object.__new__


``__new__``  vs  ``__init__`` in Metaclasses
--------------------------------------------

Remember that metaclasses are used to create new class objects (instances of type) -- so ``__new__`` is critical to creating that class.

``__new__`` is used when you want to control the creation of the class (object)

``__init__`` is used when you want to control the initialization of the class (object)

``__new__`` and ``__init__`` are both called when the module containing the class is imported for the first time. i.e. at compile time.

``__call__`` is used when you want to control how a class (object) is called (instantiation)


.. code-block:: python

   class CoolMeta(type):
       def __new__(meta, name, bases, dct):
           print('Creating class', name)
           return super(CoolMeta, meta).__new__(meta, name, bases, dct)
       def __init__(cls, name, bases, dct):
           print('Initializing class', name)
           super(CoolMeta, cls).__init__(name, bases, dct)
       def __call__(cls, *args, **kw):
           print('Meta has been called')
           return type(cls, *args, **kw)

   class CoolClass(metaclass=CoolMeta):
       def __init__(self):
           print('And now my CoolClass exists')

   print('Actually instantiating now')
   foo = CoolClass()

:download:`cool_meta.py </examples/metaprogramming/cool_meta.py>`


Metaclass example
-----------------

Consider wanting a metaclass which mangles all attribute names to
provide uppercase and lower case attributes

.. code-block:: python

    class Foo(metaclass=NameMangler):
        x = 1

    f = Foo()
    print(f.X)
    print(f.x)


NameMangler
-----------

.. code-block:: python

  class NameMangler(type):

      def __new__(cls, clsname, bases, _dict):
          uppercase_attr = {}
          for name, val in _dict.items():
              if not name.startswith('__'):
                  uppercase_attr[name.upper()] = val
                  uppercase_attr[name] = val
              else:
                  uppercase_attr[name] = val

          return super().__new__(cls, clsname, bases, uppercase_attr)


  class Foo(metaclass=NameMangler):
      x = 1


LAB: Working with NameMangler
-----------------------------

Download: :download:`mangler.py </examples/metaprogramming/mangler.py>`

Modify the NameMangler metaclass such that setting an attribute f.x also
sets f.xx

Now create a new metaclass, MangledSingleton, composed of the ``NameMangler`` class you just worked with, and the ``Singleton`` class here:
:download:`singleton.py </examples/metaprogramming/singleton.py>`

Assign it to the ``metaclass`` keyword argument of a new class and verify that it works.

Your code should look like this:

.. code-block:: python

    class MyClass(metaclass=MangledSingleton) # define this
        x = 1

    o1 = MyClass()
    o2 = MyClass()
    print(o1.X)
    assert id(o1) == id(o2)


The Singleton
-------------

One common use of metaclasses is to create a singleton:

   "The singleton pattern is a software design pattern that restricts the instantiation of a class to one object."

https://en.wikipedia.org/wiki/Singleton_pattern

The above exercise provided an example of this
(:download:`singleton.py </examples/metaprogramming/singleton.py>`)

However, metaclasses are not the only way to create a singleton. It really depends on what you are trying to do with your singleton.

http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

Class decorators?
-----------------

We touched on class decorators a bit when decorators were introduced:

.. code-block:: python

    @a_decorator
    class MyClass():
        ...

A decorator is a "callable" that returns a "callable" -- usually a modified (or "wrapped") version of the one passed in.

Class objects are callable -- you call them when you instantiate a instance:

.. code-block:: python

   an_inst = MyClass()

So you can decorate a class as well as functions and methods.

In fact, you can do many of the same things that you can do with metaclasses.

When you decorate a class, you can change it in some way, and then the
changed version replaces the one in the definition.

This also happens at compile time, rather than run time, just like metaclasses.

class decorators were actually introduced AFTER metaclasses -- maybe they
are a clearer solution to some problems?

As an example, in Python 3.7, there is a new feature in the standard library: ``Data Classes``, introduced in
`PEP 557 <https://www.python.org/dev/peps/pep-0557/>`_

They are a quick way to make a simple class whose prime purpose is to store a set of fields -- kind of like a database record. What the new tool provides is auto-generation of all the boilerplate code for the ``__init__``, etc. They could have been implemented with a metaclass, but it was decided to use a class decorator instead. From the PEP:

  "No base classes or metaclasses are used by Data Classes. Users of these classes are free to use inheritance and metaclasses without any interference from Data Classes. The decorated classes are truly "normal" Python classes. The Data Class decorator should not interfere with any usage of the class."

A key difference between using a class decorator and a metaclass is that a metaclass is used to create the class -- so you can manipulate things before the class is created.

Class decorators, on the other hand, are applied *after* the class has been created. Python is pretty dynamic, so for the most part, you can change things after the fact, but there are a few exceptions. The docstring, for instance is not mutable.

Also, due to this difference in timing, an attribute added to a class by a metaclass can be overridden by the class -- but an attribute added by a class decorator will override the class' version, if it exists. That could get a bit ugly.

Here is a bit of discussion of metaclasses vs decorators:

`Decorators versus __metaclass__ <http://jfine-python-classes.readthedocs.io/en/latest/decorators-versus-metaclass.html>`_

And another one:

`A Study of Python's More Advanced Features Part III: Classes and Metaclasses <http://sahandsaba.com/python-classes-metaclasses.html>`_

And this is a argument for class decorators by the author or the patch that enabled them (in Python 2.6):

`Jack Diederich: Class Decorators: Radically Simple  <https://www.youtube.com/watch?v=cAGliEJV9_o>`_


NameMangler Decorator Edition
-----------------------------

For a simple example, let's see how to make NameMangler with a decorator.

Here is the code:
:download:`mangler_dec.py </examples/metaprogramming/mangler_dec.py>`

It is well commented, but a couple of key points to consider:

1) A class decorator takes a class object as an argument:

.. code-block:: python

    def name_mangler(cls):

2) As a class object, you can get its attribute dict (__dict__) with:

.. code-block:: python

    attr_dict = vars(cls)

3) Class attribute dictionaries are not writable, so you need to use
   ``setattr()`` (and potentially ``delattr()``) to change the class
   attributes.


json_save
=========

For a more involved (and useful!) example, see the json_save package:

:download:`json_save.zip </examples/metaprogramming/json_save.zip>`

It may also be in your class repo solutions dir:

``solutions/metaprogramming/json_save/``

It is a system for saving and re-loading objects.

It works a bit like the ORMs -- you specify what attributes you want to save, and what their types are.

JSON
----

If you are not familiar with JSON:

`JavaScript Object Notation (JSON) <https://www.json.org/>`_ is a format borrowed from the Web -- Javascript being the de-facto scripting language in browsers.  It is a great format for communicating with browsers, but it has become a common serialization format for many other uses: it is simple, flexible, and human-readable and writable.

It also maps pretty much directly to (some of) the core Python datatypes: lists, dictionaries, strings, and numbers.

But it does not directly support more complex objects -- that is what json_save is all about.

Metaclass json_save
-------------------

The first solution uses a metaclass: ``json_save_meta.py``

It turns out that the metaclass part of the code is pretty simple and small.

But there is a lot of other nifty magic with classes in there
-- so let's take a look:


Decorator json_save
-------------------

The second solution uses a decorator: ``json_save_dec.py``

As in the metaclass case, the actual decorator is pretty simple.

And it can use much of the code from the metaclass solution -- since not much really had anything specific to metaclasses.

Let's take a look at that, too:


