import sys
import time

if __name__ == "__main__":
    print("Go!", flush=True)
    input_data = sys.stdin.read().strip()

    # with open("test.txt", "r", encoding="utf-8") as file:
    #     input_data = file.read().strip()

    result_1, result_2 = 0, 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]

    input_list = input_data.split("\n")

    row_len = len(input_list)
    col_len = len(input_list[0])

    input_list = ['.' * row_len] + input_list + ['.' * row_len]
    input = [list('.' + elem + '.') for elem in input_list]
    marked = set()
    for i in range(1, row_len + 1):
        for j in range(1, col_len + 1):
            adj_value = 0   
            for direction in directions:
                if (input[i + direction[0]][j + direction[1]] == '@'):
                    adj_value += 1
            if (adj_value) < 4:
                marked.add((i, j))
    for mark in marked:
        if (input[mark[0]][mark[1]] == '@'):
            result_1 += 1
            input[mark[0]][mark[1]] = '.'
    
    result_2 = result_1
    marked.clear()

    while True:

        for i in range(1, row_len + 1):
            for j in range(1, col_len + 1):
                adj_value = 0   
                for direction in directions:
                    if (input[i + direction[0]][j + direction[1]] == '@'):
                        adj_value += 1
                if (adj_value) < 4 and input[i][j] == '@':
                    marked.add((i, j))
        if marked.__len__() == 0:
            break
        for mark in marked:
            if (input[mark[0]][mark[1]] == '@'):
                result_2 += 1
                input[mark[0]][mark[1]] = '.'
        marked.clear()

    print(f"Part 1: {result_1}\nPart 2: {result_2}\n", flush=True)
