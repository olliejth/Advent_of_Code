"""Day 1 advent of code 2020"""


def return_pair_product(values: list):
    """Returns the product of two numbers in a list with a sum of 2000"""

    for n in range(len(values)):
        copy_list = [x for x in values]
        number = copy_list[n]
        copy_list.pop(n)
        for num in copy_list:
            if num + number == 2020:
                return num * number


if __name__ == "__main__":

    with open("test_data.txt", "r", encoding="utf-8") as f_obj:
        data = [int(entry.strip()) for entry in f_obj.readlines()]

    print(return_pair_product(data))
