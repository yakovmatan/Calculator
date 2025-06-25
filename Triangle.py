from Shape import Shape
import math

class Triangle(Shape):

    def __init__(self,a,b,c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive numbers")
        if not self.is_valid_triangle(a,b,c):
            raise ArithmeticError("The sides do not form a valid triangle")
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid_triangle(a,b,c):
        return a + b > c and a + c > b and b + c > a

    def get_area(self):
        semi_p = self.get_perimeter() / 2
        return math.sqrt(semi_p * (semi_p - self.a) * (semi_p - self.b) * (semi_p - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b}, c={self.c})"

