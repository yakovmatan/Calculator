from Shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self.radius})"

