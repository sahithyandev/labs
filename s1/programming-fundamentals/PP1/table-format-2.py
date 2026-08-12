students = [
    ["Name", "Grade"],
    ["lasdjflaskjdfl", "A"],
    ["ksdjflaskd", "lB"],
    ["kjsldf", "C"],
]

# widths required for each column
column_widths = [
    0,
    0
]

for col_index in range(len(students[0])):
    for row_index in range(len(students)):
        x = students[row_index][col_index]
        required_length = len(x)
        if required_length > column_widths[col_index]:
            column_widths[col_index] = required_length

row_divider = "+" + "-" * \
    (column_widths[0] + 3) + "+" + "-" * (column_widths[1] + 3) + "+"

# to print the table
print(row_divider)

for row_index in range(len(students)):
    if row_index == 1:
        print(row_divider)
    column_1_width = students[row_index][0]
    spaces_count_for_column_1 = column_widths[0] - len(column_1_width)

    column_2_width = students[row_index][1]
    spaces_count_for_column_2 = column_widths[1] - len(column_2_width)

    print("|",
          students[row_index][0],
          " " * spaces_count_for_column_1,
          "|",
          students[row_index][1],
          " " * spaces_count_for_column_2,
          "|")

print(row_divider)
