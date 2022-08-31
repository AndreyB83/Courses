# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start»
# до величины «end» включительно. Если пользователь задаст первое число большее чем второе,
# просто поменяйте их местами.


def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end))


while True:
    try:
        start_item = int(input('Введите целое число значения "start":'))
        end_item = int(input('Введите целое число значения "end":'))
    except ValueError:
        print('Вы неверно ввели данные...')
    else:
        print(sum_range(start_item, end_item + 1))
        break
