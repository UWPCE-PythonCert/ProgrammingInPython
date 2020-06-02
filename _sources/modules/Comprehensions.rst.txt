.. _comprehensions:

##############
Comprehensions
##############

**A bit of functional programming.**


List Comprehensions
-------------------

The concept of "functional programming" is clearly defined in some contexts, but is also used in a less strict sense. Python is **not** a functional language in the strict sense, but it does support a number of functional paradigms.

In general, code is considered "Pythonic" that uses functional paradigms where they are natural, but not when they have to be forced in.

We will cover functional programming concepts more clearly later in the program, but for now, we'll talk about the syntax for a common functional paradigm: applying an expression to all the members of a sequence to produce another sequence.

Consider this common ``for`` loop structure:

.. code-block:: python

    new_list = []
    for variable in a_list:
        new_list.append(expression_with_variable))

This is such a common pattern that python added syntax to directly support it. This syntax is known as "comprehensions". The most common of which is a list comprehension, used to build up a new list. There are a couple others, which we will get too later, but they all share a similar structure.

The above structure can be expressed with a single line using a "list comprehension" like so:

.. code-block:: python

    new_list = [expression_with_variable for variable in a_list]

Nice and clear and compact, and the use of the "list" brackets (``[...]``) makes it clear you are making a list.

Recall what an expression is in Python: a bit of code (names and operators) that evaluates to a value. So in the beginning of a comprehension, you can put anything that evaluates to a value -- and that value is what gets added to the new list.
This can be a simple (or complex) math operation: ``x * 3``, or a function or method call: ``a_string.upper()``, ``int(x)``, etc.
But it can not contain any statements: code that does not return a value, such as assignment (``x = 5``), or ``for`` loops, or ``if`` blocks.


Nested Loops
............

What about nested for loops?  Sometimes you need to build up a list by looping over two sequences like so:

.. code-block:: python

    new_list = []
    for var in a_list:
        for var2 in a_list2:
            new_list.append(expression_with_var_and_var2)

This can also be expressed with a comprehension in one line:

.. code-block:: python

    new_list =  [expression_with_var_and_var2 for var in a_list for var2 in a_list2]

But the two lists are not looped through in parallel. Rather, you get all combinations of the two lists -- Sometimes called the "outer product".

For example:

.. code-block:: ipython

    In [33]: list1 = [1, 2, 3]

    In [34]: list2 = [4, 5]

    In [35]: [(a, b) for a in list1 for b in list2]
    Out[35]: [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

Note that it makes every combination of the two input lists, and thus will be ``len(list1) * len(list2)`` in size. And there is no reason for them to be the same size.

zip() with comprehensions
.........................

If you want them paired up instead, you can use ``zip()``:

.. code-block:: ipython

    In [31]: [(a, b) for a, b in zip(list1, list2)]
    Out[31]: [(1, 4), (2, 5)]


Comprehensions and map()
........................

Comprehensions are another way of expressing the "map" pattern from functional programming.

Python does have a ``map()`` function, which pre-dates comprehensions. But it does much of the same things -- and most folks think comprehensions are the more "Pythonic" way to do it. And there is nothing that can be expressed with ``map()`` that cannot be done with a comprehension. If you are not familiar with ``map()``, you can safely skip this, but if you are:

.. code-block:: python

    map(a_function, an_iterable)

is the same as:

.. code-block:: python

    [a_function(item), for item in an_iterable]

In this case, the comprehension is a tad wordier than ``map()``.  But comprehensions really shine when you don't already have a handy function to pass to map:

.. code-block:: python

    [x**2 for x in an_iterable]

To use ``map()``, you need a function:

.. code-block:: python

    def square(x):
        return x**2

    map(square, an_iterable)

There are shortcuts of course, including ``lambda`` (stay tuned for more about that):

.. code-block:: python

    map(lambda x: x**2, an_iterable)

But is that easier to read or write?


What about filter?
..................

"filtering" is another functional concept: building a new list with only *some* of the elements -- "filtering" out the ones you don't want. Python has a ``filter()`` function, also pre-dating comprehensions, but you can do it with a comprehension as well, and it does the application of the expression and the filtering in one construct, rather than having to nest ``map`` and ``filter`` calls.

This supports the common case of having a conditional in the loop:

.. code-block:: python

    new_list = []
    for variable in a_list:
        if something_is_true:
            new_list.append(expression)

This kind of "filtering" loop can be achieved by adding a conditional to the comprehension:

.. code-block:: python

    new_list = [expr for var in a_list if something_is_true]

This is expressing the "filter" pattern and the "map" pattern at the same time -- one reason I like the comprehension syntax so much.


.. rubric:: Examples:

.. code-block:: ipython

    In [341]: [x**2 for x in range(3)]
    Out[341]: [0, 1, 4]

    In [342]: [x+y for x in range(3) for y in range(5,7)]
    Out[342]: [5, 6, 6, 7, 7, 8]

    In [343]: [x*2 for x in range(6) if not x%2]
    Out[343]: [0, 4, 8]


Get creative....

How do I see all the built in Exceptions?

.. code-block:: python

    [name for name in dir(__builtin__) if "Error" in name]
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BufferError',
     'EOFError',
     ....

Note that the last one was only filtering (``if "Error" in name``), without applying any expression to the items (``name for name``).


Set Comprehensions
------------------

You can do a similar thing with sets, as well:

.. code-block:: python

    new_set = {expression_with_variable for variable in a_sequence}

The curly brackets (``{...}``) indicate a set.

This results in the same set as this for loop:

.. code-block:: python

    new_set = set()
    for variable in a_sequence:
        new_set.add(expression_with_variable)

or, indeed, the same as passing a list comp to ``set()``.

.. code-block:: python

    new_set = set([expression_with_variable for variable in a_sequence])


**Example:** Finding all the vowels in a string...

.. code-block:: ipython

    In [19]: s = "a not very long string"

    In [20]: vowels = set('aeiou')

    In [21]: { l for l in s if l in vowels }
    Out[21]: {'a', 'e', 'i', 'o'}

.. note::

  Why did I use ``set('aeiou')`` rather than just ``'aeiou'`` ? ... ``in`` works with strings as well, but is it efficient?


Dict Comprehensions
-------------------

You can also build up a dictionary with a comprehension:

.. code-block:: python

    new_dict = {key: value for variable in a_sequence}


Which is the same as this for loop:

.. code-block:: python

    new_dict = {}
    for key in a_list:
        new_dict[key] = value

A dict comprehension also uses curly brackets like the set comprehension -- Python knows it's a dict comprehension due to the ``key: value`` construct.

**Example:**

.. code-block:: ipython

    In [22]: { i: "this_%i"%i for i in range(5) }
    Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
              3: 'this_3', 4: 'this_4'}


A bit of History:
.................

dict comps are not as useful as they used to be, now that we have the ``dict()``  constructor.

In the early days of Python the only way to create a dict was with a literal::

  a_dict = {}  # an empty dict

or a dict that was already populated with a bunch of data.

If you had a bunch of data in some other form, like a couple of lists, you'd need to write a loop to fill it in:

.. code-block:: ipython

    In [1]: names = ["fred", "john", "mary"]

    In [2]: ids = [1, 2, 3]

    In [4]: d = {}

    In [5]: for id, name in zip(names, ids):
       ...:     d[id] = name
       ...:

    In [6]: d
    Out[6]: {'fred': 1, 'john': 2, 'mary': 3}

now, with dict comps, you can do:

.. code-block:: ipython

    In [9]: d = {id: name for id, name in zip(ids, names)}

    In [10]: d
    Out[10]: {1: 'fred', 2: 'john', 3: 'mary'}

But there is also a ``dict()`` constructor (actually the type object for dict):

.. code-block:: ipython

    In [13]: dict?
    Init signature: dict(self, /, *args, **kwargs)
    Docstring:
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    Type:           type

``dict()`` can take different types of arguments, and will do something different with each one.

The first option (no argument) is an empty dict -- simple enough.

The option makes a dict from the contents of another dict or similar object (called a "mapping").

The options is of interest here -- it makes a dict from an iterable of key, value pairs -- exactly what ``zip()`` gives you.

So we can create a dict from data like so:

.. code-block:: ipython

    In [14]: d = dict(zip(ids, names))

    In [15]: d
    Out[15]: {1: 'fred', 2: 'john', 3: 'mary'}

Which is more compact, and arguably more clear, than the dict comprehension.

dict comps are still nice if you need to filter the results, though:

.. code-block:: ipython

    In [16]: d = {id: name for id, name in zip(ids, names) if name != 'mary'}

    In [17]: d
    Out[17]: {1: 'fred', 2: 'john'}


Generator Comprehensions
------------------------

There is yet another type of comprehension: generator comprehensions, technically known as "generator expressions". They are very much like a list comprehension, except that they evaluate to a lazy-evaluated "iterable", rather than a list. That is, they *generate* the items on the fly.

This is useful, because we often create a comprehension simply to loop over it right away:

.. code-block:: python

    for x in [y**2 for y in a_sequence]:
        outfile.write(f"The number is: {x}")

In this case, the list comprehension: ``[y**2 for y in a_sequence]`` iterates over ``a_sequence``, computes the square of each item, and creates a whole new list with the new values.
All this, just so it can be iterated over again right away. If the original sequence is large (or is itself a lazy-evaluated iterable), then the step of creating the extra list can be expensive and unnecessary.

Generator comprehensions, on the other hand, create an iterable that evaluates the items as they are iterated over, rather than all at once ahead of time -- so the entire collection is never stored.

The syntax for a generator comprehension is the same as a list comp, except it uses regular parentheses::

  (y**2 for y in a_sequence)

So what does that evaluate to? A list comp evaluates to a list:

.. code-block:: ipython

    In [1]: l = [x**2 for x in range(4)]

    In [2]: l
    Out[2]: [0, 1, 4, 9]

    In [3]: type(l)
    Out[3]: list

A generator comp evaluates to a generator:

.. code-block:: ipython

    In [4]: g = (x**2 for x in range(4))

    In [5]: g
    Out[5]: <generator object <genexpr> at 0x102bbed00>

    In [6]: type(g)
    Out[6]: generator

A generator is an object that can be iterated over with a for loop, and it will return the values as they are asked for:

.. code-block:: ipython

    In [7]: for i in g:
       ...:     print(i)
       ...:
    0
    1
    4
    9

You will learn more about generators and other ways to make them in future lessons.

Let's use a little function to make this clear:

.. code-block:: ipython

    In [8]: def test(x):
       ...:     print("test called with: ", x)
       ...:     return x ** 2

It simply returns the square of the passed-in value, but prints it as it does so, so we can see when it is called.

.. note::
  Having a "print" in a function is a example of a "side effect" -- something that is an effect of the function being called that is not reflected in the return value of that function.
  As a rule, it's not a good idea to use functions with side effects in comprehensions. We're only doing it here as a debugging aid -- so we can clearly see when the function is being called.

If we use it in a list comp:

.. code-block:: ipython

    In [10]: [test(x) for x in range(3)]
    test called with:  0
    test called with:  1
    test called with:  2
    Out[10]: [0, 1, 4]

We see that ``test()`` gets called for all the values, and then a list is returned with all the results.
But if we use it in a generator comprehension:

.. code-block:: ipython

    In [11]: g = (test(x) for x in range(3))

Nothing gets printed (the function has not been called) until you loop through it:

.. code-block:: ipython

    In [16]: for i in g:
        ...:     print(i)
        ...:
    test called with:  0
    0
    test called with:  1
    1
    test called with:  2
    4

You can see that ``test()`` is getting called for each item *as* the loop is run.

You usually don't assign a generator expression to a variable, but rather, loop through it right away:

.. code-block:: ipython

    In [17]: for i in (test(x) for x in range(3)):
        ...:     print(i)
        ...:
    test called with:  0
    0
    test called with:  1
    1
    test called with:  2
    4

When to Use What
................

It's pretty simple:

If you need a list (or a set or dict) for further work, then use a list comp.

If you are going to immediately loop through the items created by the comprehension, use a generator comprehension.

.. note::

  The "official" term is "generator expression" -- that is what you will see in the Python docs, and a lot of online discussions. I've used the term "generator comprehension" here to better make clear the association with list comprehensions.

References
----------

This is a nice intro to comprehensions from Trey Hunner:

https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

Once you've got the hang of it, you may want to read this so you don't overdo it :-)

https://treyhunner.com/2019/03/abusing-and-overusing-list-comprehensions-in-python/

Trey writes a lot of good stuff -- I recommend browsing his site.
