def my_func(a, b, c):
    """Преобразовываем параметры функции в список и убираем минимальное значение, оставшиеся суммируем в результате"""
    list_func = [a, b, c]
    list_func.remove(min(list_func))
    return sum(list_func)

print(my_func(5, 8, 10))
