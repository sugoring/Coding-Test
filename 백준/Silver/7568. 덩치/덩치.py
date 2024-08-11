import sys

# 사람의 수 N을 입력받습니다.
N = int(sys.stdin.readline().strip())
arr = []

# 각 사람의 몸무게와 키를 입력받아 arr 리스트에 저장합니다.
for i in range(N):
    weight, height = map(int, sys.stdin.readline().strip().split())
    arr.append((weight, height))

# 초기 등수를 모두 1로 설정합니다.
ranks = [1] * N

# 등수 계산
for i in range(N):
    for j in range(N):
        if i != j:
            if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
                ranks[i] += 1

# 결과 출력
print(" ".join(map(str, ranks)))
