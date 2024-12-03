"""AoC day 3 2024"""
import re


def get_result(input_data: str) -> int:
    '''Finds sum of all "mul" instructions in a string.'''

    mull_sum = 0

    mulls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_data)

    for mull in mulls:
        mull_sum += int(mull[0]) * int(mull[1])

    return mull_sum


def get_do_dont_input(raw_input: str) -> str:
    '''Extracts only the relevant do() instructions.'''

    output_str = ""

    do_str_list = raw_input.split('do()')

    for s in do_str_list:
        output_str += s.split("don't")[0]

    return output_str


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = f_obj.readline()

    correct_input = get_do_dont_input(data)

    print(get_result(correct_input))
