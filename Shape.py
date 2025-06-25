from abc import ABC,abstractmethod
from functools import total_ordering


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

