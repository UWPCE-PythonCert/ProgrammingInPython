.. _exercise_downloader:

####################
Threaded Web Scraper
####################

If you have a lot of web sites (or web services) to hit at once, you may find that you're waiting a long time for each request to return.

In that case, your computer isn't doing much, and it could be waiting on multiple requests all at once.

In the examples, we had a news site scraper that used asyncio to asynchronously gather a bunch of data.

That approach worked well. But it was only about 100 or so simultaneous requests. Async works great for that many, but when it really shines is when you have thousands of (mostly sleeping) connections.

Another option that works well for tens to hundreds of simultaneous  connections is threading. Threading works well for this sort of thing as well, because the GIL isn't a problem -- the GIL is released when the system is waiting for a connection to return

So your job is to write a version of the newsAPI scraper that uses threads, instead.

Does is run faster or slower than the async version?

Did you find it easier or harder to write / understand the code?

A Queue?
========

You will need a way to launch a bunch of threads at once, but probably not one for each request you want to make -- that could be a lot of threads! In this case, 100 or so threads would probably work OK, but if you want the code to be extensible to larger numbers, you may want to pre-define a maximum number of threads in a thread pool.

Then you'll want to use a job Queue -- and then launch a handful of threads to process those jobs.

Experiment a bit -- how many threads give you maximum performance?


Hints
=====

Making requests
---------------
Python has a built-in client http lib (urllib). But almost everyone uses the "requests" package:

`Requests: HTTP for Humans <http://docs.python-requests.org/>`_

.. code-block:: bash

    $ pip install requests

Should do it.


