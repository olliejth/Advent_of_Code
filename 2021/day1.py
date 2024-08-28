"""2021 AoC Day 1."""


def read_input(filename: str) -> list[str]:
    """Returns data contained within "filename separated by new lines."""
    with open(filename, "r") as f:
        return f.readlines()


def map_depth_of_ocean(depth_list: list[str]) -> int:
    """Returns number of times that ocean depth increases between readings."""
    increase_counter = 0
    for i, d in enumerate(depth_list):
        if i != 0 and int(d) > int(depth_list[i-1]):
            increase_counter += 1

    return increase_counter


def map_cumulative_depth(depth_list: list[str]) -> int:
    data_length = len(depth_list)
    max_index = data_length - 2
    last_sum = 0
    increase_counter = 0
    for i in range(0, data_length):
        # print(i)
        if i < max_index:
            depth_sum = int(depth_list[i]) + \
                int(depth_list[i+1]) + int(depth_list[i+2])
        if i != 0 and depth_sum > last_sum:
            increase_counter += 1
        last_sum = depth_sum

    return increase_counter


imported_data = read_input("example_data.txt")

no_of_increases = map_depth_of_ocean(imported_data)


print(map_cumulative_depth(imported_data))
