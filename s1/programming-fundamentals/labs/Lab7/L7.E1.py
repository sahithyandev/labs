
# I am using typing module to annotate Dict and Any types
# I like to include type annotations so that I can use autocompletition in my editor
from typing import Any, Dict


def maximum_deflection(load: float, length: float, youngs_modulus: float, moment_of_inertia: float):
    return load * pow(length, 3) / (48 * youngs_modulus * moment_of_inertia)


def maximum_bending_stress(load: float, length: float, moment_of_inertia: float):
    return load * length / (4 * moment_of_inertia)


def parse_beam_data(index: int, beam_data: str):
    parts = [float(part) for part in beam_data.split()]
    # structure of parts will be [length, youngs modulus, moment of inertia, load]

    return {
        "index": index,
        "length": parts[0],
        "youngs_modulus": parts[1] * pow(10, 9),  # because gigapascal
        "moment_of_inertia": parts[2],
        "load": parts[3] * pow(10, 3),  # because kilonewtons
    }


def stringify_beam_details(beam_details: Dict[str, Any]):

    # %1.6f is used to format the floating point output to 1 decimal places before and 6 decimal places after the dot
    # Similarily %9.2f is used to format the floating point output to 9 decimal places before and 2 decimal places after the dot
    return "Beam %d: Length: %.1f m, Max Deflection: %1.6f m, Max Bending Stress: %9.2f Pa" % (
        beam_details["index"],
        beam_details["length"],
        maximum_deflection(
            beam_details["load"],
            beam_details["length"],
            beam_details["youngs_modulus"],
            beam_details["moment_of_inertia"]
        ),
        maximum_bending_stress(
            beam_details["load"],
            beam_details["length"],
            beam_details["moment_of_inertia"]
        )
    )


# with keyword is to avoid calling the close method manually
with open(input()) as beam_data_file:
    last_processed_line_count = 1
    while True:
        line = beam_data_file.readline()
        # After all the lines are read, readline method will return empty string
        if line == "":
            break
        parsed_beam_data = parse_beam_data(last_processed_line_count, line)
        print(stringify_beam_details(parsed_beam_data))
        last_processed_line_count += 1
