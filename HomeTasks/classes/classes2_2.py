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
        return print(f"Автомобиль заведен")

    def turn_off(self):
        return print(f"Автомобиль заглушен")

    def get_year(self):
        return print(f"Год выпуска авто: {self.year}")

    def get_type(self):
        return print(f"Марка авто: {self.type}")

    def get_color(self):
        return print(f"Цвет авто: {self.color}")


# выводим результат:

car = Car('black', 'audi', '2022')
car.turn_on()
car.turn_off()
car.get_year()
car.get_type()
car.get_color()
