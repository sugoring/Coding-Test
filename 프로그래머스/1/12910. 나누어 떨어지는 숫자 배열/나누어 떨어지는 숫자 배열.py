def solution(arr, divisor):
    list = []
    
    for e in arr:
        if e % divisor == 0:
            list.append(e)
            
    list.sort()
    if len(list) == 0:
        list.append(-1)
    
    return list