matrix1 = [
    [2,3],
    [1,5]
]
matrix2 = [[5,0,3,7,5],[9,0,9,1,2]]
matrix3 = [[2,1],[3,5],[7,4],[2,6]]
def convert_to_1d(matrix):
    one_d = []
    for row in matrix:
        for value in row:
            one_d.append(value)
    return one_d
print(convert_to_1d(matrix1))
print(convert_to_1d(matrix2))
print(convert_to_1d(matrix3))