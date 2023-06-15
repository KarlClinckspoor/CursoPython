import pint
ureg = pint.UnitRegistry(autoconvert_offset_to_baseunit = True)

n = (3.4 * ureg.g / (4 * ureg.g / ureg.mole))
R = 8.314472 * ureg.J / ureg.K / ureg.mole
T = ureg.Quantity(77, ureg.degF)
V = 35 * ureg.milliliters
p = n * R * T / V
p.to('bar')