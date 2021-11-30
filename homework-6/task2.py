# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    __length = None
    __width = None
    weight = None
    thick = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def result(self):
        self.weight = 10
        self.thick = 2
        result = self.length * self.width * self.weight * self.thick
        print(f'Необходимое количество асфальта для покрытия: {result} тонн')

building_road = Road(6500, 20)
building_road.result()
