# Функция count_lines(name) читает входной файл и подсчитывает количество строк в нем.
# Функция count_chars(name) читает входной файл и подсчитывает количество символов в нем.
# Функция test(name) вызывает обе функции подсчета с заданным именем входного файла.
# Все три функции модуля my_mod должны ожидать передачи строки с именем файла.

def count_lines(name):
    with open(name) as file:
        len(file.readlines())


def count_chars(name):
    with open(name) as file:
        len(file.read())


def test(name):
    return print(f'Количество строк в файле: {count_lines(name)}; количество символов в файле: {count_chars(name)}')


if __name__ == "__main__":
    print(test('name'))
