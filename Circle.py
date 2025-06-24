import Shape
import math


class Circle(Shape):

    def __int__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radio = radius

    def get_area(self):
        return math.pi * self.radio ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radio
