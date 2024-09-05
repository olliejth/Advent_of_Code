"""Contains the functions and script for solving the AOC challenge."""


def is_game_possible(game: str, act_vals: dict) -> bool:
    """Returns boolean value on whether a game is possible."""
    pass


def get_highest_from_game(game: list[str]):
    hand_highest = {"blue": 0, "red": 0, "green": 0}

    game_list = []
    for hand in game:
        h_list = []
        for h in hand:
            h_list.append(h.split(" "))
        game_list.append(h_list)

    for hand in game_list:
        hand_dict = {"blue": 0, "red": 0, "green": 0}
        for go in hand:
            hand_dict[go[1]] += int(go[0])

        for k in hand_dict.keys():
            if hand_dict[k] > hand_highest[k]:
                hand_highest[k] = hand_dict[k]

    return hand_highest


def clean_game_data(game: str) -> dict:
    """Converts game data into a format that is easier to work with."""
    game = game.replace("Game ", "").split(":")

    game_dict = {}
    game_dict["game_no"] = game[0]
    game_dict["hands"] = []
    hand_list = []
    for hand in game[1].split(";"):
        hand_list.append(hand.strip())

    nested_hand_list = []
    for hand in hand_list:
        nested_hand_list.append(hand.split(", "))

    game_dict['hands'] = nested_hand_list

    return game_dict


def multiply_dict_values(game_dict: dict) -> int:
    product = 1
    values = list(game_dict.values())
    for num in values:
        product *= num

    return product


def get_sum_possible_games(game_list: list[str]) -> int:
    """Returns the sum of a given input of the possible game IDs."""
    game_no_count = 0
    prod_sum = 0
    highest_pos = {"blue": 14, "red": 12, "green": 13}

    for game in game_list:
        cleaned_data = clean_game_data(game)
        highest_from_game = get_highest_from_game(cleaned_data["hands"])

        # possible = True
        # for k in highest_pos.keys():
        #     if highest_from_game[k] > highest_pos[k]:
        #         possible = False

        # if possible:
        #     game_no_count += int(cleaned_data['game_no'])

    # return game_no_count

        power_product = multiply_dict_values(highest_from_game)

        prod_sum += power_product

    return prod_sum


if __name__ == "__main__":

    # data = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

    # print(get_sum_possible_games(data))

    with open('test_data.txt', 'r', encoding='utf-8') as f_obj:
        game_data = f_obj.readlines()

    data_list = []
    for game in game_data:
        data_list.append(game)

    print(get_sum_possible_games(data_list))
