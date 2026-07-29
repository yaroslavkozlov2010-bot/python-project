from sympy import *

x = symbols('x')

eq = Eq(1*x**4 + 4*x**3 + 6*x**2 + 4*x + 1, 0)

answers = solve(eq)

print(answers)