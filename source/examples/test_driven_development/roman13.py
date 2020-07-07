"""
roman.py

A Roman numeral to arabic numeral (and back!) converter

complete with tests

tests are expected to be able to be run with the pytest system
"""

import pytest

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))


def to_roman(n):
    """convert integer to Roman numeral"""
    if not (0 < n < 4000):
        raise ValueError("number out of range (must be 1..3999)")

    if int(n) != n:
        raise ValueError("Only integers can be converted to Roman numerals")

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result


def is_valid_roman_numeral(s):
    """
    check if the input is a valid roman numeral

    returns True if it is, False other wise
    """
    # does it use only valid characters?
    for c in s:
        if c not in "MDCLXVI":
            return False

    # are any chars repeated too much?
    for c in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
        if c in s:
            return False

    return True


def from_roman(s):
    """convert Roman numeral to integer"""
    if not is_valid_roman_numeral(s):
        raise ValueError(f"{s} is not a valid Roman numeral")
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
            # print(f'found, {numeral} of length, {len(numeral)} adding {integer}')
    return result


#####################################
#  Tests for roman numeral conversion
#####################################

KNOWN_VALUES = ( (1, 'I'),
                 (2, 'II'),
                 (3, 'III'),
                 (4, 'IV'),
                 (5, 'V'),
                 (6, 'VI'),
                 (7, 'VII'),
                 (8, 'VIII'),
                 (9, 'IX'),
                 (10, 'X'),
                 (50, 'L'),
                 (100, 'C'),
                 (500, 'D'),
                 (1000, 'M'),
                 (31, 'XXXI'),
                 (148, 'CXLVIII'),
                 (294, 'CCXCIV'),
                 (312, 'CCCXII'),
                 (421, 'CDXXI'),
                 (528, 'DXXVIII'),
                 (621, 'DCXXI'),
                 (782, 'DCCLXXXII'),
                 (870, 'DCCCLXX'),
                 (941, 'CMXLI'),
                 (1043, 'MXLIII'),
                 (1110, 'MCX'),
                 (1226, 'MCCXXVI'),
                 (1301, 'MCCCI'),
                 (1485, 'MCDLXXXV'),
                 (1509, 'MDIX'),
                 (1607, 'MDCVII'),
                 (1754, 'MDCCLIV'),
                 (1832, 'MDCCCXXXII'),
                 (1993, 'MCMXCIII'),
                 (2074, 'MMLXXIV'),
                 (2152, 'MMCLII'),
                 (2212, 'MMCCXII'),
                 (2343, 'MMCCCXLIII'),
                 (2499, 'MMCDXCIX'),
                 (2574, 'MMDLXXIV'),
                 (2646, 'MMDCXLVI'),
                 (2723, 'MMDCCXXIII'),
                 (2892, 'MMDCCCXCII'),
                 (2975, 'MMCMLXXV'),
                 (3051, 'MMMLI'),
                 (3185, 'MMMCLXXXV'),
                 (3250, 'MMMCCL'),
                 (3313, 'MMMCCCXIII'),
                 (3408, 'MMMCDVIII'),
                 (3501, 'MMMDI'),
                 (3610, 'MMMDCX'),
                 (3743, 'MMMDCCXLIII'),
                 (3844, 'MMMDCCCXLIV'),
                 (3888, 'MMMDCCCLXXXVIII'),
                 (3940, 'MMMCMXL'),
                 (3999, 'MMMCMXCIX'),
                 )


def test_to_roman_known_values():
    """
    to_roman should give known result with known input
    """
    for integer, numeral in KNOWN_VALUES:
        result = to_roman(integer)
        assert numeral == result


def test_too_large():
    """
    to_roman should raise an ValueError when passed
    values over 3999
    """
    with pytest.raises(ValueError):
        to_roman(4000)


def test_zero():
    """to_roman should raise an ValueError with 0 input"""
    with pytest.raises(ValueError):
        to_roman(0)


def test_negative():
    """to_roman should raise an ValueError with negative input"""
    with pytest.raises(ValueError):
        to_roman(-1)


def test_non_integer():
    """to_roman should raise an ValueError with non-integer input"""
    with pytest.raises(ValueError):
        to_roman(0.5)


def test_float_with_integer_value():
    """to_roman should work for floats with integer values"""
    assert to_roman(3.0) == "III"

# ####################
# Tests for from_roman


def test_from_roman_known_values():
    """from_roman should give known result with known input"""
    for integer, numeral in KNOWN_VALUES:
        result = from_roman(numeral)
        assert integer == result


def test_roundtrip():
    """from_roman(to_roman(n))==n for all n"""
    for integer in range(1, 4000):
        numeral = to_roman(integer)
        result = from_roman(numeral)
        assert integer == result


# #####################
# The following to test for valid roman numerals

def test_invalid_character():
    """
    Roman numerals can only use these characters:

    M, D, C, L, X, V, I

    This tests that other characters will cause a failure
    """
    for s in ['Z', 'XXIIIQ', 'QXXIII', 'XXYIII']:
        with pytest.raises(ValueError):
            from_roman(s)


def test_too_many_repeated_numerals():
    '''from_roman should fail with too many repeated numerals'''
    for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
        with pytest.raises(ValueError):
            from_roman(s)


def test_repeated_pairs():
    '''from_roman should fail with repeated pairs of numerals'''
    for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
        with pytest.raises(ValueError):
            from_roman(s)


def test_malformed_antecedents():
    '''from_roman should fail with malformed antecedents'''
    for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
              'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
        with pytest.raises(ValueError):
            from_roman(s)


