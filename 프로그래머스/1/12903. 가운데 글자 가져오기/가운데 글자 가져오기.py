def solution(s):
    i = len(s) // 2
    if len(s) % 2 == 0: 
        answer = s[i-1] + s[i]
    else:
        answer = s[i] 
    return answer