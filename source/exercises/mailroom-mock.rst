.. _exercise_mailroom_mocking:

Mocking Mailroom
================

You should now have a nice mailroom program, complete with an object-oriented structure and bundled up into a nice python package.

And a complete set of unit tests for the logic code.

But your command line user interface code is likely not tested. It's hard to auto-test user-interaction...

Your mission is to get mailroom fully tested.

Start with your object oriented mailroom in a proper python package.

Coverage
--------

First run coverage on your current tests. I like pytest-cov:

.. code-block:: bash

  $ pip install pytest-cov

  $ pytest --cov=mailroom

or, to get the nifty html output:

.. code-block:: bash

  $ pytest --cov=mailroom --cov-report html

That will result in a pile of html in an ``htmlcov`` directory -- point your browser to the index.html file in there, and click away...

Once you've run coverage -- add tests to get it up close to 100% on your logic code.

Fixtures
--------

Fixtures are a really good way to make your tests cleaner and more independent. With mailroom, you should have a couple fixtures that set up a donor database with some data in it -- and maybe one or two for ``Donor`` objects.

Clean up your tests with fixtures -- and keep the coverage up!

One possible use for a fixture is providing a file to write to for the code that writes files. Or maybe a directory to put the files in, and then it can clean up the dir in teardown.


Mocking input
-------------

Once you have 100% coverage for the logic code -- it's time to test the UI.

You should be able to use mocking to mock the ``input`` function, and then actually test your user interface code, too.

Can you get 100% test coverage?



