import pytest

from day2 import find_paper_for_one_box


def test_returns_correct_paper_area_for_one_box1():

    res = find_paper_for_one_box('2x3x4')

    assert res == 58


def test_returns_correct_paper_area_for_one_box2():

    res = find_paper_for_one_box('1x1x10')

    assert res == 43


def test_paper_for_one_box_returns_error_on_empty_string():

    with pytest.raises(ValueError):
        find_paper_for_one_box('')


def test_paper_for_one_box_returns_error_on_invalid_box():

    with pytest.raises(ValueError):
        find_paper_for_one_box('23x45')


def test_wrong_box_type_error():

    with pytest.raises(TypeError):
        find_paper_for_one_box(4)
