# перемножить числовые значения словаря:
from functools import reduce

_dict = {1: 2, 3: 4, 5: 6, 7: 8}
print('Произведение элементов словаря =', reduce(lambda x, y: x*y, _dict.values()) * reduce(lambda x, y: x*y, _dict))
