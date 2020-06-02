.. _ipyparallel_quickstart:

IPython Parallel Quickstart
===========================

Aside from its `official documentation`_ the following steps will get you quickly started with IPython Parallel.

.. code-block:: bash

    $ pip install ipyparallel

To start 1 controller and 4 engines:

.. code-block:: bash

    $ ipcluster start -n 4

At this point you can interact with the cluster via IPython.

.. code-block:: Ipython

    In [1]: import ipyparallel as ipp

    In [2]: c = ipp.Client()

    In [3]: c.ids
    Out[3]: [0, 1, 2, 3]

    In [4]: c[:].apply_sync(lambda : "Hello, World")
    Out[4]: [ 'Hello, World', 'Hello, World', 'Hello, World', 'Hello, World' ]

.. _official documentation: https://ipyparallel.readthedocs.io/en/latest/
