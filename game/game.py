# Код от DeepSeek
from random import *

class Hero():
    def __init__(self, name, health, armor, power, new):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.new = new

    def print_info(self):
        print('Урон:', self.power)
        print('Здоровье:', self.health)
        print('Броня:', self.armor)

    def check_alive(self):
        if self.health > 0:
            print('Уровень здоровья:', self.health)
            print('Уровень брони:', self.armor)
        else:
            print(self.name, 'мертв')

    def strike(self, enemy):
        print('-> Удар! ')
        print(self.name, 'атакует', enemy.name, '\n')  # убрал self.weapon
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name, 'покачнулся(-ась).')
        print('Класс брони упал до', enemy.armor)
        print('Уровень здоровья снизился до', enemy.health, '\n')
        
class Warrior(Hero): 
    def hello(self):
        self.new = False
        print('НОВЫЙ ГЕРОЙ! Из глубины леса появляется искусный воин', self.name)
        self.print_info()  # вызываем метод экземпляра

    def attack(self, enemy):
        print(self.name, 'беспощадно нападает на', enemy.name)
        self.strike(enemy)  # вызываем метод экземпляра
        print('Уровень здоровья:', self.health)
        print('Уровень брони:', self.armor)

class Dragon(Hero):
    def hello(self):
        self.new = False
        print('НОВЫЙ ГЕРОЙ! С неба спускается свирепый дракон', self.name)
        self.print_info()  # вызываем метод экземпляра

    def attack(self, enemy):
        print(self.name, 'беспощадно нападает на', enemy.name)
        self.strike(enemy)  # вызываем метод экземпляра
        print('Уровень здоровья:', self.health)
        print('Уровень брони:', self.armor)

knight = Warrior('Ричард', 50, 25, 20, True)
print('Приветствуем тебя, славный рыцарь', knight.name)
print('Ты стоишь у входа в лес, полный смертельных опасностей')
into = input('Готов ли ты войти внутрь и сразиться с врагами (да/нет)?\n')

if into == 'да':
    print('\n***Да начнется битва!***\n')

    enemies = [
        Warrior('Питер', 45, 30, 10, True),
        Warrior('Сержио', 55, 40, 15, True),
        Dragon('Дрогон', 60, 70, 30, True),
        Dragon('Визерион', 65, 55, 45, True)
    ]

    play = True
    while play:
        if knight.health <= 0:
            print('Рыцарь', knight.name, 'погиб в поединке с врагами')
            play = False
            break

        if len(enemies) == 0:
            print('Рыцарь', knight.name, 'одолел всех врагов')
            play = False
            break
        
        enemy = choice(enemies)  # выбираем случайного врага
        enemy.hello()
        enemy.print_info()
        
        attack_enemy = input('Вступить в бой с врагом (да/нет)?\n')
        if attack_enemy == 'да':
            if randint(0, 1) == 0:
                knight.attack(enemy)  # рыцарь атакует
            else:
                enemy.attack(knight)  # враг атакует
        
        if enemy.health <= 0:
            print(enemy.name, 'погиб от руки', knight.name)
            enemies.remove(enemy)
    else:
        print('Рыцарь', knight.name, 'решил не вступать в бой')

print('Тут и сказочке конец.')

end = input()