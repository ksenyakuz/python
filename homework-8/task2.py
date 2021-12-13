# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def divide_by_zero(num_1, num_2):
        try:
            return (num_1 / num_2)
        except:
            return (f'Деление на ноль!')


result = ZeroDivision(50, 10)
print(result.divide_by_zero(50, 10))

print(ZeroDivision.divide_by_zero(30, 0))
