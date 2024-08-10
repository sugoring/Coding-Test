import sys

input = sys.stdin.read
data = input().strip().split('\n')

T = int(data[0])

for i in range(1, T + 1):
    expression = data[i].split()
    result = float(expression[0])
    
    for operator in expression[1:]:
        if operator == '@':
            result *= 3
        elif operator == '%':
            result += 5
        elif operator == '#':
            result -= 7

    print(f"{result:.2f}")
