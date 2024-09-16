# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."


class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        House.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    # def __len__(self):
    #     return self.number_of_floors
    #
    # def __str__(self):
    #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    #
    # def __eq__(self, other):
    #     return self.number_of_floors == other.number_of_floors
    #
    # def __lt__(self, other):
    #     return self.number_of_floors < other.number_of_floors
    #
    # def __le__(self, other):
    #     return self.number_of_floors <= other.number_of_floors
    #
    # def __gt__(self, other):
    #     return self.number_of_floors > other.number_of_floors
    #
    # def __ge__(self, other):
    #     return self.number_of_floors >= other.number_of_floors
    #
    # def __ne__(self, other):
    #     return self.number_of_floors != other.number_of_floors
    #
    # def __add__(self, other):
    #     if isinstance(other, int):
    #         self.number_of_floors += other
    #     else:
    #         self.number_of_floors += other.number_of_floors
    #     return self
    #
    # def __radd__(self, other):
    #     if isinstance(other, int):
    #         self.number_of_floors += other
    #     else:
    #         self.number_of_floors += other.number_of_floors
    #     return self
    #
    # def go_to(self, new_floor):
    #     if self.number_of_floors < new_floor:
    #         print('Такого этажа не существует')
    #     else:
    #         for i in range(1, new_floor + 1):
    #             print(i)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

# # Занание 1
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
#
# h1.go_to(5)
# h2.go_to(10)
#
# # Задание 2
# h1 = House('ЖК Эльбрус', 10) # переопределяем параметры объекта
# h2 = House('ЖК Акация', 20) # переопределяем параметры объекта
#
# # __str__
# print(h1)
# print(str(h2)) # данная запись тоже корректна ??? - работает
#
# # __len__
# print(len(h1))
# print(len(h2))

# Задание 3
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
#
# print(h1 == h2)
#
# h1 += 10 # __iadd__ ??? работает и без iadd
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__
#
# h1 = h1 + h2
# print(h1)
#
# h1 = h2 + h1
# print(h1)

# Задание 4

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
input() # Для того, чтобы диструктор __del__ не удирал с памяти оставшыеся объекты.