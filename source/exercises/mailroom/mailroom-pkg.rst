.. _exercise_mailroom_package:

Mailroom -- as a Python Package
===============================

The mailroom program is a small but complete system -- if you wanted to make it available for others to test and run, making a "proper" python package is a great idea. Making a package of it will also make it easier to develop and test, even if you are the only one to use it.

Code Structure
--------------

Start with your existing version of mailroom.

It should already be structured with the "logic" code distinct from the user interface (yes, a command line *is* a user interface). But you may have it all in one file. This isn't *too* bad for such a small program, but as a program grows, you really want to keep things separate, in a well organized package.

The first step is to re-structure your code into separate files:

 - one (or more) for the logic code: the code than manipulates the data
 - one for the user-interface code: the code with the interactive loops and all the "input" and "print" statements
 - one (or more) for tests.

You should have all this pretty distinct after having refactored for the unit testing. If not, this is a good time to do it!

In addition to those three, you will want to write a top-level script file (perhaps called ``mailman.py``) that does little but import the ui code and run a ``main()`` function. It should look something like this:

.. code-block:: python

    #!/usr/bin/env python
    from mailman import cli

    if __name__ == "__main__":
        cli.main()

Yes, that's it! This has the advantage of keeping the top-level script really simple, as it has to get put somewhere else and it can keep the "real" code in the package where it belongs.

.. note:: Be careful here -- it is important not to call your top-level script the same thing as your package, in this case ``mailroom.py``. If you do, than when installed, python will find the script, rather than the package, when you do ``import mailroom``. You can call it ``mailroom`` without the Python, but that may confuse Windows.


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
      bin
          mailman.py

You will need to import the logic code from model.py in the cli code in order to use it. You can wait until you learn about mocking to write the code in test_cli.py (so you can leave that out)

Now write your ``setup.py`` to support your package.


Making the top-level script runnable
------------------------------------

To get the script installed you have two options. I prefer the more straightforward one, `the scripts keyword argument <http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-scripts-keyword-argument>`_

But if you want to get fancy, you can use ``setuptools``'s `entry points <http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point>`_

.. note:: On Unix systems, including the Mac, the simple ``scripts`` keyword argument method works well and is simple. But it may not work as well on Windows -- it relies in your script being named ``something.py`` and that Windows is configured to run all files with ``.py`` extensions. Not all windows systems are set up this way. But the "entry points" method builds a little exe file to call your script, so it's more reliable.


Including data files
--------------------

NOTE: If you have a database of donors in a file that you load, then that should go in the package as well. Probably inside the mailroom dir, in a ``data`` dir or similar. Then you need to add it to your setup.py to make sure it gets copied into the installed package.

There are a few ways to do this:

http://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files

I personally like the simplest one with the least magic:

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

If you installed in editable mode, then you can update the code and re-run the tests or the script, and it will use the new code right away.











