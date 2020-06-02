import pytest
from unittest import mock


def get_color():
    color = input("what is your favorite color?")
    if color == "red":
        return "that's a stupid color"
    if color == "blue":
        return "Hey! that's mine too!"
    else:
        raise ValueError("nothing to say about that color")
    return color


@mock.patch('builtins.input')
def test_get_color_red(mocked_input):
    mocked_input.return_value = "red"
    result = get_color()
    assert "stupid" in result


@mock.patch('builtins.input')
def test_get_color_blue(mocked_input):
    mocked_input.return_value = "blue"
    result = get_color()
    assert "Hey!" in result


@mock.patch('builtins.input')
def test_get_color_purple(mocked_input):
    mocked_input.return_value = "purple"
    with pytest.raises(ValueError):
        result = get_color()



