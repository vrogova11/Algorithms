"""
https://drive.google.com/file/d/1zH1f4k0AT6KrwKlKinLUCrSKuRfeIFwa/view?usp=sharing
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
let_1 = input('Введите первую букву от a до z: ')
let_2 = input('Введите вторую букву от a до z: ')
kod_1 = ord(let_1)
kod_2 = ord(let_2)
num_1 = kod_1 - 96
num_2 = kod_2 - 96
print(f'Порядковый номер буквы {let_1} = {num_1}')
print(f'Порядковый номер буквы {let_2} = {num_2}')
if num_1 < num_2:
    k = num_2 - num_1 - 1
elif num_1 > num_2:
    k = num_1 - num_2 - 1
else:
    k = 0
print(f'Количество букв между {let_1} и {let_2} = {k}')
