"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести
на экран. Например, если введено число 3486, надо вывести 6843.
"""
import timeit
import cProfile

def fun(a):
    a = int(a)
    if a // 10 == 0:
        return f'{a}'
    else:
        rez = a % 10
        return f'{rez}{fun(a // 10)}'

print(timeit.timeit('fun(1234)', number=1000, globals=globals()))   # 0.004672999999999997
print(timeit.timeit('fun(123450797879)', number=1000, globals=globals()))   # 0.016053700000000004
print(timeit.timeit('fun(123456987980000000)', number=1000, globals=globals()))   # 0.0242338
print(timeit.timeit('fun(12345665450604640545064060)', number=1000, globals=globals()))  # 0.0234973

# def fun(a):
#     list_a = list(str(a))
#     list_a.reverse()
#     return ''.join(map(str, list_a))
#
#
# print(timeit.timeit('fun(1234)', number=1000, globals=globals()))  # 0.0019638000000000017
# print(timeit.timeit('fun(123450797879)', number=1000, globals=globals()))  # 0.003942000000000001
# print(timeit.timeit('fun(123456987980000000)', number=1000, globals=globals()))  # 0.005256800000000006
# print(timeit.timeit('fun(12345665450604640545064060)', number=1000, globals=globals()))  # 0.007255299999999992

# def fun(a):
#     a = str(a)
#     return a[len(a)::-1]
#
#
# print(timeit.timeit('fun(1234)', number=1000, globals=globals()))  # 0.0004055000000000031
# print(timeit.timeit('fun(123450797879)', number=1000, globals=globals()))  # 0.000418700000000001
# print(timeit.timeit('fun(123456987980000000)', number=1000, globals=globals()))  # 0.0004424000000000025
# print(timeit.timeit('fun(12345665450604640545064060)', number=1000, globals=globals()))  # 0.0004768999999999954

cProfile.run('fun(12345665450604640545064060)')

# Вывод: 1 вариант имеет линейную асимптотику, но работает медленнее всего, т.к. я использую рекурсию.
#        2 вариант также имеет линейную асимптотику, но работает примерно в 10 раз быстрее 1 варианта.
#        3 вариант также имеет лингейную асимптотику и работате примерно в 10 раз быстрее 2 варианта, т.к. включает одно преобразование типа и делает 1 срез.