K, N = map(int, input().split())
lan_lengths = [int(input()) for _ in range(K)]

start = 1
end = max(lan_lengths)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(length // mid for length in lan_lengths)
    
    if count >= N:  # N개 이상의 랜선을 만들 수 있는 경우
        result = mid  # 가능한 길이로 저장
        start = mid + 1  # 더 긴 길이를 탐색
    else:
        end = mid - 1  # 더 짧은 길이를 탐색

print(result)
