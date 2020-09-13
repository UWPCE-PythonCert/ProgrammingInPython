.. _exercise_mailroom_full_testing:


Mailroom With Full Unit Tests
=============================

You should now have a version of the mailroom program that has complete tests for all the logic code.
That is: every function in mailroom that does not contain a ``print`` or ``input`` call should be tested.

And, critically: every function that contains a ``print`` or ``input`` should contain *no other logic at all*.

But now you've learned about more advanced techniques, like mocking and parameterized tests, so you should be able get your mailroom tests to 100% coverage -- and maybe even make the tests more efficient and complete with some other techniques.

The Task
--------

Use mocking of the ``input()`` function to write a full set of tests for the interactive portion of your mailroom program.

Then run ``coverage`` and make sure everything is covered -- if not, then find those holes and fill them. You should be able to provide a report indicating 100% coverage.




