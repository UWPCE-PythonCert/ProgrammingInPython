.. _python_for_linux:

###########################
Setting Up Linux for Python
###########################


Debian and Related Distros (Ubuntu, Linux Mint)
===============================================

Python
-------

For this program, you need Python3.6.* or 3.7.*

Debian distros already have the stable python2 and python3 releases preinstalled (`Debian Wiki <https://wiki.debian.org/Python>`_).

Try the following command:

.. code-block:: bash

  $ python3
  Python 3.6.3 (default, March 26 2017, 15:33:32)
  [GCC 4.9.2 on linux]
  >>>

I'm pretty sure that 18.4 (the most recent long term support release) has 3.6, if so, you are set.

That's nice, which one is the default version? Just type ``python`` to see. It's probably python2 still:

.. code-block:: bash

  $ python
  Python 2.7.9 (default, April 2 2015, 15:33:32)
  [GCC 4.9.2 on linux2]
  >>>

If you want to make ``python3.6`` the default version then add the line ``alias python=python3`` to your user's ``/home/{user}/.bashrc`` file like so:

.. code-block:: bash

  $ # before the change
  $ python
  Python 2.7.9 (default, April 2 2015, 15:33:32)
  [GCC 4.9.2 on linux2]
  >>>

  $ echo "alias python=python3" >> ~/.bashrc
  $ echo "alias pip=pip3" >> ~/.bashrc
  $ echo "alias ipython=ipython3" >> ~/.bashrc
  $ source ~/.bashrc

  $ # after the change
  $ python
  Python 3.6.3 (default, March 26 2017, 15:33:32)
  [GCC 4.9.2 on linux]
  >>>

Alternatively, you can always remember to type ``python3`` whenever you want Python.

Note: your version number may vary, but it needs to be ``3.6.*`` or ``3.7.*``

You may not have pip and ipython installed yet, but you will as you follow the instructions below.

If you don't have the version you want installed then use the package manager to find and install it:

.. code-block:: bash

   $ # search the package manager for it
   $ sudo apt-cache search python | grep '^python3.7\ -'
   python3.7 - Interactive high-level object-oriented language (version 3.7)
   $ # install it
   $ sudo apt-get install python3.7

(If you cant find 3.7, try 3.6 instead)

Terminal
---------

Every Linux box has a terminal emulator -- find and use it.



pip
---

``pip`` is the Python package installer.

Many Python packages are also available directly from your distro -- but you'll get the latest and greatest if you use ``pip`` to install it instead.

To get pip, the first option is to use your system package manager, something like:

.. code-block:: bash

    $ sudo apt-get install python3-pip

If that doesn't work, then try "ensure-pip":

.. code-block:: bash

    $ python3 -m ensurepip --upgrade


  $ python3 -m ensurepip --upgrade

You can now use pip to install other packages. The first thing you may want to do is update pip itself:

.. code-block:: bash

  $ python3 -m pip install --upgrade pip

Using pip:
----------

To use pip to install a package, you invoke it with this command::

  python3 -m pip install the_name_of_the_package

Where ``python3`` is the command you use to invoke the Python you want to use (could be ``python3``)

**NOTE:** You will frequently see advice to use pip like so::

  $ pip install something_or_other

Which often works, but also can invoke the *wrong* version of pip. The above command::

  $ python3 -m pip install something_or_other

calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of python that you are running (in this case python3).


iPython
--------

One extra package we are going to use in class is ``iPython``::

  $ sudo python3 -m pip install ipython

You should now be able to run ``iPython``::

  $ ipython3
  Python 3.6.4 ()
  Type "copyright", "credits" or "license" for more information.

  IPython 2.0.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.

git
----

Git is likely to be there on your system already, but if not:

.. code-block:: bash

    $ sudo apt-get install git

==================================================
Fedora and Red Hat Related Distros (CentOS)
==================================================

.. warning::

	CentOS is probably the most popular distro of these related flavors. However, getting Python3 on it can be a pain. You have been warned! (but there are lots of tutorials on the web -- google "install python3 on CentOS")


Python
-------

Fedora distros already have the stable python2 and python3 releases preinstalled `[2] <Fedora Wiki>`_. However, CentOS, the most popular distro only has the stable python2 release. Try the following commands:

.. code-block:: bash

	[centos@ip-172-31-21-5 ~]$ python2
	Python 2.7.5 (default, Jun 17 2014, 18:11:42)
	[GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>>

	[centos@ip-172-31-21-5 ~]$ python3
	-bash: python3: command not found


Let's install python3 using the package manager. Step one install "Software Collections" to help us:

.. code-block:: bash

   $ sudo yum -y install scl-utils

Then go to the `software collections listing <https://www.softwarecollections.org/en/scls/>`_ and click on the Python collection version you want to install.

Probably this one:

https://www.softwarecollections.org/en/scls/rhscl/rh-python35/


Note, you also need to know which version of CentOS you are using (probably 6 or 7). For example, we care about `python version 3.5` so let's go the `.rpm` i want to install `here <https://www.softwarecollections.org/repos/rhscl/rh-python35/epel-7-x86_64/noarch/>`_:

.. code-block:: bash

	$ # add this package to the rpm package manager
	$ sudo rpm -Uvh https://www.softwarecollections.org/repos/rhscl/rh-python34/epel-7-x86_64/noarch/rhscl-rh-python35-epel-7-x86_64.noarch.rpm

	$ # install the right python version
	$ sudo yum install rh-python35

When you want to use python3 run this command:

.. code-block:: bash

	[centos@ip-172-31-21-5 ~]$ scl enable rh-python35 bash


Terminal
---------

Every Linux box has a terminal emulator -- find and use it.


git
----

Git is likely to be there on your system already, but if not:

.. code-block:: bash

    $ sudo yum install git

pip
---

``pip`` is the Python package installer.

Many Python packages are also available directly from your distro -- but you'll get the latest and greatest if you use ``pip`` to install it instead.

In CentOS, if you used the above technique to install Python3, then it comes with pip. Try:

.. code-block:: bash

	[centos@ip-172-31-21-5 ~]$ python -m pip -V
	pip 8.1.2 from /opt/rh/rh-python35/root/usr/lib/python3.5/site-packages (python 3.5)

Using pip:
----------

To use pip to install a package, you invoke it with this command::

  python -m pip install the_name_of_the_package

Where ``python`` is the command you use to invoke the Python you want to use (could be `python3`)

**NOTE:** You will frequently see advice to use pip like so::

  $ pip install something_or_other

Which often works, but also can invoke the *wrong* version of pip. The above command::

  $ python -m pip install something_or_other

calls Python, and tells it to run the ``pip`` module. It is exactly the same as calling pip directly, except that you are assured that you are getting the version of pip connected the version of python that you are running.

iPython
--------

One we are going to use in class is ``iPython``::

  $ sudo pip install ipython[all]

You should now be able to run ``iPython``::

    $ ipython3
	Python 3.5.2 ()
	Type "copyright", "credits" or "license" for more information.

	IPython 5.1.0 -- An enhanced Interactive Python.
	?         -> Introduction and overview of IPython's features.
	%quickref -> Quick reference.
	help      -> Python's own help system.
	object?   -> Details about 'object', use 'object??' for extra details.


Footnotes:
==========

Debian Wiki
===========

https://wiki.debian.org/Python

Fedora Wiki
=============

https://fedoraproject.org/wiki/Packaging:Python

