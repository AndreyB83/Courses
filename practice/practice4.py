# Даны три слова 'аквариум', 'мармелад' и 'рама'. Выведите на экран сперва все
# виды букв, которые присутствуют во всех словах сразу, а затем все виды букв,
# которые присутствуют в любом из них.


def words_info(word_1, word_2, word_3):
    dif_1 = set(word_1) - set(word_2) - set(word_3)
    dif_2 = set(word_2) - set(word_3) - set(word_1)
    dif_3 = set(word_3) - set(word_2) - set(word_1)
    print(f'Общие символы: {set(word_1) & set(word_2) & set(word_3)}')
    print(f'Уникальные символы: {dif_1 | dif_2 | dif_3}')


if __name__ == '__main__':
    words_info('аквариум', 'мармелад', 'рама')
