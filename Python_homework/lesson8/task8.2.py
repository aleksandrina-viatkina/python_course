class MyErrorZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    if input('Если Вы хотите расчитать операцию "деление" - нажмите Enter, если выйти - Q ').upper() == 'Q':
        break
    num1 = input('Введите делимое - положительное число: ')
    num2 = input('Введите делитель - положительное число: ')
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            raise MyErrorZeroDiv('Деление на ноль невозможно. Программа завершена')
        result = num1 // num2
    except MyErrorZeroDiv as my_err:
        print(my_err)
    except ValueError:
        print('Ошибка! Необходимо ввести число')
    else:
        print(f'Результат операции - {result}')


