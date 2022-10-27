# Напишите программу, которая бы считала по просьбе пользователя
# позволить пользователю ввести начало и конец счета, а также интервал
# между называемыми целыми числами

def get_int(welcome_message):
    while True:
        try:
            _int = int(input(welcome_message))
        except ValueError as e:
            print(e)
        else:
            break
    return _int


def my_range(start, end, step):
    for i in range(start, end, step):
        print(i)


if __name__ == '__main__':
    _start = get_int('Введите начало интервала: ')
    _end = get_int('Введите конец интервала ')
    _step = get_int('Введите шаг интервала: ')
    my_range(_start, _end, _step)
