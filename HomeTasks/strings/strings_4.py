# Пользователь вводит  строку и символ. Необходимо определить индексы первого и
# последнего вхождения символа в строке.

try:
    _string = str(input('Введите строку:'))
    understring = input('Введите символ:')
    print('Индекс первого вхождения символа в строке:', _string.find(understring))
    print('Индекс последнего вхождения символа в строке:', _string.rfind(understring))
except ValueError as e:
    print(e)
