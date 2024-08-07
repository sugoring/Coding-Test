import sys

number = int(sys.stdin.readline())
arr = []

for i in range(number):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(a + b)
    
for result in arr:
    print(result)
