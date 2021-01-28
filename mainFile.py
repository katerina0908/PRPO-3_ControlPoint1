# Дан массив из 10 чисел.
# Сколько элементов массива больше своих «соседей»,­ т.е. предыдущег­о и последующе­го.
# Первый и последний элементы не рассматривать.

import random
import numpy as np

mas = np.array([random.randrange(-50, 50) for _ in range(10)])

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

# 4. Определить, превосходит ли первый элемент массива из десяти чисел
# среднее значение элементов этого массива.

if mas[0] > np.mean(mas):
    answer = 'превосходит'
else: answer = 'не превосходит'

print('Первый элемент массива', mas[0], answer, 'среднее значение элементов массива', np.mean(mas))

# 5. Дан массив из 10 чисел. Определить­ сколько раз меняется знак у его элементов.

cntOfChange = 0

for i in range(1, len(mas)):
    if (mas[i] > 0 and mas[i-1] < 0) or (mas[i] < 0 and mas[i-1] > 0):
        cntOfChange += 1

if cntOfChange in (0, 1, 5, 6, 7, 8, 9, 10):
    s = 'раз'
else: s = 'раза'

print('У элементов массива знак меняется', cntOfChange, s)