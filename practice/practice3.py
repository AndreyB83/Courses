# Дано множество целых чисекл {-3, 8, 15, -5, 0, 7}.

def sum_under_7(_set):
    return sum(filter(lambda x: x < 7, _set))


def print_set_info(_set):
    print(f'Min: {min(_set)}')
    print(f'Max: {max(_set)}')
    print(f'Sum under 7: {sum_under_7(_set)}')


if __name__ == '__main__':
    