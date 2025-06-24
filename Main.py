from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Hexagon import Hexagon

shapes = [Rectangle(3,4), Square(2), Triangle(5,7), Circle(3), Hexagon(3)]

for shape in shapes:
    print(repr(shape))
    print(shape)
