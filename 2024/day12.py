

with open('data.txt', 'r', encoding='utf-8') as f_obj:
    data = [obj.strip() for obj in f_obj.readlines()]

X_LIM = range(len(data[0]))
Y_LIM = range(len(data))
OPTIONS = {(1, 0): '1', (0, 1): '2', (-1, 0): '3', (0, -1): '4'}
X_C = {1.5: (1, 1), 2.5: (-1, 1), 3.5: (-1, -1), 4.5: (1, -1)}


def get_letter_perimeter(letter: str, x: int, y: int, data: list[str]):

    adjacent = 0
    for opt in OPTIONS.keys():
        new_x = x + opt[0]
        new_y = y + opt[1]
        if new_x in X_LIM and new_y in Y_LIM:
            new_char = data[new_y][new_x]
            if new_char == letter:
                adjacent += 1

    plant_perimeter = 4 - adjacent

    return [plant_perimeter, adjacent]


def get_patch_sides(adjacents: list[int]) -> int:

    if len(adjacents) == 1 or min(adjacents) == 3:
        return 4

    return 4 + (adjacents.count(1) * 2)


def get_patch_vertices(letter: str, patch_coords: list, data: list[str]) -> int:

    vertices = 0

    for coord in patch_coords:
        adjacents = []
        one_five = data[y + X_C[1.5][1]][x + X_C[1.5][0]]
        two_five = data[X_C[2.5][1]][X_C[2.5][0]]
        three_five = data[X_C[3.5][1]][X_C[3.5][0]]
        four_five = data[X_C[4.5][1]][X_C[4.5][0]]
        x = coord[0]
        y = coord[1]
        for opt in OPTIONS.keys():
            new_x = x + opt[0]
            new_y = y + opt[1]
            if new_x in X_LIM and new_y in Y_LIM:
                new_char = data[new_y][new_x]
                if new_char == letter:
                    adjacents.append(OPTIONS[opt])

        print(f'ADJs: {adjacents}')

        if len(adjacents) > 3:
            print('This_1')
            vert = 0
        elif len(adjacents) == 0:
            vert = 4
        # elif len(adjacents) == 3:
        #     if '1'
        elif len(adjacents) == 2:
            if '1' in adjacents and '3' in adjacents:
                print('This_2')
                vert = 0
            elif '2' in adjacents and '4' in adjacents:
                print('This_3')
                vert = 0
            else:
                if '1' in adjacents and '2' in adjacents:
                    if one_five == letter:
                        vert = 1
                    else:
                        vert = 2
                elif '3' in adjacents and '2' in adjacents:
                    if two_five == letter:
                        vert = 1
                    else:
                        vert = 2
                elif '3' in adjacents and '4' in adjacents:
                    if three_five == letter:
                        vert = 1
                    else:
                        vert = 2
                elif '1' in adjacents and '4' in adjacents:
                    print(f'Letter: {letter}')
                    print(f'Four_five: {four_five}')
                    if four_five == letter:
                        vert = 1
                    else:
                        vert = 2
        else:
            vert = 2
        print(f'Coords: {[x, y]}')
        print(f'Verts: {vert}')
        print('-')
        vertices += vert

    return vertices


def get_area_and_per(letter: str, x: int, y: int, data: list[str]) -> dict:

    patch_coords = [(x, y)]
    same_letters = [(x, y)]

    while len(same_letters) >= 1:
        new_coords = []
        for coord in same_letters:
            for opt in OPTIONS.keys():
                new_x = coord[0] + opt[0]
                new_y = coord[1] + opt[1]
                new_coord = (new_x, new_y)
                if new_x in X_LIM and new_y in Y_LIM and new_coord not in patch_coords:
                    new_char = data[new_y][new_x]
                    if new_char == letter:
                        patch_coords.append(new_coord)
                        new_coords.append(new_coord)

        same_letters = new_coords

    # patch_per = 0
    # patch_adj = []
    # for c in patch_coords:
    #     res = get_letter_perimeter(letter, c[0], c[1], data)
    #     patch_per += res[0]
    #     patch_adj.append(res[1])

    # print(patch_adj)

    patch_vertices = get_patch_vertices(letter, patch_coords, data)
    print(patch_vertices)

    patch_area = len(patch_coords)

    patch_cost = patch_area * patch_vertices

    return {'sum': patch_cost, 'coords': patch_coords}


def get_result(data: list[str]) -> int:

    cost_sum = 0
    coords_visited = []

    for y, line in enumerate(data):
        for x, let in enumerate(line):
            if (x, y) not in coords_visited:
                patch = get_area_and_per(let, x, y, data)
                coords_visited.extend(patch['coords'])
                cost_sum += patch['sum']

    print(cost_sum)


if __name__ == "__main__":

    get_result(data)
