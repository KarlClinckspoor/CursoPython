def convert_distance(value, from_, to):
    """Converts "value" from the unit "from_" to the unit "to" first by converting it to meters, then
    converting meters to the desired unit"""

    factor_to_m = {
        "m": 1,
        "dm": 1 / 10,
        "cm": 1 / 100,
        "mm": 1 / 1000,
        "km": 1e3,
        "inch": 1 / 39.3700787,
        "in": 1 / 39.3700787,
        "ft": 1 / 3.2808399,
        "feet": 1 / 3.2808399,
        "foot": 1 / 3.2808399,
        "mile": 1609.344,
    }
    factor_from_m = {key: 1 / val for key, val in factor_to_m.items()}

    if from_ not in factor_to_m.keys():
        raise NotImplementedError(f"Unit {from_} not implemented yet!")
    if to not in factor_to_m.keys():
        raise NotImplementedError(f"Unit {to} not implemented yet!")

    value_in_m = factor_to_m[from_] * value
    value_in_to = factor_from_m[to] * value_in_m
    return value_in_to


def test_atol(value, reference, atol=1e-5):
    return abs(value - reference) < atol


assert test_atol(convert_unit(1, "m", "cm"), 100)
assert test_atol(convert_unit(1, "km", "m"), 1000)
assert test_atol(convert_unit(12, "inch", "feet"), 1)
assert test_atol(convert_unit(12, "feet", "inch"), 12 * 12)
assert test_atol(convert_unit(1, "mile", "feet"), 5280)

# Para testar que uma exceção é levantada, precisamos do pacote unittest.
import unittest


class Test(unittest.TestCase):
    def test_nonexistant_unit(self):
        with self.assertRaises(NotImplementedError):
            test_atol(convert_distance(1, "marathon", "km"), 42.194988)


t = Test()
t.test_nonexistant_unit()
