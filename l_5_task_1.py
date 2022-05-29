# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', 'name k_1 k_2 k_3 k_4 profit')
count_c = int(input('Введите количество компаний: '))
all_comp = set()
all_profit = 0
i = 0
while i < count_c:
    name = input('Введите название предприятия: ')
    k_1 = int(input('Введите прибыль за 1 квартал: '))
    k_2 = int(input('Введите прибыль за 2 квартал: '))
    k_3 = int(input('Введите прибыль за 3 квартал: '))
    k_4 = int(input('Введите прибыль за 4 квартал: '))
    profit = (k_1 + k_2 + k_3 + k_4) / 4
    one_comp = Company(name, k_1, k_2, k_3, k_4, profit)
    all_comp.add(one_comp)
    all_profit += profit
    i += 1

print(all_comp)
mid_profit = all_profit/count_c
print(f'Средняя прибыль за год для всех предприятий: {mid_profit}')

print('Предприятия с прибылью выше средней:')
for j in all_comp:
    if j.profit > mid_profit:
        print(f'Предприятие {j.name} заработало: {j.profit}.')

print('Предприятия с прибылью ниже средней:')
for cmp in all_comp:
    if cmp.profit < mid_profit:
        print(f'Предприятие {cmp.name} заработало: {cmp.profit}.')
