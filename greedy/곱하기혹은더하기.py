data = input()

array = int(data[0])

for i in range(1, len(data)):
    n = int(data[i])
    if n <= 1 or array <= 1:
        array += n
    else:
        array *= n
        
print(array)
