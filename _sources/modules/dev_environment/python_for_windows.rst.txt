.. _python_for_windows:

#############################
Setting up Windows for Python
#############################

Getting The Tools
==================

Python
-------

There are a number of Python distributions available -- many designed for easier support of scientific programming:

- Anaconda
- Enthought Canopy
- Python(x,y)
- etc....

But for basic use, the installer from python.org is the way to go, and that is what we will be using in this program.

https://www.python.org/downloads/

You want the installer for Python 3.7 -- probably 64 bit, though if you have a 32 bit system, you can get that.

There is essentially no difference for the purposes of this course.

Double click and install.

Ensure that the Install launcher for all users (recommended) and the Add Python 3.7 to PATH checkboxes at the bottom are checked.

**Add Python 3.7 to PATH step is important!** If this is not checked then when you try to run your python code it won't be able to find the executable.

See: `Installing Python on Windows <https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html>`_

.. _git_bash:

Terminal
---------

If you are confident in your use of the "DOS Box" or "powershell", command lines, feel free to use one of those. However, your life may be easier if you install "Git Bash", as then you can follow unix-style terminal instructions exactly, and do not have to translate. Also, your instructors are more experienced with Bash.

From now on, if you hear the terms "bash", "shell" or "terminal", or "command line" know that this is the application that is being referred to. We will use those terms interchangeably to mean ANY command line.

When you install Git Bash, you are installing git (and a git gui) as well, thus killing two birds with one stone!

https://git-for-windows.github.io/

Select the download button on the page and launch downloaded executable, then follow the prompts. On "Choosing default editor used by Git" step it is best to select Notepad++ (which you need to have installed first) unless you are comfortable with non-graphical editors like vim.
You can go through the rest of the prompts using default values. Once you are done, a terminal window should pop up - try out some commands like ``ls`` or ``git help``.

You can use this git with the DOS box or Powershell as well.

This is also a good bet for running Python -- If you use the Git Bash shell, you can use the same commands as Linux and OS-X users. Regardless of which shell you choose, you will need to add Python to your environment. It is possible that this was done during the installation of Python. If you type 'which python' into your terminal, and get back the answer '/c/python37/python', then you are good to go, otherwise (which shouldn't happen if you checked the "Add Python 3.7 to PATH" checkbox when you installed Python above), follow the instructions here:

http://www.computerhope.com/issues/ch000549.htm

You will want to add:

``C:\Users\YourUserName\AppData\Local\Programs\Python\Python37``

and

``C:\Users\YourUserName\AppData\Local\Programs\Python\Python37\Scripts``

to ``PATH``

Here are steps for updating path:

::

    cd
    touch .bash_profile

You can edit this file using Notepad, locate this file in File Explorer in This PC > Local Disk > Users > YourUsername

Add to the file (file should be empty):

::

    PATH=$PATH:/C/Users/YourUserName/AppData/Local/Programs/Python/Python37:/C/Users/YourUserName/AppData/Local/Programs/Python/Scripts

Note: your python executable may be located in a different path, to check the path you need to start windows shell (``cmd``) and type ``where python`` - this command will output where python is currently installed.

Save the file and start a new gitbash shell.

Once you have done that, you should be able to type ``python`` at the command prompt, and get something like:

::

  Python 3.7.0 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  [GCC 4.2.1 (Windows build 7584) (dot 3)] on win64
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

This is the Python interpreter.

Type ``ctrl+Z`` to get out (or ``exit()``)

Note: if you have trouble running ``python`` command in your gitbash (it hangs), try running this instead: ``winpty python``. To avoid having to type ``winpty python`` all the time, it's strongly recommended that you create an alias like below:

::

  $ echo "alias python='winpty python'" >> ~/.bash_profile

You will need to close the current bash window and restart a new one to get this alias. Then from now on, you can just type ``python`` and it should work on git bash (no more hanging) as well.

git
---

If you installed Git Bash, you will already have git, both usable in the terminal and as a gui, and can safely skip this section. If not, you still need a git client. You can use the above link and install git (it will install the bash shell as well, of course, but you can use your shell of choice instead).

There is also TortoiseGit:

https://code.google.com/p/tortoisegit/

Which integrates git with the file manager. Feel free to use this if you already have an understanding of how git works, but for the purposes of learning, it may be better to use a command line client (git Bash above).


pip
---

``pip`` is the Python package installer. It is updated faster than Python itself, so once you have Python you want to get the latest version of pip working::

  $ python -m ensurepip --upgrade

It should download and install the latest ``pip``.

You can now use pip to install other packages.

The first thing you may want to do is update pip itself:

.. code-block:: bash

  $ python -m pip install --upgrade pip

Using pip:
----------

To use pip to install a package, you invoke it with this command::

  python -m pip install the_name_of_the_package

Where ``python`` is the command you use to invoke the Python you want to use .

**NOTE:** You will frequently see advice to use pip like so::

  $ pip install something_or_other

Which often works, but also can invoke the *wrong* version of pip. The above command::

  $ python -m pip install something_or_other

calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of Python that you are running.


iPython
--------

One extra package we are going to use from the beginning in the program is ``iPython``::

  $ python -m pip install ipython

(It will install a LOT)

You should now be able to run ``iPython`` from the git bash shell or "DOS Box" or PowerShell::

    $ ipython
    Python 3.7.0 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
    (or from the DOS box or PowerShell prompt)

We will use this in class as our default Python interpreter.


Testing it out
--------------

To be ready for the program, you need to have:
 - python
 - pip
 - iPython
 - git

All available from the command line.

To try it out, you should be able to run all of these commands, and get something like the following results:

(recall that you can get out of the python or iPython command lines with ``ctrl+Z`` (if that doesn't work, try ``ctrl+D`` -- the \*nix version))

For Python:

::

  hosun@DESKTOP-GJT06Q0 MINGW64 ~
  $ python
  Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> ^Z


For iPython:

::

  hosun@DESKTOP-GJT06Q0 MINGW64 ~
  $ ipython
  Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
  Type 'copyright', 'credits' or 'license' for more information
  IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

  In [1]:
  Do you really want to exit ([y]/n)? y


For pip:

::

  hosun@DESKTOP-GJT06Q0 MINGW64 ~
  $ python -m pip --version
  pip 18.0 from C:\Python37\lib\site-packages\pip (python 3.7)


For git:

::

  hosun@DESKTOP-GJT06Q0 MINGW64 ~
  $ git --version
  git version 2.18.3.windows.1

