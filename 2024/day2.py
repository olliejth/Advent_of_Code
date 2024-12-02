"""AoC day 2 2024."""


def is_report_safe(report: list[str]) -> bool:
    '''Returns bool for if report is safe.'''
    int_rep = [int(n) for n in report]

    rep_length = len(int_rep)

    if int_rep[1] > int_rep[0]:
        for i in range(1, rep_length):
            diff = int_rep[i] - int_rep[i - 1]
            if diff not in [1, 2, 3]:
                return False
        return True

    elif int_rep[1] < int_rep[0]:
        for i in range(1, rep_length):
            diff = int_rep[i] - int_rep[i - 1]
            if diff not in [-1, -2, -3]:
                return False
        return True

    else:
        return False


def calculate_safe_reports(report_list: list) -> int:
    '''Calculates number of safe reports from input list.'''
    safe_sum = 0

    big_list = []
    for rep in report_list:
        med_list = []
        med_list.append(rep.copy())
        for i in range(len(rep)):
            to_add = rep.copy()
            del to_add[i]
            med_list.append(to_add)
        big_list.append(med_list)

    for med_list in big_list:
        safe_list = [is_report_safe(report) for report in med_list]
        if any(safe_list):
            print('Safe')
            safe_sum += 1
        else:
            print('Unsafe')

    return safe_sum


if __name__ == "__main__":

    with open('data.txt', 'r', encoding='utf-8') as f_obj:
        data = [line.split() for line in f_obj.readlines()]

    print(calculate_safe_reports(data))
