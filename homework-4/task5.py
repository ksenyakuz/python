# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


from functools import reduce

def mul_num(a,b):
    return a * b

my_list = [i for i in range(100, 1001) if i % 2 == 0]
result = reduce(mul_num, my_list)

print(my_list)
print(result)
