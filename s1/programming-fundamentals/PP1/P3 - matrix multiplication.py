def input_matrix(expected_row_count=None):
    [row_count, col_count] = map(int, input("Enter row x column: ").split())
    if (expected_row_count is not None and row_count != expected_row_count):
        exit()

    matrix = []
    for i in range(row_count):
        row = input().split()
        if len(row) != col_count:
            exit()
        parsed_row = []
        for element in row:
            # handle the error, just in case, if the user has provided an invalid input
            try:
                parsed = float(element)
                if "." not in element:
                    parsed = int(element)
                parsed_row.append(parsed)
            except:
                print("Error")
                exit(0)
        matrix.append(parsed_row)
    return matrix


matrixA = input_matrix()
matrixB = input_matrix(expected_row_count=len(matrixA[0]))

matrixOutput = []

for i in range(len(matrixA)):
    l = []
    for j in range(len(matrixB[0])):
        l.append(0)
    matrixOutput.append(l)


for i in range(len(matrixA)):
    for j in range(len(matrixB[i])):
        for k in range(len(matrixA[i])):
            matrixOutput[i][j] += matrixA[i][k] * matrixB[k][j]

for row in matrixOutput:
    for element in row:
        print(element, end=" ")
    print()
