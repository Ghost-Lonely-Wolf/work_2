class Stationery:
    def __init__(self, title='Название'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки')

t = Stationery()
t.draw()

p = Pen('Ручку')
p.draw()

s = Pencil('Карандаш')
s.draw()

h = Handle('Маркер')
h.draw()