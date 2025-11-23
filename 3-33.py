array = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15]
]

print("Array before swapping columns:")
for row in array:
    for value in row:
        print(value, end=' ')
    print()

for i in range(3):  # 3 rows
    array[i][0], array[i][4] = array[i][4], array[i][0]

print("\nArray after swapping columns:")
for row in array:
    for value in row:
        print(value, end=' ')
    print()