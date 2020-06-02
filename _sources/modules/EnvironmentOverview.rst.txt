############################################
Introduction to your Programming Environment
############################################

This program is a course of instruction in developing with the Python programming language.

Python is a language with multiple implementations, and many different ways to edit and run code.

One's development environment is a personal thing. What is most productive for you depends on what platform you use, how you like to work, what the people you work with are using, etc. It is a very personal choice.

Each of you starting this program comes with a different background and experience. So we do not require that you use a particular development environment. Indeed, each of the instructors in the program uses their own tools and approach.

However, there are some core requirements, and we provide advice for what to do if you are just getting started.

Core Requirements for Python Development
========================================

There are three basic elements to your environment when working with Python for this class:

* A way to run your code, add packages to Python, use git, etc.

  - You really need at least a little familiarity with the command line for this.

* A Python interpreter

  - We use "cPython" version 3.6 or greater for this class.

* A way to edit your code.

  - Any good programmer's text editor with a Python mode will work well.

If you are already set up with all this, then go straight here:

:ref:`testing_your_setup`

and give it a try.

If you are not sure, then read on ...

The Command Line (cli)
----------------------

Having some facility on the command line is important for a software developer.

We won't cover this much in class, so if you are not comfortable,
please bone up on your own.

We have some resources here: `PythonResources--command line <http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/command_line.html>`_

**Windows:**

Most of the demos in class, etc., will be done using the "bash" command line shell on OS-X or Linux.

Windows provides the "DOS" command line, which is OK, but pretty old and limited, or "Power Shell," a more modern, powerful, flexible command shell.

If you are comfortable with either of these, go for it.

If not, you can use the "git Bash" shell, which is much like the bash shell on OS-X and Linux. Or, on Windows 10, look into the "bash shell for Windows," otherwise known as the "Windows Subsystem for Linux." More info is available here:
`PythonResources--Windows Bash  <http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/windows_bash.html>`_

Accessing the Command Line
--------------------------

On any system, make sure you know how to get to a command line, and set the "working directory" to where your code resides.
Most modern UIs provide a way to start up a teminal from the file manager:

Windows
.......

Windows used to provide a "open command window here" options with a ``shift+right-click`` menu. Give a try; if it works, great. If not, then this might help:

`Open Command Window Here on Windows 10 <https://www.windowscentral.com/add-open-command-window-here-back-context-menu-windows-10>`_

OS-X
....

On The Mac, you can add a "New Terminal at Folder" right-click menu item by:


   Head into System Preferences and select Keyboard > Shortcuts > Services. Find "New Terminal at Folder" in the settings and click the box. Now, when you're in Finder, just right-click a folder and you're shown the open to open Terminal. When you do, it'll start right in the folder you're in.

`Launch an OS-X Terminal Window <https://lifehacker.com/launch-an-os-x-terminal-window-from-a-specific-folder-1466745514>`_

Linux
.....

Whether you use the KDE or GNOME Desktop (or anything else), there should be a way to open a shell from the file manager. Find it, it's very handy.


The Python Interpreter
----------------------

Python comes with a built-in interpreter.

You see it when you type ``python3`` at the command line:

.. code-block:: bash

    $ python3
    Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
    [Clang 6.0 (clang-600.0.57)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

That last thing you see, ``>>>`` is the "Python prompt".

This is where you can type code.

Notice that when it starts up, it tells you the version info. If the ``python3`` command did not work for you, or you got a version that is older than Python 3.6.4, you will need to install a new Python. Follow one of these:

:ref:`python_for_mac`

:ref:`python_for_windows`

:ref:`python_for_linux`

Note that you can use the interpreter to run a Python script as well:

.. code-block:: bash

  $ python3 the name_of_the_file.py

More on that here:

:ref:`how_to_run_a_python_file`


Other interpreters
..................

In addition to the built-in interpreter, there are several more advanced
interpreters available to you.

We'll be using one in this course called ``iPython`` -- more on that elsewhere.

The Editor
----------

Typing code in an interpreter is great for exploring.

But for anything "real," you'll want to save the work you are doing in a more permanent fashion.

This is where a "programmer's text editor" fits in.

Any good text editor will do.

MS Word is **not** a text editor.

Nor is *TextEdit* on a Mac.

``Notepad`` on Windows is a text editor, but a crappy one.

You need a real "programmers text editor."

A text editor saves only what it shows you, with no special formatting
characters hidden behind the scenes.

At a minimum, your editor should have:

* Syntax Colorization
* Automatic Indentation

In addition, great features to add include:

* Tab completion
* Code linting
* Jump-to-definition

Have an editor that does all this? Feel free to use it, and you can skip to the next section.

If not, we recommend SublimeText or Atom:

SublimeText:
............

`Sublime Text <http://www.sublimetext.com/>`_

:ref:`sublime_as_ide`

Atom
....

`Atom <https://atom.io/>`_

:ref:`atom_as_ide`

And, of course, vim or Emacs on Linux, if you are familiar with those.

Why No IDE?
-----------

An IDE does not give you much that you can't get with a good editor plus a good interpreter.

An IDE often weighs a great deal.

Setting up IDEs to work with different projects can be challenging and time-consuming.

An IDE, once set up, can hide a a lot of what is going on under the hood.  Particularly when you are first learning, you don't want too much done for you, So we recommend using an editor and the command line.

**That said ...**

You may want to try the educational edition of PyCharm, which some people like a lot:

https://www.jetbrains.com/pycharm-edu/

.. _testing_your_setup:

Testing Your setup
==================

If you have access to a command line, and Python installed, and a text editor or IDE ready to go, here's how you can make sure it's all working correctly.

Python Interpreter
------------------

If you have Python installed and know how to run a python file, give this a try to make sure you're all setup:

Create a file called ``install_test.py``, with the following content:

.. code-block:: python

    #!/usr/bin/env python3

    import sys
    print("This is my first python program")

    version = sys.version_info

    if version.major == 3:
        if version.minor < 6:
            print("You should be running version 3.6 or 3.7")
        else:
            print("You are running python {}.{} -- all good!".format(
                   version.major, version.minor))

    else:
        print("You need to run Python 3!")
        print("This is version: {}.{}".format(version.major, version.minor))

Run it with your version of python. It should result in something like this::

    This is my first python program
    You are running python3.6 -- all good!

(Version 3.6 or 3.7 is fine)

If you can't figure out how to run it, see: :ref:`how_to_run_a_python_file`

If you can run, it but don't get that nice "all good" message, then you either do not have Python installed, or you have the wrong version.

Go to one of:

:ref:`python_for_mac`

:ref:`python_for_windows`

:ref:`python_for_linux`

And try again.

iPython
-------

You should also be able to run iPython:

.. code-block:: bash

    $ ipython
    Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]:

If that doesn't work, try:

.. code-block:: bash

  $ python3 -m pip install iPython

And try it again (you may need to restart your terminal).

If that doesn't work, go back to the install instructions.

git
---

We will be using the git Source Code Version Control System (along with the gitHub service) to manage your assignments.

There will be another lesson on getting that all set up for class, but for now, you should have a git client installed. Try:

.. code-block:: bash

  $ git --version
  git version 2.15.2 (Apple Git-101.1)

If that reports a version newer than about 2.15, you are all set (as of this writing the latest version is 2.18).

If the git command does not work, go back to the install instructions for your platform above, and get it installed.

Other Helpful Hints
===================

There are a number of other assorted helpful materials here:

:ref:`supplemental_materials`


