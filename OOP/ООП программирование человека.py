class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_age(self):
        print(f'Мой возраст: {self.age}')
    
    def say_phrase(self):
        print('Человек рожден, чтобы оставить свой след в этом мире.')

human_name = input('Вписать имя человека: ')
human_age = int(input('Вписать возраст человека: '))
human = Human(human_name, human_age)

print(f'Объект {human_name} создан.')

if input(f'Сказать возраст человека по имени {human_name} (да/нет)?\n>>> ') == 'да':
    human.say_age()


class Warrior(Human):
    def __init__(self, name, age, level): 
        super().__init__(name, age) # Добавление методов из родительского класса (супер класса)
        self.level = level # Присваивание уникального метода

    def say_level(self):
        print(f'Я, {self.name}, стал воином в {self.age}, и мой  уровень - {self.level}')
    
    def say_phrase(self):
        print('Я воин, и я рожден, чтобы убивать и захватывать!')

warrior_level = input('Введи уровень воина: ')
warrior = Warrior(human_name, human_age, warrior_level)

if input(f'Разврешить воину {human_name} сказать свой уровень?\n>>> ') == 'да':
    warrior.say_level()

people = [human, warrior]

for person in people:
    person.say_phrase()

end = input()
