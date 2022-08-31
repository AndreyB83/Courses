# Напишите функцию, чтобы проверить, является ли строка панграммой или нет.
# Панграмма — фраза, содержащая в себе все буквы алфавита.

while True:
    _list = str(input('Введите строку, состоящую из букв кириллицы:'))


    def kirillica(_list, alphabet=None):
        if alphabet is None:
            alphabet = set('абвгдеёжзийклмнопрстуфхцчшщьъэюя')
        return not alphabet.isdisjoint(_list)


    try:
        if kirillica(_list) is True and _list.isalpha():
            break
        else:
            print('Неверно введены символы')
    except:
        print('Что-то пошло не так...')

_list = set(_list)
alphabet = set('абвгдеёжзийклмнопрстуфхцчшщьъэюя')

if _list == alphabet:
    print('Введенная строка ЯВЛЯЕТСЯ панграммой')
else:
    print('Введенная строка НЕ ЯВЛЯЕТСЯ панграммой')
