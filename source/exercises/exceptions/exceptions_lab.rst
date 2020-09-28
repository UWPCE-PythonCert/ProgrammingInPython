.. _exercise_exceptions_lab:

**************
Exceptions Lab
**************

Learning Exceptions
===================

Just a little bit for the basics -- this is a bit of an odd example, but should give you the idea if you're still not sure.

Alternatively, see if you can clean up some of your other code (mailroom, maybe) with Exception handling.

Exceptions Lab
---------------

Improving ``input``

* The ``input()``  function can generate two exceptions: ``EOFError``
  or ``KeyboardInterrupt``  on end-of-file(EOF) or canceled input.

* Create a wrapper function, perhaps ``safe_input()``  that returns ``None``
  rather rather than raising these exceptions, when the user enters ``^C``  for Keyboard Interrupt, or ``^D`` (``^Z``  on Windows) for End Of File.
