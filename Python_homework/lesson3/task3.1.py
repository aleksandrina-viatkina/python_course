def division_func(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 // num2
        print(result)
    except ZeroDivisionError:
        print('Ошибка! Деление на ноль невозможно')
    except ValueError:
        print('Ошибка! Необходимо ввести число')


division_func(input('Введите первое число '), input('Введите второе число '))
