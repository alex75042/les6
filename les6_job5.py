#5. Реализовать класс Stationery (канцелярская принадлежность).
#● определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
#● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#● в каждом классе реализовать переопределение метода draw. Для каждого класса
#метод должен выводить уникальное сообщение;
#● создать экземпляры классов и проверить, 
#что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.stationery = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def pen_met(self):
        print(self.stationery, ' writing')


class Pensil(Stationery):

    def pensil_met(self):
        print(self.stationery, ' for drawing')


class Handle(Stationery):

    def handle_met(self):
        print(self.stationery, ' for marks')

my_pen = Pen('Pen')
my_pen.draw()
my_pen.pen_met()

my_pensil = Pensil('Pensil')
my_pensil.draw()
my_pensil.pensil_met()

my_handle = Handle('Handle')
my_handle.draw()
my_handle.handle_met()



