# Написать программу сложения и умножения двух положительных целых шестнадцатеричных
# чисел. При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
number_1 = input('Введите первое положительное целое шестнадцатиричное число:')
number_2 = input('Введите второе положительное целое шестнадцатиричное число:')
num_1 = list(number_1)
num_2 = list(number_2)

dict_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for i in range(1, len(num_1) + 1):
    if num_1[-i] in dict_16.keys():
        num_1[-i] = dict_16[num_1[-i]]

for i in range(1, len(num_2) + 1):
    if num_2[-i] in dict_16.keys():
        num_2[-i] = dict_16[num_2[-i]]

num_3 = deque()
if len(num_1) > len(num_2):
    for j in range(1, len(num_2) + 1):
        sum_ = int(num_1[-j]) + int(num_2[-j])
        num_3.appendleft(sum_)
    for k in range(len(num_1) - len(num_2)):
        num_3.appendleft(int(num_1[len(num_1) - len(num_2) - 1 - k]))
else:
    for j in range(1, len(num_1) + 1):
        sum_ = int(num_2[-j]) + int(num_1[-j])
        num_3.appendleft(sum_)
    for k in range(len(num_2) - len(num_1)):
        num_3.appendleft(int(num_2[len(num_2) - len(num_1) - 1 - k]))

summa_ = deque()
ost = 0
for i in range(1, len(num_3) + 1):
    num = num_3.pop()
    if num % 16 != 0:
        summa_.appendleft(num % 16 + ost)
        ost = num // 16
    else:
        summa_.appendleft(0 + ost)
        ost = 1
print(summa_)

summa_1 = deque()
dict_16 = {10: 'А', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
for i in range(1, len(summa_) + 1):
    spam = summa_.pop()
    if spam in dict_16.keys():
        summa_1.appendleft(dict_16[spam])
    else:
        summa_1.appendleft(spam)

print(summa_1)
