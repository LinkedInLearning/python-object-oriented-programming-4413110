# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized. 
    # We will add more functions to the init method since books have more than just a title.
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties each one of these attributes is called an instance attribute
        # because the value that it holds is only used by the instance of the object that it is declared on.
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy",1225,39.95)
b2 = Book("The Catcher in the Rye","JD Saliger",234,29.95)

# TODO: print the price of book1
print(b1.getprice())


# TODO: try setting the discount
#print(b2.getprice())
#b2.setdiscount(0.25)
#print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2.__secret)