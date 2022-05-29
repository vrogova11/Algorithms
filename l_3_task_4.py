"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 40
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

set_number = set(array)
d = {}
count = 0
max_count = 0
for num in set_number:
    for j in range(len(array)):
        if array[j] == num:
            count += 1
    d[num] = count
    if count > max_count:
        max_count = count
        max_num = num
    count = 0
print(d)
print(max_num)
