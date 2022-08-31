# Написать калькулятор. Пользователь вводит два числа и оператор.
# Необходимо вычислить результат операции и вывести на экран.
# Операторы, которые должен “знать” калькулятор: +, -, /, *, **, %, //.

try:
    first_number = float(input('Введите первое число:'))
    second_number = float(input('Введите второе число:'))
    operation = input('Введите наименование операции:')

    from decimal import Decimal

    if operation == '+':
        print(Decimal(first_number + second_number))
    elif operation == '-':
        print(Decimal(first_number - second_number))
    elif operation == '*':
        print(Decimal(first_number * second_number))
    elif operation == '/':
        print(Decimal(first_number / second_number))
    elif operation == '**':
        print(Decimal(first_number ** second_number))
    elif operation == '//':
        print(Decimal(first_number // second_number))
    elif operation == '%':
        print(Decimal(first_number % second_number))
except ZeroDivisionError:
    print('Ошибка деления на ноль')
except ValueError as e:
    print(e)
