.. _python_for_mac:

**************************
Setting up OS-X for Python
**************************

==================
Getting The Tools
==================


OS-X comes with Python out of the box, but not the full setup you'll need for development or this class. It also doesn't have the latest version(s), and no version of Python 3.

So we recommend installing a new version.


**Note**:


If you use ``macports`` or ``homebrew`` to manage \*nix software on your machine, feel free to use those for ``python``, ``git``, etc, as well. But make sure you have Python 3.8.*

If not, then read on.

Terminal
---------

You will need a command line terminal. The built-in "terminal" application works fine. Find it in::

  /Applications/Utilities/Terminal

Drag it to the dock to easily access.

Python
------

While OS-X does provide Python out of the box, it tends not to have the
latest version, and you really don't want to mess with the system
installation. So we recommend installing an independent installation from
``python.org``:

Download the latest release of Python installer from Python.org:

https://www.python.org/downloads/

NOTE: As of this writting, version 3.9.0 was jsut released -- it will work fine. But we willnot be using any 3.9 features in this course, and examples will generally be in 3.8 -- so 3.8 or 3.9 is fine.

Double click the installer and follow the prompts. The defaults are your best bet. Simple as that.

Oddly, this does NOT install a ``python`` command, but rather a ``python3`` command. If you want to be able to simply type ``python`` and get python3, then you can add a symlink to the install. Type this at a terminal prompt:

.. code-block:: bash

  $ cd /Library/Frameworks/Python.framework/Versions/3.8/bin
  $ ln -s python3.8 python

(replace the 3.8 above with 3.9 if you have installed 3.9)

Or an add an alias in your shell by adding the following line::

  alias python='python3'

to your ``.bash_profile`` file.

Once you have done that, you should be able to type ``python`` at the command prompt, and get something like:

.. code-block:: bash

  $ python
  Python 3.8.6 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
  [Clang 6.0 (clang-600.0.57)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

This is the Python interpreter.

Type ``ctrl+D`` to get out (or ``exit()``)

.. note:: If all this is confusing to you -- take heart -- you will get used it it. And in the meantime, you can simply type ``python3`` when you want to run python.

pip
---

``pip`` is the Python package installer. It is updated more frequently than Python itself, so once you have Python, you want to get the latest version of pip working::

  $ python3 -m ensurepip --upgrade

[``python`` may work too, if you set things up correctly above, but ``python3`` should always work.]

It should download and install the latest ``pip``. Or let you know that you already have it.

You can now use pip to install other packages. The first thing you may want to do is update pip itself:

.. code-block:: bash

  $ python3 -m pip install --upgrade pip

Using pip:
----------

To use pip to install a package, you invoke it with this command::

  python3 -m pip install the_name_of_the_package

Where ``python3`` is the command you use to invoke the Python you want to use.

**NOTE:** You will frequently see advice to use pip like so::

    $ pip install something_or_other

This often works, but also can invoke the *wrong* version of pip. This command::

  $ python3 -m pip install something_or_other

calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of Python that you are running.

iPython
--------

One package we are going to use in the program from the beginning is ``iPython``. You can install it with ``pip`` like so::

  $ python3 -m pip install ipython

(It will install a LOT...).

Now you should now be able to run ``iPython``:

.. code-block:: ipython

  $ ipython
  Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
  Type 'copyright', 'credits' or 'license' for more information
  IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

  In [1]:

Which you can also get out of with ``ctrl+D`` or ``exit()``

git
----

git is a source code version control system. It is not strictly related to Python, but it (or a similar system) is a critical tool for software development in general, and it is very widely used in the Python community.
We will be using it, along with the gitHub classroom service, in the program to hand in assignments and support code review.

You will need a git client. The gitHub GUI client may be nice; I honestly don't know. However, we will be using the command line client in class.

There are a couple of options for a command line client.

https://git-scm.com/download/mac

Perhpas the easiest, particularly if you need a compiler for any other reason, is to get git as part of the XCode command line tools, You can install XCode from the App Store. But be forwarned -- it is a VERY big download: 11.2GB!

Ifyou only need git, this has everything you need out of the box, and is a 500(!) times smaller download.

https://sourceforge.net/projects/git-osx-installer/

NOTE: if you get a warning like:

"... can't be opened because it is from an untrusted developer"

you'll need to go to  system preferences:

  "Security and Privacy"

Depending on the OS-X version, you will need to check the box saying "Open Anyway," or perhaps the box saying you can install untrusted packages. 

After either of these is installed, the ``git`` command should work:

.. code-block:: bash

  $ git --version
  git version 2.24.3 (Apple Git-128)


Testing it out
--------------

To be ready for this course, you need to have, all available from the command line:
 - python
 - pip
 - iPython
 - git

To try it out, you should be able to run all of the following commands, and get something like the results shown:

(recall that you can get out of the Python or iPython command lines with ``ctrl+D`` or ``exit()``

For Python:
...........

.. code-block:: bash

  $ python3
  Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
  [Clang 6.0 (clang-600.0.57)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.  
  >>>


For iPython:
............

.. code-block:: bash

  $ ipython
  Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
  Type 'copyright', 'credits' or 'license' for more information
  IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

  In [1]: 

For pip:
........

.. code-block:: bash

  $ python3 -m pip --version
  pip 20.2.3 from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip (python 3.8)

Note that when you ask pip for ``--version`` it tells you which version of python it is "connected" to.
Make sure that's the one you expect!

For git:
........

.. code-block:: bash

  $ git --version
  git version 2.24.3 (Apple Git-128)


If those commands all run -- you are all set!
