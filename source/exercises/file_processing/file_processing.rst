.. _exercise_file_processing:

###############
File Processing
###############

A bit of practice with reading and processing files.


File reading and parsing
========================

Download this text file:

:download:`students.txt <./students.txt>`

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

