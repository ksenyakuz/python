# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def sep_func(num_1, num_2):
    try:
        return num_1 // num_2
    except ZeroDivisionError:
        print('Деление на ноль!')


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

sep_numbers = sep_func(number_1, number_2)
print(f'Результат деления: {sep_numbers}')