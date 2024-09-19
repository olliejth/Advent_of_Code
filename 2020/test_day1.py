
from day1 import count_occurences, reformat_input, get_number_of_valid_passwords


def test_count_occurences_correct_output():

    assert count_occurences("a", "aaa") == 3


def test_reformat_input_output_has_correct_keys():

    output = (reformat_input("1-3 a: abcde")).keys()

    assert "min" in output
    assert "max" in output
    assert "letter" in output
    assert "password" in output
    assert len(output) == 4


def test_get_number_of_valid_passwords_correct_output():

    input_data = ["1-3 a: abcde",
                  "1-3 b: cdefg",
                  "2-9 c: ccccccccc"]

    assert get_number_of_valid_passwords(input_data) == 2
