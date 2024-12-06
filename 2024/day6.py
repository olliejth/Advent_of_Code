"""AoC day 6 2024"""
from datetime import datetime


def get_guard_location(data: list[str]) -> list[int]:
    '''Finds location and direction of guard and locations of obstacles.'''

    dirs = {
        '^': 'N',
        '>': 'E',
        'v': 'S',
        '<': 'W'
    }

    obstacles = []

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char in ['>', '<', '^', 'v']:
                coords = [x, y]
                direction = dirs[char]
            elif char == '#':
                obstacles.append([x, y])

    return coords, direction, obstacles


def get_next_loc(guard_loc: list[int], guard_dir: str, obstacles: list) -> list:
    '''Returns new location of guard.'''

    next_dir = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

    if guard_dir == 'N':
        new_loc = [guard_loc[0], guard_loc[1] - 1]
    elif guard_dir == 'E':
        new_loc = [guard_loc[0] + 1, guard_loc[1]]
    elif guard_dir == 'S':
        new_loc = [guard_loc[0], guard_loc[1] + 1]
    elif guard_dir == 'W':
        new_loc = [guard_loc[0] - 1, guard_loc[1]]

    if new_loc not in obstacles:
        return new_loc, guard_dir
    else:
        guard_dir = next_dir[guard_dir]
        new_loc, guard_dir = get_next_loc(guard_loc, guard_dir, obstacles)
        return new_loc, guard_dir


def get_result(data: list[str]) -> int:
    '''Solves AoC 2024 day 6 part 1.'''

    loc_list = []
    vert_limit = range(len(data))
    hor_limit = range(len(data[0]))

    start_loc, start_dir, obstacles = get_guard_location(data)
    loc_list.append(start_loc)

    guard_loc = start_loc
    guard_dir = start_dir

    counter = 0

    while True:
        if counter > 18000:
            print('Loop')
            return False
        if guard_loc[0] in hor_limit and guard_loc[1] in vert_limit:
            new_loc, new_dir = get_next_loc(guard_loc, guard_dir, obstacles)
            guard_loc = new_loc
            guard_dir = new_dir
            counter += 1
        else:
            print('No loop')
            return True


def make_new_data(row_i: int, col_i: int, data: list[str]) -> list[str]:
    '''Creates new data set with new obstacle at [row_i, col_i].'''

    new_data = []
    for y, line in enumerate(data):
        if y == row_i:
            new_line = f'{line[:col_i]}#{line[col_i+1:]}'
            new_data.append(new_line)
        else:
            new_data.append(line)

    return new_data


def get_result_2(data: list[str]) -> int:
    '''Calculates number of obstacle locs that could cause loops.'''

    iter_num = 0
    obstacle_sum = 0

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            print(f'Loc number: {iter_num}')
            iter_num += 1
            if data[y][x] not in ['>', '<', '^', 'v', '#']:
                new_data = make_new_data(y, x, data)
                if not get_result(new_data):
                    obstacle_sum += 1

    print('\n')
    return obstacle_sum


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [obj.strip() for obj in f_obj.readlines()]

    t1 = datetime.now()

    print(f'Part 2 result: {get_result_2(data)}')

    print(f'\nTime elapsed: {datetime.now() - t1}')

    # for line in data:
    #     print(line)

    # print('\n\n')

    # new_data = make_new_data(0, 0, data)

    # for line in new_data:
    #     print(line)
