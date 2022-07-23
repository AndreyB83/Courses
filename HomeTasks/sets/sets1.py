def superset(set_1, set_2):
    if set_1 > set_2:
        print('Объект', set_1, ' является чистым супермножеством.')
    elif set_2 > set_1:
        print('Объект', set_2, ' является чистым супермножеством.')
    elif set_1 == set_2:
        print('Множества равны.')
    else:
        print('Супермножество не обнаружено.')


set_3 = {23, 45, 33, 7}
set_4 = {33, 23, 69, 7, 2, 45}
superset(set_3, set_4)
