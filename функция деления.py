def division(a, b, mode):
    if mode == '1':
        return a / b
    elif mode == '2':
        return a // b
    else:
        return None

print('\nВНИМАНИЕ: началась внезапная программа деления:')

while True:
    try:
        mode = input('Введи цифру:\n1. Обычное деление\n2. Деление без остатка\n>>> ')
        a = int(input('Введи первое число (делимое): '))
        b = int(input('Введи второе число (делитель): '))

        result = division(a, b, mode)
        
        if result is not None:
            print(f'Ответ: {result}')
            break

    except (ZeroDivisionError, ValueError): # Ловит исключения деления на ноль и неправильного ввода 
        print('\nЧто тебе в школе говорили? Делить на ноль нельзя.\nА еще, надо ввести туда число, если ты ввел ничего или букву.\nДавай по новой, непризнанный гений.\n')

input() # Нужно, чтобы терминал не закрылся сразу
