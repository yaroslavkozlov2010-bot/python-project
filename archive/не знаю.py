while input('Чтобы начать работу, нажми Enter. Напиши 0, чтобы выключить программу: ') != '0':
    while True:
        try:
            numbers = input('Введи числа через пробел: ').split()

            if not numbers:
                print('Вы ничего не ввели. Пожалуйста, введите числа')
                continue

            numbers = list(map(int, numbers))
            
            break
        except ValueError:
            print('Нужно ввести числа')

    print(f'Обычный список: {numbers}\n')

    for number in range(len(numbers)):
        if numbers[number] % 2 == 0:
            numbers[number] **= 2

    print(f'Список квадратов для четных чисел: {numbers}\n')

print('\nПрограмма завершена')