# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый,
# так и во второй список в порядке возрастания.

from random import randint

list_1 = [randint(0, 10000) for _ in range(randint(0, 10000))]
list_2 = [randint(0, 10000) for _ in range(randint(0, 10000))]
print(sorted(set(list_1).intersection(set(list_2))))
