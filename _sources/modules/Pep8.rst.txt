:orphan:

.. _pep8:


########################
Coding Style and Linting
########################

**Readablity Counts**

It really is worth it to have consistently styled code!


pep-8
=====

Style Guide for Python

You should all be familiar with this by now -- but we're going to hammer it home anyway!

Defines a good baseline for your own local style guide

The 'rules' are just suggestions. From the document:

    *Most importantly: know when to be inconsistent -- sometimes the
    style guide just doesn't apply*

and:

    *A Foolish Consistency is the Hobgoblin of Little Minds*



Important pep8 Recommendations
------------------------------

Tabs or Spaces
..............

This one is pretty much non-negotiable:

-  https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces

-  Use 4 space indents. The tabs vs. spaces wars will likely never
   completely come to peaceful conclusion. But the Python community has
   standardized on 4 space indents. Unless you have compelling reasons
   not to, you should too.

-  Python 3 disallows mixing of tabs and spaces. With Python 2, you can
   run with the -tt flag which will force errors on mixed use of tabs
   and spaces.

-  Let your editor help you by having it insert 4 spaces for the tab
   key, turning on visible whitespace markers, and/or integrating a
   PEP-8 plugin

- If your editor doesn't do this right -- **Fix It**

Line Length
...........

-  https://www.python.org/dev/peps/pep-0008/#maximum-line-length

-  Maximum line length of 79 characters

-  This is an easy one to let run away early. If 79 characters is too
   short, find a line length your team can agree on and stick to it as
   specified in PEP-8 -- I like 95 characters or so.



Encoding
........

-  https://www.python.org/dev/peps/pep-0008/#source-file-encoding

-  The default encoding in Python 2 is ASCII, in Python 3 it is UTF-8.
   UTF-8 has become ubiquitous enough that you probably haven't noticed.
   But do check your editor at some point -- or if something weird happens.

-  If you insert a non encodable character in a string literal, the
   interpreter will throw a SyntaxError when it reaches it.

-  For py2, if you want to use non-ascii encoding, UTF-8 for example, insert

   ::

       # coding: utf-8

   near the top of the file.

Comparing to Singletons
.......................

-  When comparing with singletons such as None, use ``x is None``, not ``x == None``. `Why? <http://jaredgrubb.blogspot.com/2009/04/python-is-none-vs-none.html>`_ ( also ``x is True`` and ``x is False``)


Naming Conventions
------------------

-  variables, attributes, and modules names should be lowercase, with
   words separated by underscores

-  class names should be CamelCase, aka StudlyCaps

-  constants should be ALL CAPS


Argument Conventions
--------------------

-  Instance methods should have a first argument called self
-  Class methods should have a first argument called cls
-  There's nothing magic about these names. You don't have to use this
   convention, but not adopting it will likely confuse future readers

Imports
-------

-  `imports <https://www.python.org/dev/peps/pep-0008/#imports>`_
   should be near the top of the file

-  imports should be grouped in the following order, separated by a
   blank line:

   #. standard library imports
   #. related third party imports
   #. local application/library specific imports

-  avoid wildcard imports (``import *``) to keep the namespace clean for
   both humans and automated tools


Public and Non-public Class Members
-----------------------------------

Python does not have a mechanism for restricting access to a variable or method, but it does have culture and convention.

The default is public. This works for most things.

If you do not want people to change your attribute or method, and especially if you do not want people to depend on this attribute or method always remaining the same, make it private by using a single underscore in front.

``_my_private_method``

If you are particularly paranoid: A non-public attribute has two leading underscores and no trailing underscores and triggers Python's name mangling.

``__my_paranoid_method``

Continuing long lines
---------------------

PEP-8 is pretty flexible about how to continue long lines:

https://www.python.org/dev/peps/pep-0008/#indentation

But I'm kind of opinionated, so:

Lots of Arguments or Parameters:
................................

If your function defintion or call can fit on one line, great:

.. code-block:: python

  def fun(arg1, arg2, arg3=None):
     some_code

but if not:

.. code-block:: python

  def fun(arg1, arg2, arg3, arg4=None, kwargument="a_default", kwargument2="some other value", yet_another=something, **kwargs):
     some_code

Then you need to break it. You can break it after a few arguments, when you run out of space, but I find that very hard to read. So -- if they don't all fit on one line, put them each on their own line:

.. code-block:: python

  def fun(arg1,
          arg2,
          arg3,
          arg4=None,
          kwargument="a_default",
          kwargument2="some other value",
          yet_another=something,
          **kwargs
          ):
     some_code

Isn't that easier to read?

Tools to help
-------------

-  `pyflakes <https://pypi.python.org/pypi/pyflakes>`__ - searches for
   bugs, but without importing modules

-  `Pylint <http://www.pylint.org/>`__ - style guide, searches for bugs

-  `pycodestyle <https://pypi.python.org/pypi/pycodestyle>`__ - tests conformance to
   PEP-8

-  `flake8 <https://pypi.python.org/pypi/flake8>`__ combines pyflakes,
   pycodestyle, and mccabe, a code complexity analyzer


pylint
------

Interesting options:

::

    -d (msg ids), --disable=(msg ids)      Disable the messages identified in the messages table
    --generate-rcfile/--rcfile             Saves/restores a configuration

Poor code example:

:download:`listing1.py </examples/pep8/listing1.py>`

was adapted from `Doug Hellman <http://doughellmann.com/2008/03/01/static-code-analizers-for-python.html>`_

What can you spot as an error, bad practice, or poor style?

Now see what pylint listing1.py has to say:

.. code-block:: bash

    $ pip install pylint

    $ pylint listing1.py


pyflakes
--------

Doesn't check style, just checks for functional errors, but does not run code.

Now see what pyflakes listing1.py has to say

.. code-block:: bash

    $ pip install pyflakes

    $ pyflakes listing1.py

How much overlap with pylint?

pycodestyle
-----------

Used to be called "pep8" -- but Guido didn't like that it gave a tool apparent authority -- so they changed it.

Only checks style

Interesting options:

::

    --statistics         count errors and warnings
    --count              print total number of errors and warnings to standard error and set exit code to 1 if total is not null

Now see what pycodestyle listing1.py has to say

.. code-block:: bash

    $ pip install pycodestyle

    $ pycodestyle listing1.py

What's the overlap in pycodestyle's output versus the other two tools?

flake8
------

A tool which wraps pycodestyle, pyflakes, and mccabe

`mccabe <http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html>`_
is a "microtool" written by Ned Batchelder (author of coverage) for
assessing
`Cyclomatic Complexity <http://en.wikipedia.org/wiki/Cyclomatic_complexity>`__

Interesting options:

::

    --max-complexity=N    McCabe complexity threshold

Now see what flake8 listing1.py has to say

.. code-block:: bash

    $ pip install pycodestyle

    $ pycodestyle listing1.py

What's the overlap in flake8 output versus the other tools?

Give them a try on your own code -- mailroom?

skipping particular lines
-------------------------

Each of the tools has a way to mark particular lines to be ignored.

For instance, flake8 has the ``# noqa`` marker. It's a comment as far as Python is concerned, but flake8 will skip that line if you mark it that way:

.. code-block:: python

  def functionName(self, int):
      local = 5 + 5  # noqa
      module_variable = 5*5
      return module_variable

This can be very nice to make the linter in your editor stop bugging you, and even nicer if you have an automated linter running -- like on a CI system.

Analyzing a large codebase in the wild
---------------------------------------

It can be instructive to see what happens if you run these tools on a large established code base...

.. code-block:: bash

  $ pip install django

    cd /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages

    flake8 django

    pylint django

Code Analysis Tool Battle Royale
--------------------------------

Try this!

.. code-block:: bash

    $ pylint flake8
    $ flake8 pylint

Analysis Tool Summary
---------------------

-  There is no magic bullet that guarantees functional, beautiful code
-  Some classes of programming errors can be found before runtime
-  With the PEP-8 tools, it is easy to let rules such as line length
   slip by
-  It's up to you to determine your thresholds

Conclusion:
-----------

Personally, I use flake8 -- it gets most of it for me. Though a run with pylint isn't a bad idea once in a while....

Also -- if you set up your editor with a linter -- you'll be encouraged to fix it a bit at a time as you write -- much better way to go.

Pythonic Style
==============

Good "Pythonic" style goes beyond style guides and things linters can figure out for you.

The `Hitchhiker's Guide to Python: Code Style <http://docs.python-guide.org/en/latest/writing/style/>`_ is a good read that gets into a nice level of detail.


