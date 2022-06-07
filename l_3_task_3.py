"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_el = array[0]
min_el = array[0]
for i in range(1, len(array)):
    if array[i] > max_el:
        max_el = array[i]
    if array[i] < min_el:
        min_el = array[i]
print(f'max = {max_el}')
print(f'min = {min_el}')
array[array.index(max_el)] = array[array.index(min_el)]
print(array)
