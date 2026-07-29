find = input('Искать модуль вектора или площадь/объем? (1 - модуль, 2 - площадь/объем): ')

def module_2d(x, y):
    return (x**2 + y**2)**(1/2)

def module_3d(x, y, z):
    return (x**2 + y**2 + z**2)**(1/2)

def module_4d(x, y, z, w):
    return (x**2 + y**2 + z**2 + w**2)**(1/2)

if find == '1':
    # Поиск модулей вектора в разных пространствах
    dimension = input('В каком пространстве будешь искать модуль вектора? (2D/3D/4D): ').lower()

    if dimension == '2d':
        print('Поиск модуля вектора в 2D пространстве')

        x = int(input('Введи первое число: '))
        y = int(input('Введи второе число: '))

        dimension_2d = module_2d(x, y)
        print(dimension_2d)

    elif dimension == '3d':
        print('Поиск модуля вектора в 3D пространстве')

        x = int(input('Введи первое число: '))
        y = int(input('Введи второе число: '))
        z = int(input('Введи третье число: '))

        dimension_3d = module_3d(x, y, z)
        print(dimension_3d)
        
    elif dimension == '4d':
        print('Поиск модуля вектора в 4D пространстве')

        x = int(input('Введи первое число: '))
        y = int(input('Введи второе число: '))
        z = int(input('Введи третье число: '))
        w = int(input('Введи четвертое число: '))

        dimension_4d = module_4d(x, y, z, w)
        print(dimension_4d)

elif find == '2':
    # Нахождение площади и объема в разных пространствах
    area = input('В каком пространстве будешь искать? (2D/3D/4D): ').lower()

    if area == '2d':

        a = int(input('Введи первое число: '))
        b = int(input('Введи второе число: '))

        print(a * b)

    elif area == '3d':

        a = int(input('Введи первое число: '))
        b = int(input('Введи второе число: '))
        c = int(input('Введи третье число: '))

        print(a * b * c)

    elif area == '4d':

        a = int(input('Введи первое число: '))
        b = int(input('Введи второе число: '))
        c = int(input('Введи третье число: '))
        d = int(input('Введи четвертое число: '))

        print(a * b * c * d)

end = input()