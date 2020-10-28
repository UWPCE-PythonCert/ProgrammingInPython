.. _static_and_class_methods:


########################
Static and Class Methods
########################

You've seen how methods of a class are *bound* to an instance when it is
created.

And you've seen how the argument ``self`` is then automatically passed to the method when it is called.

And you've seen how you can call *unbound* methods on a class object so
long as you pass an instance of that class as the first argument.


**But what if you don't want or need an instance?**


Static Methods
--------------

A *static method* is a method that doesn't get self:

.. code-block:: ipython

    In [36]: class StaticAdder:

       ....:     @staticmethod
       ....:     def add(a, b):
       ....:         return a + b
       ....:

    In [37]: StaticAdder.add(3, 6)
    Out[37]: 9


Where are static methods useful?

Usually they aren't.  It is often better just to write a module-level function.

An example from the Standard Library (tarfile.py):

.. code-block:: python

    class TarInfo:
        # ...
        @staticmethod
        def _create_payload(payload):
            """Return the string payload filled with zero bytes
               up to the next 512 byte border.
            """
            blocks, remainder = divmod(len(payload), BLOCKSIZE)
            if remainder > 0:
                payload += (BLOCKSIZE - remainder) * NUL
            return payload


Class Methods
-------------

A class method gets the class object, rather than an instance, as the first
argument

.. code-block:: ipython

    In [41]: class Classy:
       ....:     x = 2
       ....:     @classmethod
       ....:     def a_class_method(cls, y):
       ....:         print("in a class method: ", cls)
       ....:         return y ** cls.x
       ....:
    In [42]: Classy.a_class_method(4)
    in a class method:  <class '__main__.Classy'>
    Out[42]: 16


Why?
----

Unlike static methods, class methods are quite common.

They have the advantage of being friendly to subclassing.

Consider this:

.. code-block:: ipython

    In [44]: class SubClassy(Classy):
       ....:     x = 3
       ....:

    In [45]: SubClassy.a_class_method(4)
    in a class method:  <class '__main__.SubClassy'>
    Out[45]: 64

``a_class_method`` is defined in the ``Classy`` class (see above).
And it prints the class that it is called on. But despite being defined in ``Classy``, it gets the ``SubClassy`` class object as the first parameter (``cls``).
So a classmethod will "do the right thing" when used in a subclass.

Alternate Constructors
-----------------------

Because of this friendliness to subclassing, class methods are often used to
build alternate constructors.

Consider the case of wanting to build a dictionary with a given iterable of
keys:

.. code-block:: ipython

    In [57]: d = dict([1,2,3])
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-57-50c56a77d95f> in <module>()
    ----> 1 d = dict([1,2,3])

    TypeError: cannot convert dictionary update sequence element #0 to a sequence


The stock constructor for a dictionary won't work this way. So the dict object
implements an alternate constructor that *can*.

.. code-block:: python

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
        If not specified, the value defaults to None.
        '''
        self = cls()
        for key in iterable:
            self[key] = value
        return self

(This is actually from the ``OrderedDict`` implementation in ``collections.py``).

See also ``datetime.datetime.now()``, etc....


Properties, Static Methods and Class Methods are powerful features of Python's OO model.

They are implemented using an underlying structure called *descriptors*

`Here is a low level look`_ at how the descriptor protocol works.

The cool part is that this mechanism is available to you, the programmer, as
well.

.. _Here is a low level look: https://docs.python.org/2/howto/descriptor.html


For the Circle Excercise: use a class method to make an alternate constructor that takes the diameter instead.

Ultimately, make a subclass of ``Circle``, called ``Sphere``. Check and see if the ``.from_diameter`` alternate consructor still works!



