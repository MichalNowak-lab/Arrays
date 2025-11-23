matrix1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
matrix2 = [
        [1,2,3,4,5],
        [6,7,8,9,0],
    ]
matrix3 = [
        [5,6,7,8],
    ]
def transpose_matrix(m):
    transpose = [[m[j][i] for j in range(len(m))]for i in range(len(m[0]))]
    return transpose
print(transpose_matrix(matrix1))
print(transpose_matrix(matrix2))
print(transpose_matrix(matrix3))