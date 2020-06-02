#!/usr/bin/env python3

"""
Some example code demonstrating some super() behaviour
"""

# Define a multiple inheritance scheme:
class A():
    def __init__(self):
        print("in A __init__")
        print("self's class is:", self.__class__)
        s = super().__init__()


class B():
    def __init__(self):
        print("in B.__init__")
        s = super().__init__()


class C():
    def __init__(self):
        print("in C.__init__")
        s = super().__init__()


class D(C, B, A):
    def __init__(self):
        print("self's class is:", self.__class__)
        super().__init__()

# print our D's method resoluton order
#  Is it what you expect?
print("\nD's mro:")
print( D.__mro__)
# see what happens when you create a D object:
print("\ninitializing a D object:")
d = D()


# ## super's parameters
# To do its thing, super() needs to know two things:
#
# ``super(type, obj)``
#
# It needs to know that type (class) that you want the super-classes of,
# AND it needs to know the actual object instance at the time it is called.
#
# python3 fills these in for you at run time, but in python2, you needed to
# specify them:
#
# ```
# class A(object):
#     def __init__(self):
#         super(A, self).__init__()
# ```
#
# But why do you need BOTH `A` and `self`? -- isn't `self` an instance of `A`?
#
# Not neccesarily -- if A's method is being called from a subclass, then
# `self` will be an instance of the subclass. `super()` requires that the object be an instance of the class (or a subclass).
#
# This distiction will come up later....
#
# Again, py3 takes care of this for you, though you CAN still spell it out.

# see what you get with super by itself:
s_c = super(C, d)
print("\n the super object of super(C, d) itself")
print(s_c)


# This works because `d` is a `D` object, which is a subclass of `C`.

# create a C instance:
c = C()

# and try to create a super with the missmatch
print("\n the super object of super(D, c)")
try:
    super(D, c)
except TypeError as err:
    print(err)
# But this gives a TypeError: `C` is NOT a subclass of `D`

# it doesn't have to be an exact intance, jsust a subclass:

print("\n the super object of super(A, d)")
s_a = super(A, d)
print(s_a)


print("\n the super object of super(B, d)")
s_b = super(B, d)
print(s_b)

print("\nD inherits from both A and B, so that worked...")

print("\nD's MRO:")
print(D.__mro__)


# An Example of why you want to use super() everywhere.

# Classes without super()

class A():
    def this(self):
        print("in A.this")

class B():
    def this(self):
        print("in B.this")

class C(A,B):
    def this(self):
        print("in C.this")
        A.this(self)
        B.this(self)

print("\nRunning without super()")
print("Creating a C instance without super() -- and calling it's this method:")
c = C()
c.this()

print("C's `this` explicitly called both A and B's methods -- so they all get called.")

# Using super in just C:

print("\n using super() in C, but not everywhere...")

class A():
    def this(self):
        print("in A.this")

class B(A):
    def this(self):
        print("in B.this")

class C(B):
    def this(self):
        print("in C.this")
        super().this()


print("\n C's MRO")
print(C.__mro__)

print("\ncreating a C instance and calling it's this() method:")
c = C()
c.this()

print("**NOTE:  `A.this` did NOT get called!")

# **Note:**  `A.this` did NOT get called!
#
# Even though it is in in the MRO.
#
# Python stopped when it found the method in B.

# ### Using super everywhere:

print("using super everywhere:")

class Base():
    def this(self):
        pass # just so there is a base that has the method

class A(Base):
    def this(self):
        print("in A.this")
        super().this()

class B(Base):
    def this(self):
        print("in B.this")
        super().this()
class C(A,B):
    def this(self):
        print("in C.this")
        super().this()


print("\nnow create a C instance and call its this() method:")
c = C()
c.this()

print("Now both A and B's methods get called -- probably what you want.")

print("\nAnd the MRO of the base class")
print(Base.__mro__)

# But if you don't want both called -- better to just be Explicit, rather than use super():

class Base():
    def this(self):
        pass # just so there is a base that has the method

class A(Base):
    def this(self):
        print("in A.this")
        super().this()

class B(Base):
    def this(self):
        print("in B.this")
        super().this()

class C(A,B):
    def this(self):
        print("in C.this")
        A.this(self)

print("\nIf you want total control of what methods get called --don't use super"
      "and be explicit")

c = C()
c.this()


print("**Whoa** -- A and B's method DID get called! -- why?")

print("A's MRO:")
print(A.__mro__)


print("B is not there")

print("\nBut if we print the class of each instance when this() is called")

class Base():
    def this(self):
        pass # just so there is a base that has the method

class A(Base):
    def this(self):
        print("in A.this")
        print("self's class in A's this method:", self.__class__)
        super().this()

class B(Base):
    def this(self):
        print("in B.this")
        super().this()

class C(A,B):
    def this(self):
        print("in C.this")
        A.this(self)


print("and create a c instance and call this():")
c = C()
c.this()

print("In A's this method -- self is a C object")

print("C's MRO:")
print(C.__mro__)

print("\nRemember, `super()` is dynamic -- what it calls is determined at run time.")
print("That's how it knows to call ``B``'s method too.")
print("Which is why we say that using `super()` is *part* of the interface of"
      "the class.")
