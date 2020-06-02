.. _exercise_mailroom_meta:


Mailroom -- metaprogramming it!
===============================

So far, your mailroom program may not have any way to save or re-load the donor data. Some of you may have added code to save and load the data in a text file or JSON, but even if you have, you might want a more flexivle and extensible system once your data gets more complicated.


JSON
----

`JavaScript Object Notation (JSON) <https://www.json.org/>`_ is a format borrowed from the Web -- Javascript being the de-facto scripting language in browsers.  It is a great format for communicating with browsers, but it has become a common serialization format for many other uses: it is simple, flexible, and human-readable and writable.

It also maps pretty much directly to (some of) the core Python datatypes: lists, dictionaries, strings, and numbers.

So JSON is a nice way to save data for a program like Mailman.

Goal
----

Your goal is to use a JSON-save system started in the Metaprogramming Lesson (:ref:`metaprogramming`) to make your model classes saveable and loadable as JSON.

YOu can download the package here:

:download:`json_save.zip </examples/metaprogramming/json_save.zip>`

And it may also be in your class repo solutions dir:

``solutions/metaprogramming/json_save/``

You can use either the decorator-based or meta-class based approach.

You may need to extend the JSON-save module a bit to make it work for you!

When you are done, your class that holds the database of donors and their data should have ``save`` and ``load`` methods that will, naturally, save and load the entire dataset.

**make sure it's tested!**




