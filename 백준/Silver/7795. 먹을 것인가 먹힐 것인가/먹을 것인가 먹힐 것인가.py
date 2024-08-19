import sys
import bisect

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))

    A.sort()
    B.sort()

    count = 0

    for a in A:
        count += bisect.bisect_left(B, a)
    
    print(count)
