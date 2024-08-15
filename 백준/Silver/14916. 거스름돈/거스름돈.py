import sys

N = int(sys.stdin.readline())

count = 0
five = N // 5

while five >= 0:
    if (N - five * 5) % 2 == 0:
        print((N - five * 5) // 2 + five)
        break
    five -= 1
else:
    print(-1)
