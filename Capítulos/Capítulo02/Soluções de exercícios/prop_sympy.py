import sympy as sp

(
    a,
    b,
    c,
    delta_a,
    delta_b,
    delta_c,
) = sp.symbols("a b c delta_a delta_b delta_c")

f = a + b / c

delta_f = sp.sqrt(
    sp.Derivative(f, a) ** 2 * delta_a**2
    + sp.Derivative(f, b) ** 2 * delta_b**2
    + sp.Derivative(f, c) ** 2 * delta_c**2
)

sub_dict = {a: 5, b: 3, c: 2, delta_a: 0.1, delta_b: 0.2, delta_c: 0.5}
f_eval = f.subs(sub_dict)
delta_f_eval = delta_f.subs(sub_dict).doit()

print(f)
print(f_eval)
print(delta_f_eval)
