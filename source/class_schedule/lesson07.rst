.. _session_1_07:

#####################################
Session 7: Object Oriented Programing
#####################################

Object Oriented Programing: classes, instance and class attributes, subclassing and inheritance.


Readings
========

.. toctree::
    :maxdepth: 1

    ../modules/ObjectOrientationOverview
    ../modules/PythonClasses
    ../modules/SubclassingAndInheritance

Supplemental reading
--------------------

* Dive into Python3: 7.2 -- 7.3

   - http://www.diveintopython3.net/iterators.html#defining-classes

* Think Python: 15 -- 18

   - http://www.greenteapress.com/thinkpython/html/thinkpython016.html

Some Videos to watch:
---------------------

Python Class Toolkit by *Raymond Hettinger*

https://youtu.be/HTLu2DFOdTg

https://speakerdeck.com/pyconslides/pythons-class-development-toolkit-by-raymond-hettinger


The Art of Subclassing by *Raymond Hettinger*

http://pyvideo.org/video/879/the-art-of-subclassing

The most salient points from that video are as follows:

* **Subclassing is not for Specialization**

* **Classes and subclassing are for code re-use -- not creating taxonomies**

* **Bear in mind that the subclass is in charge**

Note that the previous talk and this one were back to back at PyCon -- but despite their contradictory titles -- they have similar messages.

Stop Writing Classes
....................

by *Jack Diederich*

http://pyvideo.org/video/880/stop-writing-classes

"If your class has only two methods -- and one of them is ``__init__``
-- you don't need a class"


Exercises:
==========

.. toctree::
    :maxdepth: 1

    ../exercises/oo_intro.rst
    ../exercises/html_renderer.rst
    ../exercises/html_renderer_tutorial.rst
