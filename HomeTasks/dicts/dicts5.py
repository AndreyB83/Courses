_string = 'pythonist'
_dict = {}
for i in _string:
    if i not in _dict:
        _dict[i] = 1
    else:
        _dict[i] += 1
print(_dict)
