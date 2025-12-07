import sys
import time

DIRECTION = (1, 0)

def traverse_light(diagram: list[list[str]],):
    pass

def split(diagram: list[str], coordinate: tuple[int, int], split_amount: int):

    left = (coordinate[0], coordinate[1] - 1)
    right = (coordinate[0], coordinate[1] + 1)
    
    while left[0] < len(diagram) and (diagram[left[0]][left[1]]) == '.':
        diagram[left[0]][left[1]] = '|'
        left = (left[0] + DIRECTION[0]), (left[1] + DIRECTION[1])
    if  left[0] < len(diagram) and (diagram[left[0]][left[1]]) == '^':
        for line in diagram: print(line)
        split_amount += split(diagram, left, split_amount)

    while right[0] < len(diagram) and (diagram[right[0]][right[1]]) == '.':
        diagram[right[0]][right[1]] = '|'
        right = (right[0] + DIRECTION[0]), (right[1] + DIRECTION[1])
    if  right[0] < len(diagram) and (diagram[right[0]][right[1]]) == '^':
        for line in diagram: print(line)
        split_amount += split(diagram, right, split_amount)

    return 1

if __name__ == "__main__":
    start_time = time.time()

    print("Go!", flush=True)
    # input_data = sys.stdin.read()   
    
    with open("test.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip()

    diagram = input_data.strip().split('\n')

    start_coords = (0, diagram[0].index('S'))

    diagram = [list(line) for line in diagram]
    start_coords = (start_coords[0] + DIRECTION[0]), (start_coords[1] + DIRECTION[1])
    
    while start_coords[0] < diagram.__len__() and (diagram[start_coords[0]][start_coords[1]]) == '.':

        diagram[start_coords[0]][start_coords[1]] = '|'
        start_coords = (start_coords[0] + DIRECTION[0]), (start_coords[1] + DIRECTION[1])

    result_1, result_2 = 0, 0
    result_1 += split(diagram, start_coords, -1)



    

    print(f"Part 1: {result_1}\nPart 2: {result_2}\nSolved in {round((time.time() - start_time) * 1000, 2)} ms", flush=True)