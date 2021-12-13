# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма чисел равна: ')
        return f'с = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение чисел равно: ')
        return f'с = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'с = {self.a} + {self.b} * i'


num_1 = ComplexNumber(2, 4)
num_2 = ComplexNumber(6, 8)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 * num_2)
