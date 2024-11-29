"""Day 1 AoC 2016"""


def get_new_direction(current: str, turn: str) -> str:
    """Gets new moving direction from previous
    direction and new instruction."""

    if current == 'W' and turn == 'R':
        return 'N'

    dirs = ['N', 'E', 'S', 'W']
    cur_index = dirs.index(current)

    if turn == 'R':
        return dirs[cur_index + 1]

    return dirs[cur_index - 1]


def find_shortest_path(directions: list[str]) -> int:
    """Returns lowest number of blocks to destination."""
    travel = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    direction = 'N'
    coords_list = [[0, 0]]

    for d in directions:
        turn, blocks = d[0], int(d[1:])
        new_direction = get_new_direction(direction, turn)

        for i in range(blocks):

            travel[new_direction] += 1

            x = travel['E'] - travel['W']
            y = travel['N'] - travel['S']

            coords = [x, y]

            if coords in coords_list:
                return abs(x) + abs(y)

            coords_list.append(coords)

        direction = new_direction

    print('No locs visited twice.')


if __name__ == '__main__':

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [item.strip() for item in f_obj.readline().split(',')]

    print(find_shortest_path(data))
