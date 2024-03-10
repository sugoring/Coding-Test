def solution(x):
    return True if x % sum(int(digit) for digit in str(x)) == 0 else False
