IPython Introduction
====================

You have installed `IPython`_.

IPython is an advanced Python interpreter that offers enhancements.

You can read more about it in the `official documentation`_.

Specifically, you'll want to pay attention to the information about

`Using IPython for Interactive Work`_.

.. _IPython: http://ipython.org
.. _official documentation: http://ipython.org/ipython-doc/stable/index.html
.. _Using IPython for Interactive Work: http://ipython.org/ipython-doc/stable/interactive/index.html

The very basics of IPython
--------------------------

IPython can do a lot for you, but for starters, here are the key pieces
you'll want to know:

Start it up

.. code-block:: bash

  $ ipython
  Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19)
  Type "copyright", "credits" or "license" for more information.

  IPython 4.0.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.


This is the stuff I use every day:

* command line recall:

  - hit the "up arrow" key
  - if you have typed a bit, it will find the last command that starts the same way.

* basic shell commands:

  - ``ls``, ``cd``, ``pwd``

* any shell command:

 - ``! the_shell_command``

* pasting from the clipboard:

  - ``%paste`` (this keeps whitespace cleaner for you)



* getting help:

  - ``something?``

* tab completion:

  - ``something.<tab>``

* running a python file:

  - ``run the_name_of_the_file.py``


That's it -- you can get a lot done with those.

