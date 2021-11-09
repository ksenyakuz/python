# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# 1 list

season = ['winter', 'spring', 'summer', 'autumn']

month = int(input('Введите номер месяца от 1 до 12: '))

if month == 12 or month == 1 or month == 2:
    print(season[0])
elif month == 3 or month == 4 or month == 5:
    print(season[1])
elif month == 6 or month == 7 or month == 8:
    print(season[2])
elif month == 9 or month == 10 or month == 11:
    print(season[3])
else:
    print('Такого месяца не существует')

# 2 dict

season_1 = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

month_1 = int(input('Введите номер месяца от 1 до 12: '))

if month_1 == 12 or month_1 == 1 or month_1 == 2:
    print(season_1.get(1))
if month_1 == 3 or month_1 == 4 or month_1 == 5:
    print(season_1.get(2))
if month_1 == 6 or month_1 == 7 or month_1 == 8:
    print(season_1.get(3))
if month_1 == 9 or month_1 == 10 or month_1 == 11:
    print(season_1.get(4))
else:
    print('Такого месяца не существует')
