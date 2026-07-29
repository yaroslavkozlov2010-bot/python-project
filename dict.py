titles = {
    'Гоголь': 'Мертвые души', 
    'Лев Толстой': 'Война и мир'
}

print(titles)
print(titles['Гоголь'])
print(titles['Лев Толстой'])
print(titles.keys())
print(titles.values())

# Программа предлагает пользователю добавить автора
add = input('Хотите кого-нибудь добавить (да/нет)?\n>>> ')
if add == 'да':
    # Спрашивает количество авторов  
    try:
        amount_name = int(input('Сколько?\n>>> '))

    except ValueError:
        print('Ошибка! Нужно ввести число, тупое ты животное. Но ладно, так уж и быть, добавлю 1-го автора')
        amount_name = 1

    for i in range(amount_name):
        # Спрашивает имя автора
        name = input('Кого добавить?\n>>> ')

        # Просит добавить произведение автора, затем добавляет новую пару
        title = input('Добавь его/ее произведение\n>>> ')
        titles[name] = title

# Вывод нового словаря, его ключей и значений
print('\nОбновленный словарь, ключи и значения:')
print(titles)
print(titles.keys())
print(titles.values())
