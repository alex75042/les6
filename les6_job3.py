#3. Реализовать базовый класс Worker (работник).
#● определить атрибуты: name, surname, position (должность),
# income (доход);
#● последний атрибут должен быть защищённым
# и ссылаться на словарь, содержащий
#элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
#● создать класс Position (должность) на базе класса Worker;
#● в классе Position реализовать методы получения
# полного имени сотрудника
#(get_full_name) и дохода с учётом премии (get_total_income);
#● проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.


class Worker():


    def work_plan(self, name, surname, position, __income__):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = __income__
        print(name, surname, position, __income__)

class Position(Worker):

    def get_full_name(self):
        full_name = []
        full_name.append(name)
        full_name.append(surname)
        self.full_name = full_name
        return self.full_name
    def get_total_income(self):
        total_income = int(income['wage']) + int(income['bonus'])
        self.total_income = total_income
        return self.total_income

name = str(input('Имя'))
surname = str(input('Фамилия'))
position = str(input('Должность'))
income = {}
income['wage'] = str(input('зарплата'))
income['bonus'] = str(input('премия'))

sheet = Worker()
sheet.work_plan(name, surname, position, income)

sheet_f = Position()
print(sheet_f.get_full_name(), sheet_f.get_total_income())
