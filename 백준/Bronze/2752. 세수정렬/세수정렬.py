import sys
numbers = list(map(int, input().strip().split()))

numbers.sort()

print(numbers[0], numbers[1], numbers[2])
