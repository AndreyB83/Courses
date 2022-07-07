from functools import reduce

#задан список:
_list = [23, 25, 27, 29]
print('Сумма элементов списка равна:', sum(_list))
print('Произведение элементов списка равно:', reduce(lambda x, y: x*y, _list))