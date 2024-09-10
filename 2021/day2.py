
def get_new_positions(direction: list, position: dict[int]) -> tuple[int, int]:
    h_position = position["horizontal"]
    depth = position["depth"]
    aim = position["aim"]

    if direction[0] == "forward":
        h_position += int(direction[1])
        depth += (int(direction[1]) * aim)
    elif direction[0] == "up":
        aim -= int(direction[1])
    elif direction[0] == "down":
        aim += int(direction[1])

    return h_position, depth, aim


def get_final_positions(directions: list[str]) -> int:
    positions = {"horizontal": 0, "depth": 0, "aim": 0}

    for direction in directions:
        dir_list = direction.split()
        new_h, new_d, new_aim = get_new_positions(dir_list, positions)
        positions["horizontal"] = new_h
        positions["depth"] = new_d
        positions["aim"] = new_aim

    res = positions["horizontal"] * positions["depth"]

    return res


if __name__ == "__main__":

    with open("example_data.txt", "r", encoding="utf-8") as f_obj:
        data = [item.strip() for item in list(f_obj.readlines())]

    print(get_final_positions(data))
