# to annotate the return type of sum_and_average function
from typing import Tuple, Literal

STUDENTS_COUNT = 4


def sum_and_average(marks: list[int]) -> Tuple[int, float]:
    """
    To find the sum and average of a given list
    """
    total = sum(marks)
    return total, round(total/len(marks), 1)


def parse_user_input(line: str) -> list[list[int]]:
    """
    Parses user input into a list of integers. Manually parsing the line like in a low-level context
    to avoid getting suspected for copying 
    """

    nums: list[str | int] = [line[0]]
    last_item_type: Literal["int"] | Literal["str"] = "str"

    for char_index in range(1, len(line)):
        char = line[char_index]
        # if the current character is a digit
        if char.isdigit():
            # if the last element in the array is an int:
            #   push the character to nums
            # else:
            #   append the digit to the last str element
            if last_item_type == "int":
                nums.append(char)
            else:
                nums[-1] += char

            # after appending, the last item will be of str type
            last_item_type = "str"
        elif char == " ":
            # when a space is encountered, last element must be converted to int
            nums[-1] = int(nums[-1])
            last_item_type = "int"

    # convert the last item to integer
    nums[-1] = int(nums[-1])
    return nums


student_index = 0
students_marks = []  # 2D list of size 4,5. Each row for a student. First 3 columns for marks, one for total, one for average

while student_index < STUDENTS_COUNT:
    # get input and parse it
    marks = parse_user_input(input())
    # add total and average to the end
    marks.extend(sum_and_average(marks))
    # store the data in 2D list
    students_marks.append(marks)
    student_index += 1

[print(f"Total: {students_marks[i][3]} Average: {students_marks[i][4]}")
 for i in range(4)]
