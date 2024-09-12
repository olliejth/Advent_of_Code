"""Advent of code 2021 day 3."""


def convert_binary_to_decimal(bin_num: str) -> int:
    """Converts binary number as a string to decimal format integer"""
    return int(bin_num, 2)


def get_gamma_value(data_list: list[str]) -> str:
    """Returns gamma value from input data list"""
    gamma_val = ""
    for i in range(len(data_list[0])):
        count = {"0": 0, "1": 0}
        for number in data_list:
            if number[i] == "1":
                count["1"] += 1
            elif number[i] == "0":
                count["0"] += 1

        final_count = 0
        integer = ""
        for k, v in count.items():
            if v > final_count:
                final_count = v
                integer = k

        gamma_val += integer

    return gamma_val


def get_epsilon_value(gamma_val: str) -> str:
    """Returns the epsilon value that corresponds to a given gamma value"""
    epsilon_value = ""

    for integer in gamma_val:
        vals = ["0", "1"]
        vals.remove(integer)
        epsilon_value += vals[0]

    return epsilon_value


def get_power_consumption(data_list: list[str]) -> int:
    """Returns the submarine power consumption from a list of binary inputs"""
    gamma_value = get_gamma_value(data_list)
    epsilon_value = get_epsilon_value(gamma_value)

    gamma_dec = convert_binary_to_decimal(gamma_value)
    epsilon_dec = convert_binary_to_decimal(epsilon_value)

    return gamma_dec * epsilon_dec


if __name__ == "__main__":

    with open("example_data.txt", "r", encoding="utf-8") as f_obj:
        data = [item.strip() for item in list(f_obj.readlines())]

    print(get_power_consumption(data))
