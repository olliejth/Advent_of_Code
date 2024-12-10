"""AoC day 9 2024"""
from time import sleep


def expand_input(data: str) -> list:
    '''Expands data with free-space according to day rules.'''

    print('-\nExpand started.\n-')

    new_seq = []

    counter = 0
    for i, char in enumerate(data):
        if i % 2 == 0:
            new_seq.append(int(char) * str(counter))
            counter += 1
        else:
            new_seq.append(int(char) * '.')

    return new_seq


def find_last_number(exp_data: list) -> list:
    '''Finds the number and index of the last numeric value in a string.'''

    cpy_data = exp_data.copy()

    cpy_data.reverse()

    for i, char in enumerate(cpy_data):
        if char.isnumeric():
            return char, (i+1) * -1


def contract_expanded_input(exp_data: list) -> str:
    '''Collapses expanded data to get final order.'''

    exp_data = [x for x in exp_data if x != '']

    print('-\nContract started.\n-')

    num_of_nums = sum([c.isnumeric() for c in exp_data])

    for i, char in enumerate(exp_data[:num_of_nums]):
        if char == '.':
            last_num, last_idx = find_last_number(exp_data)
            exp_data[i] = last_num
            exp_data[last_idx] = '.'

    con_data = exp_data[:exp_data.index('.')]

    return con_data


def generate_contracted_output(exp_data: list, rev_num_ids: list,
                               gaps: list[int]) -> str:
    '''Generates contracted data according to the day rules.'''

    only_dots = ['.' * i for i in range(10)]

    for pair in rev_num_ids[:-1]:
        num_idx = pair[0]
        num_seq = pair[1]
        num_length = len(num_seq) // pair[2]
        gaps_before = [idx for idx in gaps if idx < num_idx]

        for i in gaps_before:
            dot_seq = exp_data[i]
            num_of_dots = dot_seq.count('.')

            if num_length <= num_of_dots:
                if dot_seq in only_dots:
                    nd = '.' * (num_of_dots - num_length)
                    new_seq = f'{num_seq}{nd}'
                else:
                    first_dot_id = exp_data[i].find('.')
                    front_nums = exp_data[i][:first_dot_id]
                    front_num_length = len(front_nums)
                    nd = '.' * (num_of_dots - num_length - front_num_length)
                    new_seq = f'{front_nums}{num_seq}{nd}'
                exp_data[i] = new_seq
                exp_data[num_idx] = '.' * num_length
                break

    con_data = ''.join(exp_data)

    return con_data


def contract_expanded_input_part2(exp_data: list) -> str:
    '''Collapses expanded data to get final order.'''

    print('-\nContract started.\n-')

    counter = 0
    rev_num_ids = []
    for i, seq in enumerate(exp_data):
        if seq and '.' not in seq:
            rev_num_ids.append([i, seq, len(str(counter))])
            counter += 1
    rev_num_ids.reverse()

    all_gaps = range(1, len(exp_data), 2)

    sleep(1)

    con_data = generate_contracted_output(exp_data, rev_num_ids, all_gaps)

    # if len(con_data) < 200:
    #     print(f'My answer: {con_data}')
    #     print(f'AC answer: 00992111777.44.333....5555.6666.....8888..')

    return con_data


def calculate_checksum(con_data: str) -> int:
    '''Calculates checksum from contracted data.'''

    print('-\nChecksum started.\n-')

    checksum = 0

    for i, char in enumerate(con_data):
        if char != '.':
            checksum += i * int(char)

    return checksum


def get_result(data: str) -> int:
    '''Master function'''

    expanded_data = expand_input(data)
    # contracted_data = contract_expanded_input(expanded_data)
    contracted_data = contract_expanded_input_part2(expanded_data)
    checksum = calculate_checksum(contracted_data)

    return checksum


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = f_obj.readline()

    print(f'Length of data = {len(data)}')

    res = get_result(data)

    print(f'-\nTotal checksum: {res}\n-')

    # WRONG ANSWER: 111107819580
