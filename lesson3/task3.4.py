"""Способ 1 - с функцией возведения в степень"""
def my_func(x, y):
    print (pow(x,y))

my_func(5,-2)

"""Способ 2 - с помощью цикла"""

def my_func2(x, y):
    result = 1
    if y >= 0:
        print('Ошибка! Необходимо, чтобы значение y было отрицательным ')
    else:
        for i in range(abs(y)):
            result *= x
        result = 1 / result
        print(round(result, 4))


my_func2(2, -3)
