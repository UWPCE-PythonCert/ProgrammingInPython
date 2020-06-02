:orphan:

.. _logging:

###############################
Logging and the logging module
###############################


What is Logging?
================

.. rst-class:: left small

      What is logging?

            In computing, a logfile is a file that records either events that occur in an operating system or other software runs, or messages between different users of a communication software.

            Logging is the act of keeping a log. In the simplest case, messages are written to a single logfile.


      (https://en.wikipedia.org/wiki/Logfile)

      But in fact, a file is only *one* place to keep a log. You may want to send a log of what your program is doing to another system, to the console, or????

what to log?
------------

.. rst-class:: medium::

    What might you want to log?

System information

Error messages

Fine-grain tracing output


The logging module
-------------------

A flexible logging system that comes with the standard library

Any module using the logging api can have logging output routed the same
as your code.

Resources for learning more:

https://docs.python.org/3.5/howto/logging.html

http://docs.python-guide.org/en/latest/writing/logging/

https://pymotw.com/3/logging/


Why not ``print()``?
--------------------

We've all been using ``print()`` all over the place to track what's going on in a program.

And I still use it -- a lot.

But we (usually) don't want all sorts of crap sent to stdout when the program is running in production.

So we comment out or delete those ``print()`` s -- but if we wanted to know what the program was doing when developing -- maybe we want to know when something unanticipated goes wrong, too?

The ``logging`` module give you a flexible system that allows you to monitor what's going on in your system, when you need to, without cluttering things up when you don't need it.


Background
==========

.. rst-class:: left

      There are lots of good tutorials, etc, on the web for getting you started with *using* the logging module.

      But not much about how it works -- how it is structured.

      I found it hard to get beyond the basics without that knowledge, so the following should help.

      The logging module provides a very flexible framework for customizing the logging in a simple or complex application.

The ``logging`` module
-----------------------

.. code-block:: python

    import logging

The logging module not only provides the classes and functions required to build a logging system, but also a place to centrally manage the logging for an entire application.

This allows you to set up logging in one place, and everywhere in the app, the system can be used.

So, for instance, when developing and debugging, you may want logging messages to go to the console, but for deployment, to log files.

That configuration can be changed in one place.

(NOTE: this is one good reason to prefer logging over ``print()``)

Logging "levels"
----------------

The built in way to catagorize logging messages is by level.

Levels are ordered numerically, so you can think of them as in order of importance, and it's easy to choose how much detail you want.

The built-in set is::

      CRITICAL    50
      ERROR       40
      WARNING     30
      INFO        20
      DEBUG       10

so DEBUG provides the most detail, and CRITICAL you'd pretty much always want to see.


The logging API provides easy ways to send messages with these levels:

.. code-block:: python

    logging.debug('this is a debugging message')


https://docs.python.org/3/library/logging.html#levels

similarly:

.. code-block:: python

    logging.critical('this is a critical message')
    logging.error('this is a error message')
    logging.warning('this is a warning message')
    logging.info('this is a information message')
    logging.debug('this is a debug message')

Note that if you have not configured the logger, a default configuration will automatically be set up -- so you can alwlays call these in yoru code, and it won't fail.

This is actually particularly nice -- you can add logging messages to your code, and they will "do the right thing" when run inside any application, whether it's been spcifically configured or not.

The logging classes
-------------------

The four main classes (you need to deal with) for logging

-  Loggers  - the interface for your code
-  Handlers - handle log routing
-  Filters  - define which log messages to let through
-  Formatters - how the log messages get rendered

The ``Logger`` class
--------------------

The ``Logger`` class is the core class that handles logging.

Messages get sent to a ``Logger`` instance, and it is responsibile for routing them appropriately.

``Logger`` s can be  nested in a hierarchical fashion, so that a message can be sent to sub-loggers, and any messages not handled will be passed the chain to eventually be handled by the "root" logger.

There is always a root logger, and often the only one you need.

Each ``Logger`` represents a single logging channel.


``Logger`` instances are given text names, with module-style "dots" representing the hierarchy:

.. code-block:: python

    "main"
    "main.sub_logger1"
    "main.sub_logger2"
    ...

The "root" logger has no name, but is the root of all created loggers

The logging module keeps track of all the loggers you create, so you can reference them by name.

``logging.getLogger()``
------------------------

The ``logging.getLogger()`` function returns the logger you ask for:

.. code-block:: python

  the_root_logger = logging.getLogger()
  another_logger = logging.getLogger("name")

If the logger you ask for doesn't exist, ``getLogger()`` will create a new one for you by that name. (It won't be configured, though...)

This whole system allows you to have multiple loggers without having to pass logging instances around.

The ``Handler`` classes
-----------------------

logging ``Handler`` s are what actually do the work of, well, handling, the log message.

Formatting it, and actually writing to a file or somehow performing the 'log' duty.

There are handlers for writing to files, streams (stdout, stderr), sockets, and nifty things like automaticaly rotating log files.

And, of course, you can make your own.

Each logger can have multiple Handlers


You will most likely use:

 - ``FileHandler``
 - ``StreamHandler``

The others are documented here.

https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers

The ``Formatter`` classes
-------------------------

``Formatters`` are responsible for formatting the log message.

Each log message is stored in a ``LogRecord`` object, which has a lot of data about the message and where it came from.

So you can use a formatter to add the data you want to your log entry.

.. code-block:: python

   formatter = logging.Formatter('%(levelname)s - %(module)s - %(message)s')

``levelname`` is the "level" of the log message: debug, warning, etc. ``module`` is the name of the module the message came from. ``message`` is the message itself.

There are lots of other options:

https://docs.python.org/3/library/logging.html#logrecord-attributes

Each ``Handler`` can have its own ``Formatter``

The Filter classes
------------------

Each ``Logger`` can have a ``Filter`` object.

``Filters`` determine which messages will be handled by a given logger, and which pass on to other loggers up the hierarchy.

They can do very flexible filtering based on where the message came from, etc.

But only really needed for complex systems:

Loggers filter by "level" by default -- which is enough for most uses.


Basic logging usage
-------------------

As you can see from the above -- the logging system is a complex nest of classes that can be configured and mixed and matched in complex ways.

The system was ported from Java -- can you tell?

However, the module provides a Pythonic API for common usage: the ``logging.basicConfig()`` function.

Example:

.. code-block:: python

    import logging

    logging.basicConfig(filename='example.log',
                        filemode='w',
                        format='%(asctime)s %(message)s',
                        level=logging.DEBUG)


This creates a "root" logger, and sets it up with:

* a ``FileHandler`` with the given filename and mode

   - The mode is the file opening mode: 'w' to clobber and make a new file each time, 'a' to append to an existing file

* sets up the handler to use the provided format string

  -  ``asctime`` provides a datetime stamp (you can specify a format for that, too)

* sets the level to debug -- so all messages will get logged.


What does ``basicConfig`` do for you?
--------------------------------------
A LOT!

If you were to do this by hand:

.. code-block:: python

      filename = 'example.log'
      filemode = 'w'
      handler = logger.FileHandler(filename, mode)
      format_str = '%(asctime)s %(message)s'
      fmt = logger.Formatter(format_str)
      handler.setFormatter(fmt)
      logging.root.addHandler(h)
      logging.root.setLevel(logging.EBUG)

Wouldn't that be fun?


A more complex logging setup
----------------------------

See:

``examples/logging/example.py``

In there, a logging system is set up that logs to a file, and also the console.

It calls a fake "application" that does things in random order, logging as it goes...


References
----------

The logging system is very powerful and flexible.

And frankly, not as clean and Pythonic as it could be...

So it's pretty tricky to figure out.

I highly recommend the cookbook to get beyond the basics:

https://docs.python.org/3/howto/logging-cookbook.html

Also these:

http://atlee.ca/blog/posts/diving-into-python-logging.html

http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python






