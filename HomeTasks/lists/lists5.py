#задан список:
_list = [12, 87, 99, 11]
num_min = min(_list)
num_max = max(_list)
for index in range(len(_list)):
    if _list[index] == num_min:
        _list[index] = num_max
        break

for index in range(len(_list)):
    if _list[index] == num_max:
        _list[index] = num_min
        break
print(_list)
