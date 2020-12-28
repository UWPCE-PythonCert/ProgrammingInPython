.. _exercise_mailroom_package:

Mailroom -- as a Python Package
===============================

The mailroom program is a small but complete system -- if you wanted to make it available for others to test and run, making a "proper" python package is a great idea. Making a package of it will also make it easier to develop and test, even if you are the only one to use it.

Code Structure
--------------

Start with your existing version of mailroom.

It may already be structured with the "logic" code distinct from the user interface (yes, a command line *is* a user interface). But you may have it all in one file. This isn't *too* bad for such a small program, but as a program grows, you really want to keep things separate, in a well organized package.

The first step is to re-structure your code into separate files:

 - One (or more) for the logic code: the code that manipulates the data
 - One for the user-interface code: the code with the interactive loops and all the "input" and "print" statements
 - One (or more) for the unit tests.

You should have all this pretty distinct after having refactored for the unit testing. If not, this is a good time to do it!

In addition to those three, you will need a single function to call that will start the program.
That can be defined in a new file, as a "script", but for something as simple as this, it can be in with your interface code.
That file can then have an ``if __name__ == "__main__"`` block
which should be as simple as:

.. code-block:: python

    if __name__ == "__main__":
        main()


Making the Package
------------------

Put all these in a python package structure, something like this::

  mailroom
      setup.py
      mailroom\
          __init__.py
          model.py
          cli.py
          tests\
              __init__.py
              test_model.py
              test_cli.py

You will need to import the logic code from model.py in the cli code in order to use it.
You can wait until you learn about mocking to write the code in test_cli.py (so you can leave that out)

Now write a ``setup.py`` file to support the installation of your package.


Making the top-level script runnable
------------------------------------

To get the script installed you have two options. I used to prefer the more straightforward one, `the scripts keyword argument <http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-scripts-keyword-argument>`_

But it turns out that while the simple ``scripts`` keyword argument method works well and is simple, it may not work as well on Windows -- it relies in your script being named ``something.py`` and that Windows is configured to run all files with ``.py`` extensions. Not all windows systems are set up this way. But the "entry points" method builds a little ``.exe`` file to call your script, so it's more reliable.

And the Python community has moved very much towards using setuptools entry points, so that's really the way to go now:

http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point

In this case, that will look a lot like this:

.. code-block:: python

      entry_points={'console_scripts': ['mailroom=mailroom.cli:main']},

That's a bit complicated, so I'll break it down for you. In this case, we only want a single script, but setuptools allows multiple types of entry points, and multiple instances of each type (e.g. you can have more than one script) to the code, so the argument is a potentially large dictionary.
The keys of the dict are the various types of entry points.
In this case, we want a single script that can be run in a terminal (or "console"),  so we have a dict with one key: ``console_scripts``.

The value of that entry is a list of strings -- each one describing the console script. This string is of the form::

  SCRIPTNAME=MODULE:FUNCTION_NAME

setuptools will create a wrapper script with the name given, and that wrapper will call the function in the module that is specified.
So: ``'mailroom=mailroom.cli:main'`` means: create a start up script called "mailroom" that will then call the ``main`` function in the ``cli`` module in the ``mailroom`` package.

Once this is all set up, and you install the package (either in editable mode or not)::

  pip install -e ./

you should then be able to type "mailroom" at the command line and have your program run.


Including Data Files
--------------------

If you have a database of donors in a file that you load, then that should go in the package as well. Probably inside the mailroom dir, in a ``data`` dir or similar. Then you need to add it to your setup.py to make sure it gets copied into the installed package.

(If you are not saving the donor data to a file -- that's fine. You can ignore this section for now)

There are a few ways to do this:

http://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files

I personally like the simplest one with the least magic:

`include_package_data=True <http://python-packaging.readthedocs.io/en/latest/non-code-files.html#adding-non-code-files>`_

Then you'll get the data file included in the package in the same place.

Now you'll need to write your code to find that data file.
You can do that by using the ``__file__`` module attribute, which is the path to a python module at run time  -- then the location of the data file will be relative to the path that your code is in.
A little massaging with a ``pathlib.Path`` should do it.


Testing your Package
--------------------

When you are done, you should be able to both install your package fully:

.. code-block:: bash

  $ pip install .

or in "editable" mode:

.. code-block:: bash

  $ pip install -e .

When that is done, you should be able to run the top-level script from anywhere:

.. code-block:: bash

    $ mailroom

and run the test from within the package:

.. code-block:: bash

    $ pytest --pyargs mailroom

(or run the tests from the test dir as well)

If you installed in editable mode, then you can update the code and re-run the tests or the script, and it will use the new code right away.

