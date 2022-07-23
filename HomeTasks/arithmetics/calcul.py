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



