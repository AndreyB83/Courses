# Имеется список с произвольными данными. Необходимо преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.
# Результаты выведите на экран. Использовать lambda-функции.

from collections import Hashable

in_list = (123, 'fgH12', [1, 2, 3, 4], '@', 56.6, False, {1: 2, 'a': 'b'}, {1, 2, 3}, (4, 5, 6))
result = filter(lambda x: isinstance(x, Hashable), in_list)
print(set(result))
