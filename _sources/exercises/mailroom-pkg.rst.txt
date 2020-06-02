.. _exercise_mailroom_package:

Mailroom -- as a Python Package
===============================

The mailroom program, particularly the Object Oriented version, is a pretty complete system -- if you wanted to make it available for others to test snd run, making a "proper" python package is a great idea.

Code Structure
--------------

Start with an Object Oriented mailroom.

It should already be structured with the "logic" code distinct from the user interface (yes, a command line *is* a user interface). But you may have it all in one file. This isn't *too* bad for such a small program, but as a program grows, you really want to keep things separate, in a well organized package.

The first step is to re-structure your code into separate files:

 - one (or more) for the logic code (the Donor and DonorDB classes)
 - one for the user-interface code
 - one (or more) for tests.

Then you are going to want a top-level script file that does little but import the ui code and run a ``main()`` function.

Making the Package
------------------

Put all these in a python package structure, something like this::

  mailroom
      setup.py
      mailroom\
          __init__.py
          model.py
          ui
          tests\
              test_model.py
              test_ui.py
      bin
          mailroom.py

You will need to import the logic code from model.py in the ui code in order to use it. You can wait until you learn about mocking to write the code in test_ui.py

Now write your ``setup.py`` to support your package.

Making the top-level script runnable
------------------------------------

To get the script installed you have two options. I prefer the more straightforward one, `the scripts keyword argument <http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-scripts-keyword-argument>`_

But if you want to get fancy, you can use ``setuptools``'s `entry points <http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point>`_


Including data files
--------------------

NOTE: If you have a database of donors in a file that you load, then that should go in the package as well. Probably inside the mailroom dir, in a ``data`` dir or similar. Then you need to add it to your setup.py to make sure it gets copied into the installed package.

There are a few ways to do this:

http://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files

I personally like the simiplest one with the least magic:

`include_package_data=True <http://python-packaging.readthedocs.io/en/latest/non-code-files.html#adding-non-code-files>`_

Then you'll get the data file included in the package in the same place.

Now you'll need to write your code to find that data file. You can do that by using the __file__ module attribute -- then the location of the data file will be relative to the __file__ that your code is in. A little massaging with a ``pathlib.Path`` should do it.

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

    $ mailroom.py

and run the test from within the package:

.. code-block:: bash

    $ pytest --pyargs mailroom











