import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))  # 리스트를 집합으로 변경
M = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

for query in queries:
    if query in A:  # 집합에서 쿼리 확인 (평균 O(1))
        print(1)
    else:
        print(0)
