#!/usr/bin/env python


class A(object):
    def my_method(self):
        print("called A")


class B(A):
    def my_method(self):
        print("called B")
        super(B, self).my_method()


class C(A):
    def my_method(self):
        print("called C")
        super(C, self).my_method()


class B1(B):
    def my_method(self):
        print("called B1")
        super(B1, self).my_method()


class C1(C):
    def my_method(self):
        print("called C1")
        super(C1, self).my_method()


class D(B1, C1):
    def my_method(self):
        print("called D")
        super(D, self).my_method()

print(D.mro())
d = D()
print(d.my_method())
