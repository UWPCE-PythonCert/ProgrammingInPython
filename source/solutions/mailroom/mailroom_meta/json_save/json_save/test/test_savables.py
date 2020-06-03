#!/usr/bin/env python

"""
tests for the savable objects
"""
import pytest

import json

from json_save.saveables import *

# The simple, almost json <-> python ones:
#         Type, default, example
basics = [(String, "This is a string"),
          (Int, 23),
          (Float, 3.1458),
          (Bool, True),
          (Bool, False),
          (List, [2, 3, 4]),
          (Tuple, (1, 2, 3.4, "this")),
          ]


@pytest.mark.parametrize(('Type', 'val'), basics)
def test_basics(Type, val):
    print("original value:", val)
    js = json.dumps(Type.to_json_compat(val))
    print("js is:", js)
    val2 = Type.to_python(json.loads(js))
    print("new value is:", val2)
    assert val == val2
    assert type(val) == type(val2)


dicts = [{"this": 14, "that": 1.23},
         {34: 15, 23: 5},
         {3.4: "float_key", 1.2: "float_key"},
         {(1, 2, 3): "tuple_key"},
         {(3, 4, 5): "tuple_int", ("this", "that"): "tuple_str"},
         {4: "int_key", 1.23: "float_key", (1, 2, 3): "tuple_key"},
         ]


@pytest.mark.parametrize('val', dicts)
def test_dicts(val):
    print("original value:", val)
    jsc = Dict.to_json_compat(val)
    print("json_compat:", jsc)
    js = json.dumps(Dict.to_json_compat(val))
    print("js is:", js)
    val2 = Dict.to_python(json.loads(js))
    print("new value is:", val2)
    assert val == val2
    assert type(val) == type(val2)
    # check that the types of the keys is the same
    for k1, k2 in zip(val.keys(), val2.keys()):
        assert type(k1) is type(k2)


# These are dicts that can't be saved
# -- mixing string and non-string keys
bad_dicts = [{"this": "string_key", 4: "int_key"},
             {3: "int_key", "this": "string_key"},
             {None: "none_key", "this": "string_key"},
             {"this": "string_key", None: "none_key"},
             ]

@pytest.mark.parametrize("val", bad_dicts)
def test_bad_dicts(val):
    print("original value:", val)
    with pytest.raises(TypeError):
        Dict.to_json_compat(val)
