# Пользователь вводит строку и символ. Определить количество
# вхождений символа в строку, независимо от регистра.

import re

try:
    string_with_symbol = str(input('Введите строку с спец. символами:'))
    _symbol = len(re.findall(r'\W+', string_with_symbol))
    if _symbol:
        print('Количество спец. символов в строке:', _symbol)
    else:
        print('Символы не обнаружены')
except ValueError as e:
    print(e)
