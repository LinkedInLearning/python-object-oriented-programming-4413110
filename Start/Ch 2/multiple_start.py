# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"


# Class C is our class that will inherit from the base classes A and B. 
# It does this by separating them with a comma within parenthesis.
class C(A, B):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)


c = C()
print(C.__mro__)
c.showprops()