#%%[code]
# Класс
# Создаем чертеж (класс)
class Computer: # Скобки у родительского класса необязательны
    def __init__(self, brand, cpu):  # __init__ — это конструктор. Он создает свойства
        self.brand = brand          # Свойство: марка
        self.cpu = cpu              # Свойство: процессор

    def turn_on(self):              # Метод — это функция внутри класса
        print(f"Компьютер {self.brand} на процессоре {self.cpu} включился!")

# Создаем объект (как `new` в JS, но в Python слово `new` писать НЕ нужно)
my_pc = Computer("ASUS", "Intel i5")

# Обращаемся к свойствам и методам через точку
print(my_pc.brand)  # Выведет: ASUS
my_pc.turn_on()     # Выведет: Компьютер ASUS на процессоре Intel i5 включился!

# Класс (Наследование)
# Создаем дочерний класс Laptop, который копирует всё у Computer
class Laptop(Computer):
    def __init__(self, brand, cpu, battery):
        super().__init__(brand, cpu)  # super() забирает свойства у родителя
        self.battery = battery        # Добавляем свое новое свойство

my_laptop = Laptop("Apple", "M3", 100)
my_laptop.turn_on()  # Метод turn_on() работает, хотя мы его здесь не писали!

#%%[code]
# Класс (Полиморфизм)
class TextEditor:
    def open_file(self):
        print("Открываю текстовый файл в VS Code...")

class ImageEditor:
    def open_file(self):
        print("Открываю картинку в Photoshop...")

# Мы можем запустить один и тот же метод в цикле для разных объектов:
programs = [TextEditor(), ImageEditor()]
for app in programs:
    app.open_file()  # Каждая программа отработает по-своему

#%%[code]
# Класс (Инкапсуляция)
class BankAccount:
    def __init__(self, money):
        self.__balance = money  # ДВА подчеркивания делают переменную приватной

    def get_balance(self):      # Специальный метод (геттер) для безопасного просмотра
        return self.__balance

account = BankAccount(5000)
# print(account.__balance)  # ОШИБКА! Напрямую к переменной не подобраться
print(account.get_balance())  # Правильно. Выведет: 5000
