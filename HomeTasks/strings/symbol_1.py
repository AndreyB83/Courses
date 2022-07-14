_string = input(str('Введите строку:'))
_symbol = input('Введите символ:')
_symbol_num = 0

for i in _string.lower():
    if i in _symbol.lower():
        _symbol_num += 1
    else:
        pass
    
print('Количество символов в строке:', _symbol_num)
