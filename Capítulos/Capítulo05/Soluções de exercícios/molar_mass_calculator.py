massas_atômicas = {
    "H": 1.0080,
    "He": 4.0026,
    "Li": 6.94,
    "Be": 9.0122,
    "B": 10.81,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.06,
    "Cl": 35.45,
    "Ar": 39.95,
    "K": 39.098,
    "Ca": 40.078,
    "Sc": 44.956,
    "Ti": 47.867,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.630,
    "As": 74.922,
    "Se": 78.971,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.468,
    "Sr": 87.62,
    "Y": 88.906,
    "Zr": 91.224,
    "Nb": 92.906,
    "Mo": 95.95,
    "Ru": 101.07,
    "Rh": 102.91,
    "Pd": 106.42,
    "Ag": 107.87,
    "Cd": 112.41,
    "In": 114.82,
    "Sn": 118.71,
    "Sb": 121.76,
    "Te": 127.60,
    "I": 126.90,
    "Xe": 131.29,
    "Cs": 132.91,
    "Ba": 137.33,
    "La": 138.91,
    "Ce": 140.12,
    "Pr": 140.91,
    "Nd": 144.24,
    "Sm": 150.36,
    "Eu": 151.96,
    "Gd": 157.25,
    "Tb": 158.93,
    "Dy": 162.50,
    "Ho": 164.93,
    "Er": 167.26,
    "Tm": 168.93,
    "Yb": 173.05,
    "Lu": 174.97,
    "Hf": 178.49,
    "Ta": 180.95,
    "W": 183.84,
    "Re": 186.21,
    "Os": 190.23,
    "Ir": 192.22,
    "Pt": 195.08,
    "Au": 196.97,
    "Hg": 200.59,
    "Tl": 204.38,
    "Pb": 207.2,
    "Bi": 208.98,
}


def molar_mass_calculator(formula, atomic_mass_table):
    assert ("(" not in formula) or (")" not in formula), "Can't have parentheses!"
    assert len(formula) > 0, "Can't have an empty formula!"
    assert "J" not in formula, "There's no J in any element!"
    formula += "J"  # Workaround to properly process the last item
    elements = []

    current_symbol = ""
    current_multiplier = ""
    for letter in formula:
        # First loop iteration, to start
        if current_symbol == "":
            current_symbol = letter
            continue
        # Last loop, finalizing symbol
        if letter == "J":  # Reached end, finalizes the last symbol
            current_multiplier = 1 if current_multiplier == "" else int(current_multiplier)
            temp = [current_symbol] * current_multiplier
            elements.extend(temp)
            continue

        # Intermediate loops
        if letter.isupper():  # Starting a new symbol
            # Store the previous one
            current_multiplier = 1 if current_multiplier == "" else int(current_multiplier)
            temp = [current_symbol] * current_multiplier
            elements.extend(temp)
            # Start a new symbol
            current_multiplier = ""
            current_symbol = letter
            continue
        if letter.islower():  # Continuing symbol
            current_symbol += letter
            continue
        if letter.isnumeric():  # Reached number
            current_multiplier += letter
            continue

    masses = [atomic_mass_table[i] for i in elements]
    return sum(masses)


assert abs(molar_mass_calculator("Fe2O3", massas_atômicas) - 159.69) < 1e-2
assert abs(molar_mass_calculator("C12H22O11", massas_atômicas) - 342.30) < 1e-2
