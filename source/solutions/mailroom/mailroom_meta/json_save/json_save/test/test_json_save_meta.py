#!/usr/bin/env python3

"""
tests for  json_save
"""

import json_save.json_save_meta as js

import pytest


class NoInit(js.JsonSaveable):
    x = js.Int()
    y = js.String()


# A few simple examples to test
class SimpleClass(js.JsonSaveable):

    a = js.Int()
    b = js.Float()

    def __init__(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b


class ClassWithList(js.JsonSaveable):

    x = js.Int()
    lst = js.List()

    def __init__(self, x, lst):
        self.x = x
        self.lst = lst


class ClassWithDict(js.JsonSaveable):
    x = js.Int()
    d = js.Dict()

    def __init__(self, x, d):
        self.x = x
        self.d = d


@pytest.fixture
def nested_example():
    lst = [SimpleClass(3, 4.5),
           SimpleClass(100, 5.2),
           SimpleClass(34, 89.1),
           ]

    return ClassWithList(34, lst)


@pytest.fixture
def nested_dict():
    d = {'this': SimpleClass(3, 4.5),
         'that': SimpleClass(100, 5.2),
         'other': SimpleClass(34, 89.1),
         }

    return ClassWithDict(34, d)


def test_hasattr():
    ts = NoInit()
    # has the attributes even though no __init__ exists
    # they should be the default values
    assert ts.x == 0
    assert ts.y == ""


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

    print(saved)
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

    reconstructed = js.from_json(json_str)

    assert reconstructed == nested_dict
