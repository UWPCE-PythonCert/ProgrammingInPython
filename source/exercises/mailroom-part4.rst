.. _exercise_mailroom_part4_testing:

Mailroom Part 4
=================

**Add a full suite of unit tests.**

"Full suite" means all the code is tested. In practice, it's very hard to test the user interaction, but you can test everything else. Therefore you should make sure that there is as little logic and untested code in the user interaction portion of the program as possible.

This is a big step; you may find that your code is hard to test. If that's the case, it's a good sign that you *should* refactor your code.

I like to say: "If it's hard to test, it's not well structured."

Put in the tests **before** you make the other changes below. That's much of the point of tests. You can know that you haven't broken anything when you refactor!

.. Confusing last sentence. Do you mean that if you test the components beforehand, you will know that the components work before refacotring so that any breakage that occurs after refacatoring will have been caused by the refactoring? 

Guidelines
----------

Here are some suggestions on what should be refactored in your mailroom code.

As mentioned above, testing user interaction code is harder (code with ``print`` and ``input`` functions) then testing the rest of your code. Testing user interaction code requires more advanced unit testing methodologies that will be revisited in future courses. Therefore, you should refactor your code so that the user interaction code contains as little business logic as possible. It should only interact with the user either by asking them for input or by responding to their request to print out data. Separating business logic from user interaction code is a good practice in general and we will come back to this concept in later lessons.

The refactor in this lesson will allow you to unit test functions with business logic.

We will go over the components that should be refactored so that you are able to unit test your mailroom. After the refactor, your code should improve and be better modularized. If that's not the case then maybe you should revisit your refactor approach.

For unit testing framework you should use `pytest <https://docs.pytest.org/en/latest/>`_; it has a simple interface and rich features.

Your code should have 3 main features so far:

* Send a thank you (adds a new donor or updates existing donor info)
* Create a report
* Send letters (creates files)


Send Thank You
...............

Even though every mailroom implementation will be unique, most likely this function will require a significant refactor for most of you.
You can break up the code into components that handle user flow and data manipulation logic. Your unit tests should test the data manipulation logic code: generating thank you text, adding or updating donors, and listing donors.


Create Report
.............

This function should only need slight modification. Split up user presentation (``print`` function calls) and data logic (actual creating of rows).
Your data logic function can either return the report string already formatted or return a list of formatted rows that can be joined and printed in the user presentation function.
Then you can write a unit test for your data logic function.

Example:

.. code-block:: python

    def display_report():
        for row in get_report():
            print(row)



Here you would write a unit test for ``get_report`` function.

Send Letters
............

This function should require very little or no change to make it unit-testable.
The unit test can assert that a file is created per donor entry (hint: ``os.path`` module), and that the file content contains text as expected.

Note that you should test the file creation separately from testing the file content (that the correct text being generated). That way you don't need to read each file generated to know it contains correct text. So the function that generates the text should be separate from the function that writes the file.

.. entirely possible I made errors here. Not sure if the test is that the file contains text or that the file contains the correct text.

For example:

.. code-block:: python

    def get_letter_text(name):
        """Get letter text for file content"""
        return f"{name}, thanks a lot!"


    def test_get_letter_text():
        expected = "Frank, thanks a lot!"
        assert get_letter_text("Frank") == expected



