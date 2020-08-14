.. _exercise_mailroom_exceptions:


Mailroom With Exceptions
========================

**Improve your mailroom by adding exception handling**

Exceptions
----------

Now that you've learned about exception handling, you can update your code to handle errors better, such as when a user inputs bad data.

This is a great use case for "Easier to Ask Forgiveness Than Permission" (EAFTP)

For example, when you are asking the user for a donation amount, it should be a number. rather than trying to parse the text they input to make sure it's a number, simply try to "turn it into" an integer (or float, you decide), and if you get an error, you know they didn't pass in a number:

.. code-block:: python

    amount = input("how much?")
    try:
        amount = int(amount)
    except ValueError:
        # report the error and go back
        print("you need to provide a number")

    # If the code gets here, then you know that the amount is now an integer.

There may be other places in your code where handling an Exception would be helpful -- keep them in mind! You never want your program to crash if the error is recoverable.
