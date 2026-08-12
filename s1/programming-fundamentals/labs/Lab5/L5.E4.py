# matrix as a 2 dimensional list
matrix = []
count_count = 0

# start with a while loop that looks like an infinte loop
# we will break out when the user input is -1
while True:
    user_input = input("")

    # stop looping when the input is -1
    if user_input == "-1":
        break

    row = []
    # loop thorugh each item in the user input
    for element in user_input.split(" "):
        # handle the error, just in case, if the user has provided an invalid input
        try:
            parsed = float(element)
            if "." not in element:
                parsed = int(element)
            row.append(parsed)
        except:
            print("Error")
            exit(0)

    # if column_count is not initialized
    if count_count == 0:
        # we set it to length of the row
        count_count = len(row)
    # otherwise, we check if its equal to length of the row
    elif len(row) != count_count:
        # if not, it's an invalid matrix
        print("Invalid Matrix")
        exit(0)

    matrix.append(row)

print(matrix)

# go through each column
# select 1 column and then go through each row
for columnIndex in range(0, count_count):
    for rowIndex in range(0, len(matrix)):
        # we are using end="" to avoid ending with a newline character
        # otherwise each print statement will print on a new line
        print(matrix[rowIndex][columnIndex], end=" ")
    print()  # to insert a newline character
