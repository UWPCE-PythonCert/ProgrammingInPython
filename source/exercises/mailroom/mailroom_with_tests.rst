.. _exercise_mailroom_testing:


Mailroom With Unit Tests
========================

**Add a full suite of unit tests.**

"Full suite" means all the code is tested. In practice, it's very hard to test the user interaction, but you can test everything else. Therefore you should make sure that there is as little logic and untested code in the user interaction portion of the program as possible.

This is a big step; you may find that your code is hard to test. If that's the case, it's a good sign that you *should refactor your code*.

I like to say: "If it's hard to test, it's not well structured."

Put in the tests **before** you make the other changes below. That's much of the point of tests. And while in this case, it's not really TDD, as you already have working code, you still want to write the tests as early as possible, so you know your refactored code is correct.

Guidelines
----------

Here are some suggestions on what should be refactored in your mailroom code.

As mentioned above, testing user interaction code (code with ``print`` and ``input`` functions) is harder than testing the rest of your code.
Testing user interaction code requires more advanced unit testing methodologies that will be revisited in future courses.
Therefore, you should refactor your code so that the user interaction code contains as little business logic as possible.
It should only interact with the user either by asking them for input or by responding to their request to print out data.
Separating business logic from user interaction code is a good practice in general and we will come back to this concept in later lessons.

The refactoring in this lesson will allow you to unit test the functions with business logic, even if you don't test the user interaction code.

We will go over the components that should be refactored so that you are able to unit test your mailroom. After the refactor, your code should improve and be better modularized. If that's not the case then maybe you should revisit your refactoring approach.

For unit testing framework you should use `pytest <https://docs.pytest.org/en/latest/>`_; it has a simple interface and rich features.


Mailroom Code Structure
-----------------------

Your code should have 3 main features so far:

* Send a thank you (adds a new donor or updates existing donor info)
* Create a report
* Send letters (creates files)


Send Thank You
...............

Even though every mailroom implementation will be unique, most likely this function will require a significant refactor for most of you.
You can break up the code into components that handle user interaction and data manipulation logic. Your unit tests should test the data manipulation logic code: generating the thank you text, adding or updating donors, and listing donors.


Create Report
.............

This function should only need slight modification. Split up user presentation (``print`` function calls) and data logic (actual creating of rows).
Your data logic function can either return the report string already formatted or return a list of formatted rows that can be joined and printed in the user presentation function.

This allows you to write a unit test for your data logic function.

Example:

.. code-block:: python

    def display_report():
        for row in get_report():
            print(row)


Here you would write a unit test for ``get_report`` function. Remember: TDD -- write that test *before* the function!

Send Letters
............

This function should require very little or no change to make it unit-testable.
To make it testable, you'll need to follow the same "separation of concerns" approach: the code that creates the letters should be separate from the code that prints them to the screen.
This both allows you to test the letter creation, and leaves the door open to do something else with the letters: save to to a file, send as an email, etc.
So the code that makes a letter likely will return a string with the entire letter contents.

For example:

.. code-block:: python

    def get_letter_text(name):
        """Get letter text for file content"""
        return f"{name}, thanks a lot!"


    def test_get_letter_text():
        expected = "Frank, thanks a lot!"
        assert get_letter_text("Frank") == expected

Note that some thought should go into the test of the letter. If it's really simple, then simiply comparing to a full letter is OK. But it might be better to test the important parts of the letter: Does it contain the correct name? does it contain the right amounts of money? rather than the entire text.

When you are done, every function in mailroom that does not contain a ``print`` or ``input`` call should be tested.

And, critically: every function that contains a ``print`` or ``input`` should contain *no other logic at all*.

Yes, that does mean that that you'll have some very simple functions like:

.. code-block:: python

def print_letter(donor):
    print(make_letter(donor))

But trust me -- that is a Good Thing™

.. note:: Testing print() is rearely neccesasry if you factor your code correctly. But it would be able to test your menu code with `input()` in it. This is a pretty advanced topic, but if you want to give it a try, there is more on advanced testing here: :ref:`advanced_testing`

 



