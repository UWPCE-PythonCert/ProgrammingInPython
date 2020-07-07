.. _exercise_mailroom_part2_dict_files:


Mailroom Part 2
=================

**Incorporate file writing and dictionary use.**

Use dicts where appropriate.
----------------------------

Part 1 of this assignment used these basic data types: numbers, strings, lists and tuples.

However, using dictionaries, covered in Lesson 4, will let you re-write your program a bit more simply and efficiently.

Update your mailroom program to:

  - Use dicts where appropriate.

  - See if you can use a dict to switch between the user's selections.

  - See if you can use a dict to switch between the users selections.
    see :ref:`dict_as_switch` for what this means.

  - Convert your main donor data structure to be a dict.

  - Try to use a dict and the ``.format()`` method to produce the letter as one
    big template, rather than building up a big string that produces the letter in parts.


Example:

.. code-block:: ipython

  In [3]: d
  Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


  In [5]: "My name is {first_name} {last_name}".format(**d)
  Out[5]: 'My name is Chris Barker'

Don't worry too much about the ``**``. We'll get into the details later, but for now it means, more or less, "pass this whole dict in as a bunch of keyword arguments."


Update mailroom with file writing.
----------------------------------

**Goal: Write a full set of letters to all donors to individual files on disk.**

In the first version of mailroom, you generated a letter to a donor who had just made a new donation, and printed it to the screen.

In this version of your program, add a function (and a menu item to invoke it), that goes through all the donors in your donor data structure, generates a thank you letter for each donor, and writes each letter to disk as a text file.

Your main menu may look something like::

  Choose an action:

  1 - Send a Thank You to a single donor.
  2 - Create a Report.
  3 - Send letters to all donors.
  4 - Quit

The letters should each get a unique file name -- you can keep it really simple and just use the donor's name or add a date timestamp for additional uniqueness.

You want to avoid specifying a hardcoded file path when creating the files, for example don't to this:

.. code-block:: python

    open("/home/users/bob/dev/mailroom/thank_you.txt", "w")


Doing so will prevent other users from running the program as it will fail to find your path. Instead, you can create files in the current working directory or you can use a temporary directory.
To identify a temporary directory you can use a handy function like `tempfile.gettempdir() <https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir/>`_ which is also OS agnostic (meaning it can handle temp directory differences between different operating systems).

After running the "send letters to everyone" option, you should see some new files in the directory. There should be a file for each donor in the database, in this case 4.

After choosing action (3) above, using my example database, I get these files::

  Jeff_Bezos.txt
  Mark_Zuckerberg.txt
  Paul_Allen.txt
  William_Gates_III.txt

(If you want to get really fancy, ask the user for a directory name to write to!)

An example file content looks like this::

  Dear Jeff Bezos,

          Thank you for your very kind donation of $877.33.

          It will be put to very good use.

                         Sincerely,
                            -The Team

Feel free to enhance your letter template with some more information about past generosity, etc....

The idea is to require you to structure your code so that you can write the same letter to the screen or to disk (and thus anywhere else) and also exercise a bit of file writing. Remember to review the `with <http://www.diveintopython3.net/files.html#with>`_ statement as it is the preferred method when working with files.

