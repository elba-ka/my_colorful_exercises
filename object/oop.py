import math
class Parallelogram:
    def __init__(self, width, height, angle):
        self.width = width
        self.height = height
        self.angle = angle
    @property
    def area(self):
        return self.width * self.height * math.sin(self.angle)

    @property
    def perimeter(self):
        return (self.height + self.width) * 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def calculate_area(self):
        return self.width * self.height

    @property
    def calculate_perimeter(self):
        return (self.height + self.width) * 2
class Square:
    def __init__(self, side):
        self.side = side
    @property
    def area(self):
        return self.side * self.side
    @property
    def perimeter(self):
        return self.side * 4


class Diamond:
    def __init__(self, side, angle):
        self.side = side
        self.angle = angle

    @property
    def area(self):
        return self.side * self.side * math.sin(self.angle)
    @property
    def perimeter(self):
        return self.side * 4

class Cirecle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius * self.radius * 3.14

    @property
    def perimeter(self):
        return 2 *self.radius * 3.14
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    @ property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p-self.a)*(p-self.b)*(p-self.c))*0.5

    @property
    def perimeter(self):
        return self.a + self.b +self.c


pa1 = Parallelogram(2, 5, 70)
pa2 = Parallelogram(5, 6, 115)
rect1 = Rectangle(2, 5)
rect2 = Rectangle(5, 6)
sq1 = Square(9)
sq2 = Square(3)
da1 = Diamond(9, -30)
da2 = Diamond(3, 20)
ci1 = Cirecle(5)
ci2 = Cirecle(11)
tr1 = Triangle(5, 3, 1)


print(pa1.area, pa1.perimeter)
print(pa2.area, pa2.perimeter)
print(rect1.calculate_area, rect1.calculate_perimeter)
print(rect2.calculate_area, rect2.calculate_perimeter)
print(sq1.area, sq1.perimeter)
print(sq2.area, sq2.perimeter)
print(da1.area, da1.perimeter)
print(int(da2.area), da2.perimeter)
print(ci1.area, int(ci1.perimeter))
print(ci2.area, ci2.perimeter)
print(tr1.area, tr1.perimeter)