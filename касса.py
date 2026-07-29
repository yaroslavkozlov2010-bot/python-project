from datetime import datetime
import os

# Сохраняем заказ в файл
def writeFile_save_order(menu, shawarmas, price):
    with open('orders.txt', 'a', encoding='utf-8') as file:
        file.write(f'--- Заказ ---\n')
        for item in shawarmas:
            file.write(f'- {item} {menu[item]} руб.\n')
        file.write(f'Итого: {price} руб.\n')
        file.write(f'Время: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
        file.write('-' * 50 + '\n')  # Пустая строка между заказами

    print(f"Файл был сохранен по этому пути: {os.path.abspath('orders.txt')}")

# ОСНОВА
menu = {
    'смоленский парень': 300,
    'брат из брянска': 300,
    'классика с курицей': 280,
    'Двойное мясо': 420,
    'острая с халапеньо': 340,
    'с сыром и грибами': 370,
    'вегетарианская': 310,
    'люкс с мраморной говядиной': 450,
    'с картошкой фри внутри': 330,
    'барбекю с беконом': 390,
    'домашняя': 350,
    'с мясом ягнёнка': 440
}

shawarmas = []
price = 0

while input('Введи 0, чтобы закончить. Чтобы начать/продолжить, введи Enter: ') != '0':

    print('Меню:')
    for shawarma in menu:
        print(shawarma)
    print(' ')

    shawarma = input('Введи название шаурмы: ').lower()

    # Показывает шаурму и цену этой шаурмы. Если ее нет, то начинает цикл заново
    if shawarma in menu:
        print(f'{shawarma} - {menu[shawarma]} руб')
    else:
        print('Такой нет в меню')
        continue

    add_shawarma = input('Добавить шаурму? (да/нет): ').lower()
    if add_shawarma == 'да':
        shawarmas.append(shawarma)
        price += menu[shawarma]

    add_pork = input('Добавать свинину? (да/нет): ').lower()    
    if add_pork == 'да':
        price += 10 # прибавляет 10 рублей, если покупатель выбрал свинину

# Финальный чек
print('\n--- Ваш заказ ---')
for item in shawarmas:
    print(f'- {item} {menu[item]} руб.')
print(f'Итого: {price} руб.')

writeFile_save_order(menu, shawarmas, price)

input()
