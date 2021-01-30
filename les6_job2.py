#2. Реализовать класс Road (дорога).
#● определить атрибуты: length (длина), width (ширина);
#● значения атрибутов должны передаваться
# при создании экземпляра класса;
#● атрибуты сделать защищёнными;
#● определить метод расчёта массы асфальта,
# необходимого для покрытия всей дороги;
#● использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв. метра
#дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#● проверить работу метода.

#Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road():
    massa_1 = 25

    def area(self, lenght, width):
        self.length = lenght
        self.width = width
        self.arr = int(self.length) * int(self.width) * Road.massa_1
        return self.arr

    def get_massa_f(self, depth):
        self.depth = depth

        self.massa_f = self.arr * int(self.depth)
        return self.massa_f

leng = input('длинна дороги, м.')
widt = input('ширина, м.')
dept = input('толщина, см')
a = Road()
a.area(leng, widt)
print('Необходимо асфальта ', a.get_massa_f(dept) / 1000, 'тн.')
