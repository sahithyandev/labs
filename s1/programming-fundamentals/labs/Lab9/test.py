def get_atom_count(atoms, atom_name):
    if atom_name not in atoms:
        return 0

    atom_name_index = atoms.index(atom_name)
    return atoms[atom_name_index + 1]


print(get_atom_count(["S", 4, "O", 3, "Cl", 6], "Cl"))
