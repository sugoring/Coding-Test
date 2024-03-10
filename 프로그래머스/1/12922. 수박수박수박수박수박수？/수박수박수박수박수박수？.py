def solution(n):
    if n % 2 == 0:
        answer = '수박' * (n // 2)
    elif n == 1:
        answer = '수'
    else:
        answer = '수박' * (n // 2) + '수'
    return answer