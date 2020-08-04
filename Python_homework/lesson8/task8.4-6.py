from abc import abstractmethod
class Storage:
    @staticmethod
    def get_to_storage():
        i = 1
        dep =''
        while i <= 3:
            #обозначаем подразделение
            if i == 1:
                dep = 'Офис'
            elif i == 2:
                dep = 'Цех'
            elif i == 3:
                dep = 'Склад'
            if input(f'Нажмите Enter, если нужно заказать технику в {dep}, иначе - нажмите Q: ').upper() == 'Q':
                break
            try:
                printer_name = input('Введите модель принтера  ')
                printer_quant = int(input('Введите необходимое количество принтеров  '))
                scanner_name = input('Введите модель сканера  ')
                scanner_quant = int(input('Введите необходимое количество сканеров  '))
                copier_name = input('Введите модель ксерокса  ')
                copier_quant = int(input('Введите необходимое количество ксероксов  '))
                equipment = {dep: {'Принтеры': {'Модель': printer_name, 'Количество': printer_quant},
                               'Сканеры': {'Модель': scanner_name, 'Количество': scanner_quant},
                               'Ксероксы': {'Модель': copier_name, 'Количество': copier_quant}}}
            except ValueError:
                print('Неверный формат введенных данных')
                continue
            print(equipment)
            i += 1





class OfficeEquipment(Storage):
    def __init__(self, department, name, price, quantity, num_pages):
        self.dep = department
        self.name = name
        self.price = price
        self.quant = quantity
        self.number_of_pages = num_pages

    @abstractmethod
    def print_pages(self):
        pass

class Printer(OfficeEquipment):
    def __str__(self):
        return f'Заказ в {self.dep}: принтеры - {self.name} по цене {self.price} в количестве {self.quant} шт.'

    def print_pages(self):
        return f'В принтер {self.name} помещается {self.number_of_pages} листов для печати за один раз.'


class Scanner(OfficeEquipment):
    def __str__(self):
        return f'Заказ в {self.dep}: сканеры - {self.name} по цене {self.price} в количестве {self.quant} шт.'

    def print_pages(self):
        return f'Сканер {self.name} может отсканировать {self.number_of_pages} листов за один раз.'


class Copier(OfficeEquipment):
    def __str__(self):
        return f'Заказ в {self.dep}: ксероксы - {self.name} по цене {self.price} в количестве {self.quant} шт.'
    def print_pages(self):
        return f'Ксерокс {self.name} может сделать {self.number_of_pages} копий за один раз.'


pos1 = Printer('Цех', 'HP lazer 800', 5000, 5, 200)
pos2 = Scanner('Склад', 'Canon X30', 3500, 5, 80)
pos3 = Copier('Офис', 'Xerox A8', 4300, 3, 100)
print(pos1)
print(pos2)
print(pos3)
print(f'Общая сумма заказа офисного оборудования составляет {float(pos1.price + pos2.price + pos3.price)} руб.')
print('--- Возможности печати ---')
print(pos1.print_pages())
print(pos2.print_pages())
print(pos3.print_pages())
print()
print('Делаем заказ по департаментам')
s = Storage()
s.get_to_storage()
