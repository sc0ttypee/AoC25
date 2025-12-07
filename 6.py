import sys

if __name__ == "__main__":
    print("Go!", flush=True)
    input_data = sys.stdin.read()
    result_1, result_2 = 0, 0

    input_data = input_data.split('\n')

    operator_string = input_data.pop()
    elements = input_data
    elements.reverse()
    value = 0
    
    for idx, char in enumerate(operator_string):
        if (operator_string[idx] != ' '):
            operator = operator_string[idx]
            result_2 += value
            value = 0
        if (operator == '+'):
            cnt = 0
            for elem_string in elements:
                if (elem_string[idx] == ' '): continue
                value += int(elem_string[idx]) * 10 ** cnt
                cnt += 1
        if (operator == '*'):
            cnt = 0
            if value == 0:
                value = 1
            num = 0
            for elem_string in elements:
                if (elem_string[idx] == ' '): continue
                num += int(elem_string[idx]) * 10 ** cnt
                cnt += 1
            if (num != 0): value *= num
            
    result_2 += value

    elements = [x.split(' ') for x in input_data]
    elements = [[int(y) for y in x if not y == '']for x in elements]
    operators = [x for x in operator_string if not x == ' ']
    length = len(operators)

    while (operators):
        operator = operators[-1]
        if (operator == '+'):
            start = 0
            for elem in elements:
                start += elem.pop()
        elif (operator == '*'):
            start = elements[0].pop()
            for elem in elements[1:]:
                start = start * elem.pop()
        result_1 += start
        operators.pop()

    print(f"Part 1: {result_1}\nPart 2: {result_2}", flush=True)