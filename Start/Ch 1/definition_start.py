# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, title) -> None:
        self.title = title

# TODO: create instances of the class
book1 = Book("Brave New World")
book2 = Book("War and peace")

# TODO: print the class and property
print(book1)
print(book1.title)
