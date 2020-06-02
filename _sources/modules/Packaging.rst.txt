.. _packaging:

######################
Packages and Packaging
######################

Packages, modules, imports, oh my!
==================================

Before we get started on making your own package -- let's remind
ourselves about packages and modules, and importing....

**Modules**

A python "module" is a single namespace, with a collection of values:

  * functions
  * constants
  * class definitions
  * really any old value.

A module usually corresponds to a single file: ``something.py``


**Packages**

A "package" is essentially a module, except it can have other modules (and indeed other packages) inside it.

A package usually corresponds to a directory with a file in it called ``__init__.py`` and any number
of python files or other package directories::

  a_package
     __init__.py
     module_a.py
     a_sub_package
       __init__.py
       module_b.py

The ``__init__.py`` can be totally empty -- or it can have arbitrary python code in it.
The code will be run when the package is imported -- just like a module.

Modules inside packages are *not* automatically imported. So, with the above structure::

  import a_package

will run the code in ``a_package/__init__.py``. Any names defined in the ``__init__.py`` will be available in::

  a_package.a_name

But::

 a_package.module_a

will not exist. To get submodules, you need to explicitly import them like so:

  import a_package.module_a


More on Importing
-----------------

You usually import a module like this:

.. code-block:: python

  import something

or::

  from something import something_else

or a few names from a package::

  from something import (name_1,
                         name_2,
                         name_3,
                         x,
                         y)

You also can optionally rename stuff as you import it::

  import numpy as np

This is a common pattern for using large packages (maybe with long names) and not having to type a lot.


``import *``
------------

::

  from something import *

Means: "import all the names in the module, "something".

You really don't want to do that! It is an old pattern that is now an anti-pattern.

But if you do encounter it, it doesn't actually import all the names -- it imports the ones defined in the module's ``__all__`` variable.

``__all__`` is a list of names that you want ``import *`` to import.
So the module author can control it, and not accidentally override builtins or bring a lot of extraneous names into your namespace.

But really -- **don't use ``import *``**


Relative imports
----------------

Relative imports were added with PEP 328:

https://www.python.org/dev/peps/pep-0328/

The final version is described here:

https://www.python.org/dev/peps/pep-0328/#guido-s-decision

This gets confusing! There is a good discussion on Stack Overflow here:

http://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

Relative imports allow you to refer to other modules relative to where the existing module is in the package hierarchy, rather than in the entire python module namespace. For instance, with the following package structure::

  package/
      __init__.py
      subpackage1/
          __init__.py
          moduleX.py
          moduleY.py
      subpackage2/
          __init__.py
          moduleZ.py
      moduleA.py

You can do (in ``moduleX.py``):

.. code-block:: python

  from .moduleY import spam
  from . import moduleY
  from ..subpackage1 import moduleY
  from ..subpackage2.moduleZ import eggs
  from ..moduleA import foo
  from ...package import bar
  from ...sys import path

Similarly to \*nix shells:

"." means "the current package"

".." means "the package above this one"

Note that you have to use the ``from`` form of import when using relative imports.

**Caveats:**

* you can only use relative imports from within a package

* you can not use relative imports from the interpreter

* you can not use relative imports from a top-level script


The alternative is to always use absolute imports:

.. code-block:: python

  from package.subpackage import moduleX
  from package.moduleA import foo

Advantages of relative imports:

* Package does not have to be installed

* You can move things around, and not much has to change

Advantages of absolute imports:

* explicit is better than implicit
* imports are the same regardless of where you put the package
* imports are the same in package code, command line, tests, scripts, etc.

There is debate about which is the "one way to do it" -- a bit unpythonic, but you'll need to make your own decision.


sys.modules
-----------

``sys.modules`` is simply a dictionary that stores all teh already imported modules.
The keys are the module names, and the values are the module objects themselves:

.. code-block:: ipython

  In [3]: import sys

  In [4]: type(sys.modules)
  Out[4]: dict

  In [6]: sys.modules['textwrap']
  Out[6]: <module 'textwrap' from '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/textwrap.py'>

  In [10]: [var for var in vars(sys.modules['textwrap']) if var.startswith("__")]
  Out[10]:
  ['__spec__',
   '__package__',
   '__loader__',
   '__doc__',
   '__cached__',
   '__name__',
   '__all__',
   '__file__',
   '__builtins__']

you can access the module through the ``sys.modules`` dict:

.. code-block:: ipython

  In [12]: sys.modules['textwrap'].__file__
  Out[12]: '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/textwrap.py'

Which is the same as:

.. code-block:: ipython

  In [13]: import textwrap

  In [14]: textwrap.__file__
  Out[14]: '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/textwrap.py'

  In [15]: type(textwrap)
  Out[15]: module

  In [16]: textwrap is sys.modules['textwrap']
  Out[16]: True

So, more or less, when you import a module, the interpreter:

* Looks to see if the module is already in ``sys.modules``.

* If it is, it binds a name to the existing module in the current module's namespace.

* If it isn't:

 - A module object is created
 - The code in the file is run
 - The module is added to sys.modules
 - The module is added to the current namespace.

Implications of module import process:
--------------------------------------

* The code in a module only runs once per program run.
* Importing a module again is cheap and fast.
* Every place your code imports a module it gets the *same* object
  - You can use this to share "global" state where you want to.

* If you change the code in a module while the program is running -- the change will **not** show up, even if re-imported.

  - That's what ``imp.reload()`` is for.

The module search path
----------------------

The interpreter keeps a list (``sys.path``) of all the places that it looks for modules or packages when you do an import:

.. code-block:: python

    import sys
    for p in sys.path:
        print p

you can manipulate that list to add or remove paths to let python find modules in a new place.

Every module has a ``__file__`` name that points to the path it lives in. This lets you add paths relative to where you are, etc.

 .. note:: It's usually better to use setuptools' "develop" mode (or ``pip install -e``) instead -- see below.

Reloading
---------

Once loaded, a module stays loaded.

If you import it again (usually in another module) it will simply load up the versions already there -- rather than re-running the code.

And you can access all the already loaded modules from ``sys.modules``. sys.modules is a dict with the module names as the keys, and the module objects as the values

.. code-block:: ipython

  In [4]: import sys

  In [5]: sys.modules.keys()
  Out[5]: dict_keys(['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'posix', 'zipimport', 'encodings', 'codecs', '_codecs'

A lot there!

There's no reason too -- but you could import an already imported module like so:

.. code-block:: ipython

  In [10]: math = sys.modules['math']

  In [11]: math.sin(math.pi)
  Out[11]: 1.2246467991473532e-16

  In [12]: math.sin(math.pi / 2)
  Out[12]: 1.0


Python Distributions
====================

So far in this class, we've used the Python from python.org. It works great, and supports a lots of packages via pip.

But there are also a few "curated" distributions. These provide python and a package management system for hard-to-build packages.

Widely used by the scipy community:

(lots of hard to build stuff that needs to work together...)

  * Anaconda (https://store.continuum.io/cshop/anaconda/)
  * Canopy (https://www.enthought.com/products/canopy/)
  * ActivePython (http://www.activestate.com/activepython)

Anaconda has seen a LOT of growth recently -- it's based on the open-source conda packaging system, and provides both a commercial curated set of packages, and a community-developed collection of packages known as conda-forge:

https://conda-forge.org/

If you are doing data science or scientific development -- I recommend you take a look at Anaconda, conda and conda-forge.


Installing Packages
===================

Every Python installation has its own stdlib and ``site-packages`` folder.

``site-packages``  is the default place for third-party packages.


From source
-----------

* (``setup.py install`` )

* With the system installer (apt-get, yum, etc...)


From binaries
-------------

* Binary wheels -- (More and more of those available)

* ``pip`` should find appropriate binary wheels if they are there.


A bit of history:
-----------------

In the beginning, there was the ``distutils``:

But ``distutils``  is missing some key features:

* package versioning
* package discovery
* auto-install

- And then came ``PyPi``

- And then came ``setuptools`` (with easy_install)

- But that wasn't well maintained...

- Then there was ``distribute/pip``

- Which has now been merged back into ``setuptools``

Now it's pretty stable: pip+setuptools+wheel: use them.

**warning** -- setuptools still provides easy_install, but it has mostly been deprecated, so you really want to use pip. And sometimes setuptools will invoke it for you under the hood by accident :-(


Installing Packages
-------------------

Actually, it's still a bit of a mess

But getting better, and the mess is *almost* cleaned up.


Current State of Packaging
--------------------------

To build packages: setuptools
.............................

  * https://pythonhosted.org/setuptools/

setuptools provides extensions to the build-in distutils:

https://docs.python.org/3/library/distutils.html

But there are a couple of those extensions that you really do need, so most folks use setuptools for everything. In fact, pip itself requires setuptools.


To install packages: pip
........................

  * https://pip.pypa.io/en/latest/installing.html

For binary packages: wheels
...........................

  * http://www.python.org/dev/peps/pep-0427/

(installable by pip)


Compiled Packages
-----------------

Biggest issue is with compiled extensions:

  * (C/C++, Fortran, etc.)

  * You need the right compiler set up

Dependencies:

  * Here's where it gets really ugly

  * Particularly on Windows

Linux
.....

Pretty straightforward:

1. Is there a system package?

  * use it (apt-get install the_package)

2. Try ``pip install``: it may just work!

3. Install the dependencies, build from source::

    python setup.py build

    python setup.py install

(may need "something-devel" packages)


Windows
.......

Sometimes simpler:

1) A lot of packages have Windows wheels now.

  - Often installable with pip (pip will install a wheel for you if it exists)
  - Usually for python.org builds
  - Excellent source: http://www.lfd.uci.edu/~gohlke/pythonlibs/
  - Make sure you get 32 or 64 bit consistent

2) But if no binaries:

  - Hope the dependencies are available!
  - Set up the compiler

MS now has a compiler just for python2!

http://www.microsoft.com/en-us/download/details.aspx?id=44266

.. NOTE: add info on Windows compiler for py3

OS-X
....

Lots of Python versions:
  - Apple's built-in (different for each version of OS)
  - python.org builds
  - 32+64 bit Intel (and even PPC still kicking around)
  - Macports
  - Homebrew

Binary wheels are pretty much compatible between them -- yeah!

If you have to build it yourself

Xcode compiler (the right version)

  - Version 3.* for 32 bit PPC+Intel

  - Version > 4.* for 32+64 bit Intel

(make sure to get the SDKs for older versions)

If extra dependencies:

  - macports or homebrew often easiest way to build them


Final Recommendations
---------------------

First try: ``pip install``

If that doesn't work:

Read the docs of the package you want to install

Do what they say

(Or use conda!)


virtualenv
----------

``virtualenv`` is a tool to create isolated Python environments.

Very useful for developing multiple apps

Or deploying more than one app on one system

http://www.virtualenv.org/en/latest/index.html}

Remember the notes from the beginning of class? :ref:`virtualenv_section`

**NOTE:** conda also provides a similar isolated environment system.


Building Your Own Package
=========================

The very basics of what you need to know to make your own package.


Why Build a Package?
--------------------

There are a bunch of nifty tools that help you build, install and
distribute packages.

Using a well structured, standard layout for your package makes it
easy to use those tools.

Even if you never want to give anyone else your code, a well
structured package eases development.


What is a Package?
--------------------

**A collection of modules**

* ... and the documentation

* ... and the tests

* ... and any top-level scripts

* ... and any data files required

* ... and a way to build and install it...


Python packaging tools:
------------------------

The ``distutils``::

    from distutils.core import setup

Getting klunky, hard to extend, maybe destined for deprecation...

But it gets the job done -- and it does it well for the simple cases.

``setuptools``: for extra features

``pip``: for installing packages

``wheel``: for binary distributions

These last three are pretty much the standard now -- very well maintained by:

"The Python Packaging Authority" -- PaPA

https://www.pypa.io/en/latest/


Where do I go to figure this out?
---------------------------------

This is a really good guide:

Python Packaging User Guide:

https://packaging.python.org/

and a more detailed tutorial:

http://python-packaging.readthedocs.io/en/latest/

**Follow one of them**

There is a sample project here:

https://github.com/pypa/sampleproject

(this has all the complexity you might need...)

You can use this as a template for your own packages.

Here is an opinionated update -- a little more fancy, but some good ideas:

https://blog.ionelmc.ro/2014/05/25/python-packaging/

Rather than doing it by hand, you can use the nifty "cookie cutter" project:

https://cookiecutter.readthedocs.io/en/latest/

And there are a few templates that can be used with that.

The core template written by the author:

https://github.com/audreyr/cookiecutter-pypackage

And one written by the author of the opinionated blog post above:

https://github.com/ionelmc/cookiecutter-pylibrary

Either are great starting points.

Basic Package Structure:
------------------------

::

    package_name/
        bin/
        CHANGES.txt
        docs/
        LICENSE.txt
        MANIFEST.in
        README.txt
        setup.py
        package_name/
              __init__.py
              module1.py
              module2.py
              test/
                  __init__.py
                  test_module1.py
                  test_module2.py


``CHANGES.txt``: log of changes with each release

``LICENSE.txt``: text of the license you choose (do choose one!)

``MANIFEST.in``: description of what non-code files to include

``README.txt``: description of the package -- should be written in ReST (for PyPi):

(http://docutils.sourceforge.net/rst.html)

``setup.py``: distutils script for building/installing package.


``bin/``: This is where you put top-level scripts

  ( some folks use ``scripts`` )

``docs/``: the documentation

``package_name/``: The main package -- this is where the code goes.

``test/``: your unit tests. Options here:

Put it inside the package -- supports ::

     $ pip install package_name
     >> import package_name.test
     >> package_name.test.runall()

Or keep it at the top level.

Some notes on that:
` Where to put Tests <http://pythonchb.github.io/PythonTopics/where_to_put_tests.html>`_

The ``setup.py`` File
----------------------

Your ``setup.py`` file is what describes your package, and tells the distutils how to package, build and install it

It is python code, so you can add anything custom you need to it

But in the simple case, it is essentially declarative.


``http://docs.python.org/3/distutils/``

An example:
...........

.. code-block:: python

  from setuptools import setup

  setup(
    name='PackageName',
    version='0.1.0',
    author='An Awesome Coder',
    author_email='aac@example.com',
    packages=['package_name', 'package_name.test'],
    scripts=['bin/script1','bin/script2'],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "pytest",
    ],
 )

``setup.cfg``
--------------

**NOTE:** this is usually a pretty advanced option -- simple packages don't need this.

``setup.cfg`` provides a way to give the end user some ability to customize the install

It's an ``ini`` style file::

  [command]
  option=value
  ...

simple to read and write.

``command`` is one of the Distutils commands (e.g. build_py, install)

``option`` is one of the options that command supports.

Note that an option spelled ``--foo-bar`` on the command-line is spelled f``foo_bar`` in configuration files.


Running ``setup.py``
--------------------

With a ``setup.py`` script defined, setuptools can do a lot:

* builds a source distribution (a tar archive of all the files needed to build and install the package)::

    python setup.py sdist

* builds wheels::

    ./setup.py bdist_wheel

(you need the wheel package for this to work: ``pip install wheel``)

* build from source::

    python setup.py build

* and install::

    python setup.py install

* install in "develop" or "editable" mode::

    python setup.py develop

or::

   pip install .


setuptools
-----------

``setuptools`` is an extension to ``distutils`` that provides a number of extensions::

    from setuptools import setup

superset of the ``distutils setup``

This buys you a bunch of additional functionality:

  * auto-finding packages
  * better script installation
  * resource (non-code files) management
  * **develop mode**
  * a LOT more

http://pythonhosted.org//setuptools/

wheels
-------

Wheels are a new binary format for packages.

http://wheel.readthedocs.org/en/latest/

Pretty simple, essentially a zip archive of all the stuff that gets put
in ``site-packages``.

Can be just pure python or binary with compiled extensions

Compatible with virtualenv.

Building a wheel::

  python setup.py bdist_wheel

Create a set of wheels (a wheelhouse)::

  # Build a directory of wheels for pyramid and all its dependencies
  pip wheel --wheel-dir=/tmp/wheelhouse pyramid

  # Install from cached wheels
  pip install --use-wheel --no-index --find-links=/tmp/wheelhouse pyramid

``pip install packagename`` will find wheels for Windows and OS-X and "manylinux"

``pip install --no-use-wheel`` avoids that.

manylinux
---------

There are a lot of Linux distributions out there. So for a long time, there were not easily available binary wheels for Linux -- how could you define a standard with all the Linux distros out there?

Enter "manylinux" -- no one thinks you can support all Linux distros, but it was found that you could support many of the common ones, by building on an older version, and restricting system libraries. This approach worked well for Canopy and conda, so PyPi adopted a similar strategy with manylinux:

https://github.com/pypa/manylinux

So there are now binary wheels for Linux on PyPi.

The core scipy stack is a great example -- you can now ``pip install numpy`` on all three systems easily with pip.

PyPi
-----

The Python package index:

https://pypi.python.org/pypi

You've all used this -- ``pip install`` searches it.

To upload your package to PyPi::

  python setup.py register

  python setup.py sdist bdist_wheel upload


http://docs.python.org/2/distutils/packageindex.html

NOTE: only do this if you really want to share your package with the world!


Under Development
------------------

Develop mode is *really* *really* nice::

  $ python setup.py develop

or::

  $ pip install -e ./

(the e stands for "editable" -- it is the same thing)

It puts links into the python installation to your code, so that your package is installed, but any changes will immediately take effect.

This way all your test code, and client code, etc, can all import your package the usual way.

No ``sys.path`` hacking

Good idea to use it for anything more than a single file project.

(requires ``setuptools``)

Running tests
-------------

It can be a good idea to set up your tests to be run from ``setup.py``

So that you (or your users) can:

.. code-block:: bash

  $ pip install .
  $ python setup.py test

**Note:** there is debate about whether this is a good idea. But if you want to:

To do this, you need to add a ``test_suite`` stanza in setup.py.

**pytest**

.. code-block:: python

  setup(
    #...,
    setup_requires=['pytest-runner', ...],
    tests_require=['pytest', ...],
    #...,
  )

And create an alias into setup.cfg file::

  [aliases]
  test=pytest

https://pytest.org/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner

This may not be required, as pytest will also let you run the tests installed with a package with::

    pytest --pyargs package_name


**unittest**

.. code-block:: python

  test_suite="tests"


Handling the version number:
----------------------------

One key rule in software (and ANY computer use!):

Never put the same information in more than one place!

With a python package, you want:

.. code-block:: python

  import the_package

  the_package.__version__

To return the version string -- something like:

"1.2.3"

Using ``__version__`` is not a requirement, but it is a very commonly used convention -- *use it*!

But you also need to specify it in the ``setup.py``:

.. code-block:: python

  setup(name='package_name',
        version="1.2.3",
        ...
        )

Not Good.

My solution:
............

Put the version in the package __init__

__version__ = "1.2.3"

In the setup.py, you could import the package to get the version number
... but it's not a safe practice to import your package when installing
it (or building it, or...)

So: read the ``__version__`` string yourself with code like:

.. code-block:: python

  def get_version():
      """
      Reads the version string from the package __init__ and returns it
      """
      with open(os.path.join("capitalize", "__init__.py")) as init_file:
          for line in init_file:
              parts = line.strip().partition("=")
              if parts[0].strip() == "__version__":
                  return parts[2].strip().strip("'").strip('"')
      return None

**Alternative:**

You can have a script that automatically updates the version number in whatever places it needs to. For instance:

https://pypi.python.org/pypi/bumpversion

Though I think it's better to have the version set in the code itself.


Semantic Versioning
-------------------

Another note on version numbers.

The software development world (at least the open-source one...) has
established a standard for what version numbers mean, known as semantic
versioning. This is helpful to users, as they can know what to expect
they upgrade.

In short, with a x.y.z version number:

x is the Major version -- it could mean changes in API, major features, etc.

  - Likely to to be incompatible with previous versions

y is the Minor version -- added features, etc, that are backwards compatible.

z is the "patch" version -- bug fixes, etc. -- should be compatible.

Read all about it:

http://semver.org/


Tools to help:
--------------

Tox:

https://tox.readthedocs.io/en/latest/

Versioneer:

https://github.com/warner/python-versioneer

Dealing with data files
-----------------------

Oftentimes a package will require some files that are not Python code. In that case, you need to make sure the files are included with the package some how.

There are a few ways to do this:

http://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files

The simplest option: package_data
..................................

I personally like the simplest one with the least magic:

.. code-block:: python

  setup(
      ...
      package_data={'pkg_name': ['data/datatfile1',
                                 'data/datafile2']},
      ...
        )

https://packaging.python.org/tutorials/distributing-packages/#package-data

Then you'll get the data file included in the package in the same place relative to your code regardless of how (or whether) it is installed.

Now you'll need to write your code to find that data file. You can do that by using the ``__file__`` module attribute -- then the location of the data file will be relative to the ``__file__`` that your code is in. A little massaging with a ``pathlib.Path`` should do it. Putting the path to the data directory in the package's ``__init__.py`` provides a way for the rest of your code to find it.

In ``pkg_name/__init__.py``:

.. code-block:: python

    from pathlib import Path

    data_dir = data_file = Path(__file__).parent / "data"

Now you can get that dir anywhere else in your code:

.. code-block:: python

    from pkg_name import data_dir


More complex option: data_files
...............................

Using the data_files setup option lets you put data files outside your package. They will get installed into the path of ``sys.prefix``, so you can find them in your code with a path relative to ``sys.prefix``.

However, this means that the location of the files is different depending on whether the code is properly installed or not. And develop mode (or editable mode) does NOT install the data files.

I honestly can't think of any reason to do this.

https://packaging.python.org/tutorials/distributing-packages/#data-files

More magic: pkg_resources
.........................

setuptools provides a pkg_resources system to access resources (such as data files) of the packages. It is a complex (and I think ugly) system, with lots of features.

http://setuptools.readthedocs.io/en/latest/pkg_resources.html

But for just using it to find data files, it has some advantages -- the primary one that is it can find data files that are inside zipped-up packages. (Python can import modules from zip files, but you can't easily read data files from inside a zipped package)

To use pkg_resources, you include the files with ``package_data`` in setup.py but access them with the pkg_resources API:

.. code-block:: python

    from pkg_resources import resource_string
    foo_config = resource_string(__name__, 'foo.conf')

http://setuptools.readthedocs.io/en/latest/pkg_resources.html#resourcemanager-api

Getting Started With a New Package
----------------------------------

For anything but a single-file script (and maybe even then):

1. Create the basic package structure

2. Write a ``setup.py``

3. ``pip install -e .``

4. Put some tests in ``package/test``

5. ``pytest`` in the test dir, or ``pytest --pyargs package_name``

or use "Cookie Cutter":

https://cookiecutter.readthedocs.io/en/latest/

LAB: A Small Example Package
----------------------------

* Create a small package

  - package structure

  - ``setup.py``

  - ``python setup.py develop``

  - ``at least one working test``

* If you have some code of your own ready to go -- use that.

* If you don't have any code of your own to package, start with the silly code in:

:download:`capitalize.zip <../examples/packaging/capitalize.zip>`

Or go straight to making a package our of your mailroom project.


