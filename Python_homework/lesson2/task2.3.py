month = int(input('Введите номер месяца '))
# Решение через list
if month in [12, 1, 2]:
    print('winter')
elif month in [3, 4, 5]:
    print('spring')
elif month in [3, 4, 5]:
    print('spring')
elif month in [6, 7, 8]:
    print('summer')
elif month in [9, 10, 11]:
    print('autumn')
else:
    print('Некорректно введен номер месяца, попробуйте еще раз')

# Решение через dict
month_2 = int(input('Введите номер месяца '))
seasons = dict(winter = (12, 1, 2), spring = (3, 4, 5), summer= (6, 7, 8), autumn = (9, 10, 11))
for key in seasons:
    if month_2 in seasons[key]:
        print(key)