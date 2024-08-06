# 회원의 수를 정하기 위한 숫자를 입력받습니다.
number = int(input())

# 2차원 배열을 생성합니다. 배열의 각 원소는 [나이, 이름] 형태입니다.
members = []

# 입력받은 수만큼 나이와 이름을 입력받아 배열에 추가합니다.
for i in range(number):
    age, name = input().split()
    age = int(age)
    members.append([age, name])

# 나이순으로 배열을 정렬합니다.
members.sort(key=lambda x: x[0])

# 정렬된 배열을 출력합니다.
for member in members:
    print(f"{member[0]} {member[1]}")