str = list(input().split('-'))

result = 0
for i in str[0].split('+'):
    result += int(i)
    
for i in str[1:]:
    for j in i.split('+'):
        result -= int(j)
        
print(result)