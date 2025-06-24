from Shape import Shape
import math

class Hexagon(Shape):

    def __init__(self,side):
        if side <= 0:
            raise ValueError("Enter a positive side length")
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2

    def get_perimeter(self):
        return self.side * 6
