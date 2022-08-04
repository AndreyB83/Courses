from random import randint

_keys = list(randint(0, 9) for _ in range(randint(0, 1000)))
print(_keys)
_values = []

for i in _keys:
    _values.append(_keys.count(i))
print(_values)

_dict = dict(zip(_keys, _values))
print(_dict)
sorted_values = sorted(_dict.values(), reverse=True)
print(sorted_values)
sorted_values3 = sorted_values[:3]
print(sorted_values3)
sorted_dict = {}

for i in sorted_values3:
    for key in _dict.keys():
        if _dict[key] == i:
            sorted_dict[key] = _dict[key]
            break
print(sorted_dict)
