# 입력 데이터를 받음
input_data = input()

# 입력 받은 좌표에서 행 값 추출
row = int(input_data[1])

# 입력 받은 좌표에서 열 값 추출 및 변환
column = int(ord(input_data[0]) - ord('a')) + 1

# 나이트가 이동할 수 있는 모든 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 이동할 수 있는 위치의 개수를 저장할 변수 초기화
result = 0

# 모든 이동 가능한 방향에 대해 반복하여 검사
for step in steps:
    # 다음 이동할 행, 열 좌표 계산
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 다음 이동할 위치가 체스판 안에 있는지 확인
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        # 이동할 수 있는 위치라면 결과 값 증가
        result += 1
        
# 결과 값 출력
print(result)
