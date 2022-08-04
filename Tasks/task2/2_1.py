_tuple = (2, 6, 45, 32, 144, 8)

for i in _tuple:
    if i % 1 != 0:
        print(_tuple)
        break
else:
    print(tuple(sorted(_tuple)))
