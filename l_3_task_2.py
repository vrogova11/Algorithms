"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
именно в этих позициях первого массива стоят четные числа.
"""
import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_2 = []
for i in range(1, len(array)):
    if array[i-1] % 2 == 0:
        array_2.append(i-1)
print(array_2)
