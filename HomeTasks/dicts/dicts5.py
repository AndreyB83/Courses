# Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
# Результаты выведите на экран.

_string = 'pythonist'
_dict = {}

for i in _string:
    if i not in _dict:
        _dict[i] = 1
    else:
        _dict[i] += 1

print(_dict)
