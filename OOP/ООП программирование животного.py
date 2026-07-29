class Animal():
    # конструктор класса
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    # метод Голос
    def make_voice(self):
        print(self.voice)

# создание экземпляра класса my_animal
my_animal = input('Какое животное будем программировать?\n>>> ')
voice_animal = input('Как животное отвечает на команду "Голос"?\n>>> ')
animal = Animal(my_animal, voice_animal)

# вывод сообщения о создании объекта
print(f'Объект {animal.name} создан.')

# запрос разрешения дать команду "Голос" и реакция на ответ
if input('Подать команду "Голос" (да/нет)?\n>>> ') == 'да':
    animal.make_voice()

end = input('...')
