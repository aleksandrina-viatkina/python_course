class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        total_sum = f'{self.a + other.a} + {self.b + other.b} * i'
        return f'Сумма равна {total_sum}'

    def __mul__(self, other):
        total_mul = f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'
        return f'Произведение равно {total_mul}'


c1 = ComplexNum(2, 5)
c2 = ComplexNum(1, 3)
print(c1 + c2)
print(c1 * c2)
