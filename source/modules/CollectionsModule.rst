.. _collections_module:

######################
The Collections Module
######################

Python has a very complete set of built in standard types that support most programming tasks. These include strings and numbers, and also types that can be used to hold other objects -- or "collection" types.

* tuples
* lists
* dictionaries

You can get pretty darn far with just these basic types -- but some problems require (or could be helped by) more complex collection types.

This was recognised by the Python development team, so a number of genreally useful collection types are provided in the collections module.

The collections module
----------------------

The first step is to see what's there by looking at the documentation:

https://docs.python.org/3/library/collections.html

You can see a pretty nice list of options (kind of in order of usefulness)

* ``namedtuple()``: factory function for creating tuple subclasses with named fields
* ``deque``: list-like container with fast appends and pops on either end
* ``Counter``: dict subclass for counting hashable objects
* ``OrderedDict``: dict subclass that remembers the order entries were added
* ``defaultdict``: dict subclass that calls a factory function to supply missing values
* ``ChainMap``: dict-like class for creating a single view of multiple mappings

These are just the regular builtin types, but in a form that they can be subclassed -- to make your own custom version.

* ``UserDict``: wrapper around dictionary objects for easier dict subclassing
* ``UserList``: wrapper around list objects for easier list subclassing
* ``UserString``: wrapper around string objects for easier string subclassing

To get an idea what these all are, read the docs, or a nice overview Python Module of the Week:

https://pymotw.com/3/collections/

Using the collection types
--------------------------

To use these special types, they must be imported:

.. code-block:: ipython

  In [4]: from collections import defaultdict

Then you can use it -- creating a ``defaultdict`` with a empty list as a default:

.. code-block:: ipython

    In [8]: dd = defaultdict(list)

    In [9]: dd['this'].append(23)

    In [10]: dd
    Out[10]: defaultdict(list, {'this': [23]})

    In [11]: dd['this'].append(4)

    In [12]: dd['this'].append(4)

    In [13]: dd
    Out[13]: defaultdict(list, {'this': [23, 4, 4]})

    In [14]: dd['that'].append(4)

And you'll get a dict that will automatically put an empty list in when the key isn't there yet. Kind of a handy replacement from having to call ``dict.setdefault`` each time.

Similarly for the others.

Take a bit of time to try them out -- you may find them really useful.





