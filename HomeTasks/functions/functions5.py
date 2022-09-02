# Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
# а также выводит на экран имя функции и ее параметры.


def time_dec(func):
    def wrapper(*args, **kwargs):

        from time import perf_counter

        t1_start = perf_counter()
        func(*args, **kwargs)
        t1_stop = perf_counter()

        print(f"Время выполнения функции {t1_stop - t1_start}, сек.")
        print(f"Имя декорируемой функции: {func.__name__}")
        print('args:', *args)
        print('kwargs:', **kwargs)
        return func(*args, **kwargs)
    return wrapper


@time_dec
def fun():
    print("проверочная функция")


fun()
