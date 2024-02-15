# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

#TODO: For A and B class create an attribute "name" that will take different values
class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"


class C(A, B):
    def __init__(self):
        super().__init__()
    #TODO: Create the method "showprops" returning the attributes it owns

c = C()
#TODO: You can use showprops() and also call "Class.__mro__" to find out all the parent classes
