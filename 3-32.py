from random import randint
arr = [[randint(1,22) for i in range(5)] for j in range(3)]
print(arr)
for row in arr:
    for item in row:
        print(item, end= ' ')
    print()
arr[0],arr[2]=arr[2],arr[0]
print('\n')
for row in arr:
    for item in row:
        print(item,end=' ')
    print()