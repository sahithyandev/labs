INPUT_FILE_NAME = "contamination_analysis.txt"

# I like to use types in my code
from typing import Dict

# a function to count atoms in a chemical formula
# i am manually parsing the input instead of using regex
def count_atoms(chemical: str) -> Dict[str, int]:
    atoms = {}

    last_atom = ["", ""]  # [atom, count]
    for char in (chemical+"-"): # "-" is added to last so that my algorithm works correct
        if char == "-":
            # by default the count is 1
            count = 1
            # we use the count when it's non-empty
            if last_atom[1] != "":
                count = int(last_atom[1])


            if last_atom[0] in atoms:
                atoms[last_atom[0]] += count
            else:
                atoms[last_atom[0]] = count

            # after adding the last atom to the atoms dictionary, clear the last atom data
            last_atom[0] = ""
            last_atom[1] = ""
        # digits are concat-ed to the count
        # other characters are concat-ed to the atom name
        elif char.isalpha():
            last_atom[0] += char
        elif char.isdigit():
            last_atom[1] += char

    return atoms

# open the files and store the file handles in the list
groups = [open(f"Level_{i}.txt", "w") for i in range(5)]

# a function to check if the atoms in a dictionary is enough to the required numbers of atoms
# mutates the input atom details
def is_enough_atoms(atom_details: Dict[str, int], required: Dict[str, int]):
    for key in required:
        # surely a no if
        # key is not in the list
        # required number is greater than existing count
        if key not in atom_details or required[key] > atom_details[key]:
            return False

    for key in required:
        atom_details[key] -= required[key]
    return True

# categorizes chemicals into groups
# uses bitmask (with length 3) for that
def put_chemical_into_group(chemical_name, atom_count_details: Dict[str, int]):
    # 000 - for group 0
    # 001 - for group 1
    # 010 - for group 2
    # 100 - for group 3
    # anything else for group 4
    criteria_condition = 0

    if is_enough_atoms(atom_count_details, {"S": 1, "O": 4, "Na": 1}):
        criteria_condition = criteria_condition | 1

    if is_enough_atoms(atom_count_details, {"S": 1, "O": 3, "Mg": 1}):
        criteria_condition = criteria_condition | 2

    if is_enough_atoms(atom_count_details, {"O": 2, "Cl": 3}):
        criteria_condition = criteria_condition | 4
    chemical_name += "\n"

    if criteria_condition < 2: # it's either 0 or 1
        groups[criteria_condition].write(chemical_name)
    elif criteria_condition == 2:
        groups[2].write(chemical_name)
    elif criteria_condition == 4:
        groups[3].write(chemical_name)
    else:
        groups[4].write(chemical_name)

with open(INPUT_FILE_NAME) as chemical_file:
    for line in chemical_file:
        parts = line.replace("\n", "").split()
        atom_count = count_atoms(parts[1])
        put_chemical_into_group(parts[0], atom_count)

    # close all files at last
    for group in groups:
        group.close()
