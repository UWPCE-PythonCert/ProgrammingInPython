#!usr/bin/env python

"""
example to show how fixtures work in pytest

to run this and see the output:

py.test -s -v pytest_fixtures.py
"""

import pytest


@pytest.fixture
# with module-level scope
#@pytest.fixture(scope="module")
def example_fixture():
    """
    An example fixture that does nothing useful

    But does return an object you can use for testing
    """
    print("I am running the fixture now")
    return {"this": 3,
            "that": 2}


# now use the fixture in a couple tests
def test_one(example_fixture):
    print("running test_one")
    assert example_fixture["this"] == 3


def test_two(example_fixture):
    print("running test_two")
    assert example_fixture["that"] == 2

# with teardown:
@pytest.fixture(scope="module")
def example_fixture2():
    """
    An example fixture that does nothing useful

    But does return an object you can use for testing
    """
    print("I am running the fixture now")
    yield {"this": 3,
           "that": 2}
    print("and now I am running the teardown code")


# using the fixture with teardown:
def test_three(example_fixture2):
    print("running test_three")
    assert example_fixture2["this"] == 3


def test_four(example_fixture2):
    print("running test_four")
    assert example_fixture2["this"] == 3
