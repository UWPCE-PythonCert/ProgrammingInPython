.. _oo_vs_functional:

#########################################
Object Oriented vs Functional Programming
#########################################

Functional Programming is an alternative to Object Oriented Programming, which is to say that it takes a different perspective.  As to a definition, that can be rather tricky.

Definitions--by definition--are a statement of the exact meaning of a word: an exact statement or description of the nature, scope or meaning of something -- I looked it up.

What we're talking about here is more akin to two constellations of related ideas.  I tend to picture a three dimensional space with the Functional Programming cloud here and a separate Object Oriented cloud coalescing over here.

There are ideas that are somewhere in the middle between the two, and those might represent either equally shared ideas or in some cases, when you drill into them, you might find different approaches to address one thing, one idea.

Let's think of it in another way….

Programming paradigms are like human cultures
=============================================

Programming paradigms coalesce around certain values and tend to have unique aesthetics. The people of these cultures generally need to solve the same problems, but they often find different solutions, or prefer one approach to another due to their differential weighting of cultural values.  In some cases a given culture might not even recognize a problem that another culture considers among its first priorities to solve.

Cultures can have variations and can mix, borrowing ideas from one another as they see fit.  Let's consider an example.

There is, arguably, a North American culture with Canada, Mexico and the United States interacting with each other in commerce, academics, politics and in the general exchange of ideas.  However, the three clearly have distinct ways of solving problems.  And then, within any one country, there are sub cultures and cross-cutting cultures.  The Northwest of the United States for instance has a culture which is different from the culture in the Southwest.  Indeed the Northwestern United States likely has more in common with British Columbia in Canada than it has with Florida or Alabama in the Southeastern US.

This is all to say that to try to define--to actually nail down a definition--of Object Oriented Programming, Functional Programming, or of any other paradigm is perhaps a misguided errand.  It is perhaps better to think of them as constellations of ideas or as rich cultures that help you think about solutions to the problems you're trying to solve with software.

Objects!
========

Take one of the main ideas in OBJECT Oriented programs: Objects.

In Python perhaps we talk and even think more often about classes (or types), but when we instantiate a class, when we make an instance of a class, we have an object.

Functions!
==========

Take one of the main ideas in FUNCTIONAL programming:  Functions.

Since we discuss objects and classes elsewhere, let's jump into functions. We’ll start with high school math.

As you may recall, functions take arguments and return a value.  The strict definition can be found on Wikipedia:

https://en.wikipedia.org/wiki/Function_(mathematics)

In mathematics, a function is a relation between a set of inputs and a set of permissible outputs with the property that each input is related to exactly one output.

So functions take arguments and return a single, deterministic output, and for a given set of arguments the same value is always returned.

Keep this definition in mind as we work through this material.

Keep in mind also the fact that functions in Python are first-class language constructs.  Likewise we’ll talk about what that means as we work our way through the material.

Mutability, Immutability and State Management
---------------------------------------------

Think about functions and the stability they imply.  One set of inputs, one result.  Hand in hand with this, is the idea of immutability.

When you started with Python you might have been all over lists like I was.  You might have wondered:

  “Why would I use these relatively less flexible things called Tuples when I can use these highly flexible things called Lists?”

Well, a part of the answer there is immutability.  When you start to think functionally you start to think about state -- the management of state -- in a different way.  You start to think that nailing things down can be a good thing.

Control Flow versus Data Flow
-----------------------------

Another idea that typically falls more into the functional camp than into the object oriented camp is data flow.  What is data flow?  If you come from a programming environment like Matlab, Octave or R you do it all the time.

You’re mapping transformations en masse across entire sets of data and transforming your way to a solution.  You’re doing mutations on Numpy arrays or Pandas DataFrames.  You’re not focused as much on if/then/else constructs.  It’s more like working toward a solution with a Rubik’s Cube.

You’re thinking, “What series of transformations do I need to make on this collection of data, in order to get it into a state that represents a solution?”

That's what functional programming is all about:

* Immutable types
* First class functions
* Functions without side effects
* Data transformations





