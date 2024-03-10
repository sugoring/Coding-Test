# 입력을 받음
data = input()

# 결과를 저장할 리스트 초기화
result = []

# 숫자의 합을 저장할 변수 초기화
value = 0

# 입력으로 받은 각 문자에 대해 반복
for x in data:
    # 만약 문자가 알파벳이면 결과 리스트에 추가
    if x.isalpha:
        result.append(x)
    # 숫자라면 숫자의 합을 계산하기 위해 값을 더함
    else:
        value += int(x)

# 알파벳을 사전 순으로 정렬
result.sort()

# 숫자의 합이 0이 아니라면 결과 리스트에 추가
if value != 0:
    result.append(str(value))
    
# 결과 리스트를 문자열로 변환하여 출력
print(''.join(result))
