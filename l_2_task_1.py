"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
завершается, а запрашивает новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления
на ноль, если он ввел его в качестве делителя.
https://drive.google.com/file/d/1u8qGPy_gWb9HIuexGyWB_4o4ACk36n5P/view?usp=sharing
"""
while True:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    while True:
        c = str(input('Введите знак операции +, -, *, / или 0 для выхода из программы: '))
        while c not in ('+', '-', '*', '/', '0'):
            print('Введен неверный знак операции!')
            c = str(input('Введите знак операции +, -, *, / или 0 для выхода из программы: '))
        if c != '0':
            if c == '+':
                rez = a + b
            elif c == '-':
                rez = a - b
            elif c == '*':
                rez = a * b
            elif b != 0:
                rez = a / b
            else:
                print('Деление на ноль невозможно!')
                break
            print(f'{rez = }')
            break
            break
        else:
            quit()






