from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Hexagon import Hexagon

class Menu:

    @staticmethod
    def print_menu():
        print("\nChoose a shape to calculate area and perimeter:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Hexagon")
        print("6. Exit")

    @staticmethod
    def handle_choice(choice):
        try:
            if choice == "1":
                side = float(input("Enter the side length: "))
                shape = Square(side)
            elif choice == "2":
                width = float(input("Enter the width: "))
                height = float(input("Enter the height: "))
                shape = Rectangle(width, height)
            elif choice == "3":
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                shape = Triangle(a, b, c)
            elif choice == "4":
                radius = float(input("Enter the radius: "))
                shape = Circle(radius)
            elif choice == "5":
                side = float(input("Enter the side length of the hexagon: "))
                shape = Hexagon(side)
            elif choice == "6":
                return False
            else:
                print("Invalid choice, please try again.")
                return True

            print(repr(shape))
            print(shape)

        except Exception as e:
            print(f"Error: {e}")

        return True