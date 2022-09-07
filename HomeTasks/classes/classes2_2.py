# Напишите программу с классом Car. Создайте конструктор класса Car.
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов. Первый — запуск автомобиля,
# при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета.

class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def turn_on(self):
        return f"Автомобиль заведен"

    def turn_off(self):
        return f"Автомобиль заглушен"

    def get_year(self):
        return f"Год выпуска авто: {self.year}"

    def get_type(self):
        return f"Марка авто: {self.type}"

    def get_color(self):
        return f"Цвет авто: {self.color}"


# выводим результат:

car = Car('black', 'audi', 2022)
print(car.turn_on())
print(car.turn_off())
print(car.get_year())
print(car.get_type())
print(car.get_color())
