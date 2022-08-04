_dict = {'key1': 'value_1', 'key2': 2, 'key3': '3'}
_value = input(str('Введите искомое в словаре значение:'))
_values = str(_dict.values())
if _value in _values:
    print('В заданном словаре существует значение', _value)
else:
    print('В заданном словаре значения', _value, 'нет.')
