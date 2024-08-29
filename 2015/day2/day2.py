"""Functions and main script of the 2015 AoC day 2 challenges."""


def read_input(filename: str) -> list[str]:
    """Returns data contained within "filename separated by new lines."""
    with open(filename, "r") as f:
        return f.readlines()


def find_paper_for_one_box(box_dimensions: str) -> int:
    if not isinstance(box_dimensions, str):
        raise TypeError('Invalid input type')

    dim_list = box_dimensions.split('x')
    if len(dim_list) != 3:
        raise ValueError('Invalid box data provided.')

    s1, s2, s3 = dim_list[0], dim_list[1], dim_list[2]
    a1 = int(s1) * int(s2)
    a2 = int(s2) * int(s3)
    a3 = int(s3) * int(s1)

    slack_area = min((a1, a2, a3))

    final_area = 2*a1 + 2*a2 + 2*a3 + slack_area

    return final_area


if __name__ == "__main__":

    input_data = read_input('input_data.txt')

    total_area_sum = 0

    for box in input_data:
        total_area_sum += find_paper_for_one_box(box.strip())

    print(total_area_sum)
