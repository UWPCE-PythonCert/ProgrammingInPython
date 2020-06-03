"""
Test file for frange
"""
from math import isclose
from frange import frange

import pytest


def list_close(l1, l2, rel_tol=1e-15):
    """tests that two iterables of values are close"""
    for a, b in zip(l1, l2):
        assert isclose(a, b, rel_tol=rel_tol)
    return True


def test_frange():
    '''
    tests the basics
    '''
    r = frange(10, 20, 100)
    assert r[0] == 10.0
    assert r[1] == 10.1
    assert r[100] == 20.0


def test_index_too_large():
    r = frange(100, 200, 10)
    with pytest.raises(IndexError):
        r[11]
    with pytest.raises(IndexError):
        r[-12]


def test_frange_neg_index():
    '''
    tests the basics
    '''
    r = frange(10, 20, 100)
    assert r[-1] == 20.0
    assert r[-2] == 19.9
    assert r[-101] == 10.0


def test_length():
    assert len(frange(0, 100)) == 101


def test_full_slice():
    r = frange(10, 20, 100)
    assert r == r[:]


def test_slice_start():
    r = frange(0, 1, 10)
    assert r[1:] == frange(0.1, 1, 9)
    assert r[2:] == frange(0.2, 1, 8)


def test_slice_stop():
    r = frange(0, 1, 20)
    print(list(r))
    print("sliced [:8] --", r[:8])
    print(list(r[:8]))
    assert len(r[:8]) == 8
    assert list_close(r[:8], list(r)[:8])


def test_slice_start_stop():
    r = frange(0, 1, 10)
    print(list(r))
    print("sliced [2:8] --", r[1:8])
    print(list(r[2:8]))
    assert len(r[2:8]) == 6
    assert list_close(r[2:8], list(r)[2:8])


def test_slice_start_neg_end():
    assert (list(frange(0, 10, 10)[1:-1]) ==
            [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])


def test_slice_start_neg_end2():
    assert (list(frange(0, 10, 10)[2:-2]) ==
            [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])


def test_backwards():
    list_close(frange(1, 0, 10),
               [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
               )


def test_start_stop_same():
    with pytest.raises(ValueError):
        assert list(frange(3, 3)) == []


def test_zero_num_steps():
    with pytest.raises(ValueError):
        assert list(frange(3, 10, 0)) == []
