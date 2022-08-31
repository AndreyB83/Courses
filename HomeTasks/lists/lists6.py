# Дан список. Необходимо определить,
# есть ли в списке повторяющиеся элементы,
# если да, то вывести на экран это значение.

_list = [23, 45, 'f', 'aa', 53, 'f', 87, 45, 'go']
repit_items = []

for i in _list:
    if _list.count(i) > 1:
        repit_items.append(i)

print(repit_items)
