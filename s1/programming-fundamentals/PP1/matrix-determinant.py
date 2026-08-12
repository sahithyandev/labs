matrix = [
    [10, 2, 3, 4],
    [5, 6, -7, 8],
    [15, 1, 2, 3],
    [4, 5, 6, 7],
]


def cofactor(m, row_i, row_j):
    reduced_matrix = []
    for row in range(1, len(m)):
        _row = []
        for col in range(len(m[0])):
            if col != row_j:
                _row.append(m[row][col])
        reduced_matrix.append(_row)

    return ((-1) ** (row_i + row_j)) * determinent(reduced_matrix)


def determinent(m):
    if len(m) == 2 and len(m[0]) == 2:
        return m[0][0] * m[1][1] - m[1][0] * m[0][1]
    s = 0
    for i in range(len(m[0])):
        x = (m[0][i]) * cofactor(m, 0, i)
        s += x
    return s


print(determinent(matrix))
