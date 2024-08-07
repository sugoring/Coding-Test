import sys

# 첫 번째 줄에서 점의 개수를 입력받습니다.
n = int(sys.stdin.readline().strip())
points = []

# 각 점의 좌표를 입력받아 리스트에 저장합니다.
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    points.append((x, y))

# 점들을 정렬합니다. x좌표를 기준으로, x좌표가 같으면 y좌표를 기준으로 정렬합니다.
points.sort(key=lambda point: (point[0], point[1]))

# 정렬된 점들을 출력합니다.
for point in points:
    print(point[0], point[1])
