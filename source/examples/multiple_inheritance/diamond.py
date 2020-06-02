#!/usr/bin/env python
"""
example of the classic "diamond problem"

In this case, class A is at the root of the class hierarchy

B and C both inherit from A

D inherits from B and C

ASCII art that shows this:

     -----
     | A |
     -----
     /   \
    /     \
-----     -----
| B |     | C |
-----     -----
    \     /
     \   /
     -----
     | D |
     -----

So what's the problem?

If you call a method on D -- it calls B and C's method -- and each
of them call A's method. So A's method gets called twice!

The reason this is a tricky is that when you write the D class, you may not
know that B and C both inherit from A. And you may indeed *need* to call both
B and C's method.

"""


class A(object):
    def do_your_stuff(self):
        print("doing A's stuff")


class Default(A):
    def do_your_stuff(self):
        print('doing Default stuff')


class B(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print("doing B's stuff")


class C(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print("doing C's stuff")


class D(B, C):
    def do_your_stuff(self):
        B.do_your_stuff(self)
        C.do_your_stuff(self)
        print("doing D's stuff")


if __name__ == '__main__':
    a = A()
    print("\ncalling A's method")
    a.do_your_stuff()

    default = Default()
    print("\ncalling Default's method")
    default.do_your_stuff()

    print("\ncalling B's method")
    b = B()
    b.do_your_stuff()

    print("\ncalling C's method")
    c = C()
    c.do_your_stuff()

    print("\ncalling D's method")
    d = D()
    d.do_your_stuff()
