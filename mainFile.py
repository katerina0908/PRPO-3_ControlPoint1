# Дан массив из 10 чисел.
# Сколько элементов массива больше своих «соседей»,­ т.е. предыдущег­о и последующе­го.
# Первый и последний элементы не рассматривать.

import random

mas = []
for i in range(10):
    mas.append(random.randrange(0,10))

print(mas)

bigger = 0

for i in range(1, len(mas) - 1):
    if mas[i] > mas[i-1] and mas[i] > mas[i+1]:
        bigger += 1

print(bigger)