arr = [list(map(int, input().split())) for _ in range(5)]
max_sum = 0
max_index = 0

for i in range(5):
    if max_sum < sum(arr[i]):
        max_sum = sum(arr[i])
        max_index = i + 1

print(max_index, max_sum)
