import sys

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())

left = 0
right = M - 1

count = 0  

for _ in range(J):
    loc = int(sys.stdin.readline()) - 1 

    if loc < left:  
        count += left - loc
        left = loc
        right = left + M - 1
    elif loc > right: 
        count += loc - right
        right = loc
        left = right - M + 1
   

print(count)




