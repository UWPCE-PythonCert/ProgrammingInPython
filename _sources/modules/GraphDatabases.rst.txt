:orphan:

.. _graph_databases:

###############
Graph Databases
###############

In computing, a graph database is a database that uses graph structures for semantic queries with nodes, edges and properties to represent and store data.

https://en.wikipedia.org/wiki/Graph_database

For those of you that aren't familiar with the mathematical concept of  a "graph" -- what all this means is that the database itself stores not just the data, but the relationships between the data.

This is in contrast to RDBMSs, where the data are stored in individual tables, with the relationships between the tables maintained via primary and foreign keys, and the actual relationships determined on the fly by searching multiple tables during "join" queries. RDBMSs are well optimized for these kinds of queries, but Graph Databases can be much more efficient for data retrieval when the records have complex relationships.

I find it a bit ironic that "relational" databases, aren't directly storing the relationships :-)

The wikipedia page has a pretty good description / example of how that works.

There are a number of commercial and open source Graph databases out there, and more than a few have Python drivers.

neo4j
=====

`neo4j <https://neo4j.com/>`_ is perhaps the most `popular <https://db-engines.com/en/ranking/graph+dbms>`_ graph database as of this writing, and it comes with a Python driver and good documentation, so we'll use that one for examples.

Here is a nice Python based tutorial about graph databases and neo4j:

`Talking About your Data Relationships <https://medium.com/labcodes/graph-databases-talking-about-your-data-relationships-with-python-b438c689dc89>`_

And `here are the docs <https://neo4j.com/developer/python/>`_ for the python driver.

And the Python API documentation: `python-driver API  <https://neo4j.com/docs/api/python-driver/current/>`_

There are a lot of other great docs and tutorial on the neo4j web site -- well worth checking out if you want to really learn how to use it.

And here is the "official" :download:`neo4j developer manual: Python </examples/graph_databases/neo4j-developer-manual-3.3-python.pdf>`


neo4j example
=============

Setup
-----

When we use databases, we introduce additional setup that we must perform before we can create and access our data. These setup activities can get really complex, and in reality, when developing software professionally, we may find that the setup is performed by someone other than a developer -- that's what sys admins are for :-).

To allow us to focus on Python development we are going to use the simplest way possible to get a database running, that will work whether you use Linux, MacOS or Windows.

Here, we’ll talk you through the steps to get Neo4j working.

What are we going to do?

* First we’ll sign up for a free, online Neo4j account.

* Then, we’ll configure the online database so we can start developing.

* Next, we’ll make sure we have secure access to our database.

* Final step is to install the requisite Python modules.

At that point, Python development can commence!

Let’s get started.

GraphenDB
.........

`GraphenDB <https://www.graphenedb.com/>`_ is a hosting service for neo4j databases. They provide free "sandbox" accounts for small databases you can use to test and learn how to use it.

The getting started guide is here: `Getting Started <https://docs.graphenedb.com/docs/getting-started>`_

Getting an account:
...................

1. Go to https://www.graphenedb.com/

2. Click on the "Sign up" button in the upper right to get signed up for an account.

3. Once you have created an account, you need to create a database. You can create a small (but not that small!) "Hobby" database for free.

4. Once you create the database, it will create a username (the name of the database you gave it) and generated password. Be sure to record your user name and password.

Note that when your database is set up, you also get connection strings for both "bolt" and http REST interfaces. Originally designed for neo4j, Bolt is a highly efficient, lightweight client-server protocol designed for database applications.

https://boltprotocol.org/


Managing your password:
.......................

We always have to sign on to our network database, using our user name and password. That means these credentials must be accessible to our Python program. But we must make sure that our password is secure. If we check code containing the password in to github, it will give access to anyone who reads our repo. With many online services, that will incur costs for which we would be responsible.

But don’t worry, we can guard against that easily. Here’s how:

First, edit your ``.gitignore`` file and add the following 2 lines at the end of the file, exactly as shown:

::

    # secrets
    .config/

This will ensure that you don't accidentally add your password to git.

NOTE: this still puts your password in plain text on your computer! So not really secure for really critical use!

Now, in the parent directory of your local project, make a new directory called ``.config``. Note the leading period.

In the newly create ``.config`` directory create a new file called ``config``. Note no leading period.

Edit the ``config`` file using your preferred editor, creating lines as follows:

::

    [configuration]

    neo4juser =
    neo4jpw =

At the end of the lines, enter a space after the =, and then the user name and password created in step 4. above. Your config file will look something like this:

::

    [configuration]

    neo4juser = example1
    neo4jpw = f.wJRVveeeg9LL.CyWKF4RbGf2SWTKp

Save that config file

Your user name and password are now safely stored where Python can access them. The ``.gitignore`` change will prevent the ``.config`` files from being accidentally pushed to github.

So now we need to setup access to Neo4j from Python. To do that we need to install the neo4j driver, which wires up Python to Neo4j.

.. code-block:: bash

    pip install neo4j-driver

Now, we are ready to start using our database!

Cypher
------

Neo4j uses a query language called Cypher. It plays the same role as SQL for RDBMSs -- and the official driver uses it to "talk" to the database.

https://neo4j.com/developer/cypher-query-language/

And here is a nice introduction:

https://www.airpair.com/neo4j/posts/getting-started-with-neo4j-and-cypher


Quick test
..........

You can find example code in the class repo in:

IntroPython-2017/examples/nosql/neo4j

We are going to play with the code to get a feel for neo4j.


Other interfaces for neo4j
==========================

neo4j-client is the default Python interface developed by the neo4j team. There are other options:

neomodel
--------

Is a Django ORM-like Object Mapper for neo4j

http://neomodel.readthedocs.io/en/latest/

Py2neo
------

Py2neo is a client library and toolkit for working with Neo4j from within Python applications and from the command line. The core library has no external dependencies and has been carefully designed to be easy and intuitive to use.

It "speaks" the bolt protocol directly.

http://py2neo.org/v3/

A bit more about Graphs
=======================

Graph data structures can be very useful for certain catagories of problems:

If you Google something like: "applications of graph data structure in computer science" you will get a lot of pages to explore, like this one:

http://www.cs.cmu.edu/afs/cs/academic/class/15210-s14/www/lectures/graphs.pdf

I encourage you to read up about them.

If you do find a use-case, or simply want to explore the topic experimentally with Python, the main package for working with graphs in python is `networkx`:

https://networkx.github.io/

It provides a pretty fully featured set of graph data structures, and the common algorithms for manipulating and exploring them.

There is even a package for storing networkx graphs in neo4j:

https://neonx.readthedocs.io

So you can store your graph in the neo4j database, and work with it with networkx. This may even give you a nicer, more pythonic interface to neo4j.


