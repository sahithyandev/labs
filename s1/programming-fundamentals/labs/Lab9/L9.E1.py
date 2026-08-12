import os
import matplotlib.pyplot as plt

input_file_name = "input.txt"

# Your code should be included here.
# Avoid using the print function in the code, as it may cause errors

# functions for basic equations
def parallel_resistance(r1, r2):
    return (r1 * r2) / (r1 + r2)


def calculate_v_out(v_in, r1, r2):
    return v_in * r2 / (r1+r2)

def calculate_v_new(v_in, r1, r2, rL):
    resultant_of_r2_and_rL = parallel_resistance(r2, rL)
    return v_in * (resultant_of_r2_and_rL) / (r1 + resultant_of_r2_and_rL)

output_file = open("output.txt","w")

with open(input_file_name, "r") as input_file:
    lines = input_file.readlines()
    first_line_parts = lines[0].replace("\n", "").split(", ")
    [v_in, expected_v_out] = list(map(int, first_line_parts[0:-1]))
    tolerance = float(first_line_parts[2])
    resistors = list(map(int, lines[1].split(", ")))

    n = len(resistors)

    # a tuple to store the minimal power pair
    minimal_resistor_pair = (None, None)  # (r1, r2)

    for r1_i in range(n):
        for r2_i in range(r1_i + 1, n): # uses r1_i + 1 to reduce the number of loops by half
            r1, r2 = resistors[r1_i], resistors[r2_i]
            v_out = calculate_v_out(v_in, r1, r2)
            delta_v = abs(v_out - expected_v_out)

            # we don't have to calculate the real power dissipation becuase
            # it is inversely proportional to r1+r2
            # when power dissispation is low, r1 + r2 will be high
            power_dissipation_inverse = r1 + r2

            if delta_v <= tolerance:
                if minimal_resistor_pair[0] is None or minimal_resistor_pair[1] + minimal_resistor_pair[0] < power_dissipation_inverse:
                    minimal_resistor_pair = (r1, r2)

            # check with the reversed pair
            v_out_reversed_pair = v_in - v_out
            delta_v_reversed = abs(v_out_reversed_pair - expected_v_out)

            if delta_v_reversed > tolerance:
                continue
            if minimal_resistor_pair[0] is None or minimal_resistor_pair[1] + minimal_resistor_pair[0] < power_dissipation_inverse:
                minimal_resistor_pair = (r2, r1)

    r1 = minimal_resistor_pair[0]
    r2 = minimal_resistor_pair[1]
    output_file.write(f"{r1}, {r2}")
    output_file.close()
    xvalues = []
    yvalues = []

    for i in range(100):
        rL = (i + 1) * 10
        xvalues.append(rL)
        yvalues.append(calculate_v_new(v_in, r1, r2, rL))

    plt.plot(xvalues, yvalues)

    # Adding labels and title
    plt.xlabel('Resistance (ohms)')
    plt.ylabel('Voltage (V)')
    plt.title('Voltage vs Resistance')
    plt.show()
