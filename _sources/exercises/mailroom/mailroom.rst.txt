.. _exercise_mailroom_part1:


Mailroom
========


**Overall Assignment Structure**

This is the first in a multi-part exercise that will make use of your Python programming skills as you develop them during this course. You will start work on the program in this assignment, and then you will build on it in future lessons, as you learn more of Python's powerful features.

This progressive work will give you a strong foundation for success in the final project, a Mailroom program using object-oriented structure, fully tested, and bundled up as a Python package.


Overall Program Goal:
---------------------

You work in the mail room at a local charity. Part of your job is to write
incredibly boring, repetitive emails thanking your donors for their generous
gifts. You are tired of doing this over and over again, so you've decided to
let Python help you out of a jam and do your work for you.


The Program:
------------

Write a small command-line script called ``mailroom.py``. This script should be executable. The script should accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each. You can store that data structure in the global namespace.

* The script should prompt the user (you) to choose from a menu of 3 actions:
  "Send a Thank You", "Create a Report" or "quit".

Send a Thank You
----------------

* If the user (you) selects "Send a Thank You" option, prompt for a Full Name.

  * If the user types ``list`` show them a list of the donor names and re-prompt.
  * If the user types a name not in the list, add that name to the data structure and use it.
  * If the user types a name in the list, use it.
* Once a name has been selected, prompt for a donation amount.

  * Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
  * Add that amount to the donation history of the selected user.

* Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.

Create a Report
-----------------

* If the user (you) selected "Create a Report," print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations, and average donation amount as values in each row. You do not need to print out all of each donor's donations, just the summary info.
  - Using string formatting, format the output rows as nicely as possible.  The end result should be tabular (values in each column should align with those above and below).
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return
  to the original prompt.

* From the original prompt, the user should be able to quit the script cleanly.


Your report should look something like this::

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14

Guidelines
----------

First, factor your script into separate functions. Each of the above
tasks can be accomplished by a series of steps.  Write discreet functions
that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive
programs are a classic use case for the ``while`` loop.

Of course, ``input()`` will be useful here.

Put the functions you write into the script at the top.

Put your main interaction into an ``if __name__ == '__main__'`` block.

Finally, for Part 1 use only functions and the basic Python data types you've learned
about so far in Lessons 1-3. There is no need to go any farther than that for this assignment.

If you're having a hard time getting started, or need some pointers, you should read the tutorial here: :ref:`exercise_mailroom_part1_tutorial`

