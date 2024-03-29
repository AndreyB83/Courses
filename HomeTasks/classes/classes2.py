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

    def new_year(self, new_year):
        self.year = new_year
        return f"Год выпуска авто: {new_year}"

    def new_type(self, new_type):
        self.type = new_type
        return f"Марка авто: {new_type}"

    def new_color(self, new_color):
        self.color = new_color
        return f"Цвет авто: {new_color}"


# выводим результат:

car = Car('color', 'type', 'year')
print(car.turn_on())
print(car.turn_off())
print(car.new_year(2023))
print(car.new_type('audi'))
print(car.new_color('black'))
