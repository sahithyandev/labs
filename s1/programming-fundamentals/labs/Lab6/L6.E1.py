# I am using this to annotate the Tupe return type
# I like to include type annotations
# so that I can use autocompletition in my editor
from typing import Tuple


def get_dimensions_for_matrix() -> Tuple[int, int]:
    """
    Includes error handling.
    """
    dimension_input = input("Enter the dimension: ").split(",")
    if len(dimension_input) != 2:
        print("Invalid input for the dimensions")
        exit(1)

    try:
        row_count = int(dimension_input[0])
        column_count = int(dimension_input[1])
    except:
        print("Invalid input for the dimensions")
        exit(1)

    return row_count, column_count


def parse_as_number(number: str):
    """
    Parses the input as int or float. Includes error handling.
    """
    try:
        parsed_as_float = float(number)
        parsed_as_int = int(number)
    except:
        print("Error")
        exit(1)

    if parsed_as_float == parsed_as_int:
        return parsed_as_int
    else:
        return parsed_as_float


def input_matrix(expected_dimension: Tuple[int, int], message: str = None) -> list[list[int]]:
    """
    expected_dimension = (row count, column count)    
    message parameter will be printed, if passed, before starting user input.
    """
    [row_count, column_count] = expected_dimension

    # print message if provided
    if message is not None:
        print(message)

    matrix = []
    for _ in range(row_count):
        row = input().split()

        # it's invalid when the column count doesn't match
        if len(row) != column_count:
            print("Invalid Matrix")
            exit(1)

        parsed_row = [parse_as_number(element) for element in row]
        matrix.append(parsed_row)

    return matrix


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    transposed = []
    # interchange looping order to
    # select a column and
    # loop over all rows
    for column_index in range(len(matrix[0])):
        _row = []  # to store the new row
        for row_index in range(len(matrix)):
            _row.append(matrix[row_index][column_index])

        transposed.append(_row)
    return transposed


def product(matrixA: list[list[int]], matrixB: list[list[int]]) -> list[list[int]]:
    matrixA_row_count = len(matrixA)
    matrixA_col_count = len(matrixA[0])
    matrixB_col_count = len(matrixB[0])

    output_matrix = []
    # loop through each row in matrix A
    for row_index in range(matrixA_row_count):
        _row = []
        # loop through each column in matrix B
        for col_index in range(matrixB_col_count):
            element = 0
            # loop through each element pairs
            for element_index in range(matrixA_col_count):
                element += matrixA[row_index][element_index] * \
                    matrixB[element_index][col_index]

            _row.append(element)
        output_matrix.append(_row)

    return output_matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


dimensions = get_dimensions_for_matrix()
matrixA = input_matrix(dimensions, "Enter Matrix A:")
matrixB = input_matrix(dimensions, "Enter Matrix B:")

print_matrix(product(matrixA, transpose(matrixB)))
