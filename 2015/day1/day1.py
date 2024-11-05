"""Day 1 AoC 2015"""


def find_floor(instructions: str) -> int:
    """Finds the floor number from a string of parentheses."""

    if not isinstance(instructions, str):
        raise TypeError('Input instructions must be a string.')

    count = 0

    for i, b in enumerate(instructions):
        if b not in '()':
            raise ValueError('Instructions must only contain parentheses.')
        elif b == '(':
            count += 1
        elif b == ')':
            count -= 1
        if count < 0:
            return i + 1

    return count, 'Basement never entered'


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = f_obj.readline()

    print(find_floor(data))
