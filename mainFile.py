# Дан массив из 10 чисел.
# Сколько элементов массива больше своих «соседей»,­ т.е. предыдущег­о и последующе­го.
# Первый и последний элементы не рассматривать.

import random
import numpy as np

mas = np.array([random.randrange(100) for _ in range(10)])

print('Исходный массив: ')
print(mas)

bigger = 0

for i in range(1, len(mas) - 1):
    if mas[i] > mas[i-1] and mas[i] > mas[i+1]:
        bigger += 1

print('Кол-во элементов массива, которые больше своих соседей: ')
print(bigger)

# task-2
# Для массива из 10 чисел найти номер первого элемента, большего 25.

for i in range(len(mas)):
    if mas[i] > 25:
        #print(i, mas[i])
        bigger25 = i
        break

print('Порядковый номер первого элемента массива, большего 25: ')
print(i+1)

# task-3
# В массиве из 10 чисел найти сумму элементов больших, чем второй элемент этого массива.

sumBigger10 = np.sum([elem for elem in mas if elem>10])

print('Сумма элементов больших, чем второй элемент массива (', mas[1], '):')
print(sumBigger10)

# task-6
# Найти, сколько элементов массива из 10 чисел больше, чем четвертый элемент этого массива.

biggerThan4 = 0

for i in range(1, len(mas)):
    if mas[i] > mas[3]:
        biggerThan4 += 1

print(biggerThan4, 'элементов массива больше, чем 4й элемент', mas[3])

# 7. Найти сумму элементов массива из 10 чисел, меньших, чем 21.

masLessThan21 = np.where(mas < 21, mas, 0)

print('Сумма элементов массива, меньших, чем 21: ')
print(np.sum(masLessThan21))

# 16. Отобразить массив виде гистораммы
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = mas

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure

plt.show()