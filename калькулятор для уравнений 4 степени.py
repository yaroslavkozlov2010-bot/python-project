from sympy import *
from datetime import datetime
from time import sleep

def log_error(e):
    with open('error.txt', 'a', encoding='utf-8') as file:
        file.write(f'Ошибка: {e}\n')
        file.write(f'Время: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        file.write('-' * 50 + '\n')

def save_solution(eq, pretty_answers):
    with open('answers.txt', 'a', encoding='utf-8') as file:
        file.write('=' * 50 + '\n')
        file.write(f'Уравнение: {eq}\n')
        file.write(f'Ответ: {pretty_answers}\n')
        file.write(f'Время: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
        file.write('=' * 50 + '\n')
        file.write('\n')

def show_history():
    try:
        with open('answers.txt', 'r', encoding='utf-8') as file:
            content= file.read()
        print(content)
    except FileNotFoundError:
        print('Файл не создан. Повторите после решения')

# ОСНОВА
x = symbols('x')

while True:
    try:

        try:
            numbers = input('Введи коэффециенты через пробел: ').split()

            if not numbers:
                print('Ничего не было введено. Пожалуйста, введите числа или завершите работу программы')
                continue

            coefficient = list(map(float, numbers))

            equal = input('чему равно это уравнение: ')

            if not equal:
                print('По умолчанию будет 0')
                equal = 0

            equal = float(equal)

        except ValueError:
            print('Нужно ввести числа, а не буквы') 
            continue

        a, b, c, d, e = coefficient

        eq = Eq(a*x**4 + b*x**3 + c*x**2 + d*x + e, equal)

        answers = solve(eq, x)

        pretty_answers = []

        for answer in answers:
            pretty = answer.evalf(4)
            pretty_answers.append(pretty)
        
        print(f'Ответ: {pretty_answers}')

        sleep(10)
        break

    except ValueError:
        print(f'Ошибка! Нужно 5 коэффециентов, а не {len(coefficient)}\nПопробуй снова\n')

    except Exception as e:
        log_error(e)
        print(f'Неизвестная ошибка {e}')

save_solution(eq, pretty_answers)

show_history()