from sympy import *

# Объявляем переменную
x = symbols('x')

# Решаем неравенство относительно x (или любой другой переменной, которую записали)
solution = reduce_inequalities(x**2 - 4 > 0, x)
print(solution)

solution_3 = reduce_inequalities(453 + 2*x < 4, x)
print(solution_3)