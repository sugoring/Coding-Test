import sys

N = int(sys.stdin.readline().strip())

numbers = []
for _ in range(N): 
    num = int(sys.stdin.readline().strip())
    numbers.append(num)

numbers.sort()
for i in range(N):
    print(numbers[i])
