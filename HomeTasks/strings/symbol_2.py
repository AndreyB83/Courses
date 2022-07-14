_string = input(str('Введите строку:'))
_symbol = input('Введите символ:')

for index in range(len(_string)):
    if _string[index] == _symbol:
        print('Индекс первого вхождения символа равен:', (index))
        break

for index in reversed(range(len(_string))):
    if _string[index] == _symbol:
        print('Индекс последнего вхождения символа равен:', (index))
        break