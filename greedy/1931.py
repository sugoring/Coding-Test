n = int(input())
meet = [tuple(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], x[0]))
count = 1 if meet[0][1] != 0 else 0
compare = meet[0][1]

for i in range(1, n):
    if compare <= meet[i][0]:
        count += 1
        compare = meet[i][1]
    else:
        continue
    
print(count)