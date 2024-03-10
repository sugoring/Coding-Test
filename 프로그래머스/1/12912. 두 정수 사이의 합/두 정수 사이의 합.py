def solution(a, b):
    sum = 0
    list = [a, b]
    list.sort()
    
    for i in range(list[0], list[1] + 1):
        sum += i

    return sum