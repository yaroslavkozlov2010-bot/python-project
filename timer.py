from time import sleep

# Таймер
second = int(input('Type seconds (if you need minutes here is formula: min * 60): '))

for i in range(second, 0, -1): # принимает second, считает до нуля отнимая единицу
    print(f'{i}   ', end='\r')
    sleep(1)
print('0')

input('Write something to close the program, for example "Enter" or something another... ')
