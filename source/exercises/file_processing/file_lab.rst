.. _exercise_file_lab:

#############
File Exercise
#############


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
