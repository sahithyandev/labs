students_initial = input().split()
moves = input().split()


students_final = students_initial[::]

for i in range(len(moves)):
    move_to_make = moves[i]
    direction = move_to_make[0]
    move_units = int(move_to_make[1:])
    if move_units == 0:
        continue

    student_index_in_final_list = students_final.index(students_initial[i])
    student_to_move = students_final.pop(student_index_in_final_list)
    new_index = student_index_in_final_list
    if direction == "L":
        new_index += move_units
    else:
        new_index -= move_units
    students_final.insert(new_index, student_to_move)

for student in students_initial:
    print(students_final.index(student) + 1, end=" ")
