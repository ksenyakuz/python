# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def use_fabric(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def use_fabric(self):
        result = (self.v / 6.5 + 0.5)
        return result


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def use_fabric(self):
        result = (self.h * 2 + 0.3)
        return result


    def use_fabric_all(self, list_1):
        i = 0
        for suit in list_1:
            i += suit.use_fabric
        return f'Общий расход ткани: {i}'


coat = Coat(42)
suit = Suit(1.96)
suit_2 = Suit(1.65)
suit_3 = Suit(1.76)

print(coat.use_fabric)
print(suit.use_fabric)

suit_list = [suit, suit_2, suit_3]
print(suit.use_fabric_all(suit_list))
