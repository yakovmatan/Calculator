from abc import ABC,abstractmethod
from functools import total_ordering
from os import replace


@total_ordering
class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} - area: {self.get_area():.2f} perimeter: {self.get_perimeter():.2f}"

    def __repr__(self):
        return f"<{self.__class__.__name__} object>"

    def __eq__(self, other):
        if not isinstance(other,Shape):
            return False
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        if not isinstance(other,Shape):
            return NotImplemented
        return self.get_area() < other.get_area()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.get_area() * other
        elif isinstance(other, Shape):
            return self.get_area() * other.get_area()
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
