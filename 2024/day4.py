"""Day 4 AoC 2024"""


def is_xmas(puzzle_in: list[str], r: int, i: int, coords: list[list]) -> bool:
    '''Checks whether sequence of coordinates returns "XMAS".'''

    row_i = coords[0]
    let_i = coords[1]

    word = 'X'

    for k in range(3):
        try:
            i_coord = i + let_i[k]
            r_coord = r + row_i[k]
            if i_coord >= 0 and r_coord >= 0:
                word += puzzle_in[r_coord][i_coord]
        except:
            pass

    if word.upper() == 'XMAS':
        return True
    return False


def find_xmas(puzzle_in: list[str], r: int, i: int) -> bool:
    '''Returns bool for if there are any valid '''

    if puzzle_in[r][i] != 'X':
        return 0

    potential_xmas = [[[0, 0, 0], [1, 2, 3]], [[0, 0, 0], [-1, -2, -3]],
                      [[1, 2, 3], [0, 0, 0]], [[-1, -2, -3], [0, 0, 0]],
                      [[-1, -2, -3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]],
                      [[-1, -2, -3], [-1, -2, -3]], [[1, 2, 3], [-1, -2, -3]]]

    results = [is_xmas(puzzle_in, r, i, coords) for coords in potential_xmas]
    res_sum = 0
    for res in results:
        if res:
            res_sum += 1

    return res_sum


def get_result(puzzle_input: list[str]) -> int:
    '''Returns number of word search XMASs in input.'''

    xmas_sum = 0

    puzzle_len = len(puzzle_input)
    row_len = len(puzzle_input[0])

    for r in range(puzzle_len):
        for i in range(row_len):
            xmas_sum += find_xmas(puzzle_input, r, i)

    return xmas_sum


def is_x_mas_square(puzzle_in: list[str], r: int, i: int) -> bool:
    '''Returns whether an A has a surrounding "MAS" X shape.'''

    if puzzle_in[r][i] != 'A':
        return False

    coords = [puzzle_in[r + 1][i + 1],
              puzzle_in[r + 1][i - 1],
              puzzle_in[r - 1][i + 1],
              puzzle_in[r - 1][i - 1]]

    pair1 = [coords[0], coords[3]]
    pair2 = [coords[1], coords[2]]

    is_square = True

    for pair in [pair1, pair2]:
        if 'S' not in pair or 'M' not in pair:
            is_square = False

    if is_square:
        return True
    return False


def get_result_two(puzzle_input: list[str]) -> int:
    '''Finds occurrences of X-MAS squares in list of strings.'''

    puzzle_len = len(puzzle_input)
    row_len = len(puzzle_input[0])

    x_mas_sum = 0

    for r in range(1, puzzle_len - 1):
        for i in range(1, row_len - 1):
            if is_x_mas_square(puzzle_input, r, i):
                x_mas_sum += 1

    return x_mas_sum


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [obj.strip() for obj in f_obj.readlines()]

    print(f'Part 1 answer: {get_result(data)}')
    print(f'Part 2 answer: {get_result_two(data)}')
