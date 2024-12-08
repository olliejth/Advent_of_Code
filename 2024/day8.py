"""AoC day 8 2024"""


def get_uniques(data: list[str]) -> list[str]:
    '''Returns unique characters that could be antennas'''

    uniques = []

    for c in ''.join(data):
        if c != '.' and c not in uniques:
            uniques.append(c)

    return uniques


def get_character_coordinates(character: str, data: list[str]) -> list[list]:
    '''Returns list of all coordinates of a specific character.'''

    coords = []

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == character:
                coords.append([x, y])

    return coords


def find_antenna_positions(coords: list[list]) -> list[list]:
    '''Returns all of the antenna positions for each character.'''

    antenna_locs = []

    for coord in coords:
        cpy_coords = coords.copy()
        del cpy_coords[cpy_coords.index(coord)]

        for other_coord in cpy_coords:
            vec_diff = [other_coord[0] - coord[0], other_coord[1] - coord[1]]
            for i in range(1, 100):
                antenna_pos = [other_coord[0] + (vec_diff[0] * i),
                               other_coord[1] + (vec_diff[1] * i)]
                if antenna_pos not in antenna_locs:
                    antenna_locs.append(antenna_pos)

    return antenna_locs


def filter_coordinates(antenna_coords: list[list], x_lim: range, y_lim: range,
                       antenna_positions) -> list[list]:
    '''Ensures antenna coordinates are within an acceptable range and
    removes duplicates.'''

    filtered_data = []

    for coord in antenna_coords:
        if coord[0] in x_lim and coord[1] in y_lim and coord not in antenna_positions:
            filtered_data.append(coord)

    return filtered_data


def get_result(data: list[str]) -> int:
    '''Master function for part 1.'''

    antenna_positions = []

    chars = get_uniques(data)
    x_lim = range(len(data[0]))
    y_lim = range(len(data))

    for char in chars:
        c_coords = get_character_coordinates(char, data)
        for coord in c_coords:
            if coord not in antenna_positions:
                antenna_positions.append(coord)
        a_locs = find_antenna_positions(c_coords)
        a_locs = filter_coordinates(a_locs, x_lim, y_lim, antenna_positions)
        [antenna_positions.append(loc) for loc in a_locs]

    return antenna_positions


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [obj.strip() for obj in f_obj.readlines()]

    antennas = get_result(data)

    with open('result.txt', 'r', encoding='utf-8') as f_obj:
        result = [obj.strip() for obj in f_obj.readlines()]

    print(f'\nNumber of antinodes: {len(antennas)}\n')
