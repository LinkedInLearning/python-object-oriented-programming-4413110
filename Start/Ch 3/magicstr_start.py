# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

# The str function is used to provide a user-friendly string description of the object and is
# usually intended to be displayed to the user.

# The repr function is used to generate a more developer facing string that ideally can be
# used to recreate the object in its current state. It's also commonly used for debugging purposes.
# It gets used a lot to display detailed information.

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: use the __repr__ method to return an obj representation
    def __repr__(self):
        return f"title={self.title},author{self.author},price={self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))