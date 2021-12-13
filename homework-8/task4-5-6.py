# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class Store:
    def __init__(self):
        self.dict = {}

    def add_to(self, technique):
        self.dict.setdefault(technique.group_name(), []).append(technique)

    def extract(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class Technique:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Technique):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'

    def action(self):
        return 'Печатает'


class Scanner(Technique):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Xerox(Technique):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует'


store = Store()
scanner = Scanner('hp', '500', 2000)
store.add_to(scanner)
scanner = Scanner('hp', '600', 2002)
store.add_to(scanner)
scanner = Scanner('hp', '700', 2004)
store.add_to(scanner)

printer = Printer('e-15', 'sony', 100, 2013)
store.add_to(printer)
printer = Printer('e-20', 'sony', 150, 2014)
store.add_to(printer)
printer = Printer('e-30', 'sony', 200, 2015)
store.add_to(printer)

xerox = Xerox('xerox', '105', 2011)
store.add_to(xerox)
xerox = Xerox('xerox', '205', 2013)
store.add_to(xerox)
xerox = Xerox('xerox', '305', 2015)
store.add_to(xerox)

print(store.dict)
