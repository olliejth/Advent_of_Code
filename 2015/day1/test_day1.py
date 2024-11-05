"""Test file for day 1."""

import pytest
from day1 import find_floor


def test_find_floor_returns_int():

    res = find_floor("((")

    assert isinstance(res, int)


@pytest.mark.parametrize("a, expected", [
    ('()()', 0),
    ('))(((((', 3),
    (')())())', -3),
])
def test_find_floor_valid_inputs(a, expected):
    assert find_floor(a) == expected


def test_find_floor_invalid_input_type():

    with pytest.raises(TypeError) as err:
        find_floor(3)


def test_find_floor_invalid_input_value():

    with pytest.raises(ValueError) as err:
        find_floor('hello')
