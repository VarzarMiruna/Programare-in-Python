def change_mat(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j < i:
                matrix[i][j] = 0
    return matrix


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# print(change_mat(matrix))
mat = change_mat(matrix)
for row in mat:
    print(row)