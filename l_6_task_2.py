"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести
на экран. Например, если введено число 3486, надо вывести 6843.
"""
import sys


class SumMemory:

    def __init__(self):
        """
        _sum_memory - общее количество занятой памяти
        _types - словарь вида {'type': [count, size]}
        """
        self._sum_memory = 0
        self._types = {}

    def extend(self, *args):
        for obj in args:
            self._add(obj)

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        self._sum_memory += spam
        eggs = type(obj)
        if eggs in self._types:
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1, spam]

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self._add(key)
                    self._add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self._add(item)

    def __str__(self):
        return f'Переменные заняли в сумме {self._sum_memory} байт\n' + \
               '\n'.join([f'Объекты класса {key} в количестве {value[0]} заняли {value[1]} байт'
                          for key, value in self._types.items()])


def fun(a):
    list_a = list(str(a))
    list_a.reverse()
    fin_list = ''.join(map(str, list_a))
    return fin_list


num = int(input('Введите целое число: '))

sum_mem = SumMemory()
sum_mem.extend(fun(num))
print(sum_mem)

# Введите целое число: 3434343434343434343434
# Переменные заняли в сумме 71 байт