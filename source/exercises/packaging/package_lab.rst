LAB: A Small Example Package
============================

* Create a small package

  - package structure

  - ``setup.py``

  - ``python setup.py develop``

  - ``at least one working test``


* Here is a ridiculously simple and useless package to use as an example:

:download:`capitalize.zip <capitalize.zip>`

Unzip that, and you will find::

    capital_mod.py: The module that does the "real work"

    cap_data.txt: A data file needed by the module

    main.py: the actual main function that runs the script.

    cap_script.py: A simple top-level script -- all it does is call ``main``

    test_capital_mod.py: test code for the module

    sample_text_file.txt: an example file you can use to try it out.

Your mission is to put all these files in an package hierarchy, and then write a simple ``setup.py`` file that will build and install it as a package.


