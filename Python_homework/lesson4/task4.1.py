from sys import argv

name, hours, tax_per_hour, bonus = argv
salary = float(hours)*float(tax_per_hour) + float(bonus)
print(f'Заработная плата сотрудника составит {salary} руб.')