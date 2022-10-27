# Напишите цикл for, который выводит элементы
# словаря в отсортированном порядке (по возрастанию).

if __name__ == '__main__':
    dict_1 = {'a': 1, 'b': 2, 'c': 3}

    for key in sorted(dict_1.keys()):
        print(key, dict_1.get(key), dict_1[key])
