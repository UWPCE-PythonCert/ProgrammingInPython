.. _advanced_argument_passing:

#########################
Advanced Argument Passing
#########################

This is a very, very nifty Python feature -- it really lets you write dynamic programs.

Keyword arguments
=================

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [151]: def fun(x=0, y=0, z=0):
            print(x,y,z)
       .....:
    In [152]: fun(1,2,3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(z=3, y=2)
    0 2 3


A Common Idiom:
---------------

.. code-block: python

    def fun(x, y=None):
        if y is None:
            do_something_different
        go_on_here



Can set defaults to variables
-----------------------------

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4


Defaults are evaluated when the function is defined

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4
    In [159]: y = 6
    In [160]: fun()
    x is: 4

This is a **very** important point.


Function arguments in variables
-------------------------------

When a function is called, its arguments are really just:

* a tuple (positional arguments)
* a dict (keyword arguments)

.. code-block:: python

    def f(x, y, w=0, h=0):
        print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))

    position = (3,4)
    size = {'h': 10, 'w': 20}

    >>> f(*position, **size)
    position: 3, 4 -- shape: 20, 10


Function parameters in variables
--------------------------------

You can also pull the parameters out in the function as a tuple and a dict:

.. code-block:: ipython

    def f(*args, **kwargs):
        print("the positional arguments are:", args)
        print("the keyword arguments are:", kwargs)

    In [389]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the keyword arguments are: {'this': 5, 'that': 7}

This can be very powerful...

Passing a dict to str.format()
-------------------------------

Now that you know that keyword args are really a dict,
you know how this nifty trick works:

The string ``format()`` method takes keyword arguments:

.. code-block:: ipython

    In [24]: "My name is {first} {last}".format(last="Barker", first="Chris")
    Out[24]: 'My name is Chris Barker'

Build a dict of the keys and values:

.. code-block:: ipython

    In [25]: d = {"last":"Barker", "first":"Chris"}

And pass to ``format()`` with ``**``

.. code-block:: ipython

    In [26]: "My name is {first} {last}".format(**d)
    Out[26]: 'My name is Chris Barker'

Kinda handy for the dict lab, eh?

This:

.. code-block:: ipython

  print("{} is from {}, and he likes "
        "{} cake, {} fruit, {} salad, "
        "and {} pasta.".format(food_prefs["name"],
                               food_prefs["city"],
                               food_prefs["cake"],
                               food_prefs["fruit"],
                               food_prefs["salad"],
                               food_prefs["pasta"]))

Becomes:

.. code-block:: ipython

  print("{name} is from {city}, and he likes "
        "{cake} cake, {fruit} fruit, {salad} salad, "
        "and {pasta} pasta.".format(**food_prefs))

Note that this is particularity useful when the same value is used in multiple places in the format string.

.. _keyword_only_arguments:

Keyword Only Arguments
======================

The usual function signature looks something like:

.. code-block:: python

    def fun (pos1, pos2, key1='this', key2='that'):
        print(pos1, pos2, key1, key2)

In this case, we have two positional parameters and two keyword parameters.

But all four can be passed as either positional or keyword arguments:

.. code-block:: ipython

    In [21]: fun(1,2,3,4)
    1 2 3 4

    In [22]: fun(pos1=1, pos2=2, key1=3, key2=4)
    1 2 3 4

or out of order:

.. code-block:: ipython

    In [23]: fun(key1=1, pos2=2, pos1=3, key2=4)
    3 2 1 4

And the positional arguments are all required:

.. code-block:: ipython

    In [24]: fun(3)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-24-5ef8442810a5> in <module>()
    ----> 1 fun(3)

    TypeError: fun() missing 1 required positional argument: 'pos2'

**But:**  Notice that you can either have a required argument with no keyword, or an optional argument with a keyword (and a default). And keyword arguments can also be passed as positional arguments.

This was considered less than ideal -- with some APIs, you want to require a keyword be used -- and you may have a required argument that you want users to pass as a keyword (rather than positional) argument.

In Python 3 -- "keyword only" arguments were added:

https://www.python.org/dev/peps/pep-3102/

So you can do:

.. code-block:: python

    def fun (pos1, pos2, *, key1='this'):
        print(pos1, pos2, key1)

Now the user can only provide a value for key1 as a keyword argument. If they pass a third positional argument, it'll be an error:

.. code-block:: ipython

    In [26]: fun(1,2,3)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-26-057c5c08ae41> in <module>()
    ----> 1 fun(1,2,3)

    TypeError: fun() takes 2 positional arguments but 3 were given

So Python will not just move that third argument along for you. You need to use the keyword:

.. code-block:: ipython

    In [29]: fun(1,2, key1=3)
    1 2 3

But you can still let it be the default:

.. code-block:: ipython

    In [30]: fun(1,2)
    1 2 this

However, with keyword only arguments you can make it required by providing no default:

.. code-block:: python

    def fun(pos1, pos2, *, key1):
        print(pos1, pos2, key1)

.. code-block:: ipython

    In [32]: fun(1,2)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-32-0dfacfcc443e> in <module>()
    ----> 1 fun(1,2)

    TypeError: fun() missing 1 required keyword-only argument: 'key1'

So you HAVE to provide it, and you HAVE to provide it as a keyword argument.

.. code-block:: ipython

    In [34]: fun(1,2, key1='that')
    1 2 that

What about ``*args``?
---------------------

Asside from allowing keyword-only paramters with or without defaults, a key addition is that you can now have variable numbers of positional arguments, without them getting confused with the keyword arguments:

.. code-block:: python

    def fun (pos1, pos2, *args, key1='this'):
        print(pos1, pos2, args, key1)

.. code-block:: ipython

    In [36]: fun(1,2)
    1 2 () this

    In [37]: fun(1,2,3)
    1 2 (3,) this

Notice how the third argument did NOT get assigned to key1?

And you can pass any number in:

.. code-block:: ipython

    In [39]: fun(1,2,3,4,5,6,7, key1='that')
    1 2 (3, 4, 5, 6, 7) that

This is actually the primary motivation for the PEP -- it makes a cleaner separation of positional and keyword arguments.

So for ALL the features in one function:

.. code-block:: python

    def fun (pos1, pos2, *args, key1='this', **kwargs):
        print(pos1, pos2, args, key1, kwargs)

.. code-block:: ipython

    In [42]: fun(1,2,3,4, this='that', fred='bob')
    1 2 (3, 4) this {'this': 'that', 'fred': 'bob'}

or:

.. code-block:: ipython

    In [44]: args = (1,2,3,4)

    In [45]: kwargs = {'this':'that', 'fred':'bob'}

    In [46]: fun(*args, **kwargs)
    1 2 (3, 4) this {'this': 'that', 'fred': 'bob'}

Lots of Flexibility!!





