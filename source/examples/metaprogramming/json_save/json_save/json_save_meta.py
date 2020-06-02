#!/usr/bin/env python3

"""
json_save

metaclass based system for saving objects in a JSON format

This could be useful, but it's kept simple to show the use of metaclasses

The idea is that you subclass from JsonSavable, and then you get an object
that be saved and reloaded to/from JSON
"""

import json

# import * is a bad idea in general, but helpful for a modules that's part
# of a package, where you control the names.
from .saveables import *


class MetaJsonSaveable(type):
    """
    The metaclass for creating JsonSavable classes

    Deriving from type makes it a metaclass.

    Note: the __init__ gets run at compile time, not run time.
          (module import time)
    """
    def __init__(cls, name, bases, attr_dict):
        # it gets the class object as the first param.
        # and then the same parameters as the type() factory function

        # you want to call the regular type initilizer:
        super().__init__(name, bases, attr_dict)

        # here's where we work with the class attributes:
        # these will the attributes that get saved and reconstructed from json.
        # each class object gets its own dict
        cls._attrs_to_save = {}
        for key, attr in attr_dict.items():
            if isinstance(attr, Saveable):
                cls._attrs_to_save[key] = attr
        # special case JsonSaveable -- no attrs to save yet
        if cls.__name__ != "JsonSaveable" and (not cls._attrs_to_save):
            raise TypeError(f"{cls.__name__} class has no saveable attributes.\n"
                            "           Note that Savable attributes must be instances")

        # register this class so we can re-construct instances.
        Saveable.ALL_SAVEABLES[attr_dict["__qualname__"]] = cls


class JsonSaveable(metaclass=MetaJsonSaveable):
    """
    mixin for JsonSavable objects
    """
    def __new__(cls, *args, **kwargs):
        """
        This adds instance attributes to assure they are all there, even if
        they are not set in the subclasses __init__
        """
        # create the instance
        obj = super().__new__(cls)
        # set the instance attributes to defaults
        for attr, typ in cls._attrs_to_save.items():
            setattr(obj, attr, typ.default)
        return obj

    def __eq__(self, other):
        """
        default equality method that checks if all of the saved attributes
        are equal
        """
        for attr in self._attrs_to_save:
            try:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False
        return True

    def to_json_compat(self):
        """
        converts this object to a json-compatible dict.

        returns the dict
        """
        # add and __obj_type attribute, so it can be reconstructed
        dic = {"__obj_type": self.__class__.__qualname__}
        for attr, typ in self._attrs_to_save.items():
            dic[attr] = typ.to_json_compat(getattr(self, attr))
        return dic

    @classmethod
    def from_json_dict(cls, dic):
        """
        creates an instance of this class populated by the contents of
        the json compatible dict

        the object is created with __new__ before setting the attributes

        NOTE: __init__ is not called.
        There should not be any extra initialization required in __init__
        """
        # create a new object
        obj = cls.__new__(cls)
        for attr, typ in cls._attrs_to_save.items():
            setattr(obj, attr, typ.to_python(dic[attr]))
        # make sure it gets initialized
        # obj.__init__()
        return obj

    def to_json(self, fp=None, indent=4):
        """
        Converts the object to JSON

        :param fp=None: an open file_like object to write the json to.
                        If it is None, then a string with the JSON
                        will be returned as a string

        :param indent=4: The indentation level desired in the JSON
        """
        if fp is None:
            return json.dumps(self.to_json_compat(), indent=indent)
        else:
            json.dump(self.to_json_compat(), fp, indent=indent)

    def __str__(self):
        msg = ["{} object, with attributes:".format(self.__class__.__qualname__)]
        for attr in self._attrs_to_save.keys():
            msg.append("{}: {}".format(attr, getattr(self, attr)))
        return "\n".join(msg)


def from_json_dict(j_dict):
    """
    factory function that creates an arbitrary JsonSavable
    object from a json-compatible dict.
    """
    # determine the class it is.
    obj_type = j_dict["__obj_type"]
    obj = Saveable.ALL_SAVEABLES[obj_type].from_json_dict(j_dict)
    return obj


def from_json(_json):
    """
    factory function that re-creates a JsonSavable object
    from a json string or file
    """
    if isinstance(_json, str):
        return from_json_dict(json.loads(_json))
    else:  # assume a file-like object
        return from_json_dict(json.load(_json))


if __name__ == "__main__":

    # Example of using it.
    class MyClass(JsonSaveable):

        x = Int()
        y = Float()
        l = List()

        def __init__(self, x, lst):
            self.x = x
            self.lst = lst


    class OtherSaveable(JsonSavable):

        foo = String()
        bar = Int()

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
