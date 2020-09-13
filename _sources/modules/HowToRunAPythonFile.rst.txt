.. _how_to_run_a_python_file:

How to run a python file
========================

A file with python code in it is a 'module' or 'script'

(more on the distinction later on...)

It should be named with the ``.py`` extension: ``some_name.py``

If you want to run the code directly (it is a script), you have a couple options:

1) call python on the command line, and pass in your module name

.. code-block:: bash

  $ python3 the_name_of_the_script.py

2) On \*nix (linux, OS-X, Windows bash), you can make the file "executable"::

       $ chmod +x the_file.py

   And make sure it has a "shebang" line at the top::

       #!/usr/bin/env python

   Then you can run it directly::

       ./the_file.py

3) On Windows, the `.py` extensions can be associated with the python interpreter, so it can be run directly. This is clunkier than the \*nix "shebang line" approach, so I don't recommend it -- but it is an option. But Windows does come with the "py" executable, that will examine a python file, look for a "shebang" line, and then run your file with the right executable.


4) run ``ipython``, and run it from within iPython with the ``run`` command

.. code-block:: ipython

  In [1]: run the_file.py

5) Various IDEs (PyCharm, IDLE, etc) have a way to run the module you are currently editing -- if you use one of these tools, learn how to do that. Make sure that it is using the version of Python that you want it to be.
