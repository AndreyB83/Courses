_list = [12, 'd', 1000, 'xxx@bk.ru', 67, 0, 'ff']
num = int(input('Введите целое число:'))
result = []

try:
    for i in _list:
        result.append(num / i)
except (TypeError, ValueError) as e:
    print(e)
except ZeroDivisionError:
    print('Ошибка деления на ноль')
else:
    print(result)
