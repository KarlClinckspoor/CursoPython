atomic_masses = {
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


def _find_next_counter(formula: str) -> (str, int):
    """
    Given a formula, finds the next counter and its value converted to int.
    Since values equal to 1 can be omitted, an empty string is interpreted as 1.
    Works by checking if the letters are uppercase, which means a new symbol started,
    which breaks the loop.

    Example: Fe2CO3 will return 2, since it starts at F and finds 2 before an uppercase letter.
    Example: CO3 will return 3.

    This is used mostly to find the next counter after a parenthesis.

    :param formula: Formula to search
    :return:
    """
    counter = ""
    for letter in formula:
        if letter.isupper():
            break
        if letter.isnumeric():
            counter += letter
    return counter, int(counter) if counter else 1


def _find_matching_parenthesis_idx(string: str, start_index: int) -> int:
    """
    Finds the index of a matching parenthesis in a string, given a start index.
    Iterates through the string and when the parenthesis "depth" is 0, returns
    the index.

    :param string: string with parentheses to find
    :param start_index: Index where the first parenthesis is.
    :return: the index of the matching parenthesis.
    """
    assert len(string) > 1, "Can't have strings of length 0 or 1!"
    assert (
        string[start_index] == "("
    ), "This should be called with the index of the first parenthesis!"
    depth = 1
    for i, letter in enumerate(string[start_index:]):
        if i == 0:
            continue

        if letter == "(":
            depth += 1
        elif letter == ")":
            depth -= 1

        if depth == 0:
            break
    else:
        raise Exception("The loop should't exit naturally!")
    idx = start_index + i
    if idx == 0:
        raise Exception("Couldn't find matching parenthesis!")
    assert string[idx] == ")"
    return idx


assert _find_matching_parenthesis_idx("abc(defghi(jklmno)pqr)", 3) == 21
assert _find_matching_parenthesis_idx("abc(defghi(jklmno)pqr)", 10) == 17

assert _find_matching_parenthesis_idx("abc(defg)hi(jklmno)p(qr)", 3) == 8
assert _find_matching_parenthesis_idx("abc(defg)hi(jklmno)p(qr)", 11) == 18
assert _find_matching_parenthesis_idx("abc(defg)hi(jklmno)p(qr)", 20) == 23


def _formula_simplifier(formula: str) -> list[str]:
    """
    Goes through a chemical formula and simplifies its contents to a list of strings,
    where each entry is an element. E.g., Fe2CO3 will return ['Fe', 'Fe', 'C', 'O', 'O', 'O']
    :param formula: a chemical formula with only symbols in the periodic table. If it contains
        a 'J', then it is considered invalid.
    :return: a list of strings where each element is repeated the number of times it appears in the formula
    """
    stopping_symbol = "J"
    assert len(formula) > 0, "Can't have an empty formula!"
    assert stopping_symbol not in formula, f"The symbol {stopping_symbol} is forbidden!"
    formula += stopping_symbol  # Convenient stopping point
    elements = []

    current_symbol = ""
    current_multiplier = ""
    i = 0
    while True:
        if i >= len(formula):
            break

        letter = formula[i]
        i += 1

        # If we get a parenthesis, recursive call this function with only the parenthesis interior
        if letter == "(":
            matching_parenthesis_i = _find_matching_parenthesis_idx(formula, i - 1)
            inner_elements = _formula_simplifier(formula[i:matching_parenthesis_i])
            inner_multiplier_str, inner_multiplier = _find_next_counter(
                formula[matching_parenthesis_i + 1 :]
            )
            elements.extend(inner_elements * inner_multiplier)
            # Set i to after the possible counter of parenthesis
            i = matching_parenthesis_i + 1 + len(inner_multiplier_str)
            continue

        # First loop iteration, to start
        if current_symbol == "":
            current_symbol = letter
            continue
        # Last loop, finalizing symbol
        if letter == stopping_symbol:  # Reached end, finalizes last symbol in storage
            current_multiplier = 1 if current_multiplier == "" else int(current_multiplier)
            temp = [current_symbol] * current_multiplier
            elements.extend(temp)
            break

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

    return elements


def molar_mass_calculator(formula: str, atomic_masses: dict[str, float]) -> float:
    """
    Given a chemical formula containing the elements present in the dict atomic_masses,
    gives the sum of the atomic masses of all elements.
    :param formula: a string with the chemical formula, e.g., 'CH3COOH', 'Fe(C5H5)2'
    :param atomic_masses: a dict with entries like atom symbol: mass, e.g., 'He': 4.0026.
    :return: a float with the sum of all elements
    """
    elements = _formula_simplifier(formula)
    return sum(atomic_masses[i] for i in elements)


assert abs(molar_mass_calculator("Fe(HCO3)2", atomic_masses) - 177.88) < 1e-2
assert abs(molar_mass_calculator("Fe((HCO3))2", atomic_masses) - 177.88) < 1e-2
assert abs(molar_mass_calculator("Fe2((HCO3))4", atomic_masses) - 177.88 * 2) < 1e-2
assert abs(molar_mass_calculator("CH3COOH", atomic_masses) - 60.052) < 1e-2
assert abs(molar_mass_calculator("Si(CH3)4", atomic_masses) - 88.225) < 1e-2
assert abs(molar_mass_calculator("Fe(C5H5)2", atomic_masses) - 186.04) < 1e-2
assert abs(molar_mass_calculator("RhH(CO)(P(C6H5)3)3", atomic_masses) - 918.8) < 1e-2
