# калькулятор квадрата


from decimal import Decimal


side_of_square = input('Введите значение длины стороны квадрата, мм:')
side_of_square = float(side_of_square)
s_square = side_of_square ** 2
p_square = side_of_square * 4
d_square = side_of_square * 2 ** 0.5

print('Площадь квадрата равна:', Decimal(s_square), 'мм2')
print('Периметр квадрата равен:', Decimal(p_square), 'мм')
d_square = Decimal(d_square)
print('Длина диагонали квадрата равна:', round(d_square, 2), 'мм')