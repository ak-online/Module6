class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = list(color)
        self.filled = True
    def get_color(self):
        return self.__color
    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)
    def __is_valid_color(self, r, g, b):
        list_color = (r, g, b)
        if all(i >= 0 and i <= 255 for i in list_color):
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, *n_sides):
        if all(i > 0 for i in n_sides) and len(self.__sides) == len(n_sides):
            return True
        else:
            return False
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, diameter):
        super().__init__(color, diameter)
        self.__radius = diameter / 2
    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides

    def get_square(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        res = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return res


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        if len(sides) == 1:
            super().set_sides(sides[0])
            self.__sides = [sides[0]] * self.sides_count
    def get_volume(self):
        s_length = self.get_sides()[0]
        return s_length **3


print('CIRCLE')
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
print(len(circle1))
print('Circle square', circle1.get_square())

print('TRIANGLE')
t1 = Triangle((200, 200, 100), 10, 6, 1)
print(t1.get_color())
circle1.set_color(555, 656, 1177) # не Изменится
print(t1.get_color())
t1.set_sides(100, 100, 100)  # Изменится
print(t1.get_sides())
print('Triangle square', t1.get_square())

print('CUBE')
cube1 = Cube((222, 35, 130), 6)
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
print(cube1.get_volume())



