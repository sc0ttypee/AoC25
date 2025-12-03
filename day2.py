import sys
import time

if __name__ == "__main__":
    start_time = time.time()
    input = sys.stdin.read()
    
    rngs = map(lambda x : x.split("-"), input.split(","))
    counter = 0

    for rng in rngs:
        start = int(rng[0])
        end = int(rng[1])
        for possibility in range(start, end + 1):
            possibility_str = str(possibility)
            half = len(possibility_str) // 2
            if (len(possibility_str) % 2 != 0):
                continue
            if (possibility_str[:half] == possibility_str[half:]):
                counter += possibility

    print(f"Counter is: {counter}\nCalculation took {time.time() - start_time} seconds")