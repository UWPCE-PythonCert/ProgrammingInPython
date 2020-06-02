#!/usr/bin/env python

"""
Examples of using json_save
"""

import json_save.json_save_meta as js

# Metaclass examples

class MyClass(js.JsonSaveable):

    x = js.Int()
    y = js.Float()
    lst = js.List()

    def __init__(self, x, lst):
        self.x = x
        self.lst = lst


class OtherSaveable(js.JsonSaveable):

    foo = js.String()
    bar = js.Int()

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

# create one:
print("about to create a instance")
mc = MyClass(5, [3, 5, 7, 9])

print(mc)

jc = mc.to_json_compat()

# re-create it from the dict:
mc2 = MyClass.from_json_dict(jc)

print(mc2 == "fred")

assert mc2 == mc

print(mc.to_json())

# now try it nested...
mc_nest = MyClass(34, [OtherSaveable("this", 2),
                       OtherSaveable("that", 64),
                       ])

mc_nest_comp = mc_nest.to_json_compat()
print(mc_nest_comp)

# can we re-create it?
mc_nest2 = MyClass.from_json_dict(mc_nest_comp)

print(mc_nest)
print(mc_nest2)

assert mc_nest == mc_nest2

