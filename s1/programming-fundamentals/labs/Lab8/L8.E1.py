from math import pi, sqrt, atan, degrees


# Parse the input into a dictionary
def parse_input_line(line: str):
    segments = line.split()
    # ^ type R L C V f
    return {
        "type": segments[0],
        "r": int(segments[1]),
        "l": int(segments[2]) * pow(10, -3),
        # ^ because input is in millihentries
        "c": int(segments[3]) * pow(10, -6),
        # ^ because input is in microfarads
        "v": int(segments[4]),
        "f": int(segments[5])
    }


# Calculate z_total and phi of a series circuit
def analyseSeriesCircuit(circuit, z_l, z_c):
    return {
        "z_total": sqrt(circuit["r"] ** 2 + (z_l-z_c) ** 2),
        "phi": degrees(atan((z_l - z_c) / circuit["r"]))
    }


# Calculate z_total and phi of a parallel circuit
def analyseParallelCircuit(circuit, z_l, z_c):
    return {
        "z_total": 1 / sqrt(1 / (circuit["r"] ** 2) + (1/z_l-1/z_c) ** 2),
        "phi": degrees(atan((1/z_l - 1/z_c) * circuit["r"]))
    }


# Analyse and prints the information of the circuit in the required format
def analyse_and_print(circuit):
    # common calculations (for series and parallel) can be done here
    omega = 2 * pi * circuit["f"]
    z_l = omega * circuit["l"]
    z_c = 1 / (omega * circuit["c"])

    analysed_results =\
        analyseSeriesCircuit(circuit, z_l, z_c) if circuit["type"] == "series" \
        else analyseParallelCircuit(circuit, z_l, z_c)

    current = circuit["v"] / analysed_results["z_total"]
    print(circuit["type"], round(z_l, 1), round(z_c, 1), round(analysed_results["z_total"], 1),
          round(current, 1), round(analysed_results["phi"], 1))


input_file_name = input()

with open(input_file_name, "r") as input_file:
    line = None
    while True:
        line = input_file.readline()
        if line == "":
            break
        analyse_and_print(parse_input_line(line))
