import sys

number = int(sys.stdin.readline())

members = []

for i in range(number):
    name, dd, mm, yyyy = sys.stdin.readline().split()
    members.append([name, int(dd), int(mm), int(yyyy)])

members.sort(key=lambda x: x[1])
members.sort(key=lambda x: x[2])
members.sort(key=lambda x: x[3])


print(members[number-1][0])
print(members[0][0])

