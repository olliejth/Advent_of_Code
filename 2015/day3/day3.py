'''AoC day 3 2015.'''


def is_new_house(x: int, y: int, houses: list) -> bool:
    '''Returns a bool value for if the current house
    has not been visited yet.'''

    if (x, y) in houses:
        return False
    return True


def calculate_house_number(directions: str) -> int:
    '''Returns the number of unique houses visited.'''

    s_x, s_y = 0, 0
    r_x, r_y = 0, 0
    count = 1
    houses = [[0, 0]]

    for i, a in enumerate(directions):
        if i % 2 == 0:
            if a == '<':
                s_x -= 1
            elif a == '>':
                s_x += 1
            elif a == 'v':
                s_y -= 1
            elif a == '^':
                s_y += 1
            if [s_x, s_y] not in houses:
                count += 1
                houses.append([s_x, s_y])
        else:
            if a == '<':
                r_x -= 1
            elif a == '>':
                r_x += 1
            elif a == 'v':
                r_y -= 1
            elif a == '^':
                r_y += 1
            if [r_x, r_y] not in houses:
                count += 1
                houses.append([r_x, r_y])

    return count


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = f_obj.readline()

    print(calculate_house_number(data))
