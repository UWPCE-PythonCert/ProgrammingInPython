.. _properties:

##########
Properties
##########

https://en.wikipedia.org/wiki/Property_%28programming%29#Python

Attributes are clear and concise
--------------------------------

.. container::

    One of the strengths of Python is lack of clutter.

    .. code-block:: ipython

        In [5]: class C:
                def __init__(self):
                        self.x = 5
        In [6]: c = C()
        In [7]: c.x
        Out[7]: 5
        In [8]: c.x = 8
        In [9]: c.x
        Out[9]: 8

And we want to maintain this clarity as we develop our programs.

Getter and Setters
------------------

But what if you need to add behavior later?


* do some calculation
* check data validity
* keep things in sync


.. code-block:: ipython

    In [5]: class C:
       ...:     def __init__(self):
       ...:         self.x = 5
       ...:     def get_x(self):
       ...:         return self.x
       ...:     def set_x(self, x):
       ...:         self.x = x
       ...:
    In [6]: c = C()
    In [7]: c.get_x()
    Out[7]: 5
    In [8]: c.set_x(8)
    In [9]: c.get_x()
    Out[9]: 8

This is verbose -- `Java`_?

.. _Java: http://dirtsimple.org/2004/12/python-is-not-java.html

Properties
----------

.. code-block:: ipython

    In [27]: class C:
       ....:     _x = None
       ....:     @property
       ....:     def x(self):
       ....:         return self._x
       ....:     @x.setter
       ....:     def x(self, value):
       ....:         self._x = value
    In [28]: c = C()
    In [30]: c.x = 5
    In [31]: print(c.x)
    5

Now the interface is like simple attribute access!

Decorators
----------

What's up with the "@" symbols?

Those are "decorations". It is a syntax for wrapping functions up with something special.

We will cover decorators in detail in another part of the program, but for now just copy the syntax.

.. code-block:: python

    @property
    def x(self):

means: make a property called x with this as the "getter".

.. code-block:: python

    @x.setter
    def x(self, value):

means: make the "setter" of the 'x' property this new function.

Read Only Attributes
--------------------

You do not need to define a setter. If you don't, you get a "read only" attribute:

.. code-block:: ipython

    In [11]: class D():
       ....:     def __init__(self, x=5):
       ....:         self._x = x
       ....:     @property
       ....:     def x(self):
       ....:         """I am read only"""
       ....:         return self._x
       ....:
    In [12]: d = D()
    In [13]: d.x
    Out[13]: 5
    In [14]: d.x = 6
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-14-c83386d97be3> in <module>()
    ----> 1 d.x = 6
    AttributeError: can't set attribute

Deleters
--------

If you want to do something special when a property is deleted, you can define a deleter as well:

.. code-block:: ipython

    In [11]: class D():
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     @property
       ....:     def x(self):
       ....:         return self._x
       ....:     @x.deleter
       ....:     def x(self):
       ....:         del self._x

If you leave this out, the property can't be deleted, which is usually
what you want.

Play around with some properties code:

:download:`properties_example.py <../examples/properties/properties_example.py>`
