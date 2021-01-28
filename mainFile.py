# Дан массив из 10 чисел.
# Сколько элементов массива больше своих «соседей»,­ т.е. предыдущег­о и последующе­го.
# Первый и последний элементы не рассматривать.

import random
import numpy as np

mas = np.array([random.randrange(20) for _ in range(10)])

masUnique = np.unique(mas)
cntElemMas = len(masUnique)
while cntElemMas < 10:
    masUniqueShort = np.unique(masUnique)
    newElem = np.array([random.randrange(20) for _ in range(10 - cntElemMas)])
    masUnique = np.append(
    masUniqueShort, newElem)
    cntElemMas = len(np.unique(masUnique))

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

# 8. Дан массив из 10 чисел. Увеличить на единицу значения всех элементов кратных 5.
print('Дублирую исходный массив: ')
print(mas)
print('Новый массив, где все элементы, кратные 5, увеличены на 1: ')
print(np.where(mas%5 == 0, mas+1, mas))

# 9. Для массива из 10 целых чисел подчитать сумму элементов,­ значения которых не кратны 3.
masNotMultiples3 = np.where(mas%3 != 0, mas, 0)

print('Сумма элементов масива, значения которых не кратны 3: ')
print(np.sum(masNotMultiples3))

# 10. Для массива из десяти чисел подсчитать, сколько чисел меньше первого элемента массива
# и одновременно больше последнего элемента.

mas0 = mas[0]
mas9 = mas[9]
masStrange = np.where(np.where(mas < mas0, mas, 0) > mas9, 1, 0)
print('В массиве', np.sum(masStrange), 'элементов, которые меньше первого элемента', mas0,
      "и больше последнего элемента", mas9)

# 12. Дан массив из 10 разных чисел. Найти элемент, меньше всего отличающий­ся от второго.
print('Исходный массив: ')
print(mas)
print("Отсортированный массив из уникальных значений: ")
masUniqueSort = np.unique(masUnique)
print(masUniqueSort)

if masUniqueSort[1] - masUniqueSort[0] < masUniqueSort[2] - masUniqueSort[1]:
    el = masUniqueSort[0]
else: el = masUniqueSort[2]
print('Элемент, меньше всего отличающийся от второго: ')
print(el)

# 14. В массиве из 10 целых чисел подсчитать­ количество­ элементов,­ кратных 3.
masMultiples3 = np.where(mas%3 == 0, 1, 0)

print('Кол-во элементов масива, значения которых кратны 3: ')
print(np.sum(masMultiples3))

# 15. Найти сумму элементов массива из 10 чисел, меньших, чем 5-й элемент этого массива.
mas4 = mas[4]
print('Сумма элементов масива, значения которых меньше 5-го элемента массива', mas[4], ': ')
print(np.sum(np.where(mas < mas4, mas, 0)))