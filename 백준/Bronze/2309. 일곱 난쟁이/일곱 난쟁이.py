# 9개의 숫자를 저장할 배열을 선언
numbers = []

# 사용자로부터 9개의 숫자를 입력받아 배열에 추가
for _ in range(9):
    numbers.append(int(input()))

# 배열을 오름차순으로 정렬
numbers.sort()

# 배열의 모든 숫자의 합을 계산
total_sum = sum(numbers)

# 두 명의 숫자를 제외했을 때 합이 100이 되는 경우를 찾음
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if total_sum - numbers[i] - numbers[j] == 100:
            for k in range(len(numbers)):
                if k != i and k != j:
                    print(numbers[k])
            exit()
