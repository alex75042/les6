#4. Реализуйте базовый класс Car.
#● у класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина
#поехала, остановилась, повернула (куда);
#● опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar;
#● добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
#● для классов TownCar и WorkCar
# переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    def on_auto_start(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_polise = is_police
        print(self.name, ' цвет ', self.color)

    def go(self, go):
        self.go = go
        print('машина поехала? ', self.go)

    def stop_1(self, stop_1):
        self.stop_1 = stop_1
        print('Остановка ', self.stop_1)
    def turn(self, turn):
        self.turn = turn
        print('направление движения ', self.turn)

class SportCar(Car):
    pass
class PoliceCar(Car):
    pass
class TownCar(Car):
    def show_speed(self,speed):
        self.speed = speed
        if self.speed > 60:
            print('превышаем')
        else:
            pass
class WorkCar(Car):
    def show_speed(self,speed):
        self.speed = speed
        if self.speed > 40:
            print('скорость ', speed, ' > 40')
        else:
            pass


my_nam = input('TownCar, SportCar, WorkCar, PoliceCar?')
my_name = Car()

go_1 = input('поехали? да / нет')
st = input('Остановка?')
tur = input('налево, направо, прямо, назад')
speed = int(input('Скорость?'))
my_name.on_auto_start(speed, 'синий', my_nam, 'мигалка')
my_name.go(go_1)
my_name.stop_1(st)
my_name.turn(tur)

if my_nam == 'SportCar':
    a = SportCar()
elif my_nam =='PoliceCar':
    a = PoliceCar()
elif my_nam == 'TownCar':
    a = TownCar()
    a.show_speed(speed)
elif my_nam == 'WorkCar':
    a = WorkCar()
    a.show_speed(speed)
else:
    pass
