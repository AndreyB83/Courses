deposit = int(input('Введите сумму депозита:'))
years = int(input('Ведите срок вклада, лет:'))
profit = float(deposit * (1.1 ** years))
print(profit - deposit)
