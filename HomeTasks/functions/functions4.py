# Напишите генератор custom_ange(start, end, step),
# который генерирует все целые числа от значения «start»
# до величины «end» включительно с шагом «step».
# Если пользователь задаст первое число большее чем второе,
# просто поменяйте их местами. «step» по умолчанию равен = 1.
# Также не допускать ввод дробных чисел.


def custom_ange(start, end, step=1):
    for number in range(start, end, step):
        if start > end:
            start, end = end, start
        yield number


while True:
    try:
        start_item = int(input('Введите целое число значения "start":'))
        end_item = int(input('Введите целое число значения "end":'))
    except ValueError:
        print('Вы неверно ввели данные...')
    else:
        break

try:
    step_item = int(input('Введите целое число значения "step":'))
except ValueError:
    print(list(custom_ange(start_item, end_item + 1)))
else:
    print(list(custom_ange(start_item, end_item + 1, step_item)))
