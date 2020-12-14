.. _exercise_mailroom_oo:

##########################
Mailroom - Object Oriented
##########################

Making Mailroom Object Oriented.

**Goal:** Refactor the mailroom program using classes to help organize the code.

The functionality is the same as the earlier mailroom(s).

But this time, we want to use an OO approach to better structure the code to make it more extensible.

It was quite reasonable to build the simple mailroom program using a
single module, a simple data structure, and functions that manipulate
that data structure. In fact, you've already done that :-)

But if one were to expand the program with additional functionality, it
would start to get a bit unwieldy and hard to maintain. So it's a pretty good candidate for an object-oriented approach.

As you design appropriate classes, keep in mind these three guidelines for good code structure:


1) Encapsulation: You have a data structure that holds your data, and functions that manipulate that data; you want data and methods "bundled up" in a neat package so that everything that works with that data structure are within one unit. The rest of the code doesn't need to know about the data structure you are using.

2) Separation of Concerns: The user-interaction code should be cleanly separated from the data handling code.

   https://en.wikipedia.org/wiki/Separation_of_concerns

   There should be no use of the ``input()`` function in the classes that hold the data!  Nor any use of ``print()`` -- these are for user interaction, and you want the data handling code to be potentially usable with totally different user interaction -- such as a desktop GUI or Web interface.

In the spirit of separation of concerns, you also want keep your Command Line Interface code in a separate file(s), as they already should be in your mailroom-as-a-package version. In fact, you should be able to keep the structure of your package pretty much the same -- simply replacing the model code with classes.


3) As always: **DRY** (Don't Repeat Yourself): Anywhere you see repeated code; refactor it!


The Program
===========

See: :ref:`exercise_mailroom_part1` to remind yourself what the program needs to do.


Guidelines
-----------

One of the hardest parts of OO design (particularly in Python) is to know how "low" to go with the classes and data structures. In particular, you might have a bit of data collected together (say, a donor's name and donation history). This can be a simple tuple with a few items in it; a dict with those same data available as ``key:value`` pairs; or a class, with class attributes (and, possibly, methods).

There are no hard and fast rules, but here are some guidelines:

For this simple problem, simple tuples could work fine. However, in order for the code to be more flexible in the future: for example, if new "fields" were added to the donor object, it's probably better to use a more structured data type, so you don't have to worry about changing the order or number of fields.

So now you have to think about using a dict or class. Again for flexibility, a dict is a bit easier; you can add fields to it very easily. However, with a class, you can build some functionality in there, too. This is where encapsulation comes in. For instance, one thing you might want to do is get the total of all donations a donor has made in the past. If you add a method to compute that (or a property!), then the rest of the code doesn't need to know how the donations are stored.

Consider ``data[0]`` (stored in a tuple) vs ``data["name"]`` (stored in a dict) vs ``data.name`` (a class).
Which one is more readable?
Keep in mind that another benefit of using OO for data encapsulation is ability of modern IDEs to provide auto-completion, which reduces the number of bugs and helps to produce code faster.

Another way to think about it is "data" vs "code" -- dicts are for data, classes are for code.
Sometimes it's not totally clear which is which, but if you think about how static is, that can be be a guide.
In this example, every donor is going to have a name, and a donation history, and maybe in the future a bunch of other information (address, email, phone number ....).
Whatever it is, every donor will have the same set -- so it's good to use code to manage it.

Below are more detailed suggestions on breaking down your existing code into multiple modules that will be part of a single mailroom program.


Modules and Classes
...................

You may organize your code to your preference and keep it simple by having all of the model code in a single file. But you should at least separate the code that manipulates data (the "model" code) from the command line interface code, as you did for mailroom-as-a-package.

Optionally, you could further organize your model code into separate modules: maybe one for the Donor object, one for the DonorCollection object.

What is a module? A module is a python file with a collection of code that can be imported into other python files.

Modules can contain functions, classes, and even variables (constants).

Here is an example file structure for ``mailroom_oo`` package -- it should be similar to what you already have:

::

  └── mailroom
     ├── __init__.py
     ├── cli.py
     ├── model.py
     └── tests
        ├── __init__.py
        ├── test_cli.py
        └── test_model.py


The module ``model.py`` can contain the ``Donor`` and ``DonorCollection`` classes.

The module ``cli.py`` would include all of your user interaction functions and main program flow (and a ``main()`` function that can be called to start up the program (and used as an entry_point).


``Donor`` Class
...............

**Class responsible for donor data encapsulation**

This class will hold all the information about a *single* donor, and have attributes, properties, and methods to provide access to the donor-specific information that is needed.
Any code that only accesses information about a single donor should be part of this class.


``DonorCollection`` Class
.........................

**Class responsible for donor collection data encapsulation**

This class will hold all of the donor objects, as well as methods to add a new donor, search for a given donor, etc. If you want a way to save and re-load your data, this class would hold that method, too.

Your class for the collection of donors will also hold the code that generates reports about multiple donors.

In short: if the functionality involves more than one donor -- it belongs in this class.

Note that the ``DonorCollection`` class should be holding, and working with, ``Donor`` objects -- it should NOT work directly with a list of donations, etc.

The main data structure in your class can be a dictionary with a key as donor name and value as donor object:


.. code-block:: python

    class DonorCollection:
        def __init__(self, *donors):
            self.donors = {obj.name: obj for obj in donors}


This design allows you to quickly look up donor by their name and get a donor object instance to work with.

Another option is to simply use a list of donor objects. You get to choose which you think is more appropriate.

Remember that you should use `self.donors` attribute in any methods that need access the individual donors. Most of your methods in this class will utilize it in some way. This is really what classes are designed for.

Note that external code probably shouldn't access the ``.donors`` list (or dict, or ...) directly but rather ask the DonorCollection class for the information it needs: e.g. if you need to add a new donation to a particular donor, calla method like ``find_donor()`` to get the donor you want, and then work with that Donor object directly.

**Examples:**

Generating a thank you letter to a donor only requires knowledge of that one donor -- so that code belongs in the ``Donor`` class.

Generating a report about all the donors requires knowledge of all the donors, so that code belongs in the ``DonorCollection`` class.

.. note:: You've previously sorted simple data structures like list and dictionaries, but here we're dealing with objects -- not to worry, that is a really simple thing to do with python! You can use ``operator.attrgetter`` with the ``sorted`` function (review the python docs for usage documentation) to make it easy to sort based on various attributes of a Donor.


Command Line Interface
.......................

**Module responsible for main program flow (CLI - Command Line Interface)**

Let's call this module ``cli.py``.  This module will be using the classes we defined: ``Donor`` and ``DonorCollection``.
It will also handle interaction with the user via the ``input`` function calls that gather user input and to provide the output to the console.

What should go into this module?

A set of user-interaction menu functions -- to handle each of the modes of the program.

These will include ``input()`` function calls to gather user input, and ``print()`` functions to print results to console.

.. note:: Console print statements don't belong in your data classes. So for features such as "send letters," in which we are simply printing instead of "sending", the data class methods should return a string, and let the UI code do the printing. This will mean there may be very simple functions in the UI code that simply call a method and print the results -- but that does keep flexibility for other ways of handling user interaction.

.. rubric:: Why is this separation of data and method so important?

The idea here is that we should be able to fairly easy replace this CLI program with a different type of interface,
such as a GUI (Graphical User Interface), without having to make any changes to our data classes.
If that was the case, then you would implement the GUI elements and use your data classes the same way as they are used in CLI.

Note that this arrangement is a one-way street: the CLI code will need to know about the Donor and DonorCollection classes, but the model code shouldn't need to know anything about the CLI code: it manages the information, and returns what's asked for (like a donor letter or report), but it doesn't know what is done with that information.

In short: the cli.py module will import the model module, but the model module shouldn't import the cli module.


Test-Driven Development
-----------------------

At this point we have done a great job refactoring the more complex code out of data-holding classes and we are left with simple classes that are more straightforward to unit test. As you build your classes, update the tests you already have to the logic code to the new API. Ideally, update the tests first, then the code.

The ``Donor`` and ``DonorCollection`` classes should now have 100 percent code coverage, which means that every line of code in your ``donor_models.py`` file will be run at least once when your tests are run.

For the moment, don't worry about testing most of the command line interface code. That requires simulating user input, which is an advanced testing topic. But you can (hopefully) see some of the benefits of separating the user-interaction code from the logic code; your logic code is much easier to test with no user-interaction involved.

.. rubric:: refactoring non-OO code

In this case, you already have working code without an OO structure. You should be able to re-use a fair bit of your existing code.
However, you should still start with the OO structure/design.
That is, rather than take a non-OO function and try to make it a method of a class, decide what method you need, and what it's API should be, and then see if you have code you can use to fill in that function.

You should expect to re-use a lot of the command line interface code, while refactoring most of the logic code.

If you are not sure at the start what functionality you data classes will need, you can start with the CLI code, and as you find the need for a function, add it to your model classes (after writing a test first, of course).


Exercise Guidelines
===================

OO mailroom is the final step in the mailroom project. And you are near the end of the class.

So this is your chance to really do things "right". Strive to make this code as good, by every definition, as you can. If you have gotten feedback from your instructors, now is the chance to incorporate recommended changes.

With that in mind:

Functionality
-------------

* The logic is correct -- i.e. the program works :-)

* The logic is robust -- you are handling obvious expected errors reasonably:

  - User inputting a non-number as a donation

  - Trying to make a negative donation

  - User getting capitalization or spacing or ??? wrong with a name.

    - Maybe add logic where you tell them that the name is not in the DB, and do they want to create it, rather than simply creating a new record for a typo in a donor name.

.. rubric:: Code structure

* Classes should have clear purpose and encapsulation: only the code within a class should know exactly how the data are stored, for instance.

* Anything that only needs to know about one donor should be in the ``Donor`` class

* Anything that needs to know about the collection should be in a ``DonorCollection`` class.

* Any user interaction should be outside the "logic" code. (Sometimes called the "Model", or "Business logic")

  - You should be able to re-use all the logic code with a different UI -- Web App, GUI, etc.

  - There should be no ``input()`` or ``print()`` functions in the logic code.

  - The logic code should be 100% testable (without mocking ``input()`` or any fancy stuff like that)

.. rubric:: Testing

* All logic code should be tested.

* Tests should be isolated to test one thing each

* Tests should (reasonably) check for handling of weird input.

* Tests should be isolated -- that is, they will work if run by themselves, and in any order.

  - This means they should not rely on any global state.

  - you'll probably find this easier with a well structured OO approach -- that is, you can test an individual donor functionality without knowing about the rest of the donors.


.. rubric:: The "soft" stuff:

Style:
    - Conform to PEP8! (or another consistent style)
      (You can use 95 char or some other reasonable number for line length)

Docstrings:
    Functions and classes should all have good docstrings. They can be very short if the function does something simple.

Naming:
    All classes, functions, methods, attributes, variables should have appropriate names: meaningful, but not too detailed.


Extra Ideas:
------------

In case you are bored -- what features can you add?

* Fancier reporting

* More error checking -- does the user really want to create a new donor? or was it a typo in the donor name?

* The next project is an html renderer -- maybe use it to make a nice html report?

* The sky's the limit!
