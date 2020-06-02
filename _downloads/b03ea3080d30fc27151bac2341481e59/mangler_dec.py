#!/usr/bin/env python3

"""
class decorator that adds both upper and lower case versions of
class attributes.

Same as the NameMangler metaclass, but with a class decorator instead

Usage example:

@name_mangler
class Foo:
    x = 1

f = Foo()
print(f.x)
print(f.X)
"""


def name_mangler(cls):
    """
    Class decorator that adds upper and lower case names to the
    decorated class
    """
    # get the dictionary of class attributes
    att_dict = vars(cls)
    # create a new dict to hold the attributes
    new_attrs = {}
    # loop thorough all the class attributes
    for name, val in att_dict.items():
        # skip all the "dunder" attributes
        if not name.startswith("__"):
            # Create both upper and lower case versions of all non-dunder names
            #   They are stored in the new_attrs dict, as you can't
            #   update the class namespace while looping through it.
            new_attrs[name.upper()] = val
            new_attrs[name.lower()] = val
    # Add the new names to the cls attributes
    #   you can't directly update the __dict__ -- class __dict__s are not
    #   writable.
    for name, val in new_attrs.items():
        setattr(cls, name, val)
    return cls


@name_mangler
class Foo:
    x = 1
    Y = 2


# note that it works for methods, too!
@name_mangler
class Bar:
    x = 1

    def a_method(self):
        print("in a_method")


if __name__ == "__main__":
    f = Foo()
    print(f.x)
    print(f.X)
    print(f.y)
    print(f.Y)

    b = Bar()
    b.A_METHOD()

