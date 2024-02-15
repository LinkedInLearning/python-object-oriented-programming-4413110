# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# TODO: Add abstract class "JSONify" with abstract method "toJSON"

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
        
    # TODO: Override "toJSON" method to return a JSON representation of "calcArea"


c = Circle(10)
print(c.calcArea())
