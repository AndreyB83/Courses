# Пользователь вводит строку. Преобразовать строку к кортежу.
# Подсчитать частоту встречающихся букв в строке.
# Результаты вывести на экран в формате “символ : количество вхождений”.

_string = input('Введите строку:')
_string_in_tuple = tuple(_string)
is_alpha = tuple(filter(str.isalpha, _string_in_tuple))

for i in is_alpha:
    print('Символ:', i, 'количество вхождений:', (is_alpha.count(i)))
