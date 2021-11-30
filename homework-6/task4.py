# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет: {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет: {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше разрешенных 40 км!'
        else:
            return f'Скорость автомобиля {self.name} в пределах допустимого'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущая скорость рабочего автомобиля {self.name} сотавляет: {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше разрешенных 60 км!'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'

bmw = SportCar(120, 'black', 'bmw', False)
opel = TownCar(50, 'green', 'opel', False)
mazda = WorkCar(60, 'red', 'mazda', True)
ford = PoliceCar(90, 'white', 'ford', True)

print(bmw.turn_right())
print(opel.turn_left())

print(f'{mazda.turn_left()}, {ford.go()}')
print(f'{opel.turn_right()}, {bmw.stop()}')

print(f'{bmw.go()}, {bmw.show_speed()}')
print(f'{ford.go()}, {ford.show_speed()}')

print(f'{bmw.name}, цвет: {bmw.color}')
print(f'{mazda.name}, цвет: {mazda.color}')
print(f'{opel.name}, цвет: {opel.color}')
print(f'{ford.name}, цвет: {ford.color}')

print(f'{ford.name} - полицейская машина? {ford.is_police}')
print(f'{opel.name} - полицейская машина? {opel.is_police}')

print(mazda.show_speed())
print(opel.show_speed())
print(ford.show_speed())
print(bmw.show_speed())

