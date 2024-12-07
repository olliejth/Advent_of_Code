"""AoC Day 7 2024"""

import operator
import itertools


def generate_combinations(n):
    # Generate all combinations of '+' and '*' of length n
    combinations = itertools.product('+*|', repeat=n)
    return [''.join(comb) for comb in combinations]


def is_possible(equation: dict, combination: str) -> bool:
    '''Finds whether combination of operators results in sum.'''

    ops = {'+': operator.add,
           '*': operator.mul}

    result = equation['nums'][0]

    for i, op in enumerate(combination):
        # print(equation)
        # print(combination)
        # print('---')
        result = ops[op](result, equation['nums'][i + 1])

    if result == equation['res']:
        return True
    return False


def get_new_numbers(equation: dict, combination: str) -> list:
    '''Gets new numbers by joining using the concat operator |'''

    combined_list = []
    for k, op in enumerate(combination):
        combined_list.append(equation['nums'][k])
        combined_list.append(op)
    combined_list.append(equation['nums'][-1])

    # [6, '+', 8, '|', 6, '+', 15],

    new_nums = []
    idx = 0
    number = ''
    while idx < len(combined_list):
        if idx == len(combined_list) - 1:
            if number:
                new_nums.append(int(number))
            else:
                new_nums.append(combined_list[-1])
            idx += 1
        elif combined_list[idx + 1] == '|':
            if not number:
                number += str(combined_list[idx])
            number += str(combined_list[idx+2])
            idx += 2
        else:
            if number:
                new_nums.append(int(number))
            if idx > 0 and combined_list[idx - 1] != '|':
                new_nums.append(combined_list[idx])
            elif idx == 0:
                new_nums.append(combined_list[idx])
            idx += 2
            number = ''

    equation['nums'] = new_nums
    combination = [c for c in combination if c != '|']

    return [equation, combination]


def return_sum(equation: dict) -> int:
    '''Returns the equation sum if it is possible.'''
    # Format: {'res': 190, 'nums': [10, 19]}

    nodes = len(equation['nums']) - 1

    combinations = generate_combinations(nodes)

    for comb in combinations:
        print(comb)
        eq_copy = equation.copy()
        # print(equation)
        # print(comb)
        # print('---')
        if '|' in comb:
            eq_copy, comb = get_new_numbers(eq_copy, comb)
        print(eq_copy)
        print(comb)
        print('---')
        if is_possible(eq_copy, comb):
            return equation['res']

    return 0


def part2(data: list[dict]) -> int:
    '''Finds the sum of all possible results.'''

    poss_sum = 0

    for i, eq in enumerate(data):
        # print(i)
        sum_change = return_sum(eq)
        poss_sum += sum_change
        # if sum_change:
        #     print(f'Success: {i}')
        # else:
        #     print(f'Failure: {i}')

    return poss_sum


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [obj.strip() for obj in f_obj.readlines()]

    formatted_data = []
    for obj in data:
        split_data = obj.split(':')
        result = int(split_data[0])
        nums = [int(n) for n in split_data[1].split()]
        formatted_data.append({
            'res': result,
            'nums': nums})

    # print(get_new_numbers({'res': 7290, 'nums': [6, 8, 6, 15]}, '|+*'))
    print(return_sum({'res': 7290, 'nums': [6, 8, 6, 15]}))
