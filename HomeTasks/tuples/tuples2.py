_string = input('Введите строку:')
_string_in_tuple = tuple(_string)
is_alpha = tuple(filter(str.isalpha, _string_in_tuple))

for i in is_alpha:
    print('Символ:', i, 'количество вхождений:', (is_alpha.count(i)))
