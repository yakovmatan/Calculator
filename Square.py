from Rectangle import Rectangle

class Square(Rectangle):

    def __init__(self,side):
        if side <= 0:
            raise ValueError("Enter a positive side length")
        super().__init__(side,side)

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.width})"