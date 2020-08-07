class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


def make_list(*args):
    my_list = []
    while True:
        my_num = input('Введите целое число. Если Вы хотите выйти, введите Q: ')
        if my_num == 'Q' or my_num == 'q':
            print('Вы вышли')
            break
        try:
            if  my_num.isdigit() == False:
                raise MyException('Ошибка. Знаничение должно быть числовым.')
        except MyException as my_err:
                print(my_err)
                y_or_no = input('Хотите ли Вы продолжить, попробовать еще раз? Y/N ')
                if y_or_no == 'Y' or y_or_no == 'y':
                    continue
                else:
                    print(f'Программа завершена, введены числа {my_list}')
                    break
        else:
            my_num = int(my_num)
            my_list.append(my_num)
make_list()
