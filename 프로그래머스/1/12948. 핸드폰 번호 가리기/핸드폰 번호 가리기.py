def solution(phone_number):
    n = len(phone_number)
    last = phone_number[-4:]
    return '*' * (n - 4) + last