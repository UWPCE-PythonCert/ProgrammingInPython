.. _installing_python:


================================
Installing Python and core tools
================================


The following is the recommended setup for the UWPCE Python Certificate Program. It is not necessary to have exactly this same setup, but if you choose to use a different setup, we will be less able to support you if you need help.

Minimal Setup
=============

Although it is OK to use different tools, there are some requirements to successfully do the work the program requires:

#. cPython version 3.8.*
#. A way to edit Python files (Programmers Text Editor)
#. A way to run your code -- command line, IDE, etc.
#. A way to use the "git" source code version control system

You can be successful in the program as long as you have the above. If you don't already have a setup that fulfills those requirements -- read on.

Platforms
---------

Python is a very platform independent system, it can run on all major operating systems, including micro controllers even. It is most commonly used in production on Windows, Linux or OS-X systems.

For this program, we feel it is best for students to work in an environment in which they are comfortable, and which they will ultimately use to do production work.

We have included instructions for Windows, Linux and OS-X systems -- any of these are fine.

Python Itself
-------------

Python is a "byte compiled, interpreted" language. What this means to you is that you need a Python interpreter to run your Python code. It also means that that is all you need -- write some code, and run it with Python. That's it.

There are a number of different Python interpreters (or run-time environments) available:

- cPython
- PyPy
- Jython
- Iron Python
- MicroPython

These each have their own special uses. For example, for interaction with the Java VM or Microsoft CLR, or running on micro controllers. But most production Python is run with the cPython interpreter, and most people mean cPython when they say "Python".

For this program, you will need cPython version 3.8, installed and running so that when you type "python" at your command line, it starts up.

cPython itself is available from a number of sources, or "distributions". We recommend the version available from `python.org`.

Python is also available as part of the Anaconda data analysis environment, as well as a few other sources. These Python distributions will work fine for this class, but when we get to advanced topics like virtual environments, there are some differences -- and you will be responsible for adapting to these differences.


Your Development Environment
============================

There are four elements to your environment when working with Python:

* The Command Line
* The Interpreter
* The Editor
* The source code version control system

Some folks use an Integrated Development Environment (IDE), which combines some or all of these functions. For this class, we don't recommend using an IDE, because while it can make some things easier, it can also hide things that will be good for you to understand. But it's your call -- you should use tools you are comfortable with.

Minimal Requirements
--------------------

In order to be productive in this program, you need to be able to do the following:

* Manipulate files and write and save Python code in files.
  You really, really want a "real" programmer's editor (not Notepad!) for this.

* Run your code with Python 3.8 or higher

* Run the iPython interactive interpreter

* Install new packages with pip

* Use the git source code management system (with GitHub Classroom)

If you are not set up and comfortable with doing all that, read and follow these instructions:

:ref:`installing_python`

Then come back and follow the rest of this review.


The Command Line (CLI)
======================

Having some familiarity with the command line is important

Familiarity with basic use of the command line is a prerequisite for the program, so we won't cover this much in class. If you are not comfortable with the command line, please bone up on your own.

We have some resources here: :ref:`command_line_basics`

We suggest running through the **CLI** tutorial at "learn code the hard way":

`Command Line Crash Course <https://learnpythonthehardway.org/book/appendixa.html>`_

Or, for Linux and OS-X users:

`Linux command line for you and me! <https://lym.readthedocs.io/en/latest/>`_


Windows:
--------

Most of the demos in lessons will be done using the "bash" command line shell on OS-X. This is identical to the bash shell on Linux.

Windows provides the "DOS" command line, which is OK, but pretty old and limited, or "Power Shell" -- a more modern, powerful, flexible command shell.

If you are comfortable with either of these -- go for it.

If not, you can use the "git Bash" shell -- which is much like the bash shell
on OS-X and Linux: :ref:`git_bash`

Or, on Windows 10, look into the "bash shell for Windows" otherwise known as the "Linux subsystem for Windows" - - more info here: :ref:`windows_bash`

OS-X
----

OS-X comes out of the box with a bash command line. You can access it by running the "Terminal" application, which you can find under:

Applications => Utilities => Terminal.app

Drag and Drop it into the dock for easy access.

The Terminal app can be interfaced with the Finder, making it easy to open it up with the working dir set to the current folder in the finder:

On The Mac, you may have a "New Terminal at Folder" right-click (or command click -- "secondary click") menu item already -- try it! If not, you can turn it on by following these instructions:

   Head into System Preferences and select Keyboard => Shortcuts => Services. Find "New Terminal at Folder" in the settings and click the box. Now, when you're in Finder, just right-click a folder and you're shown the open to open Terminal. When you do, it'll start right in the folder you're in.

See: `launch an OS-X terminal in a folder <https://lifehacker.com/launch-an-os-x-terminal-window-from-a-specific-folder-1466745514>`_

for more detail.

Linux
-----

Whether you use the KDE or GNOME Desktop (or anything else), there should be a way to open a shell from the file manager. Find it, it's very handy.


The Python Interpreter
======================

If you haven't already, install everything you need following these instructions:
:ref:`setup_details`

Python comes with a built-in interpreter.

You see it when you type ``python`` at the command line:

.. code-block:: bash

  $ python
  Python 3.8.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

That last thing you see, ``>>>`` is the "Python prompt".

This is where you can type code.


Python in the Interpreter
-------------------------

Try it out:

.. code-block:: python

    >>> print("hello world!")
    hello world!
    >>> 4 + 5
    9
    >>> 2 ** 8 - 1
    255
    >>> print ("one string" + " plus another")
    one string plus another
    >>>

To get out of the interpreter, you can type::

  exit()

Or hit `ctrl+D` on Linux and OS-X or `ctrl+Z` On Windows.


Tools in the Interpreter
------------------------

When you are in the interpreter, there are a number of tools available to
you.

There is a help system:

.. code-block:: python

    >>> help(str)
    Help on class str in module __builtin__:

    class str(basestring)
     |  str(object='') -> string
     |
     |  Return a nice string representation of the object.
     |  If the argument is a string, the return value is the same object.
     ...

You can type ``q`` to exit the help viewer.


You can also use the ``dir`` builtin to find out about the attributes of a
given object:

.. code-block:: python

    >>> bob = "this is a string"
    >>> dir(bob)
    ['__add__', '__class__', '__contains__', '__delattr__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
     ...
     'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
     'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill']
    >>> help(bob.rpartition)

This allows you quite a bit of latitude in exploring what Python is.

Advanced Interpreters
---------------------

In addition to the built-in interpreter, there are several more advanced
interpreters available to you.

We'll be using one in this course called ``iPython``

Some information about iPython can be found here: :ref:`ipython_resources`

The Editor
==========

Typing code in an interpreter is great for exploring.

But for anything "real", you'll want to save the work you are doing in a more permanent fashion.

This is where an editor fits in.

.. _editor_for_python:

Text Editors Only
-----------------

Any good programmer's text editor will do.

MS Word is **not** a text editor.

Nor is *TextEdit* on a Mac.

``Notepad`` on Windows is a text editor -- but a poor one.

You need a real "Programmer's Text Editor"

A text editor saves only what it shows you, with no special formatting
characters hidden behind the scenes.

Minimum Requirements
--------------------

At a minimum, your editor should have:

* Syntax Colorization
* Automatic Indentation

In addition, great features to add include:

* Tab completion
* Code linting
* Jump-to-definition

Have an editor that does all this? Feel free to use it.

If not, we recommend "Sublime Text":

http://www.sublimetext.com/

:ref:`sublime_as_ide`

"Atom" is another good open source option.

https://atom.io/

:ref:`atom_as_ide`

"Visual Studio Code" is a relatively new cross platform offering from Microsoft -- a lot of folks seem to like it:

:ref:`vsc_as_ide`

And, of course, vim or Emacs on Linux, if you are familiar with one of those.


Why No Full IDE?
----------------

An IDE does not give you much that you can't get with a good editor plus a good interpreter.

An IDE often weighs a great deal.

Setting up IDEs to work with different projects can be challenging and time-consuming.

Particularly when you are first learning, you don't want too much done for you.


Why an IDE?
-----------

That said ...

You may want to go get the educational edition of PyCharm:

https://www.jetbrains.com/pycharm-edu/

Which a lot of people like a lot. 

VSCode from MS is apretty full featured IDE as well.

But do make sure, when you set up and IDE, that you know what its doing when you click "run", and that it is using the version of Python that you expect. (cPython 3.8 in this case)

Version Control System
======================

While not strictly necessary to develop code, it is a very, very, good idea to manage your code in a Version Control System:

https://en.wikipedia.org/wiki/Version_control

This is such a critical software development practice the we use it in the program for you to mange your projects and turn in assignments (via gitHub classroom), so that you can gain familiarity with the practice.

git
---

git (https://en.wikipedia.org/wiki/Git) is an open-source version control system that has become an industry standard -- very widely used in both commercial and open-source development.

We will be using git and the web service GitHub for collaboration in this program.

Make sure you are set up to use git on your machine. If you have using a command line client, you should be able to type::

  git --version

and get something like this as a response::

  git version 2.17.2 (Apple Git-81)

Am I ready to go?
=================

To see if you have Python ready to start class, try this:

:ref:`testing_your_setup`
