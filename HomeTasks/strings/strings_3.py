# Пользователь вводит строку и символ.
# Определить количество вхождений символа в строку, независимо от регистра.

try:
    _string = str(input('Введите строку:'))
    understring = input('Введите символ:')
    print('Количество вхождений символа в строку:', _string.lower().count(understring.lower()))
except ValueError as e:
    print(e)
