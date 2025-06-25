from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Hexagon import Hexagon

shapes = [Rectangle(3,4), Square(2), Triangle(5,7,3), Circle(3), Hexagon(3)]

for shape in shapes:
    print(repr(shape))
    print(shape)

print("=== Comparisons ===")
base_shape = shapes[0]
for other in shapes[1:]:
    print(f"{repr(base_shape)} == {repr(other)}?  {base_shape == other}")
    print(f"{repr(base_shape)} < {repr(other)}?  {base_shape < other}")
    print(f"{repr(base_shape)} > {repr(other)}?  {base_shape > other}")
    print()

print("=== Multiplication of areas ===")
for i in range(len(shapes)):
    for j in range(i + 1, len(shapes)):
        s1 = shapes[i]
        s2 = shapes[j]
        product = s1 * s2
        print(f"{repr(s1)} * {repr(s2)} = {product:.2f}")

print()

print("=== Multiplication with shapes and numbers ===")
shape = Square(4)
factor = 3
print(f"{repr(shape)} * {factor} = {shape * factor:.2f}")
print(f"{factor} * {repr(shape)} = {factor * shape:.2f}")
