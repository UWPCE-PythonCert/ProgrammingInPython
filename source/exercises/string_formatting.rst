.. _exercise_string_formatting:

##########################
String Formatting Exercise
##########################

Goal
====
In this exercise we will reinforce the important concepts of string formatting, so that these start to become second nature!

Procedure
=========
Create a new file called ``strformat_lab.py`` in the exercise repo.

When the empty script is available and runnable, complete the following four tasks.


Task One
--------
* Write a format string that will take the following four element tuple:

    ``( 2, 123.4567, 10000, 12345.67)``

    and produce:

    ``'file_002 :   123.46, 1.00e+04, 1.23e+04'``


Let's look at each of the four tuple elements in turn:

1) The first element is used to generate a filename that can help with file sorting. The idea behind the "file_002" is that if you have a bunch of files that you want to name with numbers that can be sorted, you need to "pad" the numbers with zeros to get the right sort order.

To illustrate this further let's look at an example:

.. code-block:: ipython

    In [10]: fnames = ['file1', 'file2', 'file10', 'file11']
    In [11]: fnames.sort()
    In [12]: fnames
    Out[12]: ['file1', 'file10', 'file11', 'file2']

That is probably not what you wanted. However:

.. code-block:: ipython

    In [1]: fnames = ['file001', 'file002', 'file010', 'file011']
    In [3]: sorted(fnames)
    Out[3]: ['file001', 'file002', 'file010', 'file011']

That works!

So you need to find a string formatting operator that will "pad" the number with zeros for you.

2) The second element is a floating point number. You should display it with 2 decimal places shown.

3) The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.

4) The fourth value is a float with a lot of digits -- display it in scientific notation with 3 significant figures.


Task Two
--------

Using your results from Task One, repeat the exercise, but this time using an alternate type of format string (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you've not used them already).


Task Three
----------

Dynamically Building up format strings
--------------------------------------

* Rewrite:

``"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)``

to take an arbitrary number of values.

Hint: You can pass in a tuple of values to a function with a ``*``:

.. code-block:: ipython

    In [52]: t = (1,2,3)

    In [53]: "the 3 numbers are: {:d}, {:d}, {:d}".format(*t)
    Out[53]: 'the 3 numbers are: 1, 2, 3'

The idea here is that you may have a tuple of three numbers, but might also have 4 or 5 or 2 or....

so you can dynamically build up the format string to accommodate the length of the tuple.

The string object has the ``format()`` method, so you can call it with a string that is bound to a name, not just a string literal. For example:

.. code-block:: ipython

    In [16]: form_string = "{:d}, {:d}"

    In [17]: nums = (34, 56)

    In [18]: fstring.format(*nums)
    Out[18]: '34, 56'

So in the example above, how would you make a form_string that was the right length for an arbitrary tuple?


Put your code in a function that will return the final string like so:

.. code-block:: ipython

    In [20]: formatter((2,3,5))
    Out[20]: 'the 3 numbers are: 2, 3, 5'

    In [21]: formatter((2,3,5,7,9))
    Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'

It will look like:

.. code-block:: python

  def formatter(in_tuple):
      do_something_here_to_make_a_format_string

      return form_string.format(*in_tuple)


Task Four
----------

* Given a 5 element tuple:

    ``( 4, 30, 2017, 2, 27)``

    use string formating to print:

    ``'02 27 2017 04 30'``

Hint: use index numbers to specify positions.


Task Five
---------
f-strings are new to Python (version 3.6), but are very powerful and efficient. This means they are worth understanding and using. And this is made easier than it might be because they use the same, familiar formatting language that is conventionally used in Python (in ``.format()``).

So in this exercise we are going to specifically use f-strings.

Here's the simplest example, to show how you can use available variables in a f-string:

.. code-block:: ipython

    In [2]: name = 'Andy'
    In [3]: f'Your name is {name}'
    Out[3]: 'Your name is Andy'

In addition to referencing variables in the local scope, f-strings can evaluate simple expressions in line like so:

.. code-block:: ipython

    In [5]: f"Your name is {name.upper()}"
    Out[5]: 'Your name is ANDY'

    In [6]: name = "andy"

    In [7]: f"Your name is {name.upper()}"
    Out[7]: 'Your name is ANDY'

or

.. code-block:: ipython

    In [8]: a = 5

    In [9]: b = 10

    In [10]: f"The sum is: {a+b}"
    Out[10]: 'The sum is: 15'


* Here's a task for you: Given the following four element list:

    ``['oranges', 1.3, 'lemons', 1.1]``

* Write an f-string that will display:

    ``The weight of an orange is 1.3 and the weight of a lemon is 1.1``

* Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).


Task Six
---------
Often it's convenient to display data in columns. String formatting helps to make this straightforward.

Suppose you'd like to display something like:

     'First               $99.01    Second              $88.09  '

One way to do that is:

.. code-block:: ipython

    '{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')


In this simple example everything aligns nicely. But that will not be the case when the numbers to the left of the decimal place vary.
Then you will need to use alignment specifiers. Do some research on this using the links below. Then:

* Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

* And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? It can be done on one short line!


Resources on string formatting
==============================

The official reference docs:

https://docs.python.org/3/library/string.html#format-string-syntax

And a more human-readable intro:

https://pyformat.info/

A nice "Cookbook":

https://mkaz.blog/code/python-string-format-cookbook/


Submitting Your Work
====================
Put the file in your student directory in a new subdirectory named for this lesson, and add it to your clone early.

Make frequent commits with good, clear messages about what you're doing and why.

When you're done and ready for the instructors to review your work, push your changes to your gitHub fork and then go to the gitHub website and make a pull request.

Copy the gitHub link to the pull request, and use the +Submit Assignment link located in the top right corner to submit the URL here.
