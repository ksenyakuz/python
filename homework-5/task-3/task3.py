# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('test_2.txt', 'r') as file_obj:
    for i in file_obj:
        salary = i.split()[-1]
        surname = i.split()[0]
        if int(salary) < 20000:
            print(f'Оклад менее 20000: {surname} - {salary}')

with open('test_2.txt', 'r') as file_obj:
    sum = 0
    count = 10
    for line in file_obj:
        sum += int(line.split()[-1])
    average = sum / count

    print(f'Средняя величина дохода всех сотрудников: {average}')
