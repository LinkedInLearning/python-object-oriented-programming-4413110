# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

#TODO: Import "ABC"(abstract base classes) and abstractmethod from abc

#TODO: Inherit from ABC indicates that this is an abstract base class
class GraphicShape:
    def __init__(self):
        super().__init__()
    # declaring a method as abstract requires a subclass to implement it
    def calcArea(self):
        pass

#TODO: Create specific versions of "calcArea" for different shapes
class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side


g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
