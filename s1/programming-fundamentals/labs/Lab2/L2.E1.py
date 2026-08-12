# use array instead of 3 different variables
# for ease of use
angles = []

# take 3 angles from user
for i in range(3):
    angles.append(int(input(f'Enter angle {i + 1}: ')))

# going to find the max angle and sum of angles
sumOfAngles = 0
maxAngle = 0

for theta in angles:
    # any angle cannot be negative
    if theta <= 0:
        print("Angles do not form a triangle")
        exit(1)
    sumOfAngles += theta
    # if sum of angles already exceed 180 we can exit early
    if sumOfAngles > 180:
        print("Angles do not form a triangle")
        exit(1)
    # check if current angle is greater than max angle
    # and update max angle accordingly
    if theta > maxAngle:
        maxAngle = theta

# if sum of angles isn't 180
# triangle cannot be formed
if sumOfAngles != 180:
    print("Angles do not form a triangle")
    exit(1)

# output based on the maximum angle
if maxAngle > 90:
    print("Obtuse angled")
    exit(0)
if maxAngle == 90:
    print("Right angled")
    exit(0)
if maxAngle < 90:
    print("Acute angled")
