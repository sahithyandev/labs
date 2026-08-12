import matplotlib.pyplot as plt

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = [
    "model1.txt",
    "model2.txt",
    "model3.txt",
]
################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    with open(file_name) as input_file:
        for line in input_file:
            speed.append(int(line.split()[1]))

################## YOUR CODE ENDS HERE. ########################################
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
    ################## YOUR CODE STARTS HERE. ######################################
    # Read the values using get_speed function and return the converted values as a list.
    speeds_from_file = get_speed(filename)
    return [round(5 * speed / 18, 4) for speed in speeds_from_file]

################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    # Acceleration list is initialized to zero.
    # i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    # Write the code to calculate the acceleration.
    for speed_index in range(1, len(speeds)):
        acceleration.append(
            (speeds[speed_index] - speeds[speed_index - 1]) * 10)

################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

max_acceleration_file = open("max_acceleration.txt", "w")

TIMES = [
    t / 1000 for t in range(0, 1001, 100)
]


def draw_line_graph(input_file: str):
    speeds = convert_kmph_to_ms(input_file)
    accelerations = get_acceleration(speeds)
    _max_acceleration = None
    file_index = input_file[-5]

    plt.plot(TIMES, accelerations,
             label=f'model_{file_index}')

    for acc_i in range(len(accelerations)):
        acc = accelerations[acc_i]
        if _max_acceleration is None or acc > _max_acceleration:
            _max_acceleration = acc

    max_acceleration_file.write(
        "model" + file_index + " " + str(round(_max_acceleration, 2)) + "\n")


draw_line_graph(MODEL_1_INPUT_FILE)
draw_line_graph(MODEL_2_INPUT_FILE)
draw_line_graph(MODEL_3_INPUT_FILE)
max_acceleration_file.close()
# Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable
# names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files

# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')

# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.show()
