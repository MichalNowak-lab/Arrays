

arr = [[-38, 19], [5,40],[-7,11],[29,16]]
max_val = arr[0][0]
max_index = (0,0)
min_val = arr[0][0]
min_index = (0,0)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]> max_val:
            max_val = arr[i][j]
            max_index = (i,j)

for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x]< min_val:
            min_val = arr[x][y]
            min_index = (x,y)
print("Biggest value:", max_val)
print("Index (row, column):", max_index)
print("Smallest value:", min_val)
print("Index (row, column):", min_index)