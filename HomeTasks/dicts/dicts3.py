# Создайте словарь, в котором ключами будут числа от 1 до 10,
# а значениями эти же числа, возведенные в куб.
# Результаты выведите на экран.

_dict = {i: i ** 3 for i in range(1, 11)}
print(_dict)
