class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Результат операции : {self.quantity:.2f}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if other == 0:
            return 'Деление на ноль невозможно!'
        else:
            return Cell(self.quantity / other.quantity)

    def make_order(self, el_in_row):
        row = ''
        for i in range(int(self.quantity / el_in_row)):
            row += f'{"*" * el_in_row}\n'
        row += f'{"*" * (self.quantity % el_in_row)}'
        return row


c_1 = Cell(17)
c_2 = Cell(12)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order(5))
