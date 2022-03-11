.. _decorators:

##########
Decorators
##########

.. NOTE: bring over some of the good stuff from the Py300 version

**A Short Reminder**


Functions are things that generate values based on input (arguments).

In Python, functions are first-class objects.

This means that you can bind names to them, pass them around, etc., just like
other objects.

Because of this fact, you can write functions that take functions as
arguments and/or return functions as values:

.. code-block:: python

    def substitute(a_function):
        def new_function(*args, **kwargs):
            return "I'm not that other function"
        return new_function


A Definition
------------

There are many things you can do with a simple pattern like this one.
So many, that we give it a special name:

**Decorator**

    "A decorator is a function that takes a function as an argument and
    returns a function as a return value."

    That's nice and all, but why is that useful?

An Example
----------

Imagine you are trying to debug a module with a number of functions like this one:

.. code-block:: python

    def add(a, b):
        return a + b

You want to see when each function is called, with what arguments and
with what result. So you rewrite each function as follows:

.. code-block:: python

    def add(a, b):
        print("Function 'add' called with args: {}, {}".format(a, b) )
        result = a + b
        print("\tResult --> {}".format(result))
        return result


That's not particularly nice, especially if you have lots of functions
in your module.

Now imagine we defined the following, more generic *decorator*:

.. code-block:: python

    def logged_func(func):
        def logged(*args, **kwargs):
            print("Function {} called".format(func.__name__))
            if args:
                print("\twith args: {}".format(args))
            if kwargs:
                print("\twith kwargs: {}".format(kwargs))
            result = func(*args, **kwargs)
            print("\t Result --> {}".format(result))
            return result
        return logged


We could then make logging versions of our module functions:

.. code-block:: python

    logging_add = logged_func(add)

Then, where we want to see the results, we can use the logged version:

.. code-block:: ipython

    In [37]: logging_add(3, 4)
    Function 'add' called
        with args: (3, 4)
         Result --> 7
    Out[37]: 7


This is nice, but we have to call the new function wherever we originally
had the old one.

It'd be nicer if we could just call the old function and have it log.

Remembering that you can easily rebind symbols in Python using *assignment
statements* leads you to this form:

.. code-block:: python

    def logged_func(func):
        # implemented above

    def add(a, b):
        return a + b
    add = logged_func(add)

And now you can simply use the code you've already written and calls to
``add`` will be logged:

.. code-block:: ipython

    In [41]: add(3, 4)
    Function 'add' called
        with args: (3, 4)
         Result --> 7
    Out[41]: 7

Syntax
------

Rebinding the name of a function to the result of calling a decorator on that
function is called **decoration**.

Because this is so common, Python provides a special operator to perform it
more *declaratively*: the ``@`` operator -- I told you I'd eventually explain what was going on under the hood with
that weird `@` symbol.

This is rebinding the name:

.. code-block:: python

    def add(a, b):
        return a + b
    add = logged_func(add)

And this means exactly the same thing, with the decoration syntax:

.. code-block:: python

    @logged_func
    def add(a, b):
        return a + b


The declarative form (called a decorator expression) is far more common,
but both have the identical result, and can be used interchangeably.

Here's another simple example. First we define a decorator -- note that it is a function that takes an argument, and returns a function:

.. code-block:: python

    In [1]: def my_decorator(func):
       ...:      def inner():
       ...:          print('running inner')
       ...:      return inner
       ...:

And we can apply it with the regular calling and rebinding syntax:

.. code-block:: ipython

    In [2]: def other_func():
       ...:     print('running other_func')

    In [3]: other_func()
    running other_func

    In [4]: other_func = my_decorator(other_func)

    In [5]: other_func()
    In [5]: running inner

    In [6]: other_func
    Out[6]: <function __main__.my_decorator.<locals>.inner>

Notice that ``other_func`` is now the "inner" function, which lives in the "my_decorator" namespace...

And this is the same with the decoration syntax:

.. code-block:: python

    In [7]: @my_decorator
       ...: def other_func():
       ...:      print('running other_func')
       ...:

    In [8]: other_func()
    running inner

    In [9]: other_func
    Out[9]: <function __main__.my_decorator.<locals>.inner>

Notice that ``other_func`` is the "inner" function here as well.

Decorators have the power to replace the decorated function with a different one!

And they do it with compact, declarative syntax that has the decoration right at the top where the function is defined.


Callables
---------

Our original definition of a *decorator* was nice and simple, but a tiny bit incomplete.

In reality, decorators can be used with anything that is *callable*.

Remember that a *callable* is a function, a class object, a method in a class, or a instance of a class that implements the ``__call__`` special method.

So in fact the definition should be updated as follows:

  "A decorator is a callable that takes a callable as an argument and returns a callable as a return value."


An Example
----------

Consider a decorator that would save the results of calling an expensive
function with given arguments so that it would not have to be re-computed with the same input (which is known an memoizing...).

.. code-block:: python

    class Memoize:
        """
        memoize decorator from avinash.vora
        http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
        """
        def __init__(self, function):  # runs when memoize class is called
            self.function = function
            self.memoized = {}

        def __call__(self, *args):  # runs when memoize instance is called
            try:
                return self.memoized[args]
            except KeyError:
                self.memoized[args] = self.function(*args)
                return self.memoized[args]


Let's try that out with a potentially expensive function:

.. code-block:: ipython

    In [56]: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in range(n))
       ....:

    In [57]: sum2x(10000000)
    Out[57]: 99999990000000

    In [58]: sum2x(10000000)
    Out[58]: 99999990000000

Run that code yourself and see how much faster it returns the second time.

It's nice to see that in action, but what if we want to know *exactly*
how much difference it made?


Nested Decorators
-----------------

You can stack decorator expressions.  The result is like calling each
decorator in order, from bottom to top:

.. code-block:: python

    @decorator_two
    @decorator_one
    def func(x):
        pass

    # is exactly equal to:
    def func(x):
        pass
    func = decorator_two(decorator_one(func))


Let's define another decorator that will time how long a given call takes:

.. code-block:: python

    import time
    def timed_func(func):
        def timed(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print("time expired: {}".format(elapsed))
            return result
        return timed


And now we can use this new decorator stacked along with our memoizing
decorator:

.. code-block:: ipython

    In [71]: @timed_func
       ....: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in range(n))
    In [72]: sum2x(10000000)
    time expired: 0.997071027756
    Out[72]: 99999990000000
    In [73]: sum2x(10000000)
    time expired: 4.05311584473e-06
    Out[73]: 99999990000000


Parameterized Decorators
------------------------

The purpose of the outer function in the decorator is to receive the function to be decorated, adding anything to scope that should be there before the decorated function is called.

The inner function runs the function being decorated, so its inputs are the same as the function being decorated.

How do we add more input parameters to our decorator? Like this example from Django:

.. code-block:: python

   @register.filter(name='cut')
   def cut(value, arg):
       return value.replace(arg, '')


Add yet another function in scope:

.. code-block:: python

    def decorator(arg1, arg2):
        def real_decorator(function):
            def wrapper(*args, **kwargs):
                print("Congratulations. You decorated a function that does
                       something with {} and {}".format(arg1, arg2))
                function(*args, **kwargs)
            return wrapper
        return real_decorator


    @decorator("arg1", "arg2")
    def print_args(*args):
        for arg in args:
            print(arg)


Last example from: http://scottlobdell.me/2015/04/decorators-arguments-python/


Examples from the Standard Library
----------------------------------

It's going to be a lot more common for you to use pre-defined decorators than for you to be writing your own.

We've seen a few already:

For example, ``@staticmethod`` and ``@classmethod`` can also be used as simple
callables, without the nifty decorator expression:

.. code-block:: python

    class C:
        @staticmethod
        def add(a, b):
            return a + b

Is exactly the same as:

.. code-block:: python

    class C:
        def add(a, b):
            return a + b
        add = staticmethod(add)

Note that the "``def``" binds the name ``add``, then the next line
rebinds it.

[Note that this is exactly how you defined a ``staticmethod`` before the decoration syntax was added in python 2.4]

The ``classmethod()`` builtin can do the same thing:

.. code-block:: python

    # in declarative style
    class C:
        @classmethod
        def from_iterable(cls, seq):
            # method body

    # in imperative style:
    class C:
        def from_iterable(cls, seq):
            # method body
        from_iterable = classmethod(from_iterable)


property()
-----------

Remember the ``property()`` builtin?

Perhaps most commonly, you'll see the ``property()`` builtin used this way.

Previously, we saw this code:

.. code-block:: python

    class C:
        def __init__(self):
            self._x = None
        @property
        def x(self):
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
        @x.deleter
        def x(self):
            del self._x


But this could also be accomplished like so:

.. code-block:: python

    class C:
        def __init__(self):
            self._x = None
        def getx(self):
            return self._x
        def setx(self, value):
            self._x = value
        def delx(self):
            del self._x
        x = property(getx, setx, delx,
                     "I'm the 'x' property.")


:download:`property_ugly.py <../examples/decorators/property_ugly.py>`


Note that in this case, the decorator object returned by the property decorator
itself implements additional decorators as attributes on the returned method
object. So you could actually do this:


.. code-block:: python

    class C:
        def __init__(self):
            self._x = None
        def x(self):
            return self._x
        x = property(x)
        def _set_x(self, value):
            self._x = value
        x = x.setter(_set_x)
        def _del_x(self):
            del self._x
        x = x.deleter(_del_x)

But that's getting really ugly! Makes you appreciate the ``@``, doesn't it?


Import Time vs. Run Time
------------------------

Decorators are run at import time. Run this code and see what happens when:

:download:`play_with_imports.py <../examples/decorators/play_with_imports.py>`


What if my decorated function uses unknown inputs?
--------------------------------------------------

If you don't know what parameters the decorated function will take (and you usually don't), you want to make sure the inner function that you are replacing the decorated function with takes ANY arguments, and passes them on to the decorated function.

``*args, **kwargs`` is your friend here:

A decorator that wraps an html `<p>` tag around the output of any decorated function.

.. code-block:: python

    def p_decorate(func):
        def func_wrapper(*args, **kwargs):
            return "<p>{0}</p>".format(func(*args, **kwargs))
        return func_wrapper


    @p_decorate
    def get_fullname(first_name, last_name):
        return f"{first_name} {last_name}"

    In [124]: get_fullname('Chris', 'Barker')
    Out[124]: '<p>Chris Barker</p>'


Functools Library
-----------------

Single dispatch:
 - create many functions that do the same sort of thing, but based on type
 - decorator determines type, and decides which function is run

https://docs.python.org/3/library/functools.html#functools.singledispatch

Memoize decorator we created earlier is in Functools:

https://docs.python.org/3/library/functools.html#functools.lru_cache

LAB
===

A little excercise. See the "p_decorate" decorator defined above -- it wrapped an html <p> tag (paragraph) around the results of any function that returned a string.

Can you make a version that will wrap any other tag -- specified as a parameter of the decorator itself? For example:

.. code-block:: ipython

    @add_tag('p')
    def get_fullname(first_name, last_name):
        return f"{first_name} {last_name}"

    In [124]: get_fullname('Chris', 'Barker')
    Out[124]: '<p>Chris Barker</p>'

Just like the ``p_decorate`` one above.

But:

.. code-block:: ipython

    @add_tag('div')
    def get_fullname(first_name, last_name):
        return f"{first_name} {last_name}"

    In [124]: get_fullname('Chris', 'Barker')
    Out[124]: '<div>Chris Barker</div>'

and you could pass any tag in.

This can be accomplished either with a closure --nesting another level of functions in the decorator, or with a callable class, like the memoize example. Maybe try both, and decide which you like better.


Further Reading:
----------------

*Fluent Python* by Luciano Ramalho, Chapter 7.

Another good overview:

https://dbader.org/blog/python-decorators


