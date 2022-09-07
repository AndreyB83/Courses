# Напишите программу с классом Math. Создайте два атрибута — a и b.
# Напишите методы addition — сложение, multiplication — умножение,
# division — деление, subtraction — вычитание.
# При передаче в методы параметров a и b
# с ними нужно производить соответствующие действия и печатать ответ.

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
 #       try:
 #           if b == 0
 #       except ZeroDivisionError as e:
 #       print(e)
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


# выводим результат:

math = Math(5, 8)
print(math.addition())
print(math.multiplication())
print(math.division())
print(math.subtraction())
