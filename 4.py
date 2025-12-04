import sys
import time

if __name__ == "__main__":
    start_time = time.time()

    print("Go!", flush=True)
    input_data = None
    first_run = True

    input_data = sys.stdin.read().strip()
    # with open("test.txt", "r", encoding="utf-8") as file:
    #     input_data = file.read() 

    result_1, result_2 = 0, 0
    directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

    input_list = input_data.split("\n")

    input = [list(elem) for elem in input_list]

    for i in range(0, input.__len__()):
        for j in range(0, input[0].__len__()):
            adj_value = 0
            for direction in directions:
                i_offset = i + direction[0]    
                j_offset = j + direction[1]
                if (i_offset < 0 or i_offset > input.__len__() - 1 or j_offset < 0 or j_offset > input[0].__len__() - 1):
                    continue
                else:
                    if (input[i_offset][j_offset] == '@'):
                        adj_value += 1
                    else:
                        continue
            if (adj_value < 4 and input[i][j] == '@'):
                result_1 += 1
    run_result = -1
    indices = []
    while (run_result != 0):
        for i in range(0, input.__len__()):
            for j in range(0, input[0].__len__()):
                adj_value = 0
                for direction in directions:
                    i_offset = i + direction[0]    
                    j_offset = j + direction[1]
                    if (i_offset < 0 or i_offset > input.__len__() - 1 or j_offset < 0 or j_offset > input[0].__len__() - 1):
                        continue
                    else:
                        if (input[i_offset][j_offset] == '@'):
                            adj_value += 1
                        else:
                            continue
                if (adj_value < 4 and input[i][j] == '@'):
                    if (run_result == -1):
                        run_result += 2
                    else:
                        run_result += 1
                    indices.append((i, j))
        if (run_result == -1):
            break
        result_2 += run_result
        for index in indices:
            input[index[0]].pop(index[1])
            input[index[0]].insert(index[1], '.')
        if (run_result != 0):
            run_result = -1


    

    print(f"Part 1: {result_1}\nPart 2: {result_2}\nSolved in {round((time.time() - start_time) * 1000, 2)} ms", flush=True)