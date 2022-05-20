"""
https://drive.google.com/file/d/1zH1f4k0AT6KrwKlKinLUCrSKuRfeIFwa/view?usp=sharing
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""
x1 = float(input('Введите координату x1: '))
y1 = float(input('Введите координату y1: '))
x2 = float(input('Введите координату x2: '))
y2 = float(input('Введите координату y2: '))
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
print(f'y = {k:.1f}x + {b:.1f}')
