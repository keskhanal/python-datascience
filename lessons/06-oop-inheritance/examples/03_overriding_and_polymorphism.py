"""Method overriding and polymorphism."""

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        return f"{self.__class__.__name__} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):                      # overrides Shape.area
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# Polymorphism: the same call works on every shape, each does its own thing.
shapes = [Rectangle(3, 4), Circle(5), Square(2)]
for shape in shapes:
    print(shape.describe())

# Duck typing: Python only cares that the method exists.
class Triangle:                          # not a Shape subclass at all
    def area(self):
        return 6.0
    def describe(self):
        return f"Triangle with area {self.area():.2f}"

for shape in shapes + [Triangle()]:
    print(shape.describe())
