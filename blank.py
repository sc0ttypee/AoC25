import sys
import time

if __name__ == "__main__":
    start_time = time.time()

    print("Go!", flush=True)
    input_data = sys.stdin.read()   
    
    result_1, result_2 = 0, 0
    

    print(f"Part 1: {result_1}\nPart 2: {result_2}\nSolved in {round((time.time() - start_time) * 1000, 2)} ms", flush=True)