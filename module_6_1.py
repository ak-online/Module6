"""
2 класса родителя: Animal, Plant
Для класса Animal атрибуты
    alive = True(живой)
    и fed = False(накормленный),
    name - индивидуальное название каждого животного.

Для класса Plant атрибут edible = False(съедобность),
    name - индивидуальное название каждого растения
"""
class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
"""
4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.
У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.

"""
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

"""
У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
"""
class Flower(Plant):
    #edible = True
    pass
class Fruit(Plant):
    edible = True

"""
Создайте классы Animal и Plant с соответствующими атрибутами и методами
Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами. 
При необходимости переопределите значения атрибутов.
Создайте объекты этих классов.
"""
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)