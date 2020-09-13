:orphan:

NOTE: this is only the start of a tutorial -- it would be nice to complete it some day!

===============
Python Tutorial
===============

This is a tutorial to get you started. Not a lot of explanation,
but enough to get you going with writing basic python code.

This tutorial uses exclusively Python3.

You may want to also check out some other tutorial options:

* **Jessica McKeller's beginning tutorial** (Video)
  https://www.youtube.com/watch?v=MirG-vJOg04

* **The Python Tutorial**
  (https://docs.python.org/3/tutorial/): This is the
  official tutorial from the Python website. No more authoritative source is
  available.

* **Code Academy Python Track**
  (http://www.codecademy.com/tracks/python): Often
  cited as a great resource, this site offers an entertaining and engaging
  approach and in-browser work.

* **Learn Python the Hard Way**
  (https://learnpythonthehardway.org/python3/): Solid and gradual.
  This course offers a great foundation for folks who have never
  programmed in any language before. It used be be fully available
  for free online -- but now you can only get the first bits. But still
  a good way to get started.


Running Your Code
=================

There are a number of ways to run python code:

- At the interpreter, often referred to as a REPL (Read, Evaluate, Print Loop)
- At an enhanced interpreter such as iPython
- In a browser-based interactive system such as the Jupyter Notebook
- From an IDE, such as IDLE or PyCharm
- Calling python from the command line to run a file.

While working with an interactive interpreter can be an excellent way to explore Python (and I highly recommend it), For this tutorial, to get you used to "real" production development, you will write, edit, and save your code in a programmer's text editor, and run it from the command line.


A Programmer's Text Editor
--------------------------

See These notes for getting set up with an editor and Python itself: :ref:`setting_up_dev_environment`



The Python Interpreter
----------------------

Python is a "byte compiled, interpreted" language. What this means to you is that you need a Python interpreter to run your Python code. It also means that that is all you need -- write some code, and run it with Python. That's it.

There are a few Python interpreters (or run-times) available:

- cPython
- PyPy
- Jython
- Iron Python
- MicroPython

These each have their own special uses for interaction the the Java VM or CLR, or running on micro controllers. But most production Python is run with the cPython interpreter, and most people mean cPython when they say "Python".


For this tutorial, you will need cPython version 3.7 or 3.8, installed and running so that when you type "python" at your command line, it starts up:

.. code-block:: bash

  MacBook-Pro:~ Chris$ python
  Python 3.7.4 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

Your result may be slightly different, but it should say Python 3. *something* there at the top, and give you the command prompt (``>>>``) at the end.

You can get out of it by typing ctrl+D (on OS-X and Linux) or ctrl+Z (On Windows), or typing ``exit()`` and then <return>.

Your first "program"
--------------------

Create your first program by typing this into your text editor::

    print("this worked!")

Type it exactly as above, with no extra space at the beginning, and no other characters.

Save the file as ``first.py``. Make sure to save it somewhere that makes sense, maybe a directory you create for this purpose, called "tutorial".

Start up the command line ("Terminal" on OS-X, "Command Prompt" on Windows), and "Navigate" to the directory where you just saved that file::

  cd tutorial

Now run your little program, by typing ``python first.py`` and hitting <return>. You should get something like this:

.. code-block:: bash

  MacBook-Pro:tutorial Chris$ python first.py
  this worked!
  MacBook-Pro:tutorial Chris$

If this is *NOT* what you got then something went wrong. Some things to check:

 - Did you save the file?
 - Is your command prompt "in" the same directory as the file?
   - you can check this by typing ``ls`` on \*nix, and ``dir`` on Windows, to see what files are in the dir that the command prompt is in.
 - Did you type *exactly* the same line as above?

What did you just do?
.....................

The "python" command starts up the python interpreter. If you "pass in" a file name, by typing the name of the file after "python", then the interpreter will read that file and run any code that is in it.

In this case, python ran the one line of code you put in that file, which told it to print the text: "this worked!" -- and that is what it did.

The print function
------------------

You can display just about anything in Python with the ``print()`` function. Simply type::

  print(what you want to print)

examples:

  print(45)
  print("this is a bit of text")

you can print more than one thing by separating them with commas, inside the parenthesis::

  print("the value of pi is:", 3.1459, "to four decimal places")


Text in Python
--------------

Text in python is supported by the "str" datatype, which is short for "string". The text datatype is often referred to as "strings" in computer science because it is a series, or string, of characters.

In Python3, strings can be any length, and contain any character (in virtually any language). This is because they support "Unicode" which is a system for representing all the characters of virtually all the languages used on earth.

There are many complications to full support of Unicode, but for the most part, in Python it "just works". Any text you can put in your text editor should work fine.

.. note:: With Unicode, the actual characters can be stored in multiple ways in the files themselves. If you've heard of "plain text", there really is no such thing anymore with Unicode. The exact way the text is stored is known as the "encoding". These days, an encoding known and "utf-8" is the mast commonly used. Python assumes that you are using utf-8 encoded files, but if strange things happen, make sure your editor is using utf-8. (or ASCII, which is an older encoding that does not support multiple languages -- but ASCII is subset of utf-8, so it still works.)

To create a str, you simply type what you want surrounded by either double or single quotes (the apostrophe).

Type this in a new file, called ``strings.py``:

.. code-block:: python

  print("This is a basic string")

  print('This is exactly the same string')

  print("You want to use double quotes if there's an apostrophe, like this: ' in the string")

  print('You can use single quotes if you want to "quote" a word')

run the file, and you should get something like this::

  MacBook-Pro:tutorial Chris$ python strings.py
  This is a basic string
  This is exactly the same string
  You want to use double quotes if there's an apostrophe, like this: ' in the string
  You can use single quotes if you want to "quote" a word

Numbers in Python
-----------------

Python supports two types of numbers: integers (int) -- or "whole numbers", with no fractional part:

.. code-block:: python

  3, 123, -345, 23473948

integers can be negative or positive and as large as you want:

.. code-block:: python

>>> print(12345678987654321234567890987654321234567898765)
12345678987654321234567890987654321234567898765

"real numbers" are called "floating point" (float) numbers. They are internally stored as binary, but you write them as regular decimal (base 10) numbers:

.. code-block:: python

    2.3, 3.0, 3.2459, -23.21

Note that while the integer`3` and the float `3.0` have the same value, they are different types of numbers. But for the most part, Python will convert from integer to floating point numbers for you (and back again), so this distinction is rarely important.

Math
----

Being a computer language, Python, of course, supports the regular math functions. Type the following into a file named math.py and run it:

.. code-block:: python

  print(3)
  print(3 * 4)
  print(3 * 4 + 10 - 2)
  print("twelve divided by 5 is:")
  print(12 / 5)

  print("twelve divided by 5 is:")
  print(12 // 5)

What is the difference between ``12 / 5`` and ``12 // 5`` ? Run your this code and find out.

Order of Operations
-------------------

Python follows the standard rules of "operator precedence" from algebra -- which operations are performed first when there are a bunch in a row:

https://en.wikipedia.org/wiki/Order_of_operations

Add this to the ``math.py`` file:

.. code-block:: python

  print(3 + 4 / 2)

run the file, and see if you get the answer you expect. The result should be 5.0, not 6.0.

That is because multiplication and division are a higher priority than addition, so Python divided 4 by 2 to get 2.0, and then added 3 + 2.0 to get 5.0.

Always keep that in mind when you do math expressions in Python. If you want to change the order of operations, you can group them with parentheses. Try adding this to the ``math.py`` file and run it:

.. code-block:: python

  print(3 + (4 / 2))
  print((3 + 4) / 2)

Python will always evaluate what is in parentheses first.

Variables
---------

Directly printing things is not all that useful -- though Python does make a good calculator!

To do anything more complicated, you need to store values to be used later. We do this by "assigning" them to a "variable", essentially giving them a name. Save the following in a ``variables.py`` file:

.. code-block:: python

    x = 5
    y = 20
    z = x + y

    print("the value of z is: ", z)

The equals sign: ``=`` is the "assignment operator". It assigns a value to a name, and then when you use the name in the future, Python will replace it with the value it is assigned to when it is used.

Names can (and generally should) be long and descriptive, and can contain letters, numbers (but not at the beginning) and only a few symbols, like the underscore character:

.. code-block:: python

  rectangle_width = 200
  rectangle_height = 23
  rectangle_area = rectangle_width * rectangle_height

Comments
--------

Try running this code:

.. code-block:: python

    print("this")
    # print ("that")
    print("the other")

What does it print?

"that" didn't print because the "#" symbol (the hash) tells python not to run any code after it on that line.

How about this?

.. code-block:: python

    print("this")
    print ("that")  I think we need this line too
    print("the other")

And this?

.. code-block:: python

    # Here we are printing useless stuff:
    print("this")
    print ("that")  # I think we need this line too
    print("the other")

comments can come after running code on a line as well. Using the hash to "comment out" parts of code is used in two ways:

1) To add a little extra description to some code, to explain what it doing.

2) To temporarily disable some code






























