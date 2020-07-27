class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surmane = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник - {self.name, self.surmane}')

    def get_total_income(self):
        print(f'Доход сотрудника с учетом премии: {self._income.get("wage") + self._income.get("bonus"):.2f} тыс. руб.')

pos_1 = Position('Ivan', 'Ivanov', 'Manager', 50000, 8000)
pos_1.get_full_name()
pos_1.get_total_income()