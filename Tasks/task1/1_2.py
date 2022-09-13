list_1 = [1, 2, 3]
list_2 = [11, 22, 33]
list_3 = str(list_1 + list_2)
list_final = []
for num in list_3:
    list_final.append([num, len(num)])
print(list_final)

