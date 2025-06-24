from Shape import Shape
import math

class Triangle(Shape):

    def __init__(self,base,height):
        if base <= 0 or height <= 0:
            raise ValueError("base and height must be positive numbers")
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2

    def get_perimeter(self):
        half_base = self.base / 2
        side = math.sqrt(half_base ** 2 + self.height ** 2)
        perimeter = self.base + 2 * side
        return perimeter

