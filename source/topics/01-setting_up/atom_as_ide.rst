.. _atom_as_ide:

##########################################
Turning Atom Into a Lightweight Python IDE
##########################################

Atom is the self-proclaimed "hackable text editor for the 21st Century." It has a nice modern interface, and is highly customizable yet can also be used productively with minimal setup and configuration.


Requirements
============

Any IDE should ease your development experience by providing the following:

* It should provide excellent, configurable syntax colorization.
* It should allow for robust tab completion.
* It should offer the ability to jump to the definition of symbols in other files.
* It should perform automatic code linting to help avoid silly mistakes.
* It should be able to interact with a Python interpreter such that when debugging, the editor will follow along with the debugger.

Atom does all this and more, but some functionality requires you to select and install packages.


Which Version?
==============

The latest version is the best version. Atom is regularly maintained, so the latest
version will have the latest bug fixes and updates.


Installation
============

Go to the Atom website_.

.. _website: https://atom.io/

On the main page, click the big red button to download the installer, then run the installer.

If it is not offering the correct platform: on the main page, below the big red button, click Other Platforms and find the installer for your operating system.

If you already have Atom installed, but want to check for a newer version, go to
``Help`` -> ``Check for Update``.


Basic Settings
==============

Atom can be used out of the box with no setup as a text editor. It automatically
recognizes file types and helpfully highlights text accordingly. To use in this manner,
write your Python files in Atom, then run them in your Python command prompt.


Extending the Editor
====================

When you first open Atom, a Welcome Guide appears. This provides some quick and helpful information on
how to open projects, install packages, and customize your themes and styling.

Atom has great documentation_ on how to hack and configure it. Read the Flight Manual_ for tons of information on
everything you can do. You can also watch a Getting Started video_.

.. _documentation: https://atom.io/docs
.. _Manual: http://flight-manual.atom.io/
.. _video: https://www.youtube.com/watch?v=U5POoGSrtGg

Atom has a configuration file which you can modify called config.cson.
Access it via ``File`` -> ``Config...``

::

  "*":
    core:
      themes: [
        "atom-dark-ui"
        "solarized-light-syntax"
      ]
    editor:
      fontSize: 19
    "exception-reporting":
      userId: "6e2a9c3f-7ddb-7deb-b5f7-b58f2f87ac0d"
    "tree-view":
      hideVcsIgnoredFiles: true

Here you can quickly change the theme or font size. Some packages will require you to add configs
or make adjustments here. Read the documentation carefully when installing packages.

In general, you can extend Atom by installing packages, and then accessing their functionality from the Packages
drop-down menu. Access the Install Packages page from the Welcome Guide page. If the Welcome Guide is not open,
you can open it via ``Help`` -> ``Welcome Guide``.

Keyboard shortcuts are specified in the packages menus if available.

The Useful Packages presented below are only a few options of many.


Useful Packages
===============

Running Scripts
---------------

To run scripts within Atom, you will need to install the Script_ package. The Script package supports a ton of languages,
including Python!

.. _Script: https://atom.io/packages/script

Autocompletion
--------------

By default, Atom knows which Python packages you have imported, variables you have created
and so on. Autocomplete_ ships with Atom and requires no setup.

.. _Autocomplete: http://flight-manual.atom.io/using-atom/sections/autocomplete/

Code Linting
------------

To get code linting functionality in Atom, you will need to install a linting package
of which there are many to choose from. linter-pylint_ works well, and requires minimal
setup.

.. _linter-pylint: https://atom.io/packages/linter-pylint

White Space Management
----------------------

Atom knows when you are writing Python and helps you out by dealing with spaces and tabs
in the same way. When in a Python file, if you type 4 spaces, then hit delete, you are
taken back a tab.

The Whitespace_ package ships with Atom and requires no setup. Under the ``Packages`` -> ``Whitespace`` menu,
you will find tools to turn all tabs into spaces, all spaces into tabs, among other whitespace-related options.

.. _Whitespace: https://atom.io/packages/whitespace

Debugging
---------

To use a Python debugger in Atom, you will need to install the python-debugger_ package. Once installed, turn on the
debugger by going to ``Packages`` -> ``python-debugger`` -> ``Toggle``.

.. _python-debugger: https://atom.io/packages/python-debugger
