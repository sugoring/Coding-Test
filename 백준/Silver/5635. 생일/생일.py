import sys

number = int(sys.stdin.readline())

members = []

for _ in range(number):
    name, dd, mm, yyyy = sys.stdin.readline().split()
    members.append([name, int(dd), int(mm), int(yyyy)])

# 한 번의 sort에서 여러 키를 사용하여 정렬합니다.
members.sort(key=lambda x: (x[3], x[2], x[1]))

print(members[-1][0])
print(members[0][0])
