number_abc = int(input('Введите трехзначное целое число:'))
number_ab = number_abc // 10
number_c = number_abc % 10
number_a = number_ab // 10
number_b = number_ab % 10
sum_abc = number_a + number_b + number_c
print('Сумма чисел равна:', sum_abc)
