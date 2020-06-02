#!/usr/bin/env python3


class X():
    pass


class Y():
    pass


class A(X, Y):
    pass


class B(Y, X):
    pass


class C(A, B):
    pass
