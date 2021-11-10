# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    if num_1 > num_3 and num_2 > num_3:
        return num_1 + num_2
    elif num_1 > num_2 and num_3 > num_2:
        return num_1 + num_3
    elif num_2 > num_1 and num_3 > num_1:
        return num_2 + num_3

first_num = int(input('Первое число: '))
second_num = int(input('Второе число: '))
third_num = int(input('Третье число: '))

summ_numbers = my_func(first_num, second_num, third_num)
print(f'Сумма наибольших чисел: {summ_numbers}')