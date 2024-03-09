n, k = map(int, input().split())
count = 0

while n > 1:
    target = (n // k) * k # 나누어 떨어지는 수를 찾아내기
    count += (n - target) 
    n = target
    
    if n < k:
        break

    n //= k
    count += 1

print(count)
