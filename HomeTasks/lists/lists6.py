# задан список:
_list = [23, 45, 'f', 'aa', 53, 'f', 87, 45, 'go']
_repit = 0
list_2 = []

for _repit in _list:
    if _list.count(_repit) > 1:
        list_2.append(_repit)
        continue
print(list_2)
