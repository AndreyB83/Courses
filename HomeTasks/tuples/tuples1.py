# даны два кортежа:
tuple_1 = (23, 'abc', 'and83@bk.ru', 348, 'h', 'f')
tuple_2 = (45, 'h', 'k', 48, 'and83@bk.ru', 55, 'df', 348)

for i in tuple_1:
    if i in tuple_2:
        print(i)
