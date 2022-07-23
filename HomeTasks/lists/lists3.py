#задан список чисел:
_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 70, 60, 50, 40, 30, 20, 10]
_del = 20

for i in _list:
    if i == _del:
        _list.remove(_del)
print(_list)