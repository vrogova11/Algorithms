"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
https://drive.google.com/file/d/1u8qGPy_gWb9HIuexGyWB_4o4ACk36n5P/view?usp=sharing
"""
from random import randint

n = randint(0, 100)
print('Отгадайте заданное целое число от 0 до 100! У Вас есть 10 попыток!')
for i in range(1, 11):
    a = int(input(f'{i} попытка: '))
    if a > n:
        print('Введенное число больше загаданного!')
    elif a < n:
        print('Введенное число меньше загаданного!')
    else:
        print('Вы угадали!')
        break
