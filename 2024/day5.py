"""AoC day 5 2024"""


def is_valid_update(update: list[int], rules: list[tuple]) -> bool:
    '''Checks whether an update abides by the rules.'''

    for i, num in enumerate(update):
        for later_num in update[i:]:
            if (later_num, num) in rules:
                return False
    return True


def get_middle_sum(valid_ups: list[list]) -> int:
    '''Returns sum of middle numbers from valid updates.'''

    valid_sum = 0

    for update in valid_ups:
        middle_idx = int(((len(update) + 1) / 2) - 1)
        valid_sum += update[middle_idx]

    return valid_sum


def find_blockers(idx: int, num: int, update: list[int], rules: list[tuple]) -> list[bool]:
    '''Finds whether there are any rules which would stop'''

    up_copy = update.copy()
    del up_copy[idx]

    blocker_list = [(n, num) in rules for n in up_copy]

    return blocker_list


def fix_invalid(invalid_updates: list[list], rules: list[tuple]) -> list[list]:
    '''Returns fixed version of invalid updates.'''
    output_list = []

    for update in invalid_updates:
        update_length = len(update)
        new_update = []
        while len(new_update) < update_length:
            for idx, num in enumerate(update):
                blocker_list = find_blockers(idx, num, update, rules)
                if not any(blocker_list):
                    new_update.append(num)
                    del update[idx]
        output_list.append(new_update)

    return output_list


def get_result(rules: list[tuple], updates: list[list]) -> int:
    '''AoC 2024 day 5 part 1.'''

    valid_updates = []
    invalid_updates = []

    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    valid_sum = get_middle_sum(valid_updates)

    fixed_updates = fix_invalid(invalid_updates, rules)

    invalid_sum = get_middle_sum(fixed_updates)

    return valid_sum, invalid_sum


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [obj.strip() for obj in f_obj.readlines()]

    space_idx = data.index('')

    rules_str = data[:space_idx]
    rules = [(int(item.split('|')[0]), int(item.split('|')[1]))
             for item in rules_str]
    updates_str = data[space_idx + 1:]
    updates = []
    for update in updates_str:
        up_list = []
        for num in update.split(','):
            up_list.append(int(num))
        updates.append(up_list)

    valid_sum, invalid_sum = get_result(rules, updates)

    print(f'Valid sum    :  {valid_sum}')
    print(f'Invalid sum  :  {invalid_sum}')
