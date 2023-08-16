# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, pages, author, price):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.__secret = "This is a secret attribute"

    # instance methods are defined like any other function, with the
    # first argument as the object ("self" is just a convention)
    def set_discount(self, amount):
        self._discount = amount

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price


# create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# print the price of book1
print(b1.get_price())

# try setting the discount
print(b2.get_price())
b2.set_discount(0.25)
print(b2.get_price())

# properties with double underscores are hidden by the interpreter
print(b2._discount)
# print(b2.__secret)
# print(b2._Book__secret)
