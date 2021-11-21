# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json

profit = {}
elem = {}
subject = 0
average = 0
i = 0

with open('test_7.txt', 'r') as file_obj:
    for line in file_obj:
        firm, form, earning, damage = line.split()
        profit[firm] = int(earning) - int(damage)
        if profit.setdefault(firm) >= 0:
            subject = subject + profit.setdefault(firm)
            i += 1
    if i != 0:
        average = subject / i
        print(f'Средняя прибыль: {average}')

    elem = {'Средняя прибыль': (average)}
    profit.update(elem)

    print(f'Прибыль компаний: {profit}')


with open('new_test_7.json', 'w') as write_js:
    json.dump(profit, write_js)
