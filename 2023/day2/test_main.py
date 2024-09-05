from main import get_sum_possible_games, clean_game_data


def test_given_data_output():
    """Tests correct output is returned given the provided data."""

    data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

    assert get_sum_possible_games(data) == 8


def test_clean_game_data_correct_output_type():
    """Tests that the clean data function outputs the correct data type."""

    res = clean_game_data(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")

    assert isinstance(res, dict)
