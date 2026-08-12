matrix = [
    [1, 2, 3,    4],
    [5, 6, 7,    8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [1, 1, 1, 6],
    [17, 18, 19, 20]
]


def pop_row(matrix: list[list[int]], index: int):
    return matrix.pop(index)


def pop_column(matrix: list[list[int]], index: int):
    column = []
    for row in matrix:
        column.append(row.pop(index))
    return column


last_popped_row_index = 0
last_popped_column_index = len(matrix[0]) - 1

while len(matrix) > 0 and len(matrix[0]) > 0:
    popped_row = pop_row(matrix, last_popped_row_index)
    if last_popped_row_index == 0:
        last_popped_row_index = len(matrix) - 1
    else:
        popped_row.reverse()
        last_popped_row_index = 0
    print(*popped_row, end=" ")

    popped_column = pop_column(matrix, last_popped_column_index)
    if last_popped_column_index == 0:
        popped_column.reverse()
        last_popped_column_index = len(matrix[0]) - 1
    else:
        last_popped_column_index = 0
    print(*popped_column, end=" ")

print()
