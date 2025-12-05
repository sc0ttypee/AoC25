import sys

if __name__ == "__main__":
    print("Go!", flush=True)

    input_data = sys.stdin.read()

    id_ranges, available_ids = input_data.split("\n\n")
    result_1, result_2 = 0, 0

    id_ranges = id_ranges.split('\n')
    available_ids = available_ids.split('\n')

    available_ids = [int(x) for x in available_ids]
    id_ranges = [(int(x) , int(y)) for x, y in  [x.split('-') for x in id_ranges]]
    id_ranges.sort(key = lambda x : x[0])

    for id in available_ids:
        for range in id_ranges:
            if (range[0] <= id <= range[1]):
                result_1 += 1
                break

    while (True):
        # start with first elem in sorted list, remove and save start and end index
        start_range = id_ranges.pop(0)
        interval_start = start_range[0]
        interval_end = start_range[1]

        while id_ranges:
            # iterate over all elements in the for loop.
            # for each element where the start is smaller than the previously saved end, set the end as the new "end"
            # break as soon as the next start index is no longer in the interval.
            # then add the sum of the difference (end - start) to the result
            range = id_ranges[0]
            if (range[0] <= interval_end):
                interval_end = max(interval_end, range[1])
                id_ranges.pop(0)
            else:
                break
        result_2 += (interval_end - interval_start + 1)
        if (not id_ranges):
            break
                
    print(f"Part 1: {result_1}\nPart 2: {result_2}", flush=True)