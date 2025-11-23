array = [15, 8, 31, 47, 2, 19]
i = 0
total = 0
while i < len(array):
    total+=array[i]
    i+=1
total = total / len(array)
print(array)
print(total)