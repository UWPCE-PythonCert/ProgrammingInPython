.. _windows_bash:

*****************************************
Using Windows Bash for Python Development
*****************************************

**CAUTION** -- none of the instructors in the program use this -- so this is experimental -- proceed at your own risk!

With Windows 10, Microsoft has introduced the "Windows Subsystem for Linux" (WSL). Technically, it's not Linux at all (it is not running the Linux kernel), but it does provide an actual bash shell, and access to much (all) of the packages available in Ubuntu Linux, providing a very Linux-like environment.

If you run Windows 10, but want to be able to work in an environment that is very much like Linux (and the OS-X command line) Windows-bash may be a good options for you.

Using WSL to Build a Python Development Environment on Windows
==============================================================

Here is a recent post about how to do Python with the "WSL":

https://pbpython.com/wsl-python.html

Let us know if it works for you!


Offical Docs
============

The following are some addition links, of that doesn't get it done:


Installing the System
---------------------

Here are MS's docs:

https://msdn.microsoft.com/commandline/wsl/about

and the install guide:

https://msdn.microsoft.com/en-us/commandline/wsl/install_guide


Installing / running Python
---------------------------

To use Python from within the bash shell, you probably want a "linux" Python, rather than the native Windows installer. Unfortunately, the Ubuntu version that Windows Bash is hooked up to does not natively have the latest Python version -:( (though it may now)

Using the environment
=====================

The WSL provides a full linux experience -- but, most importantly, it does not suport any GUI environment. If you are comfortable with a command line editor like vim or Emacs, then you can work entirely in the bash shell. However, you may very well want to work with a nice modern GUI editor like Sublime Text or Notepad++. This is quite possible, as the systems share a file system. From the FAQ:

  One of the benefits of WSL is being able to use the same file with both Windows and Linux apps or tools.

So you can manipulate and edit your files, as well as use the browser, etc, in regular Windows, and still run Python and git, etc in the bash shell.

