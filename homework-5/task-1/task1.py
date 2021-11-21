# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []

while True:
    result = input('Введите текст: ')
    if result == '':
        print(my_list)
        exit()
    else:
        result_2 = result + '\n'
        my_list.append(result_2)

    with open("test.txt", "w") as file_obj:
        file_obj.writelines(my_list)
