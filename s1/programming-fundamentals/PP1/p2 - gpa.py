[subjects_count, row_count] = list(map(int, input().split()))
# [5, 4]

subjects_grades = input().split()
# ["A", "B", "B", "D", "C"]

subjects_weights = list(map(int, input().split()))
# [3, 2, 2, 1, 3]

grading_schema = {
    # "A": 4.0,
    # "B": 3.0,
    # "C": 2.0,
    # "D": 0.0
}

for _ in range(row_count):
    [grade, grade_point] = input().split()
    grading_schema[grade] = float(grade_point)

gpa = 0
for i in range(subjects_count):
    gpa += grading_schema[subjects_grades[i]] * subjects_weights[i]
gpa = round(gpa / sum(subjects_weights), 2)
print(f"{gpa}")

closest_grade = "A"
delta = abs(grading_schema[closest_grade] - gpa)
for i in grading_schema:
    _new_delta = abs(grading_schema[i] - gpa)
    if _new_delta < delta:
        delta = _new_delta
        closest_grade = i

print(closest_grade)
