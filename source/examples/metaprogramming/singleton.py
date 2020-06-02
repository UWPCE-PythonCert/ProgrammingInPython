#!/usr/bin/env python3

"""
example of using __metaclass__ to impliment the singleton pattern
"""


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class MyClass(metaclass=Singleton):
    pass

object1 = MyClass()
object2 = MyClass()

print(id(object1))
print(id(object2))
