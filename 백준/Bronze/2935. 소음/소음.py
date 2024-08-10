import sys
input = sys.stdin.read
data = input().strip().split('\n')

A = int(data[0])
operator = data[1]
B = int(data[2])

if operator == '+':
    result = A + B
elif operator == '*':
    result = A * B

print(result)
