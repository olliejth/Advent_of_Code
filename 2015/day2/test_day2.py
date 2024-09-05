import pytest

from day2 import find_paper_for_one_box, get_ribbon_length, clean_data


def test_returns_correct_paper_area_for_one_box1():

    res = find_paper_for_one_box([2, 3, 4])

    assert res == 58


def test_returns_correct_paper_area_for_one_box2():

    res = find_paper_for_one_box([1, 1, 10])

    assert res == 43


def test_paper_for_one_box_returns_error_on_empty_string():

    with pytest.raises(TypeError):
        find_paper_for_one_box('')


def test_paper_for_one_box_returns_error_on_invalid_box():

    with pytest.raises(TypeError):
        find_paper_for_one_box('23x45')


def test_wrong_box_type_error():

    with pytest.raises(TypeError):
        find_paper_for_one_box(4)


def test_clean_data():

    res = clean_data('2x3x4\n')

    assert res == [2, 3, 4]


def test_valid_answer1():

    res = get_ribbon_length([2, 3, 4])

    assert res == 34


def test_valid_answer2():

    res = get_ribbon_length([1, 1, 10])

    assert res == 14
