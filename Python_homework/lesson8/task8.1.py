class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        data = f'{self.day} - {self.month} - {self.year}'
        return data

    @classmethod
    def change_type(cls, day, month, year):
        my_list = [day, month, year]
        for el in my_list:
            print(int(el), end=' ')

    @staticmethod
    def valid(day, month, year):
        if not 1 <= day <= 31:
            print('Некорректно введено число - день')
        if not 1 <= month <= 12:
            print('Некорректно введен месяц')
        if not 2000 <= year <= 2020:
            print('Некорректно введен год')
        if 1 <= day <= 31 and 1 <= month <= 12 and 2000 <= year <= 2020:
            print('Все в порядке.Значения введены верно.')


date = Date(8, 11, 1990)
print(date)
print(date.change_type(8, 11, 2020))
date.valid(35, 13, 2020)
