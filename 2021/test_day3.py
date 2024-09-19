import pytest
from day3 import convert_binary_to_decimal, get_epsilon_value, get_gamma_value, get_power_consumption


def test_convert_binary_to_decimal_correct_output():

    assert convert_binary_to_decimal("10110") == 22


def test_get_gamma_correct_output(sample_binary_data):

    assert get_gamma_value(sample_binary_data) == "10110"


def test_get_epsilon_correct_output():

    assert get_epsilon_value("10110") == "01001"


def test_get_power_consumption_correct_output(sample_binary_data):

    assert get_power_consumption(sample_binary_data) == 198


def test_get_power_consumption_type_error1():

    with pytest.raises(TypeError) as err:
        get_power_consumption(12)

    assert str(err.value) == "Invalid input data type."


def test_get_power_consumption_type_error2():

    with pytest.raises(TypeError) as err:
        get_power_consumption(["a", "b", 3])

    assert str(err.value) == "Input list contains invalid data types."
