# Пользователь вводит строку и символ.
# Определить количество вхождений символа в строку,
# независимо от регистра, при этом нельзя использовать метод count.

try:
    _string = str(input('Введите строку:'))
    _symbol = input('Введите символ:')
    _symbol_num = 0

    for i in _string.lower():
        if i in _symbol.lower():
            _symbol_num += 1
        else:
            continue

    print('Количество символов в строке:', _symbol_num)
except ValueError as e:
    print(e)
