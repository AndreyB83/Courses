# Пользователь вводит количество рублей, которые он кладет на вклад,
# и количество лет. Рассчитать прибыль, если известно,
# что условия банка 10% годовых (каждый год размер вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Вывести прибыль на экран.

try:
    deposit = int(input('Введите сумму депозита:'))
    years = int(input('Ведите срок вклада, лет:'))
    profit = float(deposit * (1.1 ** years))
    print(profit - deposit)
except ValueError as e:
    print(e)