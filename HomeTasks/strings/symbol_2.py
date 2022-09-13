# Пользователь вводит  строку и символ.
# Необходимо определить индексы первого и последнего вхождения символа в строке,
# при этом нельзя использовать строковые методы для поиска.

try:
    _string = str(input('Введите строку:'))
    _symbol = input('Введите символ:')

    for index in range(len(_string)):
        if _string[index] == _symbol:
            print('Индекс первого вхождения символа равен:', index)
            break

    for index in reversed(range(len(_string))):
        if _string[index] == _symbol:
            print('Индекс последнего вхождения символа равен:', index)
        break

except ValueError as e:
    print(e)
