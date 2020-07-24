from functools import reduce

def multipl(el1, el2):
    return el1 * el2

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(multipl, my_list))

'''При помощи лямбда функции'''
my_list2 = [el for el in range(100, 1001) if el % 2 == 0]
my_func = lambda a, b : a*b
print(reduce(my_func, my_list2))