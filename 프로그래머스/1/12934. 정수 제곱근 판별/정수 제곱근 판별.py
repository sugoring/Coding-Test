import math

def solution(n):
    m = int(math.sqrt(n))
    if m**2 == n:
        answer = (m+1)**2
    else:
        answer = -1
    return answer
