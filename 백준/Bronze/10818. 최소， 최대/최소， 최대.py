n = int(input())
arr = list(map(int, input().split()))

maximum = arr[0]
minimum = arr[0]

for i in range(1, n):
    if maximum < arr[i]:
        maximum = arr[i]
    elif minimum > arr[i]:
        minimum = arr[i]

print(minimum, maximum)
