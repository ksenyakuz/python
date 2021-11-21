# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ['First word\n', 'The second word\n', 'Third and last word\n']

with open("test_1.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_1.txt") as file_obj:
    lines = 0
    words = 0
    for line in file_obj:
        lines += line.count("\n")
        words = len(line.split(' '))
        print(f'Количество слов в строке: {words}')
    print(f'Количество строк: {lines}')

