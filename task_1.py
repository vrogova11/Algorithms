"""
https://drive.google.com/file/d/1zH1f4k0AT6KrwKlKinLUCrSKuRfeIFwa/view?usp=sharing
"""
number = int(input('Введите число от 100 до 999: '))
num_1 = number // 100
num_2 = number % 100 // 10
num_3 = number % 10
print(f'Сумма цифр {num_1}, {num_2}, {num_3} = {num_1 + num_2 + num_3}')
print(f'Произведение цифр {num_1}, {num_2}, {num_3} = {num_1 * num_2 * num_3}')
