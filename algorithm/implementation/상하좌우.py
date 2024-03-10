# 격자의 크기 입력 받기
n = int(input())

# 현재 위치 초기화 (시작점은 (1, 1))
x, y = 1, 1

# 이동 계획 입력 받기
plans = input().split()

# 상, 하, 좌, 우 이동에 따른 x, y의 변화량 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동 방향에 따른 문자열 정의
move_types = ['L', 'R', 'U', 'D']

# 각 이동 계획에 따라 이동하기
for plan in plans:
    # 이동 방향을 확인하여 이동할 위치 계산
    for i in range(len(move_types)):
        if plan == move_types[i]:  # 현재 이동 계획이 이동 방향 문자열과 일치하는지 확인
            nx = x + dx[i]  # 다음 x 좌표 계산
            ny = y + dy[i]  # 다음 y 좌표 계산
    
    # 만약 이동한 위치가 격자를 벗어나면 넘어가기
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    
    # 이동한 위치가 격자 내에 있으면 현재 위치 갱신
    x, y = nx, ny
    
# 최종 위치 출력
print(x, y)
