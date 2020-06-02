.. _exercise_file_lab:

#############
File Exercise
#############

A bit of practice with files

Goal:
=====

Get a little bit of practice with handling files and parsing simple text.


Paths and File Processing
=========================

* Write a program which prints the full path for all files in the current
  directory, one per line. Use either the ``os`` module or ``pathlib``.

* Write a program which copies a file from a source, to a destination
  (without using shutil, or the OS copy command (you are essentially writing a simple version of the OS copy command)).

  - This should work for any kind of file, so you need to open
    the files in binary mode: ``open(filename, 'rb')`` (or ``'wb'`` for
    writing). Note that for binary files, you can't use ``readline()`` --
    lines don't have any meaning for binary files.

  - Test it with both text and binary files (maybe a jpeg or something of your choosing).

  - Advanced: make it work for any size file: i.e. don't read the entire
    contents of the file into memory at once.

  - This should only be a few lines of code :-)


File reading and parsing
========================

Download this text file:

:download:`students.txt <../examples/file_exercise/students.txt>`

In it, you will find a list of names and what programming languages they have used in the past. This may be similar to a list generated at the beginning of this class.

Write a little script that reads that file and generates a list of all the languages that have been used.

What might be the best data structure to use to keep track of bunch of values (the languages) without duplication?

The file format:
----------------

The first line of the file is:

``Name: Nickname, languages``

And each line looks something like this:

``Jagger, Michael: Mick, shell, python``

So a colon after the name, then the nickname, and then one or more languages.

However, like real data files, the file is NOT well-formed. Only some lines have nicknames, and other small differences, so you will need to write some code to make sure you get it all correct.

How can you tell the difference between a nickname and a language?

Extra challenge: keep track of how many students specified each language.

