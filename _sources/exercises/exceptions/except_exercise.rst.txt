.. _exercise_exceptions:

###################
Exceptions Exercise
###################

This is a little exercise that shows you how to handle exceptions in a way that mirrors actual development.

Procedure
=========

Here are two files that you should be in the github classroom repo:

:download:`except_exercise.py`

:download:`except_test.py`

Run ``except_exercise.py``::

   $ python except_exercise.py

(or ``run except_exercise.py`` in iPython)

You will find that it crashes with an exception.

Your job is to write the proper exception handler in the
``except_exercise.py`` file, so that the code can run.

It will then crash again.

You will then need to handle the next exception.

There are instructions in the ``except_exercise.py`` file telling you want you want to achieve.

This is simulating writing code that is using another library -- your code is ``except_exercise.py`` and ``except_test.py`` is the other library. So you don't want to alter ``except_test.py`` -- only change the ``except_exercise.py`` file.

**Hint:** the exceptions themselves usually come from the other file, so you will get a traceback like this::

    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    ~/PythonStuff/UWPCE/Temp/except_exercise.py in <module>()
         15 first_try = ['spam', 'cheese', 'mr death']
         16
    ---> 17 joke = fun(first_try[0])
         18
         19

    ~/PythonStuff/UWPCE/Temp/except_test.py in fun(reaper)
         13 def fun(reaper):
         14     if reaper == 'spam':
    ---> 15         print(s)
         16     elif reaper == 'cheese':
         17         print()

    NameError: name 's' is not defined

The ``NameError`` is coming from line 15 of ``except_test.py``. But this is not your code! So you need to look higher up in the traceback to see where in *your* code the exception is triggered. That is where you put your ``try--except`` block.

In this case, that's line 17 of ``except_exercise.py``. In real life, it can be higher up in a much deeper stack trace -- but keep looking 'till you see your code.

Results
-------

When you are done, running ``except_exercise.py`` should result in output something like this::

    Spam, Spam, Spam, Spam, Beautiful Spam

    Customer: Not much of a cheese shop really, is it?
    Shopkeeper: Finest in the district, sir.
    Customer: And what leads you to that conclusion?
    Shopkeeper: Well, it's so clean.
    Customer:  It's certainly uncontaminated by cheese.


Why are you doing this?
-----------------------

This is a kind of silly exercise, but in real life, this is a common work flow -- you call a library, and find that in certain circumstances it raises an exception.
As the code in the library is out of your hands, you need to decide how to handle that exception in your code instead.
