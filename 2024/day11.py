def get_result(data: list[str]):

    for _ in range(36):
        new_list = []
        for stone in data:
            l = len(stone)
            if stone == '0':
                new_list.append('1')
            elif l % 2 == 0:
                l2 = len(stone) // 2
                new_list.append(f'{int(stone[:l2])}')
                new_list.append(f'{int(stone[l2:])}')
            else:
                new_list.append(f'{int(stone) * 2024}')
        data = new_list

    return len(data)


def get_result2(data: list[str]) -> int:

    cache_dict = {}

    for _ in range(36):
        new_list = []
        for stone in data:
            if cache_dict.get(stone):
                data.extend(cache_dict[stone])
            else:
                if stone == '0':
                    new = '1'
                    new_list.append('1')
                else:
                    stone_len = len(stone)
                    if stone_len % 2 == 0:
                        mid = stone_len // 2
                        new = [stone[:mid], stone[mid:]]
                        new_list.extend(new)
                    else:
                        new = str(int(stone) * 2024)
                        new_list.append(str(int(stone) * 2024))
                cache_dict[stone] = new
        data = new_list

    return len(data)


def get_start_map(raw_input: str) -> dict[int, int]:
    result = {}
    for num in raw_input:
        num = int(num)
        result[num] = result.get(num, 0) + 1
    return result


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = f_obj.readline().split()

    print(get_start_map(data))


# If the stone is engraved with the number 0, it is
# replaced by a stone engraved with the number 1.

# If the stone is engraved with a number that has an
# even number of digits, it is replaced by two stones.
# The left half of the digits are engraved on the new left stone,
# and the right half of the digits are engraved on the new right
# stone. (The new numbers don't keep extra leading zeroes: 1000
# would become stones 10 and 0.)

# If none of the other rules apply, the stone is replaced by a new stone;
# the old stone's number multiplied by 2024 is engraved on the new stone.
