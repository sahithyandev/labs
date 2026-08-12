
def read_matrix_data(matrix_file_name: str) -> list[list[int]]:
    # reads all matrices from the file
    matrices = []
    with open(matrix_file_name, "r") as matrix_data_file:
        lines = matrix_data_file.readlines()
        i = 1
        row_column_count = None
        # parses all matrices
        while i < len(lines):
            line = lines[i].replace("\n", "")
            if "," not in line:
                row_column_count = int(line)
                i += 1
                matrices.append([])
                continue

            row_elements = list(map(int, line.split(",")))
            if len(row_elements) != row_column_count:
                print("Invalid matrix")
                exit(1)
            matrices[-1].append(row_elements)
            i += 1

    return matrices


def minor(matrix: list[list[int]], row_i: int, col_i: int) -> float | int | list[list[int]]:
    # calculates minor of the matrix
    # when the matrix is 2x2, then the minor is returned as a number instead of a 1x1 matrix
    minor_matrix = []
    if len(matrix) == 2:
        return matrix[row_i - 1][col_i - 1]
    for row in range(len(matrix)):
        if row == row_i:
            continue
        _row = []
        for col in range(len(matrix[0])):
            if col != col_i:
                _row.append(matrix[row][col])
        minor_matrix.append(_row)
    return minor_matrix


def cofactor(matrix: list[list[int]], row_i: int, col_i: int) -> float:
    minor_matrix = minor(matrix, row_i, col_i)
    return ((-1) ** (row_i + col_i)) * determinent(minor_matrix)


def cofactor_matrix(matrix: list[list[int]]):
    m_cofactor = []
    for row_i in range(len(matrix)):
        row = [cofactor(matrix, row_i, col_index)
               for col_index in range(len([matrix[0]]))]
        m_cofactor.append(row)
    return m_cofactor


def determinent(matrix: int | float | list[list[int]]):
    if type(matrix) is float or type(matrix) is int:
        return matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    determinent_number = 0
    for i in range(len(matrix[0])):
        determinent_number += (matrix[0][i]) * cofactor(matrix, 0, i)
    return determinent_number


def transpose(matrix: list[list[int]]):
    # loop over the columns
    # for each column, loop over the rows
    # and create a new matrix
    return [
        [
            matrix[row_index][col_index]
            for row_index in range(len(matrix))
        ]
        for col_index in range(len(matrix[0]))
    ]


matrices = read_matrix_data(
    "matrix_data.txt"
)


def find_inverse_and_stringify(i: int):
    matrix = matrices[i]
    det = determinent(matrix)
    adjoint_matrix = transpose(cofactor_matrix(matrix))
    output = [f"Inverse of Matrix {i+1}:\n"]
    for row_i in range(len(adjoint_matrix)):
        for col_i in range(len(adjoint_matrix[0])):
            output.append(f"{adjoint_matrix[row_i][col_i]/det:7.2f}")
        output[-1] = output[-1] + "\n"

    return "".join(output)


with open("output.txt", "w") as output_file:
    for matrix_i in range(len(matrices)):
        print(find_inverse_and_stringify(matrix_i))
