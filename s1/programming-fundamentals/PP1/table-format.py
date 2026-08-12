row_count = int(input())
rows = [
]
column_headings = ["Name", "Grade"]
column_sizes = [2 + len(column_headings[0]), 2 + len(column_headings[1])]


def convert_marks_to_grade(marks: int):
    if marks >= 81:
        return "A"
    if marks >= 61:
        return "B"
    if marks >= 41:
        return "C"
    if marks >= 21:
        return "D"
    return "F"


for i in range(row_count):
    current_row = input().split()
    rows.append([current_row[0], convert_marks_to_grade(int(current_row[1]))])
    current_row = rows[i]
    for j in range(len(current_row)):
        required_length = len(str(current_row[j])) + 2
        if required_length > column_sizes[j]:
            column_sizes[j] = required_length


def add_padding_to_cell(content: str, required_length: int):
    return f" {content}{' ' * (required_length - 1 - len(str(content)))}"


row_divider = f"+{'-' * column_sizes[0]}+{'-'*column_sizes[1]}+"

# display table
print(row_divider)
print(
    f"|{add_padding_to_cell(column_headings[0], column_sizes[0])}|{add_padding_to_cell(column_headings[1], column_sizes[1])}|")
print(row_divider)
for row in rows:
    print(
        f"|{add_padding_to_cell(row[0], column_sizes[0])}|{add_padding_to_cell(row[1],column_sizes[1])}|")
print(row_divider)
