import sys

if __name__ == "__main__":

    print("Go!", flush=True)
    input_data = sys.stdin.read().splitlines()
    result_1, result_2 = 0, 0

    for line in input_data:
        int_list = [int(x) for x in line]
        last = int_list[-1]
        rest = int_list[:-1]
        highest_left = -1
        highest_right = -1
        max_val = 9
        while (max_val > 0 and highest_left == -1):
            try:
                idx = rest.index(max_val)
                highest_left = rest[idx]
                rest = rest[idx + 1:]
            except:
                max_val -= 1
                continue
        max_val = 9
        while (max_val > 0 and highest_right == -1):
            try:
                idx = rest.index(max_val)
                highest_right = rest[idx]
            except:
                max_val -= 1
                continue
        if (highest_right < last):
            result_1 += highest_left * 10 + last
        else:
            result_1 += highest_left * 10 + highest_right

    zip_with = [10 ** x for x in range(11, -1, -1)]

    for line in input_data:
        int_list = [int(x) for x in line]
        delete_budget = int_list.__len__() - 12
        result = []
        for digit in int_list:
            while result.__len__() > 0 and result[-1] < digit and delete_budget > 0:
                result.pop()
                delete_budget -= 1
            result.append(digit)
        result = result[:12]
        line_value = 0
        for idx, elem in enumerate(result):
            line_value += elem * zip_with[idx]
        result_2 += line_value
    print(f"Part 1: {result_1}\nPart 2: {result_2}", flush=True)