import sys

N = int(sys.stdin.readline())
seats = list(sys.stdin.readline().strip())
count = len(seats)
count += 1

if seats.count('L') > 0:
    count -= seats.count('L') // 2

print(min(N, count))


