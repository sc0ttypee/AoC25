import sys
import time
import math

if __name__ == "__main__":
    start_time = time.time()

    print("Go!", flush=True)
    input_data = sys.stdin.read().splitlines()
    
    result_1, result_2 = 0, 0

    for line in input_data:
        int_list = [int(x) for x in line]
        int_list.reverse()
        lowest = 1
        while (int_list.__len__() > 12):
            try:
                int_list.pop(int_list.index(lowest))
            except:
                lowest +=1
                continue

        int_list.reverse()
        counter = 11
        res = 0
        for x in int_list:
            res += x * 10 ** counter
            counter -= 1
        print(res)
        result_2 += res
    print(result_2)

def part_1(input_data):
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
                print(f"highest left: {highest_left}")
                rest = rest[idx + 1:]
            except:
                max_val -= 1
                continue
        max_val = 9
        while (max_val > 0 and highest_right == -1):
            try:
                idx = rest.index(max_val)
                highest_right = rest[idx]
                print(f"highest right: {highest_right}")
            except:
                max_val -= 1
                continue
        if (highest_right < last):
            result_1 += highest_left * 10 + last
            print(highest_left * 10 + last)
        else:
            result_1 += highest_left * 10 + highest_right
            print(highest_left * 10 + highest_right)


    print(f"Part 1: {result_1}\nPart 2: {result_2}\nSolved in {round((time.time() - start_time) * 1000, 2)} ms", flush=True)