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

# В массиве из 10 чисел найти сумму элементов больших, чем второй элемент этого массива.

sumBigger10 = np.sum([elem for elem in mas if elem>10])

print('Сумма элементов больших, чем второй элемент массива (', mas[1], '):')
print(sumBigger10)