import Shape

class Triangle(Shape):

    def __init__(self,base,height):
        if base < 1 or height < 1:
            raise ValueError("base and height must be positive numbers")
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2
