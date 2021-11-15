# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count, cycle

# a
for i in count(1):
    if i > 20:
        break
    print(i)


# б
list_1 = [10, 20, 30, 40, 50, 60]
res = 0

for elem in cycle(list_1):
    res += 1
    if res > 18:
        break
    print(elem)
