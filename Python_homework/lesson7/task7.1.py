class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __add__(self, other):
        sum_data= [[self.matrix_data[i][j]+other.matrix_data[i][j] for j in range(len(self.matrix_data[0]))]
            for i in range(len(self.matrix_data))]
        return sum_data

    def __str__(self):
        return 'матрица:\n'+'\n'.join(' '.join(map(str, row)) for row in self.matrix_data)

m_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(m_1)
print(m_2)
m_3 = Matrix(m_1+m_2)
print(f'Сумма двух матриц - {m_3}')

