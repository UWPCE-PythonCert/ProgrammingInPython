:orphan:

.. _nosql:

################
No SQL Databases
################

"No SQL"?
=========

Structured Query Language (SQL) is the standard language for communicating with relational database management systems (RDBMS).

But an RDBMS system is not always the best way to store your data.

There are other alternatives, each with there own approach, but as RDBMSs and SQL are so ubiquitous, they are all lumped in under the moniker "NoSQL".

I personally hate things that are defined by what they are NOT, rather than what they are, but that's the terminology these days.

What is a Database?
-------------------

A database is an organized collection of data. The data are typically organized to model relevant aspects of reality in a way that supports processes requiring this information.

Usually a way to persist and recover that organized data.

These days, when you say "Database" almost everyone thinks "Relational Database", and SQL is the standard way to do that.

SQL RDBMS systems are robust, powerful, scalable, and very well optimized.

But: They require you to adapt the relational data model.


Non RDBMS options:
------------------

A key buzzword these days is "NOSQL"

OK: They don't use SQL -- but what are they?

Not one thing, but key features are mostly shared:

* "schema less"

 - Document oriented

* More direct mapping to an object model.

* Highly Scalable

 - Easier to distribute / parallelize than RDBMSs


Database Schema
---------------

**Schema:**

A database schema is the organization of data, and description of how a database is constructed: Divided into database tables, and relationships: foreign keys, etc...

Includes what fields in which tables, what data type each field is, normalization of shared data, etc.

This requires a fair bit of work up-front, and can be hard to adapt as the system requirements changes.

It also can be a bit ugly to map your programming data model to the schema.


Schemaless
----------

Schemaless databases generally follow a "document model".

Each entry in the database is a "document":

* essentially an arbitrary collection of fields.
* often looks like a Python dict.

Not every entry has to have exactly the same structure.

Maps well to dynamic programming languages.

Adapts well as the system changes.


NoSQL in Python:
----------------

Three Categories:


1. Simple key-value object store:
---------------------------------

- shelve
- anydbm
- Can store (almost) any Python object
- Only provides storage and retrieval


2. External NoSQL system:
-------------------------

* Python bindings to external NoSQL system

* Doesn't store full Python objects

* Generally stores arbitrary collections of data (but not classes)

* Can be simple key-value stores:

  - Redis, etc...

* Or a more full featured document database:

  - In-database searching, etc.

  - mongoDB, etc...

* "Graph" databases (:ref:`graph_databases`):

  - neo4j, etc.

* Or a Map/Reduce engine:

   - Hadoop


3. Python Object Database:
--------------------------

* Stores and retrieves arbitrary Python objects.

  - Don't need to adapt your data model at all.

* ZODB is the only robust maintained system (I know of)

* ZODB is as close a match as you can get between the store and your code -- references and everything.

http://blog.startifact.com/posts/older/a-misconception-about-the-zodb.html

(note that that post says "it's been around for more than a decade", and it was written a decade ago!)

Why a DB at all?
----------------

Reasons to use a database:

- Need to persist the data your application uses

- May need to store more data than you can hold in memory

- May need to have multiple applications (or multiple instances) accessing the same data

- May need to scale -- have the DB running on a separate server(s)

- May need to access data from systems written in different languages.


ZODB
----

The Zope Object Data Base: A native object database for Python

* Transparent persistence for Python objects

* Full ACID-compatible transaction support (including savepoints)

* History/undo ability

* Efficient support for binary large objects (BLOBs)

* Pluggable storages

* Scalable architecture

`ZODB <http://www.zodb.org/>`_


MongoDB
--------

Document-Oriented Storage

 * JSON-style documents with dynamic schemas offer simplicity and power.

Full Index Support
 * Index on any attribute, just like you're used to.

Replication & High Availability
 * Mirror across LANs and WANs for scale and peace of mind.

Auto-Sharding
 * Scale horizontally without compromising functionality.

Querying
 * Rich, document-based queries.

`MongoDB Web Site <https://www.mongodb.org/>`_


Other Options to Consider:
--------------------------

Redis: Advanced, Scalable  key-value store.
( not well supported on Windows :-( )

- http://redis.io/

Riak: High availablity/scalablity (but not so good for small)

- http://docs.basho.com/riak/latest/dev/taste-of-riak/python/

HyperDex: "Next generation key-value store"

- http://hyperdex.org/

Apache Cassandra: A more schema-based NoSQL solution

- http://pycassa.github.io/pycassa/

This is a nice page with a summary:

- https://www.fullstackpython.com/no-sql-datastore.html

(there are some good links to other resources on that page, too)

An Example
==========

The following are examples of using some of these systems to store some data.

The Data Model
--------------

To store your data, you need to have a structure for the data -- this is the data model. For this example, we will build an Address Book with a not quite trivial data model.

I'm a programmer first, and a database guy second (or third or...) so I start with the data model I want in the code.

There are people::

    self.first_name
    self.last_name
    self.middle_name
    self.cell_phone
    self.email

There are households::

    self.name
    self.people
    self.address
    self.phone

(similarly businesses)

:download:`address_book_model.py </examples/nosql/address_book_model.py>`

Using ZODB
----------

ZODB stored Python objects.

To make an object persistent (persistent should be installed with zodb):

.. code-block:: python

  import persistent

  class Something(persistent.Persistent):
      def __init__(self):
          self.a_field = ''
          self.another_field ''

When a change is made to the fields, the DB will keep it updated.


Mutable Attributes
-------------------

``Something.this = that`` will trigger a DB action

But:

``Something.a_list.append`` will not trigger anything.

The DB doesn't know that that the list has been altered.

Solution:

``from persistent.list import PersistentList``

``self.a_list = PersistentList()``

(also ``PersistantDict()`` )

(or write getters and setters...)

``Examples/nosql/address_book_zodb.py``

mongoDB
-------

Essentially a key-value store, but the values are JSON-like objects.
(Actually BSON (binary JSON) )

So you can store any object that can look like JSON:
  * dicts
  * lists
  * numbers
  * strings
  * richer than JSON.

mongoDB and Python
------------------

mongoDB is written in C++ -- can be accessed by various language drivers.

http://docs.mongodb.org/manual/applications/drivers/

For Python: ``PyMongo``

http://api.mongodb.org/python/current/tutorial.html

To install the python api for mongoDB:

``pip install pymongo`` - binary wheels available!

There are also various tools for integrating mongoDB with Frameworks:

* Django MongoDB Engine
* mongodb_beaker
* MongoLog: Python logging handler
* Flask-PyMongo
* others...

Getting started with mongoDB
----------------------------

The mongoDB (database) is a separate program. Installers here:

http://www.mongodb.org/downloads

**NOTE:** mongo is also available as a service, with a free "sandbox" to try it out:

https://www.mongodb.com/cloud/atlas

Installing Mongo
................

Simple copy and paste install or use homebrew (at least on OS-X)

Drop the files from ``bin`` into ``usr/local/bin`` or similar, or in your home dir somewhere you can find them.

- I put it in a "mongo" dir in my home dir. Then added it to my PATH for now:

  - Editing ``~/.bash_profile``, and adding:

::

  # Adding PATH for mongo local install
  PATH="~/mongo/bin:${PATH}
  export PATH

Anaconda Install
................

If you are using the Anaconda Python distribution (or miniconda) Mongo is available from conda::

  conda install mongodb pymongo


Starting Mongo
..............

Create a dir for the database:

``$ mkdir mongo_data``

And start it up:

``$ mongod --dbpath=mongo_data/``

It will give you a bunch of startup messages, and then end by indicating which port it is listening on::

  I NETWORK  [initandlisten] waiting for connections on port 27017

So you know you can connect to it on port 27017

Creating a DB:
--------------

Make sure you've got the mongo drivers installed:

pip install pymongo

.. code-block:: python

  # create the DB
  from pymongo import MongoClient

  client = MongoClient('localhost', 27017)
  store = client.store_name # creates a Database
  people = store.people # creates a collection

Mongo will link to the given database and collection, or create new ones if they don't exist.

Adding some stuff:

.. code-block:: python

    people.insert_one({'first_name': 'Fred',
                       'last_name': 'Jones'})

Pulling Stuff Out:
------------------

And reading it back:

.. code-block:: ipython

  In [16]: people.find_one({'first_name':"Fred"})
  Out[16]:
    {'_id': ObjectId('534dcdcb5c84d28b596ad15e'),
     'first_name': 'Fred',
     'last_name': 'Jones'}

Note that it adds an ObjectID for you.

:download:`/examples/nosql/address_book_mongo.py`

and

:download:`/examples/nosql/test_address_book_mongo.py`

(or in the class repo in : ``examples/nosql``)
