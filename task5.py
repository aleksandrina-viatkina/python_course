gross = int(input('Введите значение выручки фирмы, руб.: '))
costs = int(input('Введите значение издержек фирмы, руб.: '))
profit = gross - costs

if profit > 0:
    print(f'Финансовый результат - прибыль в размере {profit:.2f} руб.')
    rent = profit / gross
    print(f'Рентабельность составит {rent:.2f}')
    staff = int(input('Для определения прибыли в расчете на 1 сотрудника, введите количество сотрудников в Вашей фирме: '))
    profit_per_staff = profit / staff
    print(f'Прибыль в расчете на 1 сотрудника фирмы составит {profit_per_staff:.2f} руб.')
elif profit == 0:
    print(f'Финансовый результат - фирма сработала в 0')
else:
    print(f'Финансовый результат - убыток в размере {profit:.2f} руб.')