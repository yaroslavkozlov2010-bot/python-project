# Подсчет чисел
count = 0

x = int(input('Введи число: '))
while x != 0:
    if x % 4 == 0:
        count += 1
    x = int(input('Введи число: '))    
print(count)

print(' ')

# Сумма чисел
summ = 0

y = int(input('Введи число: '))
while y != 0:
    if y % 6 == 0:
        summ += y
    y = int(input('Введи число: '))
print(summ)

print(' ')

# Минимум
minimum = 30001
n = int(input('Кол-во чисел: '))

for i in range(n):
    z = int(input('Введи число: '))
    if z % 3 == 0:
        minimum = min(minimum, z)
print(minimum)



print(' ')

# Максимум
maximum = 0

w = int(input('Введи число: '))
while w != 0:
    pass


# Оканчивается на число n
minimum_2 = 30001
m = int(input('Кол-во: '))

for i in range(m):
    v = int(input('Введи число: '))
    if v % 10 == 6:
        minimum_2 = min(minimum_2, v)
print(minimum_2)

print('\nСР ')

#%%
# То, что попадось мне на ОГЭ
# Высчитать среднее арифметическое трехзначных чисел, если их нет, то выводит "NO"
count = 0
sum = 0

x = int(input('Введи число: '))
while x != 0:
    if 100 <= x <= 999: # Промежуток от 100 до 999
        count += 1
        sum += x
    x = int(input('Введи число: '))

if count > 0:
    print(sum / count)
else:
    print('NO')
# %%
