import sys
input = sys.stdin.read

A, B, C = map(int, input().strip().split())

numbers = [A, B, C]
numbers.sort()

print(numbers[1])
