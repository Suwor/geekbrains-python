class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки для ручки')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки для карандаша')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки для маркера')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер. Бесполезное свойство. Впрочем, как и сама задача.')

pen.draw()
pencil.draw()
handle.draw()
