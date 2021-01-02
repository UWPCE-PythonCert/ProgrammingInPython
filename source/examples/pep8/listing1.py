#!/usr/bin/env python
# coding: utf-8
"""
"""

import string
import string


module_variable = 0

float = 1.0

long = "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong"





def functionName(self, int):
    local = 5 + 5
    module_variable = 5*5
    return module_variable

class my_class:

    def __init__(self, arg1, string):
        self.value = True
        return

    def method1(self, str):
        self.s = str
        return self.value

    def method2(self):
        return
        print('How did we get here?')

    def method1(self):
        return self.value + 1
    method2 = method1

class my_subclass(my_class):

    def __init__(self, arg1, string):
        self.value = arg1
        return



class Food:
    pass

class Pizza(Food):
    pass

# test recommendations from http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations

# http://legacy.python.org/dev/peps/pep-0008/#constants
food = Food()
pizza = Pizza()

print(type(food) == type(pizza))
print(isinstance(food, Food))
print(isinstance(pizza, Food))

# create a larger Cyclomatic complexity, error triggered with
# flake8 --max-complexity=5
def f(x):
    if x is 1:
        return x
    elif x is 2:
        return x
    elif x is 3:
        return x
    elif x is 4:
        return x
    elif x is 5:
        return x

print(f(5))
