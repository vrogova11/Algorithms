"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
https://drive.google.com/file/d/1u8qGPy_gWb9HIuexGyWB_4o4ACk36n5P/view?usp=sharing
"""
def fun_c(a):
    c = 0
    if a // 10 == 0:
        if a % 2 == 0:
            c = 1
        else:
            c = 0
        return c
    else:
        if a % 10 % 2 == 0:
            c = 1
        else:
            c = 0
        return c + fun_c(a // 10)


def fun_n(a):
    n = 0
    if a // 10 == 0:
        if a % 2 != 0:
            n = 1
        else:
            n = 0
        return n
    else:
        if a % 10 % 2 != 0:
            n = 1
        else:
            n = 0
        return n + fun_n(a // 10)


a = int(input('Введите натуральное число: '))
count_c = fun_c(a)
count_n = fun_n(a)

print(count_c)
print(count_n)
