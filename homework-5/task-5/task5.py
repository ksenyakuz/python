# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def my_sum():
    with open('test_5.txt', 'w') as file_obj:
        numbers = input('Введите цифры через пробел: ')
        file_obj.writelines(numbers)
        result = numbers.split()
        print(sum(map(int, result)))

my_sum()
