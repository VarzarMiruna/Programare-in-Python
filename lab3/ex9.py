def seats(mat):
    pos = []
    for j in range(len(mat[0])):
        height = mat[0][j]
        for i in range(1, len(mat)):
            if mat[i][j] <= height:
                pos.append((i, j))
            else:
                height = mat[i][j]
    return pos

matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

seat = seats(matrix)
print(seat)
