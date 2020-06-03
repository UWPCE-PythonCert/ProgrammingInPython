#!/usr/bin/env python

"""
adapted from coding bat: https://codingbat.com/python
"""


def walnut_party(walnuts, is_weekend):
    """
    basic solution
    """
    if is_weekend and walnuts >= 40:
        return True
    elif 40 <= walnuts <= 60:
        return True
    return False


def walnut_party2(walnuts, is_weekend):
    """
    Direct return of bool result
    """
    if is_weekend:
        return (walnuts >= 40)
    return (walnuts >= 40 and walnuts <= 60)


def walnut_party3(walnuts, is_weekend):
    """
    Conditional expression
    """
    return (walnuts >= 40) if is_weekend else (walnuts >= 40 and walnuts <= 60)

if __name__ == "__main__":
    # some tests

    assert walnut_party(30, False) is False
    assert walnut_party(50, False) is True
    assert walnut_party(70, True) is True
    assert walnut_party(30, True) is False
    assert walnut_party(50, True) is True
    assert walnut_party(60, False) is True
    assert walnut_party(61, False) is False
    assert walnut_party(40, False) is True
    assert walnut_party(39, False) is False
    assert walnut_party(40, True) is True
    assert walnut_party(39, True) is False

    print("All tests passed")
