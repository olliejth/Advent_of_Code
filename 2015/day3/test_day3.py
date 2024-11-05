'''Test fine for day3.'''
import pytest

from day3 import is_new_house, calculate_house_number


@pytest.mark.parametrize('x, y, res', [
    (0, 0, False),
    (1, -3, True),
    (2, 1000000000000000, True),
    (-10000000000000, 3, False),
    (0, 2, True)
])
def test_is_new_house_valid_input(x, y, res, visited_houses):

    assert is_new_house(x, y, visited_houses) == res


@pytest.mark.parametrize('dirs, res', [
    ('^>v<', 4),
    ('>', 2),
    ('^v^v^v^v^v', 2)
])
def test_calculate_house_number_valid_input(dirs, res):

    assert calculate_house_number(dirs) == res
