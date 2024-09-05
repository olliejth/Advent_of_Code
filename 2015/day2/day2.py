"""Functions and main script of the 2015 AoC day 2 challenges."""


def read_input(filename: str) -> list[str]:
    """Returns data contained within "filename separated by new lines."""
    with open(filename, "r") as f:
        return f.readlines()


def clean_data(box_dims: str) -> list[int]:
    box_dims = box_dims.strip()
    box_dims = box_dims.split('x')
    output_list = []
    for num in box_dims:
        output_list.append(int(num))

    return output_list


def find_paper_for_one_box(box_dims: list) -> int:
    if not isinstance(box_dims, list):
        raise TypeError('Invalid input type')

    if len(box_dims) != 3:
        raise TypeError('Invalid box data provided.')

    s1, s2, s3 = box_dims[0], box_dims[1], box_dims[2]
    a1 = s1 * s2
    a2 = s2 * s3
    a3 = s3 * s1

    slack_area = min((a1, a2, a3))

    final_area = 2*a1 + 2*a2 + 2*a3 + slack_area

    return final_area


def get_ribbon_length(box_dims: list[int]) -> int:
    """Returns required ribbon length for box of given dimensions."""
    s1, s2, s3 = box_dims[0], box_dims[1], box_dims[2]
    vol = s1 * s2 * s3

    p1 = s1 + s2
    p2 = s2 + s3
    p3 = s1 + s3

    ribbon_p = min([p1, p2, p3])

    total_length = 2*ribbon_p + vol

    return total_length


if __name__ == "__main__":

    input_data = read_input('input_data.txt')

    total_area_sum, total_ribbon_length = 0, 0
    for box in input_data:
        box = clean_data(box)
        total_area_sum += find_paper_for_one_box(box)
        total_ribbon_length += get_ribbon_length(box)

    print(total_area_sum)
    print(total_ribbon_length)
