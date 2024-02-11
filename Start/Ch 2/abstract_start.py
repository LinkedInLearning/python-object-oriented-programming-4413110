# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
# We will create a base class that lets users create different kind of 2 deminsional shapes.

# We want to enforce the Circle and Square classes to inherit the calcArea from class GraphicShape.
# We also want to prevent the class GraphicShape itself from being instantiated.

# Import the abc method from the python standard library. The ABC is abstract base methods we import
# along with abstractmethod.
# We inherit abstractmethod from the ABC class for GraphicShape.

from abc import ABC, abstractmethod 
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
# adding the decorator @ with abstractmethod means classes must inherit calcArea.
    @abstractmethod 
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        return self.side * self.side


c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
