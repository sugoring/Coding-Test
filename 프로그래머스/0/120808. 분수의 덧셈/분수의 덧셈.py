def solution(numer1, denom1, numer2, denom2):
    new_numer = numer1 * denom2 + numer2 * denom1
    new_denom = denom1 * denom2
    
    greatest_common_divisor = gcd(new_numer, new_denom)
    
    result_numer = new_numer // greatest_common_divisor
    result_denom = new_denom // greatest_common_divisor
    
    return [result_numer, result_denom]

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a