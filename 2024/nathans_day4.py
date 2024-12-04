def read_input(filename):

    with open(filename) as f:
        lines = f.readlines()

    return lines


def check_down_right(i, j, lines):

    if j + 3 < len(lines[i])-1 and i + 3 < len(lines):
        i = i
        j = j
        if not lines[i+2][j+2] == "A":
            return 0
        if not lines[i+3][j+3] == "S":
            return 0
    else:
        return 0

    return 1


def check_down_left(i, j, lines):

    if j - 3 >= 0 and i + 3 < len(lines):
        i = i
        j = j
        if not lines[i+2][j-2] == "A":
            return 0
        if not lines[i+3][j-3] == "S":
            return 0
    else:
        return 0

    return 1


def check_up_left(i, j, lines):

    if j - 3 >= 0 and i - 3 >= 0:
        i = i
        j = j
        if not lines[i-2][j-2] == "A":
            return 0
        if not lines[i-3][j-3] == "S":
            return 0
    else:
        return 0

    return 1


def check_up_right(i, j, lines):

    if j + 3 < len(lines[i])-1 and i - 3 >= 0:
        i = i
        j = j
        if not lines[i-2][j+2] == "A":
            return 0
        if not lines[i-3][j+3] == "S":
            return 0
    else:
        return 0

    return 1


def check(i, j, lines):

    right = False
    left = False
    if (i > 0 and i < len(lines) - 1) and (j > 0 and j < len(lines[i])-1):
        mas_r = lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1]

        if mas_r == "MAS" or mas_r[::-1] == "MAS":
            right = True

        mas_l = lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1]
        if mas_l == "MAS" or mas_l[::-1] == "MAS":
            left = True

    if right and left:
        return 1
    else:
        return 0


def day4(lines):

    count = 0
    for i in range(len(lines)):

        for j in range(len(lines[i])):
            if lines[i][j] == "A":

                count += check(i, j, lines)

    return count


if __name__ == "__main__":
    filename = 'input.txt'
    test_data = ["MMMSXXMASM",
                 "MSAMXMSMSA",
                 "AMXSXMAAMM",
                 "MSAMASMSMX",
                 "XMASAMXAMM",
                 "XXAMMXXAMA",
                 "SMSMSASXSS",
                 "SAXAMASAAA",
                 "MAMMMXMMMM",
                 "MXMXAXMASX"]
    input_data = read_input(filename)
    # input_data = test_data
    print(day4(input_data))
