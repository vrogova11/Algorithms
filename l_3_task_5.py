"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный»
и «максимальный отрицательный». Это два абсолютно разных значения.
"""
import random

SIZE = 40
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

for i in range(len(array)):
    if array[i] < 0:
        max_num = array[i]
        break
for j in range(i+1, len(array)):
    if array[j] < 0:
        if array[j] > max_num:
            max_num = array[j]

print(max_num)
