# Напишите программу, которая с помощью анонимной функции
# извлекает из списка числа, делимые на 15. Результат вывести на экран.

result = filter(lambda x: x % 15 == 0, [15, 20, 30, 40, 50, 60])
print(list(result))
