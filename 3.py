import sys
import time
import math

if __name__ == "__main__":
    start_time = time.time()

    print("Go!", flush=True)
    input_data = sys.stdin.read().splitlines()
    
    result_1, result_2 = 0, 0

    for line in input_data:
        highest_left = -1
        index_01 = -1
        highest_right = -1
        index_02 = -1
        highest = 9
        int_list = [int(x) for x in line]
        while(highest > 0 and highest_left == -1):
            try:
                index_01 = int_list.index(highest)
                highest_left = int_list.pop(index_01)
            except:
                highest -= 1
                continue
        if (index_01 == int_list.__len__() -1):
            highest_right = highest_left
            highest_left = -1
            while(highest > 0 and highest_left == -1):
                try:
                    index_01 = int_list.index(highest)
                    highest_left = int_list.pop(index_01)
                except:
                    highest -= 1
                    continue
        else:
            highest = 9
            while(highest > 0 and highest_right == -1):
                try:
                    index_02 = int_list.index(highest)
                    highest_right = int_list.pop(index_02)
                except:
                    highest -= 1
                    continue
        print(f"{highest_left}{highest_right}")

    print(f"Part 1: {result_1}\nPart 2: {result_2}\nSolved in {round((time.time() - start_time) * 1000, 2)} ms", flush=True)