

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


imported_data = read_input("example_data.txt")

no_of_increases = map_depth_of_ocean(imported_data)

print(no_of_increases)

# if __name__ == "__main__":
#     """Main script"""
