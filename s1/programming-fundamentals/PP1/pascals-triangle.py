n = 7
triangle = [
    [1],
    [1, 1],
    [1, 2, 1]
]
max_single_length = 1

while len(triangle) < n:
    _row = [1]
    previous_row = triangle[len(triangle) - 1]
    for element in range(len(previous_row) - 1):
        up_left = previous_row[element]
        up_right = previous_row[element + 1]
        current = up_left + up_right
        if max_single_length < len(str(current)):
            max_single_length = len(str(current))
        _row.append(current)

    _row.append(1)
    triangle.append(_row)


def required_length(elements: list[int]):
    max_length = 0
    # len(elements)

    for element in elements:
        max_length += len(str(element)) + 1

    return int(max_length)


max_length = required_length(triangle[len(triangle) - 1])
for row_index in range(len(triangle)):
    row = triangle[row_index]
    print(" " * int(max_length - required_length(row)), end="")
    for element in row:
        if row_index % 2 == 0:
            print(element, end=" " * 4)
        else:
            print(str(element).center(max_single_length), end=" "*3)
    print()
