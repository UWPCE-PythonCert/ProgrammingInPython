.. _exercise_mailroom_part1_tutorial:


Mailroom Tutorial
=================

Controlling Main Program Flow
-----------------------------

One of the key components of the mailroom program is managing program flow and interacting with the user. Ideally main flow code should be cleanly separate from your feature code.

The best way to manage the program flow of an interactive prompt is to use a ``while True`` loop, which means you will keep asking the user for input until the user selects a feature or exits.

There are several ways to write your main interactive loop. Let's consider these two options:


Option 1:
.........

.. code-block:: python

    def do_something():
        # do things

    def main():
        while True:
            do_something()

    main()

Option 2:
.........

.. code-block:: python

    def do_something()
        # do things
        main()

    def main():
        do_something()

    main()


Can you see the advantages of one example over the other?

In the first one, ``do_something`` is not aware of how the main function works and as you add more features they don't need to know about how the main function works either.
The call stack will also keep getting deeper and deeper, which can make error stack traces hard to debug.

Another advantage is simpler code logic, and simpler code logic means fewer bugs!

Let's look at a simple program to utilize the ``while True`` loop and how we can handle user response:

.. code-block:: python

    import sys  # imports go at the top of the file


    fruits = ['Apples', 'Oranges', 'Pears']

    prompt = "\n".join(("Welcome to the fruit stand!",
              "Please choose from below options:",
              "1 - View fruits",
              "2 - Add a fruit",
              "3 - Remove a fruit",
              "4 - Exit",
              ">>> "))


    def view_fruits():
        print("\n".join(fruits))


    def add_fruit():
        new_fruit = input("Name of the fruit to add?").title()
        fruits.append(new_fruit)


    def remove_fruit():
        purge_fruit = input("Name of the fruit to remove?").title()
        if purge_fruit not in fruits:
            print("This fruit does not exist!")
        else:
            fruits.remove(purge_fruit)

    def exit_program():
        print("Bye!")
        sys.exit()  # exit the interactive script


    def main():
        while True:
            response = input(prompt)  # continuously collect user selection
            # now redirect to feature functions based on the user selection
            if response == "1":
                view_fruits()
            elif response == "2":
                add_fruit()
            elif response == "3":
                remove_fruit()
            elif response == "4":
                exit_program()
            else:
                print("Not a valid option!")


    if __name__ == "__main__":
        # don't forget this block to guard against your code running automatically if this module is imported
        main()



Choosing A Data Structure
-------------------------


So far in this course, we have learned about strings, tuples, and lists. We will apply these data structures to hold our mailroom donor information.
Choosing the right data structure is critical and our donor data structure will change in Parts 2 and 3 of this assignment as we learn about additional structures.

What goes into this decision to use a specific data structure? Here are a couple of things to consider.

* Efficiency: We often need to look up data; are you able to efficiently look up the data you need?
* Ease of use: Is the code straightforward and simple for basic operations?
* Features: Does the code do everything you need to do for your requirements?

Let's consider each data structure.

A simple string would probably be able to do what we need feature-wise but the code to implement these features would be quite complex and not very efficient.

A tuple would be an issue when adding donors since it is an immutable data structure.

A list would satisfy all of the needed features with a fairly simple code to implement. It makes the most sense to use a list for the main data structure. Actually, we can use a combination of both tuples and a list.

Here is a potential data structure to consider:

.. code-block:: python

    donor_db = [("William Gates, III", [653772.32, 12.17]),
                ("Jeff Bezos", [877.33]),
                ("Paul Allen", [663.23, 43.87, 1.32]),
                ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
                ]

Why choose tuples for the inner donor record? Well, another part of using the right data structure is to reduce bugs; you are setting clear expectations that a single donor entry only contains two items.


Sorting
-------

Python makes sorting fairly easy and has utilities for sorting simple lists as well as more complex structures like lists of tuples as above.

Let's start with a structure that represents student records: student name and age.

::

    >>> students = [('Bob', 39), ('Joe', 26), ('Jimmy', 40)]

We will use the ``sorted`` function to do the sorting and either sort by name or age. There are actually several ways to accomplish that, we will look at some of them.

The first option is to use optional ``key`` param, which accepts a function object - it can be any custom function we define as long as input and output are correctly implemented.

    >>> def sort_key(student):
            return student[1]
    >>> sorted(students, key=sort_key)
    [('Joe', 26), ('Bob', 39), ('Jimmy', 40)]

``sort_key`` function takes in a single parameter that represents the item in the list, in our case the student record, you then need to return which field should be used for sort comparison. We are using field at index 1, that's the age.


Another option is to use a ``itemgetter`` function from ``operator`` module, it accepts a parameter for list item index value, similar to our ``sort_key`` function:

    >>> from operator import itemgetter
    >>> sorted(students, key=itemgetter(1))
    [('Joe', 26), ('Bob', 39), ('Jimmy', 40)]
    >>> sorted(students, key=itemgetter(0))
    [('Bob', 39), ('Jimmy', 40), ('Joe', 26)]

Using second option makes the most sense in simple cases like above since we're not doing anything complicated and simply need to sort on the index. If our student record also included the last name:

    >>> students = [('Bob Mac', 39), ('Joe Acer', 26), ('Jimmy Lenovo', 40)]

Then the custom function becomes really handy to sort on the last name:

    >>> def sort_key(student):
            return student[0].split(" ")[1]
    >>> sorted(students, key=sort_key)
    [('Joe Acer', 26), ('Jimmy Lenovo', 40), ('Bob Mac', 39)]


Note: you might see a lot of examples online using the ``lambda`` statement, it is valid and can be used but isn't preferred because the syntax isn't elegant or very readable:

.. code-block:: python

    sorted(students, key=lambda x: x[0].split(" ")[1], reverse=True)

