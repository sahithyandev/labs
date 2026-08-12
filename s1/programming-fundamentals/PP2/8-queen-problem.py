chess_board = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
]
# chess board
# cell states
# space - normal cell
# q - queen
# x - not possible

queen_positions = ["a1", "b7", "c4", "e8", "f2", "h3"]


def convert_column_to_number(column):
    return ord(column) - 97


def convert_row_to_number(row):
    return int(row) - 1


def convert_coordinates_to_string(row_index, col_index):
    return chr(col_index+97) + str(row_index + 1)


def mark_queen_position(position):
    col = convert_column_to_number(position[0])
    row = convert_row_to_number(position[1])

    #  mark the column
    for row_index in range(8):
        chess_board[row_index][col] = "x"

    # mark the row
    for column_index in range(8):
        chess_board[row][column_index] = "x"

    # main diagonal
    start_offset = -1 * min(col, row)
    max_offset = (7 - max(col, row))

    for offset in range(start_offset, max_offset + 1):
        print(
            f"MAIN diagonal {convert_coordinates_to_string(row+offset, col+offset)}")
        chess_board[row + offset][col+offset] = "x"

    # secondary diagonal
    start_offset = -1 * min(col, 7-row)
    max_offset = 7 - max(col, 7 - row)

    for offset in range(start_offset, max_offset + 1):
        print(
            f"SECONDARY diagonal {convert_coordinates_to_string(row-offset, col+offset)}")
        chess_board[row - offset][col+offset] = "x"

    chess_board[row][col] = "q"


for pos in queen_positions:
    mark_queen_position(pos)
    for line in chess_board:
        print("".join(line))
    input()

for row in range(8):
    for col in range(8):
        cell = chess_board[row][col]
        if cell == " ":
            print("REMAINING", convert_coordinates_to_string(row, col))
