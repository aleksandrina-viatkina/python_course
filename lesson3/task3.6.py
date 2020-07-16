def int_func():
    my_str = input('Введите строку в нижнем регистре латинского алфавита ').split()
    small_alph = range(ord('a'), ord('z') + 1)
    err = False
    for word in my_str:
        for i in word:
            if ord(i) not in small_alph:
                err = True
    if err:
        print('Неверный формат строки')
    else:
        my_str = ' '.join(my_str)
        print(my_str.title())


int_func()


"""Попробовала другим способом ограничить заглавные буквы"""


def int_func2():
    my_str = input('Введите строку в нижнем регистре латинского алфавита ')
    if my_str.islower():
        print(my_str.title())
    else:
        print('Неверный формат строки')

int_func2()
