"""AoC day 1 2024"""


def get_differences_sum(list_one: list[int], list_two: list[int]) -> int:
    '''Returns the sum of the differences between the numbers
    in two lists starting with the smallest from each'''
    diff_sum = 0

    list_one.sort()
    list_two.sort()

    for i in range(len(list_one)):
        diff_sum += abs(list1[i] - list_two[i])

    return diff_sum


def count_list_duplicates(list_one: list[int], list_two: list[int]) -> int:
    '''Multiplies each number in list_one by the number of 
    times it appears in list_two and sums them'''
    dupe_sum = 0

    for num in list_one:
        dupe_sum += num * list_two.count(num)

    return dupe_sum


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [line.strip().split() for line in f_obj.readlines()]

    list1 = []
    list2 = []

    for pair in data:
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))

    print(count_list_duplicates(list1, list2))
