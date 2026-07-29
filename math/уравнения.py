#%% [markdown]
## Это новая ячейка


#%% [code]
from sympy import *

print('Обычное уравнение:')
# Объявляем переменную
x = symbols('x')

# Пишем уравнение
equation = Eq(x**2 + x + 1, 0)

# Находим корни
roots = solve(equation, x)
pprint(roots)

#%%
# Тригонометрическое уравнение
print('Тригонометрическое уравнение:')
equation_2 = Eq(sin(x), 0)

roots_2 = solve(equation_2, x)
pprint(roots_2)


#%%
# Система уранений
print('Система уранений:')
y = symbols('y') # Без x, потому что я объявлял его выше

# Записываем систему уравнений (пишется в виде списка уравнений)
system = [
    Eq(x + y, 5),
    Eq(x - y, 1)
]

# Находим корни
solution = solve(system, (x, y))
pprint(solution)

print(' ')

#%%
# Рациональное уравнение (так же, как и первое)
print('Рациональное уравнение:')
c = symbols('c')

rational = Eq((c*c*c)/(c+c+c), c)

root_c = solve(rational, c)
pprint(root_c)

#%%
# Задаем уравнение 1/x + 1/y = 17
equation = Eq(1/x + 1/y, 17)

# Решаем относительно x (чтобы получить y) или y (чтобы получить x)
y_solution = solve(equation, y)
x_solution = solve(equation, x) 

print("Выражение для y:")
pprint(y_solution)

print("Выражение для x:")
pprint(x_solution)

pprint(x_solution + y_solution)

#%% [code]
# Показательные уравнения
print('Показательные уравнения:')
eq = Eq(2**x + 5**4, 79)

answer = solve(eq, x)

pprint(answer)
