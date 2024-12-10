

def trail_head_score(data, x, y):

    options = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    char_val = 0

    y_lim = range(len(data))
    x_lim = range(len(data[0]))

    valid_coords = [[y, x]]

    while char_val < 9:

        new_valids = []

        for coord in valid_coords:
            coord_y, coord_x = coord[0], coord[1]

            for change in options:
                new_coord_y = coord_y + change[0]
                new_coord_x = coord_x + change[1]
                if new_coord_x in x_lim and new_coord_y in y_lim:
                    new_char = data[new_coord_y][new_coord_x]
                    if int(new_char) == char_val + 1:
                        new_valids.append([new_coord_y, new_coord_x])

        valid_coords = new_valids
        char_val += 1

    # output_coords = []
    # for cd in valid_coords:
    #     if cd not in output_coords:
    #         output_coords.append(cd)

    return len(valid_coords)


def get_result(data):

    total = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '0':
                total += trail_head_score(data, x, y)

    return total


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [x.strip() for x in f_obj.readlines()]

    print(get_result(data))
