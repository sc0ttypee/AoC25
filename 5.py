import sys
import time

if __name__ == "__main__":
    start_time = time.time()

    print("Go!", flush=True)
    # input_data = sys.stdin.read().strip()
    result_1, result_2 = 0, 0
    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip()
    id_ranges, available_ids = input_data.split('\n\n')

    id_ranges = id_ranges.split('\n')
    available_ids = available_ids.split('\n')

    fresh = set()

    available_ids = [int(x) for x in available_ids]
    print("creating ranges...")
    id_ranges = [set([i for i in range(int(x), int(y) + 1)]) for x, y in  [x.split('-') for x in id_ranges]]
    for x in id_ranges: fresh.update(x)
    x = [i for i in range(1, 3 + 1)]

    print("checking ids...")
    for id in available_ids:
        if (id in fresh): result_1 += 1

    

    print(f"Part 1: {result_1}\nPart 2: {result_2}\nSolved in {round((time.time() - start_time) * 1000, 2)} ms", flush=True)