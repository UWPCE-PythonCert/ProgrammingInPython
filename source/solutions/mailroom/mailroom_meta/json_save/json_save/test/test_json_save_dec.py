#!/usr/bin/env python

"""
test code for the decorator version of json_save
"""

import pytest

import json_save.json_save_dec as js


# Some simple classes to test:

@js.json_save
class NoInit:
    x = js.Int()
    y = js.String()


@js.json_save
class SimpleClass:

    a = js.Int()
    b = js.Float()

    def __init__(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b


@js.json_save
class ClassWithList:

    x = js.Int()
    lst = js.List()

    def __init__(self, x, lst):
        self.x = x
        self.lst = lst


@js.json_save
class ClassWithDict:
    x = js.Int()
    d = js.Dict()

    def __init__(self, x, d):
        self.x = x
        self.d = d


@pytest.fixture
def nested_example():
    l = [SimpleClass(3, 4.5),
         SimpleClass(100, 5.2),
         SimpleClass(34, 89.1),
         ]

    return ClassWithList(34, l)

@pytest.fixture
def nested_dict():
    d = {'this': SimpleClass(3, 4.5),
         'that': SimpleClass(100, 5.2),
         'other': SimpleClass(34, 89.1),
         }

    return ClassWithDict(34, d)


# now the actual test code

# this doesn't work yet
# def test_hasattr():
#     ts = NoInit()
#     # has the attributes even though no __init__ exists
#     # they should be the default values
#     assert ts.x == 0
#     assert ts.y == ""


def test_attrs():
    ts = SimpleClass()

    attrs = ts._attrs_to_save
    assert list(attrs.keys()) == ['a', 'b']


def test_simple_save():

    ts = SimpleClass()
    ts.a = 5
    ts.b = 3.14

    saved = ts.to_json_compat()
    assert saved['a'] == 5
    assert saved['b'] == 3.14
    assert saved['__obj_type'] == 'SimpleClass'


def test_list_attr():

    cwl = ClassWithList(10, [1, 5, 2, 8])

    saved = cwl.to_json_compat()
    assert saved['x'] == 10
    assert saved['lst'] == [1, 5, 2, 8]
    assert saved['__obj_type'] == 'ClassWithList'


def test_nested(nested_example):

    saved = nested_example.to_json_compat()

    assert saved['x'] == 34
    assert len(saved['lst']) == 3
    for obj in saved['lst']:
        assert obj['__obj_type'] == 'SimpleClass'


def test_save_load_simple():
    sc = SimpleClass(5, 3.14)

    jc = sc.to_json_compat()

    # re-create it from the dict:
    sc2 = SimpleClass.from_json_dict(jc)

    assert sc == sc2


def test_save_load_nested(nested_example):

    jc = nested_example.to_json_compat()

    # re-create it from the dict:
    nested_example2 = ClassWithList.from_json_dict(jc)

    assert nested_example == nested_example2


def test_from_json_dict(nested_example):

    j_dict = nested_example.to_json_compat()

    reconstructed = js.from_json_dict(j_dict)

    assert reconstructed == nested_example


def test_from_json(nested_example):
    """
    can it be re-created from an actual json string?
    """

    json_str = nested_example.to_json()

    reconstructed = js.from_json(json_str)

    assert reconstructed == nested_example


def test_from_json_file(nested_example):
    """
    can it be re-created from an actual json file?
    """

    json_str = nested_example.to_json()
    with open("temp.json", 'w') as tempfile:
        tempfile.write(nested_example.to_json())

    with open("temp.json") as tempfile:
        reconstructed = js.from_json(tempfile)

    reconstructed = js.from_json(json_str)

    assert reconstructed == nested_example


def test_dict():
    """
    a simple class with a dict attribute
    """
    cwd = ClassWithDict(45, {"this": 34, "that": 12})

    # see if it can be reconstructed

    jc = cwd.to_json_compat()

    # re-create it from the dict:
    cwd2 = ClassWithDict.from_json_dict(jc)

    assert cwd == cwd2


def test_from_json_dict2(nested_dict):
    """
    can it be re-created from an actual json string?
    """

    json_str = nested_dict.to_json()
    print(js.Saveable.ALL_SAVEABLES)
    reconstructed = js.from_json(json_str)

    assert reconstructed == nested_dict

