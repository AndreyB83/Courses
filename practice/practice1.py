# Напишите цикл for, который выводит код ASCII каждого символа в имени S

def get_str(welcom_message):
    _str = input(welcom_message)
    return _str


def get_ascii(message):
    for item in message:
        if ord(item) > MAX_ASCII_CODE:
            print('Строка содержит не ASCII символ!')
            break
        print(item, ord(item))

if __name__ == '__main__':