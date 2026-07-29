import random as rnd
import time as t

names = []


print('Список отсортируется сам.')

add_name = input('Добавь фамилию и имя ученика (чтобы завершить, нажмите Enter): ')

while add_name != '':
    names.append(add_name)
    add_name = input('Добавь фамилию и имя ученика (чтобы завершить, нажмите Enter): ')
names.sort()

# Вывод списка людей и вывод количества тех, кто идет на сдачу экзамена
result = ', '.join(names)
print(f'Отсортерованный список: {result}. Подсчет: {len(names)}')

# Проверка на ошибки
while True:
    try:
        player = int(input('Выбери количество тех, кто идет в аудиторию на устную часть экзамена по английсокму языку: '))

        if player > len(names):
            print(f'Ошибка: участников не может быть больше {len(names)}.')
            continue # Возвращаемся в начало цикла

        break # Если всё верно, выходим из цикла
    except ValueError:
        print('Ошибка: нужно ввести целое число.')


# Вывод людей, которые идут на сдачу устного экзамена
print('Подожди 3 секунды...')
t.sleep(3)

players = ', '.join(rnd.sample(names, k=player))

print(f'Участники: {players}')

end = input()
