# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def get_date(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid_num(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Введено корректно'
                else:
                    return f'Неверно введен год'
            else:
                return f'Неверно введен месяц'
        else:
            return f'Неверно введен день'

    def __str__(self):
        return f'Текущая дата {Data.get_date(self.day_month_year)}'


result = Data('13 - 12 - 2021')
print(result)
print(result.valid_num(13, 12, 2021))

print(Data.get_date('22 - 13 - 2021'))
print(Data.valid_num(22, 13, 2021))
print(Data.get_date('32 - 12 - 2000'))
print(Data.valid_num(32, 12, 2000))
print(Data.get_date('1 - 3 - 2025'))
print(Data.valid_num(1, 3, 2025))
