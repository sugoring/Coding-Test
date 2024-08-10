import sys

number = int(sys.stdin.readline())

members = []

for _ in range(number):
    name, dd, mm, yyyy = sys.stdin.readline().split()
    if (len(dd) == 1):
        dd = "0" + dd
    if (len(mm) == 1):
        mm = "0" + mm
    yyyymmdd = yyyy + mm + dd
    
    members.append([name, int(yyyymmdd)])

members.sort(key=lambda x: x[1])

print(members[-1][0])
print(members[0][0])