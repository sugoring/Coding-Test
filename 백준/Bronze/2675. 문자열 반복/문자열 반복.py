import sys

input = sys.stdin.read
data = input().strip().split('\n')

T = int(data[0])

for i in range(1, T + 1):
    R, S = data[i].split()
    R = int(R)
    
    result = ''.join([char * R for char in S])
    
    print(result)
