# 가능한 모든 시간의 경우를 하나씩 세어서 해결하는 문제를 완전 탐색(Brute Forcing) 문제 유형

# 입력으로 시간을 받음
h = int(input())

# '3'이 포함된 경우의 수를 저장할 변수 초기화
count = 0

# 시간 단위를 0부터 입력받은 시간까지 반복
for i in range(0, h + 1):
    # 분 단위를 0부터 59까지 반복
    for j in range(60):
        # 초 단위를 0부터 59까지 반복
        for k in range(60):
            # 시, 분, 초를 문자열로 합쳐서 '3'이 포함되어 있는지 확인
            if '3' in str(i) + str(j) + str(k):
                # '3'이 포함되어 있으면 count 변수를 1 증가
                count += 1

# '3'이 포함된 경우의 수 출력
print(count)
