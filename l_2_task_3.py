"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести
на экран. Например, если введено число 3486, надо вывести 6843.
https://drive.google.com/file/d/1u8qGPy_gWb9HIuexGyWB_4o4ACk36n5P/view?usp=sharing
"""
def fun(a):
    if a // 10 == 0:
        return f'{a}'
    else:
        rez = a % 10
        return f'{rez}{fun(a // 10)}'


a = int(input('Введите натуральное число: '))
num = fun(a)
print(int(num))