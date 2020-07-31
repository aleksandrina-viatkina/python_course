class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки карандашом.')


class Pencil(Stationery):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки ручкой.')


class Handle(Stationery):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки маркером.')


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
