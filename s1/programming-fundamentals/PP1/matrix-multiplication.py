matrixA = [
    # 2 row
    # 5 col
    [1, 2, 3, 4, 5],
    [4, 5, 6, 1, 2]
]

matrixB = [
    # 5 row
    # 2 col
    [7, 8],
    [9, 10],
    [11, 2],
    [1, 2],
    [0, 3],
]


def multiply(m1, m2):
    # m1 is n x m
    # m2 is m x p
    result_matrix = []

    # to create the structure
    for row_i in range(len(m1)):
        column_count = len(m2[0])
        row = []
        for col_i in range(column_count):
            row.append(0)
        result_matrix.append(row)

    # update the values
    for row_i in range(len(m1)):
        for col_i in range(len(m2[0])):
            # row and col selected
            for i in range(len(m1[0])):
                result_matrix[row_i][col_i] += m1[row_i][i] * m2[i][col_i]

    return result_matrix


result = multiply(matrixA, matrixB)
print(result)
