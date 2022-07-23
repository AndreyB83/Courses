#задан список:
_list = [1, 2, 5, '', 'fff', '3', '', 8]
_del = ''

for i in _list:
    if i == _del:
        _list.remove(_del)
print(_list)
