# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])

name_1 = input('Ваше имя: ')
surname_1 = input('Ваша фамилия: ')
year_1 = input('Ваш год рождения: ')
city_1 = input('Ваш город проживания: ')
email_1 = input('Ваш email: ')
phone_1 = input('Ваш телефон: ')

print(user_info(name_1, surname_1, year_1, city_1, email_1, phone_1))