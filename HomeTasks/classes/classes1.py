# Напишите программу с классом Math. Создайте два атрибута — a и b.
# Напишите методы addition — сложение, multiplication — умножение,
# division — деление, subtraction — вычитание.
# При передаче в методы параметров a и b
# с ними нужно производить соответствующие действия и печатать ответ.

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a, b):
        return print(a + b)

    def multiplication(self, a, b):
        return print(a * b)

    def division(self, a, b):
 #       try:
 #           if b == 0
 #       except ZeroDivisionError as e:
 #       print(e)
        return print(a / b)

    def subtraction(self, a, b):
        return print(a - b)


# выводим результат:

math = Math('a', 'b')
math.addition(2, 3)
math.multiplication(5, 8)
math.division(4, 8)
math.subtraction(6, 9)
